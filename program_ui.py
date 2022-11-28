from tkinter import *
from tkinter import filedialog
from file_organizer import *

class FileOrganizerUI(FileOrganizer):
    def __init__(self, path: str = "", files: list = [] ,extensions: list = [], master: Tk = None):
        super().__init__(path, files, extensions)
        master.title("File Organizer V0.0.2")
        master.geometry("400x400")
        master.config(bg="black")
        master.resizable(False, False)

        self.pathname = StringVar(None, value="Wait for directory...")
        self.checkbox_value_all = BooleanVar(value=True)
        self.checkbox_value_mp4 = BooleanVar(value=True)
        self.checkbox_value_pdf = BooleanVar(value=True)
        self.checkbox_value_exe = BooleanVar(value=True)

        self.options = {"mp4":self.checkbox_value_mp4, "pdf":self.checkbox_value_pdf, "exe":self.checkbox_value_exe}

        Entry(bg="#fff", font=("Arial Bold", 10), textvariable=self.pathname, state=DISABLED).place(x=50, y=25,  width=225, height=25)
        Button(text="Search", relief="flat", bg="white", cursor="hand2", command=lambda:self.set_path()).place(x=300, y=25, width=50, height=25)

        Button(text="ORGANIZE", relief="flat", bg="white", cursor="hand2", command=lambda:self.organize()).place(x=50, y=75, width=125, height=25)
        Button(text="Revert ORGANIZE", relief="flat", bg="white", cursor="hand2", command=lambda:self.reverse_organize()).place(x=50, y=110, width=125, height=25)

        Checkbutton(text="ALL", variable=self.checkbox_value_all, command=lambda:self.set_all_values_to_true()).place(x=50, y=200, width=50, height=25)
        Checkbutton(text="MP4", variable=self.checkbox_value_mp4, command=lambda:self.set_all_to_false()).place(x=50, y=230, width=50, height=25)
        Checkbutton(text="PDF", variable=self.checkbox_value_pdf, command=lambda:self.set_all_to_false()).place(x=50, y=260, width=50, height=25)
        Checkbutton(text="EXE", variable=self.checkbox_value_exe, command=lambda:self.set_all_to_false()).place(x=50, y=290, width=50, height=25)

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
            self.checkbox_value_mp4.set(True)
            self.checkbox_value_pdf.set(True)
            self.checkbox_value_exe.set(True)
        else:
            self.checkbox_value_mp4.set(False)
            self.checkbox_value_pdf.set(False)
            self.checkbox_value_exe.set(False)

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

