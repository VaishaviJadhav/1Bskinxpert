from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql

signup = Tk()
signup.title('Sign Up Page')

# Maximize the window size to the screen size while keeping the window decorations
signup.geometry(f"{signup.winfo_screenwidth()}x{signup.winfo_screenheight()}")  # Fullscreen-like size
signup.resizable(True, True)  # Allow resizing the window (so minimize and maximize buttons are active)

# Function to handle signup action
def signup_action():
    u = usernameEntry.get()
    p = passwordEntry.get()

    if u == "" or p == "":
        messagebox.showerror("Error!", "All fields are required")
    else:
        try:
            # Establishing MySQL connection
            connection = pymysql.connect(host='localhost', user='root', password='Azra@23oct', database='skinxpert')
            cur = connection.cursor()
            
            # Check if the username already exists
            cur.execute("SELECT * FROM signup WHERE username=%s", (u,))
            row = cur.fetchone()
            if row:
                messagebox.showerror("Error!", "Username already exists")
            else:
                # Insert the new user into the database
                cur.execute("INSERT INTO signup (username, password) VALUES (%s, %s)", (u, p))
                connection.commit()
                messagebox.showinfo("Success", "User signed up successfully")
                signup.destroy()
                import login  # Go back to login page
            connection.close()
        except Exception as e:
            messagebox.showerror("Error", f"{e}")

# Function to go to the login page
def login_page():
    signup.destroy()
    import login

# Load the background image
bg_image = Image.open('signupbg.jpg')  # Open the image file
bg_image = bg_image.resize((signup.winfo_screenwidth(), signup.winfo_screenheight()))  # Resize to screen size
bg = ImageTk.PhotoImage(bg_image)  # Convert the image to a Tkinter-compatible format

# Create the label with the resized image
bgLabel = Label(signup, image=bg)
bgLabel.place(relwidth=1, relheight=1)  # Make the label cover the entire window

# Username Entry
usernameEntry = Entry(signup, font=('Arial', 28), fg='darkolivegreen', bg='white')
usernameEntry.place(x=550, y=310, width=350)
usernameEntry.insert(0, '')  # Set initial text (optional)

# Password Entry
passwordEntry = Entry(signup, font=('Arial', 28), fg='darkolivegreen', bg='white', show="*")  # Mask the password
passwordEntry.place(x=550, y=430, width=350)
passwordEntry.insert(0, '')  # Set initial text (optional)

# Signup Button
signup_button = Button(signup, text="Sign Up", font=('Times New Roman', 28), bd=0, bg='darkolivegreen', fg='white',
                       activebackground='darkolivegreen', activeforeground='white', width=8, command=signup_action)
signup_button.place(x=550, y=550)

# Already have an account? Button (Go to login page)
login_button = Button(signup, text="Login", font=('Times New Roman', 28), bd=0, bg='darkolivegreen', fg='white',
                      activebackground='darkolivegreen', activeforeground='white', width=8, command=login_page)
login_button.place(x=850, y=680)

signup.mainloop()
