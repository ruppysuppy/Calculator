#Basic Calculator
#Created on: 25/12/2018 05:02 pm

#version 0.0.1: Created the Basic Layout for the Calculator
#Updated on: 25/12/2018 05:21 pm

#version 0.0.2: Completed the Layout
#Updated on: 25/12/2018 06:29 pm

#version 0.0.3: Added Functionality of Buttons (C , = , DEL left)
#Updated on: 25/12/2018 07:05 pm

#version 0.0.4: Added Functionality of C , = and DEL Buttons
#Updated on: 25/12/2018 07:17 pm

#version 0.0.5: Completed polishing of Basic Calculator
#Updated on: 25/12/2018 07:31 pm

#version 0.0.6: Completed Scientific Calculator
#Updated on: 26/12/2018 09:35 am

#version 0.0.7: Updated UI and polished it up
#Updated on: 26/12/2018 09:38 am

#version 0.0.8: Made the Algorith more efficient (using approximation)
#Updated on: 26/12/2018 09:46 am


#Importing Modules

from tkinter import *
from math import *

#Variables

col = 'gray80' #Used to set the overall background colour
shouldAdd = True #Used as flag to check when to clear the text field

#Functions

#function for updating the calculator whenever a button is pressed

def updateEntry(character):
    #getting the global value of shouldAdd
    global shouldAdd
    #Checking whether shouldAdd is False, if so clearing the text field
    if (shouldAdd == False):
        C()
    #enabling the text entry modification
    entry.config(state = NORMAL)
    #geting the data and modifying it to add the character of the pressed button
    data = (entry.get("1.0", END)).rstrip('\n') + character
    #deleting what was in the text-box
    entry.delete('1.0', END)
    #inserting the modified data
    entry.insert(END, data)
    #disabling the text entry modification
    entry.config(state = DISABLED)

#function for deleting what was in the text-box

def C():
    #getting the global value of shouldAdd
    global shouldAdd
    #Changing shouldAdd to True
    shouldAdd = True
    #enabling the text entry modification
    entry.config(state = NORMAL)
    #deleting what was in the text-box
    entry.delete('1.0', END)
    #disabling the text entry modification
    entry.config(state = DISABLED)

def DEL():
    #getting the global value of shouldAdd
    global shouldAdd
    #Checking whether shouldAdd is False, if so clearing the text field
    if (shouldAdd == False):
        C()
    #enabling the text entry modification
    entry.config(state = NORMAL)
    #geting the data and modifying it to delete the last character
    data = (entry.get("1.0", END)).rstrip('\n')
    data = data[:-1:]
    #deleting what was in the text-box
    entry.delete('1.0', END)
    #inserting the modified data
    entry.insert(END, data)
    #disabling the text entry modification
    entry.config(state = DISABLED)

def evaluate():
    #getting the global value of shouldAdd
    global shouldAdd
    #Changing shouldAdd to False
    shouldAdd = False
    #enabling the text entry modification
    entry.config(state = NORMAL)
    #geting the data and modifying it to delete the last character
    data = (entry.get("1.0", END)).rstrip('\n')

    #evaluating the solution
    try:
        solution = eval (data)
        solint = int(solution)
        solfloat = solution -solint
        if (solfloat <= 0.005):
            solfloat = 0
        solution = solfloat + solint
        solution = str(solution)
    except:
        solution = 'Syntax Error\n'

    #creating the required data
    data = data + '\n=' + solution

    #deleting what was in the text-box
    entry.delete('1.0', END)
    #inserting the modified data
    entry.insert(END, data)
    #disabling the text entry modification
    entry.config(state = DISABLED)

#Creating The Main Window

Window=Tk()
Window.title('Calculator')

#Outline On The Side

frame_outer = Frame(Window , bg = 'black')
frame_outer.pack(fill = 'both' , expand = True , padx = 5 , pady = 5)

frame_inner = Frame(frame_outer, bg=col)
frame_inner.pack(fill = 'both' , expand = True , padx = 2 , pady = 2)

#Text-field for User input and output

entry = Text(frame_inner , font = ('arial' , 25 , 'bold') , width = 50 , height = 3)
entry.grid(row = 1 , column = 1 , sticky = N + E + S+ W , columnspan = 7 , padx = 10 , pady = 5)
entry.config(state = DISABLED)

#Frames For Each Element

framePlus = Frame(frame_inner , bg=col)
frameMinus = Frame(frame_inner , bg=col)
frameMultiply = Frame(frame_inner , bg=col)
frameDivide = Frame(frame_inner , bg=col)
frame1 = Frame(frame_inner , bg=col)
frame2 = Frame(frame_inner , bg=col)
frame3 = Frame(frame_inner , bg=col)
frame4 = Frame(frame_inner , bg=col)
frame5 = Frame(frame_inner , bg=col)
frame6 = Frame(frame_inner , bg=col)
frame7 = Frame(frame_inner , bg=col)
frame8 = Frame(frame_inner , bg=col)
frame9 = Frame(frame_inner , bg=col)
frame0 = Frame(frame_inner , bg=col)
frameC = Frame(frame_inner , bg=col)
frameDEL = Frame(frame_inner , bg=col)
frameDot = Frame(frame_inner , bg=col)
frameEqual = Frame(frame_inner , bg=col)
frameOpB = Frame(frame_inner , bg=col)
frameClB = Frame(frame_inner , bg=col)
framesin = Frame(frame_inner , bg=col)
frameasin = Frame(frame_inner , bg=col)
framecos = Frame(frame_inner , bg=col)
frameacos = Frame(frame_inner , bg=col)
frametan = Frame(frame_inner , bg=col)
frameatan = Frame(frame_inner , bg=col)
framepi = Frame(frame_inner , bg=col)
framee = Frame(frame_inner , bg=col)
framelog10 = Frame(frame_inner , bg=col)
framelog = Frame(frame_inner , bg=col)
framepow = Frame(frame_inner , bg=col)
framefact = Frame(frame_inner , bg=col)
framemod = Frame(frame_inner , bg=col)

#Adding Frames (For Clean UI Elements)

framePlus.grid(row = 2 , column = 1 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameMinus.grid(row = 2 , column = 2 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameMultiply.grid(row = 2 , column = 3 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameDivide.grid(row = 2 , column = 4 , sticky = N+E+S+W , padx = 5 , pady = 5)
frame1.grid(row = 5 , column = 1 , sticky = N+E+S+W , padx = 5 , pady = 5)
frame2.grid(row = 5 , column = 2 , sticky = N+E+S+W , padx = 5 , pady = 5)
frame3.grid(row = 5 , column = 3 , sticky = N+E+S+W , padx = 5 , pady = 5)
frame4.grid(row = 4 , column = 1 , sticky = N+E+S+W , padx = 5 , pady = 5)
frame5.grid(row = 4 , column = 2 , sticky = N+E+S+W , padx = 5 , pady = 5)
frame6.grid(row = 4 , column = 3 , sticky = N+E+S+W , padx = 5 , pady = 5)
frame7.grid(row = 3 , column = 1 , sticky = N+E+S+W , padx = 5 , pady = 5)
frame8.grid(row = 3 , column = 2 , sticky = N+E+S+W , padx = 5 , pady = 5)
frame9.grid(row = 3 , column = 3 , sticky = N+E+S+W , padx = 5 , pady = 5)
frame0.grid(row = 6 , column = 1 , sticky = N+E+S+W , padx = 5 , pady = 5 , columnspan = 2)
frameC.grid(row = 3 , column = 4 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameDEL.grid(row = 4 , column = 4 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameDot.grid(row = 6 , column = 3 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameEqual.grid(row = 6 , column = 6 , sticky = N+E+S+W , padx = 5 , pady = 5 , columnspan = 2)
frameOpB.grid(row = 5 , column = 4 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameClB.grid(row = 5 , column = 5 , sticky = N+E+S+W , padx = 5 , pady = 5)
framesin.grid(row = 2 , column = 5 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameasin.grid(row = 2 , column = 6 , sticky = N+E+S+W , padx = 5 , pady = 5)
framecos.grid(row = 3 , column = 5 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameacos.grid(row = 3 , column = 6 , sticky = N+E+S+W , padx = 5 , pady = 5)
frametan.grid(row = 4 , column = 5 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameatan.grid(row = 4 , column = 6 , sticky = N+E+S+W , padx = 5 , pady = 5)
framepi.grid(row = 6 , column = 4 , sticky = N+E+S+W , padx = 5 , pady = 5)
framee.grid(row = 6 , column = 5 , sticky = N+E+S+W , padx = 5 , pady = 5)
framelog10.grid(row = 5 , column = 6 , sticky = N+E+S+W , padx = 5 , pady = 5)
framelog.grid(row = 5 , column = 7 , sticky = N+E+S+W , padx = 5 , pady = 5)
framepow.grid(row = 2 , column = 7 , sticky = N+E+S+W , padx = 5 , pady = 5)
framefact.grid(row = 3 , column = 7 , sticky = N+E+S+W , padx = 5 , pady = 5)
framemod.grid(row = 4 , column = 7 , sticky = N+E+S+W , padx = 5 , pady = 5)

#Creating the Buttons

buttonPlus = Button(framePlus , text = '+' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('+'))
buttonMinus = Button(frameMinus , text = '-' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('-'))
buttonMultiply = Button(frameMultiply , text = '*' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('*'))
buttonDivide = Button(frameDivide , text = '/' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('/'))
button1 = Button(frame1 , text = '1' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('1'))
button2 = Button(frame2 , text = '2' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('2'))
button3 = Button(frame3 , text = '3' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('3'))
button4 = Button(frame4 , text = '4' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('4'))
button5 = Button(frame5 , text = '5' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('5'))
button6 = Button(frame6 , text = '6' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('6'))
button7 = Button(frame7 , text = '7' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('7'))
button8 = Button(frame8 , text = '8' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('8'))
button9 = Button(frame9 , text = '9' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('9'))
button0 = Button(frame0 , text = '0' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('0'))
buttonC = Button(frameC , text = 'C' , font = ('arial' , 13 , 'bold') , command = C)
buttonDEL = Button(frameDEL , text = 'DEL' , font = ('arial' , 13 , 'bold') , command = DEL)
buttonDot = Button(frameDot , text = '.' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('.'))
buttonEqual = Button(frameEqual , text = '=' , font = ('arial' , 13 , 'bold') , command = evaluate)
buttonOpB = Button(frameOpB , text = '(' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('('))
buttonClB = Button(frameClB , text = ')' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry(')'))
buttonpi = Button(framepi , text = 'pi' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('pi'))
buttone = Button(framee , text = 'e' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('e'))
buttonsin = Button(framesin , text = 'sin' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('sin('))
buttonasin = Button(frameasin , text = 'asin' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('asin('))
buttoncos = Button(framecos , text = 'cos' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('cos('))
buttonacos = Button(frameacos , text = 'acos' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('acos('))
buttontan = Button(frametan , text = 'tan' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('tan('))
buttonatan = Button(frameatan , text = 'atan' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('atan('))
buttonlog10 = Button(framelog10 , text = 'log10' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('log10('))
buttonlog = Button(framelog , text = 'log' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('log('))
buttonpow = Button(framepow , text = 'x^y' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('**'))
buttonfact = Button(framefact , text = 'x!' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('factorial('))
buttonmod = Button(framemod , text = '|x|' , font = ('arial' , 13 , 'bold') , command = lambda: updateEntry('abs('))

#Packing The Buttons

buttonPlus.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonMinus.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonMultiply.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonDivide.pack(padx = 2 , pady = 2 , fill = BOTH)
button1.pack(padx = 2 , pady = 2 , fill = BOTH)
button2.pack(padx = 2 , pady = 2 , fill = BOTH)
button3.pack(padx = 2 , pady = 2 , fill = BOTH)
button4.pack(padx = 2 , pady = 2 , fill = BOTH)
button5.pack(padx = 2 , pady = 2 , fill = BOTH)
button6.pack(padx = 2 , pady = 2 , fill = BOTH)
button7.pack(padx = 2 , pady = 2 , fill = BOTH)
button8.pack(padx = 2 , pady = 2 , fill = BOTH)
button9.pack(padx = 2 , pady = 2 , fill = BOTH)
button0.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonC.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonDEL.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonDot.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonEqual.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonOpB.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonClB.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonpi.pack(padx = 2 , pady = 2 , fill = BOTH)
buttone.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonsin.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonasin.pack(padx = 2 , pady = 2 , fill = BOTH)
buttoncos.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonacos.pack(padx = 2 , pady = 2 , fill = BOTH)
buttontan.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonatan.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonlog10.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonlog.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonpow.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonfact.pack(padx = 2 , pady = 2 , fill = BOTH)
buttonmod.pack(padx = 2 , pady = 2 , fill = BOTH)

#Mainloop
                
Window.mainloop()
