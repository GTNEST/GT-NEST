import tkinter as tk
from tkinter import messagebox
import random

# Simulated temperature (random for now)
def get_temperature():
    return round(random.uniform(18.0, 28.0), 1)

# Switch to dashboard screen
def show_dashboard():
    login_frame.pack_forget()
    dashboard_frame.pack(fill="both", expand=True)
    update_temp()

# Switch back to login screen
def logout():
    dashboard_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

# Handle login button click
def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    # You could validate here if needed
    if username and password:
        show_dashboard()
    else:
        messagebox.showwarning("Login Failed", "Please enter both username and password.")

# Toggle light
def toggle_light():
    if light_button.config('text')[-1] == 'Turn On Light':
        light_button.config(text='Turn Off Light', bg='yellow')
        light_status.config(text='Light is ON', fg='green')
    else:
        light_button.config(text='Turn On Light', bg='gray')
        light_status.config(text='Light is OFF', fg='red')

# Toggle alarm
def toggle_alarm():
    if alarm_button.config('text')[-1] == 'Activate Alarm':
        alarm_button.config(text='Deactivate Alarm', bg='red')
        alarm_status.config(text='Alarm is ON', fg='red')
    else:
        alarm_button.config(text='Activate Alarm', bg='gray')
        alarm_status.config(text='Alarm is OFF', fg='green')

# Update temperature every 3 seconds
def update_temp():
    temp = get_temperature()
    temp_label.config(text=f"Temperature: {temp}°C")
    if dashboard_frame.winfo_ismapped():
        root.after(3000, update_temp)

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("🏠 Smart Home App")
root.geometry("350x400")
root.resizable(False, False)

# ----- LOGIN SCREEN -----
login_frame = tk.Frame(root)

login_title = tk.Label(login_frame, text="Login", font=("Arial", 16, "bold"))
login_title.pack(pady=20)

tk.Label(login_frame, text="Username").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack(pady=5)

tk.Label(login_frame, text="Password").pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(login_frame, text="Login", width=15, command=handle_login)
login_button.pack(pady=20)

login_frame.pack(fill="both", expand=True)

# ----- DASHBOARD SCREEN -----
dashboard_frame = tk.Frame(root)

title = tk.Label(dashboard_frame, text="Smart Home Dashboard", font=("Arial", 16, "bold"))
title.pack(pady=10)

light_button = tk.Button(dashboard_frame, text="Turn On Light", width=20, command=toggle_light, bg='gray')
light_button.pack(pady=5)
light_status = tk.Label(dashboard_frame, text="Light is OFF", font=("Arial", 12), fg='red')
light_status.pack()

alarm_button = tk.Button(dashboard_frame, text="Activate Alarm", width=20, command=toggle_alarm, bg='gray')
alarm_button.pack(pady=5)
alarm_status = tk.Label(dashboard_frame, text="Alarm is OFF", font=("Arial", 12), fg='green')
alarm_status.pack()

temp_label = tk.Label(dashboard_frame, text="Temperature: --°C", font=("Arial", 14))
temp_label.pack(pady=20)

back_button = tk.Button(dashboard_frame, text="← Logout", command=logout)
back_button.pack(pady=10)

# Start GUI loop
root.mainloop()
