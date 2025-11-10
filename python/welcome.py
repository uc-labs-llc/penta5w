import tkinter as tk
from tkinter import font as tkfont

# --- Configuration for Dark Theme ---
BG_COLOR_MAIN = '#1a1a2e'    # Dark background matching project theme
FG_COLOR_TEXT = '#FFFFFF'    # White text
ACCENT_COLOR = '#667eea'     # Primary accent color (Blue/Purple)
CARD_BG_COLOR = '#252547'    # Slightly lighter background for the content box

def create_penta_w_welcome_window():
    """Creates a visually appealing Tkinter window with the welcome message."""
    
    # 1. Setup the main window
    root = tk.Tk()
    root.title("Penta-W Framework Welcome")
    root.configure(bg=BG_COLOR_MAIN)
    
    # Calculate window position to center it on the screen
    window_width = 700
    window_height = 350
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.resizable(False, False) # Prevent resizing for clean look

    # 2. Define custom fonts
    # Using 'Inter' (or a close system default like Arial) since custom fonts 
    # require extra steps; we rely on size and weight for impact.
    
    large_font = tkfont.Font(family="Inter", size=24, weight="bold")
    # FIX: Changed "heavy" to "bold" to fix TclError.
    accent_font = tkfont.Font(family="Inter", size=36, weight="bold") 
    body_font = tkfont.Font(family="Inter", size=16)

    # 3. Create a styled container Frame (the "Card")
    card_frame = tk.Frame(root, bg=CARD_BG_COLOR, padx=40, pady=40, relief=tk.RIDGE, bd=5, highlightbackground=ACCENT_COLOR, highlightthickness=2)
    card_frame.pack(expand=True, padx=30, pady=30)

    # 4. Add Welcome Text
    tk.Label(
        card_frame, 
        text="Hello and Welcome to The",
        bg=CARD_BG_COLOR, 
        fg=FG_COLOR_TEXT, 
        font=large_font
    ).pack(pady=(0, 5))

    # 5. Add the Penta-W Framework Title (Accent Color)
    tk.Label(
        card_frame, 
        text="Penta-W Framework",
        bg=CARD_BG_COLOR, 
        fg=ACCENT_COLOR, 
        font=accent_font
    ).pack(pady=5)
    
    # 6. Add the Subtitle
    tk.Label(
        card_frame, 
        text="for Conceptual Clarity (5 W)",
        bg=CARD_BG_COLOR, 
        fg=FG_COLOR_TEXT, 
        font=body_font
    ).pack(pady=(5, 20))

    # 7. Add a Call to Action / Context Button
    tk.Button(
        card_frame, 
        text="Explore the 5 Ws",
        bg=ACCENT_COLOR, 
        fg=FG_COLOR_TEXT, 
        activebackground=ACCENT_COLOR,
        activeforeground=FG_COLOR_TEXT,
        font=body_font,
        cursor="hand2",
        command=lambda: root.destroy(), # Simple action to close the window
        relief=tk.FLAT,
        padx=20,
        pady=10
    ).pack(pady=(10, 0))

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    create_penta_w_welcome_window()
