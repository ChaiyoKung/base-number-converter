from tkinter import *
from tkinter import ttk, messagebox





def Convert(event=None):
    txt1.config(state='normal')
    txt1.delete(1.0, END)
    List = []
    Sum = 0
    u = 0
    b = cbb1.get() #<<< Str
    try:
        n = ent1.get() #<<< Str
        n = n.upper()
        for i in n:
            if i == "A":
                i = 10
            if i == "B":
                i = 11
            if i == "C":
                i = 12
            if i == "D":
                i = 13
            if i == "E":
                i = 14
            if i == "F":
                i = 15
            List.append(i)
        List.reverse()
        for x in List:
            Sum = Sum + (int(x)*(int(b)**u))
            u += 1
            
        ######### Split Calulate #########

        List = []
        num = Sum
        b2 = cbb2.get()
        if num == 0:
            his_log = open("history_log.txt","a")
            his_log.write("0\n")
            #print("0",end='')
            his_log.close()
        else:
            while num != 0:
                x = num % int(b2)
                num = num // int(b2)
                if x == 10:
                    x = "A"
                if x == 11:
                    x = "B"
                if x == 12:
                    x = "C"
                if x == 13:
                    x = "D"
                if x == 14:
                    x = "E"
                if x == 15:
                    x = "F"     
                List.append(x)
            List.reverse()
            his_log = open("history_log.txt","a")
            his_log.write(str(n)+" ["+str(b)+"to"+str(b2)+" is] ")
            #print(str(n)+" ["+str(b)+"to"+str(b2)+" is] ",end='')
            for i in List:
                #print(i,end='')
                txt1.insert(END, str(i))
                his_log.write(str(i))
            his_log.write("\n")
            his_log.close()
        txt1.config(state='disable')
        #print("\n")
    except:
        if b=="2":
            messagebox.showerror("Error","You can enter 0 and 1")
        elif b=="8":
            messagebox.showerror("Error","You can enter 0-7")
        elif b=="10":
            messagebox.showerror("Error","You can enter 0-9")
        elif b=="16":
            messagebox.showerror("Error","You can enter 0-9 and A-F")
        else:
            messagebox.showerror("Error","Something error")




    
def His_log():
    global root2
    root2 = Toplevel()
    root2.title("History")
    root2.geometry("660x415")

    hfm = Frame(root2)
    hfm.pack()

    hfm2 = Frame(root2)
    hfm2.pack()

    his_scrbar = Scrollbar(hfm)
    
    txt2 = Text(hfm, yscrollcommand=his_scrbar.set)
    txt2.pack(side=LEFT)

    his = open("history_log.txt","r")
    for t in his:
        txt2.insert(END, t)
    his.close()

    his_scrbar.config(command=txt2.yview)
    his_scrbar.pack(side=LEFT, fill=Y)

    clr_bt = Button(hfm2, text='Clear', command=ClearHis, padx=10, bg='#ffa6bc')
    clr_bt.pack()
    
    root2.mainloop()




    
def ClearHis():
    his = open("history_log.txt","w")
    his.truncate(0)
    his.close()

    root2.destroy()
    
base_box = []
for bs in range(2,16+1,1):
	base_box.append(bs)


root = Tk()
root.title("Base Number Converter")
root.geometry("500x150")

fm = Frame(root)
fm.place(anchor=S, x=250, y=60)

fm2 = Frame(root)
fm2.place(anchor=CENTER, x=250, y=75)

fm3 = Frame(root)
fm3.place(anchor=N, x=250, y=90)

lb1 = Label(fm, text="Select base and Enter number")
lb1.pack(side=TOP)

cbb1 = ttk.Combobox(fm, values=base_box, width=3)
cbb1.set(10)
cbb1.pack(side=LEFT)

ent1 = Entry(fm)
ent1.pack(side=LEFT)

cnv_bt = Button(fm2, text="Convert to", padx=10, bg="#007FFF", fg='white', bd=1, relief="solid", command=Convert)
cnv_bt.bind_all('<Return>', Convert)
cnv_bt.pack()

cbb2 = ttk.Combobox(fm3, values=base_box, width=3)
cbb2.set(2)
cbb2.pack(side=LEFT)

txt1 = Text(fm3, height=1, width=50, state='disabled')
txt1.pack(side=LEFT)

his_bt = Button(root, text="History", command=His_log)
his_bt.pack(side=BOTTOM)

root.mainloop()
