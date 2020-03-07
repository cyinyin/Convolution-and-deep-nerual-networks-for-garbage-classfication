from keras.models import load_model
from keras.preprocessing import image
from graduation_project.photo_resize import Photo_Deal_Method
import numpy as np


def pre_photo(width = 150,height = 150,open_path_2 = None,open_path_3 = None,model_path = None):
#open_path2:validation image path  open_path3:test image path  model_path:model file path
    from graduation_project.recognition import save_path

    if model_path == None:
        processing = Photo_Deal_Method()
        save_path_1 = processing.Path_Judge('E:\python_workspace\graduation_project\program\FC3')
        model_path = save_path_1 + r'\train_model.h5'
    else:
        model_path = model_path

    model = load_model(model_path)

    test_datagen = image.ImageDataGenerator(
        rescale=1. / 255,
    )

    if open_path_2 == None:
        open_path_2 = save_path + r'\validation'
    else:
        open_path_2 = open_path_2
    
    validation_generator = test_datagen.flow_from_directory(
        open_path_2,
        target_size=(width, height),
        class_mode='categorical',
    )

    predict_photo = image.ImageDataGenerator(
        rescale = 1./255,
    )

    if open_path_3 == None:
        open_path_3 = save_path + r'\final_test'
    else:
        open_path_3 = open_path_3
        print(open_path_3)
    predict_generator = predict_photo.flow_from_directory(
        open_path_3,
        target_size = (width,height),
        shuffle = False,
        batch_size = 1,

    )
    # predict_generator.reset()

    value = model.predict_generator(
        predict_generator,
    )

    predict_class_indices = np.argmax(value,axis = 1)

    #Generate predict tags
    labels = validation_generator.class_indices
    label = dict((v,k) for k,v in labels.items())

    predictions = [label[i] for i in predict_class_indices]

    filenames = predict_generator.filenames

    # print('\t\ttitle','\t\t\t\tpretict','\t\t\tprobility')
    # for idx in range(len(filenames)):
    #     print(filenames[idx],'\t\t',predictions[idx],'\t\t\t\t',np.max(value,axis = 1)[idx])

    #return images' filename,prediction family,probability
    return filenames,predictions,np.max(value,axis = 1),model

if __name__ == '__main__':
    m = pre_photo(150,150,r'E:\python_workspace\graduation_project\image_data\validation',
                r'E:\python_workspace\graduation_project\trash',
                r'E:\python_workspace\graduation_project\program\FC4\train_model.h5')

# import tensorflow as tf
# import os
#
# os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
#
# a = tf.constant(1.)
# b = tf.constant(2.)
# print(a+b)
#
# print('GPU:', tf.test.is_gpu_available())
