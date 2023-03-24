from tkinter import filedialog
import basicOperation
import ImgPreprocess
import globalRoot
import openImage

global Globalflag

#保存图像
def SaveImage():
    openImage.cv = None
    openImage.height1 = 0
    openImage.im = None
    openImage.img = None
    openImage.width1 = 0  
    Globalflag = globalRoot.Globalflag

    if Globalflag == 1 :
        p = basicOperation.pEditor
        basicOperation.opEditor = 1
        basicOperation.imEditor = 0
        basicOperation.counterEditor = 1
    elif Globalflag == 2:
        p = ImgPreprocess.pPre
        ImgPreprocess.opPre = 1
        ImgPreprocess.imPre = 0

    if p.mode != 'RGB':
        p = p.convert('RGB')
    savefilename = filedialog.asksaveasfilename()  #保存  返回文件名
    p.save(savefilename)
    
    if Globalflag == 1 :
        basicOperation.cvEditor[0].destroy()
    elif Globalflag == 2:
        ImgPreprocess.cvPre[0].destroy()

#图像另存为
def SaveAsImage():
    openImage.cv = None
    openImage.height1 = 0
    openImage.im = None
    openImage.img = None
    openImage.width1 = 0  
    Globalflag = globalRoot.Globalflag


    if Globalflag == 1 :
        p = basicOperation.pEditor
        basicOperation.opEditor = 1
        basicOperation.imEditor = 0
        basicOperation.counterEditor = 1
    elif Globalflag == 2:
        p = ImgPreprocess.pPre
        ImgPreprocess.opPre = 1
        ImgPreprocess.imPre = 0

    if p.mode != 'RGB':
        p = p.convert('RGB')
    newfile = filedialog.asksaveasfile()#另存为 会创建文件
    p.save(newfile)
    
    if Globalflag == 1 :
        basicOperation.cvEditor[0].destroy()
    elif Globalflag == 2:
        ImgPreprocess.cvPre[0].destroy()

