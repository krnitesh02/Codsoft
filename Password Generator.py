import tkinter as tk
import random
import string
def generate_password():
    password_len = int(length_entry.get())
    if password_len < 8:
        password_label.config(text="Password length should be at least 8 characters")
    else:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(password_len))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
window = tk.Tk()
window.title("Password Generator")


length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()
password_label = tk.Label(window, text="")
password_label.pack()
password_entry = tk.Entry(window)
password_entry.pack()

window.mainloop()