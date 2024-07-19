import tkinter as tk
from tkinter import PhotoImage, messagebox
from jarvis import Jarvis  # Ensure this file is saved as jarvis.py

class JarvisApp:
    def __init__(self, root):
        self.jarvis = Jarvis()
        self.root = root
        self.root.title("Jarvis Voice Assistant")
        self.root.geometry("400x300")
        self.root.configure(bg="#2C3E50")  # Dark background color

        # Load and set logo image
        self.logo_img = PhotoImage(file="logo.png")  # Add a logo image to your project directory
        self.logo_label = tk.Label(root, image=self.logo_img, bg="#2C3E50")
        self.logo_label.pack(pady=20)

        # Title Label
        self.title_label = tk.Label(root, text="Jarvis Voice Assistant", font=("Helvetica", 18, "bold"), fg="#ECF0F1", bg="#2C3E50")
        self.title_label.pack(pady=10)

        # Start Button
        self.start_button = tk.Button(root, text="Start", command=self.start_jarvis, font=("Helvetica", 14), bg="#27AE60", fg="#FFFFFF", height=2, width=15)
        self.start_button.pack(pady=10)

        # Quit Button
        self.quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Helvetica", 14), bg="#E74C3C", fg="#FFFFFF", height=2, width=15)
        self.quit_button.pack(pady=10)

    def start_jarvis(self):
        try:
            self.jarvis.wishMe()
            self.jarvis.executeTask()
        except Exception as e:
            messagebox.showerror("Error", "An error occurred: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisApp(root)
    root.mainloop()
