import tkinter as tk
def greet_user(name_entry=None):
    name = name_entry.get()  # Access entered text from the entry widget
    print(f"Hello, {name}!")

def create_button_window():
    window = tk.Tk()
    window.title("Enter Your Name")

    label = tk.Label(window, text="Please enter your name:")
    label.pack()

    name_entry = tk.Entry(window)
    name_entry.pack()

    greet_button = tk.Button(window, text="Greet Me", command=greet_user)  # Link button to function
    greet_button.pack()

    window.mainloop()

create_button_window()
