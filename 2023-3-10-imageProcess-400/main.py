from PIL import Image, ImageTk
import tkinter
import basicOperation
import globalRoot
import openImage
import ImgPreprocess
import SaveImage
from tkinter import messagebox

def View():
    root = globalRoot.root
    # 菜单条
    menubar = tkinter.Menu(root)
    # 文件
    file = tkinter.Menu(menubar, tearoff=False)
    menubar.add_cascade(label='文件', menu=file)
    file.add_command(label='加载图像', command=openImage.LoadImage)
    file.add_command(label='保存图像', command=SaveImage.SaveImage)
    file.add_command(label='另存为', command=SaveImage.SaveAsImage)
    file.add_separator()
    file.add_command(label='退出', command=openImage.quit_gui)   #退出

    def getScale(value):
        globalRoot.scaleBin = value
    scale = tkinter.Scale(root, from_=127, to=255, orient=tkinter.HORIZONTAL, command=getScale)
    scale.place(x=10, y=30)
    # 工具条
    toolbar = tkinter.Frame(root, height=20)
    toolbar.grid(row=0, column=0)

    buttonGray = tkinter.Button(toolbar, text='灰度化', width=8, command=basicOperation.GrayImg)
    buttonGray.grid(row=0, column=2)
    buttonBin = tkinter.Button(toolbar, text='二值化', width=8, command=basicOperation.BinImg)
    buttonBin.grid(row=0, column=3)
    buttonAve = tkinter.Button(toolbar, text='均值滤波', width=10, command=ImgPreprocess.ImgAveBlur)
    buttonAve.grid(row=0, column=4)
    buttonMedian = tkinter.Button(toolbar, text='中值滤波', width=10, command=ImgPreprocess.ImgMedianBlur)
    buttonMedian.grid(row=0, column=5)
    buttonLap = tkinter.Button(toolbar, text='拉普拉斯锐化', width=12, command=basicOperation.ImgSharpen)
    buttonLap.grid(row=0, column=6)
    buttonCanny = tkinter.Button(toolbar, text='边缘检测', width=10, command=ImgPreprocess.Canny)
    buttonCanny.grid(row=0, column=7)
    buttonHist = tkinter.Button(toolbar, text='图像直方图', width=10, command=basicOperation.ImgHist)
    buttonHist.grid(row=0, column=8)
    def help_():
        messagebox.showinfo("学号-姓名","20101122-张金璐")
    buttonHelp= tkinter.Button(toolbar, text='帮助', width=8, command=help_)
    buttonHelp.grid(row=0, column=9)


    root.config(menu=menubar)
    root.mainloop()



def main():
    View()


if __name__ == "__main__":
    main()
