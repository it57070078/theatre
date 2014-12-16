import sys
from Tkinter import *
from time import *
import tkMessageBox
import tkFont
import ttk

#make time select
time_button = []
seat_button = []
seat = []
pic_list = ["001.gif", "002.gif", "003.gif", "004.gif"]
pic_dict = dict((i[:3],i) for i in pic_list)

class Home(Frame):
    """
    Create Home page for enable User choose movie and their show time
    """
    def __init__(self, master=None):
        self.content[:] = []
        Frame.__init__(self, master)
        self.home = Label(self,  width=800,height=600, bg='#464646').place(x=0, y=0)
        self.frame = LabelFrame(self.home, width=800,height=600, bg='#464646')
        self.home_page_template()
        self.time_select(self.frame)

    movie_data = open('movie_name.txt', 'r')
    movie_name = dict((i, j) for i, j in [map(lambda x=i[-3:]: x, i.split(',')) for i in movie_data.read().splitlines()])

    line = []
    def selected(self, val):
        """show button value after press, and append to current select name "line" """
        print 'opening selected'
        self.line = []
        line = self.line
        data = val
        date = 'date_'+strftime('%d/%m/')+str(int(strftime('%Y'))+543)

        line.append(date)
        line.append(data[:3])
        line.append(data[-5:])
        print 'current select  ', line
        Label(text=self.movie_name[data[:3]][:12], fg='white', bg ='#464646',\
              font=tkFont.Font(size = 20, weight=tkFont.BOLD)).place(x=155, y=545)
        Label(text=data[:3], fg='white', bg ='#464646',\
              font='Angsna 9 italic').place(x=155, y=575)

        Label(text=data[-5:], fg='white', bg ='#464646', font=tkFont.Font(size = 20, weight=tkFont.BOLD)).place(x=445, y=545)

        self.SUBMIT.config(state='normal')

    def time_select(self, frame_1):
        """read available times to declare buttons to listening when User pressed theirs"""
        time_data = open('time.txt', 'r')
        time = [map(lambda x: x, i.split()) for i in time_data]

        #showtime_bg = Label(frame_1, width=100)
        #showtime_bg.place(x=440, y =100)

        for i in self.content:
            print self.content

        '''define default value and command for all button'''
        for i in xrange(len(time)):
            time_button.append([])
            for j in xrange(1, len(time[i])):
                val = time[i][0]+' '+str(time[i][j])
                temp = Button(self.content[i], text=str(time[i][j]), bg = 'black', fg='#2E8B57', width=6, font='Helvetica 10 bold italic')
                temp.config(command = lambda value=val: self.selected(value))
                time_button[i].append(temp)

        '''show button in frame'''
        y = 5
        for i in time_button:
            x , y, count = 5, 5, 0
            for j in i:
                if count == 4:
                    x = 5
                    y += 35
                j.place(x=x, y=y)
                x += 60
                count += 1



    def seat_part(self):
        self.home = Label(self,  width=800,height=600, bg='#464646').place(x=0, y=0)

        pic = PhotoImage(file='seat_bg.gif')
        poster = Label(image=pic)
        poster.image = pic
        poster.place(x=0, y=55)

        frame_2 = LabelFrame(self.home, width=400,height=400, bg='#464646')
        frame_2.place(x=80,y=150)
        frame_3 = LabelFrame(self.home, width=100, bg='#464646')
        frame_3.place(x=520,y=150)
        frame_4 = LabelFrame(self.home, width=100, bg='red')
        frame_4.place(x=80,y=650)

        seat_bg = Label(frame_2,text = 'here',bg='#464646')
        seat_bg.pack()

        #make name input
        nlabel6 = Label(frame_3,text='Please fill your name',bg = '#464646', fg = 'gray',font='Helvetica 10 italic').pack()

        self.name = StringVar()
        name_data = Entry(frame_3, width = 32, justify='center', textvariable=self.name)
        name_data.pack()


        #make seat input
        Label(frame_3,text='Selected seat',bg = '#464646', fg='gray', font='Helvetica 10 italic').pack()

        self.current_seat = Label(frame_3, text ='-- check some available seat --', width=24, font='Angsna 10 italic', fg='blue')
        self.current_seat.pack()
        butt_bar = Label(frame_3, bg = '#464646')
        butt_bar.pack()

        #make buttom nGui
        def back():
            frame_2.place_forget()
            frame_3.place_forget()
            frame_4.place_forget()
            poster.place_forget()
            seat_bg.place_forget()

            seat[:] = []
            self.order = 'refresh'
            self.__init__()

        def send_data():
            price = 80
            # define ticket cost here
            if len(self.name.get()) != 0:
                self.line.append(str(self.name.get()))
            else:
                self.line.append('-Anonymous-')
            qty = len(seat)
            self.line.append(str(qty).zfill(2))
            self.line.append(str(qty*price))
            self.line.append(str(seat[0]+' - '+seat[-1]))
            self.line[2] = self.line[2][:2]+' : '+self.line[2][-2:]
            print self.line
            data = ' '.join(self.line)
            print data
            if tkMessageBox.askyesno(title="Confirm", message="Your ticket is \n  "+self.line[0]+\
                    '\n Movie     : '+ self.movie_name[self.line[1]]+\
                    '\n Show Time : '+ self.line[2]+\
                    '\n Customer  : '+ self.line[3]+ \
                    '\n Amount    : '+ self.line[4]+ \
                    '\n Price     : '+ self.line[5]+' Bath'+ \
                    '\n Seat No.  : '+ self.line[6]):
                data_list = open('data.txt', 'a+')
                data_list.writelines(data)
                tkMessageBox.showinfo(title='Success!', message='Saved\nYour ticket is available')
                data_list.close()
            else :
                self.line[:] = []
                seat[:] = []
                print self.line
            back()

        def clear_all():
            if len(seat):
                for i in seat_button:
                    i.deselect()
                self.current_seat.config(text='-- check some available seat --')
                seat[:] = []
                print seat

            else:
                pass
        # Create option bar contain button and thumbnail
        thumb = PhotoImage(file=pic_dict[self.line[1]])
        thumbnail = Label(butt_bar, image=thumb)
        thumbnail.image = thumb
        thumbnail.grid(row=0)
        Label(butt_bar, text='Option',bg = '#464646', fg='gray', font='Helvetica 10 italic').grid(row=1)
        Button(butt_bar, text='Submit', width=21, command=send_data).grid()
        Button(butt_bar, text='New movie', width=21, command =back).grid()
        Button(butt_bar, text='Clear', width=21, command=clear_all).grid()



        def var_states(val, but):
            def cleared(text):
                tkMessageBox.showinfo(title='Sorry', message=text+'\n Try again please...')
                but.deselect()
                clear_all()
                print 'cleared'

            print "Select Seat: " + str(val.get())
            if len(seat) == 0:
                seat.append(val.get())
                self.current_seat.config(text=seat[0])
                self.left, self.right = int(val.get()[1])-1, int(val.get()[1])+1
            else:
                print seat[-1],
                self.left, self.right = int(seat[-1][1])-1, int(seat[-1][1])+2

                if int((val.get())[1]) in xrange(self.left, self.right) and (val.get())[0] == seat[0][0]:
                    seat.append(val.get())
                    self.current_seat.config(text=str(seat[0]+' - '+seat[-1]))
                elif int((val.get())[1]) not in xrange(self.left, self.right):
                    cleared('You can not put space between your seat')
                elif (val.get())[0] != seat[0][0]:
                    cleared('You can not select different row')
                else:
                    cleared('Unknow type error')

            print 'you can select left', self.left, 'right', self.right


        seat_char = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        booked = [i[2] for i in self.check_booked() if i[0] == self.line[1] and i[1] == self.line[2]]

        for i in xrange(1, 13):
            for j in xrange(9):
                var2 = StringVar()
                chkbut = Checkbutton(seat_bg, text=seat_char[i]+str(j+1), bg='#464646',)
                chkbut.config(variable=var2.set(seat_char[i]+str(j+1)))
                chkbut.config(command=lambda v=var2, but=chkbut: var_states(v, but))
                chkbut.grid(row=i, column=j)
                if len(booked) > 0:
                    if booked[0][0] == seat_char[i] and j in xrange(int(booked[0][1])-1, int(booked[0][3])+1):
                        chkbut.select()
                        chkbut.config(state='disabled')
                        if j >= int(booked[0][3]):
                            del booked[0]
                seat_button.append(chkbut)

    content = []

    def check_booked(self):
        '''check booked seat'''
        seat_file = open("data.txt", 'r')
        today = 'date_'+strftime('%d/%m/')+str(int(strftime('%Y'))+543)
        booked_all = [j for j in [map(lambda x: x, i.split()) for i in seat_file.read().splitlines()]]
        booked = [[x[1], x[2][:2]+'.'+x[2][-2:], x[6]] for x in booked_all if x[0] == today]
        seat_file.close()
        print booked
        return booked

    def home_page_template(self):
        frame_1 = self.frame
        frame_1.place(x=0, y=0)
        def close_frame(frame):
            frame.place_forget()
            self.seat_part()

        #make buttom
        self.SUBMIT = Button(frame_1, text = 'Submit', state='disabled', command=lambda frame=frame_1:close_frame(frame))
        self.SUBMIT.place(x=560, y=550)
        Button(self.home, text = 'Quit', command=out).place(x=650, y=550)

        #make label
        Label(self.home, text='BOX OFFICE', fg='white', bg = '#464646', font = tkFont.Font(size = 30)).place(x=50 ,y=10)
        Label(self.home, text='Current Date :'+strftime('%d %B %Y'), bg = '#464646', fg='gray', font ='Angsna 9 italic').place(x= 300 ,y=15)
        Label(frame_1, text='Movies', fg='#2E8B57', bg = '#464646',  font = tkFont.Font(size = 10, weight=tkFont.BOLD)).place(x=175 ,y=60)
        Label(frame_1, text='Round Time', fg='#2E8B57',bg = '#464646',  font = tkFont.Font(size = 10, weight=tkFont.BOLD)).place(x=500 ,y=60)
        Label(frame_1, text='Current Movie :',bg = '#464646',  font = tkFont.Font(size = 15, weight=tkFont.NORMAL)).place(x=15 ,y=550)
        Label(frame_1, text='Round :',bg = '#464646',  font = tkFont.Font(size = 15, weight=tkFont.NORMAL)).place(x=365 ,y=550)

        #make Content


        y, x = 95, 10 #Define content position here
        for i in xrange(4):
            Canvas(frame_1,height = 100,width= 270,bg = '#2E8B57').place(x=x+122, y=y)
            poster_pic = PhotoImage(file=pic_list[i])
            poster = Label(frame_1, image=poster_pic)
            poster.image = poster_pic
            poster.place(x = x, y = y-10)
            show_time = Canvas(frame_1, height = 100,width= 270,bg = '#2E8B57')
            show_time.place(x=x+422, y=y)
            self.content.append(show_time)
            Label(frame_1, text=str('(Cinema '+str(int(pic_list[i][:3]))+')'), \
                  fg='white',bg='#2E8B57', font='angsna 9').place(x=x+165, y = y+35)
            Label(frame_1, text=str(self.movie_name[pic_list[i][:3]])[:25],\
                  fg='white',bg='#2E8B57', font='Helvetica 12 bold italic').place(x=x+165, y = y+10)
            y += 110

        return frame_1


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

def run_app():
    page = Home
    mGui = Tk()
    mGui.geometry('800x600+550+200')
    mGui.title('Theatre Manager')
    mGui.resizable(width=FALSE, height=FALSE)
    mGui.config(menu=make_menu(mGui))
    app = page(mGui)
    app.mainloop()
run_app()
#-------------------------------Done----------------------------#
