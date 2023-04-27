from tkinter import *
import pyautogui
import time
import sys
from cx_Freeze import setup, Executable
import py2exe
import sys
from cx_Freeze import setup, Executable



base = None
if (sys.platform == "win32"):
    base = "Win32GUI"


   
def main_logic():
    c1_info=c1.get()
    c2_info=c2.get()
    c3_info=c3.get()
    c4_info=c4.get()
    c5_info=c5.get()
    delay_info=delay.get()
    number_info=number.get()
    y=int(number_info/5)

    time.sleep(16)

    for i in range (y):
        pyautogui.typewrite(c1_info)
        pyautogui.typewrite("\n")
        time.sleep(delay_info)
        
        pyautogui.typewrite(c2_info)
        pyautogui.typewrite("\n")
        time.sleep(delay_info)

        pyautogui.typewrite(c3_info)
        pyautogui.typewrite("\n")
        time.sleep(delay_info)

        pyautogui.typewrite(c4_info)
        pyautogui.typewrite("\n")
        time.sleep(delay_info)

        pyautogui.typewrite(c5_info)
        pyautogui.typewrite("\n")
        time.sleep(delay_info)


screen = Tk()
screen.geometry("570x860")
screen.title("FacebookAutoCommenter ( Made by BzTheRpR )--V 1.1")




heading = Label(text="Weelcome To Facebook Auto Commenter",bg="black",fg="blue",width="500",height="3")
heading.pack()

bgcolor= Label(bg="#000000",width="10000",height="100")
bgcolor.pack()

c1=Label(text="Enter the 1st comment",bg="#a8a2c5")
c1.place(x=2,y=70)
c2=Label(text="Enter the 2nd comment",bg="#a8a2c5")
c2.place(x=2,y=140)
c3=Label(text="Enter the 3rd comment",bg="#a8a2c5")
c3.place(x=2,y=210)
c4=Label(text="Enter the 4th comment",bg="#a8a2c5")
c4.place(x=2,y=280)
c5=Label(text="Enter the 5th comment",bg="#a8a2c5")
c5.place(x=2,y=350)

delaynotice=Label(text="👉We are highly recommanding you to select the delay time atleast 2 SECONDS or facebook may ban you",bg="black",fg="red")
delaynotice.place(x=2,y=450)
delay=Label(text="Enter The Delay Time Between Two Comments",bg="#a8a2c5")
delay.place(x=2,y=475)

numbernotice=Label(text="👉We are highly recommanding you to type any number between 200 to 250 or facebook may ban you",bg="black",fg="red")
numbernotice.place(x=2,y=550)
number=Label(text="Please enter how much comment you want to type",bg="#a8a2c5")
number.place(x=2,y=575)

c1=StringVar()
c2=StringVar()
c3=StringVar()
c4=StringVar()
c5=StringVar()
delay=IntVar()
number=IntVar()


c1_entry=Entry(textvariable=c1,bg="#c0bec8")
c2_entry=Entry(textvariable=c2,bg="#c0bec8")
c3_entry=Entry(textvariable=c3,bg="#c0bec8")
c4_entry=Entry(textvariable=c4,bg="#c0bec8")
c5_entry=Entry(textvariable=c5,bg="#c0bec8")

delay_entry=Entry(textvariable=delay,bg="#c0bec8")
number_entry=Entry(textvariable=number,bg="#c0bec8")


c1_entry.place(x=2 ,y=90,width="500",height="35" )
c2_entry.place(x=2 ,y=160,width="500",height="35" )
c3_entry.place(x=2 ,y=230,width="500",height="35" )
c4_entry.place(x=2 ,y=300,width="500",height="35" )
c5_entry.place(x=2 ,y=370,width="500",height="35" )
delay_entry.place(x=2 ,y=495,height="25" )
number_entry.place(x=2 ,y=595,height="25" )

LetsGo_notice1=Label(text="👉After filling up all the boxes open facebook and goto the comment box",bg="black",fg="red")
LetsGo_notice1.place(x=2 ,y=650 )

LetsGo_notice2=Label(text="👉Now click on 'Lets Go' ",bg="black",fg="red")
LetsGo_notice2.place(x=2 ,y=680 )

LetsGo_notice3=Label(text="👉Then tap\press\click in the comment box and 'DO_NO_TOUCH_ANYTHING' ",bg="black",fg="red")
LetsGo_notice3.place(x=2 ,y=710 )

LetsGo_notice4=Label(text="👉After clicking 'Lets Go' Facebook Auto Commenter will start in 16 SECONDS!!!",bg="black",fg="red")
LetsGo_notice4.place(x=2 ,y=740 )

LetsGo_notice5=Label(text="👉Then wait for 16 seconds and see the BOOOMM 💣💣🎆🎇",bg="black",fg="red")
LetsGo_notice5.place(x=2 ,y=770)



LetsGo=Button(screen,text="Lets Go",bg="green",fg="red",command=main_logic)
LetsGo.place(x=230,y=800,width="100",height="50")




screen.mainloop()


