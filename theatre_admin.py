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

            self.update_date()

        template()

        self.round_manage()
        self.button_inframe()
        self.show_detail_list()
        self.show_overview()
        self.show_current_time('show')

        mainloop()


    def update_date(self):
        '''show last update time'''
        Label(self.root, bg='white', text=strftime('Last update : %A %d %B %Y')).place(x = 310, y = 5)

    f_data = open('data.txt', 'r')
    data = [map(lambda x: x,i.split()) for i in f_data]
    #[(date_12/12/2557), (001),(1045),(K.Guide),(01),(80),(D1D1)]
    #------0----------------1-----2------3--------4----5-----6---

    def button_inframe(self):
        ''' show all button'''

        close_butt = Button(self.root, text = 'Close', command = quit)
        close_butt.place(x = 690, y = 460, width = 50, height = 20)  #Close program
        self.button_list.append(close_butt)

        detail_but = Button(self.root, text = 'Detail')
        detail_but.place(x = 620, y = 460, width = 50, height = 20) #Description of frame composition
        self.button_list.append(detail_but)

        edit_but = Button(self.root, text = 'Edit' , command=self.edit_time)
        edit_but.place(x = 440, y = 460, width = 50, height = 20) #Open Edit mode
        self.button_list.append(edit_but)

        update_butt = Button(self.root, text = 'Update' , command=self.save_setting)
        self.button_list.append(update_butt)

    def show_detail_list(self,bg_color = 'black'):
        """ show list of data and detail (included date,movie,time,name,amout, price ,seat)"""
        y, num = 90, len(self.data)
        data =  self.data
        data.reverse()
        for i in data[-num:-(num-7)]:
            text = '#00be8f'
            seat = str(i[6][:2] + ' - ' + i[6][2:])
            time = i[1]
            name = i[3][:20].capitalize()
            line = ((str(num)+'.'), i[0][5:15], i[1], i[2], name, str(int(i[4])), i[5], seat)
            line1 = '{0[0]:<12}{0[1]:<40}{0[2]:<30}{0[3]:<20}{0[4]:^40}'.format(line)
            line2 = '{0[5]:<15}{0[6]:^30}{0[7]:^25}'.format(line)
            txt1 = Label(self.root, bg=bg_color, fg=text, text=line1)
            txt1.place(x = 5, y = y)
            txt2 = Label(self.root, bg=bg_color, fg=text, text=line2, width=40)
            txt2.place(x = 500, y = y)
            y += 20
            num -= 1

    def show_overview(self):
        print 'opening show_overview()'
        stat_pic = PhotoImage(file = "stat.gif")
        data = self.data
        date = self.map_date()
        result = self.analysis_data(date)
        total_seat = ' Audience : ' + str(result['audience'])
        total_income = 'Income : ' + str(result['income'])

        Label(self.root, fg='blue', text='Statistic').place(x = 50, y = 250)
        Label(self.root, bg='#00be8f', text='Max audience  Cinema : -     Movie : -').place(x = 30, y = 280)
        Label(self.root, bg='#00be8f', text='Most of week  :  '+str(result['most_week'])).place(x = 40, y = 300)
        Label(self.root, bg='#00be8f', text='Most of month  :  '+str(result['most_month'])).place(x = 40, y = 320)

        Label(self.root, bg='#00be8f', text='Total sold ticket '+'_'*30).place(x = 30, y = 340)
        Label(self.root, bg='#00be8f', text='In week  :').place(x = 40, y = 360)
        Label(self.root, bg='#00be8f', text='In month  :').place(x = 40, y = 380)

        Label(self.root, fg='blue', text=' Present day stat ').place(x = 52, y = 410)
        Label(self.root, bg='#00be8f', text=total_seat).place(x = 30, y = 430)
        Label(self.root, bg='#00be8f', text=total_income).place(x = 150, y = 430)

    def map_date(self):
        tran_int = lambda alist : map(int,alist)
        date = [tran_int(x[0][5:15].split('/')) for x in self.data]
        return date

    def analysis_data(self, date):
        result = dict()
        date_now = (int(strftime('%d')), int(strftime('%m')), int(strftime('%Y'))+543)
        day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        result['audience'] = sum(map(int, [x[4] for x in self.data]))
        result['income'] = sum(map(int, [x[5] for x in self.data]))
        week, month = [], []
        if date_now[0] > 7:
            for i in xrange(len(self.data)):
                if date[i][0] > 1 and date[i][1] == date_now[1]:
                    month.append(self.data[i])
                if date[i][0] > date_now[0]-7:
                    week.append(self.data[i])
        else :
            for i in xrange(len(self.data)):
                if date[i][1] >= date_now[1] - 1:
                    if date[i][0] <= date_now[0] and date[i][1] == date_now[1]:
                        month.append(self.data[i])
                    elif date[i][0] > date_now[0] and date[i][1] == date_now[1]-1:
                        month.append(self.data[i])





        for i in month:
            print i

        #most of week
        result['most_week'] = max([x[1] for x in self.data[-7:]])
        #most of month
        result['most_month'] = max([x[1] for x in month])

        #total sold in week
        ##result['total_week'] = sum([x[4] for x in self.data[-7:]])

        #total sold in month
        ##result['total_month'] = sum([x[4] for x in month])

        return result # dict of stat , for show in overview part

    button_list = []
    var_list = []
    chkbut_list = []
    time = ['10.45', '11.30', '12.15', '13.00', '13.45', '14.30', '15.15']


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

    def show_current_time(self, order):
        """
        Show checkbutton box state
        and Box values in console
        """
        print 'Opening function show_current_time() as '+str(order)+' mode'
        status = ['disabled', 'normal'][order == 'edit']

        edit_but = self.button_list[2]
        if status == 'disabled':
            edit_but.config(state='normal')
        else :
            edit_but.config(state='disable')
        y = 280
        for i in xrange(len(self.chkbut_list)):
            x = 495
            for j in xrange(len(self.chkbut_list[i])):
                #print self.var_list[i][j].get(), #for check current values of each checkboxes button
                self.chkbut_list[i][j].config(state=status)
                self.chkbut_list[i][j].place(x=x, y=y)
                x += 45
            #print ''
            y += 25

    def edit_time(self):
        """read and write new edit showtime"""
        print 'Opening function edit_time()'
        self.show_current_time('edit')
        update_butt = self.button_list[3]
        update_butt.place(x = 550, y = 460, width = 50, height = 20) #Update

    def save_setting(self):
        """"saved new setting"""
        update_butt = self.button_list[3]
        update_butt.place_forget()
        self.show_current_time('show')
        for i in self.button_list:
            print i
        print 'saved new setting'
        time = self.time
        time_data = open('time.txt', 'r')
        serial = [i[:3] for i in time_data]
        time_data.close()
        time_data = open('time.txt', 'wt')
        cmp_time = [list(x) for x in zip(*self.var_list)]

        new_time = []

        for i in xrange(len(cmp_time)):
            new_time.append([])
            for j in xrange(len(cmp_time[i])):
                 if cmp_time[i][j].get():
                    new_time[i].append(time[j])
        print 'Current setting is ...'
        for i in xrange(len(new_time)):
            print serial[i], ' '.join(new_time[i])
            time_data.write(str(str(serial[i])+' '+ ' '.join(new_time[i]))+'\n')

Theatre()

