import os
import tkinter as tk
from tkinter import filedialog
import pygame

class AudiobookPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Audiobook Player")
        self.current_book = None
        self.playlist = []
        self.current_index = 0

        # Create and configure the GUI components
        self.create_gui()
        
        # Initialize Pygame
        pygame.init()
        
    def create_gui(self):
        # Create and configure the GUI components
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(pady=10)
        
        open_button = tk.Button(self.root, text="Open Audiobook", command=self.open_audiobook)
        open_button.pack(pady=10)
        
        play_button = tk.Button(self.root, text="Play", command=self.play)
        play_button.pack()
        
        pause_button = tk.Button(self.root, text="Pause", command=self.pause)
        pause_button.pack()
        
        stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        stop_button.pack()

    def open_audiobook(self):
        audiobook_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.m4a *.ogg")])
        if audiobook_file:
            self.playlist.append(audiobook_file)
            self.listbox.insert(tk.END, os.path.basename(audiobook_file))
    
    def play(self):
        if not self.current_book:
            if self.playlist:
                self.current_book = pygame.mixer.music
                self.current_book.load(self.playlist[self.current_index])
                self.current_book.play()
        else:
            self.current_book.unpause()
    
    def pause(self):
        if self.current_book:
            self.current_book.pause()
    
    def stop(self):
        if self.current_book:
            self.current_book.stop()
            self.current_book = None
    
if __name__ == "__main__":
    root = tk.Tk()
    app = AudiobookPlayer(root)
    root.mainloop()
