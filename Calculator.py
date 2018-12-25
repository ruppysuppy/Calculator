#Basic Calculator
#Created on: 25/12/2018 05:02 pm

#version 0.0.1: Created the basic layout for the Calculator
#Updated on: 25/12/2018 05:21 pm

#Importing Modules

from tkinter import *

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

#Frames for Each Element

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
frameBack = Frame(frame_inner , bg=col)
frameDot = Frame(frame_inner , bg=col)
frameEqual = Frame(frame_inner , bg=col)

#Adding Frames for Utility

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
frame0.grid(row = 6 , column = 1 , sticky = N+E+S+W , columnspan = 2 , padx = 5 , pady = 5)
frameC.grid(row = 3 , column = 4 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameBack.grid(row = 4 , column = 4 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameDot.grid(row = 6 , column = 3 , sticky = N+E+S+W , padx = 5 , pady = 5)
frameEqual.grid(row = 5 , column = 4 , sticky = N+E+S+W , padx = 5 , pady = 5 , rowspan = 2)

#Mainloop
                
Window.mainloop()