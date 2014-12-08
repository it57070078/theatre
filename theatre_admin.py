'''
Administrator Part
- Show box office detail
- Show summarized income
- Show seat deatail
'''
from Tkinter import *
from time import *
import sys

class Frame(object):
    '''
    Represent frame of theatre manager
    '''
    def __init__(self):               
        self.root = Tk()
        self.root.geometry("800x500")
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.title("Theatre Manager")
        self.photo = PhotoImage(file = "logo2.gif")
        self.label = Label(image = self.photo)
        self.label.image = self.photo # keep a reference!
        self.label.place(x = 0, y = 0)
        '''show last update time'''
        Label(self.root, bg='white', text=strftime('Last update : %A %d %B %Y')).place(x = 310, y = 5)

        day = IntVar()
        month = IntVar()
        year = IntVar()
        f_data = open('data.txt', 'r')
        data = [map(lambda x: x,i.split()) for i in f_data]

        ''' show all button'''
        def button_inframe():
            Button(self.root, text = 'Update')\
            .place(x = 620, y = 460, width = 50, height = 20) #Update
            Button(self.root, text = 'Close', command = quit)\
            .place(x = 740, y = 460, width = 50, height = 20)  #Close program
            Button(self.root, text = 'Detail').\
            place(x = 680, y = 460, width = 50, height = 20) #Description of frame composition
        def show_detail_list(data):
            y, num = 90, 1
            for i in data[-10:]:
                line = str(num)+(' '*10)
                line += i[0][5:15].center(12) + i[1].rjust(30) + i[2].rjust(30)
                line += (' '*20) + i[3].ljust(40)
                line += (' '*10) + str(int(i[4])) + i[5].center(50)
                line += str(i[6][:2] + ' - ' + i[6][2:])
                Label(self.root, text=line).place(x = 5, y = y)
                y += 20
                num += 1
        def show_detail_total(data):
            total_seat = 'Total audience : ' + str(sum([int(x[4]) for x in data]))
            total_income = 'Total income : ' + str(sum([int(x[5]) for x in data]))
            Label(self.root, text=total_seat).place(x = 5, y = 440)
            Label(self.root, text=total_income).place(x = 150, y = 440)    
        button_inframe()
        show_detail_list(data)
        show_detail_total(data)
        self.root.mainloop()
#--------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    Frame()
