from keras.models import Sequential
from keras.layers import Conv2D,AveragePooling2D,MaxPooling2D,ZeroPadding2D
from keras.layers import Dropout,Activation,BatchNormalization
from keras.layers import Dense,Flatten

#Visual Geometry Group Network
class VGGnet:
    def __init__(self,Input_Shape,kinds):
        self.Input_Shape = Input_Shape
        self.kinds = kinds

    def VGG(self):
        model = Sequential()

        # model.add(ZeroPadding2D((1,1),input_shape = self.Input_Shape))
        # model.add(Conv2D(32,(3,3),activation = 'relu'))
        # model.add(BatchNormalization())
        # model.add(AveragePooling2D(2,2))
        # model.add(MaxPooling2D(3,3))

        #Flatten -> Dense
        # model.add(Flatten())
        model.add(Flatten(input_shape=self.Input_Shape))
        model.add(Dense(256,activation = 'relu'))
        # model.add(Dropout(0.4))
        model.add(Dense(128,activation = 'relu'))
        # model.add(Dropout(0.3))
        model.add(Dense(32,activation = 'relu'))
        # model.add(Dropout(0.2))
        model.add(Dense(32,activation = 'relu'))
        if self.kinds == 2:
            model.add(Dense(self.kinds,activation = 'sigmod'))
        elif self.kinds > 2:
            model.add(Dense(self.kinds,activation = 'softmax'))
        else:
            return 'Too few species to identify'

        return model


