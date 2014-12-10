import sys
from Tkinter import *
from time import *
import tkMessageBox
import tkFont
import ttk

def naxt():
    mGui.destroy()
    nGui = Tk()
    nGui.geometry('800x600+500+200')
    nGui.title('Theatre Maneger')
    def thank_you():
        check = choose.get() #check incorrect input
        if check.isdigit() == False and '.' not in check:
            tkMessageBox.showinfo(message='Incorrect Input \n Please Try Again.')
            return
        
        select = int(choose.get())
        price = (select * 80)
        thank = tkMessageBox.askyesno(title = 'Thank You',message='     Booking Completed \n     Total  =  '+  str(price) + '    Bath')
        if thank > 0:
            nGui.destroy()
            return
    def out_1():
        nExit = tkMessageBox.askyesno(title="Quit",message="Are You Sure")
        if nExit > 0:
            nGui.destroy()
            return
        
    #make label header
    nlabel = Label(nGui,text='Buy Ticket',bg = 'gray', font = tkFont.Font(size = 30, weight=tkFont.BOLD)).place(x=50,y=0)
    nlabel2 = Label(nGui,text='Current Date :'+strftime('%d %B %Y'),bg = 'gray',  font = tkFont.Font(size = 10, weight=tkFont.NORMAL)).place(x= 450 ,y=0)
    nlabel4 = Label(nGui,text='Seat    from',bg = 'gray',font = tkFont.Font(size = 15, weight=tkFont.NORMAL)).place(x=375, y=470)
    nlabel5 = Label(nGui,text='to',bg = 'gray',font = tkFont.Font(size = 15, weight=tkFont.NORMAL)).place(x=617, y=470)

    #make entry box

    start = StringVar()
    nentry = Entry(nGui,textvariable=start).place(x= 490,y= 475)

    stop = StringVar()
    nentry2 = Entry(nGui,textvariable=stop).place(x= 640,y= 475)

    #make buttom nGui
    nbutton = Button(text = 'Summit',command = thank_you).place(x=300,y=530)
    nbutton2 = Button(text = 'Quit',command = out_1).place(x=400,y=530)
    
    #make seat input
    nlabel3 = Label(nGui,text='select seat amount',bg = 'gray',font = tkFont.Font(size = 15, weight=tkFont.NORMAL)).place(x=50, y=470)
    choose = StringVar()
    select = Entry(nGui,textvariable=choose).place(x= 230, y=475)

    
    nGui.config(background = 'gray')
 
def out():
    mExit = tkMessageBox.askyesno(title="Quit",message="Are You Sure")
    if mExit > 0:
        mGui.destroy()
        return
def about():
    tkMessageBox.showinfo(title='About',message='This is project in PSIT subject')
    return
def helpdocs():
    tkMessageBox.showinfo(title='Help Docs',message='This application help you to booking movies \n - select your movie and seat')
    return
def creator():
    tkMessageBox.showinfo(title='Creator',message='     CREAT BY \n57070041 Traisak Traisenee \n57070078 Patcharapon Sophon')
    return    
def thanks():
    tkMessageBox.showinfo(title='Thanks',message='    THANKS  \n Chotipat Pornavalai ')
    return
## Poster office
def pic_1():
    header_pic = PhotoImage(file = "001.gif")
    header = Label(image = header_pic)
    header.image = header_pic 
    header.place(x = 8, y = 90)
def pic_2():
    header_pic = PhotoImage(file = "002.gif")
    header = Label(image = header_pic)
    header.image = header_pic 
    header.place(x = 8, y = 200)
def pic_3():
    header_pic = PhotoImage(file = "003.gif")
    header = Label(image = header_pic)
    header.image = header_pic 
    header.place(x = 8, y = 310)
def pic_4():
    header_pic = PhotoImage(file = "004.gif")
    header = Label(image = header_pic)
    header.image = header_pic 
    header.place(x = 8, y = 420)
#name movie
def get_movie(name, time):
    movielabel = Label(text= name,bg = 'gray',  font = tkFont.Font(size = 15, weight=tkFont.NORMAL)).place(x=225 ,y=550)
    roundlabel = Label(text= time,bg = 'gray',  font = tkFont.Font(size = 15, weight=tkFont.NORMAL)).place(x=450 ,y=550)

#make time select
def time_select(mGui):
    time_data = open('time.txt', 'r')
    time = [map(lambda x: x,i.split()) for i in time_data]
    y = 100
    for i in time:
        x = 440
        count = 0
        for j in i[1:]:
            if count == 5:
                y += 35
                x = 440
            temp = Button(text=str(j)).place(x = x, y = y)
            x += 50
            count += 1
        if count > 5:
            y -= 35
        y += 110

    
mGui = Tk() 
mGui.geometry('800x600+550+200')
mGui.title('Theatre Manager')
mGui.resizable(width=FALSE, height=FALSE)
#make label
mlabel = Label(text='BOX OFFICE',bg = 'gray', font = tkFont.Font(size = 30, weight=tkFont.BOLD)).place(x=50 ,y=0)
mlabel2 = Label(text='Current Date :'+strftime('%d %B %Y'),bg = 'gray',  font = tkFont.Font(size = 10, weight=tkFont.NORMAL)).place(x= 300 ,y=5)
mlabel3 = Label(text='Movies',bg = 'gray',  font = tkFont.Font(size = 10, weight=tkFont.BOLD)).place(x=175 ,y=60)
mlabel4 = Label(text='Round Time',bg = 'gray',  font = tkFont.Font(size = 10, weight=tkFont.BOLD)).place(x=500 ,y=60)
mlabel5 = Label(text='Current Movie :',bg = 'gray',  font = tkFont.Font(size = 15, weight=tkFont.NORMAL)).place(x=75 ,y=550)
mlabel6 = Label(text='Round :',bg = 'gray',  font = tkFont.Font(size = 15, weight=tkFont.NORMAL)).place(x=365 ,y=550)

#make buttom
mbutton = Button(text = 'Summit',command = naxt).place(x=550,y=550)
mbutton2 = Button(text = 'Quit',command = out).place(x=650,y=550)

#make About menu
menubar = Menu(mGui)
filemenu = Menu(menubar,tearoff = 0)
filemenu.add_command(label='Creator', command = creator)
filemenu.add_command(label='Thanks' , command = thanks)
menubar.add_cascade(label="About Me",menu=filemenu)

#make Help menu
helpmenu = Menu(menubar,tearoff = 0)
helpmenu.add_command(label='Help Docs', command = helpdocs)
helpmenu.add_command(label='About' , command = about)
menubar.add_cascade(label="Help",menu=helpmenu)

#make Canvas movie
canvas_1 = Canvas(mGui,height = 100,width= 225,bg = '#2E8B57').place(x=160,y=90)
canvas_2 = Canvas(mGui,height = 100,width= 225,bg = '#2E8B57').place(x=160,y=200)
canvas_3 = Canvas(mGui,height = 100,width= 225,bg = '#2E8B57').place(x=160,y=310)
canvas_4 = Canvas(mGui,height = 100,width= 225,bg = '#2E8B57').place(x=160,y=420)

#make Canvas Round Time
canvas_5 = Canvas(mGui,height = 100,width= 270,bg = '#2E8B57').place(x=430,y=90)
canvas_6 = Canvas(mGui,height = 100,width= 270,bg = '#2E8B57').place(x=430,y=200)
canvas_7 = Canvas(mGui,height = 100,width= 270,bg = '#2E8B57').place(x=430,y=310)
canvas_8 = Canvas(mGui,height = 100,width= 270,bg = '#2E8B57').place(x=430,y=420)


pic_1(),pic_2(),pic_3(),pic_4()
time_select(mGui)
mGui.config(menu = menubar, background= 'gray')
mGui.mainloop()
