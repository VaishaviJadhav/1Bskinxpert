import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pillow_avif
import pymysql
import sys

# Capture the product type from command line arguments
ptype = sys.argv[1] 

connection = pymysql.connect(host='localhost', user='root', password='Azra@23oct', database='skinxpert')
cur = connection.cursor()

# Fetch Skin Type
cur.execute("SELECT skintype FROM signup WHERE id = 1")
fetch_result = cur.fetchone()

if fetch_result:
    stype = fetch_result[0]
else:
    stype = "Unknown"

# Products for Oily Skin
if stype == "Dry Skin":
    products = [
        {"name": "Derma Co Cleanser", "image": "./images/Dermaoilycleanser.png", "price": 239},
        {"name": "Cetaphil Cleanser", "image": "./images/CetaOilycleanser.avif", "price": 364},
        {"name": "Minimalist Cleanser", "image": "./images/Minoilycleanser.avif", "price": 299},
        {"name": "Dot And Key Serum", "image": "./images/dryserumdotkey.jpg", "price": 695},
        {"name": "Dr Sheth Cleanser", "image": "./images/Dryshethcleanser.webp", "price": 331},
        {"name": "The Ordinary Serum", "image": "./images/dryordinaryserum.jpg", "price": 609},
        {"name": "Cera Ve Serum", "image": "./images/dryserumcera.webp", "price": 999},
        {"name": "Mario Badescu Toner", "image": "./images/drytonermario.webp", "price": 420},
        {"name": "Pixi Beauty Glow Tonic", "image": "./images/drytonerpixi.webp", "price": 1550},
        {"name": "Simple Toner", "image": "./images/drytonersimple.jpg", "price": 10}
    ]

# Products for Oily Skin
elif stype == "Oily Skin":
   if ptype=="cleanser":
    products = [
        {"name": "Cetaphil Gentle \nCleanser", "image": "op1.jpg", "price": 399, "type": "oily"},
        {"name": "Minimalist Oat \nCleanser", "image": "op2.jpg", "price": 284, "type": "oily"},
        {"name": "Minimalist Hydroulaunic\nSerum", "image": "op3.jpg", "price": 284, "type": "oily"},
        {"name": "Derma Co Niacinamide \nSerum", "image": "op4.jpg", "price": 149, "type": "oily"},
        {"name": "Cetaphil Moisturising \nCream", "image": "op5.jpg", "price": 1092, "type": "oily"},
        {"name": "Minimalist Salicylic \nAcid Cleanser", "image": "op6.jpg", "price": 284, "type": "oily"},
        {"name": "Neutrogena Oil-Free\nAcne Wash", "image": "op7.jpg", "price": 642, "type": "oily"},
        {"name": "Plum Green Tea \nAlcohol-Free Toner", "image": "op8.jpg", "price": 378, "type": "oily"},
        {"name": "Minimalist PHA \nNiacinamide Toner", "image": "op9.jpg", "price": 399, "type": "oily"},
        {"name": "Ordinary Niacinamide Zinc", "image": "op10.jpg", "price": 600, "type": "oily"},
        {"name": "Re’equil Dry Touch Sunscreen", "image": "op11.jpg", "price": 580, "type": "oily"},
        {"name": "COSRX BHA Blackhead Power Liquid", "image": "op12.jpg", "price": 1531, "type": "oily"},
        {"name": "Neutrogena Hydro Boost Gel", "image": "op13.jpg", "price": 750, "type": "oily"},
        {"name": "Bioderma Sebium Lotion", "image": "op14.jpg", "price": 1929, "type": "oily"},
        {"name": "La Roche-Posay Effaclar Purifying Foaming Gel", "image": "op15.jpg", "price": 809, "type": "oily"},
        {"name": "COSRX AHA/BHA Clarifying Treatment Toner", "image": "op16.jpg", "price": 926, "type": "oily"},
        {"name": "Innisfree Green Tea Seed Serum", "image": "op17.jpg", "price": 788, "type": "oily"}
    ]

# Products for Combination Skin
elif stype == "Combination Skin":
    products = [
        {"name": "Cetaphil Gentle Cleanser", "image": "./images/op1.jpg", "price": 399},
        {"name": "Minimalist Salicylic Acid Cleanser", "image": "./images/op6.jpg", "price": 284},
        {"name": "Bioderma Sebium Lotion", "image": "./images/op14.jpg", "price": 1929},
        {"name": "COSRX BHA Blackhead Power Liquid", "image": "./images/op12.jpg", "price": 1531},
        {"name": "La Roche-Posay Purifying Gel", "image": "./images/op15.jpg", "price": 809},
        {"name": "Ordinary Hyaluronic Acid", "image": "./images/op19.jpg", "price": 284}
    ]



class SkincareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Skincare Dashboard")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f5f5f5")

        # Search Bar
        search_frame = tk.Frame(self.root, bg="#ffffff", height=50)
        search_frame.pack(fill=tk.X, padx=10, pady=5)

        # Search Entry
        self.search_entry = ttk.Entry(search_frame, width=40, font=("Arial", 12))
        self.search_entry.pack(pady=10, padx=10, side=tk.LEFT)
        ttk.Button(search_frame, text="Search", command=self.search_product).pack(pady=10, padx=10, side=tk.LEFT)

        sidebar = tk.Frame(self.root, width=120, bg="#d8e6d1")
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        tk.Button(sidebar, text="My Routine", font=("Helvetica", 14),command=my_routine).place(x=6, y=200, width=115, height=40)
        tk.Button(sidebar, text="Home Remedies", font=("Helvetica", 10)).place(x=6, y=250, width=115, height=40)

        # Filter Dropdown Menu
        self.filter_var = tk.StringVar()
        self.filter_var.set("Filter by Price")
        filter_menu = ttk.Combobox(search_frame, textvariable=self.filter_var, state="readonly")
        filter_menu['values'] = ["<500", "<800", "<1,000", "All"]
        filter_menu.pack(pady=10, padx=10, side=tk.LEFT)
        filter_menu.bind("<<ComboboxSelected>>", self.filter_products)

        # Product Display Area
        self.canvas = tk.Canvas(self.root, bg="white")
        self.scroll_frame = tk.Frame(self.canvas, bg="white")
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")

        # Display Products
        self.display_products(products)

    def display_products(self, product_list):
        """Clears and displays products."""
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        row, col = 0, 0
        for product in product_list:
            self.create_product_card(self.scroll_frame, product["image"], product["name"], product["price"], row, col)
            col += 1
            if col > 5:
                col = 0
                row += 1

        # Scroll configuration
        self.scroll_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def create_product_card(self, parent, image_path, title, price, row, col):
        """Creates a product card with image, name, and price."""
        card = tk.Frame(parent, bg="#d8e6d1", bd=3, relief=tk.RIDGE, width=170, height=250)
        card.grid(row=row, column=col, padx=10, pady=10)
        card.pack_propagate(False)

        # Load image
        try:
            pil_img = Image.open(image_path)
            pil_img = pil_img.resize((150, 120), Image.Resampling.LANCZOS)
        except FileNotFoundError:
            pil_img = Image.new("RGB", (150, 120), (200, 200, 200))

        img = ImageTk.PhotoImage(pil_img)
        img_label = tk.Label(card, image=img, bg="#d8e6d1")
        img_label.image = img
        img_label.pack(pady=5)

        # Product Name
        name_label = tk.Label(card, text=title, font=("Arial", 10), bg="#d8e6d1", wraplength=150, justify="center")
        name_label.pack()

        # Product Price
        price_label = tk.Label(card, text=f"₹{price}", font=("Arial", 11), fg="green", bg="#d8e6d1")
        price_label.pack()

        # Add to Cart Button
        ttk.Button(card, text="Add to Cart").pack(pady=5)

    def filter_products(self, event):
        """Filters products based on the selected price range."""
        selected_filter = self.filter_var.get()
        filtered_products = []

        if selected_filter == "<500":
            filtered_products = [p for p in products if p["price"] < 500]
        elif selected_filter == "<800":
            filtered_products = [p for p in products if p["price"] < 800]
        elif selected_filter == "<1,000":
            filtered_products = [p for p in products if p["price"] < 1000]
        else:
            filtered_products = products

        self.display_products(filtered_products)

    def search_product(self):
        """Searches for a product by name."""
        query = self.search_entry.get().lower()
        searched_products = [p for p in products if query in p["name"].lower()]
        self.display_products(searched_products)
    
def my_routine():
    import myroutine
    

# Run Application
root = tk.Tk()
app = SkincareApp(root)
root.mainloop()
