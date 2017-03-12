# encoding=utf-8
import tkinter
from tkinter import *
from tkinter import ttk
# from PIL import ImageTk
import tkinter.messagebox
from natural_language import *

root = Tk()
root.geometry('650x300+400+200')
root.title('电影评论打分系统')


def b1_click():
    root.title('电影评论打分系统(KNN模式)')


def b2_click():
    start()
    root.title('电影评论打分系统(SVM模式)')


def b3_click():
    root.title('电影评论打分系统(Naive Bayes模式)')


def b4_click():
    result=machine_learning(var1.get())
    var2.set(result[0][0]*10.0)


def rank(var):
    return 0

# canvas = Canvas(root, width=600, height=400, bg='blue')
# canvas.pack(expand=YES, fill=BOTH)
button1 = Button(root, text='KNN', font=('Arial', 12), command=b1_click)
button1.grid(row=0, column=0)
button2 = Button(root, text='SVM', font=('Arial', 12), command=b2_click)
button2.grid(row=0, column=1)
button3 = Button(root, text='Naive Bayes', font=('Arial', 12), command=b3_click)
button3.grid(row=0, column=3)
label1 = Label(root, text='输入评论：', height=5, width=10, wraplength=100, font=('黑体', 12))
label1.grid(row=1, column=4, rowspan=3)
# var1, var2 保存输入的评论
var1 = StringVar()
var2 = StringVar()
e1 = Entry(root, bd=4, foreground='red', font=('黑体', 15), textvariable=var1)
e1.grid(row=1, column=5, rowspan=3, columnspan=3, padx=5, pady=5)
label2 = Label(root, text='分数：', font=('黑体', 12))
label2.grid(row=5, column=4, rowspan=3)
# e2 = Entry(root, bd=4, foreground='red', font=('黑体', 15), textvarible=var2)
# e2.grid(row=5, column=5, rowspan=3, columnspan=3, padx=5, pady=5)
label3 = Label(root, textvariable=var2, fg='red', font=('黑体', 15))
label3.grid(row=5, column=5, rowspan=3)
button3 = Button(root, text='提交', font=('Arial', 12), command=b4_click)
button3.grid(row=1, column=9, rowspan=3, padx=5, pady=5)
mainloop()
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         Frame(height=600, width=800, bg='#f0fff0').pack()
#         self.createWidgets()
#         self.pack()
#
#     def createWidgets(self):
#         self.inputBox = Entry(self)
#         self.inputBox.pack(side=LEFT)
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.inputBox.get() or 'world'
#         tkinter.messagebox.showinfo('Message', 'Hello, %s'%name)
#
# if __name__ == '__main__':
#     app = Application()
#     app.master.title('电影评论打分系统')
#     app.mainloop()
