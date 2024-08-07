from tkinter import *# importing tkinter module to create a GUI window
import re# importing re module to handle numbers that starting with 0
from math import *# importing math module to handle sqrt
from tkinter import messagebox as tmsg# importing messagebox to show different messages to the user
#Calculator window
root=Tk()#Tk() class instance
root.title("My Calculator")#Title
root.iconbitmap("C:\\Users\\user\\Downloads\\my_calculator.ico")#icon
root.geometry("410x550")#size determined
root.maxsize(410,550)#fixing maxsize
root.minsize(410,550)#fixing minsize
#expression function to handle expressions
def math_expression(expression):
    #using try to handle errors
    try:
        # to replace the the keyboard symbols into python expressions
        expression = expression.replace("^", "**")
        expression = expression.replace("x", "*")
        expression = expression.replace("−", "-")
        expression = expression.replace("÷", "/")
        expression = expression.replace("rem", "%")       
        # Handle percentage calculation
        if "%." in expression:
            # Split by % and calculate percentage
            parts = expression.split('%.')
            base = eval(parts[0])  # Get the base value
            percentage = eval(parts[1]) / 100  # Convert percentage to decimal
            return str(base * percentage)           
        expression=re.sub(r'\b0+(\d)', r'\1', expression)#cutting leading zeros     
        # Handle square root calculation
        expression = expression.replace("√", "sqrt")
        if "sqrt" in expression:
            expression = expression.replace("sqrt", "sqrt(")
            expression += ")"# Ensure there is a closing parenthesis
        # Evaluate the expression
        return str(eval(expression))
    #if error caught then error message will be printed
    except Exception as e:
        return "Error"
#math_func to handle math inputs
def math_func(event):
    value=event.widget.cget("text")#to put inputs in the screen
    #if user press = button then get the value
    if value=='=':
        expression=val_entry.get("0.1",END)# getting the expression from text box
        ans=math_expression(expression)# calling the math_expression() and passing the expression
        val_entry.delete("0.1",END)# deleting user entry
        val_entry.insert(END,ans)# inserting the result
    #if user press AC button then clears the screen
    elif value=="AC":
        val_entry.delete("0.1",END)# deleting entry
    #if user press X button then removes single values 
    elif value=="X":
        val_entry.delete(f'{END}-2c', END)# deleting one character
    elif value=="%.":
        expression=val_entry.get("0.1",END)#taking the all inputs
        ans=math_expression(expression)#sending the input to math_expression()
        val_entry.delete("0.1",END)#clearing the screen
        val_entry.insert(END,ans+"%.")# inserting  the answer
    #put normal values
    else:
        val_entry.insert(END,value)# inserting the expression
#Help Menu options
#Rate menu
def RATE():
    #creating rate window
    rate_window=Toplevel(root)#using top level root 
    rate_window.title("Rate Us")#title
    rate_window.iconbitmap("C:\\Users\\user\\Downloads\\my_calculator.ico")#icon
    rate_window.geometry("300x275")#determining size
    rate_window.maxsize(300,275)#fixing max size
    rate_window.minsize(300,275)#fixing min size
    uframe=Frame(rate_window,bg="seagreen1",pady=20,borderwidth=4,relief="groove")#upper frame
    uframe.pack(fill=X)
    title=Label(uframe,text="Rate us here please",font=("poppins",15,"bold"),bg="white",fg="black")#title 
    title.pack()
    lframe=Frame(rate_window,bg="aquamarine2",pady=20,borderwidth=4,relief="groove")#lower frame
    lframe.pack(fill=X)
    #rate scale to rate 
    rate_scale=Scale(lframe,from_=0, to=100, orient="horizontal",sliderlength=5,sliderrelief="sunken",tickinterval=50,bg="aquamarine2",borderwidth=2,relief="solid",font=("poppins",10,"bold"))
    rate_scale.set(50)#initially setting the position to 50
    rate_scale.pack()
    f_label=Label(lframe,text="\n",bg='aquamarine2')#show label to create space
    f_label.pack()
    #submit button
    s_button=Button(lframe,text="Submit",borderwidth=2,relief="solid",font=("poppins",10,"bold"),padx=10,pady=10,bg="brown1",fg="white",command=rmessage)
    s_button.pack()
    #end of mainloop
    rate_window.mainloop()
#message window after rating
def rmessage():
    #if rating submitted then this message will be displayed
    tmsg.showinfo("Thank You!","Thank You! for your rating :)")
#About us menu
def ABOUT():
    #if clicked on about us then this message will be displayed
    tmsg.showinfo("About Us","This Calculator is made by Soumyajeet Das.\nIt is created using tkinter module in Python.\nDate: 31/07/2024")

#Help Menu
help_menu=Menu(root)
#Inside help Menu
in_help_menu=Menu(help_menu,tearoff=0)
# help menu options
in_help_menu.add_command(label="Rate Us",command=RATE)
in_help_menu.add_separator()# to separate option using a line
in_help_menu.add_command(label="About Us    ",command=ABOUT)
#config the sub help menu to change font size
in_help_menu.config(font=("Helvetica",12))#changing font of sub help menu to increase the menu size
#configuring help Menu
help_menu.add_cascade(label="   Help   ",menu=in_help_menu)
root.configure(menu=help_menu)
#upper frame of the calculator
upper_frame=Frame(root,bg="seagreen1")
upper_frame.pack(fill=BOTH)
#show label to make free space 
temp0=Label(upper_frame,bg="seagreen1",font=("Poppins",9,"bold"))
temp0.pack()
#text box to put value
val_entry=Text(upper_frame,height=3,width=17,font=("Poppins",30,"bold"),borderwidth=2,relief="solid")
val_entry.pack()
#show label to make free space
temp1=Label(upper_frame,bg="seagreen1",font=("Poppins",9,"bold"))
temp1.pack()
#lower frame of the calculator
lower_frame=Frame(root,bg="seagreen1")
lower_frame.pack(fill=BOTH)
#show label to make free space
temp2=Label(lower_frame,text="   ",bg="seagreen1",font=("Poppins",9,"bold"))
temp2.grid(row=1,column=1)
#AC button
ac=Button(lower_frame,text="AC",font=("Poppins",14,"bold"),bg="firebrick1",fg="white",padx=20,pady=6,borderwidth=4,relief="groove")
ac.grid(row=1,column=2)
ac.bind("<Button-1>",math_func)# event handling
#show label to make free space
temp2=Label(lower_frame,text="  ",bg="seagreen1",font=("Poppins",9,"bold"))
temp2.grid(row=1,column=3)
#left parenthesis button
lp=Button(lower_frame,text="(",font=("Poppins",14,"bold"),bg="purple1",fg="white",padx=18,pady=6,borderwidth=4,relief="groove")
lp.grid(row=1,column=4)
lp.bind("<Button-1>",math_func)# event handling
#show label to make free space
temp3=Label(lower_frame,text="  ",bg="seagreen1",font=("Poppins",9,"bold"))
temp3.grid(row=1,column=5)
#right parenthesis button
rp=Button(lower_frame,text=")",font=("Poppins",14,"bold"),bg="purple1",fg="white",padx=18,pady=6,borderwidth=4,relief="groove")
rp.grid(row=1,column=6)
rp.bind("<Button-1>",math_func)# event handling
#show label to make free space
temp4=Label(lower_frame,text="  ",bg="seagreen1",font=("Poppins",9,"bold"))
temp4.grid(row=1,column=7)
#Percentage button
per=Button(lower_frame,text="%.",font=("Poppins",14,"bold"),bg="purple1",fg="white",padx=10,pady=6,borderwidth=4,relief="groove")
per.grid(row=1,column=8)
per.bind("<Button-1>",math_func)# event handling
#show label to make free space
temp5=Label(lower_frame,text="  ",bg="seagreen1",font=("Poppins",9,"bold"))
temp5.grid(row=1,column=9)
#rootover button
rtover=Button(lower_frame,text="√",font=("Poppins",16,"bold"),bg="purple1",fg="white",padx=13,pady=5,borderwidth=4,relief="groove")
rtover.grid(row=1,column=10)
rtover.bind("<Button-1>",math_func)# event handling
#show label to make free space
temp6=Label(lower_frame,text="  ",bg="seagreen1",font=("Poppins",12,"bold"))
temp6.grid(row=2,column=1)

#new frame to decorate correctly
lower_frame2=Frame(root,bg="seagreen1")
lower_frame2.pack(fill=BOTH)
#show label to make free space
temp8=Label(lower_frame2,text="     ",bg="seagreen1",font=("Poppins",6,"bold"))
temp8.grid(row=1,column=1)
#number buttons from 0-9
#9 button
num_9=Button(lower_frame2,text="9",font=("Poppins",16,"bold"),bg="deeppink2",fg="white",padx=13,pady=5,borderwidth=4,relief="groove")
num_9.grid(row=1,column=2)
num_9.bind("<Button-1>",math_func)# event handling
#show label to make free space
temp8=Label(lower_frame2,text="  ",bg="seagreen1",font=("Poppins",6,"bold"))
temp8.grid(row=1,column=3)
#8 button
num_8=Button(lower_frame2,text="8",font=("Poppins",16,"bold"),bg="deeppink2",fg="white",padx=13,pady=5,borderwidth=4,relief="groove")
num_8.grid(row=1,column=4)
num_8.bind("<Button-1>",math_func)# event handling
#show label to make free space
temp9=Label(lower_frame2,text="  ",bg="seagreen1",font=("Poppins",6,"bold"))
temp9.grid(row=1,column=5)
#7 button
num_7=Button(lower_frame2,text="7",font=("Poppins",16,"bold"),bg="deeppink2",fg="white",padx=13,pady=5,borderwidth=4,relief="groove")
num_7.grid(row=1,column=6)
num_7.bind("<Button-1>",math_func)# event handling
#show label to make free space
temp7=Label(lower_frame2,text=" ",bg="seagreen1",font=("Poppins",6,"bold"))
temp7.grid(row=2,column=1)
#6 button
num_6=Button(lower_frame2,text="6",font=("Poppins",16,"bold"),bg="deeppink2",fg="white",padx=13,pady=5,borderwidth=4,relief="groove")
num_6.grid(row=3,column=2)
num_6.bind("<Button-1>",math_func)# event handling
#show label to make free space
temp10=Label(lower_frame2,text="  ",bg="seagreen1",font=("Poppins",6,"bold"))
temp10.grid(row=3,column=3)
#5 button
num_5=Button(lower_frame2,text="5",font=("Poppins",16,"bold"),bg="deeppink2",fg="white",padx=13,pady=5,borderwidth=4,relief="groove")
num_5.grid(row=3,column=4)
num_5.bind("<Button-1>",math_func)# event handling
#show label to make free space
temp11=Label(lower_frame2,text="  ",bg="seagreen1",font=("Poppins",6,"bold"))
temp11.grid(row=3,column=5)
#4 button
num_4=Button(lower_frame2,text="4",font=("Poppins",16,"bold"),bg="deeppink2",fg="white",padx=13,pady=5,borderwidth=4,relief="groove")
num_4.grid(row=3,column=6)
num_4.bind("<Button-1>",math_func)# event handling
#show label to make free space
temp13=Label(lower_frame2,text=" ",bg="seagreen1",font=("Poppins",6,"bold"))
temp13.grid(row=5,column=1)
#3 button
num_3=Button(lower_frame2,text="3",font=("Poppins",16,"bold"),bg="deeppink2",fg="white",padx=13,pady=5,borderwidth=4,relief="groove")
num_3.grid(row=6,column=2)
num_3.bind("<Button-1>",math_func)# event handling
#show label to make free space
temp14=Label(lower_frame2,text="  ",bg="seagreen1",font=("Poppins",6,"bold"))
temp14.grid(row=6,column=3)
#2 button
num_2=Button(lower_frame2,text="2",font=("Poppins",16,"bold"),bg="deeppink2",fg="white",padx=13,pady=5,borderwidth=4,relief="groove")
num_2.grid(row=6,column=4)
num_2.bind("<Button-1>",math_func)# event handling
#show label to make free space
temp15=Label(lower_frame2,text="  ",bg="seagreen1",font=("Poppins",6,"bold"))
temp15.grid(row=6,column=5)
#1 button
num_1=Button(lower_frame2,text="1",font=("Poppins",16,"bold"),bg="deeppink2",fg="white",padx=13,pady=5,borderwidth=4,relief="groove")
num_1.grid(row=6,column=6)
num_1.bind("<Button-1>",math_func)# event handling
#show label to make free space
temp16=Label(lower_frame2,text="  ",bg="seagreen1",font=("Poppins",6,"bold"))
temp16.grid(row=7,column=1)
#0 button
num_0=Button(lower_frame2,text="0",font=("Poppins",16,"bold"),bg="deeppink2",fg="white",padx=13,pady=5,borderwidth=4,relief="groove")
num_0.grid(row=8,column=2)
num_0.bind("<Button-1>",math_func)# event handling
#show label to make free space
temp17=Label(lower_frame2,text="  ",bg="seagreen1",font=("Poppins",6,"bold"))
temp17.grid(row=8,column=3)
#0 button
num_00=Button(lower_frame2,text="00",font=("Poppins",16,"bold"),bg="deeppink2",fg="white",padx=8,pady=5,borderwidth=4,relief="groove")
num_00.grid(row=8,column=4)
num_00.bind("<Button-1>",math_func)# event handling

#show label to make free space
temp17=Label(lower_frame2,text="  ",bg="seagreen1",font=("Poppins",6,"bold"))
temp17.grid(row=8,column=5)
# . button
full_stop=Button(lower_frame2,text=".",font=("Poppins",19,"bold"),bg="deeppink2",fg="white",padx=14,pady=0,borderwidth=4,relief="groove")
full_stop.grid(row=8,column=6)
full_stop.bind("<Button-1>",math_func)# event handling

#show label to make free space
temp18=Label(lower_frame2,text="         ",bg="seagreen1",font=("Poppins",6,"bold"))
temp18.grid(row=1,column=7)
#addition button
plus=Button(lower_frame2,text="+",font=("Poppins",19,"bold"),bg="cyan4",fg="white",padx=14,pady=0,borderwidth=4,relief="groove")
plus.grid(row=1,column=8)
plus.bind("<Button-1>",math_func)# event handling

#show label to make free space
temp19=Label(lower_frame2,text="    ",bg="seagreen1",font=("Poppins",6,"bold"))
temp19.grid(row=1,column=9)
#subtraction button
minus=Button(lower_frame2,text="−",font=("Poppins",19,"bold"),bg="cyan4",fg="white",padx=15,pady=0,borderwidth=4,relief="groove")
minus.grid(row=1,column=10)
minus.bind("<Button-1>",math_func)# event handling

#show label to make free space
temp20=Label(lower_frame2,text="         ",bg="seagreen1",font=("Poppins",6,"bold"))
temp20.grid(row=3,column=7)
# multiply button
multiply=Button(lower_frame2,text="x",font=("Poppins",19,"bold"),bg="cyan4",fg="white",padx=14,pady=0,borderwidth=4,relief="groove")
multiply.grid(row=3,column=8)
multiply.bind("<Button-1>",math_func)# event handling

# show label to make free space
temp21=Label(lower_frame2,text="    ",bg="seagreen1",font=("Poppins",6,"bold"))
temp21.grid(row=3,column=9)
# division button
division=Button(lower_frame2,text="÷",font=("Poppins",19,"bold"),bg="cyan4",fg="white",padx=15,pady=0,borderwidth=4,relief="groove")
division.grid(row=3,column=10)
division.bind("<Button-1>",math_func)# event handling

# show label to make free space
temp22=Label(lower_frame2,text="    ",bg="seagreen1",font=("Poppins",6,"bold"))
temp22.grid(row=6,column=7)
# remainder button
rem=Button(lower_frame2,text="rem",font=("Poppins",16,"bold"),bg="brown1",fg="white",padx=3,pady=5,borderwidth=4,relief="groove")
rem.grid(row=6,column=8)
rem.bind("<Button-1>",math_func)
# show label to make free space
temp23=Label(lower_frame2,text="    ",bg="seagreen1",font=("Poppins",6,"bold"))
temp23.grid(row=6,column=9)
# cap button
cap=Button(lower_frame2,text="^",font=("Poppins",16,"bold"),bg="cyan4",fg="white",padx=17,pady=5,borderwidth=4,relief="groove")
cap.grid(row=6,column=10)
cap.bind("<Button-1>",math_func)
# show label to make free space
temp24=Label(lower_frame2,text="    ",bg="seagreen1",font=("Poppins",6,"bold"))
temp24.grid(row=8,column=7)
# cap button
equalto=Button(lower_frame2,text="=",font=("Poppins",16,"bold"),bg="blue",fg="white",padx=17,pady=5,borderwidth=4,relief="groove")
equalto.grid(row=8,column=8)
equalto.bind("<Button-1>",math_func)
# show label to make free space
temp26=Label(lower_frame2,text="    ",bg="seagreen1",font=("Poppins",6,"bold"))
temp26.grid(row=8,column=9)
# cap button
cross=Button(lower_frame2,text="X",font=("Poppins",16,"bold"),bg="blue",fg="white",padx=17,pady=5,borderwidth=4,relief="groove")
cross.grid(row=8,column=10)
cross.bind("<Button-1>",math_func)
# show label to make free space
temp25=Label(lower_frame2,text=" ",bg="seagreen1",font=("Poppins",15,"bold"))
temp25.grid(row=9,column=1)
root.mainloop()# mainloop() to show the window in the screen