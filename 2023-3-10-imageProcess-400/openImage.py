from PIL import Image, ImageTk
from tkinter import filedialog, Canvas
import globalRoot
from tkinter import messagebox
import win32api,win32con
#全局变量
global img, p, cv, im, flag, num, width1, height1, filepath, Globalflag, flagnum
global x1, y1, x2, y2

def resize(w, h, w_box, h_box, pil_image):
  '''
  对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
  '''
  f1 = 1.0 * w_box/w # 1.0 forces float division in Python2
  f2 = 1.0 * h_box/h
  factor = min([f1, f2])
  width = int(w*factor)
  height = int(h*factor)
  return pil_image.resize((width, height), Image.ANTIALIAS)


#加载图像
def LoadImage():
    global img
    global cv
    global im
    global width1,height1,filepath,flagnum
    global Globalflag
    global w_box, h_box
    global img_w
    w_box=400
    h_box=400
    root = globalRoot.root
    im=[]
    img=[]
    img1=[]   #中间变量，原始图像与在画布上创建图像之间的中间变量
    cv=[]     #canvas 画布序列
    img_w=[]
    flagnum = 0

    if len(globalRoot.canvas) != 0:
        cv = globalRoot.canvas
        for k in range(len(globalRoot.canvas)):
            globalRoot.canvas[k].destroy()
        flagnum = 1
        cv.clear()
        globalRoot.canvas = []

    filepath = filedialog.askopenfilenames()  #打开图像
    length = len(filepath)
    for i in range(length):
        temp = Image.open(filepath[i])
        width0, height0 = temp.size
        temp = resize( width0, height0,w_box, h_box,temp) #调整图像大小
        width1, height1 = temp.size
        img.append(temp)
        tempImg = ImageTk.PhotoImage(img[i])
        img1.append(tempImg)
        #在画布上显示图像  mainloop要和img的作用域一致
        tempCanvas = Canvas(root, width=width1+100, height=height1+100, bg="white")
        cv.append(tempCanvas)
        cv[i].bind("<Button-1>", getImg)  #绑定鼠标事件

        tmp = cv[i].create_image((width1+100)/2, (height1+100)/2, anchor='center', image=img1[i] , tag=int(i))
        im.append(tmp)
    if length == 1:    #只处理一张图片
        #获得屏幕分辨率X轴        
        w2 = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        #获得屏幕分辨率Y
        h2 = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        x1 =  w2 / 3 - width1 / 2
        y1 =  h2 / 3 - height1 / 2
        cv[0].place(x = x1, y = y1 , width=width1+100, height=height1+100)  #绝对布局

    root.mainloop()


#鼠标绑定事件函数，得到要处理的图片   
def getImg(event): 
    global flag
    global p
    global num,flagnum
    flag = True
    global cv1
    #获取画布
    cv1=event.widget
    #获取当前选中的图形项
    ct=cv1.find_closest(event.x, event.y)
    #获取图形项对应的tag
    ct=cv1.gettags(ct)
        
    if ct is not None and len(ct) > 0:
        ct = ct[0]
        num=ct
        p=img[int(ct)]

#退出函数
def quit_gui():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        globalRoot.root.destroy()


