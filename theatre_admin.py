'''
Administrator Part
- Show box office detail
- Show summarized income
- Show seat deatail
'''
from Tkinter import *
from time import *
import sys

class Theatre:
    '''
    Represent frame of theatre manager
    '''

    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x500")
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.title("Theatre Manager")

        def template():
            '''header part'''
            header_pic = PhotoImage(file = "logo.gif")
            header = Label(image = header_pic)
            header.image = header_pic # keep a reference!
            header.place(x = 0, y = 0)

            '''stat part'''
            stat_pic = PhotoImage(file = "stat.gif")
            stat = Label(image = stat_pic)
            stat.image = stat_pic # keep a reference!
            stat.place(x = 15, y = 238)

            '''round time'''
            time_pic = PhotoImage(file = "time.gif")
            time = Label(image = time_pic)
            time.image = time_pic # keep a reference!
            time.place(x = 438, y = 250)


            self.update_time()

        template()
        
        self.button_inframe()
        self.show_detail_list()
        self.show_overview()
        self.round_manage()


        mainloop()

    def update_time(self):
        '''show last update time'''
        Label(self.root, bg='white', text=strftime('Last update : %A %d %B %Y')).place(x = 310, y = 5)

    f_data = open('data.txt', 'r')
    data = [map(lambda x: x,i.split()) for i in f_data]

    def button_inframe(self):
        ''' show all button'''
        Button(self.root, text = 'Update', command=self.edit_time)\
        .place(x = 550, y = 460, width = 50, height = 20) #Update
        Button(self.root, text = 'Close', command = quit)\
        .place(x = 690, y = 460, width = 50, height = 20)  #Close program
        Button(self.root, text = 'Detail').\
        place(x = 620, y = 460, width = 50, height = 20) #Description of frame composition

    def show_detail_list(self):
        """ show list of data and detail (included date,movie,time,name,amout, price ,seat)"""
        y, num = 90, len(self.data)
        data =  self.data
        data.reverse()
        for i in data[-num:-(num-7)]:
            seat = str(i[6][:2] + ' - ' + i[6][2:])
            time = i[1]
            name = i[3].capitalize()
            line = '{0:12}{1:40}{2:30}{3:30}{4:35}{5:12}{6:20}{7:20}'.format(str(num)+'.', i[0][5:15], i[1], i[2], name, str(int(i[4])), i[5], seat)
            Label(self.root, bg='black', fg='#00be8f', text=line).place(x = 5, y = y)
            y += 20
            num -= 1

    def show_overview(self):
        stat_pic = PhotoImage(file = "stat.gif")

        total_seat = ' Audience : ' + str(sum([int(x[4]) for x in self.data]))
        total_income = 'Income : ' + str(sum([int(x[5]) for x in self.data]))

        Label(self.root, fg='blue', text='Statistic').place(x = 50, y = 250)
        Label(self.root, bg='#00be8f', text='Max audience  Cinema : -     Movie : -').place(x = 30, y = 280)
        Label(self.root, bg='#00be8f', text='Most of week  :').place(x = 40, y = 300)
        Label(self.root, bg='#00be8f', text='Most of month  :').place(x = 40, y = 320)

        Label(self.root, bg='#00be8f', text='Total sold ticket '+'_'*30).place(x = 30, y = 340)
        Label(self.root, bg='#00be8f', text='In week  :').place(x = 40, y = 360)
        Label(self.root, bg='#00be8f', text='In month  :').place(x = 40, y = 380)

        Label(self.root, fg='blue', text=' Present day stat ').place(x = 52, y = 410)
        Label(self.root, bg='#00be8f', text=total_seat).place(x = 30, y = 430)
        Label(self.root, bg='#00be8f', text=total_income).place(x = 150, y = 430)

    var_list = []
    chkbut_list = []
    time = ['10.45', '11.30', '12.15', '13.00', '13.45', '14.30', '15.15']

    def show_current_time(self):
        """
        Show checkbutton box state
        and Box values in console
        """
        y = 280
        for i in xrange(len(self.chkbut_list)):
            x = 495
            for j in xrange(len(self.chkbut_list[i])):
                print self.var_list[i][j].get(),
                self.chkbut_list[i][j].place(x=x, y=y)
                x += 45
            print ''
            y += 25

    def round_manage(self):

        '''
        Declare Value of Check button
        Enable/Disable time for each cinema
        '''
        time,y = self.time, 280

        Label(self.root, fg='blue', text='Cinema').place(x = 580, y = 235)
        Label(self.root, text='Time').place(x = 450, y = 255)

        time_data = open('time.txt', 'r')
        show_time = [map(lambda x: x,i.split()) for i in time_data]

        for j in xrange(6):
            Label(self.root, text=str(j+1)).place(x = (500+(j*45)), y = 260)

        var_list = self.var_list
        chkbut_list = self.chkbut_list
        for i in xrange(7):
            var_list.append([])
            chkbut_list.append([])
            Label(self.root, text=time[i]).place(x = 450, y = y)
            #x = 450
            for j in xrange(len(show_time)):
                #x += 45
                var = IntVar()
                var_list[i].append(var)
                if time[i] in show_time[j]:
                    var_list[i][j].set(1)
                else :
                    var_list[i][j].set(0)
                check_but = Checkbutton(self.root, variable=var)
                chkbut_list[i].append(check_but)
            y += 25

    def edit_time(self):
        """read and write new edit showtime"""
        self.show_current_time()
        time = self.time
        time_data = open('time.txt', 'r+')
        show_time = [map(lambda x: x,i.split()) for i in time_data]
        cmp_time = [list(x) for x in zip(*self.var_list)]

        new_time = []
        for i in xrange(len(cmp_time)):
            new_time.append([])
            for j in xrange(len(cmp_time[i])):
                if cmp_time[i][j].get():
                    new_time[i].append(time[j])

        for i in new_time:
            print i










Theatre()

