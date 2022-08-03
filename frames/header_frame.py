from tkinter import ttk
from PIL import Image, ImageTk

COLOUR_PRIMARY = "#00272B"
COLOUR_SECONDARY = "#007682"
COLOUR_LIGHT_TEXT = "#C8F1FF"  # "#7EADB7"
COLOUR_LIGHT_BACKGROUND = "#E1EEEE"
COLOUR_DARK_TEXT = "003C42"


class HeaderFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self["style"] = "Background.TFrame"

        self.co3_logo_orig = Image.open("co3_sig_logo.png")
        self.resized = self.co3_logo_orig.resize((457, 75), Image.Resampling.LANCZOS)
        self.co3_logo_resized = ImageTk.PhotoImage(self.resized)
        self.co3_label = ttk.Label(self, image=self.co3_logo_resized, borderwidth=1, background=COLOUR_PRIMARY)
        self.co3_label.grid(column=0, row=0, pady=20)

        # show the frame on the container
        self.grid(column=0, row=0)
