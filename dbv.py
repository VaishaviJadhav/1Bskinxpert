import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from PIL import Image, ImageTk

class SkinExpertDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("SkinXpert - Your Personal Skin Care Assistant")
        self.root.state('zoomed')  # Full screen for Windows
        
        # Set color scheme based on the provided image
        self.primary_color = "#4D614D"  # Sage green
        self.secondary_color = "#E1E6DD"  # Light sage/mint
        self.bg_color = "#E1E6DD"  # Light sage background
        self.text_color = "#32403A"  # Dark sage
        self.accent_color = "#C8A95B"  # Gold accent
        self.light_text = "#FFFFFF"  # White text
        
        # ===== BACKGROUND IMAGE PATH =====
        # CHANGE THIS PATH to your Canva image filename
        self.background_image_path = "gcr1.jpg"  # <- REPLACE WITH YOUR IMAGE FILENAME
        # ==================================
        
        self.current_frame = None
        
        # Create main frame
        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create header frame
        self.create_header()
        
        # Create content area
        self.content_area = tk.Frame(self.main_frame, bg=self.bg_color)
        self.content_area.pack(fill=tk.BOTH, expand=True)
        
        # Create sidebar and content frames
        self.create_sidebar()
        
        # Default page - Home
        self.show_page("home")
    
    def create_header(self):
        """Create the header with logo and logout button"""
        header = tk.Frame(self.main_frame, bg=self.primary_color, height=70)
        header.pack(fill=tk.X)
        
        # Logo/Title
        logo_label = tk.Label(header, text="SkinXpert", font=("Times New Roman", 26, "bold"), 
                             bg=self.primary_color, fg=self.light_text)
        logo_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Logout button
        logout_btn = tk.Button(header, text="Logout", font=("Helvetica", 12),
                              bg=self.accent_color, fg=self.text_color, 
                              activebackground="#B59B4E", 
                              activeforeground=self.light_text,
                              cursor="hand2", bd=0, padx=15, pady=5,
                              command=self.logout)
        logout_btn.pack(side=tk.RIGHT, padx=20, pady=15)
    
    def create_sidebar(self):
        """Create the sidebar with navigation buttons"""
        # Sidebar container
        sidebar = tk.Frame(self.content_area, bg=self.primary_color, width=250)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)  # Keep the width fixed
        
        # Main content container
        self.page_container = tk.Frame(self.content_area, bg=self.bg_color)
        self.page_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Sidebar title
        sidebar_title = tk.Label(sidebar, text="Decode Your Skin", font=("Times New Roman", 18, "bold"),
                               bg=self.primary_color, fg=self.light_text)
        sidebar_title.pack(pady=(30, 20))
        
        # Gold separator line
        separator = tk.Frame(sidebar, height=2, bg=self.accent_color)
        separator.pack(fill=tk.X, padx=20, pady=5)
        
        # Navigation buttons
        nav_items = [
            {"name": "home", "text": "Home", "icon": "🏠"},
            {"name": "remedies", "text": "Home Remedies", "icon": "🌿"},
            {"name": "routine", "text": "My Routine", "icon": "⏰"},
            {"name": "chatbot", "text": "Skin Advisor", "icon": "💬"},
            {"name": "quiz", "text": "Quiz Results", "icon": "📋"},
            {"name": "cleanser", "text": "Cleansers", "icon": "❤️"},
            {"name": "sunscreen", "text": "Sunscreens", "icon": "🛒"},
            {"name": "toner", "text": "Toners", "icon": "👤"},
            {"name": "moisturizer", "Moisturizers": "Settings", "icon": "⚙️"}
        ]
        
        # Create a frame for buttons to control their width
        btn_container = tk.Frame(sidebar, bg=self.primary_color)
        btn_container.pack(fill=tk.X, padx=20, pady=10)
        
        for item in nav_items:
            btn = tk.Button(btn_container, 
                           text=f"{item['icon']} {item['text']}", 
                           font=("Helvetica", 12),
                           bg=self.primary_color, 
                           fg=self.light_text,
                           activebackground=self.accent_color,
                           activeforeground=self.text_color,
                           bd=0, cursor="hand2",
                           anchor="w", padx=10, pady=10,
                           width=20,
                           command=lambda i=item["name"]: self.show_page(i))
            btn.pack(fill=tk.X, pady=2)
        
        # Gold accent at bottom
        bottom_accent = tk.Label(sidebar, text="Unlock Your Glow!", font=("Times New Roman", 14, "italic"),
                               bg=self.primary_color, fg=self.accent_color)
        bottom_accent.pack(side=tk.BOTTOM, pady=20)
    
    def show_page(self, page_name):
        """Show the selected page"""
        # Clear current page
        if self.current_frame:
            self.current_frame.destroy()
        
        # Create new page frame
        self.current_frame = tk.Frame(self.page_container, bg=self.bg_color)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
        # Add background image if on home page
        if page_name == "home" and self.background_image_path:
            self.set_background_image()
        
        # Page title
        title_mapping = {
            "home": "Welcome to SkinXpert",
            "remedies": "Natural Home Remedies",
            "favorites": "Your Favorites",
            "cart": "Shopping Cart",
            "chatbot": "Skin Advisor Chat",
            "quiz": "Your Skin Quiz Results",
            "routine": "Your Skincare Routine",
            "profile": "User Profile",
            "settings": "Application Settings"
        }
        
        title = title_mapping.get(page_name, "SkinXpert")
        
        # Title container with accent border
        title_container = tk.Frame(self.current_frame, bg=self.bg_color)
        title_container.pack(pady=40)
        
        page_title = tk.Label(title_container, text=title, 
                             font=("Times New Roman", 24, "bold"),
                             bg=self.bg_color, fg=self.text_color)
        page_title.pack(pady=5)
        
        # Gold underline for title
        underline = tk.Frame(title_container, height=2, width=300, bg=self.accent_color)
        underline.pack()
        
        # Placeholder content
        if page_name == "home":
            self.create_home_page()
        else:
            content = tk.Label(self.current_frame, 
                              text=f"This is the {page_name} page. Add your content here.",
                              font=("Helvetica", 14),
                              bg=self.bg_color, fg=self.text_color)
            content.pack(pady=20)
    
    def set_background_image(self):
        """Set the background image for the homepage"""
        try:
            # Open and resize image to fit the window
            original = Image.open(self.background_image_path)
            
            # Get container dimensions
            container_width = self.page_container.winfo_width()
            container_height = self.page_container.winfo_height()
            
            # If container size is not available yet, use screen dimensions
            if container_width <= 1:
                container_width = self.root.winfo_screenwidth() - 250  # Account for sidebar
                container_height = self.root.winfo_screenheight() - 70  # Account for header
            
            # Resize image
            resized = original.resize((container_width, container_height), Image.LANCZOS)
            
            # Convert to PhotoImage
            bg_image = ImageTk.PhotoImage(resized)
            
            # Create a label with the image
            bg_label = tk.Label(self.current_frame, image=bg_image)
            bg_label.image = bg_image  # Keep a reference
            
            # Place the label at the bottom of the stacking order
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            
        except Exception as e:
            print(f"Could not load background image: {e}")
            # If image loading fails, continue without background
    
    def create_home_page(self):
        """Create a more attractive home page"""
        pass
        # Features section - creating this with a transparent background to overlay on the image
        # features_frame = tk.Frame(self.current_frame, bg=self.bg_color)
        # features_frame.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)
        
        # # Make the frame transparent
        # features_frame.configure(bg="")
        
        # features = [
        #     {"icon": "📋", "title": "Take a Quick Quiz", "desc": "Find your skin needs and get personalized recommendations."},
        #     {"icon": "⏰", "title": "Get a Personalized Routine", "desc": "Custom skincare routines tailored to your unique skin."},
        #     {"icon": "✨", "title": "Achieve Healthy, Glowing Skin", "desc": "Effortlessly reach your skincare goals with expert guidance."}
        # ]
        
        # for i, feature in enumerate(features):
        #     # Create a partially transparent background for the feature box
        #     feature_box = tk.Frame(features_frame, bg=self.secondary_color, padx=20, pady=20,
        #                           highlightbackground=self.accent_color, highlightthickness=1)
        #     feature_box.grid(row=0, column=i, padx=10, sticky="nsew")
            
        #     # Configure column weights
        #     features_frame.columnconfigure(i, weight=1)
            
        #     # Icon
        #     icon_label = tk.Label(feature_box, text=feature["icon"], font=("Helvetica", 24),
        #                         bg=self.secondary_color)
        #     icon_label.pack(pady=(0, 10))
            
        #     # Title
        #     title_label = tk.Label(feature_box, text=feature["title"], font=("Times New Roman", 16, "bold"),
        #                          bg=self.secondary_color, fg=self.text_color)
        #     title_label.pack(pady=(0, 5))
            
        #     # Description
        #     desc_label = tk.Label(feature_box, text=feature["desc"], font=("Helvetica", 12),
        #                         bg=self.secondary_color, fg=self.text_color, wraplength=200)
        #     desc_label.pack()
    
    def logout(self):
        """Handle logout functionality"""
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.root.destroy()
            # Here you would typically redirect to login screen

# Main function to run the application
def main():
    root = tk.Tk()
    app = SkinExpertDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()