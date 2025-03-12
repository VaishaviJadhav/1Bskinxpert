import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pillow_avif
import pymysql
import sys

class SkincareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Skincare Dashboard")
        self.root.geometry("1000x700")
        self.root.configure(bg="#ffffff")

        # Search Bar
        search_frame = tk.Frame(self.root, bg="#ffffff", height=50)
        search_frame.pack(fill=tk.X, padx=10, pady=5)

        # Search Entry
        self.search_entry = ttk.Entry(search_frame, width=40, font=("Arial", 12))
        self.search_entry.pack(pady=10, padx=10, side=tk.LEFT)
        ttk.Button(search_frame, text="Search").pack(pady=10, padx=10, side=tk.LEFT)

        # Sidebar
        sidebar = tk.Frame(self.root, width=120, bg="#d8e6d1")
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        tk.Button(sidebar, text="My Routine", font=("Helvetica", 14)).place(x=6, y=200, width=115, height=40)
        tk.Button(sidebar, text="Home Remedies", font=("Helvetica", 10)).place(x=6, y=250, width=115, height=40)

        # Content Area (Right Side)
        self.content_frame = tk.Frame(self.root, bg="#ffffff", width=800, height=600)
        self.content_frame.place(x=130, y=60)

        # ✅ Show the My Routine Page by Default
        self.show_my_routine_page()

    def show_my_routine_page(self):
        # Clear previous content
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        connection = pymysql.connect(host='localhost', user='root', password='Azra@23oct', database='skinxpert')
        cur = connection.cursor()

# Fetch Skin Type
        cur.execute("SELECT skintype FROM signup WHERE id = 1")
        fetch_result = cur.fetchone()

        if fetch_result:
           stype = fetch_result[0]
        else:
           stype = "Unknown"
        
        if stype=='Oily Skin':
        # Adding the Text for My Routine
          routine_text = """
         🌞 Morning Routine (Oily Skin)
         🧼 Cleanser – Wash your face with a salicylic acid face wash 
         (like Derma Co Salicylic Acid Cleanser) to control oil.
        💧 Moisturizer – Apply a lightweight, oil-free gel moisturizer 
         to keep skin hydrated.
         🧴 Sunscreen – Always wear an oil-free, broad-spectrum sunscreen (SPF 30+).

         🌙 Night Routine (Oily Skin)
         🧼 Cleanser – Wash your face again with the salicylic acid cleanser.
         💊 Treatment (Optional) – If you have acne, use a benzoyl peroxide 
         or retinol treatment.
         💧 Moisturizer – Apply your gel-based moisturizer to lock in hydration.

         ✨ Bonus Tip:
         - 2-3 times a week → Use a clay mask 🧖‍♀️ or BHA exfoliant to unclog pores.
         - Avoid heavy creams — they can clog pores and make skin oilier.
        """
        elif stype=="Dry Skin":
          routine_text="""🌞 Morning Routine (Dry Skin)
🧼 Cleanser – Use a hydrating, gentle cleanser (like CeraVe Hydrating Cleanser) to
 avoid stripping moisture.

 💧 Moisturizer – Apply a thick, cream-based moisturizer to keep your skin 
hydrated all day.

🧴 Sunscreen – Use a moisturizing sunscreen (SPF 30+) to protect your skin.

🌙 Night Routine (Dry Skin)
🧼 Cleanser – Wash your face with the same hydrating cleanser.

💊 Treatment (Optional) – Use a hyaluronic acid serum for extra hydration or 
retinol for anti-aging.

💧 Moisturizer – Apply a rich, nourishing night cream or a moisturizer 
with ceramides"""
        elif stype=='Combination Skin':
           routine_text="""🌞 Morning Routine (Combination Skin)
🧼 Cleanser – Use a gentle, balancing cleanser (like CeraVe Foaming Cleanser) to cleanse without drying or making skin oily.

💧 Moisturizer – Apply a lightweight, gel-based moisturizer on your face. Focus on dry areas, avoid too much on oily zones.

🧴 Sunscreen – Use an oil-free, broad-spectrum sunscreen (SPF 30+), especially on oily areas.

🌙 Night Routine (Combination Skin)
🧼 Cleanser – Wash your face again with the same cleanser.

💊 Treatment (Optional) – Apply niacinamide serum to control oil and reduce pores or hyaluronic acid for dry patches.

💧 Moisturizer – Use a light moisturizer for your oily areas and a thicker moisturizer for dry areas if needed"""
        # ✅ Text Widget to Show the Routine
        text_widget = tk.Text(self.content_frame, wrap=tk.WORD, font=("Helvetica", 20), bg="#ffffff", bd=0)
        text_widget.insert(tk.END, routine_text)
        text_widget.config(state=tk.DISABLED)  # Prevent Editing
        text_widget.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)


root = tk.Tk()
app = SkincareApp(root)
root.mainloop()
