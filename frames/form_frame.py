import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from faker import Faker
import ast
import json

COLOUR_PRIMARY = "#00272B"
COLOUR_SECONDARY = "#007682"
COLOUR_LIGHT_TEXT = "#C8F1FF"
COLOUR_LIGHT_BACKGROUND = "#E1EEEE"
COLOUR_DARK_TEXT = "#003C42"

servers = {
    "CO3 Faspex": "https://c3mxmitfas.company3.com/aspera/faspex/send/new",
    "Disney Faspex": "https://charles.studio.disney.com/aspera/faspex/"
}


def generate_fake_emails(count: int) -> str:
    """For testing purposes"""
    fake = Faker()
    email_array = []
    for _ in range(count):
        email_array.append(fake.email())

    email_list = ", ".join(email_array)

    return email_list


def generate_passphrase() -> str:
    """For testing purposes"""
    fake = Faker()
    return fake.password()


def get_server_item(serv: str, request_type: str) -> str:
    """request types should be: 'key_request' or 'value_request'"""
    for key, value in servers.items():
        if request_type == "key_request":
            if value == serv:
                return key
        elif request_type == "value_request":
            if key == serv:
                return value


class FormFrame(ttk.Frame):
    def __init__(self, container, **kwargs):

        super().__init__(container, **kwargs)

        self["style"] = "Background.TFrame"

        # -- Widgets --
        self.spacer_label = ttk.Label(self, text="", style="LightText.TLabel")
        self.to_label = ttk.Label(self, text="To: ", style="LightText.TLabel")
        self.to_entry = ttk.Entry(self, width=65, style="EntryBG.TEntry", )
        fake_emails = generate_fake_emails(4)
        self.to_entry.insert(0, fake_emails)

        self.cc_upload_label = ttk.Label(self, text="CC Upload: ", style="LightText.TLabel")
        self.cc_upload_entry = ttk.Entry(self, width=65, style="EntryBG.TEntry")
        fake_emails = generate_fake_emails(2)
        self.cc_upload_entry.insert(0, fake_emails)

        self.cc_download_label = ttk.Label(self, text="CC Download: ", style="LightText.TLabel")
        self.cc_download_entry = ttk.Entry(self, width=65, style="EntryBG.TEntry")
        fake_emails = generate_fake_emails(1)
        self.cc_download_entry.insert(0, fake_emails)

        self.faspex_label = ttk.Label(self, text="Faspex Server: ", style="LightText.TLabel")
        self.server_values = ["", "CO3 Faspex", "Disney Faspex"]
        self.faspex_combobox = ttk.Combobox(self, values=self.server_values, width=30, style="combobox_style.TCombobox")
        self.faspex_combobox.current(0)

        self.passphrase_label = ttk.Label(self, text="Passphrase: ", style="LightText.TLabel")
        self.passphrase_entry = ttk.Entry(self, width=20, style="EntryBG.TEntry")
        passphrase_placeholder = generate_passphrase()
        self.passphrase_entry.insert(0, passphrase_placeholder)

        self.file_types_label = ttk.Label(self, text="File Types: ", style="LightText.TLabel")
        self.file_types_entry = ttk.Entry(self, width=65, style="EntryBG.TEntry")
        self.file_types_entry.insert(0, "ALE,MXF,PDF,WAV")

        button_container = ttk.Frame(self, padding=10, style="Background.TFrame")

        self.load_button = ttk.Button(
            button_container,
            text="LOAD",
            style="AppButton.TButton",
            command=lambda: self.load_file()
        )

        self.save_json_button = ttk.Button(
            button_container,
            text="SAVE JSON",
            style="AppButton.TButton",
            command=lambda: self.save_file("json")
        )

        self.save_txt_button = ttk.Button(
            button_container,
            text="SAVE TEXT",
            style="AppButton.TButton",
            command=lambda: self.save_file("text")
        )

        # -- Layout --
        self.spacer_label.grid(column=0, row=0, columnspan=4)
        self.to_label.grid(column=0, row=1, sticky="E")
        self.to_entry.grid(column=1, row=1, columnspan=3, sticky="W")

        self.cc_upload_label.grid(column=0, row=2, sticky="E")
        self.cc_upload_entry.grid(column=1, row=2, columnspan=3, sticky="W")

        self.cc_download_label.grid(column=0, row=3, sticky="E")
        self.cc_download_entry.grid(column=1, row=3, columnspan=3, sticky="W")

        self.faspex_label.grid(column=0, row=4, padx=(5, 0), sticky="E")
        self.faspex_combobox.grid(column=1, row=4, sticky="W")

        self.passphrase_label.grid(column=2, row=4, sticky="E")
        self.passphrase_entry.grid(column=3, row=4, sticky="W")

        self.file_types_label.grid(column=0, row=5, sticky="E")
        self.file_types_entry.grid(column=1, row=5, columnspan=3, sticky="W")

        button_container.grid(columnspa=4, sticky="E")
        self.load_button.grid(column=0, row=0)
        self.save_json_button.grid(column=1, row=0, padx=15)
        self.save_txt_button.grid(column=2, row=0, sticky="E")

        # show the frame on the container
        self.grid(column=0, row=1, ipady=5, ipadx=3)

        for child in self.winfo_children():
            child.grid_configure(pady=6)

    def load_file(self):
        filetypes = (
            ('text files', '*.txt'),
            ('JSON files', '*.json'),
            ('All files', '*.*')
        )
        file = fd.askopenfilename(filetypes=filetypes, title="LOAD FILE")

        with open(file, "r") as data_file:
            contents = data_file.read()

        contents_dict = ast.literal_eval(contents)

        self.to_entry.delete(0, "end")
        self.to_entry.insert(0, contents_dict["to"])

        self.cc_upload_entry.delete(0, "end")
        self.cc_upload_entry.insert(0, contents_dict["cc_upload"])

        self.cc_download_entry.delete(0, "end")
        self.cc_download_entry.insert(0, contents_dict["cc_download"])

        server_loaded = get_server_item(contents_dict["url"], "key_request")
        self.faspex_combobox.set(server_loaded)

        self.passphrase_entry.delete(0, "end")
        self.passphrase_entry.insert(0, contents_dict["pass"])

        self.file_types_entry.delete(0, "end")
        file_types_str = ",".join(contents_dict["fileTypes"])
        self.file_types_entry.insert(0, file_types_str)

    def save_file(self, save_type):
        to_value = self.to_entry.get()
        cc_upload_value = self.cc_upload_entry.get()
        cc_download_value = self.cc_download_entry.get()
        faspex_combobox_value = self.faspex_combobox.get()
        faspex_url = get_server_item(faspex_combobox_value, "value_request")
        passphrase_value = self.passphrase_entry.get()
        file_types_value = self.file_types_entry.get()
        file_types_array = file_types_value.split(",")

        if to_value == "" or faspex_combobox_value == "" or passphrase_value == "":
            tk.messagebox.showinfo(
                title="oops",
                message="Please make sure the following fields are filled in:\n\nTo:\nFaspex Server:\nPassphrase:\n"
            )
        else:
            # store .get() values into a dictionary
            data_values_dict = {
                "to": to_value,
                "cc_upload": cc_upload_value,
                "cc_download": cc_download_value,
                "url": faspex_url,
                "pass": passphrase_value,
                "fileTypes": file_types_array
            }

            # dictionary converted to json then stored as string on variable assignment
            data_values_str = json.dumps(data_values_dict)
            if save_type == "text":
                file = fd.asksaveasfile(
                    title="Select Location",
                    defaultextension=".txt",
                    initialfile="sample.txt",
                    filetypes=[("Text Files", "*.txt")]
                )
                file.write(data_values_str)

            elif save_type == "json":
                file = fd.asksaveasfile(
                    title="Select Location",
                    defaultextension=".json",
                    initialfile="editorial.txt",
                    filetypes=[("JSON Files", "*.json")]
                )
                path_to_file = file.name
                with open(path_to_file, 'w') as data_file:
                    json.dump(data_values_dict, data_file, indent=4)

            self.to_entry.delete(0, 'end')
            self.cc_upload_entry.delete(0, 'end')
            self.cc_download_entry.delete(0, 'end')
            self.faspex_combobox.delete(0, 'end')
            self.passphrase_entry.delete(0, 'end')
            self.file_types_entry.delete(0, 'end')
