#Name: Jaiden Gool
#Topic: Summative Video Game
#Start Date: May 9th, 2023
#End Date: June 4th, 2023

#This is a one chapter long RPG game, which includes aspects from text RPGS, and aspects from turn based games like Pokemon.
#You will have to download all the pictures provided, or else the game will be unplayable
#Please do not enter a name that is too long; the limit is around 13 characters
#Please do not enter entries that are too long when asked by NPCs, there is very little space, so try to stick to around 3-4 words max when asked
#No other library is needed other than tkinter for this game

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#Quit Button
def QuitAction():
    Main_Window.destroy()

######Inventory Button######
def OpenInventory():
    #Gets amount of food held
    Health=(HEALTH.get())
    Apple=(APPLE.get())
    Bread=(BREAD.get())
    Chicken=(CHICKEN.get())
    Name=(NAME.get())
    Level=(LEVEL.get())

    #Command to use foods
    def UseApple():
        Health=(HEALTH.get())
        Apple=(APPLE.get())
        if Apple==0:
            Warn=tk.messagebox.showwarning("Error", "You have no apples")
        else:
            Apple=Apple-1
            Health=Health+5
            APPLE.set(Apple)
            HEALTH.set(Health)
            AppleHeld=tk.Label(InventoryFrame, text=("Held: " + str(Apple)), font="Fixedsys 15", bg="darkgray")
            AppleHeld.place(x=650, y=80)
            Health=HEALTH.get()
            Health_Label=tk.Label(InventoryFrame, text="Health: " + str(Health) + str(" / 100"), font="Fixedsys", bg="darkgray")
            Health_Label.place(x=40, y=380, height=35, width=175)
            
    def UseBread():
        Health=(HEALTH.get())
        Bread=(BREAD.get())
        if Bread==0:
            Warn=tk.messagebox.showwarning("Error", "You have no bread")
        else:
            Bread=Bread-1
            Health=Health+15
            BREAD.set(Bread)
            HEALTH.set(Health)
            BreadHeld=tk.Label(InventoryFrame, text=("Held: " + str(Bread)), font="Fixedsys 15", bg="darkgray")
            BreadHeld.place(x=650, y=230)
            Health=HEALTH.get()
            Health_Label=tk.Label(InventoryFrame, text="Health: " + str(Health) + str(" / 100"), font="Fixedsys", bg="darkgray")
            Health_Label.place(x=40, y=380, height=35, width=175)

    def UseChicken():
        Health=(HEALTH.get())
        Chicken=(CHICKEN.get())
        if Chicken==0:
            Warn=tk.messagebox.showwarning("Error", "You have no Chicken")
        else:
            Chicken=Chicken-1
            Health=Health+25
            CHICKEN.set(Chicken)
            HEALTH.set(Health)
            ChickenHeld=tk.Label(InventoryFrame, text=("Held: " + str(Chicken)), font="Fixedsys 15", bg="darkgray")
            ChickenHeld.place(x=650, y=380)
            Health=HEALTH.get()
            Health_Label=tk.Label(InventoryFrame, text="Health: " + str(Health) + str(" / 100"), font="Fixedsys", bg="darkgray")
            Health_Label.place(x=40, y=380, height=35, width=175)

    #Use Food
    AppleUse=tk.Button(InventoryFrame, text="Use", font="Fixedsys 15", bg="lightgreen", command=UseApple)
    AppleUse.place(x=650, y=110)
    BreadUse=tk.Button(InventoryFrame, text="Use", font="Fixedsys 15", bg="lightgreen", command=UseBread)
    BreadUse.place(x=650, y=260)
    ChickenUse=tk.Button(InventoryFrame, text="Use", font="Fixedsys 15", bg="lightgreen", command=UseChicken)
    ChickenUse.place(x=650, y=410)
    
    #Amount of food held
    AppleHeld=tk.Label(InventoryFrame, text=("Held: " + str(Apple)), font="Fixedsys 15", bg="darkgray")
    AppleHeld.place(x=650, y=80)
    BreadHeld=tk.Label(InventoryFrame, text=("Held: " + str(Bread)), font="Fixedsys 15", bg="darkgray")
    BreadHeld.place(x=650, y=230)
    ChickenHeld=tk.Label(InventoryFrame, text=("Held: " + str(Chicken)), font="Fixedsys 15", bg="darkgray")
    ChickenHeld.place(x=650, y=380)
    
    #Food Descriptions
    AppleDisc=tk.Label(InventoryFrame, text="Delicious, juicy, healthy apples (Heals 5 Health)", font="Fixedsys 15", bg="darkgray")
    AppleDisc.place(x=650, y=50)
    BreadDisc=tk.Label(InventoryFrame, text="Freshly baked, hot, soft bread (Heals 15 Health)", font="Fixedsys 15", bg="darkgray")
    BreadDisc.place(x=650, y=200)
    ChickenDisc=tk.Label(InventoryFrame, text="Hot, juicy, and tender baked chicken (Heals 25 Health)", font="Fixedsys 15", bg="darkgray")
    ChickenDisc.place(x=650, y=350)
    
    #Icons
    ApplePic=tk.Label(InventoryFrame, image=Apples)
    ApplePic.place(x=400, y=50)
    BreadPic=tk.Label(InventoryFrame, image=Breads)
    BreadPic.place(x=400, y=200)
    ChickenPic=tk.Label(InventoryFrame, image=Chickens)
    ChickenPic.place(x=400, y=350)

    #Shows the whole inventory
    MainFrame.place_forget()
    InventoryFrame.place(x=0, y=0)

    #Shows Health
    Health=HEALTH.get()
    Health_Label=tk.Label(InventoryFrame, text="Health: " + str(Health) + str(" / 100"), font="Fixedsys", bg="darkgray")
    Health_Label.place(x=40, y=380, height=35, width=175)

    #Shows Name
    Name_Label=tk.Label(InventoryFrame, text=(Name),
                        font="Fixedsys 20",
                        bg="darkgray")
    Name_Label.place(x=40, y=125, height=35)
    
    #Shows Character
    Character=tk.Label(InventoryFrame, image=Characters)
    Character.place(x=40, y=210)
    
    #Shows Level
    Level=tk.Label(InventoryFrame, text=("Level " + str(Level)), font="Fixedsys", bg="darkgray")
    Level.place(x=40, y=175)

    #Inventory Label
    InventoryLabel=tk.Label(InventoryFrame, text="Inventory", font="Fixedsys 22 bold", bg="darkgray", fg="red")
    InventoryLabel.place(x=150, y=40)
                   
#Back Button
def ExitInventory():
    InventoryFrame.place_forget()
    MainFrame.place(x=0, y=0)
    Health=HEALTH.get()
    Health_Label=tk.Label(MainFrame, text="Health: " + str(Health) + str(" / 100"), font="Fixedsys", bg="darkgray")
    Health_Label.place(x=780, y=25, height=35, width=175)
    
#Show MainFrame
def showMainFrame():
    Name=(NAME.get())
    if Name=="":
        Warn=tk.messagebox.showwarning("Error", "Please enter a name")
    else:
        IntroFrame.place_forget()
        MainFrame.place(x=0, y=0)
        MainFrame.after(1000, FirstDialouge)

#Resets Text Area
def ClearText():
    TextArea=tk.Label(MainFrame, text="")
    TextArea.place(x=550, y=75, width=410, height=275)
    TextArea.configure(bg="darkgray")

#Resets Choice Area
def ClearChoice():
    ChoiceArea=tk.Label(MainFrame, text="")
    ChoiceArea.place(x=550, y=350, width=410, height=150)
    ChoiceArea.configure(bg="black")

#Game Over Screen
def GameOver():
    GameOverFrame.place(x=0, y=0)

    def SecondLabel():
        GameOver=tk.Label(GameOverFrame, text="You died.", bg="gray", fg="white", font="Fixedsys")
        GameOver.place(x=510, y=200)
        GameOver.after(5000, QuitAction)
    
    YouDied=tk.Label(GameOverFrame, text="GAME OVER", fg="red", font="Fixedsys 20 bold")
    YouDied.place(x=470, y=100)
    YouDied.after(3000, SecondLabel)

######### Contains all buttons that contain dialouge #########
    
######Game Ending######    
def GameEnd():
    EndingFrame.place(x=0, y=0)

    def ThirdLabel():
        ThirdLabel=tk.Label(EndingFrame, text="Thank you for playing!", bg="gray", fg="white", font="Fixedsys 15")
        ThirdLabel.place(x=455, y=300)
        ExitButton=tk.Button(EndingFrame, text="Exit Game", font="Fixedsys", bg="gray", fg="lightblue", command=QuitAction)
        ExitButton.place(x=500, y=400, height=40)

    def SecondLabel():
        SecondLabel=tk.Label(EndingFrame, text="You have finished the game.", bg="gray", fg="white", font="Fixedsys 15")
        SecondLabel.place(x=440, y=200)
        SecondLabel.after(2000, ThirdLabel)
    
    Congrats=tk.Label(EndingFrame, text="CONGRATULATIONS!!!", fg="white", bg="orange", font="Fixedsys 20 bold")
    Congrats.place(x=400, y=100)
    Congrats.after(2000, SecondLabel)
    
######Boss Battle######
def BossBattle():
    #Victory End
    def VictoryEnd():
        Message11=tk.Label(MainFrame, text="You head down the path for your next adventure.", font="Fixedsys 10 italic", bg="darkgray")
        Message11.place(x=560, y=300)
        Message11.after(3000, GameEnd)
        
    #Victory Continue Three
    def VictoryContinueThree():
        Message10=tk.Label(MainFrame, text="And many more enemies to battle!", font="Fixedsys", bg="darkgray")
        Message10.place(x=560, y=275)
        Message10.after(2000, VictoryEnd)
        
    #Victory Continue Two
    def VictoryContinueTwo():
        Message9=tk.Label(MainFrame, text="There are many more adventures to be had...", font="Fixedsys", bg="darkgray")
        Message9.place(x=560, y=250)
        Message9.after(2000, VictoryContinueThree)
                    
    #Victory Continue
    def VictoryContinue():
        Message8=tk.Label(MainFrame, text="But the true battle is yet to finish!", font="Fixedsys", bg="darkgray")
        Message8.place(x=560, y=225)
        Message8.after(2000, VictoryContinueTwo)
        
    #Victory
    def Victory():
        Scene=tk.Label(MainFrame, image=FinalBossDefeat)
        Scene.place(x=0, y=0, width=500, height=frameHeight)
        Message7=tk.Label(MainFrame, text="You have defeated the reaper...", font="Fixedsys", bg="darkgray")
        Message7.place(x=560, y=200)
        Message7.after(2000, VictoryContinue)
        
    #Move Three Resposne
    def MoveThreeResponse():
        Choice=(int(CHOICE.get()))
        if Choice==0:
            Warn=tk.messagebox.showwarning("Error", "You must pick an action to continue")
            
        elif Choice==1:
            ClearChoice()
            EHEALTH.set(0)
            EHealth=(EHEALTH.get())
            Message5=tk.Label(MainFrame, text="You attack the reaper for 100 DMG...", font="Fixedsys", bg="darkgray")
            Message5.place(x=560, y=150)
            Message6=tk.Label(MainFrame, text="The reaper now has " + str(EHealth) + " health!", font="Fixedsys", bg="darkgray")
            Message6.place(x=560, y=175)
            Message6.after(2000, Victory)
            
        elif Choice==2:
           ClearChoice()
           Message5=tk.Label(MainFrame, text="You try to talk to the reaper but it's no use!", font="Fixedsys", bg="darkgray")
           Message5.place(x=560, y=150)
           Message6=tk.Label(MainFrame, text="The reaper shows no mercy. You have died.", font="Fixedsys", bg="darkgray")
           Message6.place(x=560, y=175)
           Message6.after(2000, GameOver)

        elif Choice==3:
            ClearChoice()
            Message5=tk.Label(MainFrame, text="The reaper catches you trying to escape.", font="Fixedsys", bg="darkgray")
            Message5.place(x=560, y=150)
            Message6=tk.Label(MainFrame, text="You have died.", font="Fixedsys", bg="darkgray")
            Message6.place(x=560, y=175)
            Message6.after(4000, GameOver)
            
    #Battle Choice Three
    def BattleChoiceThree():
        CHOICE.set(0)
        Message1=tk.Label(MainFrame, text="What will be your third move?", font="Fixedsys 10 italic", bg="darkgray")
        Message1.place(x=560, y=125)
        Battle=tk.Radiobutton(MainFrame, text="Attack", font="Fixedsys", bg="darkgray", variable=CHOICE, value=1)
        Battle.place(x=560, y=360, height=60, width=190)
        Talk=tk.Radiobutton(MainFrame, text="Talk", font="Fixedsys", bg="darkgray", variable=CHOICE, value=2)
        Talk.place(x=760, y=360, height=60, width=190)
        Run=tk.Radiobutton(MainFrame, text="Run", font="Fixedsys", bg="darkgray", variable=CHOICE, value=3)
        Run.place(x=560, y=430, height=60, width=190)
        Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", fg="red", command=MoveThreeResponse)
        Submit.place(x=760, y=430, height=60, width=190)
        
    #Reaper Move Two
    def ReaperMoveTwo():
        ClearText()
        Health=(HEALTH.get()-49)
        HEALTH.set(Health)
        Health_Label=tk.Label(MainFrame, text="Health: " + str(Health) + str(" / 100"), font="Fixedsys", bg="darkgray")
        Health_Label.place(x=780, y=25, height=35, width=175)
        Message4=tk.Label(MainFrame, text="The reaper attacks you back for 49 DMG", font="Fixedsys", bg="darkgray")
        Message4.place(x=560, y=100)
        Message4.after(2000, BattleChoiceThree)
        
    #Move Two Response
    def MoveTwoResponse():
        Choice=(int(CHOICE.get()))
        if Choice==0:
            Warn=tk.messagebox.showwarning("Error", "You must pick an action to continue")
            
        elif Choice==1:
            ClearChoice()
            EHEALTH.set(100)
            EHealth=(EHEALTH.get())
            Message5=tk.Label(MainFrame, text="You attack the reaper for 100 DMG...", font="Fixedsys", bg="darkgray")
            Message5.place(x=560, y=275)
            Message6=tk.Label(MainFrame, text="The reaper now has " + str(EHealth) + " health left!", font="Fixedsys", bg="darkgray")
            Message6.place(x=560, y=300)
            Message6.after(2000, ReaperMoveTwo)
            
        elif Choice==2:
           ClearChoice()
           Message5=tk.Label(MainFrame, text="You try to talk to the reaper but it's no use!", font="Fixedsys", bg="darkgray")
           Message5.place(x=560, y=275)
           Message6=tk.Label(MainFrame, text="The reaper shows no mercy. You have died.", font="Fixedsys", bg="darkgray")
           Message6.place(x=560, y=300)
           Message6.after(2000, GameOver)

        elif Choice==3:
            ClearChoice()
            Message5=tk.Label(MainFrame, text="The reaper catches you trying to escape.", font="Fixedsys", bg="darkgray")
            Message5.place(x=560, y=275)
            Message6=tk.Label(MainFrame, text="You have died.", font="Fixedsys", bg="darkgray")
            Message6.place(x=560, y=300)
            Message6.after(4000, GameOver)
            
    #Player's second action
    def BattleChoiceTwo():
        CHOICE.set(0)
        Message1=tk.Label(MainFrame, text="What will be your second move?", font="Fixedsys 10 italic", bg="darkgray")
        Message1.place(x=560, y=250)
        Battle=tk.Radiobutton(MainFrame, text="Attack", font="Fixedsys", bg="darkgray", variable=CHOICE, value=1)
        Battle.place(x=560, y=360, height=60, width=190)
        Talk=tk.Radiobutton(MainFrame, text="Talk", font="Fixedsys", bg="darkgray", variable=CHOICE, value=2)
        Talk.place(x=760, y=360, height=60, width=190)
        Run=tk.Radiobutton(MainFrame, text="Run", font="Fixedsys", bg="darkgray", variable=CHOICE, value=3)
        Run.place(x=560, y=430, height=60, width=190)
        Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", fg="red", command=MoveTwoResponse)
        Submit.place(x=760, y=430, height=60, width=190)
        
    #Reaper Move One
    def ReaperMoveOne():
        Health=(HEALTH.get()-49)
        HEALTH.set(Health)
        Health_Label=tk.Label(MainFrame, text="Health: " + str(Health) + str(" / 100"), font="Fixedsys", bg="darkgray")
        Health_Label.place(x=780, y=25, height=35, width=175)
        Message4=tk.Label(MainFrame, text="The reaper attacks you back for 49 DMG", font="Fixedsys", bg="darkgray")
        Message4.place(x=560, y=225)
        Message4.after(2000, BattleChoiceTwo)
        
    #Move One Response
    def MoveOneResponse():
        Choice=(int(CHOICE.get()))
        if Choice==0:
            Warn=tk.messagebox.showwarning("Error", "You must pick an action to continue")
            
        elif Choice==1:
            ClearChoice()
            EHEALTH.set(200)
            EHealth=(EHEALTH.get())
            Message2=tk.Label(MainFrame, text="You attack the reaper for 100 DMG...", font="Fixedsys", bg="darkgray")
            Message2.place(x=560, y=175)
            Message3=tk.Label(MainFrame, text="The reaper now has " + str(EHealth) + " health left!", font="Fixedsys", bg="darkgray")
            Message3.place(x=560, y=200)
            Message3.after(2000, ReaperMoveOne)
            
        elif Choice==2:
           ClearChoice()
           Message2=tk.Label(MainFrame, text="You try to talk to the enemy, but it's no use!", font="Fixedsys", bg="darkgray")
           Message2.place(x=560, y=175)
           Message3=tk.Label(MainFrame, text="The reaper strikes you down. You have died.", font="Fixedsys", bg="darkgray")
           Message3.place(x=560, y=200)
           Message3.after(2000, GameOver)

        elif Choice==3:
            ClearChoice()
            Message2=tk.Label(MainFrame, text="You try to run, but there is no escape.", font="Fixedsys", bg="darkgray")
            Message2.place(x=560, y=175)
            Message3=tk.Label(MainFrame, text="You have died.", font="Fixedsys", bg="darkgray")
            Message3.place(x=560, y=200)
            Message3.after(4000, GameOver)
            
    #Player's first action
    def BattleChoiceOne():
        CHOICE.set(0)
        Message1=tk.Label(MainFrame, text="What will be your first move?", font="Fixedsys 10 italic", bg="darkgray")
        Message1.place(x=560, y=150)
        Battle=tk.Radiobutton(MainFrame, text="Attack", font="Fixedsys", bg="darkgray", variable=CHOICE, value=1)
        Battle.place(x=560, y=360, height=60, width=190)
        Talk=tk.Radiobutton(MainFrame, text="Talk", font="Fixedsys", bg="darkgray", variable=CHOICE, value=2)
        Talk.place(x=760, y=360, height=60, width=190)
        Run=tk.Radiobutton(MainFrame, text="Run", font="Fixedsys", bg="darkgray", variable=CHOICE, value=3)
        Run.place(x=560, y=430, height=60, width=190)
        Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", fg="red", command=MoveOneResponse)
        Submit.place(x=760, y=430, height=60, width=190)
        
    #First Message
    def ContinuedIntroduction():
        ContinueIntro=tk.Label(MainFrame, text="The world is depending on you, time to fight!", font="Fixedsys 10 italic", bg="darkgray")
        ContinueIntro.place(x=560, y=125)
        ContinueIntro.after(2000, BattleChoiceOne)
    
    #Introduces the player to the second boss
    def IntroduceBoss():
        EHEALTH.set(300)
        IntroductionBoss=tk.Label(MainFrame, text="You have encountered the final boss!", font="Fixedsys 10 italic", bg="darkgray")
        IntroductionBoss.place(x=560, y=100)
        IntroductionBoss.after(2000, ContinuedIntroduction)
        
    #Changes Background
    Scene=tk.Label(MainFrame, image=LastBossAlive)
    Scene.place(x=0, y=0, width=500, height=frameHeight)
    Scene.after(2000, IntroduceBoss)
      
    #Resets Text Area
    ClearText()
    
######Path to the boss######
def Bosspath():
    #Continues game after user is ready
    def Continue():
        Choice=(int(CHOICE.get()))
        if Choice==1:
            ClearChoice()
            Message4=tk.Label(MainFrame, text="Good luck.", font="Fixedsys 10 bold", bg="darkgray")
            Message4.place(x=560, y=150)
            Message4.after(2000, BossBattle)
            
        elif Choice==2:
            Message4=tk.Label(MainFrame, text="So close, yet so far. Goodbye.", font="Fixedsys 10 bold", bg="darkgray")
            Message4.place(x=560, y=150)
            Message4.after(2000, QuitAction)
            
        else:
            Warn=tk.messagebox.showwarning("Error", "Please select an option")
            
    #Show the buttons
    def PathChoose():
        CHOICE.set(0)        
        LeftPath=tk.Radiobutton(MainFrame, text="I'm ready.", font="Fixedsys", variable=CHOICE, value=1)
        LeftPath.place(x=560, y=360, width=185, height=30)
        RightPath=tk.Radiobutton(MainFrame, text="I give up.", font="Fixedsys", variable=CHOICE, value=2)
        RightPath.place(x=765, y=360, width=185, height=30)        
        Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", command=Continue)
        Submit.place(x=720, y=400)
        
    #Describes the first path
    def DescribePaths():
        Message2=tk.Label(MainFrame, text="Do you wish to continue?", font="Fixedsys", bg="darkgray")
        Message2.place(x=560, y=125)
        Message2.after(1000, PathChoose)
        
    #Describes the area
    def DescribeScene1():
        Message1=tk.Label(MainFrame, text="You have reached the final path before the boss", font="Fixedsys 10 italic", bg="darkgray")
        Message1.place(x=560, y=100)
        Message1.after(2000, DescribePaths)

    #Changes Background
    Scene=tk.Label(MainFrame, image=BossPath)
    Scene.place(x=0, y=0, width=500, height=frameHeight)
    Scene.after(1000, DescribeScene1)
    
    #Resets Text Area
    ClearText()
    
######Second Village######
def VillageSceneTwo():
    #Adds Food
    def ContinueFood():
        ClearChoice()
        #Makes the value of food held global
        Apple=int(APPLE.get())
        Apple=int(Apple + APPLECHOOSE.get())
        APPLE.set(Apple)

        Bread=int(BREAD.get())     
        Bread=int(Bread + BREADCHOOSE.get())
        BREAD.set(Bread)
        
        Chicken=int(CHICKEN.get())
        Chicken=int(Chicken + CHICKENCHOOSE.get())
        CHICKEN.set(Chicken)

        Message5=tk.Label(MainFrame, text="I hope you are prepared for the danger ahead.", font="Fixedsys", bg="darkgray")
        Message5.place(x=560, y=225)
        Message5.after(2000, Bosspath)
        
    #Fourth Message
    def FourthDialogue():
        APPLECHOOSE.set(0)
        BREADCHOOSE.set(0)
        CHICKENCHOOSE.set(0)
        Message4=tk.Label(MainFrame, text="I see. Take some food, you must stay healthy.", font="Fixedsys", bg="darkgray")
        Message4.place(x=560, y=200)
        AppleChoose=tk.Checkbutton(MainFrame, text="Apple", font="Fixedsys", bg="darkgray", variable=APPLECHOOSE)
        AppleChoose.place(x=560, y=360, height=60, width=190)
        BreadChoose=tk.Checkbutton(MainFrame, text="Hot Bread", font="Fixedsys", bg="darkgray", variable=BREADCHOOSE)
        BreadChoose.place(x=760, y=360, height=60, width=190)
        ChickenChoose=tk.Checkbutton(MainFrame, text="Fresh Chicken", font="Fixedsys", bg="darkgray", variable=CHICKENCHOOSE)
        ChickenChoose.place(x=560, y=430, height=60, width=190)
        Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", fg="red", command=ContinueFood)
        Submit.place(x=760, y=430, height=60, width=190)
    #Third Message
    def ThirdDialogue():
        Response=(RESPONSE.get())
        if Response=="":
            Warn=tk.messagebox.showwarning("Error", "Please respond to the villager")
        else:
            ClearChoice()
            Message3=tk.Label(MainFrame, text=("You say to the villager: " + str(Response)), font="Fixedsys 10 italic", bg="darkgray")
            Message3.place(x=560, y=175)
            Message3.after(2000, FourthDialogue)
    #Second Message
    def SecondDialogue():
        RESPONSE.set("")
        Message2=tk.Label(MainFrame, text="Why have you come here?", font="Fixedsys", bg="darkgray")
        Message2.place(x=560, y=150)
        Reason=tk.Entry(MainFrame, textvariable=RESPONSE)
        Reason.place(x=560, y=360, height=30, width=390)
        Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", command=ThirdDialogue)
        Submit.place(x=720, y=400)
        
    #First Message
    def FirstDialogue():
        Message1=tk.Label(MainFrame, text="Hello? Don't you know this place is dangerous?", font="Fixedsys", bg="darkgray")
        Message1.place(x=560, y=125)
        Message1.after(2000, SecondDialogue)
    
    #Introduces the player to the first village
    def IntroduceVillageOne():
        IntroductionVillage=tk.Label(MainFrame, text="You arrive at a rundown village", font="Fixedsys 10 italic", bg="darkgray")
        IntroductionVillage.place(x=560, y=100)
        IntroductionVillage.after(2000, FirstDialogue)
        
    #Changes Background
    Scene=tk.Label(MainFrame, image=VillageScene)
    Scene.place(x=0, y=0, width=500, height=frameHeight)
    Scene.after(1000, IntroduceVillageOne)
    
    #Resets Text Area
    ClearText()

######Second Battle######
def BattleSceneTwo():
    #After Victory
    def VictoryContinue():
        Level=LEVEL.get()
        Health=(HEALTH.get()+50)
        HEALTH.set(Health)
        Health_Label=tk.Label(MainFrame, text="Health: " + str(Health) + str(" / 100"), font="Fixedsys", bg="darkgray")
        Health_Label.place(x=780, y=25, height=35, width=175)
        Message9=tk.Label(MainFrame, text=("You are now level " + str(Level) + "!"), font="Fixedsys", bg="darkgray")
        Message9.place(x=560, y=150)
        Message9.after(2000, Bosspath)
        
    #Victory
    def Victory():
        ClearText()
        Scene=tk.Label(MainFrame, image=FirstBossDefeat)
        Scene.place(x=0, y=0, width=500, height=frameHeight)
        Message7=tk.Label(MainFrame, text="You have survived!", font="Fixedsys", bg="darkgray")
        Message7.place(x=560, y=100)
        Message8=tk.Label(MainFrame, text="You have gained 100 EXP and leveled up!", font="Fixedsys", bg="darkgray")
        Level=(LEVEL.get()+1)
        LEVEL.set(Level)
        Message8.place(x=560, y=125)
        Message8.after(2000, VictoryContinue)

    #Move Two Response
    def MoveTwoResponse():
        Choice=(int(CHOICE.get()))
        if Choice==0:
            Warn=tk.messagebox.showwarning("Error", "You must pick an action to continue")
            
        elif Choice==1:
            ClearChoice()
            EHEALTH.set(0)
            EHealth=(EHEALTH.get())
            Message5=tk.Label(MainFrame, text="You attack the goblin for 50 DMG...", font="Fixedsys", bg="darkgray")
            Message5.place(x=560, y=275)
            Message6=tk.Label(MainFrame, text="The goblin now has " + str(EHealth) + " health!", font="Fixedsys", bg="darkgray")
            Message6.place(x=560, y=300)
            Message6.after(2000, Victory)
            
        elif Choice==2:
           ClearChoice()
           Message5=tk.Label(MainFrame, text="You try to talk to the goblin but it's no use!", font="Fixedsys", bg="darkgray")
           Message5.place(x=560, y=275)
           Message6=tk.Label(MainFrame, text="The goblin strikes you down. You have died.", font="Fixedsys", bg="darkgray")
           Message6.place(x=560, y=300)
           Message6.after(2000, GameOver)

        elif Choice==3:
            ClearChoice()
            Message5=tk.Label(MainFrame, text="You run past the goblin and avoid danger!", font="Fixedsys", bg="darkgray")
            Message5.place(x=560, y=275)
            Message5.after(2000, Victory)
            
    #Player's second action
    def BattleChoiceTwo():
        CHOICE.set(0)
        Message1=tk.Label(MainFrame, text="What will be your second move?", font="Fixedsys 10 italic", bg="darkgray")
        Message1.place(x=560, y=250)
        Battle=tk.Radiobutton(MainFrame, text="Attack", font="Fixedsys", bg="darkgray", variable=CHOICE, value=1)
        Battle.place(x=560, y=360, height=60, width=190)
        Talk=tk.Radiobutton(MainFrame, text="Talk", font="Fixedsys", bg="darkgray", variable=CHOICE, value=2)
        Talk.place(x=760, y=360, height=60, width=190)
        Run=tk.Radiobutton(MainFrame, text="Run", font="Fixedsys", bg="darkgray", variable=CHOICE, value=3)
        Run.place(x=560, y=430, height=60, width=190)
        Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", fg="red", command=MoveTwoResponse)
        Submit.place(x=760, y=430, height=60, width=190)
        
    #Goblin Move One
    def GoblinMoveOne():
        Health=(HEALTH.get()-25)
        HEALTH.set(Health)
        Health_Label=tk.Label(MainFrame, text="Health: " + str(Health) + str(" / 100"), font="Fixedsys", bg="darkgray")
        Health_Label.place(x=780, y=25, height=35, width=175)
        Message4=tk.Label(MainFrame, text="The goblin attacks you back for 25 DMG", font="Fixedsys", bg="darkgray")
        Message4.place(x=560, y=225)
        Message4.after(2000, BattleChoiceTwo)
        
    #Move One Response
    def MoveOneResponse():
        Choice=(int(CHOICE.get()))
        if Choice==0:
            Warn=tk.messagebox.showwarning("Error", "You must pick an action to continue")
            
        elif Choice==1:
            ClearChoice()
            EHEALTH.set(50)
            EHealth=(EHEALTH.get())
            Message2=tk.Label(MainFrame, text="You attack the goblin for 50 DMG...", font="Fixedsys", bg="darkgray")
            Message2.place(x=560, y=175)
            Message3=tk.Label(MainFrame, text="The goblin now has " + str(EHealth) + " health left!", font="Fixedsys", bg="darkgray")
            Message3.place(x=560, y=200)
            Message3.after(2000, GoblinMoveOne)
            
        elif Choice==2:
           ClearChoice()
           Message2=tk.Label(MainFrame, text="You try to talk to the goblin but it's no use!", font="Fixedsys", bg="darkgray")
           Message2.place(x=560, y=175)
           Message3=tk.Label(MainFrame, text="The goblin strikes you down. You have died.", font="Fixedsys", bg="darkgray")
           Message3.place(x=560, y=200)
           Message3.after(2000, GameOver)

        elif Choice==3:
            ClearChoice()
            Message2=tk.Label(MainFrame, text="You run past the goblin and avoid danger!", font="Fixedsys", bg="darkgray")
            Message2.place(x=560, y=175)
            Message2.after(2000, Victory)
            
            
    #Player's first action
    def BattleChoiceOne():
        CHOICE.set(0)
        Message1=tk.Label(MainFrame, text="What will be your first move?", font="Fixedsys 10 italic", bg="darkgray")
        Message1.place(x=560, y=150)
        Battle=tk.Radiobutton(MainFrame, text="Attack", font="Fixedsys", bg="darkgray", variable=CHOICE, value=1)
        Battle.place(x=560, y=360, height=60, width=190)
        Talk=tk.Radiobutton(MainFrame, text="Talk", font="Fixedsys", bg="darkgray", variable=CHOICE, value=2)
        Talk.place(x=760, y=360, height=60, width=190)
        Run=tk.Radiobutton(MainFrame, text="Run", font="Fixedsys", bg="darkgray", variable=CHOICE, value=3)
        Run.place(x=560, y=430, height=60, width=190)
        Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", fg="red", command=MoveOneResponse)
        Submit.place(x=760, y=430, height=60, width=190)
        
    #First Message
    def ContinuedIntroduction():
        ContinueIntro=tk.Label(MainFrame, text="It wants to battle!", font="Fixedsys 10 italic", bg="darkgray")
        ContinueIntro.place(x=560, y=125)
        ContinueIntro.after(2000, BattleChoiceOne)
    
    #Introduces the player to the second boss
    def IntroduceMonsterOne():
        IntroductionMonsterOne=tk.Label(MainFrame, text="You encounter a scary goblin...", font="Fixedsys 10 italic", bg="darkgray")
        IntroductionMonsterOne.place(x=560, y=100)
        IntroductionMonsterOne.after(2000, ContinuedIntroduction)
        
    #Changes Background
    Scene=tk.Label(MainFrame, image=FirstBossAlive)
    Scene.place(x=0, y=0, width=500, height=frameHeight)
    Scene.after(1000, IntroduceMonsterOne)
    
    #Resets Text Area
    ClearText()
    
######Second Path######
def PathTwo():
    #Continues game after user selects path
    def Continue():
        Choice=(int(CHOICE.get()))
        if Choice==1:
            ClearChoice()
            Message4=tk.Label(MainFrame, text="You have chosen the abandoned path", font="Fixedsys 10 bold", bg="darkgray")
            Message4.place(x=560, y=200)
            Message4.after(2000, VillageSceneTwo)
        elif Choice==2:
            ClearChoice()
            Message4=tk.Label(MainFrame, text="You have chosen the sunny path", font="Fixedsys 10 bold", bg="darkgray")
            Message4.place(x=560, y=200)
            Message4.after(2000, BattleSceneTwo)
        else:
            Warn=tk.messagebox.showwarning("Error", "Please select your path")
            
    #Show the buttons
    def PathChoose():
        CHOICE.set(0)        
        LeftPath=tk.Radiobutton(MainFrame, text="The Abandoned Road", font="Fixedsys", variable=CHOICE, value=1)
        LeftPath.place(x=560, y=360, width=185, height=30)
        RightPath=tk.Radiobutton(MainFrame, text="The Sunny Path", font="Fixedsys", variable=CHOICE, value=2)
        RightPath.place(x=765, y=360, width=185, height=30)        
        Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", command=Continue)
        Submit.place(x=720, y=400)
    #Describes the first path
    def DescribePaths():
        Message2=tk.Label(MainFrame, text="An abandoned road filled with debris?", font="Fixedsys", bg="darkgray")
        Message2.place(x=560, y=125)
        Middle=tk.Label(MainFrame, text="Or", font="Fixedsys", bg="darkgray")
        Middle.place(x=560, y=150)
        Message3=tk.Label(MainFrame, text="A beautiful path with plenty of sun?", font="Fixedsys", bg="darkgray")
        Message3.place(x=560, y=175)
        Message3.after(1000, PathChoose)
    #Describes the area
    def DescribeScene1():
        Message1=tk.Label(MainFrame, text="You come across two paths again.", font="Fixedsys 10 italic", bg="darkgray")
        Message1.place(x=560, y=100)
        Message1.after(2000, DescribePaths)

    #Changes Background
    Scene=tk.Label(MainFrame, image=PathScene)
    Scene.place(x=0, y=0, width=500, height=frameHeight)
    Scene.after(1000, DescribeScene1)
    
    #Resets Text Area
    ClearText()
    
        
######First Fight######
def BattleSceneOne():
    #After Victory
    def VictoryContinue():
        Level=LEVEL.get()
        Health=(HEALTH.get()+50)
        HEALTH.set(Health)
        Health_Label=tk.Label(MainFrame, text="Health: " + str(Health) + str(" / 100"), font="Fixedsys", bg="darkgray")
        Health_Label.place(x=780, y=25, height=35, width=175)
        Message9=tk.Label(MainFrame, text=("You are now level " + str(Level) + "!"), font="Fixedsys", bg="darkgray")
        Message9.place(x=560, y=150)
        Message9.after(2000, PathTwo)
        
    #Victory
    def Victory():
        ClearText()
        Scene=tk.Label(MainFrame, image=FirstBossDefeat)
        Scene.place(x=0, y=0, width=500, height=frameHeight)
        Message7=tk.Label(MainFrame, text="You have survived!", font="Fixedsys", bg="darkgray")
        Message7.place(x=560, y=100)
        Message8=tk.Label(MainFrame, text="You have gained 100 EXP and leveled up!", font="Fixedsys", bg="darkgray")
        Level=(LEVEL.get()+1)
        LEVEL.set(Level)
        Message8.place(x=560, y=125)
        Message8.after(2000, VictoryContinue)

    #Move Two Response
    def MoveTwoResponse():
        Choice=(int(CHOICE.get()))
        if Choice==0:
            Warn=tk.messagebox.showwarning("Error", "You must pick an action to continue")
            
        elif Choice==1:
            ClearChoice()
            EHEALTH.set(0)
            EHealth=(EHEALTH.get())
            Message5=tk.Label(MainFrame, text="You attack the goblin for 50 DMG...", font="Fixedsys", bg="darkgray")
            Message5.place(x=560, y=275)
            Message6=tk.Label(MainFrame, text="The goblin now has " + str(EHealth) + " health!", font="Fixedsys", bg="darkgray")
            Message6.place(x=560, y=300)
            Message6.after(2000, Victory)
            
        elif Choice==2:
           ClearChoice()
           Message5=tk.Label(MainFrame, text="You try to talk to the goblin but it's no use!", font="Fixedsys", bg="darkgray")
           Message5.place(x=560, y=275)
           Message6=tk.Label(MainFrame, text="The goblin strikes you down. You have died.", font="Fixedsys", bg="darkgray")
           Message6.place(x=560, y=300)
           Message6.after(2000, GameOver)

        elif Choice==3:
            ClearChoice()
            Message5=tk.Label(MainFrame, text="You run past the goblin and avoid danger!", font="Fixedsys", bg="darkgray")
            Message5.place(x=560, y=275)
            Message5.after(2000, Victory)
            
    #Player's second action
    def BattleChoiceTwo():
        CHOICE.set(0)
        Message1=tk.Label(MainFrame, text="What will be your second move?", font="Fixedsys 10 italic", bg="darkgray")
        Message1.place(x=560, y=250)
        Battle=tk.Radiobutton(MainFrame, text="Attack", font="Fixedsys", bg="darkgray", variable=CHOICE, value=1)
        Battle.place(x=560, y=360, height=60, width=190)
        Talk=tk.Radiobutton(MainFrame, text="Talk", font="Fixedsys", bg="darkgray", variable=CHOICE, value=2)
        Talk.place(x=760, y=360, height=60, width=190)
        Run=tk.Radiobutton(MainFrame, text="Run", font="Fixedsys", bg="darkgray", variable=CHOICE, value=3)
        Run.place(x=560, y=430, height=60, width=190)
        Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", fg="red", command=MoveTwoResponse)
        Submit.place(x=760, y=430, height=60, width=190)
        
    #Goblin Move One
    def GoblinMoveOne():
        Health=(HEALTH.get()-20)
        HEALTH.set(Health)
        Health_Label=tk.Label(MainFrame, text="Health: " + str(Health) + str(" / 100"), font="Fixedsys", bg="darkgray")
        Health_Label.place(x=780, y=25, height=35, width=175)
        Message4=tk.Label(MainFrame, text="The goblin attacks you back for 20 DMG", font="Fixedsys", bg="darkgray")
        Message4.place(x=560, y=225)
        Message4.after(2000, BattleChoiceTwo)
        
    #Move One Response
    def MoveOneResponse():
        Choice=(int(CHOICE.get()))
        if Choice==0:
            Warn=tk.messagebox.showwarning("Error", "You must pick an action to continue")
            
        elif Choice==1:
            ClearChoice()
            EHEALTH.set(50)
            EHealth=(EHEALTH.get())
            Message2=tk.Label(MainFrame, text="You attack the goblin for 50 DMG...", font="Fixedsys", bg="darkgray")
            Message2.place(x=560, y=175)
            Message3=tk.Label(MainFrame, text="The goblin now has " + str(EHealth) + " health left!", font="Fixedsys", bg="darkgray")
            Message3.place(x=560, y=200)
            Message3.after(2000, GoblinMoveOne)
            
        elif Choice==2:
           ClearChoice()
           Message2=tk.Label(MainFrame, text="You try to talk to the goblin but it's no use!", font="Fixedsys", bg="darkgray")
           Message2.place(x=560, y=175)
           Message3=tk.Label(MainFrame, text="The goblin strikes you down. You have died.", font="Fixedsys", bg="darkgray")
           Message3.place(x=560, y=200)
           Message3.after(2000, GameOver)

        elif Choice==3:
            ClearChoice()
            Message2=tk.Label(MainFrame, text="You run past the goblin and avoid danger!", font="Fixedsys", bg="darkgray")
            Message2.place(x=560, y=175)
            Message2.after(2000, Victory)
            
            
    #Player's first action
    def BattleChoiceOne():
        CHOICE.set(0)
        Message1=tk.Label(MainFrame, text="What will be your first move?", font="Fixedsys 10 italic", bg="darkgray")
        Message1.place(x=560, y=150)
        Battle=tk.Radiobutton(MainFrame, text="Attack", font="Fixedsys", bg="darkgray", variable=CHOICE, value=1)
        Battle.place(x=560, y=360, height=60, width=190)
        Talk=tk.Radiobutton(MainFrame, text="Talk", font="Fixedsys", bg="darkgray", variable=CHOICE, value=2)
        Talk.place(x=760, y=360, height=60, width=190)
        Run=tk.Radiobutton(MainFrame, text="Run", font="Fixedsys", bg="darkgray", variable=CHOICE, value=3)
        Run.place(x=560, y=430, height=60, width=190)
        Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", fg="red", command=MoveOneResponse)
        Submit.place(x=760, y=430, height=60, width=190)
        
    #First Message
    def ContinuedIntroduction():
        ContinueIntro=tk.Label(MainFrame, text="It wants to battle!", font="Fixedsys 10 italic", bg="darkgray")
        ContinueIntro.place(x=560, y=125)
        ContinueIntro.after(2000, BattleChoiceOne)
    
    #Introduces the player to the first monster
    def IntroduceMonsterOne():
        IntroductionMonsterOne=tk.Label(MainFrame, text="You encounter a goblin...", font="Fixedsys 10 italic", bg="darkgray")
        IntroductionMonsterOne.place(x=560, y=100)
        IntroductionMonsterOne.after(2000, ContinuedIntroduction)
        
    #Changes Background
    Scene=tk.Label(MainFrame, image=FirstBossAlive)
    Scene.place(x=0, y=0, width=500, height=frameHeight)
    Scene.after(1000, IntroduceMonsterOne)
    
    #Resets Text Area
    ClearText()
    
######First Village######
def VillageSceneOne():
    #Adds Food
    def ContinueFood():
        ClearChoice()
        #Makes the value of food held global
        Apple=0
        Apple=int(Apple + APPLECHOOSE.get())
        APPLE.set(Apple)

        Bread=0
        Bread=int(Bread + BREADCHOOSE.get())
        BREAD.set(Bread)

        Chicken=0
        Chicken=int(Chicken + CHICKENCHOOSE.get())
        CHICKEN.set(Chicken)

        Message5=tk.Label(MainFrame, text="Good luck on your journey.", font="Fixedsys", bg="darkgray")
        Message5.place(x=560, y=225)
        Message5.after(2000, PathTwo)

    #Fourth Message
    def FourthDialogue():
        Message4=tk.Label(MainFrame, text="I see. Here, choose some food to take with you.", font="Fixedsys", bg="darkgray")
        Message4.place(x=560, y=200)
        AppleChoose=tk.Checkbutton(MainFrame, text="Apple", font="Fixedsys", bg="darkgray", variable=APPLECHOOSE)
        AppleChoose.place(x=560, y=360, height=60, width=190)
        BreadChoose=tk.Checkbutton(MainFrame, text="Bread", font="Fixedsys", bg="darkgray", variable=BREADCHOOSE)
        BreadChoose.place(x=760, y=360, height=60, width=190)
        ChickenChoose=tk.Checkbutton(MainFrame, text="Chicken", font="Fixedsys", bg="darkgray", variable=CHICKENCHOOSE)
        ChickenChoose.place(x=560, y=430, height=60, width=190)
        Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", fg="red", command=ContinueFood)
        Submit.place(x=760, y=430, height=60, width=190)
    #Third Message
    def ThirdDialogue():
        Response=(RESPONSE.get())
        if Response=="":
            Warn=tk.messagebox.showwarning("Error", "Please respond to the villager")
        else:
            ClearChoice()
            Message3=tk.Label(MainFrame, text=("You say to the villager: " + str(Response)), font="Fixedsys 10 italic", bg="darkgray")
            Message3.place(x=560, y=175)
            Message3.after(2000, FourthDialogue)
    #Second Message
    def SecondDialogue():
        Message2=tk.Label(MainFrame, text="What brings you here?", font="Fixedsys", bg="darkgray")
        Message2.place(x=560, y=150)
        Reason=tk.Entry(MainFrame, textvariable=RESPONSE)
        Reason.place(x=560, y=360, height=30, width=390)
        Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", command=ThirdDialogue)
        Submit.place(x=720, y=400)
        
    #First Message
    def FirstDialogue():
        Message1=tk.Label(MainFrame, text="Welcome Traveller!", font="Fixedsys", bg="darkgray")
        Message1.place(x=560, y=125)
        Message1.after(2000, SecondDialogue)
    
    #Introduces the player to the first village
    def IntroduceVillageOne():
        IntroductionVillage=tk.Label(MainFrame, text="You arrive at a lively village", font="Fixedsys 10 italic", bg="darkgray")
        IntroductionVillage.place(x=560, y=100)
        IntroductionVillage.after(2000, FirstDialogue)
        
    #Changes Background
    Scene=tk.Label(MainFrame, image=VillageScene)
    Scene.place(x=0, y=0, width=500, height=frameHeight)
    Scene.after(1000, IntroduceVillageOne)
    
    #Resets Text Area
    ClearText()

######First Paths######    
def PathOne():
    #Continues game after user selects path
    def Continue():
        Choice=(int(CHOICE.get()))
        if Choice==1:
            ClearChoice()
            Message4=tk.Label(MainFrame, text="You have chosen the light path", font="Fixedsys 10 bold", bg="darkgray")
            Message4.place(x=560, y=200)
            Message4.after(2000, VillageSceneOne)
        elif Choice==2:
            ClearChoice()
            Message4=tk.Label(MainFrame, text="You have chosen the dark path", font="Fixedsys 10 bold", bg="darkgray")
            Message4.place(x=560, y=200)
            Message4.after(2000, BattleSceneOne)
        else:
            Warn=tk.messagebox.showwarning("Error", "Please select your path")  
    #Show the buttons
    def PathChoose():
        CHOICE.set(0)        
        LeftPath=tk.Radiobutton(MainFrame, text="The Bright Path", font="Fixedsys", variable=CHOICE, value=1)
        LeftPath.place(x=560, y=360, width=185, height=30)
        RightPath=tk.Radiobutton(MainFrame, text="The Dark Path", font="Fixedsys", variable=CHOICE, value=2)
        RightPath.place(x=765, y=360, width=185, height=30)        
        Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", command=Continue)
        Submit.place(x=720, y=400)
    #Describes the first path
    def DescribePaths():
        Message2=tk.Label(MainFrame, text="A clear bright path with beautiful trees", font="Fixedsys", bg="darkgray")
        Message2.place(x=560, y=125)
        Middle=tk.Label(MainFrame, text="Or", font="Fixedsys", bg="darkgray")
        Middle.place(x=560, y=150)
        Message3=tk.Label(MainFrame, text="A dark gloomy path surrounded by dead trees", font="Fixedsys", bg="darkgray")
        Message3.place(x=560, y=175)
        Message3.after(1000, PathChoose)
    #Describes the area
    def DescribeScene1():
        Message1=tk.Label(MainFrame, text="You come across two paths", font="Fixedsys 10 italic", bg="darkgray")
        Message1.place(x=560, y=100)
        Message1.after(2000, DescribePaths)

    #Changes Background
    Scene=tk.Label(MainFrame, image=PathScene)
    Scene.place(x=0, y=0, width=500, height=frameHeight)
    Scene.after(1000, DescribeScene1)
    
    #Resets Text Area
    ClearText()
    
        
######First Dialouge######
def FirstDialouge():
    Name=(NAME.get())
    #Second Message
    def Message2():
        Message2=tk.Label(MainFrame, text="Can you help me?", font="Fixedsys", bg="darkgray")
        Message2.place(x=560, y=125)
        #Third Action
        def Action3():
            #Fourth Message
            def Message4():
                #Fifth Message
                def Message5():
                    #Seventh Message
                    def Message7():
                        #Eigth Message
                        def Message8():
                            Choice=(int(CHOICE.get()))
                            if Choice==1:
                                Choice1.place_forget()
                                Choice2.place_forget()
                                Submit.place_forget()
                                Message8=tk.Label(MainFrame, text="Thank you! Head down that path over there.", font="Fixedsys", bg="darkgray")
                                Message8.place(x=560, y=225)
                                #Ninth Message
                                Message9=tk.Label(MainFrame, text="It will guide you on your journey.", font="Fixedsys", bg="darkgray")
                                Message9.place(x=560, y=250)
                                Message8.after(3000, PathOne)
                            elif Choice==2:
                                Choice1.place_forget()
                                Choice2.place_forget()
                                Submit.place_forget()
                                Message8=tk.Label(MainFrame, text="I understand. Goodbye.", font="Fixedsys", bg="darkgray")
                                Message8.place(x=560, y=225)
                                Message8.after(2000, QuitAction)
                            else:
                                Warn=tk.messagebox.showwarning("Error", "Please select an option")
                                
                        CHOICE.set(0)
                        Choice1=tk.Radiobutton(MainFrame, text="Yes", font="Fixedsys", variable=CHOICE, value=1)
                        Choice1.place(x=560, y=360, width=185, height=30)
                        Choice2=tk.Radiobutton(MainFrame, text="No", font="Fixedsys", variable=CHOICE, value=2)
                        Choice2.place(x=765, y=360, width=185, height=30)        
                        Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", command=Message8)
                        Submit.place(x=720, y=400)    
                    Message5=tk.Label(MainFrame, text="Our country has been invaded by monsters", font="Fixedsys", bg="darkgray")
                    Message5.place(x=560, y=175)
                    #Sixth Message
                    Message6=tk.Label(MainFrame, text="Will you help us beat them?", font="FixedSys", bg="darkgray")
                    Message6.place(x=560, y=200)
                    Message5.after(1000, Message7)
                Choice=(int(CHOICE.get()))
                if Choice==1:
                    Message4=tk.Label(MainFrame, text="Great!", font="Fixedsys", bg="darkgray")
                    Message4.place(x=560, y=150)
                    Choice1.place_forget()
                    Choice2.place_forget()
                    Submit.place_forget()
                    Message4.after(2000, Message5)
                elif Choice==2:
                    Message4=tk.Label(MainFrame, text="What a shame.", font="Fixedsys", bg="darkgray")
                    Message4.place(x=560, y=150)
                    Choice1.place_forget()
                    Choice2.place_forget()
                    Submit.place_forget()
                    Message4.after(2000, QuitAction)
                else:
                    Warn=tk.messagebox.showwarning("Error", "Please select an option")
                    
            Choice1=tk.Radiobutton(MainFrame, text="Yes", font="Fixedsys", variable=CHOICE, value=1)
            Choice1.place(x=560, y=360, width=185, height=30)
            Choice2=tk.Radiobutton(MainFrame, text="No", font="Fixedsys", variable=CHOICE, value=2)
            Choice2.place(x=765, y=360, width=185, height=30)        
            Submit=tk.Button(MainFrame, text="Submit", font="Fixedsys", bg="darkgray", command=Message4)
            Submit.place(x=720, y=400)
        Message2.after(2000, Action3)

    #First Message
    Message1=tk.Label(MainFrame, text=("Greetings", Name, "!"), font="Fixedsys", bg="darkgray")
    Message1.place(x=560, y=100)
    Message1.after(2000, Message2)

    #Name Label
    Name_Label=tk.Label(MainFrame, text=(Name),
                        font="Fixedsys 20",
                        bg="darkgray")
    Name_Label.place(x=550, y=25, height=35)

    #Health
    Health=(HEALTH.get())
    Health_Label=tk.Label(MainFrame, text="Health: " + str(Health) + str(" / 100"), font="Fixedsys", bg="darkgray")
    Health_Label.place(x=780, y=25, height=35, width=175)

##################################################################

#Set up Frame Widgets
#Name Frame
def setupIntroFrame():
    #Labels
    Name_Label=tk.Label(IntroFrame, text="What is your name?",
                  bg="gray",
                  fg="white",
                  font="Fixedsys 20 bold")
    Name_Label.place(x=375, y=100, width=350)

    #Entry Field
    Name_Entry=tk.Entry(IntroFrame, textvariable=NAME, font="Fixedsys 20")
    Name_Entry.place(x=375, y=150, width=350, height=50)

    #Buttons
    ContinueName=tk.Button(IntroFrame, text="Continue",
                           bg="gray",
                           fg="white",
                           font="Fixedsys",
                           command=showMainFrame)
    ContinueName.place(x=750, y=150, height=50)

#Main Frame
def setupMainFrame():
    #Visuals
    Scene=tk.Label(MainFrame, image=StartingScene)
    Scene.place(x=0, y=0, width=500, height=frameHeight)

    TextArea=tk.Label(MainFrame, text="")
    TextArea.place(x=550, y=75, width=410, height=275)
    TextArea.configure(bg="darkgray")

    ChoiceArea=tk.Label(MainFrame, text="")
    ChoiceArea.place(x=550, y=350, width=410, height=150)
    ChoiceArea.configure(bg="black")

    #Buttons
    QuitButton=tk.Button(MainFrame, text="Quit", font="Fixedsys", bg="red", command=QuitAction)
    QuitButton.place(x=1000, y=400, width=50, height=50)

    InventoryButton=tk.Button(MainFrame, text="Inventory", font="Fixedsys", bg="darkgray", command=OpenInventory)
    InventoryButton.place(x=987, y=200, width=85, height=55)

#Inventory Menu
def setupInventoryFrame():
    #Buttons
    ExitButton=tk.Button(InventoryFrame, text="Back", bg="darkgray", fg="red", font="Fixedsys 12", command=ExitInventory)
    ExitButton.place(x=40, y=40, height=50, width=60)

####### Main Program #######
Main_Window=tk.Tk()
Main_Window.title("Mini RPG")

frameWidth=1100
frameHeight=532
Main_Window.minsize(frameWidth, frameHeight)

#Variables

#Variable Table
#HEALTH-Int-Stores Health of user
#EXP-Int-Stores experience points of user
#CHOICE-Int-Stores user input for questions when prompted (Multiple Choice or Only Two Options)
#NAME-Str-Stores user input for their name
#RESPONSE-Str-Stores user input for questions where they enter their own responses
#APPLE-Int-Stores amount of Apples user has
#CHICKEN-Int-Stores amount of Chicken user has
#BREAD-Int-Stores amount of Bread user has
#EHEALTH-Int-Stores enemy health
#APPLECHOOSE-Int-Stores if user selected apple
#BREADCHOOSE-Int-Stores if user selected bread
#CHICKENCHOOSE-Int-Stores if user selected chicken

HEALTH=tk.IntVar()
HEALTH.set(100)

EXP=tk.IntVar()
EXP.set(0)

LEVEL=tk.IntVar()
LEVEL.set(1)

CHOICE=tk.IntVar()
CHOICE.set(0)

NAME=tk.StringVar()
NAME.set("")

RESPONSE=tk.StringVar()
RESPONSE.set("")

APPLE=tk.IntVar()
APPLE.set(0)

CHICKEN=tk.IntVar()
CHICKEN.set(0)

BREAD=tk.IntVar()
BREAD.set(0)

EHEALTH=tk.IntVar()
EHEALTH.set(100)

APPLECHOOSE=tk.IntVar()
APPLECHOOSE.set(0)

BREADCHOOSE=tk.IntVar()
BREADCHOOSE.set(0)

CHICKENCHOOSE=tk.IntVar()
CHICKENCHOOSE.set(0)


#Creates Frames in top left corner
MainFrame=tk.Frame(Main_Window, width=frameWidth, height=frameHeight)
MainFrame.place(x=0, y=0)
MainFrame.configure(bg="gray")

IntroFrame=tk.Frame(Main_Window, width=frameWidth, height=frameHeight)
IntroFrame.place(x=0, y=0)
IntroFrame.configure(bg="black")

InventoryFrame=tk.Frame(Main_Window, width=frameWidth, height=frameHeight)
InventoryFrame.place(x=0, y=0)
InventoryFrame.configure(bg="gray")

GameOverFrame=tk.Frame(Main_Window, width=frameWidth, height=frameHeight)
GameOverFrame.place(x=0, y=0)
GameOverFrame.configure(bg="black")

EndingFrame=tk.Frame(Main_Window, width=frameWidth, height=frameHeight)
EndingFrame.place(x=0, y=0)
EndingFrame.configure(bg="black")

#Scenes
StartingScene=tk.PhotoImage(file="1 Starting Scene.png")
PathScene=tk.PhotoImage(file="Paths.png")
VillageScene=tk.PhotoImage(file="Village.png")

FirstBossAlive=tk.PhotoImage(file="FirstBossAlive.png")
FirstBossDefeat=tk.PhotoImage(file="FirstBossDefeat.png")
LastBossAlive=tk.PhotoImage(file="LastBossAlive.png")
FinalBossDefeat=tk.PhotoImage(file="FinalBossDefeat.png")
BossPath=tk.PhotoImage(file="BossPath.png")

#Icons
Apples=tk.PhotoImage(file="Apple.png")
Breads=tk.PhotoImage(file="Bread.png")
Chickens=tk.PhotoImage(file="Chicken.png")
Characters=tk.PhotoImage(file="Character.png")

#Set up the frame
setupMainFrame()
setupIntroFrame()
setupInventoryFrame()

#Hides all frames except IntroFrame
MainFrame.place_forget()
InventoryFrame.place_forget()
GameOverFrame.place_forget()
EndingFrame.place_forget()

Main_Window.mainloop()
