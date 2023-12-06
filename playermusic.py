import tkinter as tk
from tkinter import ttk, filedialog
import pygame
import os
from ttkthemes import ThemedStyle

class AppleMusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Apple Music Player")

        style = ThemedStyle(self.master)
        style.set_theme("clearlooks")

        self.current_track = None
        self.paused = False
        self.volume = 0.5
        self.looping = False

        self.create_widgets()

    def create_widgets(self):
        self.background_canvas = tk.Canvas(self.master, width=600, height=400, bg="lightgray")
        self.background_canvas.pack()
        # File Selection Button
        self.select_button = ttk.Button(self.master, text="Select Track", command=self.select_track)
        self.select_button.pack(pady=10)

        # Track Info Label
        self.track_info_label = ttk.Label(self.master, text="Now Playing: None", font=("Helvetica", 12))
        self.track_info_label.pack(pady=10)

        # Album Art
        self.album_art_label = ttk.Label(self.master, text="Album Art", font=("Helvetica", 12))
        self.album_art_label.pack(pady=10)

        # Playback Controls
        control_frame = ttk.Frame(self.master)
        control_frame.pack(pady=10)

        self.play_button = ttk.Button(control_frame, text="Play", command=self.play_pause_toggle)
        self.play_button.grid(row=0, column=0, padx=10)
        self.stop_button = ttk.Button(control_frame, text="Stop", command=self.stop)
        self.stop_button.grid(row=0, column=1, padx=10)
        self.next_button = ttk.Button(control_frame, text="Next Track", command=self.play_next_track)
        self.next_button.grid(row=0, column=2, padx=10)
        self.volume_up_button = ttk.Button(control_frame, text="Volume Up", command=self.volume_up)
        self.volume_up_button.grid(row=0, column=3, padx=10)
        self.volume_down_button = ttk.Button(control_frame, text="Volume Down", command=self.volume_down)
        self.volume_down_button.grid(row=0, column=4, padx=10)
        self.loop_button = ttk.Button(control_frame, text="Toggle Loop", command=self.toggle_loop)
        self.loop_button.grid(row=0, column=5, padx=10)

        # Volume Scale
        self.volume_scale = ttk.Scale(self.master, from_=0.0, to=1.0, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.set(self.volume)
        self.volume_scale.pack(pady=10)

    def select_track(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if file_path:
            self.current_track = file_path
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)

            # Update track info and album art (placeholder)
            self.track_info_label.config(text=f"Now Playing: {os.path.basename(file_path)}")
            self.album_art_label.config(text="Album Art: Placeholder")

    def play_pause_toggle(self):
        if self.current_track:
            if not self.paused:
                pygame.mixer.music.play(-1 if self.looping else 0)
            else:
                pygame.mixer.music.unpause()
            self.paused = not self.paused

    def stop(self):
        pygame.mixer.music.stop()
        self.paused = False

    def volume_up(self):
        self.volume = min(1.0, self.volume + 0.1)
        pygame.mixer.music.set_volume(self.volume)
        self.volume_scale.set(self.volume)

    def volume_down(self):
        self.volume = max(0.0, self.volume - 0.1)
        pygame.mixer.music.set_volume(self.volume)
        self.volume_scale.set(self.volume)

    def set_volume(self, value):
        self.volume = float(value)
        pygame.mixer.music.set_volume(self.volume)

    def toggle_loop(self):
        self.looping = not self.looping

    def play_next_track(self):
        # Placeholder for handling next track logic
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = AppleMusicPlayer(root)
    root.mainloop()
