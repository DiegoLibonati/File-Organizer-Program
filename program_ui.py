from tkinter import *
from tkinter import filedialog
from file_organizer import *

class FileOrganizerUI(FileOrganizer):
    def __init__(self, path: str = "", files: list = [] ,extensions: list = [], master: Tk = None):
        super().__init__(path, files, extensions)
        master.title("File Organizer V0.1")
        master.geometry("400x400")
        master.config(bg="black")
        master.resizable(False, False)

        self.pathname = StringVar(None, value="Wait for directory...")

        Entry(bg="#fff", font=("Arial Bold", 10), textvariable=self.pathname, state=DISABLED).place(x=50, y=25,  width=225, height=25)
        Button(text="Search", relief="flat", bg="white", cursor="hand2", command=lambda:self.set_path()).place(x=300, y=25, width=50, height=25)

        Button(text="ORGANIZE", relief="flat", bg="white", cursor="hand2", command=lambda:self.organize()).place(x=50, y=75, width=125, height=25)
        Button(text="Revert ORGANIZE", relief="flat", bg="white", cursor="hand2", command=lambda:self.go_back()).place(x=50, y=110, width=125, height=25)

    def set_path(self):
        self.path = filedialog.askdirectory(title="Choose a directory")
        self.pathname.set(self.path)

    def organize(self):
        self.get_all_files_from_path()
        self.get_all_extensions_from_path()
        self.create_extension_folders()
        self.move_files_to_their_directory()

        self.path = ""
        self.pathname.set("Wait for directory...")
        self.files = []
        self.extensions = []

root = Tk()
file_organizer_ui = FileOrganizerUI(master = root)
root.mainloop()

