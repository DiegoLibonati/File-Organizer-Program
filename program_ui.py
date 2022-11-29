from tkinter import *
from tkinter import filedialog
from file_organizer import *

class FileOrganizerUI(FileOrganizer):
    def __init__(self, path: str = "", files: list = [] ,extensions: list = [], master: Tk = None):
        super().__init__(path, files, extensions)
        master.title("File Organizer V0.0.3")
        master.geometry("400x400")
        master.config(bg="black")
        master.resizable(False, False)

        self.pathname = StringVar(None, value="Wait for directory...")
        self.checkbox_value_all = BooleanVar(value=True)
        self.checkbox_value_mp4 = BooleanVar(value=True)
        self.checkbox_value_pdf = BooleanVar(value=True)
        self.checkbox_value_exe = BooleanVar(value=True)
        self.checkbox_value_jpg = BooleanVar(value=True)
        self.checkbox_value_jpeg = BooleanVar(value=True)
        self.checkbox_value_png = BooleanVar(value=True)
        self.checkbox_value_txt = BooleanVar(value=True)
        self.checkbox_value_json = BooleanVar(value=True)
        self.checkbox_value_mp3 = BooleanVar(value=True)
        self.checkbox_value_m3u8 = BooleanVar(value=True)
        self.checkbox_value_zip = BooleanVar(value=True)
        self.checkbox_value_gif = BooleanVar(value=True)

        self.options = {"mp4":self.checkbox_value_mp4, 
                        "pdf":self.checkbox_value_pdf, 
                        "exe":self.checkbox_value_exe,
                        "png":self.checkbox_value_png, 
                        "jpg":self.checkbox_value_jpg, 
                        "jpeg":self.checkbox_value_jpeg,
                        "txt": self.checkbox_value_txt,
                        "json": self.checkbox_value_json,
                        "mp3": self.checkbox_value_mp3,
                        "m3u8": self.checkbox_value_m3u8,
                        "zip": self.checkbox_value_zip,
                        "gif": self.checkbox_value_gif}

        Entry(bg="#fff", font=("Arial Bold", 10), textvariable=self.pathname, state=DISABLED).place(x=50, y=25,  width=225, height=25)
        Button(text="Search", relief="flat", bg="white", cursor="hand2", command=lambda:self.set_path()).place(x=300, y=25, width=50, height=25)

        Button(text="ORGANIZE", relief="flat", bg="white", cursor="hand2", command=lambda:self.organize()).place(x=50, y=75, width=125, height=25)
        Button(text="Revert ORGANIZE", relief="flat", bg="white", cursor="hand2", command=lambda:self.reverse_organize()).place(x=50, y=110, width=125, height=25)

        Checkbutton(text="ALL", variable=self.checkbox_value_all, command=lambda:self.set_all_values_to_true()).place(x=50, y=200, width=55, height=25)
        Checkbutton(text="MP4", variable=self.checkbox_value_mp4, command=lambda:self.set_all_to_false()).place(x=50, y=230, width=55, height=25)
        Checkbutton(text="PDF", variable=self.checkbox_value_pdf, command=lambda:self.set_all_to_false()).place(x=50, y=260, width=55, height=25)
        Checkbutton(text="EXE", variable=self.checkbox_value_exe, command=lambda:self.set_all_to_false()).place(x=50, y=290, width=55, height=25)
        Checkbutton(text="JPG", variable=self.checkbox_value_jpg, command=lambda:self.set_all_to_false()).place(x=50, y=320, width=55, height=25)
        Checkbutton(text="JPEG", variable=self.checkbox_value_jpeg, command=lambda:self.set_all_to_false()).place(x=50, y=350, width=55, height=25)

        Checkbutton(text="PNG", variable=self.checkbox_value_png, command=lambda:self.set_all_to_false()).place(x=110, y=200, width=55, height=25)
        Checkbutton(text="TXT", variable=self.checkbox_value_txt, command=lambda:self.set_all_to_false()).place(x=110, y=230, width=55, height=25)
        Checkbutton(text="JSON", variable=self.checkbox_value_json, command=lambda:self.set_all_to_false()).place(x=110, y=260, width=55, height=25)
        Checkbutton(text="MP3", variable=self.checkbox_value_mp3, command=lambda:self.set_all_to_false()).place(x=110, y=290, width=55, height=25)
        Checkbutton(text="M3U8", variable=self.checkbox_value_m3u8, command=lambda:self.set_all_to_false()).place(x=110, y=320, width=55, height=25)
        Checkbutton(text="ZIP", variable=self.checkbox_value_zip, command=lambda:self.set_all_to_false()).place(x=110, y=350, width=55, height=25)

        Checkbutton(text="GIF", variable=self.checkbox_value_gif, command=lambda:self.set_all_to_false()).place(x=170, y=200, width=55, height=25)

    def set_path(self):
        self.path = filedialog.askdirectory(title="Choose a directory")
        self.pathname.set(self.path)

    def organize(self):
        
        if self.checkbox_value_all.get():
            self.get_all_files_from_path()
            self.get_all_extensions_from_path()
            self.create_extension_folders()
            self.move_files_to_their_directory()
        else:
            self.extensions_allowed = [extension for extension, value in self.options.items() if value.get()]

            self.get_specific_files_from_path()
            self.get_all_extensions_from_path()
            self.create_extension_folders()
            self.move_files_to_their_directory()

        self.path = ""
        self.pathname.set("Wait for directory...")
        self.files = []
        self.extensions = []

    def set_all_values_to_true(self):
        if self.checkbox_value_all.get():
            for option in self.options.values():
                option.set(True)
        else:
            for option in self.options.values():
                option.set(False)

    def set_all_to_false(self):
        self.checkbox_value_all.set(False)

    def reverse_organize(self):
        self.go_back()

        self.path = ""
        self.pathname.set("Wait for directory...")
        self.files = []
        self.extensions = []

root = Tk()
file_organizer_ui = FileOrganizerUI(master = root)
root.mainloop()

