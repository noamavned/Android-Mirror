import tkinter as tk
from tkinter import messagebox
import socket
import os

# Function to validate IP address
def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

# Function to run adb commands and capture terminal output
def run_command(command):
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, f"Running command: {command}\n")
    log_text.yview(tk.END)
    log_text.config(state=tk.DISABLED)
    os.system(command)

# Function that will run when the button is clicked
def run_function():
    ip = ip_entry.get()
    if is_valid_ip(ip):
        run_command("adb kill-server")
        run_command("adb tcpip 5555")
        run_command(f"adb connect {ip}:5555")
        run_command("adb devices")
        run_command("adb devices")
        run_command("scrcpy")
    else:
        messagebox.showerror("Invalid IP", "Please enter a valid IP address.")

# Create main window
root = tk.Tk()
root.title("IP Address Validator")
root.geometry("500x400")  # Adjusted for log space
root.resizable(False, False)
root.configure(bg="#f4f4f9")

frame = tk.Frame(root, bg="#f4f4f9")
frame.pack(pady=20)

ip_label = tk.Label(frame, text="Enter IP Address:", font=("Helvetica", 14), bg="#f4f4f9", fg="#333")
ip_label.grid(row=0, column=0, pady=10)

ip_entry = tk.Entry(frame, width=25, font=("Helvetica", 12), bd=2, relief="solid", borderwidth=2)
ip_entry.grid(row=1, column=0, pady=10)

# Function to handle hover effect
def on_hover(event, button_type):
    if button_type == "submit":
        submit_button.config(bg="#5bc0de", fg="white")
        submit_button.config(cursor="hand2")
    elif button_type == "exit":
        exit_button.config(bg="#5bc0de", fg="white")
        exit_button.config(cursor="hand2")

# Function to handle leave effect
def on_leave(event, button_type):
    if button_type == "submit":
        submit_button.config(bg="#0275d8", fg="white")
        submit_button.config(cursor="arrow")
    elif button_type == "exit":
        exit_button.config(bg="#0275d8", fg="white")
        exit_button.config(cursor="arrow")

submit_button = tk.Button(frame, text="Start Mirroring", font=("Helvetica", 12), bg="#0275d8", fg="white", 
                           width=20, height=2, relief="flat", command=run_function)
submit_button.grid(row=2, column=0, pady=20)

exit_button = tk.Button(frame, text="Exit", font=("Helvetica", 12), bg="#0275d8", fg="white", 
                         width=20, height=2, relief="flat", command=root.quit)
exit_button.grid(row=3, column=0, pady=20)

# Create log Text widget for output
log_text = tk.Text(root, height=10, width=60, font=("Courier New", 10), bd=2, relief="solid", wrap=tk.WORD, state=tk.DISABLED, bg="#f4f4f9", fg="#333")
log_text.pack(pady=10)

# Bind hover and leave events with appropriate arguments
submit_button.bind("<Enter>", lambda event: on_hover(event, "submit"))
submit_button.bind("<Leave>", lambda event: on_leave(event, "submit"))
exit_button.bind("<Enter>", lambda event: on_hover(event, "exit"))
exit_button.bind("<Leave>", lambda event: on_leave(event, "exit"))

root.mainloop()
