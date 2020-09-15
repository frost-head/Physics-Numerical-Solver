from tkinter import ttk
from tkinter import *
from math import *
from PIL import ImageTk,Image
from ttkthemes import ThemedTk
root = ThemedTk(theme="breeze")

root.title("PNS")

v= range(180)
R=list(v)

v=0
r=0
t=0
h=0

s = 2
q = 1/2



def projectile():
    projection = Toplevel(bg= "#A30059")

    projection.title("MOTION")
    projection.bg= "#A30059"



    #defining objects for projectile
    background = ImageTk.PhotoImage(Image.open("design/Untitled-2.jpg"))
    space= ttk.Label(projection,image = background,border=0)
    space.image = background

    velo= ImageTk.PhotoImage(Image.open("design/velocity.png"))
    space1= Label(projection, image=velo, font = 'Arial',bg =  "#A30059")
    space1.image=velo
    time = ImageTk.PhotoImage(Image.open("design/time.png"))
    space3= Label(projection, bg=  "#A30059",image=time, font = 'Arial')
    space3.image=time
    rang= ImageTk.PhotoImage(Image.open("design/range.png"))
    space2= Label(projection, image=rang, font = 'Arial',bg ="#A30059")
    space2.image=rang
    height=ImageTk.PhotoImage(Image.open("design/height.png"))
    space4= Label(projection, image=height, font = 'Arial',bg ="#A30059")
    space4.image=height
    angle=ImageTk.PhotoImage(Image.open("design/Angle.png"))
    space5= Label(projection, image=angle, font = 'Arial',bg ="#A30059")
    space5.image=angle
    entry=ImageTk.PhotoImage(Image.open("design/entry.png"))
    Velocity= ttk.Entry(projection, width=30, font = 'Arial')
    Velocity.insert(0,v)
    Range= ttk.Entry(projection, width=30, font = 'Arial')
    Range.insert(0, r)
    Time_Period= ttk.Entry(projection, width=30, font = 'Arial')
    Time_Period.insert(0,t)


    Angle= ttk.Spinbox(projection,values =(R), width=29, font = 'Arial')

    Height= ttk.Entry(projection, width=30, font = 'Arial')
    Height.insert(0,h)


    #designing page

    space.grid(row=1,column=1,columnspan=4)
    
    Velocity.grid(row=2,column=2,padx=5,pady=5)
    space1.grid(row=2,column=1,padx=5,pady=5)

    Range.grid(row=2,column=4,padx=5,pady=5)
    space2.grid(row=2,column=3,padx=5,pady=5)

    Time_Period.grid(row=4,column=2,padx=5,pady=5)
    space3.grid(row=4,column=1,padx=5,pady=5)

    Height.grid(row=4,column=4,padx=5,pady=5)
    space4.grid(row=4,column=3,padx=5,pady=5)

    Angle.grid(row=6,column=2,padx=5,pady=5)
    space5.grid(row=6,column=1,padx=5,pady=5)


    def calculate_projectile():


        
        if(float(Velocity.get())!=0):
            Time_Period.delete(0, END)
            Time_Period.insert(0, round((2*float(Velocity.get())*sin(radians(float(Angle.get()))))/9.8))

            Height.delete(0, END)

            Height.insert(0, round(float(Velocity.get())**s*sin(radians(float(Angle.get())))**s/19.6))
            Range.delete(0, END)
            Range.insert(0, round((float(Velocity.get())**s*sin(radians(2*float(Angle.get()))))/9.8))

        elif(float(Range.get())!=0):
            Velocity.delete(0,END)
            Velocity.insert(0, round(sqrt(float(Range.get())*9.8/sin(radians(2*float(Angle.get()))))))
            Time_Period.delete(0, END)
            Time_Period.insert(0, round((2*float(Velocity.get())*sin(radians(float(Angle.get()))))/9.8 ))

            Height.delete(0, END)

            Height.insert(0, round(float(Velocity.get())**s*sin(radians(float(Angle.get())))**s/19.6))
            
        elif(float(Height.get())!=0):
            Velocity.delete(0,END)
            Velocity.insert(0,round(sqrt(float(Height.get())*19.6/sin(radians(float(Angle.get())))**s)))
            Time_Period.delete(0, END)
            Time_Period.insert(0, round((2*float(Velocity.get())*sin(radians(float(Angle.get()))))/9.8 ))
            Range.delete(0, END)
            Range.insert(0, round((float(Velocity.get())**s*sin(radians(2*float(Angle.get()))))/9.8))

        elif(float(Time_Period.get())!=0):
            Velocity.delete(0,END)
            Velocity.insert(0,round(float(Time_Period.get())*9.8/(sin(radians(float(Angle.get())))*2)))
            Range.delete(0, END)
            Range.insert(0, round((float(Velocity.get())**s*sin(radians(2*float(Angle.get()))))/9.8))
            Height.delete(0, END)

            Height.insert(0, round(float(Velocity.get())**s*sin(radians(float(Angle.get())))**s/19.6))

    def Clear():
        Velocity.delete(0,END)
        Range.delete(0,END)
        Time_Period.delete(0,END)
        Height.delete(0, END)   
        Velocity.insert(0,v)
        Range.insert(0, r) 
        Time_Period.insert(0,t)
        Height.insert(0,h)

    clear_img = ImageTk.PhotoImage(Image.open("design/clear.png"))



    clear = Button(projection ,image=clear_img, command=Clear)
    clear["bg"] = "#A30059"
    clear["border"] = "0"
    clear.image=clear_img
    clear.grid(row=7,column=4,padx=5,pady=5)


    cal_img=ImageTk.PhotoImage(Image.open("design/cal.png"))
    calculate = Button(projection, image=cal_img, command = calculate_projectile)
    calculate["bg"] = "#A30059"
    calculate["border"] = "0"
    calculate.image=cal_img
    calculate.grid(row=7,column=2,padx=5,pady=5)

    


pro = ttk.Button(root, text="Projectile", command=projectile)
pro.grid(row=1, column=2)

root.mainloop()
