import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QHBoxLayout,QVBoxLayout,QLabel,QWidget
from PyQt5.QtWidgets import QPushButton,QMessageBox,QLineEdit,QFileDialog,QRadioButton,QLCDNumber,QSlider
from PyQt5.QtGui import QIcon,QPixmap,QPalette,QBrush,QFont
from graduation_project.predict import pre_photo
from graduation_project.recognition import rec_photo
import os

#Start interface
class FirstPage(QMainWindow):

    def __init__(self,width = 1000,height = 600):
        super().__init__()
        self.setFixedSize(width, height)
        self.initUI()
        self.button()
        self.startButton.clicked.connect(self.message)

    #initialize window background image and icon
    def initUI(self):
        #setting Window icon
        self.setWindowIcon(QIcon('icon.png'))

        self.setWindowTitle('Start Interface')

        #setting background image
        palettel = QPalette()
        pix = QPixmap('sky.jpg')
        pix = pix.scaled(self.width(),self.height())
        palettel.setBrush(QPalette.Background,QBrush(pix))
        self.setPalette(palettel)

    #start up button
    def button(self):
        widget = QWidget()
        self.setCentralWidget(widget)
        self.startButton = QPushButton('START',self)
        font = QFont('宋体',35)
        font.setItalic(True)
        self.startButton.setFont(font)
        self.startButton.setFixedSize(150,50)
        self.buttonLayout(self.startButton,widget)

    #Ok button position
    def buttonLayout(self,button,widget):
        hbox = QVBoxLayout()
        hbox.addWidget(button)
        vbox = QHBoxLayout()
        vbox.addLayout(hbox)
        widget.setLayout(vbox)

    windowList = []
    def on_pushButton_clicked_1(self):
        the_window = SecondPage_1()
        self.windowList.append(the_window)
        self.close()
        the_window.show()

    windowList = []
    def on_pushButton_clicked_2(self):

        the_window = SecondPage_2()
        self.windowList.append(the_window)
        self.close()
        the_window.show()

    #ask if there is a model file
    def message(self):
        button = QMessageBox.question(self,'choose model',
                                     "If there is a model file",
                                     QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if button ==QMessageBox.Yes:
            self.on_pushButton_clicked_1()
        else:
            self.on_pushButton_clicked_2()

#Image Prediction
class SecondPage_1(QMainWindow):

    def __init__(self,width = 1000, height = 600):
        super().__init__()
        self.setFixedSize(width,height)
        self.initUI()
        #图片的位置
        self.number = 0
        self.text_button_layout_1()
        self.Path = []

    #SecondPage start
    def initUI(self):
        # setting WindowIcon
        self.setWindowIcon(QIcon('icon.png'))

        self.setWindowTitle('Image Prediction')

        # setting the background image
        palette = QPalette()
        pix = QPixmap('sky.jpg')
        pix = pix.scaled(self.width(),self.height())
        palette.setBrush(QPalette.Background,QBrush(pix))
        self.setPalette(palette)

    def back_button(self):
        self.backButton = QPushButton("Previous",self)
        font = QFont('宋体',25)
        font.setItalic(True)
        font.setBold(True)
        self.backButton.setFont(font)
        self.backButton.setFixedSize(150,50)
        self.backButton.clicked.connect(self.close_message)
        return self.backButton

    windowList = []
    def closeWin_1(self):
        the_window = FirstPage()
        self.windowList.append(the_window)
        self.close()
        the_window.show()
        self.windowList = []

    def closeWin_2(self):
        the_window =SecondPage_2()
        self.windowList.append(the_window)
        self.close()
        the_window.show()

    def close_message(self):
        close_button = QMessageBox.question(self,'return','Are you sure to return to the homepage?',
                                            QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        if close_button == QMessageBox.Yes:
            self.closeWin_1()
        else:
            self.closeWin_2()

    def buttonDialog(self,type = 'file'):
        self.choose_button = QPushButton('choose folder',self)
        font = QFont('Microsoft YaHei UI',10)
        font.setItalic(True)
        font.setBold(True)
        self.choose_button.setFont(font)
        self.choose_button.setFixedSize(110,30)
        if type == 'folder':
            self.choose_button.clicked.connect(self.showFolder)
        elif type == 'file':
            self.choose_button.clicked.connect(self.showFile)
        return self.choose_button

    def go_on_button(self,num = None):
        self.go = QPushButton('go>>',self)
        font = QFont('宋体',25)
        font.setItalic(True)
        font.setBold(True)
        self.go.setFont(font)
        self.go.setFixedSize(150,50)
        if num == 1:
            self.go.clicked.connect(self.text_button_layout_2)
        else:
            self.go.clicked.connect(self.text_button_layout_3)
        return self.go

    def set_font(self,object):
        font = QFont('宋体',10)
        font.setItalic(True)
        object.setFont(font)

    Path = []
    def showFolder(self):
        fname = QFileDialog.getExistingDirectory(None,'choose folder',r'C:\Users\DELL\.keras\models')
        self.text_edit.setText(fname)
        if self.text_edit.text() == '':
            self.Path.append(None)
        else:
            self.Path.append(fname)
        # print(self.Path)

    def showFile(self):
        fname = QFileDialog.getOpenFileName(None,'choose file',r'C:\Users\DELL\.keras\models','All files(*.h5)')
        self.text_edit.setText(fname[0])
        if self.text_edit.text() == '':
            self.Path.append(None)
        else:
            self.Path.append(fname[0])
        # print(self.Path)

    def text(self,title = None):
        self.text_edit = QLineEdit(self)
        self.text_edit.setFixedSize(600,30)
        self.text_edit.setPlaceholderText(title)
        self.set_font(self.text_edit)
        return self.text_edit

    def text_button_layout(self,text_box,buttonDialog,back_button,go_on_button,):
        widget = QWidget()
        self.setCentralWidget(widget)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(text_box)
        hbox1.addWidget(buttonDialog)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(back_button)
        hbox2.addWidget(go_on_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)

        widget.setLayout(vbox)

    def text_button_layout_1(self):
        QApplication.processEvents()
        self.text_button_layout(self.text('choose validation image path'),self.buttonDialog('folder'),
                                self.back_button(),self.go_on_button(1))

    def text_button_layout_2(self):
        QApplication.processEvents()
        self.text_button_layout(self.text('choose text iamge path'),self.buttonDialog('folder'),
                                self.back_button(),self.go_on_button())

    def text_button_layout_3(self):
        QApplication.processEvents()
        self.text_button_layout(self.text('select model file(.h5)'),self.buttonDialog('file'),
                                self.back_button(),self.Third_button_predict())


    def Third_button_predict(self):
        predict = QPushButton('Predict',self)
        predict.setFixedSize(150,50)
        font = QFont('宋体',25)
        font.setItalic(True)
        font.setBold(True)
        predict.setFont(font)
        predict.clicked.connect(self.predict_result)
        #在此处关联预测函数
        return predict

    def predict_result(self):
        self.result = pre_photo(150,150,self.Path[0],self.Path[1],self.Path[2])
        QApplication.processEvents()
        self.Firth_layout(self.FirthPage_button()[0],self.FirthPage_button()[1],self.name_kind_probability()[0],
                          self.name_kind_probability()[1],self.name_kind_probability()[2],self.Firth_show_imagewindow())

    #FirthPage Start
    def FirthPage_button(self):
        self.button_left = QPushButton('<==',self)
        self.button_right = QPushButton('==>',self)
        self.button_left.setFixedSize(60,50)
        self.button_right.setFixedSize(60,50)
        #seting image <==,==>
        self.button_left.clicked.connect(self.left_button)
        self.button_right.clicked.connect(self.right_button)
        return self.button_left,self.button_right

    def left_button(self):
        if self.button_left.text() == '<==' and self.number > 0:
            self.number -= 1
            pixmap = self.Firth_show_imagewindow(os.path.join(self.Path[1],(self.result[0])[self.number]))
            name,kind,probability = self.name_kind_probability((self.result[0])[self.number],
                                                               (self.result[1])[self.number],(self.result[2])[self.number])
            self.Firth_layout(self.button_left,self.button_right,name,kind,probability,pixmap)

    def right_button(self):
        if self.button_right.text() == '==>' and self.number < len(self.result[0]):
            self.number += 1
            pixmap = self.Firth_show_imagewindow(os.path.join(self.Path[1],(self.result[0])[self.number]))
            name,kind,probability= self.name_kind_probability((self.result[0])[self.number],
                                                              (self.result[1])[self.number],(self.result[2])[self.number])
            self.Firth_layout(self.button_left,self.button_right,name,kind,probability,pixmap)

    #show prediction image
    def Firth_show_imagewindow(self,path = None):
        label = QLabel()
        label.setMaximumSize(380,380)
        if path == None:
            pix = QPixmap(os.path.join(self.Path[1],(self.result[0])[0]))
        else:
            pix = QPixmap(path)
        label.setPixmap(pix)
        label.setVisible(True)
        label.setStyleSheet('border:1px solid black')
        return label

    #show prediction image name or probability
    def Firth_show_image_text(self,context = None):
        self.text = QLineEdit(self)
        self.text.setFixedSize(140,50)
        self.text.setPlaceholderText(context)
        self.set_font(self.text)
        self.text.setReadOnly(True)
        return self.text

    def name_kind_probability(self,name_content = None,kind_content = None,probability_content =None):
        name = self.Firth_show_image_text('image name')
        if name_content == None:
            name.setText((self.result[0])[0])
        else:
            name.setText(name_content)
        kind = self.Firth_show_image_text('kind')
        if kind_content == None:
            kind.setText((self.result[1])[0])
        else:
            kind.setText(kind_content)
        probability = self.Firth_show_image_text('prediction')
        if probability_content == None:
            probability.setText(str((self.result[2])[0]))
        else:
            probability.setText(str(probability_content))
        return name,kind,probability

    def Firth_layout(self,left_button=None,right_button=None,name = None,kind =None,probability = None,pixmap = None):
        widget = QWidget()
        self.setCentralWidget(widget)
        hbox1 = QHBoxLayout()
        hbox1.addWidget(left_button)
        hbox1.addWidget(right_button)

        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addWidget(name)
        vbox.addStretch(1)
        vbox.addWidget(kind)
        vbox.addStretch(1)
        vbox.addWidget(probability)
        vbox.addStretch(2)

        hbox = QHBoxLayout()
        hbox.addWidget(pixmap)
        hbox.addLayout(vbox)
        widget.setLayout(hbox)

    #close event
    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message','Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

#Training Nerual Network
class SecondPage_2(QMainWindow):

    def __init__(self,width = 1000,height = 600):
        super().__init__()
        self.setFixedSize(width, height)
        self.initUI()
        self.first_layout()
        self.Path_parameter = []

    def initUI(self):
        # setting WindowIcon
        self.setWindowIcon(QIcon('icon.png'))

        self.setWindowTitle('Training Nerual Network')

        # setting the background image
        palette = QPalette()
        pix = QPixmap('sky.jpg')
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)

    def back_button(self):
        backButton = QPushButton("Previous", self)
        font = QFont('宋体', 25)
        font.setItalic(True)
        font.setBold(True)
        backButton.setFont(font)
        backButton.setFixedSize(150, 50)
        backButton.clicked.connect(self.closeWin)
        return backButton

    def go_on_button(self,num = None):
        go = QPushButton('go>>')
        font = QFont('宋体',25)
        font.setItalic(True)
        font.setBold(True)
        go.setFont(font)
        go.setFixedSize(150,50)
        if num == 1:
            go.clicked.connect(self.second_layout)
        elif num == 2:
            go.clicked.connect(self.third_layout)
        elif num == 3:
            go.clicked.connect(self.firth_layout)
        elif num ==4:
            go.clicked.connect(self.fifth_layout)
        elif num == 5:
            go.clicked.connect(self.fifth_layout_1)
        elif num == 6:
            go.clicked.connect(self.fifth_layout_2)
        elif num ==7:
            go.clicked.connect(self.sixth_layout)
        elif num == 8:
            go.clicked.connect(self.seventh_layout)
        elif num == 9:
            go.clicked.connect(self.eighth_layout)
        else:
            go.clicked.connect(self.ninth_layout)
        return go

    windowList = []
    def closeWin(self):
        the_window = FirstPage()
        self.windowList.append(the_window)
        self.close()
        the_window.show()
        self.windowList = []

    def set_font(self,object):
        font = QFont('Microsoft YaHei UI',10)
        font.setItalic(True)
        object.setFont(font)

    #text box
    def text_lineEdit(self,content = None):
        self.text = QLineEdit()
        self.text.setFixedSize(600,30)
        self.text.setPlaceholderText(content)
        self.set_font(self.text)
        return self.text

    Path_parameter = []
    def show_folder(self):
        fname = QFileDialog.getExistingDirectory(None,'choose folder',r'C:\Users\DELL\.keras\models')
        self.text.setText(fname)
        if self.text.text() == '':
            self.Path_parameter.append('')
        else:
            self.Path_parameter.append(fname)
        print(self.Path_parameter)

    def buttonDialog(self,content):
        self.button_dialog = QPushButton(content,self)
        self.button_dialog.setFixedSize(110,30)
        self.button_dialog.clicked.connect(self.show_folder)
        font = QFont('Microsoft YaHei UI',10)
        font.setBold(True)
        font.setItalic(True)
        self.button_dialog.setFont(font)
        return self.button_dialog

    #first page layout
    def text_button_Layout(self,text_lineEdit = None,buttonDialog = None,back_button = None,go_on_button = None):
        widget = QWidget()
        self.setCentralWidget(widget)
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(text_lineEdit)
        hbox1.addWidget(buttonDialog)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(back_button)
        hbox2.addWidget(go_on_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)
        widget.setLayout(vbox)

    def first_layout(self):
        self.text_button_Layout(self.text_lineEdit('select unprocessed training images folder'),
                                self.buttonDialog('choose folder'),self.back_button(),self.go_on_button(1))

    def second_layout(self):
        QApplication.processEvents()
        self.text_button_Layout(self.text_lineEdit('save processed training images'),
                                self.buttonDialog('choose folder'),self.back_button(),self.go_on_button(2))

    def third_layout(self):
        QApplication.processEvents()
        self.text_button_Layout(self.text_lineEdit('select unprocessed validation images folder'),
                                self.buttonDialog('choose folder'),self.back_button(),self.go_on_button(3))

    def firth_layout(self):
        QApplication.processEvents()
        self.text_button_Layout(self.text_lineEdit('save processed validation images'),
                                self.buttonDialog('choose floder'),self.back_button(),self.go_on_button(4))

    def radio_Button(self,content = None):
        r_button = QRadioButton(content,self)
        font = QFont('Microsoft YaHei UI',20)
        font.setBold(True)
        font.setItalic(True)
        r_button.setFont(font)
        # if bool == True:
        #     r_button.setChecked(True)
        # else:
        #     r_button.setChecked(False)
        r_button.clicked.connect(lambda : self.btnstate(r_button))
        return r_button

    def btnstate(self,button):

        if button.text() == 'sgd':
            if button.isChecked() == True:
                self.Path_parameter.append('sgd')
                print(self.Path_parameter)
        elif button.text() == 'rsmprop':
            if button.isChecked() == True:
                self.Path_parameter.append('rsmprop')
                print(self.Path_parameter)
        elif button.text() == 'adam':
            if button.isChecked() == True:
                self.Path_parameter.append('adam')
                print(self.Path_parameter)
        elif button.text() == '8':
            if button.isChecked() == True:
                self.Path_parameter.append('8')
                print(self.Path_parameter)
        elif button.text() == '16':
            if button.isChecked() == True:
                self.Path_parameter.append('16')
                print(self.Path_parameter)
        elif button.text() ==  '32':
            if button.isChecked() == True:
                self.Path_parameter.append('32')
                print(self.Path_parameter)

    def label_rbutton(self,content):
        label = QLabel(content)
        font = QFont('Microsoft YaHei UI',20)
        font.setBold(True)
        font.setItalic(True)
        label.setFont(font)
        return label

    def epoches(self):
        self.text =  QLineEdit()
        self.text.setPlaceholderText('Recommended 100~200')
        self.text.setFixedSize(150,30)
        self.text.editingFinished.connect(self.get_epoches)
        return self.text

    def get_epoches(self):
        if self.text.text() != '':
            self.Path_parameter.append(self.text.text())
        else:
            self.Path_parameter.append('')
        print(self.Path_parameter)

    def fifth_layout(self):
        QApplication.processEvents()
        widget = QWidget()
        self.setCentralWidget(widget)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.label_rbutton('optimizer:'))
        hbox1.addWidget(self.radio_Button('sgd'))
        hbox1.addStretch(1)
        hbox1.addWidget(self.radio_Button('rsmprop'))
        hbox1.addStretch(1)
        hbox1.addWidget(self.radio_Button('adam'))
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.back_button())
        hbox2.addWidget(self.go_on_button(5))

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)

        widget.setLayout(vbox)

    def fifth_layout_1(self):
        QApplication.processEvents()
        widget = QWidget()
        self.setCentralWidget(widget)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.label_rbutton('batch-size:'))
        hbox1.addWidget(self.radio_Button('8'))
        hbox1.addStretch(1)
        hbox1.addWidget(self.radio_Button('16'))
        hbox1.addStretch(1)
        hbox1.addWidget(self.radio_Button('32'))
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.back_button())
        hbox2.addWidget(self.go_on_button(6))

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)

        widget.setLayout(vbox)

    def fifth_layout_2(self):
        QApplication.processEvents()
        widget = QWidget()
        self.setCentralWidget(widget)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.label_rbutton('epoches:'))
        hbox1.addWidget(self.epoches())
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.back_button())
        hbox2.addWidget(self.go_on_button(7))

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)

        widget.setLayout(vbox)

    def sixth_layout(self):
        QApplication.processEvents()
        self.text_button_Layout(self.text_lineEdit('select the folder to save tensorboard file'),
                                self.buttonDialog('choose folder'),self.back_button(),self.go_on_button(8))

    def seventh_layout(self):
        QApplication.processEvents()
        self.text_button_Layout(self.text_lineEdit('select the folder to save model file'),
                                self.buttonDialog('choose folder'),self.back_button(),self.go_on_button(9))

    def eighth_layout(self):
        QApplication.processEvents()
        self.text_button_Layout(self.text_lineEdit('selct the folder to save model-weight file'),
                                self.buttonDialog('choose folder'),self.back_button(),self.go_on_button())

    def train_button(self):
        train_button = QPushButton('Train',self)
        font = QFont('宋体',25)
        font.setItalic(True)
        font.setBold(True)
        train_button.setFont(font)
        train_button.setFixedSize(150,50)
        train_button.clicked.connect(self.train)
        return train_button

    def go_window(self):
        the_window = SecondPage_1()
        self.windowList.append(the_window)
        self.close()
        the_window.show()

    def train(self):
        parameters = []
        for item in self.Path_parameter:
            parameters.append(item.replace('/','\\'))
        rec_photo(150,150,open_path_1=parameters[0],save_path_1=parameters[1],open_path_2=parameters[2],
                  save_path_2=parameters[3],optimizer=parameters[4],batch_size=parameters[5],
                  epoche=parameters[6],save_tensorboard=parameters[7],save_model=parameters[8],
                  save_model_weight=parameters[9],save_model_structure=parameters[10])
        # self.go_window()


    def ninth_layout(self):
        QApplication.processEvents()
        self.text_button_Layout(self.text_lineEdit('select the folder to save model-structure file'),
                                self.buttonDialog('choose folder'),self.back_button(),self.train_button())


if __name__ =="__main__":
    app = QApplication(sys.argv)
    first = FirstPage()
    first.show()
    sys.exit(app.exec_())

