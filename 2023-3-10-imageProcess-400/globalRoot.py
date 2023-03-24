import tkinter
global Globalflag, scaleBin, canvas
Globalflag = 0
scaleBin = 0
canvas = []

root1 = tkinter.Tk()
root1.title("20101122张金璐")
sw = root1.winfo_screenwidth()  # 得到屏幕宽度
sh = root1.winfo_screenheight()  # 得到屏幕高度
ww = 1100
wh = 600
#窗口宽高为100
x = (sw-ww) / 2
y = (sh-wh) / 2
root1.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

root = root1
print("图像处理系统开始执行")



