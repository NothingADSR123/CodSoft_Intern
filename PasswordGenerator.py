import random
import tkinter as tk
from tkinter import simpledialog, messagebox

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def show_password(password):
    # Create a new window to display the password
    password_window = tk.Toplevel(root)
    password_window.title("Generated Password")
    
    tk.Label(password_window, text="Your Generated Password:").pack(pady=10)
    tk.Label(password_window, text=password, font=("Helvetica", 16, "bold")).pack(pady=10)
    
    tk.Button(password_window, text="Close", command=password_window.destroy).pack(pady=10)

def main():
    global root
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt the user for the desired password length
    length = simpledialog.askinteger("Input", "Enter the desired length of the password:", minvalue=1, maxvalue=100)
    
    if length:
        password = generate_password(length)
        show_password(password)

if __name__ == "__main__":
    main()
    tk.mainloop()
 
 