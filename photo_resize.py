from PIL import Image
import os
import shutil
#处理文件
class Photo_Deal_Method:

    size = (150,150)
    open_path = r'E:\Photo_Deal_Method\imageset'
    save_path = r'E:\Photo_Deal_Method\image_data'

    #the path whether exists by judging.
    '''
    return the save_path when the path have been existed ,or else return the save_path after creating it.
    '''
    def Path_Judge(self,save_path):
        if os.path.exists(save_path):
            return save_path
        else:
            try:
                'mkdir:create the last layer folder'
                os.mkdir(save_path)
                return save_path
            except:
                try:
                    '''makedirs: create a multi-tier folder,from the top-level root directory
                                  to the bottom subdirectory
                    '''
                    os.makedirs(save_path)
                    return save_path
                except:
                    return 'fail to creat files'


    def Del_Photo(self,del_path = None):
        if os.path.exists(del_path) :
            shutil.rmtree(del_path)
            print('Successful,folder deleted')
        else:
            print('Failed,floder does not exist')


    #training image preprocessing
    def Train_Photo(self,size = size,save_path = save_path + r'\train',train_open_path = open_path):

        for path in os.listdir(train_open_path):
            i = 0
            modify_path = os.path.join(train_open_path,path)
            for image in os.listdir(modify_path):
                img = Image.open(os.path.join(modify_path,image)).convert('RGB')
                #对图片进行原样复制，在进行其他操作
                img = img.copy()
                img1 = img.resize(size,Image.ANTIALIAS)
                i += 1
                if 0 < i < 10:
                    img1.save(os.path.join(self.Path_Judge(os.path.join(save_path, path)),str(path) + '_00' + str(i) +'.png'),quality = 95)
                elif 10 <= i < 100:
                    img1.save(os.path.join(self.Path_Judge(os.path.join(save_path, path)),str(path) + '_0' + str(i) +'.png'),quality = 95)
                else:
                    img1.save(os.path.join(self.Path_Judge(os.path.join(save_path, path)),str(path) + '_' + str(i) +'.png'),quality = 95)
        return 'images that to train the model have been changed'

    #validation image preprocessing
    def Validation_Photo(self,size = size,save_path = save_path + r'\validation',validation_open_path = open_path):
        for path in os.listdir(validation_open_path):
            i = 0
            modify_path = os.path.join(validation_open_path,path)
            for img in os.listdir(modify_path):
                img = Image.open(os.path.join(modify_path,img)).convert('RGB')
                img = img.copy()
                img1 = img.resize(size,Image.ANTIALIAS)
                #ANTIALIAS：平滑滤波。这是PIL 1.1.3版本中新的滤波器。对所有可以影响输出像素的输入像素进行高质量的重采样滤波，以计算输出像素值。
                #在当前的PIL版本中，这个滤波器只用于改变尺寸和缩略图方法。
                #注意：在当前的PIL版本中，ANTIALIAS滤波器是下采样（例如，将一个大的图像转换为小图）时唯一正确的滤波器
                i += 1
                if 0 < i < 10:
                    img1.save(os.path.join(self.Path_Judge(os.path.join(save_path,path)),str(path) + '_00'  + str(i) + '.png'),quality = 95)
                elif 10 <= i <100:
                    img1.save(os.path.join(self.Path_Judge(os.path.join(save_path,path)),str(path) + '_0'  + str(i) + '.png'),quality = 95)
                else:
                    img1.save(os.path.join(self.Path_Judge(os.path.join(save_path,path)),str(path) + '_'  + str(i) + '.png'),quality = 95)
        return 'images that to validathe model have been changed'

    #test image preprocessing
    def Test_Photo(self,size = size,save_path = save_path + r'\final_test',test_open_path = open_path):
        i = 0
        for img in os.listdir(test_open_path):
            # modify_path = os.path.join(test_open_path,path)
            # for img in os.listdir(modify_path):
            img = Image.open(os.path.join(test_open_path,img)).convert('RGB')
            img = img.copy()
            img1 = img.resize(size,Image.ANTIALIAS)
            #使用不同的名字,使用同名会产生二义性
            i += 1
            if  0< i < 10:
                img1.save(self.Path_Judge(save_path)+ '\\trash' + '_00' + str(i) + '.png',quality = 95)
            elif 10 <= i <100:
                img1.save(self.Path_Judge(save_path)+ '\\trash' + '_0' + str(i) + '.png',quality = 95)
            else:
                img1.save(self.Path_Judge(save_path)+ '\\trash' + '_' + str(i) + '.png',quality = 95)
        return 'images that to test the model have been changed'

if __name__ == '__main__':
    # P =Photo_Deal_Method()
    open_path ='E:\python_workspace\graduation_project'
    save_path = 'E:\python_workspace\graduation_project\image_data'
    Photo_Processing = Photo_Deal_Method()
    Photo_Processing.Train_Photo((150,150), save_path + r'\train', open_path + r'\dataset-train')
    Photo_Processing.Validation_Photo((150, 150), save_path + r'\validation', open_path + r'\dataset-test')
    # P.Test_Photo((150, 150), save_path + r'\final_test', open_path + r'\trash')

