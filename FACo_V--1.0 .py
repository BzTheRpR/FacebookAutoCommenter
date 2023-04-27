import pyautogui
import time

print("\n\n\n")

print("Made By :")

print("\n\n")

print("            :NNNNNd/        /NNNNNNNN+ ys                yNNNNNmy.           yNNNNNmy.    ")           
print("            :M/---sM:       `---dd---` hy                hd....:md           hd..../md    ")           
print("            :M.    No ::::::-   hd     hy.++-    `/+/`   hd     +M. :.-+/`   hh     oM.   ")           
print("            :M.   :M: syyyhMy   hd     hNmsyM/  :Nhohm-  hd     hN  mmd+yN-  hh     hN`   ")           
print("            :MNmmNMs     `dh    hd     hm`  yd `No   yd  hNhhhdNm-  md   yd  hNhhhdNm-    ")           
print("            :M/--:+Ns   `dh     hd     hy   od :MyooohM` hm::oNy    mo   :M. hd:/oNy      ")           
print("            :M.    oM` `mh      hd     hy   od :Msooooo  hd   -Ny   m+   :M. hh   -Ny     ")           
print("            :M.    sN `mh`      hd     hy   od .M/   :o  hd    /Mo  my   oN  hh    /Mo    ")           
print("            :MsooohMo`mN/////   hd     hy   od  sN/-/Ns  hd     yM- mMo-+N/  hh     yM-   ")           
print("            .yyyyyo- `yyyyyys   +o     ++   /o   /hdh/   +o     `so mssdh:   ++     `so   ")           
print("                                                                    mo                    ")           
print("                                                                    mo                    ")           
print("                                                                    -.                    ")
          


print("\n\n\n")

print("\t\t\t\t\tWeelcome to Facebook Auto Commenter")
print("\n\n")
print("Hello Dear User!!! Here is a NOTICE for you in the bellow.Please read the notice CAREFULLY")
print("\n")
print("NOTICE : 👉  First open facebook.\n\n")
print("         👉  In this Facebook Auto Commenter you will need to type five different commentes\n")
print("               those you want to type in the victims comment box.\n\n")
print("         👉  And you need to select the delay time after every comments.\n\n")
print("         👉  We are highly recommanding you to select the delay time atleast 2 SECONDS or facebook may ban you.\n\n")
print("         👉  And then need to select how much comments you want to write in the victims comment box.\n\n")
print("         👉  Now,Again we are highly recommanding you to type any number between 200 to 250 or facebook may ban you\n\n")
print("         👉  If you get banned from facebook for too much spaming then use VPN and start doing comment again")
print("\n\n")


c1=input("[Type the comment and press enter] Comment1 : ")
print("\n")
c2=input("[Type the comment and press enter] Comment2 : ")
print("\n")
c3=input("[Type the comment and press enter] Comment3 : ")
print("\n")
c4=input("[Type the comment and press enter] Comment4 : ")
print("\n")
c5=input("[Type the comment and press enter] Comment5 : ")
print("\n")
print("\n")

print(">>>-We are highly recommanding you to select the delay time atleast 2 SECONDS or facebook may ban you.\n")
j=int(input("Enter The Delay Time between Tow Comments [Then Press Enter] : "))
print("\n")
print("\n")

print(">>>-We are highly recommanding you to type any number between 200 to 250 or facebook may ban you\n")
x=int(input("Please enter how much comment you want to type [Then Press Enter] : "))
y=int(x/5)

print("Thank You Bruh!!! Facebook Auto Commenter will start in 16 SECONDS!!!\n          Now goto facebook and tap\press\click in the comment box\n          Wait for 16 seconds and see the BOOOMM")

time.sleep(16)


for i in range (y):
    pyautogui.typewrite(c1)
    pyautogui.typewrite("\n")
    time.sleep(j)
    
    pyautogui.typewrite(c2)
    pyautogui.typewrite("\n")
    time.sleep(j)

    pyautogui.typewrite(c3)
    pyautogui.typewrite("\n")
    time.sleep(j)

    pyautogui.typewrite(c4)
    pyautogui.typewrite("\n")
    time.sleep(j)

    pyautogui.typewrite(c5)
    pyautogui.typewrite("\n")
    time.sleep(j)
