import tkinter as tk
from tkinter import ttk, messagebox, font
from PIL import Image, ImageTk
import json
import os

class SkinCareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Natural Skin Remedies")
        self.root.geometry("1000x650")
        self.root.configure(bg="#f5f5f5")
        
        # Custom fonts
        self.title_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.subtitle_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.text_font = font.Font(family="Helvetica", size=11)
        
        # Load data
        self.load_data()
        
        # Create main frames
        self.create_header()
        self.create_sidebar()
        self.create_main_frame()
        
        # Start with the dashboard
        self.show_dashboard()
    
    def load_data(self):
        # Initialize with default data if no saved file exists
        self.remedies = {
            "Dry Skin": [
                {"name": "Honey & Avocado Mask", "ingredients": ["2 tbsp honey", "1/2 ripe avocado"], 
                 "instructions": "Mix ingredients into a paste. Apply to face for 15-20 minutes, then rinse with warm water."},
                {"name": "Olive Oil Massage", "ingredients": ["1 tbsp olive oil", "2-3 drops lavender essential oil (optional)"], 
                 "instructions": "Warm oil slightly. Massage into skin using circular motions. Leave for 30 minutes, then rinse."},
                {"name": "Oatmeal Bath", "ingredients": ["1 cup colloidal oatmeal", "1 tbsp honey"], 
                 "instructions": "Add ingredients to warm bath water. Soak for 15-20 minutes. Pat skin dry afterwards."}
            ],
            "Oily Skin": [
                {"name": "Clay & Tea Tree Mask", "ingredients": ["1 tbsp bentonite clay", "1 tbsp apple cider vinegar", "2 drops tea tree oil"], 
                 "instructions": "Mix ingredients to form a paste. Apply to face, avoiding eye area. Rinse after 10-15 minutes."},
                {"name": "Lemon & Honey Toner", "ingredients": ["1 tbsp lemon juice", "1 tbsp honey", "1/2 cup water"], 
                 "instructions": "Mix ingredients well. Apply to face with cotton pad after cleansing. Use in evenings only."},
                {"name": "Tomato & Sugar Scrub", "ingredients": ["1/2 tomato pulp", "1 tbsp sugar"], 
                 "instructions": "Mix ingredients together. Gently massage onto face. Rinse after 5 minutes."}
            ],
            "Combination Skin": [
                {"name": "Yogurt & Honey Mask", "ingredients": ["2 tbsp plain yogurt", "1 tsp honey", "1 tsp lemon juice (optional)"], 
                 "instructions": "Mix ingredients well. Apply to face for 15 minutes. Rinse with cool water."},
                {"name": "Green Tea Toner", "ingredients": ["1/4 cup brewed green tea (cooled)", "1/4 cup witch hazel"], 
                 "instructions": "Mix ingredients and store in fridge. Apply with cotton pad morning and night."},
                {"name": "Aloe & Cucumber Gel", "ingredients": ["2 tbsp aloe vera gel", "1/4 cucumber (blended)"], 
                 "instructions": "Blend ingredients until smooth. Apply to face. Can be left on or rinsed after 20 minutes."}
            ],
            "Hyperpigmentation": [
                {"name": "Turmeric Brightening Mask", "ingredients": ["1 tsp turmeric powder", "1 tbsp yogurt", "1 tsp honey"], 
                 "instructions": "Mix ingredients to form a paste. Apply to affected areas for 15 minutes. Rinse thoroughly."},
                {"name": "Licorice Root Extract", "ingredients": ["1 tsp licorice root extract", "1 tbsp aloe vera gel"], 
                 "instructions": "Mix ingredients well. Apply to dark spots at night. Use consistently for best results."},
                {"name": "Vitamin C Serum", "ingredients": ["1/4 tsp vitamin C powder", "1 tbsp distilled water", "1 tsp glycerin"], 
                 "instructions": "Mix ingredients. Apply to face after cleansing. Store in dark bottle in fridge for up to 1 week."}
            ],
            "Sensitive Skin": [
                {"name": "Chamomile Soothing Mask", "ingredients": ["2 tbsp brewed chamomile tea (cooled)", "1 tbsp oat flour"], 
                 "instructions": "Mix into a paste. Apply to clean face for 10 minutes. Rinse with cool water."},
                {"name": "Cucumber Cooling Gel", "ingredients": ["1/2 cucumber (blended)", "1 tbsp aloe vera gel"], 
                 "instructions": "Blend ingredients until smooth. Apply to irritated areas as needed. Store in fridge."},
                {"name": "Oat & Honey Cleanser", "ingredients": ["2 tbsp ground oats", "1 tsp honey", "1 tbsp water"], 
                 "instructions": "Mix ingredients. Gently massage onto damp skin. Rinse with lukewarm water."}
            ]
        }
        
        self.favorites = []
        
        # Load saved data if available
        try:
            if os.path.exists('skincare_data.json'):
                with open('skincare_data.json', 'r') as f:
                    data = json.load(f)
                    self.remedies = data.get('remedies', self.remedies)
                    self.favorites = data.get('favorites', [])
        except Exception as e:
            messagebox.showerror("Error", f"Could not load saved data: {e}")
    
    def save_data(self):
        data = {
            'remedies': self.remedies,
            'favorites': self.favorites
        }
        try:
            with open('skincare_data.json', 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Could not save data: {e}")
    
    def create_header(self):
        header_frame = tk.Frame(self.root, bg="#c5e1a5", height=70)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        label = tk.Label(header_frame, text="Natural Skin Remedies", font=self.title_font, bg="#c5e1a5", fg="#33691e")
        label.pack(pady=15)
    
    def create_sidebar(self):
        self.sidebar = tk.Frame(self.root, bg="#dcedc8", width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)
        
        # Dashboard button
        # dashboard_btn = tk.Button(self.sidebar, text="Dashboard", bg="#aed581", fg="#33691e", 
        #                         font=self.subtitle_font, bd=0, width=18, pady=10,
        #                         command=self.show_dashboard)
        # dashboard_btn.pack(pady=(20, 10))
        
        dashboard_btn = tk.Button(self.sidebar, text="Dashboard", bg="#aed581", fg="#33691e", 
                          font=self.subtitle_font, bd=0, width=18, pady=10,
                          command=self.show_dashboard)  # Calls the function to open D1.py
        dashboard_btn.pack(pady=(20, 10))





        # Skin type category buttons
        for category in self.remedies.keys():
            btn = tk.Button(self.sidebar, text=category, bg="#dcedc8", fg="#33691e", 
                         font=self.text_font, bd=0, width=20, pady=8,
                         command=lambda cat=category: self.show_category(cat))
            btn.pack(pady=5)
        
        # Favorites button
        favorites_btn = tk.Button(self.sidebar, text="My Favorites", bg="#dcedc8", fg="#33691e", 
                               font=self.text_font, bd=0, width=20, pady=8,
                               command=self.show_favorites)
        favorites_btn.pack(pady=5)
        
        # Add new remedy button
        add_btn = tk.Button(self.sidebar, text="Add New Remedy", bg="#8bc34a", fg="white", 
                          font=self.text_font, bd=0, width=20, pady=8,
                          command=self.open_add_remedy)
        add_btn.pack(pady=(20, 10))
    
    def create_main_frame(self):
        # Create main content area
        self.main_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    def clear_main_frame(self):
        # Clear all widgets from main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_dashboard(self):
        self.clear_main_frame()
        
        # Welcome section
        welcome_frame = tk.Frame(self.main_frame, bg="#f5f5f5", padx=30, pady=20)
        welcome_frame.pack(fill=tk.X)
        
        tk.Label(welcome_frame, text="Welcome to Your Natural Skin Care Guide", font=self.title_font, bg="#f5f5f5").pack(anchor="w")
        tk.Label(welcome_frame, text="Discover natural remedies for your specific skin concerns", 
                font=self.text_font, bg="#f5f5f5").pack(anchor="w", pady=(5, 20))
        
        # Create category cards
        categories_frame = tk.Frame(self.main_frame, bg="#f5f5f5", padx=20)
        categories_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configure grid
        categories_frame.columnconfigure(0, weight=1)
        categories_frame.columnconfigure(1, weight=1)
        categories_frame.columnconfigure(2, weight=1)
        
        # Create a card for each skin type
        row, col = 0, 0
        for category in self.remedies.keys():
            card = tk.Frame(categories_frame, bg="white", bd=1, relief=tk.RAISED, padx=15, pady=15)
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            tk.Label(card, text=category, font=self.subtitle_font, bg="white").pack(pady=(0, 10))
            tk.Label(card, text=f"{len(self.remedies[category])} remedies available", 
                   font=self.text_font, bg="white").pack()
            
            view_btn = tk.Button(card, text="View Remedies", bg="#8bc34a", fg="white", 
                              bd=0, padx=10, pady=5,
                              command=lambda cat=category: self.show_category(cat))
            view_btn.pack(pady=(15, 5))
            
            # Update grid position
            col += 1
            if col > 2:
                col = 0
                row += 1
        
        # Favorite remedies section if any exist
        if self.favorites:
            fav_frame = tk.Frame(self.main_frame, bg="#f5f5f5", padx=30, pady=20)
            fav_frame.pack(fill=tk.X)
            
            tk.Label(fav_frame, text="Your Favorite Remedies", font=self.subtitle_font, bg="#f5f5f5").pack(anchor="w", pady=(20, 10))
            
            # Display up to 3 favorites
            for i, fav in enumerate(self.favorites[:3]):
                fav_item = tk.Frame(fav_frame, bg="white", bd=1, relief=tk.RAISED, padx=15, pady=10)
                fav_item.pack(fill=tk.X, pady=5)
                
                for cat, remedies in self.remedies.items():
                    for remedy in remedies:
                        if f"{cat} - {remedy['name']}" == fav:
                            tk.Label(fav_item, text=remedy['name'], font=self.text_font, bg="white").pack(anchor="w")
                            tk.Label(fav_item, text=f"Category: {cat}", font=("Helvetica", 9), bg="white").pack(anchor="w")
                            break
    
    def show_category(self, category):
        self.clear_main_frame()
        
        # Category header
        header_frame = tk.Frame(self.main_frame, bg="#f5f5f5", padx=30, pady=20)
        header_frame.pack(fill=tk.X)
        
        tk.Label(header_frame, text=f"{category} Remedies", font=self.title_font, bg="#f5f5f5").pack(anchor="w")
        tk.Label(header_frame, text=f"Natural solutions for {category.lower()} concerns", 
                font=self.text_font, bg="#f5f5f5").pack(anchor="w", pady=(5, 0))
        
        # Scrollable frame for remedies
        canvas = tk.Canvas(self.main_frame, bg="#f5f5f5")
        scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f5f5f5")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True, padx=(30, 0))
        scrollbar.pack(side="right", fill="y")
        
        # Display remedies
        for remedy in self.remedies[category]:
            remedy_frame = tk.Frame(scrollable_frame, bg="white", bd=1, relief=tk.RAISED, padx=20, pady=15)
            remedy_frame.pack(fill=tk.X, pady=10, padx=10)
            
            # Title and favorite button row
            title_row = tk.Frame(remedy_frame, bg="white")
            title_row.pack(fill=tk.X)
            
            tk.Label(title_row, text=remedy["name"], font=self.subtitle_font, bg="white").pack(side=tk.LEFT)
            
            # Check if in favorites
            fav_id = f"{category} - {remedy['name']}"
            is_favorite = fav_id in self.favorites
            
            fav_btn = tk.Button(title_row, text="♥" if is_favorite else "♡", 
                             bg="white", fg="#e91e63" if is_favorite else "black", 
                             bd=0, font=("Helvetica", 16),
                             command=lambda r=remedy, c=category: self.toggle_favorite(r, c))
            fav_btn.pack(side=tk.RIGHT)
            
            # Ingredients
            ing_frame = tk.Frame(remedy_frame, bg="white")
            ing_frame.pack(fill=tk.X, pady=(10, 0), anchor="w")
            
            tk.Label(ing_frame, text="Ingredients:", font=("Helvetica", 11, "bold"), bg="white").pack(anchor="w")
            for ing in remedy["ingredients"]:
                tk.Label(ing_frame, text=f"• {ing}", font=self.text_font, bg="white").pack(anchor="w", padx=(15, 0))
            
            # Instructions
            inst_frame = tk.Frame(remedy_frame, bg="white")
            inst_frame.pack(fill=tk.X, pady=(10, 0), anchor="w")
            
            tk.Label(inst_frame, text="Instructions:", font=("Helvetica", 11, "bold"), bg="white").pack(anchor="w")
            tk.Label(inst_frame, text=remedy["instructions"], font=self.text_font, bg="white", 
                   wraplength=600, justify="left").pack(anchor="w", padx=(15, 0))
    
    def show_favorites(self):
        self.clear_main_frame()
        
        # Header
        header_frame = tk.Frame(self.main_frame, bg="#f5f5f5", padx=30, pady=20)
        header_frame.pack(fill=tk.X)
        
        tk.Label(header_frame, text="My Favorite Remedies", font=self.title_font, bg="#f5f5f5").pack(anchor="w")
        tk.Label(header_frame, text="Your saved natural skin care solutions", 
                font=self.text_font, bg="#f5f5f5").pack(anchor="w", pady=(5, 0))
        
        # Main content
        content_frame = tk.Frame(self.main_frame, bg="#f5f5f5", padx=30, pady=10)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        if not self.favorites:
            tk.Label(content_frame, text="You don't have any favorite remedies yet.", 
                   font=self.text_font, bg="#f5f5f5").pack(pady=50)
            
            add_fav_btn = tk.Button(content_frame, text="Browse Remedies", bg="#8bc34a", fg="white", 
                                 bd=0, padx=20, pady=8,
                                 command=self.show_dashboard)
            add_fav_btn.pack()
        else:
            # Scrollable frame for favorites
            canvas = tk.Canvas(content_frame, bg="#f5f5f5")
            scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas, bg="#f5f5f5")
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
            # Display favorites
            for fav in self.favorites:
                category, remedy_name = fav.split(" - ", 1)
                
                # Find the remedy in our data
                remedy = None
                for r in self.remedies[category]:
                    if r["name"] == remedy_name:
                        remedy = r
                        break
                
                if remedy:
                    remedy_frame = tk.Frame(scrollable_frame, bg="white", bd=1, relief=tk.RAISED, padx=20, pady=15)
                    remedy_frame.pack(fill=tk.X, pady=10)
                    
                    # Title row with category and remove button
                    title_row = tk.Frame(remedy_frame, bg="white")
                    title_row.pack(fill=tk.X)
                    
                    tk.Label(title_row, text=remedy["name"], font=self.subtitle_font, bg="white").pack(side=tk.LEFT)
                    tk.Label(title_row, text=f"Category: {category}", font=("Helvetica", 9), bg="white", fg="gray").pack(side=tk.LEFT, padx=(10, 0))
                    
                    fav_btn = tk.Button(title_row, text="♥", bg="white", fg="#e91e63", bd=0, font=("Helvetica", 16),
                                     command=lambda r=remedy, c=category: self.toggle_favorite(r, c))
                    fav_btn.pack(side=tk.RIGHT)
                    
                    # Ingredients
                    ing_frame = tk.Frame(remedy_frame, bg="white")
                    ing_frame.pack(fill=tk.X, pady=(10, 0), anchor="w")
                    
                    tk.Label(ing_frame, text="Ingredients:", font=("Helvetica", 11, "bold"), bg="white").pack(anchor="w")
                    for ing in remedy["ingredients"]:
                        tk.Label(ing_frame, text=f"• {ing}", font=self.text_font, bg="white").pack(anchor="w", padx=(15, 0))
                    
                    # Instructions
                    inst_frame = tk.Frame(remedy_frame, bg="white")
                    inst_frame.pack(fill=tk.X, pady=(10, 0), anchor="w")
                    
                    tk.Label(inst_frame, text="Instructions:", font=("Helvetica", 11, "bold"), bg="white").pack(anchor="w")
                    tk.Label(inst_frame, text=remedy["instructions"], font=self.text_font, bg="white", 
                           wraplength=600, justify="left").pack(anchor="w", padx=(15, 0))
    
    def toggle_favorite(self, remedy, category):
        fav_id = f"{category} - {remedy['name']}"
        
        if fav_id in self.favorites:
            self.favorites.remove(fav_id)
            messagebox.showinfo("Removed", f"'{remedy['name']}' removed from favorites")
        else:
            self.favorites.append(fav_id)
            messagebox.showinfo("Added", f"'{remedy['name']}' added to favorites")
        
        self.save_data()
        
        # Refresh current view
        if self.current_view == "favorites":
            self.show_favorites()
        elif self.current_view == "category":
            self.show_category(self.current_category)
        else:
            self.show_dashboard()
    
    def open_add_remedy(self):
        # Create a new top-level window
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Remedy")
        add_window.geometry("500x600")
        add_window.configure(bg="#f5f5f5")
        add_window.grab_set()  # Make window modal
        
        # Header
        tk.Label(add_window, text="Add New Remedy", font=self.title_font, bg="#f5f5f5").pack(pady=(20, 10))
        
        # Form frame
        form_frame = tk.Frame(add_window, bg="#f5f5f5", padx=30, pady=10)
        form_frame.pack(fill=tk.BOTH, expand=True)
        
        # Category selection
        tk.Label(form_frame, text="Category:", font=self.subtitle_font, bg="#f5f5f5").pack(anchor="w", pady=(10, 5))
        
        category_var = tk.StringVar(value=list(self.remedies.keys())[0])
        category_dropdown = ttk.Combobox(form_frame, textvariable=category_var, values=list(self.remedies.keys()))
        category_dropdown.pack(fill=tk.X, pady=(0, 15))
        
        # Remedy name
        tk.Label(form_frame, text="Remedy Name:", font=self.subtitle_font, bg="#f5f5f5").pack(anchor="w", pady=(10, 5))
        name_entry = tk.Entry(form_frame, font=self.text_font)
        name_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Ingredients
        tk.Label(form_frame, text="Ingredients (one per line):", font=self.subtitle_font, bg="#f5f5f5").pack(anchor="w", pady=(10, 5))
        ingredients_text = tk.Text(form_frame, height=5, font=self.text_font)
        ingredients_text.pack(fill=tk.X, pady=(0, 15))
        
        # Instructions
        tk.Label(form_frame, text="Instructions:", font=self.subtitle_font, bg="#f5f5f5").pack(anchor="w", pady=(10, 5))
        instructions_text = tk.Text(form_frame, height=5, font=self.text_font)
        instructions_text.pack(fill=tk.X, pady=(0, 15))
        
        # Buttons
        buttons_frame = tk.Frame(add_window, bg="#f5f5f5", padx=30, pady=20)
        buttons_frame.pack(fill=tk.X)
        
        tk.Button(buttons_frame, text="Cancel", bg="#e0e0e0", fg="black", bd=0, padx=20, pady=8,
                command=add_window.destroy).pack(side=tk.LEFT, padx=(0, 10))
        
        def save_remedy():
            # Get input values
            category = category_var.get()
            name = name_entry.get().strip()
            ingredients_raw = ingredients_text.get("1.0", tk.END).strip()
            instructions = instructions_text.get("1.0", tk.END).strip()
            
            # Validate
            if not name:
                messagebox.showerror("Error", "Please enter a remedy name")
                return
            
            if not ingredients_raw:
                messagebox.showerror("Error", "Please enter at least one ingredient")
                return
            
            if not instructions:
                messagebox.showerror("Error", "Please enter instructions")
                return
            
            # Format ingredients as list
            ingredients = [ing.strip() for ing in ingredients_raw.split('\n') if ing.strip()]
            
            # Create new remedy
            new_remedy = {
                "name": name,
                "ingredients": ingredients,
                "instructions": instructions
            }
            
            # Add to remedies
            self.remedies[category].append(new_remedy)
            
            # Save data
            self.save_data()
            
            # Close window
            add_window.destroy()
            
            # Show success message
            messagebox.showinfo("Success", f"New remedy '{name}' added to {category} category")
            
            # Refresh view if needed
            if hasattr(self, 'current_view') and hasattr(self, 'current_category'):
                if self.current_view == "category" and self.current_category == category:
                    self.show_category(category)
        
        tk.Button(buttons_frame, text="Save", bg="#8bc34a", fg="white", bd=0, padx=20, pady=8,
                command=save_remedy).pack(side=tk.RIGHT)
    
    def set_current_view(self, view, category=None):
        self.current_view = view
        self.current_category = category

if __name__ == "__main__":
    root = tk.Tk()
    app = SkinCareApp(root)
    root.mainloop()