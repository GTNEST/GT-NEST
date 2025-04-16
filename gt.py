import tkinter as tk
from tkinter import messagebox
import random


def get_temperature():
    return round(random.uniform(18.0, 28.0), 1)

def show_dashboard():
    login_frame.pack_forget()
    dashboard_frame.pack(fill="both", expand=True)
    update_temp()


def logout():
    dashboard_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)


def handle_login():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        show_dashboard()
    else:
        messagebox.showwarning("Login Failed", "Please both username and password.")

# def handle_signup():



# this section is for the function on the actual dashboard

def toggle_light():
    if light_button.config('text')[-1] == 'Turn On Light':
        light_button.config(text='Turn off Light', bg='yellow')
        light_status.config(text='Light is ON', fg='green')
    else:
        light_button.config(text='Turn On Light', bg='gray')
        light_status.config(text='Light is OFF', fg='red')


def toggle_alarm():
    if alarm_button.config('text')[-1] == 'Activate Alarm':
        alarm_button.config(text='Deactivate Alarm', bg='red')
        alarm_status.config(text='Alarm is ON', fg='red')
    else:
        alarm_button.config(text='Activate Alarm', bg='gray')
        alarm_status.config(text='Alarm is OFF', fg='green')


def update_temp():
    temp = get_temperature()
    temp_label.config(text=f"Temperature: {temp}°C")
    if dashboard_frame.winfo_ismapped():
        root.after(3000, update_temp)

root = tk.Tk()
root.title("GT AUTOMATION/MANAGEMENT SYSTEM")
root.geometry("1260x750")
root.resizable(False, False)


login_frame = tk.Frame(root)
# reminder to add background color root,background='group color'

login_title = tk.Label(login_frame, text="GT NEST LOGIN", font=("Arial", 16, "bold"))
login_title.pack(pady=20)

tk.Label(login_frame, text="Enter Username").pack()
username_entry = tk.Entry(login_frame,width=35)
username_entry.pack(pady=5)

tk.Label(login_frame, text="Enter Password").pack()
password_entry = tk.Entry(login_frame, show="*",width=35)
password_entry.pack(pady=5)

login_button = tk.Button(login_frame, text="Login", width=34, command=handle_login)
login_button.pack(pady=20)

# signup_button = tk.Button(login_frame, text="SignUp", width=34, command=handle_login)
# login_button.pack(pady=20)

login_frame.pack(fill="both", expand=True)

# /this is after the login screen when the user logs in correctly it will display the dashboard
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


root.mainloop()
