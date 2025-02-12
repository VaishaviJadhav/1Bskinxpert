import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
# import pillow_avif  # Ensure this is installed if using AVIF images
import pymysql

connection = pymysql.connect(host='localhost', user='root', password='123456', database='skinxpert')
cur = connection.cursor()

# Fetch Skin Type
cur.execute("SELECT skintype FROM signup WHERE id = 1")
fetch_result = cur.fetchone()  # Fetch one row

if fetch_result:  
    stype = fetch_result[0]  # Extract skin type
else:
    stype = "Unknown"  # Default if no result is found
if stype=="Dry Skin":
# Updated product data with names, images, and prices
 products = [
    {"name": "Derma Co Cleanser", "image": "d1.jpeg", "price": "₹239", "type": "dry" },
    {"name": "Cetaphil Cleanser", "image": "d2.jpeg", "price": "₹364","type": "dry"},
    {"name": "Minimalist Cleanser", "image": "d3.jpg", "price": "₹299","type": "dry"},
    {"name": "Dot And Key Serum", "image": "d4.jpeg", "price": "₹695","type": "dry"},
    {"name": "Dr Sheth Cleanser", "image": "d5.jpeg", "price": "₹331","type": "dry"},
    {"name": "The Ordinary Serum", "image": "d6.jpeg", "price": "₹609","type": "dry"},
    {"name": "Cera Ve Serum", "image": "d7.jpeg", "price": "₹999","type": "dry"},
    {"name": "Mario Badescu Toner", "image": "d8.jpeg", "price": "₹420","type": "dry"},
    {"name": "Pixi Beauty Glow Tonic", "image": "d9.jpeg", "price": "₹1,550","type": "dry"},
    {"name": "Simple Toner", "image": "d10.jpeg", "price": "₹200","type": "dry"},
    {"name": "Cera Ve Moisturizer", "image": "d11.jpeg", "price": "₹322","type": "dry"},
    {"name": "Dot and Key Moisturizer", "image": "d12.jpeg", "price": "₹599","type": "dry"},
    {"name": "Aqualogica Moisturizer", "image": "d13.jpeg", "price": "₹299","type": "dry"},
    {"name": "Derma Co Moisturizer", "image": "d14.jpeg", "price": "₹279","type": "dry"},
    {"name": "Dot and Key Sunscreen", "image": "d15.jpeg", "price": "₹595","type": "dry"},
    {"name": "Neutrogena Sunscreen", "image": "d16.jpeg", "price": "₹248","type": "dry"},
    {"name": "Minimalist Sunscreen", "image": "d17.jpg", "price": "₹249","type": "dry"}
    ]
elif stype=="Oily Skin":
    products = [
    {"name": "Cetaphil Gentle \nCleanser", "image": "op1.jpg", "price": "₹399", "type": "oily" },
    {"name":"Minimalist Oat \ncleanser","image":"op2.jpg","price":"₹284","type":"oily"},
    {"name":"Minimalist Hydroulaunic\nSerum ","image":"op3.jpg","price":"₹284","type":"oily"},
    {"name":"Derma Co Niacinamide \nSerum","image":"op4.jpg","price":"₹149","type":"oily"},
    {"name":"Cetaphil Moisturising \nCream","image":"op5.jpg","price":"₹1,092","type":"oily"},
    {"name":"Minimalist Salicylic \nAcid Cleanser","image":"op6.jpg","price":"₹284","type":"oily"},
    {"name":"Neutrogena Oil-Free\nAcne Wash","image":"op7.jpg","price":"₹642","type":"oily"},
    {"name":"Plum Green Tea \nAlcohol-Free Toner ","image":"op8.jpg","price":"₹378","type":"oily"},
    {"name":"Minimalist PHA \nNiacinamide Toner","image":"op9.jpg","price":"₹399","type":"oily"},
    {"name":"Ordinary Niacinamide Zinc","image":"op10.jpg","price":"₹600","type":"oily"},
    {"name":"Re’equil Dry Touch Sunscreen","image":"op11.jpg","price":"₹580","type":"oily"},
    {"name":"COSRX BHA Blackhead Power Liquid ","image":"op12.jpg","price":"₹1,531","type":"oily"},
    {"name":"Neutrogena Hydro Boost Gel","image":"op13.jpg","price":"₹750","type":"oily"},
    {"name":"Bioderma Sebium Lotion","image":"op14.jpg","price":"₹1,929","type":"oily"},
    {"name":"La Roche-Posay Effaclar Purifying Foaming Gel","image":"op15.jpg","price":"₹809","type":"oily"},
    {"name":"COSRX AHA/BHA Clarifying Treatment Toner","image":"op16.jpg","price":"₹926","type":"oily"},
    {"name":"Innisfree Green Tea Seed Serum","image":"op17.jpg","price":"₹788","type":"oily"},

 ]
elif stype=="Combination Skin":
    products = [
    {"name": "Cetaphil Gentle \nCleanser", "image": "op1.jpg", "price": "₹399", "type": "oily" },
    {"name":"Minimalist Salicylic \nAcid Cleanser","image":"op6.jpg","price":"₹284","type":"oily"},
    {"name":"Bioderma Sebium Lotion","image":"op14.jpg","price":"₹1,929","type":"oily"},
    {"name":"COSRX BHA Blackhead Power Liquid ","image":"op12.jpg","price":"₹1,531","type":"oily"},
    {"name":"La Roche-Posay Effaclar Purifying Foaming Gel","image":"op15.jpg","price":"₹809","type":"oily"},
    {"name":" Minimalist Niacinamide Serum","image":"op18.jpg","price":"₹1,092","type":"oily"},
    {"name":"COSRX BHA Blackhead Power Liquid ","image":"op12.jpg","price":"₹1,531","type":"oily"},
    {"name":"The Ordinary Hyaluronic Acid","image":"op19.jpg","price":"₹284","type":"oily"},
    {"name":"Neutrogena Oil-Free\nAcne Wash","image":"op7.jpg","price":"₹642","type":"oily"},
    {"name":"Minimalist PHA \nNiacinamide Toner","image":"op9.jpg","price":"₹399","type":"oily"},
    {"name":"Ordinary Niacinamide Zinc","image":"op10.jpg","price":"₹600","type":"oily"},
    {"name":"Re’equil Dry Touch Sunscreen","image":"op11.jpg","price":"₹580","type":"oily"},
    {"name":"Neutrogena Hydro Boost Gel","image":"op13.jpg","price":"₹750","type":"oily"},
    {"name":"COSRX AHA/BHA Clarifying Treatment Toner","image":"op16.jpg","price":"₹926","type":"oily"},
    {"name":"Innisfree Green Tea Seed Serum","image":"op17.jpg","price":"₹788","type":"oily"},
    {"name":"Plum Green Tea \nAlcohol-Free Toner ","image":"op8.jpg","price":"₹378","type":"oily"},


 ]
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

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

        # Scrollable Product Display Area
        canvas = tk.Canvas(self.root, bg="white")
        scroll_frame = tk.Frame(canvas, bg="white")
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

        # Products Data
       

        # Grid layout for products
        row, col = 0, 0
        for product in products:
            self.create_product_card(scroll_frame, product["image"], product["name"], product["price"], row, col)
            col += 1
            if col > 6:  # 5 products per row
                col = 0
                row += 1

        # Update scroll region
        scroll_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def create_product_card(self, parent, image_path, title, price, row, col):
        """ Creates a product card with a fixed size. """
        card = tk.Frame(parent, bg="#d8e6d1", bd=3, relief=tk.RIDGE, width=170, height=250)  # Fixed size
        card.grid(row=row, column=col, padx=10, pady=10)
        card.pack_propagate(False)  # Prevent resizing to fit content

        try:
            pil_img = Image.open(image_path)
            pil_img = pil_img.resize((150, 120), Image.Resampling.LANCZOS)  # Resize image
        except FileNotFoundError:
            pil_img = Image.new("RGB", (150, 120), (200, 200, 200))  # Placeholder image

        img = ImageTk.PhotoImage(pil_img)
        img_label = tk.Label(card, image=img, bg="#d8e6d1")
        img_label.image = img  # Keep reference
        img_label.pack(pady=5)

        name_label = tk.Label(card, text=title, font=("Arial", 10), bg="#d8e6d1", wraplength=150, justify="center")
        name_label.pack()

        price_label = tk.Label(card, text=f"{price}", font=("Arial", 11), fg="green", bg="#d8e6d1")
        price_label.pack()

        ttk.Button(card, text="Add to Cart").pack(pady=5)

# Run the application
root = tk.Tk()
app = SkincareApp(root)
root.mainloop()


