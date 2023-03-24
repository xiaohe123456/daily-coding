from SelectAndSearch import *
#  创建主界面
app = tk.Tk()
app.title('基于内容的图像检索')
# background = tk.PhotoImage(file="icon/nex.gif")  # 背景图片
# background2 = tk.PhotoImage(file="icon/bk2.GIF")  # 背景图片

#  添加背景和标题
bg = tk.Label(app, bg="#000000")
bg.place(relx=0, rely=0, relwidth=1, relheight=1)
title = tk.Label(app, text='基于内容的图像检索', font=("宋体", 30), compound=tk.CENTER)
title.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.15)


SelectAndSearch(app)
def quit():
    app.destroy()

leave = tk.Button(app, text = "退出", width=30, command=quit)
leave.place(relx=0.8, rely=0.9)

app.mainloop()
