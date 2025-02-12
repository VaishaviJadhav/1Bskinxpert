# import tkinter as tk
# from PIL import Image, ImageTk

# # Create the homepage window
# hp = tk.Tk()
# hp.title("Home Page")

# # Maximize the window size to the screen size while keeping the window decorations
# hp.geometry(f"{hp.winfo_screenwidth()}x{hp.winfo_screenheight()}")  # Fullscreen-like size
# hp.resizable(True, True)  # Allow resizing the window (so minimize and maximize buttons are active)

# def start_quiz():
#     import quiz1  # Import quiz1 module before destroying the window
#     hp.destroy()  # Destroy the homepage window to open the quiz

# # Load and resize the background image to fit the screen
# bg_image = Image.open("hp.jpg")  # Ensure this file exists
# bg_image = bg_image.resize((hp.winfo_screenwidth(), hp.winfo_screenheight()))  # Resize to screen size
# bg = ImageTk.PhotoImage(bg_image)  # Convert the image to a Tkinter-compatible format

# # Create the label with the resized image
# bgLabel = tk.Label(hp, image=bg)
# bgLabel.place(relwidth=1, relheight=1)  # Make the label cover the entire window

# # Button to start the quiz
# start_button = tk.Button(hp, text="Take the Quiz", font=("Times New Roman", 32), bg="darkseagreen4", fg="white",command=start_quiz)
# start_button.place(x=1000, y=630)  # Adjust button position as needed

# # Run the homepage window
# hp.mainloop()

import tkinter as tk
from PIL import ImageTk, Image

# Create the homepage window
hp = tk.Tk()
hp.title("Home Page")

# Maximize the window size to the screen size while keeping the window decorations
hp.geometry(f"{hp.winfo_screenwidth()}x{hp.winfo_screenheight()}")  # Fullscreen-like size
hp.resizable(True, True)  # Allow resizing the window (so minimize and maximize buttons are active)

def start_quiz():
    hp.destroy()  # Destroy the homepage window to open the quiz
    import quiz1  # Import and run quiz1.py (this will launch the quiz)

def dash():
    hp.destroy()  # Destroy the homepage window to open the quiz
    import dashboard  # Import and run dashboard.py (this will launch the dash)

# Load and resize the background image to fit the screen
bg_image = Image.open("hp.jpg")  # Ensure this file exists
bg_image = bg_image.resize((hp.winfo_screenwidth(), hp.winfo_screenheight()))  # Resize to screen size
bg = ImageTk.PhotoImage(bg_image)  # Convert the image to a Tkinter-compatible format

# Create the label with the resized image
bgLabel = tk.Label(hp, image=bg)
bgLabel.place(relwidth=1, relheight=1)  # Make the label cover the entire window

# Button to start the quiz
start_button = tk.Button(hp, text="Take the Quiz", font=("Times New Roman", 26), bg="darkseagreen4", fg="white", command=start_quiz)
start_button.place(x=970, y=650)  # Adjust button position as needed

# Button to view pro
view_products = tk.Button(hp, text="View Products", font=("Times New Roman", 26), bg="darkseagreen4", fg="white", command=dash)
view_products.place(x=1220, y=650)  # Adjust button position as needed

# Run the homepage window
hp.mainloop()



