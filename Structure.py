__author__ = 'mark_ts'
import random
import tkMessageBox
from Tkinter import *
class App:
    def __init__(self, master):
        class_room = Button(text = "Class Room", command = self.class_arrange)
        exam_room = Button(text = "Exam Room", command = self.exam_arrange)

        class_room.grid(padx = 10, pady = 10, row = 0, column = 0)
        exam_room.grid(padx = 10, pady = 10, row = 0, column = 1)

    def class_arrange(self):
        self.top = Toplevel() #set new window

        self.num_of_stu = StringVar(value=1) #input number of student(int value)

        Label(self.top, text = "Number of \nStudent :").grid(padx = 5, pady = 5, row = 0, column = 0)
        Entry(self.top, textvariable = self.num_of_stu, width = 5).grid(padx = 5, pady = 5, row = 0, column = 1) #Empty for input

        self.button = Button(self.top, text="Submit", command=self.slot)
        self.button.grid(padx=5, pady=5, row=0, column=2)

    def exam_arrange(self):
        self.windows = Toplevel()
        self.windows.maxsize(width = 300, height = 418)
        self.num_of_stu = StringVar(value=1)
        self.width = StringVar(value=1)
        self.height = StringVar(value=1)
        Label(self.windows, text="Number of Student :").grid(padx=5, pady=5, row=0, column=0)
        Entry(self.windows, textvariable=self.num_of_stu, width = 5).grid(padx=5, pady=5, row=0, column=1)

        Label(self.windows, text="Width x Height").grid(padx=5, pady=5, row=1, column=0)
        Entry(self.windows, textvariable=self.width, width=5).grid(padx=5, pady=5, row=1, column=1)
        Label(self.windows, text="x").grid(padx=5, pady=5, row=1, column=2)
        Entry(self.windows, textvariable=self.height, width=5).grid(padx=5, pady=5, row=1, column=3)
        Button(self.windows, text="Proceed", command=self.exam_selection).grid(padx=5, pady=5, row=2, column=3)

        self.text = Text(self.windows, width = 40, height = 10, wrap = NONE)
        self.text.grid(padx=3, pady=3, row=3, column=0, columnspan = 4)
    def slot(self):
        #self.button.config(state=DISABLED)... >> BUG
        try:
            int(self.num_of_stu.get())
            self.num = []
            self.grade = []
            Label(self.top, text=" ").grid(padx=10, pady=10, row=1, column=0)
            Label(self.top, text="No.", width=5).grid(padx=10, pady=10, row=1, column=1)
            proceed = Button(self.top, text="Proceed", command=self.selection)
            Label(self.top, text="Grade", width=5).grid(padx=10, pady=10, row=1, column=2)
            for i in xrange(int(self.num_of_stu.get())):
                self.num.append("No" + str(i))
                self.grade.append("Grade" + str(i))

            for j in xrange(len(self.num)):
                self.num[j] = StringVar(value=j+1)
                self.grade[j] = StringVar(value=0.0)

                if j > 9:
                    Label(self.top, text=j+1, width=5).grid(padx=10, pady=5, row=2+j%10, column=2+(3*(j/10)-2))
                    Entry(self.top, textvariable=self.num[j], width=5).grid(padx=10, pady=5, row=2+j%10, column=3+(3*(j/10)-2))
                    Entry(self.top, textvariable=self.grade[j], width=5).grid(padx=10, pady=5, row=2+j%10, column=4+(3*(j/10)-2))
                    proceed.grid(row=len(self.num)+2, column=4+(3*(j/10)-2), padx=20, pady=15)
                else:
                    Label(self.top, text=j+1, width=5).grid(padx=10, pady=5, row=2+j, column=0)
                    Entry(self.top, textvariable=self.num[j], width=5).grid(padx=10, pady=5, row=2+j, column=1)
                    Entry(self.top, textvariable=self.grade[j], width=5).grid(padx=10, pady=5, row=2+j, column=2)
                    proceed.grid(row=len(self.num)+2, column=2, padx=20, pady=15)

            self.button.config(state='disabled')
        except:
            tkMessageBox.showerror(title='Input error', message='Input must be number')

    def selection(self):
        try:
            for i in xrange(len(self.num)):
                int(self.num[i].get())
                float(self.grade[i].get())
            self.topend = Toplevel()
            new_num = [int(i.get()) for i in self.num]
            new_grade = [float(j.get()) for j in self.grade]
            select_dict = {}
            output_list = []
            printer = ""
            for i in xrange(len(new_num)):
                select_dict[new_num[i]] = new_grade[i]

            for i in xrange(len(new_num) / 2):
                for i in select_dict:
                    if select_dict[i] == max(select_dict.values()):
                        stu_1 = i
                        select_dict.pop(i)
                        break
                for i in select_dict:
                    if select_dict[i] == min(select_dict.values()):
                        stu_2 = i
                        select_dict.pop(i)
                        break
                output_list.append([stu_1, stu_2])
            if select_dict != {}:
                num, grade = select_dict.popitem()
                if len(output_list) == 0:
                    output_list.append([num])
                else:
                    output_list[-1].append(num)
            for i in output_list:
                printer += str(i) + "\n"
            print printer
            self.text = Text(self.topend, width = 40, height = 10, wrap = NONE)
            self.text.grid(padx=3, pady=3, row=3, column=0, columnspan = 4)
            self.text.delete(0.0, END)
            self.text.insert(0.0, printer)
        except:
            tkMessageBox.showerror(title='Input Error', message='Input must be number')
    def exam_selection(self):
        try:
            num_stu = int(self.num_of_stu.get())
            data = []
            width = int(self.width.get())
            height = int(self.height.get())
            if width * height < num_stu:
                return None
            else:
                printer = ""
                counter = 0
                for i in xrange(num_stu):
                    data.append(i + 1)
                for i in xrange(height):
                    if counter > num_stu - 1:
                        break
                    for j in xrange(width):
                        if counter > num_stu - 1:
                            break
                        num = random.choice(data)
                        printer += [str(num), "0" + str(num)][len(str(num)) == 1] + [" ", "\n"][j == width - 1]
                        data.remove(num)
                        counter += 1
                self.text.delete(0.0, END)
                self.text.insert(0.0, printer)
        except:
            tkMessageBox.showerror(title='Input error', message='Input must be number')

root = Tk()
app = App(root)
root.mainloop()