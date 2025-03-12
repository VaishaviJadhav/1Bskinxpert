import tkinter as tk
from tkinter import ttk
import subprocess
class SkincareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Skincare Dashboard")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f5f5f5")

        # Top Search Bar
        search_frame = tk.Frame(self.root, bg="#ffffff", height=50)
        search_frame.pack(fill=tk.X, padx=10, pady=5)
        search_entry = ttk.Entry(search_frame, width=40, font=("Arial", 12))
        search_entry.pack(pady=10, padx=10, side=tk.LEFT)
        ttk.Button(search_frame, text="Search").pack(pady=10, padx=10, side=tk.LEFT)

        # Sidebar
        sidebar = tk.Frame(self.root, width=200, bg="#d8e6d1")
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        ttk.Button(sidebar, text="My Routine").pack(pady=5, padx=10, fill=tk.X)
        ttk.Button(sidebar, text="Home Remedies").pack(pady=5, padx=10, fill=tk.X)

        # Green Buttons for Product Categories
        self.cleanser_button = tk.Button(self.root, text="Cleanser", 
                                         bg="#d8e6d1", fg="white", 
                                         font=("Arial", 12, "bold"),
                                         activebackground="#c1d6b8",
                                         command=self.on_cleanser_click)
        self.cleanser_button.place(x=250, y=150, width=150, height=50)

        self.moisturizer_button = tk.Button(self.root, text="Moisturizer", 
                                            bg="#d8e6d1", fg="white", 
                                            font=("Arial", 12, "bold"),
                                            activebackground="#c1d6b8",
                                            command=self.on_moisturizer_click)
        self.moisturizer_button.place(x=450, y=150, width=150, height=50)

        self.sunscreen_button = tk.Button(self.root, text="Sunscreen", 
                                          bg="#d8e6d1", fg="white", 
                                          font=("Arial", 12, "bold"),
                                          activebackground="#c1d6b8",
                                          command=self.on_sunscreen_click)
        self.sunscreen_button.place(x=250, y=250, width=150, height=50)

        self.serum_button = tk.Button(self.root, text="Serum", 
                                      bg="#d8e6d1", fg="white", 
                                      font=("Arial", 12, "bold"),
                                      activebackground="#c1d6b8",
                                      command=self.on_serum_click)
        self.serum_button.place(x=450, y=250, width=150, height=50)

    def on_cleanser_click(self):
        self.ptype = "cleanser"
        subprocess.run(["python","dashboard.py",self.ptype])

    def on_moisturizer_click(self):
        self.ptype = "moisturizer"
        print(f"Clicked on {self.ptype} button")
        self.update_ui()

    def on_sunscreen_click(self):
        self.ptype = "sunscreen"
        print(f"Clicked on {self.ptype} button")
        self.update_ui()

    def on_serum_click(self):
        self.ptype = "serum"
        print(f"Clicked on {self.ptype} button")
        self.update_ui()

    def update_ui(self):
        print(f"Selected product type: {self.ptype}")
        # You can later add a new page or display the product list here.

root = tk.Tk()
app = SkincareApp(root)
root.mainloop()
