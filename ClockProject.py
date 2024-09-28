import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import time
import threading
from playsound import playsound

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock Application")
        self.root.geometry("400x200")
        
        self.create_main_window()

    def create_main_window(self):
        # Display Current Time
        self.clock_label = tk.Label(self.root, font=("Helvetica", 24))
        self.clock_label.pack(pady=20)
        self.update_clock()

        # Buttons for Alarm, Timer, and Stopwatch
        tk.Button(self.root, text="Stopwatch", command=self.open_stopwatch_window).pack(pady=5)
        tk.Button(self.root, text="Timer", command=self.open_timer_window).pack(pady=5)
        tk.Button(self.root, text="Alarm", command=self.open_alarm_window).pack(pady=5)

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

    # Stopwatch Window
    def open_stopwatch_window(self):
        self.stopwatch_window = tk.Toplevel(self.root)
        self.stopwatch_window.title("Stopwatch")
        self.stopwatch_time = 0
        self.stopwatch_running = False

        self.stopwatch_label = tk.Label(self.stopwatch_window, text="0", font=("Helvetica", 24))
        self.stopwatch_label.pack(pady=20)

        start_button = tk.Button(self.stopwatch_window, text="Start", command=self.start_stopwatch)
        start_button.pack(side=tk.LEFT, padx=20)

        pause_button = tk.Button(self.stopwatch_window, text="Pause", command=self.pause_stopwatch)
        pause_button.pack(side=tk.LEFT, padx=20)

        reset_button = tk.Button(self.stopwatch_window, text="Reset", command=self.reset_stopwatch)
        reset_button.pack(side=tk.LEFT, padx=20)

        back_button = tk.Button(self.stopwatch_window, text="Back", command=self.stopwatch_window.destroy)
        back_button.pack(side=tk.LEFT, padx=20)

    def start_stopwatch(self):
        if not self.stopwatch_running:
            self.stopwatch_running = True
            self.update_stopwatch()

    def pause_stopwatch(self):
        self.stopwatch_running = False

    def reset_stopwatch(self):
        self.stopwatch_running = False
        self.stopwatch_time = 0
        self.stopwatch_label.config(text="0")

    def update_stopwatch(self):
        if self.stopwatch_running:
            self.stopwatch_time += 1
            self.stopwatch_label.config(text=str(self.stopwatch_time))
            self.stopwatch_window.after(1000, self.update_stopwatch)

    # Timer Window
    def open_timer_window(self):
        self.timer_window = tk.Toplevel(self.root)
        self.timer_window.title("Timer")
        self.timer_running = False

        self.timer_label = tk.Label(self.timer_window, text="Set Timer (sec):", font=("Helvetica", 14))
        self.timer_label.pack(pady=20)

        self.timer_entry = tk.Entry(self.timer_window, font=("Helvetica", 14))
        self.timer_entry.pack()

        start_button = tk.Button(self.timer_window, text="Start", command=self.start_timer)
        start_button.pack(side=tk.LEFT, padx=20)

        pause_button = tk.Button(self.timer_window, text="Pause", command=self.pause_timer)
        pause_button.pack(side=tk.LEFT, padx=20)

        reset_button = tk.Button(self.timer_window, text="Reset", command=self.reset_timer)
        reset_button.pack(side=tk.LEFT, padx=20)

        back_button = tk.Button(self.timer_window, text="Back", command=self.timer_window.destroy)
        back_button.pack(side=tk.LEFT, padx=20)

    def start_timer(self):
        if not self.timer_running:
            try:
                self.timer_seconds = int(self.timer_entry.get())
                self.timer_entry.config(state='disabled')
                self.timer_running = True
                self.update_timer()
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid number of seconds.")

    def pause_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.timer_seconds = 0
        self.timer_entry.config(state='normal')
        self.timer_label.config(text="Set Timer (sec):")

    def update_timer(self):
        if self.timer_running and self.timer_seconds > 0:
            self.timer_seconds -= 1
            self.timer_label.config(text=f"Time left: {self.timer_seconds} sec")
            self.timer_window.after(1000, self.update_timer)
        elif self.timer_seconds == 0:
            messagebox.showinfo("Timer", "Time's up!")
            self.reset_timer()

    # Alarm Window
    def open_alarm_window(self):
        self.alarm_window = tk.Toplevel(self.root)
        self.alarm_window.title("Alarm")

        tk.Label(self.alarm_window, text="Set Alarm (HH:MM:SS):", font=("Helvetica", 14)).pack(pady=20)
        self.alarm_entry = tk.Entry(self.alarm_window, font=("Helvetica", 14))
        self.alarm_entry.pack()

        set_alarm_button = tk.Button(self.alarm_window, text="Set Alarm", command=self.set_alarm)
        set_alarm_button.pack(pady=10)

        back_button = tk.Button(self.alarm_window, text="Back", command=self.alarm_window.destroy)
        back_button.pack()

    def set_alarm(self):
        alarm_time = self.alarm_entry.get()
        try:
            time.strptime(alarm_time, '%H:%M:%S')
            threading.Thread(target=self.alarm_thread, args=(alarm_time,)).start()
            messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter time in HH:MM:SS format.")

    def alarm_thread(self, alarm_time):
        while True:
            current_time = time.strftime("%H:%M:%S")
            if current_time == alarm_time:
                playsound("alarm_sound.mp3")  # Play the alarm sound
                messagebox.showinfo("Alarm", "Time to wake up!")
                break
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()
