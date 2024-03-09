import tkinter as tk
import random
import string
def generate_password(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters)for _ in range(length))
    return password
def generate_and_diplay_password():
    try:
        length=int(entry_length.get())
        if length<=0:
            result_label.config(text="please enter a positive length.")
            return
        pasword=generate_password(length)
        result_label.config(text="generated password:"+pasword)
    except ValueError:
        result_label.config(text="invalid input. please enter a valid number.")
window=tk.Tk()
window.title("password generator")

entry_length=tk.Entry(window)
entry_length.grid(row=0,column=0,padx=10,pady=10)

generate_button=tk.Button(window,text="generate password",command=generate_and_diplay_password)
generate_button.grid(row=1,column=0,pady=10)

result_label=tk.Label(window,text="")
result_label.grid(row=2,column=0,pady=10)

window.mainloop()