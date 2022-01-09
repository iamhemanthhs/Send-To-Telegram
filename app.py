import requests
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title('Save To Telegram')
root.config(bg='#0e1621')
root.geometry('600x70+600+400')
root.iconbitmap('icon.ico')
root.resizable(False,False)

mesgval=StringVar()

def sendmessage():
    message = mesgval.get()
    token = '5022255490:AAFp1MMWKXq84__4VVloMurORNWDZhvwpcs' #Telegram Bot Token
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': {5060166011}, 'text': {message}} #Chat Id of the User
    requests.post(url, data).json()



Frame1=Frame(root,bg='#243142')
Frame1.place(x=520,y=15,width=70,height=40)

sendbtn=Button(Frame1,text='Send',font=('Italic',10,NORMAL),bd=6,bg='#17212b',fg='white',command=sendmessage)
sendbtn.place(x=0,y=0,width=70,height=40)

mesgval=StringVar()

mesgbx = Entry(root, font=('Italic', 13, NORMAL),bg='#17212b',fg='white',insertbackground='white',bd=1, textvariable=mesgval)
mesgbx.place(x=10, y=14,width=500,height=40)

root.mainloop()





