import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


# Create Tkinter window
result_window = tk.Tk()
result_window.title('Result Page')

result_window.geometry(f"{result_window.winfo_screenwidth()}x{result_window.winfo_screenheight()}")  # Fullscreen-like size
result_window.resizable(True, True) 

bg=ImageTk.PhotoImage(file='qbg.jpg')
bgLabel=tk.Label(result_window,image=bg)
bgLabel.grid(row=0,column=0)
# Database connection
connection = pymysql.connect(host='localhost', user='root', password='123456', database='skinxpert')
cur = connection.cursor()

# Fetch Skin Type
cur.execute("SELECT skintype FROM signup WHERE id = 1")
fetch_result = cur.fetchone()  # Fetch one row

if fetch_result:  
    stype = fetch_result[0]  # Extract skin type
else:
    stype = "Unknown"  # Default if no result is found

cur1=connection.cursor()
cur1.execute("SELECT alevel FROM signup WHERE id = 1")
fetch_result1 = cur1.fetchone()
connection.close()
if fetch_result1:
    alevel=fetch_result1[0]
else:
    print("error error ")
# Create label inside the Tkinter window
skintypelabel = tk.Label(result_window, text=f"Your Skin Type is {stype}", font=("Times New Roman", 32),bg='darkseagreen4', fg='wheat2')
skintypelabel.place(x=400, y=100)
alevellabel = tk.Label(result_window, text=f"Your acne level is: {alevel}", font=("Times New Roman", 20),bg='darkseagreen4', fg='wheat2')
alevellabel.place(x=430,y=150)

if stype=='Dry Skin':
    a=tk.Label(result_window,text="You need ingredients that hydrate and strengthen the skin barrier while also addressing breakouts without causing irritation.",bg='darkseagreen4',font=("Times New Roman",18),fg='wheat2')
    a.place(x=30,y=250)
    label=tk.Label(result_window,text="•Hydrating & Barrier-Strengthening Ingredients:",font=("Times New Roman",17),bg='darkseagreen4',fg='wheat2')
    label.place(x=45,y=300)
    b=tk.Label(result_window,text="Hyaluronic Acid – Deeply hydrates the skin, preventing flakiness.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    b.place(x=60,y=330)
    b1=tk.Label(result_window,text="Glycerin – A humectant that attracts moisture and keeps skin supple.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    b1.place(x=60,y=360)
    b2=tk.Label(result_window,text="Niacinamide (2-5%) – Reduces redness, strengthens the skin barrier, and controls oil production.",bg='darkseagreen4',font=("Times New Roman",15),fg='wheat2')
    b2.place(x=60,y=390)
    b3=tk.Label(result_window,text="Ceramides – Restore the skin barrier and prevent moisture loss.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    b3.place(x=60,y=420)
    c1=tk.Label(result_window,text="•Gentle Acne-Fighting Ingredients:",font=("Times New Roman",17),bg='darkseagreen4',fg='wheat2')
    c1.place(x=45,y=470)
    c=tk.Label(result_window,text="Lactic Acid – A mild exfoliant that removes dead skin while keeping skin hydrated.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    c.place(x=60,y=500)
    c2=tk.Label(result_window,text="Azelaic Acid (10%) – Reduces inflammation and fades acne marks.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    c2.place(x=60,y=530)
    c3=tk.Label(result_window,text="Mandelic Acid – A gentle AHA that fights acne and evens skin tone.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    c3.place(x=60,y=560)
    c4=tk.Label(result_window,text="Zinc PCA – Helps control mild acne without drying out the skin.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    c4.place(x=60,y=590)
    def oproducts():
     result_window.destroy()
     import dashboard
    login_button=tk.Button(result_window,text="View products",font=('Times new roman',20),bd=0,bg='darkseagreen4',fg='white',activebackground='darkolivegreen',activeforeground='white',width=20,command=oproducts)
    login_button.place(x=900,y=590)
elif stype=='Oily Skin':
    a=tk.Label(result_window,text="you need ingredients that control excess oil, unclog pores, and prevent breakouts while maintaining hydration.",bg='darkseagreen4',font=("Times New Roman",18),fg='wheat2')
    a.place(x=30,y=250)
    label=tk.Label(result_window,text="•Oil-Control & Hydration Ingredients:",font=("Times New Roman",17),bg='darkseagreen4',fg='wheat2')
    label.place(x=45,y=300)
    b=tk.Label(result_window,text="Niacinamide (5-10%) – Reduces oil production, minimizes pores, and soothes inflammation.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    b.place(x=60,y=330)
    b1=tk.Label(result_window,text="Zinc PCA – Regulates sebum production and helps fight acne-causing bacteria.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    b1.place(x=60,y=360)
    b2=tk.Label(result_window,text="Green Tea Extract – Antioxidant-rich, reduces inflammation and controls oil.",bg='darkseagreen4',font=("Times New Roman",15),fg='wheat2')
    b2.place(x=60,y=390)
    b3=tk.Label(result_window,text="Aloe Vera – Lightweight hydrator that soothes acne-prone skin.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    b3.place(x=60,y=420)
    c1=tk.Label(result_window,text="•Acne-Fighting & Exfoliating Ingredients:",font=("Times New Roman",17),bg='darkseagreen4',fg='wheat2')
    c1.place(x=45,y=470)
    c=tk.Label(result_window,text="Salicylic Acid (BHA, 1-2%) – Unclogs pores, reduces blackheads, and controls oil.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    c.place(x=60,y=500)
    c2=tk.Label(result_window,text="Azelaic Acid (10%) – Treats mild acne, reduces redness, and evens out skin tone.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    c2.place(x=60,y=530)
    c3=tk.Label(result_window,text=" Tea Tree Oil – Natural antibacterial that helps fight acne.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    c3.place(x=60,y=560)
    c4=tk.Label(result_window,text="Lactic Acid or Mandelic Acid (Gentle AHAs) – Exfoliate without over-drying.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    c4.place(x=60,y=590) 
    def oproducts():
     result_window.destroy()
     import dashboard
    login_button=tk.Button(result_window,text="View products",font=('Times new roman',20),bd=0,bg='darkseagreen4',fg='white',activebackground='pink2',activeforeground='white',width=8,command=oproducts)
    login_button.place(x=900,y=590)
elif stype=='Combination Skin':
    a=tk.Label(result_window,text="you need ingredients that balance oil production in the T-zone while keeping dry areas hydrated—without clogging pores or causing breakouts.",bg='darkseagreen4',font=("Times New Roman",18),fg='wheat2')
    a.place(x=30,y=250)
    label=tk.Label(result_window,text="•Balancing & Hydrating Ingredients:",font=("Times New Roman",17),bg='darkseagreen4',fg='wheat2')
    label.place(x=45,y=300)
    b=tk.Label(result_window,text="Niacinamide (5%) – Controls oil in the T-zone while hydrating dry areas.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    b.place(x=60,y=330)
    b1=tk.Label(result_window,text="Hyaluronic Acid – Provides lightweight hydration without making skin greasy.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    b1.place(x=60,y=360)
    b2=tk.Label(result_window,text="Glycerin – A great humectant that hydrates without clogging pores.",bg='darkseagreen4',font=("Times New Roman",15),fg='wheat2')
    b2.place(x=60,y=390)
    b3=tk.Label(result_window,text="Panthenol (Vitamin B5) – Soothes and repairs the skin barrier.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    b3.place(x=60,y=420)
    c1=tk.Label(result_window,text="•Acne-Fighting & Exfoliating Ingredients:",font=("Times New Roman",17),bg='darkseagreen4',fg='wheat2')
    c1.place(x=45,y=470)
    c=tk.Label(result_window,text="Salicylic Acid (BHA, 1-2%) – Unclogs pores, reduces blackheads, and controls oil.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    c.place(x=60,y=500)
    c2=tk.Label(result_window,text="Azelaic Acid (10%) – Treats mild acne, reduces redness, and evens out skin tone.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    c2.place(x=60,y=530)
    c3=tk.Label(result_window,text=" Green Tea Extract – Calms redness and reduces excess oil production.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    c3.place(x=60,y=560)
    c4=tk.Label(result_window,text="Lactic Acid or Mandelic Acid (Gentle AHAs) – Exfoliate without over-drying.",font=("Times New Roman",15),bg='darkseagreen4',fg='wheat2')
    c4.place(x=60,y=590) 
    def oproducts():
     result_window.destroy()
     import dashboard
    login_button=tk.Button(result_window,text="View products",font=('Times new roman',28),bd=0,bg='darkseagreen4',fg='white',activebackground='pink2',activeforeground='white',width=8,command=oproducts)
    login_button.place(x=900,y=590)
result_window.mainloop()
