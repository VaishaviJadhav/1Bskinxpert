import tkinter as tk
from tkinter import ttk, font
from PIL import Image, ImageTk
import datetime
import os
from pathlib import Path
import random

class SkinXpertRoutine(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configure window for HP Victus (full screen)
        self.title("SkinXpert - Your Personalized Skincare Routine")
        self.attributes('-fullscreen', True)
        
        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Colors
        self.bg_color = "#F5F5F5"  # Light background
        self.accent_color = "#E8C4C4"  # Soft pink
        self.text_color = "#4A4A4A"  # Dark gray
        self.highlight_color = "#D14D72"  # Deeper pink for highlights
        self.card_bg = "#FFFFFF"  # White for cards
        
        # Load custom font
        self.custom_font = ("Helvetica", 12)
        self.header_font = ("Helvetica", 28, "bold")
        self.subheader_font = ("Helvetica", 16)
        self.button_font = ("Helvetica", 12, "bold")
        
        # Configure the main frame
        self.configure(bg=self.bg_color)
        
        # Create and place widgets
        self.create_widgets()
        
        # Sample routine data
        self.routine = [
            {"time": "Morning", "steps": [
                {"name": "Gentle Cleanser", "desc": "Wash face with lukewarm water", "completed": False, "image": "cleanser.png"},
                {"name": "Toner", "desc": "Apply with cotton pad", "completed": False, "image": "toner.png"},
                {"name": "Vitamin C Serum", "desc": "3-4 drops on face and neck", "completed": False, "image": "serum.png"},
                {"name": "Moisturizer", "desc": "Apply evenly across face", "completed": False, "image": "moisturizer.png"},
                {"name": "Sunscreen", "desc": "SPF 50, reapply every 2 hours", "completed": False, "image": "sunscreen.png"}
            ]},
            {"time": "Evening", "steps": [
                {"name": "Makeup Remover", "desc": "If wearing makeup", "completed": False, "image": "makeup_remover.png"},
                {"name": "Cleanser", "desc": "Double cleanse recommended", "completed": False, "image": "cleanser.png"},
                {"name": "Exfoliant", "desc": "Use 2-3 times per week", "completed": False, "image": "exfoliant.png"},
                {"name": "Treatment", "desc": "Retinol or targeted treatment", "completed": False, "image": "treatment.png"},
                {"name": "Night Cream", "desc": "Apply generously", "completed": False, "image": "night_cream.png"}
            ]}
        ]
        
        # Populate routine
        self.display_routine()
        
        # Start streak counter
        self.streak = random.randint(5, 15)  # Sample streak
        self.streak_label.config(text=f"Current Streak: {self.streak} days")
        
    def create_widgets(self):
        # Top navigation bar
        self.top_frame = tk.Frame(self, bg=self.accent_color, height=70)
        self.top_frame.pack(fill=tk.X)
        
        # App title
        self.title_label = tk.Label(self.top_frame, text="SkinXpert", font=self.header_font, 
                                    bg=self.accent_color, fg=self.text_color)
        self.title_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Home button (using text as placeholder, would use image in production)
        self.home_button = tk.Button(self.top_frame, text="🏠", font=("Helvetica", 22), 
                                     bg=self.accent_color, fg=self.text_color, 
                                     relief=tk.FLAT, command=self.go_home)
        self.home_button.pack(side=tk.RIGHT, padx=20, pady=10)
        
        # Date display
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        self.date_label = tk.Label(self, text=current_date, font=self.subheader_font, 
                                  bg=self.bg_color, fg=self.text_color)
        self.date_label.pack(pady=(20, 5))
        
        # Motivational message
        motivational_messages = [
            "Your future skin will thank you for your consistency today!",
            "Small steps every day lead to amazing skin transformations.",
            "Self-care isn't selfish, it's essential. You deserve this time.",
            "Skincare isn't just about looking good, it's about feeling good too."
        ]
        
        self.motivation_label = tk.Label(self, text=random.choice(motivational_messages), 
                                        font=self.subheader_font, bg=self.bg_color, 
                                        fg=self.highlight_color, wraplength=800)
        self.motivation_label.pack(pady=(5, 20))
        
        # Streak counter and progress frame
        self.progress_frame = tk.Frame(self, bg=self.bg_color)
        self.progress_frame.pack(fill=tk.X, padx=50, pady=10)
        
        self.streak_label = tk.Label(self.progress_frame, text="Current Streak: 0 days", 
                                    font=self.subheader_font, bg=self.bg_color, fg=self.highlight_color)
        self.streak_label.pack(side=tk.LEFT)
        
        # Progress bar
        self.progress_var = tk.DoubleVar(value=0.6)  # Sample progress (60%)
        self.progress = ttk.Progressbar(self.progress_frame, variable=self.progress_var, 
                                        length=400, mode='determinate', 
                                        style="TProgressbar")
        self.progress.pack(side=tk.RIGHT, pady=10)
        
        # Style the progressbar
        style = ttk.Style()
        style.configure("TProgressbar", thickness=20, troughcolor=self.accent_color, 
                        background=self.highlight_color)
        
        # Container for routine cards
        self.routine_container = tk.Frame(self, bg=self.bg_color)
        self.routine_container.pack(padx=50, pady=20, fill=tk.BOTH, expand=True)
        
    def display_routine(self):
        # Clear any existing widgets
        for widget in self.routine_container.winfo_children():
            widget.destroy()
            
        # Create frames for morning and evening routines
        morning_frame = tk.Frame(self.routine_container, bg=self.card_bg, 
                                padx=20, pady=20, relief=tk.RIDGE, bd=1)
        morning_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        evening_frame = tk.Frame(self.routine_container, bg=self.card_bg, 
                                padx=20, pady=20, relief=tk.RIDGE, bd=1)
        evening_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        # Configure grid
        self.routine_container.grid_columnconfigure(0, weight=1)
        self.routine_container.grid_columnconfigure(1, weight=1)
        self.routine_container.grid_rowconfigure(0, weight=1)
        
        # Display morning routine
        tk.Label(morning_frame, text="Morning Routine", font=self.subheader_font, 
                bg=self.card_bg, fg=self.highlight_color).pack(pady=(0, 15))
        
        self.create_routine_steps(morning_frame, self.routine[0]["steps"])
        
        # Display evening routine
        tk.Label(evening_frame, text="Evening Routine", font=self.subheader_font, 
                bg=self.card_bg, fg=self.highlight_color).pack(pady=(0, 15))
        
        self.create_routine_steps(evening_frame, self.routine[1]["steps"])
        
        # Add button to mark all as completed
        completion_frame = tk.Frame(self, bg=self.bg_color)
        completion_frame.pack(pady=20)
        
        complete_button = tk.Button(completion_frame, text="Mark All Completed", 
                                   font=self.button_font, bg=self.highlight_color, 
                                   fg="white", padx=15, pady=8, relief=tk.FLAT,
                                   command=self.mark_all_completed)
        complete_button.pack(side=tk.LEFT, padx=10)
        
        reset_button = tk.Button(completion_frame, text="Reset Routine", 
                               font=self.button_font, bg=self.accent_color, 
                               fg=self.text_color, padx=15, pady=8, relief=tk.FLAT,
                               command=self.reset_routine)
        reset_button.pack(side=tk.LEFT, padx=10)
        
        # Progress updates and reminders
        reminder_frame = tk.Frame(self, bg=self.bg_color)
        reminder_frame.pack(pady=10, fill=tk.X, padx=50)
        
        # Water reminder
        water_label = tk.Label(reminder_frame, text="💧 Don't forget to drink water!", 
                              font=self.custom_font, bg=self.bg_color, fg=self.text_color)
        water_label.pack(side=tk.LEFT, padx=20)
        
        # Sleep reminder
        sleep_label = tk.Label(reminder_frame, text="😴 Aim for 8 hours of sleep", 
                              font=self.custom_font, bg=self.bg_color, fg=self.text_color)
        sleep_label.pack(side=tk.RIGHT, padx=20)
        
    def create_routine_steps(self, parent, steps):
        for i, step in enumerate(steps):
            step_frame = tk.Frame(parent, bg=self.card_bg, pady=5)
            step_frame.pack(fill=tk.X, pady=5)
            
            # Checkbox for completion
            var = tk.BooleanVar(value=step["completed"])
            checkbox = tk.Checkbutton(step_frame, variable=var, bg=self.card_bg, 
                                     command=lambda v=var, s=step: self.update_progress(v, s))
            checkbox.pack(side=tk.LEFT)
            
            # Step information
            info_frame = tk.Frame(step_frame, bg=self.card_bg)
            info_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
            
            name_label = tk.Label(info_frame, text=step["name"], font=self.button_font, 
                                 bg=self.card_bg, fg=self.text_color, anchor="w")
            name_label.pack(fill=tk.X)
            
            desc_label = tk.Label(info_frame, text=step["desc"], font=self.custom_font, 
                                 bg=self.card_bg, fg="gray", anchor="w")
            desc_label.pack(fill=tk.X)
            
            # Timing or tips button (would display a popup with more information)
            tip_button = tk.Button(step_frame, text="Tips", font=("Helvetica", 10), 
                                  bg=self.accent_color, fg=self.text_color, 
                                  padx=10, relief=tk.FLAT,
                                  command=lambda s=step: self.show_tips(s))
            tip_button.pack(side=tk.RIGHT)
            
    def update_progress(self, var, step):
        step["completed"] = var.get()
        
        # Count completed steps
        total_steps = sum(len(routine["steps"]) for routine in self.routine)
        completed_steps = sum(step["completed"] for routine in self.routine 
                            for step in routine["steps"])
        
        # Update progress bar
        progress_value = completed_steps / total_steps if total_steps > 0 else 0
        self.progress_var.set(progress_value)
        
        # Check if all steps are completed
        if completed_steps == total_steps:
            self.show_completion_message()
    
    def mark_all_completed(self):
        for routine in self.routine:
            for step in routine["steps"]:
                step["completed"] = True
                
        self.progress_var.set(1.0)  # 100% complete
        self.display_routine()  # Refresh display
        self.show_completion_message()
        
    def reset_routine(self):
        for routine in self.routine:
            for step in routine["steps"]:
                step["completed"] = False
                
        self.progress_var.set(0.0)  # 0% complete
        self.display_routine()  # Refresh display
        
    def show_tips(self, step):
        # This would show a popup with tips for the specific step
        tip_window = tk.Toplevel(self)
        tip_window.title(f"Tips for {step['name']}")
        tip_window.geometry("400x300")
        tip_window.configure(bg=self.card_bg)
        
        # Header
        tk.Label(tip_window, text=f"Tips for {step['name']}", font=self.subheader_font,
                bg=self.card_bg, fg=self.highlight_color).pack(pady=15)
        
        # Sample tips
        tips = [
            f"Apply {step['name']} in gentle upward motions",
            f"Wait 1-2 minutes before applying next product",
            f"Store {step['name']} in the refrigerator for a cooling effect",
            "Use only a pea-sized amount for best results",
            "Pat gently, don't rub your skin"
        ]
        
        for tip in tips:
            tk.Label(tip_window, text=f"• {tip}", font=self.custom_font, 
                    bg=self.card_bg, fg=self.text_color, justify=tk.LEFT, 
                    wraplength=350).pack(anchor="w", padx=20, pady=5)
        
        # Close button
        tk.Button(tip_window, text="Close", font=self.button_font, 
                 bg=self.highlight_color, fg="white", padx=15, pady=5,
                 command=tip_window.destroy).pack(pady=15)
        
    def show_completion_message(self):
        # This would show a congratulatory message when all steps are completed
        self.streak += 1
        self.streak_label.config(text=f"Current Streak: {self.streak} days")
        
        # Sample completion messages
        messages = [
            "Amazing job! Your skin thanks you for your dedication!",
            "Routine complete! You're one day closer to your skin goals!",
            "Perfect! Consistency is key to great skin!",
            "Well done! Your future self will thank you for this dedication!"
        ]
        
        # Update motivation label with completion message
        self.motivation_label.config(text=random.choice(messages))
        
    def go_home(self):
        # This would navigate back to the home screen
        # For demo purposes, we're just closing the app
        self.quit()

if __name__ == "__main__":
    app = SkinXpertRoutine()
    app.mainloop()