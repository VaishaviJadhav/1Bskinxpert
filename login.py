from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql

login = Tk()
login.title('Login Page')

# Maximize the window size to the screen size while keeping the window decorations
login.geometry(f"{login.winfo_screenwidth()}x{login.winfo_screenheight()}")  # Fullscreen-like size
login.resizable(True, True)  # Allow resizing the window (so minimize and maximize buttons are active)

def login_action():
    u = usernameEntry.get()
    p = passwordEntry.get()
    if u == "" and p == "":
        messagebox.showerror("Error!", "All fields are Required")
    else:
        try:
            connection = pymysql.connect(host='localhost', user='root', password='Azra@23oct', database='skinxpert')
            cur = connection.cursor()
            cur.execute("Select * from signup where username=%s and password=%s", (u, p))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error!", "Invalid ID or Password")
            else:
                messagebox.showinfo("Success", "Login Successful")
                login.destroy()
                import homepage
                connection.close()
        except Exception as e:
            messagebox.showerror("Error", f"{e}")

def signup_page():
    login.destroy()
    import signup

# Load the background image
bg_image = Image.open('skine.jpg')  # Open the image file
bg_image = bg_image.resize((login.winfo_screenwidth(), login.winfo_screenheight()))  # Resize to screen size
bg = ImageTk.PhotoImage(bg_image)  # Convert the image to a Tkinter-compatible format

# Create the label with the resized image
bgLabel = Label(login, image=bg)
bgLabel.place(relwidth=1, relheight=1)  # Make the label cover the entire window

# # Username label
# username_label = Label(login, text="Username:", font=("Arial", 20), bg='white smoke', fg='black')
# username_label.place(x=550, y=250)

# # Password label
# password_label = Label(login, text="Password:", font=("Arial", 20), bg='white smoke', fg='black')
# password_label.place(x=550, y=370)

# Username Entry
usernameEntry = Entry(login, font=('Arial', 28), fg='darkolivegreen', bg='white')
usernameEntry.place(x=550, y=310, width=350)
usernameEntry.insert(0, '')

# Password Entry
passwordEntry = Entry(login, font=('Arial', 28), fg='darkolivegreen', bg='white', show="*")  # Adding 'show' to mask the password
passwordEntry.place(x=550, y=430, width=350)
passwordEntry.insert(0, '')

# Login button
login_button = Button(login, text="Login", font=('Times New Roman', 28), bd=0, bg='darkolivegreen', fg='white',
                      activebackground='darkolivegreen', activeforeground='white', width=8, command=login_action)
login_button.place(x=550, y=550)

# Signup button
signup_button = Button(login, text="SignUp", font=('times new roman', 28), bd=0, bg='darkolivegreen', fg='white',
                       activebackground='darkolivegreen', activeforeground='white', width=8, command=signup_page)
signup_button.place(x=850, y=680)

login.mainloop()
