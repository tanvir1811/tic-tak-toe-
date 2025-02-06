from tkinter import *
from tkinter import messagebox
b = Tk()
clicked = True
count = 0


def c(event):

    v = i.get()
    r = k.get()
    b.destroy()
    if v == "sam":
        if r == "won123":
            u = Tk()

            def m(event):
                u.destroy()
                r = Tk()
                r.title("Tic tac toe game")
                r.geometry("900x450")


                def e():
                    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
                        messagebox.showinfo("Tic tac toe game", "X is winner")
                    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
                        messagebox.showinfo("Tic tac toe game", "X is winner")
                    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
                        messagebox.showinfo("Tic tac toe game", "X is winner")
                    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
                        messagebox.showinfo("Tic tac toe game", "X is winner")
                    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
                        messagebox.showinfo("Tic tac toe game", "X is winner")
                    elif b3["text"] == "X" and b6 == "X" and b9 == "X":
                        messagebox.showinfo("Tic tac toe game", "X is winner")
                    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
                        messagebox.showinfo("Tic tac toe game", "X is winner")
                    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
                        messagebox.showinfo("Tic tac toe game", "X is winner")
                    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
                        messagebox.showinfo("Tic tac toe game", "O is winner")
                    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
                        messagebox.showinfo("Tic tac toe game", "O is winner")
                    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
                        messagebox.showinfo("Tic tac toe game", "O is winner")
                    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
                        messagebox.showinfo("Tic tac toe game", "O is winner")
                    elif b2["text"] == "O" and b5 == "O" and b8["text"] == "O":
                        messagebox.showinfo("Tic tac toe game", "O is winner")
                    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
                        messagebox.showinfo("Tic tac toe game", "O is winner")
                    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
                        messagebox.showinfo("Tic tac toe game", "O is winner")
                    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
                        messagebox.showinfo("Tic tac toe game", "O is winner")

                def b_click(b):

                    global count, clicked

                    if b["text"] == "  " and clicked == True:
                        b["text"] = "X"
                        clicked = False
                        count += 1
                        e()

                    elif b["text"] == "  " and clicked == False:
                        b["text"] = "O"
                        clicked = True
                        count += 1
                        e()

                    else:
                        messagebox.showerror("Tic tac toe game", "The button is taken ")

                b1 = Button(r, text="  ", width="7", font="lucid 50 bold", bg="light green", command=lambda: b_click(b1))
                b2 = Button(r, text="  ", width="7", font="lucid 50 bold", bg="light green", command=lambda: b_click(b2))
                b3 = Button(r, text="  ", width="7", font="lucid 50 bold", bg="light green", command=lambda: b_click(b3))
                b4 = Button(r, text="  ", width="7", font="lucid 50 bold", bg="light green", command=lambda: b_click(b4))
                b5 = Button(r, text="  ", width="7", font="lucid 50 bold", bg="light green", command=lambda: b_click(b5))
                b6 = Button(r, text="  ", width="7", font="lucid 50 bold", bg="light green", command=lambda: b_click(b6))
                b7 = Button(r, text="  ", width="7", font="lucid 50 bold", bg="light green", command=lambda: b_click(b7))
                b8 = Button(r, text="  ", width="7", font="lucid 50 bold", bg="light green", command=lambda: b_click(b8))
                b9 = Button(r, text="  ", width="7", font="lucid 50 bold", bg="light green", command=lambda: b_click(b9))
                b1.grid(column=0, row=0)
                b2.grid(column=0, row=1)
                b3.grid(column=0, row=2)
                b4.grid(column=1, row=0)
                b5.grid(column=1, row=1)
                b6.grid(column=1, row=2)

                b7.grid(column=2, row=0)
                b8.grid(column=2, row=1)
                b9.grid(column=2, row=2)

                r.mainloop()

            u.geometry("1000x500")
            q = Label(u, text="login successful", bg="light green", font="lucid 50 bold")
            w = Label(u, text="Welcome to the game", bg="Sky blue", font="lucid 30 bold")
            y = Button(u, text="Enter", bg="Sky blue", font="lucid 30 bold")
            y.bind("<Button-1>", m)
            q.pack()
            w.pack()
            y.pack()
            u.mainloop()

        else:
            u = Tk()
            u.geometry("1000x500")
            q = Label(u, text="Password is incorrect", bg="light green", font="lucid 50 bold")
            q.pack()
            u.mainloop()
    else:

        if r == "won123":
            u = Tk()
            u.geometry("1000x500")
            q = Label(u, text="Username is incorrect", bg="light green", font="lucid 50 bold")
            q.pack()
            u.mainloop()
        else:
            u = Tk()
            u.geometry("1000x500")
            q = Label(u, text="Both are incorrect", bg="light green", font="lucid 50 bold")
            q.pack()
            u.mainloop()


b.title("Tic tac toe game")
b.geometry("1000x500")
h = Frame(b, bg="orange", width="1500", height="10")
g = Label(b, text="Enter your user id", bg="sky blue", font="Lucid 30 bold ")
o = Label(b, text="Enter your password", bg="sky blue", font="Lucid 30 bold ")
f = StringVar()
p = StringVar()
p.set("")
f.set("")
i = Entry(b, bg="light green", font="lucid 20 bold ", textvariable=f)
k = Entry(b, bg="light green", font="lucid 20 bold ", textvariable=p)
j = Button(b, bg="light green", text="Enter", font="lucid 30 bold")
j.bind("<Button-1>", c)
h.pack()
g.pack()
i.pack()
o.pack()
k.pack()
j.pack()
b.mainloop()
