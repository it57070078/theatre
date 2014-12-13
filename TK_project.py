import sys
from Tkinter import *
from time import *
import tkMessageBox
import tkFont
import ttk

class SeatPart(Frame):
    ''' Identify some available seat and save data to exist file'''
    def __init__(self, master=None):
        Frame.__init__(self, master)

'''
def cont():
    mGui.destroy()
    nGui = Tk()
    nGui.geometry('800x600+500+200')
    nGui.title('Theatre Manager')

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
    nlabel = Label(nGui,text='Buy Ticket',bg = '#464646', font = tkFont.Font(size = 30, weight=tkFont.BOLD)).place(x=50,y=0)
    nlabel2 = Label(nGui,text='Current Date :'+strftime('%d %B %Y'),bg = '#464646',  font = tkFont.Font(size = 10, weight=tkFont.NORMAL)).place(x= 300 ,y=0)
    nlabel4 = Label(nGui,text='Seat    from',bg = '#464646',font = tkFont.Font(size = 15, weight=tkFont.NORMAL)).place(x=513, y=470)
    nlabel5 = Label(nGui,text='to',bg = '#464646',font = tkFont.Font(size = 15, weight=tkFont.NORMAL)).place(x=675, y=470)

    #make entry box

    start = StringVar()
    nentry = Entry(nGui,width = 5,textvariable=start).place(x= 632,y= 475)

    stop = StringVar()
    nentry2 = Entry(nGui,width = 5,textvariable=stop).place(x= 700,y= 475)

    #make buttom nGui
    nbutton = Button(text = 'Summit',command = thank_you).place(x=300,y=530)
    nbutton2 = Button(text = 'Quit',command = out_1).place(x=400,y=530)

    #make name input
    nlabel6 = Label(nGui,text='Name',bg = '#464646',font = tkFont.Font(size = 15, weight=tkFont.NORMAL)).place(x=30, y=470)
    name = StringVar()
    name_data = Entry(nGui,width = 32,textvariable=name).place(x= 92 ,y=475)

    #make seat input
    nlabel3 = Label(nGui,text='Select seat amount',bg = '#464646',font = tkFont.Font(size = 15, weight=tkFont.NORMAL)).place(x=295, y=470)
    choose = StringVar()
    select = Entry(nGui,width = 5,textvariable=choose).place(x= 470, y=475)

    nGui.config(background = '#464646')


seat = []
def var_states(val):
    print "Select Seat: " + str(val.get())
    if len(seat) == 0:
        seat.append(val.get())
    else:
        if (val.get())[0] == seat[0][0]:
            seat.append(val.get())
        else:
            print 'Can not select different row'

def show_all():
    a = sorted(seat)
    print 'you selected seat ', a[0],' - ', a[-1]

def show_seat():
        seat_bg = Label(nGui,text = 'here')
        seat_bg.place(x=120 , y=120)

        seat_char = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in xrange(1,10):
            for j in xrange(9):
                var2 = StringVar()
                a = Checkbutton(nGui, text=seat_char[i]+str(j+1))
                a.config(variable=var2.set(seat_char[i]+str(j+1)))
                a.config(command = lambda v = var2: var_states(v))
                a.grid(row = i , column =j ,sticky= W)
'''

#-------------------------------Done----------------------------#

#make time select
time_button = []
line = []

class Home(Frame):
    """
    Create Home page for enable User choose movie and their show time
    """
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.home_page_template()
        self.time_select()
    movie_data = open('movie_name.txt', 'r')
    movie_name = dict( (i,j) for i,j in [map(lambda x=i[-3:]: x, i.split(',')) for i in movie_data.read().splitlines()])

    def selected(self, val):
        """show button value after press, and append to current select name "line" """
        print 'opening selected'
        line = []
        data = val
        date = 'date_'+strftime('%d/%m')+str(int(strftime('%Y'))+543)
        line.append(date)
        line.append(data[:4])
        line.append(data[-5:])
        print 'current select  ', line
        Label(text=self.movie_name[data[:3]][:12], fg='white', bg ='#464646',\
              font=tkFont.Font(size = 20, weight=tkFont.BOLD)).place(x=155, y=545)
        Label(text=data[:3], fg='white', bg ='#464646',\
              font='Angsna 9 italic').place(x=155, y=575)

        Label(text=data[-5:], fg='white', bg ='#464646', font=tkFont.Font(size = 20, weight=tkFont.BOLD)).place(x=445, y=545)

    def time_select(self):
        """read available times to declare buttons to listening when User pressed theirs"""
        time_data = open('time.txt', 'r')
        time = [map(lambda x: x, i.split()) for i in time_data]
        y = 100
        '''define default value and command for all button'''
        for i in xrange(len(time)):
            time_button.append([])
            for j in xrange(1, len(time[i])):
                val = time[i][0]+' '+str(time[i][j])
                temp = Button(self.home, text=str(time[i][j]))
                temp.config(command = lambda value=val: self.selected(value))
                time_button[i].append(temp)
        '''show button in frame'''
        for i in time_button:
            x = 440
            count = 0
            for j in i:
                if count == 5:
                    y += 35
                    x = 440
                j.place(x = x, y = y)
                x += 50
                count += 1
            if count > 5:
                y -= 35
            y += 110

    def home_page_template(self):
        self.home = Label(self,  width=800,height=600, bg='#464646').place(x=0, y=0)
        frame_1 = LabelFrame(self.home, width=800,height=600, bg='#464646')
        frame_1.place(x=0,y=0)

        #make buttom
        Button(frame_1, text = 'Submit').place(x=560, y=550)
        Button(frame_1, text = 'Quit', command=out).place(x=650, y=550)

        #make label
        Label(frame_1, text='BOX OFFICE', fg='white', bg = '#464646', font = tkFont.Font(size = 30)).place(x=50 ,y=10)
        Label(frame_1, text='Current Date :'+strftime('%d %B %Y'), bg = '#464646', fg='gray', font ='Angsna 9 italic').place(x= 300 ,y=15)
        Label(frame_1, text='Movies', fg='#2E8B57', bg = '#464646',  font = tkFont.Font(size = 10, weight=tkFont.BOLD)).place(x=175 ,y=60)
        Label(frame_1, text='Round Time', fg='#2E8B57',bg = '#464646',  font = tkFont.Font(size = 10, weight=tkFont.BOLD)).place(x=500 ,y=60)
        Label(frame_1, text='Current Movie :',bg = '#464646',  font = tkFont.Font(size = 15, weight=tkFont.NORMAL)).place(x=15 ,y=550)
        Label(frame_1, text='Round :',bg = '#464646',  font = tkFont.Font(size = 15, weight=tkFont.NORMAL)).place(x=365 ,y=550)

        #make Content

        pic_list = ["001.gif", "002.gif", "003.gif", "004.gif"]

        y, x = 95, 10 #Define content position here
        for i in xrange(4):
            Canvas(frame_1,height = 100,width= 270,bg = '#2E8B57').place(x=x+122, y=y)
            poster_pic = PhotoImage(file=pic_list[i])
            poster = Label(image=poster_pic)
            poster.image = poster_pic
            poster.place(x = x, y = y-10)
            Canvas(frame_1, height = 100,width= 270,bg = '#2E8B57').place(x=x+422, y=y)
            Label(frame_1, text=str('(Cinema '+str(int(pic_list[i][:3]))+')'), \
                  fg='white',bg='#2E8B57', font='angsna 9').place(x=x+165, y = y+35)
            Label(frame_1, text=str(self.movie_name[pic_list[i][:3]])[:25],\
                  fg='white',bg='#2E8B57', font='Helvetica 12 bold italic').place(x=x+165, y = y+10)

            y += 110

def out():
    if tkMessageBox.askyesno(title="Quit",message="Are You Sure"):
        quit()

def make_menu(frame):

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

    #make About menu
    menubar = Menu(frame)
    filemenu = Menu(menubar,tearoff = 0)
    filemenu.add_command(label='Creator', command = creator)
    filemenu.add_command(label='Thanks' , command = thanks)
    menubar.add_cascade(label="About Me",menu=filemenu)

    #make Help menu
    helpmenu = Menu(menubar,tearoff = 0)
    helpmenu.add_command(label='Help Docs', command = helpdocs)
    helpmenu.add_command(label='About', command = about)
    menubar.add_cascade(label="Help", menu=helpmenu)
    return menubar

def run_app(page):
    mGui = Tk()
    mGui.geometry('800x600+550+200')
    mGui.title('Theatre Manager')
    mGui.resizable(width=FALSE, height=FALSE)
    mGui.config(menu=make_menu(mGui))
    app = page(mGui)
    app.mainloop()
run_app(Home)
#-------------------------------Done----------------------------#
