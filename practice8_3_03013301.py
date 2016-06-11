# -*- coding: utf-8 -*- 
import tkinter
import time
from tkinter import Label, Button, Entry, END

# 实验安排数据
schedule = [["第10周周三下午","2016/4/27","14:00-16:00","热工基础实验","压力分布规律局部换热系数"],
            ["第10周周三晚上","2016/4/27","19:00-21:00","热工基础实验","黑度角系数"],
            ["第11周周三下午","2016/5/4","14:00-16:00","燃烧实验","气体燃烧热值测试实验"],
            ["第11周周三晚上","2016/5/4","18:30-20:50","计算机实验","计算机实验"],
            ["第12周周一晚上","2016/5/9","18:30-20:50","计算机实验","计算机实验"],
            ["第12周周三下午","2016/5/11","14:00-16:00","热工基础实验","沿程阻力流态观察"],
            ["第12周周三晚上","2016/5/11","19:00-21:00","热工基础实验","喷管"],
            ["第12周周六上午","2016/5/14","9:00-11:00","燃烧实验","固液体燃烧热值测试实验"],
            ["第13周周三下午","2016/5/18","14:00-16:00","热工测量+泵与风机实验","实验7+水泵实验"],
            ["第13周周三晚上","2016/5/18","19:00-21:00","热工测量实验","实验2"],
            ["第14周周三下午","2016/5/25","14:00-16:00","热工测量实验","实验4、5"],
            ["第14周周三晚上","2016/5/25","19:00-21:00","热工测量实验","实验6"],
            ["第14周周四下午","2016/5/26","14:00-16:00","热工测量实验","实验1、3"],
            ["第15周周三下午","2016/6/1","14:00-16:00","热工测量+泵与风机实验","实验8+风机实验"]]

current = 0

def preOne():
    global current
    current = current-1
    if(current<1):
        current = 0
    setCurrent(current)

def nextOne():
    global current
    current = current+1
    if(current>14):
        current = 15
    setCurrent(current)

def reset():
    init()

def setCurrent(index):
    textWeek.delete(0, END)
    textDate.delete(0, END)
    textTime.delete(0, END)
    textSubject.delete(0, END)
    textName.delete(0, END)
    if(0<index<15):
        textWeek.insert(0, schedule[index-1][0])
        textDate.insert(0, schedule[index-1][1])
        textTime.insert(0, schedule[index-1][2])
        textSubject.insert(0, schedule[index-1][3])
        textName.insert(0, schedule[index-1][4])
    else:
        textWeek.insert(0, "没有实验啦！")
        textDate.insert(0, "没有实验啦！")
        textTime.insert(0, "没有实验啦！")
        textSubject.insert(0, "没有实验啦！")
        textName.insert(0, "没有实验啦！")
        
def init():
    global current
    epoch = time.time()
    if(epoch<1461736800):
        setCurrent(1)
        current=1
    elif (epoch<1461754800):
        setCurrent(2)
        current=2
    elif (epoch<1462341600):
        setCurrent(3)
        current=3
    elif (epoch<1462357800):
        setCurrent(4)
        current=4
    elif (epoch<1462789800):
        setCurrent(5)
        current=5
    elif (epoch<1462946400):
        setCurrent(6)
        current=6
    elif (epoch<1462964400):
        setCurrent(7)
        current=7
    elif (epoch<1463187600):
        setCurrent(8)
        current=8
    elif (epoch<1463551200):
        setCurrent(9)
        current=9
    elif (epoch<1463569200):
        setCurrent(10)
        current=10
    elif (epoch<1464156000):
        setCurrent(11)
        current=11
    elif (epoch<1464174000):
        setCurrent(12)
        current=12
    elif (epoch<1464242400):
        setCurrent(13)
        current=13
    elif (epoch<1464760800):
        setCurrent(14)
        current=14
    else:
        setCurrent(15)
        current=15

# main function
root = tkinter.Tk()
root.title("03013301_王路_实验8.3")
root.geometry('300x280')
label = Label(root,text="实验安排明细")
labelWeek = Label(root,text="周别")
labelDate = Label(root,text="日期")
labelTime = Label(root,text="时间")
labelSubject = Label(root,text="科目")
labelName = Label(root,text="名称")
textWeek = Entry(root)
textDate = Entry(root)
textTime = Entry(root)
textSubject = Entry(root)
textName = Entry(root)
btP = Button(root,text="上一个",command=preOne)
btN = Button(root,text="下一个",command=nextOne)
btC = Button(root,text="复原",command=reset)

label.place(x=90,y=10)
labelWeek.place(x=35,y=50)
labelDate.place(x=35,y=80)
labelTime.place(x=35,y=110)
labelSubject.place(x=35,y=140)
labelName.place(x=35,y=170)
textWeek.place(x=70,y=50)
textDate.place(x=70,y=80)
textTime.place(x=70,y=110)
textSubject.place(x=70,y=140)
textName.place(x=70,y=170)
btP.place(x=50,y=220)
btN.place(x=180,y=220)
btC.place(x=120,y=220)

init()
root.mainloop()