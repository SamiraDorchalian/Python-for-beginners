from tkinter import *
import os

root=Tk()
root.title('Shotdown App')
root.geometry('400x580')


#first button
restart_time_button=PhotoImage(file='resert-time.png')
first_button=Button(root,image=restart_time_button,borderwidth=0,cursor='hand2',command=restarttime)
first_button.place(x=10,y=10)

#second button
close_button=PhotoImage(file='close.png')

second_button=Button(root,image=close_button,borderwidth=0,cursor='hand2',command=root.destroy)
second_button.place(x=200,y=10)

#third button
restart_button=PhotoImage(file='restart.png')

third_button=Button(root,image=restart_button,borderwidth=0,cursor='hand2',command=restart)
third_button.place(x=10,y=200)

#fouth button
shutdown_button=PhotoImage(file='shutdown.png')

fouth_button=Button(root,image=shutdown_button,borderwidth=0,cursor='hand2',command=shutdown)
fouth_button.place(x=200,y=200)

#fifth button
logouot_button=PhotoImage(file='log-out.png')

fifth_button=Button(root,image=logouot_button,borderwidth=0,cursor='hand2',command=logout)
fifth_button.place(x=10,y=400)


root.mainloop()