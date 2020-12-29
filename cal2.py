from tkinter import*
from tkinter.messagebox import*
import math
window = Tk()
# active function to make operaion
def clck(event):
    print('button clicked......')
    b=event.widget
    text =b['text']
    print(text)
    if text =='<==':
        fetc = textfield.get()
        fet = fetc[:-1]
        print(fet)
        textfield.delete(0,END)
        textfield.insert(0,fet)
        return
    if text == 'AC':
        textfield.delete(0,END)
        return
    if text =='x':
        textfield.insert(END,'*')
        return
    if text =='=':
        try:
            fetch = textfield.get()
            if '^' in fetch:
                k = fetch.replace('^', '**')
                print()
                k = eval(k)
                textfield.delete(0, END)
                textfield.insert(0, k)
                return
            ans = eval(fetch)
            textfield.delete(0, END)
            textfield.insert(0, ans)
        except Exception as e:
            print('Error is',e)
            showerror('Error is:',e)
        return ;
    textfield.insert(END,text)
def rut():
    k=textfield.get()
    k=eval(k)
    k=math.sqrt(k)
    textfield.delete(0, END)
    textfield.insert(0, k)
def crut():
    k=textfield.get()
    k=eval(k)
    k=k**(1/3)
    textfield.delete(0, END)
    textfield.insert(0,k)
def lo():
    k = textfield.get()
    k = eval(k)
    k = math.log(k,2)
    textfield.delete(0, END)
    textfield.insert(0, k)
def exp():
    k = textfield.get()
    k = eval(k)
    k = math.exp(k)
    textfield.delete(0, END)
    textfield.insert(0, k)

window.title('my calculator')
window.maxsize(width=690,height=550) # widthxheight
window.minsize(width=690,height=550)
#picture label
fon = ('Algerian',10,'bold underline')
pic = PhotoImage(file='img/cal2.png')
headlabel = Label(window,image=pic) #text = 'my label'
headlabel.pack(side = TOP,pady=6)
headlabel= Label(window, text='MY CALCULATOR',font = fon )
headlabel.pack(side=TOP)
fan = ('Algerian',28,'bold ')
#for text field
textfield = Entry(window,font = fan,justify= RIGHT)
textfield.pack(side = TOP,pady= 6,fill = X,padx=10)
#for making frame of buttons
buttonFrame = Frame(window)
buttonFrame.pack(side = TOP)
k=1
for i in range(3):
    for j in range(3):
        btn = Button(buttonFrame, text=k, font=fan,width = 4,relief = 'raised',activebackground = 'black',activeforeground = 'red')
        btn.grid(row=i, column=j,pady =3 ,padx=3)
        btn.bind('<Button-1>',clck)
        k+=1
btn1 = Button(buttonFrame, text='.', font=fan,width = 4,relief = 'raised',activebackground = 'black',activeforeground = 'red')
btn1.grid(row=3, column=0,pady =3 ,padx=3)
btn2 = Button(buttonFrame, text=0, font=fan, width=4, relief='raised',activebackground = 'black',activeforeground = 'red')
btn2.grid(row=3, column=1, pady=3, padx=3)
btn3 = Button(buttonFrame, text='=', font=fan, width=4, relief='raised',activebackground = 'black',activeforeground = 'red')
btn3.grid(row=3, column=2, pady=3, padx=3)
btnplus = Button(buttonFrame, text='+', font=fan, width=4, relief='raised',activebackground = 'black',activeforeground = 'red')
btnplus.grid(row=0, column=3, pady=3, padx=3)
btnminus = Button(buttonFrame, text='-', font=fan, width=4, relief='raised',activebackground = 'black',activeforeground = 'red')
btnminus.grid(row=1, column=3, pady=3, padx=3)
btnmul = Button(buttonFrame, text='x', font=fan, width=4, relief='raised',activebackground = 'black',activeforeground = 'red')
btnmul.grid(row=2, column=3, pady=3, padx=3)
btndiv = Button(buttonFrame, text='/', font=fan, width=4, relief='raised',activebackground = 'black',activeforeground = 'red')
btndiv.grid(row=3, column=3, pady=3, padx=3)
dele = Button(buttonFrame, text='<==', font=fan, width=9, relief='raised',activebackground = 'black',activeforeground = 'red')
dele.grid(row=4, column=0, pady=3, padx=3,columnspan = 2)
allclear = Button(buttonFrame, text='AC', font=fan, width=9, relief='raised',activebackground = 'black',activeforeground = 'red')
allclear.grid(row=4, column=2, pady=3, padx=3,columnspan =2)
mod = Button(buttonFrame,text='%',font=fan,width=4 ,relief='raised',activebackground='black',activeforeground='red')
mod.grid(row=0,column=4,pady=3,padx=3)
root = Button(buttonFrame,text=' √',font=fan,width=4,relief='raised',activebackground='black',activeforeground='red',command=rut)
root.grid(row=1,column=4,pady=3,padx=3)
croot = Button(buttonFrame,text='3√',font=fan,width=4,relief='raised',activebackground='black',activeforeground='red',command=crut)
croot.grid(row=2,column=4,pady=3,padx=3)
power = Button(buttonFrame,text='^',font=fan,width=4,relief='raised',activebackground='black',activeforeground='red')
power.grid(row=3,column=4,pady=3,padx=3)
power.bind('<Button-1>',clck)
log = Button(buttonFrame,text='log',font=fan,width=4,relief='raised',activebackground='black',activeforeground='red',command=lo)
log.grid(row=4,column=4,pady=3,padx=3)
expo = Button(buttonFrame,text='e',font=('Baveuse',21,'bold'),width=4,relief='raised',activebackground='black',activeforeground='red',command=exp)
expo.grid(row=0,column=5,pady=3,padx=3)
rob= Button(buttonFrame,text='(',font=fan,width=4,relief='raised',activebackground='black',activeforeground='red')
rob.grid(row=1,column=5,pady=3,padx=3)
lob = Button(buttonFrame,text=')',font=fan,width=4,relief='raised',activebackground='black',activeforeground='red')
lob.grid(row=2,column=5,pady=3,padx=3)
ze = Button(buttonFrame,text='00',font=fan,width=4,relief='raised',activebackground='black',activeforeground='red')
ze.grid(row=3,column=5,pady=3,padx=3)
zee = Button(buttonFrame,text='000',font=fan,width=4,relief='raised',activebackground='black',activeforeground='red')
zee.grid(row=4,column=5,pady=3,padx=3)
mod.bind('<Button-1>',clck)
power.bind('<Button-1>',clck)
rob.bind('<Button-1>',clck)
lob.bind('<Button-1>',clck)
ze.bind('<Button-1>',clck)
zee.bind('<Button-1>',clck)
btn1.bind('<Button-1>',clck)
btn2.bind('<Button-1>',clck)
btn3.bind('<Button-1>',clck)
btnplus.bind('<Button-1>',clck)
btnminus.bind('<Button-1>',clck)
btnmul.bind('<Button-1>',clck)
btndiv.bind('<Button-1>',clck)
dele.bind('<Button-1>',clck)
allclear.bind('<Button-1>',clck)
window.mainloop() #this function used to show window again and again\
