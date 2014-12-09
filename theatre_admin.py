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
        Button(self.root, text = 'Update')\
        .place(x = 550, y = 460, width = 50, height = 20) #Update
        Button(self.root, text = 'Close', command = quit)\
        .place(x = 690, y = 460, width = 50, height = 20)  #Close program
        Button(self.root, text = 'Detail').\
        place(x = 620, y = 460, width = 50, height = 20) #Description of frame composition

    def show_detail_list(self):
        """ show list of data and detail (included date,movie,time,name,amout, price ,seat)"""
        y, num = 90, len(self.data)
        for i in self.data[-10:]:
            line = str(num)+'.'+(' '*10)
            line += i[0][5:15].center(12) + i[1].rjust(30) + i[2].rjust(30)
            line += (' '*20) + i[3].ljust(40)
            line += (' '*10) + str(int(i[4])) + i[5].center(50)
            line += str(i[6][:2] + ' - ' + i[6][2:])
            Label(self.root, bg='black', fg='#00be8f', text=line).place(x = 5, y = y)
            y += 20
            num -= 1

    def show_overview(self):
        stat_pic = PhotoImage(file = "stat.gif")

        total_seat = ' Audience : ' + str(sum([int(x[4]) for x in self.data]))
        total_income = 'Income : ' + str(sum([int(x[5]) for x in self.data]))

        Label(self.root, fg='blue', text='Statistic').place(x = 50, y = 250)
        Label(self.root, bg='#00be8f', text='Max audience  Cinema : -     Movie : -').place(x = 30, y = 280)
        Label(self.root, bg='#00be8f', text='Most of week : - ').place(x = 30, y = 300)
        Label(self.root, bg='#00be8f', text='Most of month : - ').place(x = 30, y = 320)

        Label(self.root, bg='#00be8f', text='Snack : - $   Drink : - $').place(x = 30, y = 340)
        Label(self.root, bg='#00be8f', text='Total sold ticket in week : ').place(x = 30, y = 360)
        Label(self.root, bg='#00be8f', text='Total sold ticket in month : ').place(x = 30, y = 380)

        Label(self.root, fg='blue', text=' Present day stat ').place(x = 52, y = 410)
        Label(self.root, bg='#00be8f', text=total_seat).place(x = 30, y = 430)
        Label(self.root, bg='#00be8f', text=total_income).place(x = 150, y = 430)

    def round_manage(self):
        '''Enable/Disable time for each cinema'''
        y,time = 280, ['10.45', '11.30', '12.15', '13.00', '13.45', '14.30', '15.15']
        Label(self.root, fg='blue', text='Cinema').place(x = 580, y = 235)
        Label(self.root, text='Time').place(x = 450, y = 255)

        for j in xrange(6):
            Label(self.root, text=str(j+1)).place(x = (500+(j*45)), y = 260)

        for i in xrange(7):
            Label(self.root, text=time[i]).place(x = 450, y = y)
            x = 450
            for i in xrange(6):
                x += 45
                Checkbutton(self.root).place(x = x, y = y)
            y += 25



Theatre()

