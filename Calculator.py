from tkinter import *
def click(event):
    current_text = event.widget.cget("text")
    if current_text == "=":
        try:
            result = eval(entrybox.get())
            entrybox.delete(0, END)
            entrybox.insert(END, str(result))
        except Exception as e:
            entrybox.delete(0, END)
            entrybox.insert(END, "Error")
    elif current_text == "C":
        entrybox.delete(0, END)
    else:
        entrybox.insert(END, current_text)

root = Tk()
root.title("Basic Calculator")

entrybox = Entry(root, font=("Poppins", 20), justify="right")
entrybox.grid(row=0, column=0, columnspan=4)

buttons = [
    "9", "8", "7", "+",
    "6", "5", "4", "-",
    "3", "2", "1", "*",
    "0", "C", "=", "/"
]

r= 1
c= 0
for button in buttons:
    btn =Button(root, text=button, font=("Poppins", 20),bg="white", padx=20, pady=10)
    btn.grid(row=r, column=c)
    c += 1
    if c > 3:
        c = 0
        r += 1

    btn.bind("<Button-1>", click)

root.mainloop()