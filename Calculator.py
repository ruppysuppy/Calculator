#Basic Calculator
#Created on: 25/12/2018 05:02 pm

#version 0.0.1: Created the Basic Layout for the Calculator
#Updated on: 25/12/2018 05:21 pm

#version 0.0.2: Completed the Layout
#Updated on: 25/12/2018 06:29 pm

#version 0.0.3: Added Functionality of Buttons (C , = , DEL left)
#Updated on: 25/12/2018 07:05 pm


#Importing Modules

from tkinter import *
from math import *

#Functions

#function for updating the calculator whenever a button is pressed

def updateEntry(character):
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

#Variables

col = 'gray80'

#Creating The Main Window

Window=Tk()
Window.title('Calculator')

#Outline On The Side

frame_outer = Frame(Window , bg = 'black')
frame_outer.pack(fill = 'both' , expand = True , padx = 5 , pady = 5)

frame_inner = Frame(frame_outer, bg=col)
frame_inner.pack(fill = 'both' , expand = True , padx = 2 , pady = 2)

#Text-field for User input and output

entry = Text(frame_inner , width = 50 , height = 4)
entry.grid(row = 1 , column = 1 , sticky = N + E + S+ W , columnspan = 4 , padx = 10 , pady = 5)
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
frame0.grid(row = 6 , column = 1 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameC.grid(row = 3 , column = 4 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameDEL.grid(row = 4 , column = 4 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameDot.grid(row = 6 , column = 2 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameEqual.grid(row = 5 , column = 4 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameOpB.grid(row = 6 , column = 3 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameClB.grid(row = 6 , column = 4 , sticky = N+E+S+W , padx = 5 , pady = 5)

#Creating the Buttons

buttonPlus = Button(framePlus , text = '+' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('+'))
buttonMinus = Button(frameMinus , text = '-' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('-'))
buttonMultiply = Button(frameMultiply , text = 'X' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('X'))
buttonDivide = Button(frameDivide , text = '/' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('/'))
button1 = Button(frame1 , text = '1' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('1'))
button2 = Button(frame2 , text = '2' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('2'))
button3 = Button(frame3 , text = '3' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('3'))
button4 = Button(frame4 , text = '4' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('4'))
button5 = Button(frame5 , text = '5' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('5'))
button6 = Button(frame6 , text = '6' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('6'))
button7 = Button(frame7 , text = '7' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('7'))
button8 = Button(frame8 , text = '8' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('8'))
button9 = Button(frame9 , text = '9' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('9'))
button0 = Button(frame0 , text = '0' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('0'))
buttonC = Button(frameC , text = 'C' , font = ('arial' , 15 , 'bold'))
buttonDEL = Button(frameDEL , text = 'DEL' , font = ('arial' , 15 , 'bold'))
buttonDot = Button(frameDot , text = '.' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('.'))
buttonEqual = Button(frameEqual , text = '=' , font = ('arial' , 15 , 'bold'))
buttonOpB = Button(frameOpB , text = '(' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry('('))
buttonClB = Button(frameClB , text = ')' , font = ('arial' , 15 , 'bold') , command = lambda: updateEntry(')'))

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

#Mainloop
                
Window.mainloop()