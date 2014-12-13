from Tkinter import *
master = Tk()

seat = []
def var_states(val):
   print "Select Seat: " +str(val.get())
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

seat_char = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
seat_bg = Label(master)
seat_bg.pack()

for i in xrange(1,10):
   for j in xrange(10):
         var2 = StringVar()
         a = Checkbutton(seat_bg, text=seat_char[i]+str(i+j))
         a.config(variable=var2.set(seat_char[i]+str(i+j)))
         a.config(command = lambda v = var2: var_states(v))
         a.grid(row=i, column =j, sticky=W)
under = Label(master)
under.pack()
quit_but = Button(under, text='Quit', command=master.quit, width = 5,height = 3, wraplength=100,justify="center")
quit_but.grid(row = 10,column=2)
show_but = Button(under, text='Show', command=show_all,width = 5,height = 3)
show_but.grid(row = 10, column = 0)
master.title("Seat Select")
master.geometry("500x300")
mainloop()
