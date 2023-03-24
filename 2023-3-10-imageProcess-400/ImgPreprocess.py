from PIL import Image, ImageTk
import globalRoot
import openImage
import numpy as np
import cv2
import basicOperation


#全局变量
global cvPre, imPre, imgPre, pPre, tmpimgPre
global Globalflag  
opPre = 1

#均值滤波，是由一个归一化卷积框完成的。
#只是用卷积框覆盖区域所有像素的平均值来代替中心元素
def ImgAveBlur():
    global opPre, imgPre, imPre, pPre, cvPre, tmpimgPre,numEditor
    tmpimgPre = []
    Globalflag = 2
    width1 = openImage.width1 #获取原图像大小
    height1 = openImage.height1
    root = globalRoot.root

    imgPre = openImage.img
    cvPre = openImage.cv
    imPre = openImage.im
    numEditor = openImage.num      #根据num判断当前处理的图片是否处理过，保证画布中保留的是最新的图片                  
    
    img0 = np.array(imgPre[int(numEditor)])  
    p = cv2.blur(img0, (3, 3))  #均值滤波
    pPre = Image.fromarray(p)             #矩阵转为PIL图像
    pic = ImageTk.PhotoImage(pPre)
    cvPre[int(numEditor)].delete(imPre)    #删除处理之前的图像
    imPre = cvPre[int(numEditor)].create_image((width1+100)/2, (height1+100)/2, anchor='center', image=pic,tag=int(numEditor))
    globalRoot.Globalflag = Globalflag
    opPre += 1
    tmpimgPre.append(pPre)
    globalRoot.canvas = cvPre
    root.mainloop()   

#中值滤波
#这个滤波器经常用来去除椒盐噪声
def ImgMedianBlur():
    global opPre, imgPre, imPre, pPre, cvPre, tmpimgPre
    tmpimgPre = []
    Globalflag = 2
    width1 = openImage.width1 #获取原图像大小
    height1 = openImage.height1
    root = globalRoot.root
    if basicOperation.opEditor != 1:
        imgPre = basicOperation.tmpimg
        cvPre = basicOperation.cvEditor
        imPre = basicOperation.imEditor
    else:
        imgPre = openImage.img
        cvPre = openImage.cv
        imPre = openImage.im
    img0 = np.array(imgPre[0])  
    p = cv2.medianBlur(img0, 3)
    pPre = Image.fromarray(p)             #矩阵转为PIL图像
    pic = ImageTk.PhotoImage(pPre)
    cvPre[0].delete(imPre)    #删除处理之前的图像
    imPre = cvPre[0].create_image((width1+100)/2, (height1+100)/2, anchor='center', image=pic)
    globalRoot.Globalflag = Globalflag
    opPre += 1
    tmpimgPre.append(pPre)
    root.mainloop() 

#Canny边缘检测
def Canny():    
    global opPre, imgPre, imPre, pPre, cvPre, tmpimgPre
    tmpimgPre = []
    Globalflag = 2
    width1 = openImage.width1 #获取原图像大小
    height1 = openImage.height1
    root = globalRoot.root
    if basicOperation.opEditor != 1:
        imgPre = basicOperation.tmpimg
        cvPre = basicOperation.cvEditor
        imPre = basicOperation.imEditor
    else:
        imgPre = openImage.img
        cvPre = openImage.cv
        imPre = openImage.im
    img0 = np.array(imgPre[0])  
    if imgPre[0].mode != 'RGB':
        p = img0
    else:
        p =cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)  #灰度化
    p = cv2.Canny(p,100,200)
    pPre = Image.fromarray(p)             #矩阵转为PIL图像
    pic = ImageTk.PhotoImage(pPre)
    cvPre[0].delete(imPre)    #删除处理之前的图像
    imPre = cvPre[0].create_image((width1+100)/2, (height1+100)/2, anchor='center', image=pic)
    globalRoot.Globalflag = Globalflag
    opPre += 1
    tmpimgPre.append(pPre)
    root.mainloop() 

