import sys
from Tkinter import *
from time import *
import tkMessageBox
import tkFont
import ttk
def naxt():
    nGui = Tk()
    nGui.geometry('800x600+500+200')
    nGui.title('Theatre Maneger')
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
    tkMessageBox.showinfo(title='Special Thanks',message='    THANKS  \n Chotipat Pornavalai ')
    return


mGui = Tk() 
mGui.geometry('800x600+550+200')
mGui.title('Theatre Manager')
#make label
mlabel = Label(text='BOX OFFICE',bg = 'gray', font = tkFont.Font(size = 30, weight=tkFont.BOLD)).place(x=50 ,y=0)
mlabel2 = Label(text='Current Date :'+strftime('%d %B %Y'),bg = 'gray',  font = tkFont.Font(size = 10, weight=tkFont.NORMAL)).place(x= 450 ,y=0)
mlabel3 = Label(text='Movies',bg = 'gray',  font = tkFont.Font(size = 10, weight=tkFont.BOLD)).place(x=125 ,y=60)
mlabel4 = Label(text='Round Time',bg = 'gray',  font = tkFont.Font(size = 10, weight=tkFont.BOLD)).place(x=500 ,y=60)


#make buttom
mbutton = Button(text = 'Summit',command = naxt).place(x=500,y=500)
mbutton = Button(text = 'Quit',command = out).place(x=600,y=500)

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








mGui.config(menu = menubar, background= 'gray')


mGui.mainloop()
