from PIL import Image
from PIL import ImageFilter
from PyQt5.QtWidgets import (QApplication, QMainWindow,QFileDialog,QMessageBox,QListWidget,QBoxLayout,QVBoxLayout,QHBoxLayout,QWidget,QLabel,QPushButton)

app=QApplication([])
window=QWidget()
window.setWindowTitle('Easy editor')
btn_dir=QPushButton('Папка')
ib_image=QLabel('картинки')
lw_files=QListWidget()

btn_left=QPushButton('left')
btn_right=QPushButton('right')
btn_flip=QPushButton('flip')
btn_sharp=QPushButton('sharp')
btn_bw=QPushButton('B/W')

row=QHBoxLayout()
col1=QVBoxLayout()
col2=QVBoxLayout()


col1.addWidget(btn_dir)
col2.addWidget(lw_files)
col2.addWidget(ib_image,95)
row_tools=QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
row_tools.addLayout(row_tools)
col2.addLayout(row_tools)

row.addLayout(col1,20)
row.addLayout(col2,80)
window.setLayout(row)

window.show()
wdir=""
def filter(files,extension):
    result=[]
    for filename in files:
        for ext in extension:
            if filename.endwith(ext):
                result.append(filename)
    return result

def choosewDir():
    global wdir
    wdir=QFileDialog.getExistingDirectory()

def showFileNameList():
    extension=['.jpg','.jpeg','.png','.gif','.bmp']
    choosewDir()
    filenames=filter(os.listdir(wdir),extension)

    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)
    btn_dir.clicked.connect(showFileNameList)

class ImageProcessor():
        def __init__(self):
            self.image = None
            self.filename = None
            self.dir=None
            self.save_dir="Modified/"
        def loadiimage(self,dir,filename):
            self.filename=filename
            self.dir=dir
            image_path=os.path.join(dir,filename)
            self.image=Image.open(image_path)
        def do_btw(self):
            self.image=self.image.convert('L')
            self.saveImage()
            image_path=os.path.join(self.dir,self.save_dir,self.filename)
            self.showImage(image_path)
        def saveImage(self):
            path=os.path.join(self.dir,self.save_dir)
            if not(os.path.exists(path)or os.path.isdir(path)):
                os.mkdir(path)
            image_path=os.path.join(path,self.filename)
            self.image.save(image_path)
        def blur(self):
            self.image=self.image.filter(ImageFilter.BoxBlur(4))
            image_path=os.path.join(self.dir,self.save_dir,self.filename)
            self.saveImage()
app.exec_()
