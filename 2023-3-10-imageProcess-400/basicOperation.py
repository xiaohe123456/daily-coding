import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
import globalRoot
import openImage
import ImgPreprocess
import cv2
from tkinter import messagebox

#全局变量
#c,c1为画布序号  cv是画布序列  im图片序号数组  img图片数组
global cEditor, c1Editor, cvEditor, numEditor, imEditor, imgEditor, pEditor, Globalflag, tmpimg, scaleBin
counterEditor = 1
opEditor = 1   #操作次数
a = []   #数组，保存画布序号
i = 0    #数组下标，判断相邻两次处理的图片是否一致
    
#图像灰度化
def GrayImg():
    global counterEditor        #对一张图片处理的次数
    global cEditor, c1Editor, opEditor, i   #c,c1只处理一张和多张图片时在画布上创建图像的序号，op为进行放大操作的次数，i为序号，判断当前处理图片与上一次操作处理的图片是否一致        
    global pEditor, imgEditor, cvEditor, imEditor, numEditor, tmpimg #flag为控制画布上只显示最新图片的标志 ，num为画布的序号
    tmpimg = []                           
    Globalflag = 1
    width1 = openImage.width1      #获取原图像大小
    height1 = openImage.height1
    
    root = globalRoot.root
    imgEditor = openImage.img
    cvEditor = openImage.cv
    imEditor = openImage.im 

    numEditor = openImage.num      #根据num判断当前处理的图片是否处理过，保证画布中保留的是最新的图片
    a.append(numEditor)            #根据num创建数组，根据数组相邻的两个数是否相同，判断当前处理的图片是否发生变化                       
    pEditor = imgEditor[int(numEditor)]
    
    if ImgPreprocess.opPre != 1:
        imgEditor = ImgPreprocess.tmpimgPre
        pEditor = ImgPreprocess.pPre
        imEditor = ImgPreprocess.imPre
        cvEditor = ImgPreprocess.cvPre
        ImgPreprocess.opPre = 1
        counterEditor = 1
        
    img0 = np.array(imgEditor[int(numEditor)])
    if img0.ndim==3:
        pEditor =cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)  #图像灰度化函数
        pEditor = Image.fromarray(pEditor)
        imgEditor[int(numEditor)]=pEditor
        pic = ImageTk.PhotoImage(pEditor)
        cvEditor[int(numEditor)].delete(imEditor[int(numEditor)])
        #在画布上显示图像
        cEditor = cvEditor[int(numEditor)].create_image((width1 + 100) / 2, (height1 + 100) / 2, anchor='center', image=pic,tag=int(numEditor))
        imEditor[int(numEditor)]=cEditor
    else:
        messagebox.showinfo('Prompt','image has been grayed')

    opEditor += 1
    tmpimg.append(pEditor)
    globalRoot.Globalflag = Globalflag
    globalRoot.canvas = cvEditor
    openImage.img=imgEditor
    root.mainloop()

#图像二值化
def BinImg():
    global counterEditor        #对一张图片处理的次数
    global opEditor, i, cEditor, c1Editor 
    global pEditor, imgEditor, cvEditor, imEditor, numEditor, tmpimg, scaleBin

    tmpimg = []          
    Globalflag = 1
    width1 = openImage.width1      #获取原图像大小
    height1 = openImage.height1
    
    root = globalRoot.root
    imgEditor = openImage.img
    cvEditor = openImage.cv
    imEditor = openImage.im 
    
    if ImgPreprocess.opPre != 1:
        imgEditor = ImgPreprocess.tmpimgPre
        pEditor = ImgPreprocess.pPre
        imEditor = ImgPreprocess.imPre
        cvEditor = ImgPreprocess.cvPre
        ImgPreprocess.opPre = 1
        counterEditor = 1
    numEditor = openImage.num      #根据num判断当前处理的图片是否处理过，保证画布中保留的是最新的图片
    a.append(numEditor)            #根据num创建数组，根据数组相邻的两个数是否相同，判断当前处理的图片是否发生变化                       
    
    img0 = np.array(imgEditor[int(numEditor)])
    if imgEditor[int(numEditor)].mode !='RGB':
         pEditor = img0
    else:
         pEditor = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)

    scaleBin = int(globalRoot.scaleBin)#获取滑块上二值化的小阈值
    ret,pEditor=cv2.threshold(pEditor,scaleBin,255,cv2.THRESH_BINARY)  #二值化函数
    pEditor = Image.fromarray(pEditor)
    imgEditor[int(numEditor)]=pEditor
    pic = ImageTk.PhotoImage(pEditor)
   
    cvEditor[int(numEditor)].delete(imEditor[int(numEditor)])
    cEditor = cvEditor[int(numEditor)].create_image((width1 + 100) / 2, (height1 + 100) / 2, anchor='center', image=pic,tag=int(numEditor))
    imEditor[int(numEditor)]=cEditor
    
    opEditor += 1
    tmpimg.append(pEditor)
    globalRoot.Globalflag = Globalflag
    globalRoot.canvas = cvEditor
    openImage.img=imgEditor
    root.mainloop()

#图像锐化
def ImgSharpen():
    global counterEditor  # 对一张图片处理的次数
    global cEditor, c1Editor, opEditor, i  # c,c1只处理一张和多张图片时在画布上创建图像的序号，op为进行放大操作的次数，i为序号，判断当前处理图片与上一次操作处理的图片是否一致
    global pEditor, imgEditor, cvEditor, imEditor, numEditor, tmpimg  # flag为控制画布上只显示最新图片的标志 ，num为画布的序号
    tmpimg = []
    Globalflag = 1
    width1 = openImage.width1  # 获取原图像大小
    height1 = openImage.height1

    root = globalRoot.root
    imgEditor = openImage.img
    cvEditor = openImage.cv
    imEditor = openImage.im
    numEditor = openImage.num  # 根据num判断当前处理的图片是否处理过，保证画布中保留的是最新的图片
    a.append(numEditor)  # 根据num创建数组，根据数组相邻的两个数是否相同，判断当前处理的图片是否发生变化
    pEditor = imgEditor[int(numEditor)]
    
    if ImgPreprocess.opPre != 1:
        imgEditor = ImgPreprocess.tmpimgPre
        pEditor = ImgPreprocess.pPre
        imEditor = ImgPreprocess.imPre
        cvEditor = ImgPreprocess.cvPre
        ImgPreprocess.opPre = 1
        counterEditor = 1
        
    img = np.array(imgEditor[int(numEditor)])
    #拉普拉斯  默认核大小为1 表示3*3的核 其中四个角的值均为0  只有四个邻域的值不为0
    lap = cv2.Laplacian(img,cv2.CV_64F)
    #将图像元素值的范围限制在0-255之间，以及将其转换为8位图
    pEditor = cv2.convertScaleAbs(lap)
    pEditor = Image.fromarray(pEditor)
    imgEditor[int(numEditor)]=pEditor
    pic = ImageTk.PhotoImage(pEditor)
    
    cvEditor[int(numEditor)].delete(imEditor[int(numEditor)])
    cEditor = cvEditor[int(numEditor)].create_image((width1 + 100) / 2, (height1 + 100) / 2, anchor='center', image=pic,tag=int(numEditor))
    imEditor[int(numEditor)]=cEditor
    
    opEditor += 1
    tmpimg.append(pEditor)
    globalRoot.Globalflag = Globalflag
    globalRoot.canvas = cvEditor
    openImage.img=imgEditor
    root.mainloop()


#图像直方图
def ImgHist():
    global counterEditor  # 对一张图片处理的次数
    global cEditor, c1Editor, opEditor, i  # c,c1只处理一张和多张图片时在画布上创建图像的序号，op为进行放大操作的次数，i为序号，判断当前处理图片与上一次操作处理的图片是否一致
    global pEditor, imgEditor, cvEditor, imEditor, numEditor, tmpimg  # flag为控制画布上只显示最新图片的标志 ，num为画布的序号
    tmpimg = []
    Globalflag = 1
    width1 = openImage.width1  # 获取原图像大小
    height1 = openImage.height1
    
    root = globalRoot.root
    imgEditor = openImage.img
    cvEditor = openImage.cv
    imEditor = openImage.im
    numEditor = openImage.num  # 根据num判断当前处理的图片是否处理过，保证画布中保留的是最新的图片
    a.append(numEditor)  # 根据num创建数组，根据数组相邻的两个数是否相同，判断当前处理的图片是否发生变化
    pEditor = imgEditor[int(numEditor)]
    
    if ImgPreprocess.opPre != 1:
        imgEditor = ImgPreprocess.tmpimgPre
        pEditor = ImgPreprocess.pPre
        imEditor = ImgPreprocess.imPre
        cvEditor = ImgPreprocess.cvPre
        ImgPreprocess.opPre = 1
        counterEditor = 1
    img0 = np.array(imgEditor[int(numEditor)])
    color = ('b','g','r')
    #对一个列表或数组既要遍历索引又要遍历元素时,使用内置enumerrate函数会有更加直接，优美的做法
    #enumerate会将数组或列表组成一个索引序列。使我们再获取索引和索引内容的时候更加方便 
    if img0.ndim == 3:
        for i,col in enumerate(color):
            histr = cv2.calcHist([img0],[i],None,[256],[0,256])  #彩色图像直方图
            pEditor = plt.plot(histr,color = col)
            plt.xlim([0,256])
            plt.savefig("test.jpg")
            pEditor = cv2.imread("test.jpg")
            pEditor = Image.fromarray(pEditor)
            imgEditor[int(numEditor)] = pEditor
            pic = ImageTk.PhotoImage(pEditor)
            cvEditor[int(numEditor)].delete(imEditor[int(numEditor)])
            cEditor = cvEditor[int(numEditor)].create_image((width1 + 100) / 2, (height1 + 100) / 2, anchor='center',image=pic, tag=int(numEditor))
            imEditor[int(numEditor)] = cEditor
    else:
        histr = cv2.calcHist([img0], [0], None, [256], [0, 256])  # 灰度图像直方图
        pEditor = plt.plot(histr)
        plt.xlim([0, 256])
        plt.savefig("test.jpg")
        pEditor = cv2.imread("test.jpg")
        pEditor = Image.fromarray(pEditor)
        imgEditor[int(numEditor)]=pEditor
        pic = ImageTk.PhotoImage(pEditor)
    
    cvEditor[int(numEditor)].delete(imEditor[int(numEditor)])
    cEditor = cvEditor[int(numEditor)].create_image((width1 + 100) / 2, (height1 + 100) / 2, anchor='center', image=pic,tag=int(numEditor))
    imEditor[int(numEditor)] = cEditor
    opEditor += 1
    tmpimg.append(pEditor)
    globalRoot.Globalflag = Globalflag
    globalRoot.canvas = cvEditor
    openImage.img=imgEditor
    root.mainloop()
