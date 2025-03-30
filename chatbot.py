import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
import os
from PIL import Image, ImageTk
import re

class SkincareChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Skincare Assistant")
        self.root.geometry("1200x700")  # Full HP Victus screen size
        
        # Sage green color scheme
        self.colors = {
            'bg': '#DAEBD5',  # Light sage green
            'button': '#739E82',  # Medium sage green
            'highlight': '#4F6F5A',  # Dark sage green
            'text': '#2D3F33',  # Very dark sage green
            'white': '#FFFFFF'  # White
        }
        
        self.root.configure(bg=self.colors['bg'])
        
        # Create the skincare Q&A database
        self.qa_database = {
            "what products should i use for acne?": 
                "For acne, look for products with salicylic acid, benzoyl peroxide, or retinoids. A gentle cleanser, non-comedogenic moisturizer, and SPF are essential. Consider a spot treatment for breakouts.",
            
            "how can i reduce redness on my face?": 
                "To reduce facial redness, try products with niacinamide, azelaic acid, or centella asiatica. Avoid hot water, harsh exfoliants, and triggers like alcohol or spicy foods. Always use SPF and consider a green-tinted primer.",
            
            "what's the best way to deal with dry skin?": 
                "For dry skin, use a gentle, hydrating cleanser and apply moisturizer on damp skin. Look for ingredients like hyaluronic acid, glycerin, ceramides, and squalane. Consider using a humidifier and avoid hot showers.",
            
            "how can i get rid of dark spots?": 
                "To fade dark spots, use ingredients like vitamin C, niacinamide, alpha arbutin, or tranexamic acid. Exfoliate regularly with AHAs, wear SPF daily, and be patient as results take time.",
            
            "what's a good skincare routine for beginners?": 
                "A basic skincare routine includes: 1) Gentle cleanser 2) Moisturizer 3) Sunscreen (morning). Add a treatment product based on your skin concerns once you're consistent with the basics.",
            
            "how often should i exfoliate?": 
                "Exfoliation frequency depends on your skin type and the product used. Generally, 1-3 times weekly for chemical exfoliants, 1-2 times weekly for physical scrubs. If your skin becomes irritated, reduce frequency.",
            
            "do i really need to wear sunscreen every day?": 
                "Yes, daily sunscreen is essential even on cloudy days and indoors. UV rays cause premature aging and increase skin cancer risk. Use at least SPF 30 as the final step of your morning routine.",
            
            "what causes cystic acne and how can i treat it?": 
                "Cystic acne is caused by hormones, genetics, and bacteria. Treatment options include retinoids, antibiotics, or hormonal treatments prescribed by a dermatologist. Don't squeeze cysts as this can worsen scarring.",
            
            "how can i minimize pores?": 
                "Pores can't permanently shrink, but their appearance can be minimized with regular cleansing, chemical exfoliants (BHAs), niacinamide, retinoids, and clay masks. Keep skin hydrated and always wear sunscreen.",
            
            "what ingredients should i avoid if i have sensitive skin?": 
                "Sensitive skin should avoid fragrance, alcohol, essential oils, harsh sulfates, chemical sunscreens, and high concentrations of active ingredients like retinol or glycolic acid. Patch test new products.",
            
            "how do i know my skin type?": 
                "Cleanse face, wait 30 minutes without applying products. If skin feels tight, you likely have dry skin. If shiny all over, likely oily. If only T-zone is oily, you have combination skin. Redness/itching suggests sensitive skin.",
            
            "what's the right order to apply skincare products?": 
                "General rule: thinnest to thickest texture. Morning: cleanser → toner → serum → eye cream → moisturizer → sunscreen. Evening: cleanser → toner → treatments/serums → eye cream → moisturizer/night cream.",
            
            "can diet affect my skin?": 
                "Yes, diet can impact skin. High glycemic foods and dairy may trigger acne in some people. Foods rich in antioxidants, omega-3s, and vitamins A, C, and E can support skin health. Stay hydrated for optimal skin function.",
            
            "how can i prevent wrinkles?": 
                "Prevent wrinkles by using daily sunscreen, incorporating retinoids, using antioxidants like vitamin C, staying hydrated, not smoking, getting adequate sleep, and maintaining a healthy diet rich in antioxidants.",
            
            "what's the best treatment for under-eye dark circles?": 
                "For under-eye circles, try products with caffeine, vitamin K, retinol, or vitamin C. Use a hydrating eye cream, get adequate sleep, stay hydrated, and wear sunglasses. Concealer can help camouflage as you treat.",
            
            "how should i treat skin during pregnancy?": 
                "During pregnancy, avoid retinoids, high-dose salicylic acid, hydroquinone, and certain essential oils. Safe ingredients include glycolic acid (in low percentages), vitamin C, hyaluronic acid, and niacinamide.",
            
            "what can help with oily skin?": 
                "For oily skin, use a gentle foaming cleanser, oil-free moisturizer, and ingredients like niacinamide, salicylic acid, and clay masks. Don't skip moisturizer as dehydration can increase oil production.",
            
            "how can i deal with hormonal acne?": 
                "Hormonal acne responds well to ingredients like salicylic acid and benzoyl peroxide. Consider supplements like zinc or spearmint tea. A dermatologist might prescribe spironolactone or hormonal birth control.",
            
            "what should my skincare routine include in winter?": 
                "Winter skincare should include a gentle cleanser, heavier moisturizer, hydrating serum (with hyaluronic acid), facial oil, and lip balm. Exfoliate less frequently, use a humidifier, and continue using sunscreen.",
            
            "is it normal for skincare products to sting?": 
                "Mild tingling can be normal with active ingredients like AHAs or vitamin C, but persistent stinging, burning, or redness indicates irritation. Discontinue use of products causing discomfort and simplify your routine."
        }
        
        # Create main frames
        self.create_frames()
        
        # Create header
        self.create_header()
        
        # Create chat area
        self.create_chat_area()
        
        # Create input area
        self.create_input_area()
        
        # Create image upload area
        self.create_image_upload_area()
        
        # Initialize chat with welcome message
        self.update_chat("Skincare Assistant", "Hello! I'm your skincare assistant. How can I help you today? You can ask me questions about skincare or upload an image for analysis.")
    
    def create_frames(self):
        # Left frame for chat
        self.left_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.left_frame.place(relx=0, rely=0, relwidth=0.7, relheight=1)
        
        # Right frame for image upload
        self.right_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.right_frame.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)
    
    def create_header(self):
        header_frame = tk.Frame(self.left_frame, bg=self.colors['highlight'])
        header_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        
        header_label = tk.Label(
            header_frame, 
            text="Skincare Assistant", 
            bg=self.colors['highlight'],
            fg=self.colors['white'],
            font=("Helvetica", 24, "bold")
        )
        header_label.pack(pady=15)
    
    def create_chat_area(self):
        chat_frame = tk.Frame(self.left_frame, bg=self.colors['bg'])
        chat_frame.place(relx=0.05, rely=0.12, relwidth=0.9, relheight=0.68)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            bg=self.colors['white'],
            fg=self.colors['text'],
            font=("Helvetica", 12),
            wrap=tk.WORD,
            state='disabled'
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
    
    def create_input_area(self):
        input_frame = tk.Frame(self.left_frame, bg=self.colors['bg'])
        input_frame.place(relx=0.05, rely=0.82, relwidth=0.9, relheight=0.15)
        
        self.user_input = tk.Text(
            input_frame,
            bg=self.colors['white'],
            fg=self.colors['text'],
            font=("Helvetica", 12),
            height=3,
            wrap=tk.WORD
        )
        self.user_input.pack(fill=tk.BOTH, expand=True, pady=5)
        
        button_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, pady=5)
        
        send_button = tk.Button(
            button_frame,
            text="Send",
            bg=self.colors['button'],
            fg=self.colors['white'],
            font=("Helvetica", 12, "bold"),
            relief=tk.FLAT,
            command=self.process_user_input
        )
        send_button.pack(side=tk.RIGHT, padx=10)
        
        clear_button = tk.Button(
            button_frame,
            text="Clear",
            bg=self.colors['button'],
            fg=self.colors['white'],
            font=("Helvetica", 12),
            relief=tk.FLAT,
            command=self.clear_input
        )
        clear_button.pack(side=tk.RIGHT, padx=10)
        
        # Bind Enter key to send message
        self.user_input.bind("<Return>", lambda event: self.process_user_input())
    
    def create_image_upload_area(self):
        # Title for the image section
        image_title = tk.Label(
            self.right_frame,
            text="Skin Analysis",
            bg=self.colors['highlight'],
            fg=self.colors['white'],
            font=("Helvetica", 18, "bold"),
            pady=10
        )
        image_title.pack(fill=tk.X)
        
        # Frame for the image
        self.image_frame = tk.Frame(self.right_frame, bg=self.colors['bg'])
        self.image_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.image_label = tk.Label(
            self.image_frame,
            text="Upload an image of your skin concern",
            bg=self.colors['bg'],
            fg=self.colors['text'],
            font=("Helvetica", 12),
            wraplength=250
        )
        self.image_label.pack(fill=tk.BOTH, expand=True)
        
        # Upload button
        upload_button = tk.Button(
            self.right_frame,
            text="Upload Image",
            bg=self.colors['button'],
            fg=self.colors['white'],
            font=("Helvetica", 12, "bold"),
            relief=tk.FLAT,
            command=self.upload_image
        )
        upload_button.pack(pady=20)
        
        # Analysis result section
        self.analysis_frame = tk.Frame(self.right_frame, bg=self.colors['bg'])
        self.analysis_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.analysis_label = tk.Label(
            self.analysis_frame,
            text="Skin analysis will appear here after upload",
            bg=self.colors['bg'],
            fg=self.colors['text'],
            font=("Helvetica", 12),
            wraplength=250,
            justify=tk.LEFT
        )
        self.analysis_label.pack(fill=tk.BOTH, expand=True)
    
    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
        )
        
        if file_path:
            try:
                # Open and resize image
                image = Image.open(file_path)
                image = image.resize((250, 250), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                
                # Update image display
                self.image_label.config(image=photo, text="")
                self.image_label.image = photo  # Keep a reference
                
                # Get file name for reference
                file_name = os.path.basename(file_path)
                
                # Simulate analysis
                self.perform_skin_analysis(file_name)
                
                # Add to chat
                self.update_chat("You", f"I've uploaded an image for skin analysis: {file_name}")
                self.update_chat("Skincare Assistant", f"I've analyzed your skin image ({file_name}). You can see the results in the analysis panel.")
                
            except Exception as e:
                self.update_chat("Skincare Assistant", f"Sorry, there was an error processing your image: {str(e)}")
    
    def perform_skin_analysis(self, file_name):
        # This is a simulated analysis - in a real app, you'd integrate with ML/AI
        import random
        
        skin_types = ["Normal", "Dry", "Oily", "Combination", "Sensitive"]
        concerns = ["Acne", "Redness", "Dryness", "Hyperpigmentation", "Fine lines", "Enlarged pores"]
        
        selected_type = random.choice(skin_types)
        selected_concerns = random.sample(concerns, k=random.randint(1, 3))
        
        analysis_text = f"Skin Analysis Results:\n\n" \
                       f"Detected Skin Type: {selected_type}\n\n" \
                       f"Detected Concerns:\n"
        
        for concern in selected_concerns:
            analysis_text += f"• {concern}\n"
        
        analysis_text += "\nRecommended Ingredients:\n"
        
        if "Acne" in selected_concerns:
            analysis_text += "• Salicylic Acid\n• Benzoyl Peroxide\n"
        if "Redness" in selected_concerns:
            analysis_text += "• Niacinamide\n• Centella Asiatica\n"
        if "Dryness" in selected_concerns:
            analysis_text += "• Hyaluronic Acid\n• Ceramides\n"
        if "Hyperpigmentation" in selected_concerns:
            analysis_text += "• Vitamin C\n• Alpha Arbutin\n"
        if "Fine lines" in selected_concerns:
            analysis_text += "• Retinol\n• Peptides\n"
        if "Enlarged pores" in selected_concerns:
            analysis_text += "• BHA\n• Clay\n"
        
        self.analysis_label.config(text=analysis_text)
    
    def process_user_input(self):
        user_message = self.user_input.get("1.0", tk.END).strip()
        if user_message:
            self.update_chat("You", user_message)
            self.get_bot_response(user_message)
            self.clear_input()
    
    def get_bot_response(self, user_message):
        # Convert to lowercase for matching
        user_message_lower = user_message.lower()
        
        # Check if we have a direct match in our database
        if user_message_lower in self.qa_database:
            response = self.qa_database[user_message_lower]
            self.update_chat("Skincare Assistant", response)
            return
        
        # Check for keyword matches
        best_match = None
        highest_score = 0
        
        for question, answer in self.qa_database.items():
            # Simple keyword matching algorithm
            words = set(re.findall(r'\b\w+\b', user_message_lower))
            question_words = set(re.findall(r'\b\w+\b', question))
            
            # Calculate match score based on word overlap
            common_words = words.intersection(question_words)
            if common_words:
                score = len(common_words) / len(question_words)
                if score > highest_score:
                    highest_score = score
                    best_match = answer
        
        # If we found a reasonable match (threshold can be adjusted)
        if highest_score > 0.3:
            self.update_chat("Skincare Assistant", best_match)
        else:
            self.update_chat("Skincare Assistant", "I'm not sure about that. Could you rephrase your question? Common topics include acne, dry skin, skincare routines, specific ingredients, or skin types.")
    
    def update_chat(self, sender, message):
        self.chat_display.config(state='normal')
        
        # Format based on sender
        if sender == "You":
            self.chat_display.insert(tk.END, f"\n{sender}: ", "user")
            self.chat_display.tag_configure("user", foreground="#375F4C", font=("Helvetica", 12, "bold"))
        else:
            self.chat_display.insert(tk.END, f"\n{sender}: ", "bot")
            self.chat_display.tag_configure("bot", foreground="#4F6F5A", font=("Helvetica", 12, "bold"))
        
        # Insert the message
        self.chat_display.insert(tk.END, f"{message}\n")
        
        # Auto scroll to the bottom
        self.chat_display.see(tk.END)
        self.chat_display.config(state='disabled')
    
    def clear_input(self):
        self.user_input.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SkincareChatbot(root)
    root.mainloop()