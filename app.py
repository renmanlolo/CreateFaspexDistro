import tkinter as tk
from tkinter import ttk
from frames import HeaderFrame, FormFrame

COLOUR_PRIMARY = "#00272B"
COLOUR_SECONDARY = "#007682"
COLOUR_LIGHT_TEXT = "#C8F1FF"
COLOUR_LIGHT_BACKGROUND = "#E1EEEE"
COLOUR_DARK_TEXT = "003C42"


class CreateJSONApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Background.TFrame", background=COLOUR_PRIMARY)

        style.configure(
            "LightText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
            font=("Courier New", 14, "bold")
        )

        style.configure(
            "EntryBG.TEntry",
            fieldbackground=COLOUR_LIGHT_TEXT,
            foreground=COLOUR_DARK_TEXT,
            font=("Courier New", 18)
        )

        style.configure(
            "combobox_style.TCombobox",
            fieldbackground=COLOUR_LIGHT_BACKGROUND,
            foreground=COLOUR_DARK_TEXT,
            arrowsize=20,
            font=("Courier New", 18)
        )

        style.configure(
            "AppButton.TButton",
            background=COLOUR_SECONDARY,
            foreground=COLOUR_LIGHT_TEXT,
        )

        style.map(
            "AppButton.TButton",
            background=[("pressed", "#fff"), ("active", COLOUR_PRIMARY)],
            foreground=[("pressed", COLOUR_PRIMARY)]
        )

        # -- configure the root window --
        self.title("CreateFaspexDistro")
        self["background"] = COLOUR_PRIMARY

        # -- main container ---
        container = ttk.Frame(self, style="Background.TFrame")
        container.grid()
        container.columnconfigure(0, weight=1)

        header_frame = HeaderFrame(container, relief="solid")
        form_frame = FormFrame(container)
        header_frame.grid(column=0, row=0, pady=(60, 10), padx=(40, 40))
        form_frame.grid(column=0, row=1, pady=(30, 10), padx=(40, 40))


if __name__ == "__main__":
    app = CreateJSONApp()
    app.option_add("*TCombobox*Listbox*Background", COLOUR_LIGHT_BACKGROUND)
    app.mainloop()
