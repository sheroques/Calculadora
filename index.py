from tkinter import *
from tkinter import ttk

color1 = '#050505' #black
color2 = '#faf5f5' #white
color3 = '#abe1f5' #blue
color4 = '#b8c3d4' #grey
color5 = '#f5d75f' #orange

window =Tk ()
window.title('Calculadora')
window.geometry('235x310')
window.config( bg = color1)

frame_screen = Frame(window,widt=235, height=50, bg=color3)
frame_screen.grid(row=0, column=0)
frame_body = Frame(window,widt=235, height=268)
frame_body.grid(row=1, column=0)


#calc main code
value_text=StringVar()
total_values =''
def value_enter(event):
    global total_values
    total_values  = total_values + str(event)
    value_text.set(total_values)

def calc():
    result=eval(total_values)
    value_text.set(str(result))

def clean():
    global total_values
    total_values=''
    value_text.set('')


#label

app_label = Label(frame_screen, textvariable=value_text, width = 16, height= 2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('audiowide 18'), bg=color3)
app_label.place(x=0,y=0)

#buttons first line 
b1 = Button(frame_body, text='C', width=11, height=2, bg=color4, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command=clean )
b1.place(x=0, y=0)
b2 = Button(frame_body, text='%', width=5, height=2, bg=color4, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('%'))
b2.place(x=120, y=0)
b3 = Button(frame_body, text='/', width=5, height=2, bg=color5, fg=color2, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('/') )
b3.place(x=180, y=0)

#buttons second line
b4 = Button(frame_body, text='7', width=5, height=2, bg=color4, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('7'))
b4.place(x=0, y=52)
b5= Button(frame_body, text='8', width=5, height=2, bg=color4, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('8'))
b5.place(x=60, y=52)
b6 = Button(frame_body, text='9', width=5, height=2, bg=color4, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('9'))
b6.place(x=120, y=52)
b7 = Button(frame_body, text='#', width=5, height=2, bg=color5, fg= color2, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('#'))
b7.place(x=180, y=52)

#buttons third line
b8 = Button(frame_body, text='4', width=5, height=2, bg=color4, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('4'))
b8.place(x=0, y=104)
b9= Button(frame_body, text='5', width=5, height=2, bg=color4, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('5'))
b9.place(x=60, y=104)
b10 = Button(frame_body, text='6', width=5, height=2, bg=color4, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('6'))
b10.place(x=120, y=104)
b11 = Button(frame_body, text='-', width=5, height=2, bg=color5, fg= color2, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('-'))
b11.place(x=180, y=104)

#buttons fourth line
b12 = Button(frame_body, text='1', width=5, height=2, bg=color4, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('1'))
b12.place(x=0, y=156)
b13= Button(frame_body, text='2', width=5, height=2, bg=color4, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('2'))
b13.place(x=60, y=156)
b14 = Button(frame_body, text='3', width=5, height=2, bg=color4, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('3'))
b14.place(x=120, y=156)
b15 = Button(frame_body, text='+', width=5, height=2, bg=color5, fg= color2, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('+'))
b15.place(x=180, y=156)

#buttons fifth line
b16 = Button(frame_body, text='0', width=11, height=2, bg=color4, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('0'))
b16.place(x=0, y=208)
b17= Button(frame_body, text='.', width=5, height=2, bg=color4, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= lambda: value_enter('.'))
b17.place(x=120, y=208)
b18 = Button(frame_body, text='=', width=5, height=2, bg=color4, font=('audiowide 13 bold'), relief= RAISED, overrelief=RIDGE, command= calc)
b18.place(x=180, y=209)







window.mainloop()


