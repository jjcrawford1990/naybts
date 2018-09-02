#import full tkinter module
from tkinter import *
import tkinter as tk
#import calibration data from calibration.py
import calibration

#default background colour
dbg = '#334157'
#default fg colours (font colour)
dfg = 'silver'
dfg2 = 'white'
#default fonts
dfont = 'courier 9 bold underline'
dfont2 = 'courier 9'



#generate main window class and populate with windows and buttons
    
class Proj_select(tk.Frame):
    
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.grid()
        self.configure_gui()

    def configure_gui(self):
        self.master.title('NAY Brakes Testing System')
        self.master.geometry('800x415')
        self.master.configure(bg=dbg)
        self.user_choice()

    def user_choice(self):
        self.no_cars = IntVar()
        project = StringVar()
        self.frame2 = Frame(self.master) #frame2 is generated within object (proj_select)
        self.frame2.grid(row=0, column=0)
        selectone = Label(self.frame2, text='Selection:',).grid(row=1, column=0, columnspan=1)
        selectiona = Radiobutton(self.frame2, text='IEP-5 (GWML)', variable=self.no_cars, value=5)
        selectiona.grid(row=1, column=1)
        selectionb = Radiobutton(self.frame2, text='IEP-9 (GWML)', variable=self.no_cars, value=9)
        selectionb.grid(row=2, column=1)
        selectionc = Radiobutton(self.frame2, text='ASR-3 (Abellio)', variable=self.no_cars, value=3)
        selectionc.grid(row=3, column=1)
        selectiond = Radiobutton(self.frame2, text='ASR-4 (Abellio)', variable=self.no_cars, value=4)
        selectiond.grid(row=4, column=1)
        setselection = Button(self.frame2, text='Set!', command=self.frame_set) #to run method for index creation
        setselection.grid(row=5, column=0, columnspan=2)

    #method definition of which project shall be ran, then calls the suitable method
    def frame_set(self):
        self.frame2.destroy() #destroy setting frame
        print("Number of Cars: ", self.no_cars.get())
        mainapplication_initialise = Main_application(self.no_cars.get())

class List_create:

    car_List = []
            
    def __init__(self, no_cars):
        self.no_cars = no_cars
        for i in range (self.no_cars):
            if self.is_iep():
                if self.is_leadingcar(i):
                    self.car_List.append([0,1,2,3])
                else:
                    self.car_List.append([4,5,6])
            else:
                self.car_List.append([7,8,9])
        self.list_to_tuple()

    def is_iep(self):
        return self.no_cars > 4

    def is_leadingcar(self, i):
        return i== 0 or i==self.no_cars-1

    def change_List(self):
        #car[x][y] = z
        #this method would be used to change the list values
        #and would be called by another classes method.
        pass

    def list_to_tuple(self):
        self.display_Tuple = tuple(self.car_List)
        print(self.display_Tuple)
        
#widget frame        
class Main_application(tk.Frame, List_create):

    def __init__(self, no_cars):
        List_create.__init__(self, no_cars) #initialises and inherits of the 2 parameters defined
        self.no_cars = no_cars
        print("Main Application: Number of Cars ", self.no_cars)
        self.frame = Frame(bg=dbg)
        self.frame2 = Frame(bg=dbg)#frame for button widgets        
        self.frame.grid(row=0, column=0, columnspan=no_cars+1, rowspan=6)
        self.frame2.grid(row=6, column=0, columnspan=4, rowspan=1)
        self.photo = PhotoImage(file='brakestitle.gif')
        self.maintitle = Label(self.frame, image=self.photo, bg=dbg).grid(row=0, column=0, columnspan=no_cars+1, pady=4)

        self.labelList = [] #creates an empty list "[]" called labelList
        for index in range(self.no_cars): #we create a variable "index" and iterate through numberofcars times
            carString = "Car",index+1 #carString variable is created
            self.labelList.append(Label(self.frame, text=carString, bg=dbg, fg=dfg2, font=dfont)) #adds the carString to the end of the list?
            #believe above line appends Car x to the list, the next time the for loop runs, this string has changed and so a new string is added as the next item on the list.
            self.labelList[index].grid(row=1, column=1 + index, sticky=N) #place updated label list on screen.
             
        self.bcplabel1 = Label(self.frame, text='Brake Cylinder \nPressure:', bg=dbg, fg=dfg2, font=dfont).grid(row=2, column=0, pady=5, sticky=E)
        self.aslabel1 = Label(self.frame, text='Air Suspension:', bg=dbg, fg=dfg2, font=dfont).grid(row=3, column=0, pady=5, sticky=E)
        self.mrlabel1 = Label(self.frame, text='Main Reservoir:', bg=dbg, fg=dfg2, font=dfont).grid(row=4, column=0, pady=5, sticky=E)
        self.bplabel1 = Label(self.frame, text='Brake Pipe:', bg=dbg, fg=dfg2, font=dfont).grid(row=5, column=0, pady=5, sticky=E)
        self.setting = Button(self.frame2)
        self.settingimage = PhotoImage(file='setting.gif')
        self.setting.config(image=self.settingimage, width='113', height='40', background=dbg)
        self.setting.grid(row=0, column=0, sticky=SW)
        self.pswitch = Button(self.frame2)
        self.pswitchimage = PhotoImage(file='pswitch.gif')
        self.pswitch.config(image=self.pswitchimage, width='113', height='40', background=dbg)
        self.pswitch.grid(row=0, column=1, sticky=SW)
        self.calibrate = Button(self.frame2, command=self.changevals)
        self.calibrateimage = PhotoImage(file='calibrate.gif')
        self.calibrate.config(image=self.calibrateimage, width='113', height='40', background=dbg)
        self.calibrate.grid(row=0, column=2, sticky=SW)
        self.superuser = Button(self.frame2, command = self.display_pressures)
        self.superuserimage = PhotoImage(file='superuser.gif')
        self.superuser.config(image=self.superuserimage, width='113', height='40', background=dbg)
        self.superuser.grid(row=0, column=3, sticky=SW)
                
    def changevals(self):
        self.display_Tuple[0][0] = 2.3
        self.display_Tuple[1][2] = 7.2
        self.display_Tuple[2][2] = 0.6
        
    def display_pressures(self):
        self.bcList = [] #creates an empty list "[]" called bclList
        self.mrList = []
        self.asList = []
        for i in range(self.no_cars): #we create a variable "index" and iterate through numberofcars times
            self.bcList.append(Label(self.frame, text=self.display_Tuple[i][0], bg=dbg, fg=dfg2, font=dfont2))
            self.bcList[i].grid(row=2, column=1 + i, sticky=N) #place updated label list on screen.
            self.asList.append(Label(self.frame, text=self.display_Tuple[i][1], bg=dbg, fg=dfg2, font=dfont2))
            self.asList[i].grid(row=3, column=1 + i, sticky=N)
            self.mrList.append(Label(self.frame, text=self.display_Tuple[i][2], bg=dbg, fg=dfg2, font=dfont2))
            self.mrList[i].grid(row=4, column=1 + i, sticky=N) 
        if (self.display_Tuple[0][3] != NONE): #if bp value exists, run for loop
            self.bpMin = (Label(self.frame, text=self.display_Tuple[0][3], bg=dbg, fg=dfg2, font=dfont2)).grid(row=5, column=1, sticky=N)
            self.bpMax = (Label(self.frame, text=self.display_Tuple[self.no_cars - 1][3], bg=dbg, fg=dfg2, font=dfont2)).grid(row=5, column=self.no_cars, sticky=N)


#root is the main window
root = tk.Tk()

#create instance of the main application class,which has __init__ to populate frame in root

mainapp=Proj_select(root)
