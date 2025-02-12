# import tkinter as tk
# from PIL import ImageTk, Image
# from tkinter import messagebox
# import pymysql

# # List of questions and answer choices
# questions = [
#     "How does your skin feel after washing?",
#     "How often does your skin get oily during the day?",
#     "Do you experience acne or breakouts?",
#     "How sensitive is your skin to new skincare products?",
#     "What are your skin concerns?"
# ]

# options_list = [
#     ["Tight and dry", "Normal, comfortable", "Greasy or shiny", "Dry in some areas, oily in others"],
#     ["Rarely, it stays dry", "Only on the T-zone (forehead, nose, chin)", "Stays balanced throughout the day", "Gets shiny quickly"],
#     ["Rarely or never", "Occasionally, during stress or periods", "Frequently, especially on forehead and nose", "Almost always, deep and painful acne"],
#     ["Very sensitive, I often get redness or irritation", "Occasionally reacts to strong products", "Rarely reacts, most products work fine", "Never had any reaction"],
#     ["Flakiness, tightness, rough patches", "Enlarged pores, excess oil", "Redness, irritation", "Dark spots, acne scars"]  # Last question (with images)
# ]

# results_list = [
#     ["Dry Skin", "Normal Skin", "Oily Skin", "Combination Skin"],
#     ["Dry Skin", "Combination Skin", "Normal Skin", "Oily Skin"],
#     ["Not acne-prone", "Mild acne-prone", "Moderate acne-prone", "Severe acne-prone"],
#     ["Sensitive Skin", "Mild Sensitivity", "Resilient Skin", "Non-sensitive Skin"],
#     ["Dryness Issue", "Oily Skin Issue", "Sensitive Skin Issue", "Hyperpigmentation Issue"]  # Last question (with images)
# ]

# class SkinQuizApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Skin Type Quiz")
        
#         self.question_index = 0
#         self.answers = []
#         self.images = []  # Store image references to prevent garbage collection
#         self.bg=ImageTk.PhotoImage(file='qbg.jpg')
#         # Quiz Frame
#         bgLabel = tk.Label(self.root, image=self.bg)
#         bgLabel.place(x=0, y=0)

#         self.question_label = tk.Label(self.root, text="", font=("Times New Roman", 30), bg='white')
#         self.question_label.place(x=400, y=100)

#         # Question Label
#         self.radio_buttons = []
#         button_positions = [(280, 250), (280, 370), (900, 250), (900, 370)]

      
#         # Radio Buttons for Side-by-Side Layout (Text Only)
#         self.radio_var = tk.StringVar()
#         self.radio_buttons = []
#         for i in range(4):  
#             rb = tk.Radiobutton(self.root, text="", variable=self.radio_var, value="", font=("times new roma", 20), bg="white")
#             rb.place(x=button_positions[i][0], y=button_positions[i][1])  
#             self.radio_buttons.append(rb)

#         # Next Button
#         self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=("times new roman", 20), bg="white")
#         self.next_button.place(x=400, y=500)  

#         self.load_question()
    
#     def load_question(self):
#         """Loads the current question and options."""
#         self.question_label["text"] = questions[self.question_index]
#         self.radio_var.set("")  
#         options = options_list[self.question_index]  

#         if self.question_index == 4:  # If last question (Skin Concerns), use images
#             self.load_question_with_images()
#         else:
#             for i in range(4):  
#                 self.radio_buttons[i]["text"] = options[i]
#                 self.radio_buttons[i]["value"] = options[i]
#                 self.radio_buttons[i]["image"] = ""  # Remove images from previous questions

#     def load_question_with_images(self):
#         """Loads options with images for the last question (Skin Concerns)."""
#         image_files = ["c1.jpg", "c2.jpg", "c3.jpg", "c4.jpg"]  # Update with actual file paths
#         options = options_list[self.question_index]
#         self.images = [ImageTk.PhotoImage(Image.open(img).resize((50, 50))) for img in image_files]  # Resize images

#         for i in range(4):
#             self.radio_buttons[i]["text"] = options[i]
#             self.radio_buttons[i]["value"] = options[i]
#             self.radio_buttons[i]["compound"] = "left"  # Image on the left of text
#             self.radio_buttons[i]["image"] = self.images[i]  # Set image
    
#     def next_question(self):
#         """Handles answer selection and moves to the next question."""
#         selected_option = self.radio_var.get()
#         if not selected_option:
#             messagebox.showwarning("Warning", "Please select an option!")
#             return
        
#         options = options_list[self.question_index]
#         results = results_list[self.question_index]

#         for i in range(4):
#             if selected_option == options[i]:
#                 self.answers.append(results[i])
#                 break

#         self.question_index += 1
#         if self.question_index < len(questions):
#             self.load_question()
#         else:
#             self.show_result()
    
#     def show_result(self):
#         """Displays final quiz results and stores in database."""
#         self.skin_type = max(set(self.answers[:2]), key=self.answers[:2].count)
#         self.acne_level = self.answers[2]
#         self.sensitivity = self.answers[3]
#         self.main_issue = self.answers[4]

#         # Database Connection
#         try:
#             connection = pymysql.connect(host='localhost', user='root', password='123456', database='skinxpert')
#             cur = connection.cursor()
#             cur.execute("UPDATE signup SET skintype=%s, alevel=%s WHERE id=1", (self.skin_type, self.acne_level))
#             connection.commit()
#             connection.close()
#         except pymysql.MySQLError as e:
#             messagebox.showerror("Database Error", f"Error updating database: {e}")
#             return

#         # Result Message
#         result_message = (
#             f"• Your Skin Type: {self.skin_type}\n"
#             f"• Acne Prone Level: {self.acne_level}\n"
#             f"• Sensitivity: {self.sensitivity}\n"
#             f"• Main Skin Concern: {self.main_issue}"
#         )

#         messagebox.showinfo("Your Skin Profile", result_message)
#         print(self.main_issue)

#         self.root.destroy()  
#         import quizresults  
#         self.root.quit()

# # Run the Tkinter app
# if __name__ == "__main__":
#     root = tk.Tk()
    
#     app = SkinQuizApp(root)
#     root.mainloop()
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

# List of questions and answer choices
questions = [
    "How does your skin feel after washing?",
    "How often does your skin get oily during the day?",
    "Do you experience acne or breakouts?",
    "How sensitive is your skin to new skincare products?",
    "What are your skin concerns?"
]

options_list = [
    ["Tight and dry", "Normal, comfortable", "Greasy or shiny", "Dry in some areas, oily in others"],
    ["Rarely, it stays dry", "Only on the T-zone (forehead, nose, chin)", "Stays balanced throughout the day", "Gets shiny quickly"],
    ["Rarely or never", "Occasionally, during stress or periods", "Frequently, especially on forehead and nose", "Almost always, deep and painful acne"],
    ["Very sensitive, I often get redness or irritation", "Occasionally reacts to strong products", "Rarely reacts, most products work fine", "Never had any reaction"],
    ["Flakiness, tightness, rough patches", "Enlarged pores, excess oil", "Redness, irritation", "Dark spots, acne scars"]
]

results_list = [
    ["Dry Skin", "Normal Skin", "Oily Skin", "Combination Skin"],
    ["Dry Skin", "Combination Skin", "Normal Skin", "Oily Skin"],
    ["Not acne-prone", "Mild acne-prone", "Moderate acne-prone", "Severe acne-prone"],
    ["Sensitive Skin", "Mild Sensitivity", "Resilient Skin", "Non-sensitive Skin"],
    ["Dryness Issue", "Oily Skin Issue", "Sensitive Skin Issue", "Hyperpigmentation Issue"]
]

class SkinQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Skin Type Quiz")
        
        self.question_index = 0
        self.answers = []
        self.images = []  # Store image references to prevent garbage collection
        self.bg=ImageTk.PhotoImage(file='qbg.jpg')
        # Quiz Frame
        bgLabel = tk.Label(self.root, image=self.bg)
        bgLabel.place(x=0, y=0)

        self.question_label = tk.Label(self.root, text="", font=("Times New Roman", 30), bg='white')
        self.question_label.place(x=400, y=100)

        # Question Label
        self.radio_buttons = []
        button_positions = [(280, 250), (280, 370), (900, 250), (900, 370)]

        # Radio Buttons for Side-by-Side Layout (Text Only)
        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):  
            rb = tk.Radiobutton(self.root, text="", variable=self.radio_var, value="", font=("times new roma", 20), bg="white")
            rb.place(x=button_positions[i][0], y=button_positions[i][1])  
            self.radio_buttons.append(rb)

        # Next Button
        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=("times new roman", 20), bg="white")
        self.next_button.place(x=400, y=500)  

        self.load_question()
    
    def load_question(self):
        """Loads the current question and options."""
        self.question_label["text"] = questions[self.question_index]
        self.radio_var.set("")  # Clear any previous selection
        options = options_list[self.question_index]  

        if self.question_index == 4:  # If last question (Skin Concerns), use images
            self.load_question_with_images()
        else:
            for i in range(4):  
                self.radio_buttons[i]["text"] = options[i]
                self.radio_buttons[i]["value"] = options[i]
                self.radio_buttons[i]["image"] = ""  # Remove images from previous questions

    def load_question_with_images(self):
        """Loads options with images for the last question (Skin Concerns)."""
        image_files = ["c1.jpg", "c2.jpg", "c3.jpg", "c4.jpg"]  # Update with actual file paths
        options = options_list[self.question_index]
        self.images = [ImageTk.PhotoImage(Image.open(img).resize((50, 50))) for img in image_files]  # Resize images

        for i in range(4):
            self.radio_buttons[i]["text"] = options[i]
            self.radio_buttons[i]["value"] = options[i]
            self.radio_buttons[i]["compound"] = "left"  # Image on the left of text
            self.radio_buttons[i]["image"] = self.images[i]  # Set image
    
    def next_question(self):
        """Handles answer selection and moves to the next question."""
        selected_option = self.radio_var.get()
        if not selected_option:
            messagebox.showwarning("Warning", "Please select an option!")
            return
        
        options = options_list[self.question_index]
        results = results_list[self.question_index]

        for i in range(4):
            if selected_option == options[i]:
                self.answers.append(results[i])
                break

        self.question_index += 1
        if self.question_index < len(questions):
            self.load_question()
        else:
            self.show_result()
    
    def show_result(self):
        """Displays final quiz results and stores in database."""
        self.skin_type = max(set(self.answers[:2]), key=self.answers[:2].count)
        self.acne_level = self.answers[2]
        self.sensitivity = self.answers[3]
        self.main_issue = self.answers[4]

        # Database Connection
        try:
            connection = pymysql.connect(host='localhost', user='root', password='123456', database='skinxpert')
            cur = connection.cursor()
            cur.execute("UPDATE signup SET skintype=%s, alevel=%s WHERE id=1", (self.skin_type, self.acne_level))
            connection.commit()
            connection.close()
        except pymysql.MySQLError as e:
            messagebox.showerror("Database Error", f"Error updating database: {e}")
            return

        # Result Message
        result_message = (
            f"• Your Skin Type: {self.skin_type}\n"
            f"• Acne Prone Level: {self.acne_level}\n"
            f"• Sensitivity: {self.sensitivity}\n"
            f"• Main Skin Concern: {self.main_issue}"
        )

        messagebox.showinfo("Your Skin Profile", result_message)

        self.root.destroy()  
        import quizresults  # Assuming you have a results screen to show the final result
        self.root.quit()

# Run the Tkinter app

root = tk.Tk()
app = SkinQuizApp(root)
root.mainloop()  # Start the Tkinter event loop
