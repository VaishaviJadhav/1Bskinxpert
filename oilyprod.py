import tkinter as tk
from PIL import Image, ImageTk

# Function to create a product card with x, y positioning
def create_product_card(parent, image_path, title, price, x, y):
    card = tk.Frame(parent, bg="white", bd=2, relief="ridge")  # Border for shadow effect
    card.place(x=x, y=y, width=170, height=300)  # Set position and size

    
    pil_img = Image.open(image_path)
    pil_img = pil_img.resize((150, 180), Image.Resampling.LANCZOS)  # Resize image
    tk_img = ImageTk.PhotoImage(pil_img)

    img_label = tk.Label(card, image=tk_img, bg="white")
    img_label.image = tk_img  # Keep reference to avoid garbage collection
    img_label.pack(pady=5)

    title_label = tk.Label(card, text=title, font=("Arial", 12, "bold"), bg="white")
    title_label.pack()

    price_label = tk.Label(card, text=f"₹{price}", font=("Arial", 10), fg="green", bg="white")
    price_label.pack()

    buy_button = tk.Button(card, text="Buy Now", bg="orange", fg="white")
    buy_button.pack(pady=5)

# Main Window
root = tk.Tk()
root.title("Product Display")
 # Set window size


bg = Image.open("skine.jpg")  
# Resize to fit window
bg = ImageTk.PhotoImage(bg)

bg_label = tk.Label(root, image=bg)
 # Stretch across window


products = [
    ("op1.jpg", "Cetaphil Gentle \nSkin Cleanser", "399"),
    ("op2.jpg","Minimalist Oat \nCleanser","284"),
    ("op3.jpg","Minimalist 2% hydrou\n +PGA Serum","284"),
    ("op4.jpg","Derma Co 10% \nNiacinamide Serum","149"),
    ("op5.jpg","Cetaphil Moisturising \nCream","1,092"),
    ("op6.jpg","Minimalist Sepicalm3% \nMoisturizer","331")
]


x_start = 200  # Start position
y_position = 100  # Fixed y position
spacing = 200  # Space between cards

for i, product in enumerate(products):
    image_path, title, price = product  # Unpack properly
    x = x_start + (i * spacing)  # Calculate x position
    create_product_card(root, image_path, title, price, x, y_position)

root.mainloop()
