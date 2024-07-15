import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import random
import requests
from io import BytesIO

class Magic8BallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Magic 8 Ball")
        
        self.responses = [
            "1.gif",
            "2.gif",
            "3.gif",
            "4.gif",
            "5.gif",
            "6.gif",
            "7.gif",
            "8.gif",
            "9.gif",
            "10.gif",
            "11.gif",
            # Add more response GIF URLs here
        ]
        
        self.response_label = tk.Label(self.root)
        self.response_label.pack(pady=20)
        
        self.start_button = tk.Button(self.root, text="Drink from Mimir's Well", command=self.start_game)
        self.start_button.pack(pady=10)
        
        self.restart_button = tk.Button(self.root, text="Ask Another Question", command=self.restart_game, state=tk.DISABLED)
        self.restart_button.pack(pady=10)
        
        # Preload frames for default GIF
        self.default_gif_path = "default.gif"  # Replace with your default GIF path or URL
        self.default_frames = self.load_frames(self.default_gif_path)
        self.current_frames = self.default_frames
        
        # Show default GIF initially
        self.show_frames(self.current_frames)
        self.enable_start_button()  # Enable start button initially
        
    def enable_start_button(self):
        self.start_button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.DISABLED)
    
    def start_game(self):
        response_url = random.choice(self.responses)
        print(f"Selected response URL: {response_url}")  # Debug print statement
        self.current_frames = self.load_frames(response_url)
        self.show_frames(self.current_frames)
        self.start_button.config(state=tk.DISABLED)
        self.restart_button.config(state=tk.DISABLED)  # Disable both buttons during animation
        
    def restart_game(self):
        self.current_frames = self.default_frames
        self.show_frames(self.current_frames)
        self.enable_start_button()  # Enable start button after restart
        
    def load_frames(self, gif_url):
        try:
            if gif_url.startswith('http'):
                response = requests.get(gif_url)
                gif_image = Image.open(BytesIO(response.content))
            else:
                gif_image = Image.open(gif_url)
            
            frames = []
            for frame in ImageSequence.Iterator(gif_image):
                frame = frame.convert("RGBA")
                frames.append((ImageTk.PhotoImage(frame), gif_image.info['duration']))  # Store frame and duration
            
            return frames
        
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to load response GIF: {e}")
            return []
    
    def show_frames(self, frames):
        self.current_frames = frames
        self.current_frame_index = 0
        self.show_next_frame()
    
    def show_next_frame(self):
        if self.current_frame_index < len(self.current_frames):
            frame, duration = self.current_frames[self.current_frame_index]
            self.response_label.configure(image=frame)
            self.current_frame_index += 1
            self.root.after(duration, self.show_next_frame)
        else:
            self.restart_button.config(state=tk.NORMAL)  # Enable restart button after animation

if __name__ == "__main__":
    root = tk.Tk()
    app = Magic8BallApp(root)
    root.mainloop()
