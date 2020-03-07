from graduation_project.photo_resize import Photo_Deal_Method
from graduation_project.simple_vggnet import VGGnet
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import TensorBoard
from keras.optimizers import Adam,SGD
import os
from matplotlib import pyplot as plt


#the path of training images(default select)
open_path ='E:\python_workspace\graduation_project'
save_path = 'E:\python_workspace\graduation_project\image_data'
# width = 150
# height = 150

#width,height:the size of photo
def rec_photo(width = 150,height = 150,
              open_path_1 = '',save_path_1 = '',
              open_path_2 = '',save_path_2 = '',
              optimizer = '',batch_size = '',epoche = '',save_tensorboard = '',
              save_model = '',save_model_weight = '',save_model_structure = ''):
    #open_path_1:train image path  open_path_2:validation image path
    #save_tebsirboard:the save-path that nerual network structure and traing-accuracy and loss's image
    #save_model:the save-path of model   save_weight:the save-path of model-weight
    #save_model_structure:the save-path of model structure

    #instantiation of Photo_Deal_Method
    Photo_Processing = Photo_Deal_Method()

    #processing train image
    if open_path_1 == '':
        open_path_1 = Photo_Processing.Path_Judge(open_path + r'\dataset-train')
    else:
        open_path_1 = open_path_1

    if save_path_1 == '':
        save_path_1 = Photo_Processing.Path_Judge(save_path + r'\train')
    else:
        save_path_1 = Photo_Processing.Path_Judge(save_path_1 + r'\train')
    Photo_Processing.Train_Photo((width,height),save_path_1,open_path_1)

    #processing validation image
    if open_path_2 == '':
        open_path_2 = Photo_Processing.Path_Judge(open_path + r'\dataset-validation')
    else:
        open_path_2 = open_path_2
    if save_path_2 == '':
        save_path_2 = Photo_Processing.Path_Judge(save_path + r'\validation')
    else:
        save_path_2 = save_path_2 + r'\validation'
    Photo_Processing.Train_Photo((width,height),save_path_2,open_path_2)

    # Input_Size = (width,height,3)
    if open_path_1 == '':
        model = VGGnet((width,height,3),len(os.listdir(open_path_1))).VGG()
    else:
        model = VGGnet((width,height,3),len(os.listdir(open_path_1))).VGG()


    if optimizer == '':
        optimizer = 'sgd'
    else:
        optimizer = str(optimizer)

    if len(os.listdir(open_path_1)) == 2:
        loss = 'binary_crossentropy'
        class_mode = 'binary'
    elif len(os.listdir(open_path_1)) > 2:
        loss = 'categorical_crossentropy'
        class_mode = 'categorical'
    else:
        return 'Too few species to identify'

    #model compile
    model.compile(optimizer= optimizer, loss= loss, metrics=['accuracy'])

    # if optimizer == '':
    #     model.compile(optimizer = 'sgd',loss = 'categorical_crossentropy',metrics = ['accuracy'])
    # else:
    #     model.compile(optimizer = str(optimizer),loss = 'categorical_crossentropy',metrics = ['accuracy'])

    #imagedata enhance
    train_datagen = ImageDataGenerator(
        rotation_range = 30,
        width_shift_range = 0.2,
        height_shift_range = 0.2,
        rescale = 1./255,
        # shear_range = 0.2,
        # vertical_flip = True,
        # horizontal_flip = True,
    )

    test_datagen = ImageDataGenerator(
        rescale = 1./255,
    )

    if batch_size is '':
        batch_size = 32
    else:
        batch_size = int(batch_size)

    if save_path_1 == '':
        save_path_1 = save_path + r'\train'
    else:
        save_path_1 = save_path_1
    #generate the data and label from images
    train_generator = train_datagen.flow_from_directory(
        save_path_1,
        target_size = (width,height),
        batch_size = batch_size,
        class_mode = class_mode,
    )

    if save_path_2 == '':
        save_path_2 = save_path + r'\validation'
    else:
        save_path_2 = save_path_2

    validation_generator = test_datagen.flow_from_directory(
        save_path_2,
        target_size = (width,height),
        batch_size = batch_size,
        class_mode = class_mode,
    )


    #time stamp
    import time
    time = time.strftime("%Y%m%d%H%M%S",time.localtime())
    if save_tensorboard == '':
        save_tensorboard = Photo_Processing.Path_Judge('E:\python_workspace\graduation_project\models') + '\log_%s'%(time)
    else:
        save_tensorboard = save_tensorboard + '\\log_%s'%(time)

    tensorboard = TensorBoard(log_dir = save_tensorboard,histogram_freq = 1,write_graph = True)

    if epoche is '':
        epoche = 100
    else:
        epoche = int(epoche)

    m = model.fit_generator(
        train_generator,
        steps_per_epoch = 100,
        epochs = epoche,
        validation_data = validation_generator,
        validation_steps = 30,
        callbacks = [tensorboard,],
    )

    epochs = range(len(m.history['accuracy']))
    plt.figure()
    plt.plot(epochs,m.history['loss'],'b*-',label = 'Train_loss')
    plt.plot(epochs,m.history['val_loss'],'r+-',label = 'Val_loss')
    plt.plot(epochs,m.history['accuracy'],'o-g',label = 'Train_accuracy')
    plt.plot(epochs,m.history['val_accuracy'],'purple',label = 'Val_accuracy')
    plt.title('Train and Validation accuracy')
    plt.legend()
    plt.show()

    #save the model
    if save_model == '':
        save_model = Photo_Processing.Path_Judge('E:\python_workspace\graduation_project\models') + r'\train_model.h5'
    else:
        save_model = save_model + r'\train_model.h5'
    model.save(save_model)
    #save the weights
    if save_model_weight == '':
        save_model_weight = Photo_Processing.Path_Judge('E:\python_workspace\graduation_project\models') + r'\train_model_weight.h5'
    else:
        save_model_weight = save_model_weight + r'\train_model_weight.h5'
    model.save_weights(save_model_weight)
    # #save the structure
    Json_String = model.to_json()
    if save_model_structure == '':
        save_model_structure = Photo_Processing.Path_Judge('E:\python_workspace\graduation_project\models') + r'\model_to_json.json'
    else:
        save_model_structure = save_model_structure + r'\model_to_json.json'
    open(save_model_structure,'w').write(Json_String)

    #delete the image of training
    print('model保存成功')


if __name__ == "__main__":
    parameters = ['E:/python_workspace/graduation_project/dataset-train', 'E:/python_workspace/graduation_project/image_data', 'E:/python_workspace/graduation_project/dataset-validation', 'E:/python_workspace/graduation_project/image_data', 'sgd', '16', '10', 'E:/python_workspace/graduation_project/models', 'E:/python_workspace/graduation_project/models', 'E:/python_workspace/graduation_project/models', 'E:/python_workspace/graduation_project/models']
    path = []
    for item in parameters:
        path.append(item.replace('/','\\'))
    rec_photo(150,150,
              open_path_1=path[0],save_path_1=path[1], open_path_2=path[2],save_path_2=path[3],
              optimizer=path[4], batch_size=path[5], epoche=path[6],
              save_tensorboard=path[7], save_model=path[8],
              save_model_weight=path[9], save_model_structure=path[10])
