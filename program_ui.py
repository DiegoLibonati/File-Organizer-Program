from tkinter import *
from tkinter import filedialog, messagebox
from file_organizer import *

class FileOrganizerUI(FileOrganizer):
    def __init__(self, path: str = "", files: list = [] ,extensions: list = [], master: Tk = None):
        super().__init__(path, files, extensions)
        master.title("File Organizer V0.1.5")
        master.geometry("400x600")
        master.config(bg="#F3F3F3")
        master.resizable(False, False)

        self.pathname = StringVar(None, value="Wait for directory...")
        self.min_file_size = IntVar(None, value=1)
        self.max_file_size = IntVar(None, value=10)

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
        self.checkbox_value_filters = BooleanVar(value=False)

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

    def set_path(self):
        self.path = filedialog.askdirectory(title="Choose a directory")
        self.pathname.set(self.path)

    def organize(self):
        
        if self.checkbox_value_all.get():
            if self.checkbox_value_filters.get():
                self.filters = {
                    "min_size": self.min_file_size.get(),
                    "max_size": self.max_file_size.get() 
                }

            self.get_all_files_from_path()
            self.get_all_extensions_from_path()
            self.create_extension_folders()
            self.move_files_to_their_directory()
    
        else:
            if self.checkbox_value_filters.get():
                self.filters = {
                    "min_size": self.min_file_size.get(),
                    "max_size": self.max_file_size.get() 
                }

            self.extensions_allowed = [extension for extension, value in self.options.items() if value.get()]

            self.get_specific_files_from_path()
            self.get_all_extensions_from_path()
            self.create_extension_folders()
            self.move_files_to_their_directory()

        self.pathname.set("Wait for directory...")
        self.initial_state_reset()

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
        self.revert_organizer()

        self.pathname.set("Wait for directory...")
        self.initial_state_reset()

    def enable_filters(self, filters):

        for filter in filters:
            if filter["state"] == DISABLED:
                filter.config(state=NORMAL)
                continue
            
            filter.config(state=DISABLED)
            
            if self.filters:
                self.filters = {}
            continue

root = Tk()
file_organizer_ui = FileOrganizerUI(master = root)

Entry(root,bg="#fff", fg="#000", font=("Arial Bold", 10), textvariable=file_organizer_ui.pathname, state=DISABLED).place(x=50, y=25,  width=225, height=25)
Button(root,text="Search", relief="flat", bg="#250001", fg="#fff", cursor="hand2", command=lambda:file_organizer_ui.set_path()).place(x=300, y=25, width=50, height=25)

Button(root,text="ORGANIZE", relief="flat", bg="#250001", fg="#fff", cursor="hand2", command=lambda:file_organizer_ui.organize()).place(x=50, y=75, width=125, height=25)
Button(root,text="Revert ORGANIZE", relief="flat", bg="#250001", fg="#fff", cursor="hand2", command=lambda:file_organizer_ui.reverse_organize()).place(x=50, y=110, width=125, height=25)

frame_extensions = LabelFrame(root, text="Select extensions",padx=20, pady=20)
frame_extensions.grid(row=1, column=0, pady=(150,0), padx=(50,0))
Checkbutton(frame_extensions, text="ALL", variable=file_organizer_ui.checkbox_value_all, command=lambda:file_organizer_ui.set_all_values_to_true(), width="5", anchor="w").grid(padx=1, pady=5, row=0, column=0)
Checkbutton(frame_extensions, text="MP4", variable=file_organizer_ui.checkbox_value_mp4, command=lambda:file_organizer_ui.set_all_to_false(), width="5", anchor="w").grid(padx=1, pady=5, row=1, column=0)
Checkbutton(frame_extensions, text="PDF", variable=file_organizer_ui.checkbox_value_pdf, command=lambda:file_organizer_ui.set_all_to_false(), width="5", anchor="w").grid(padx=1, pady=5, row=2, column=0)
Checkbutton(frame_extensions, text="EXE", variable=file_organizer_ui.checkbox_value_exe, command=lambda:file_organizer_ui.set_all_to_false(), width="5", anchor="w").grid(padx=1, pady=5, row=3, column=0)
Checkbutton(frame_extensions, text="JPG", variable=file_organizer_ui.checkbox_value_jpg, command=lambda:file_organizer_ui.set_all_to_false(), width="5", anchor="w").grid(padx=1, pady=5, row=4, column=0)

Checkbutton(frame_extensions, text="JPEG", variable=file_organizer_ui.checkbox_value_jpeg, command=lambda:file_organizer_ui.set_all_to_false(), width="5", anchor="w").grid(padx=1, pady=5, row=0, column=1)
Checkbutton(frame_extensions, text="PNG", variable=file_organizer_ui.checkbox_value_png, command=lambda:file_organizer_ui.set_all_to_false(), width="5", anchor="w").grid(padx=1, pady=5, row=1, column=1)
Checkbutton(frame_extensions, text="TXT", variable=file_organizer_ui.checkbox_value_txt, command=lambda:file_organizer_ui.set_all_to_false(), width="5", anchor="w").grid(padx=1, pady=5, row=2, column=1)
Checkbutton(frame_extensions, text="JSON", variable=file_organizer_ui.checkbox_value_json, command=lambda:file_organizer_ui.set_all_to_false(), width="5", anchor="w").grid(padx=1, pady=5, row=3, column=1)
Checkbutton(frame_extensions, text="MP3", variable=file_organizer_ui.checkbox_value_mp3, command=lambda:file_organizer_ui.set_all_to_false(), width="5", anchor="w").grid(padx=1, pady=5, row=4, column=1)

Checkbutton(frame_extensions, text="M3U8", variable=file_organizer_ui.checkbox_value_m3u8, command=lambda:file_organizer_ui.set_all_to_false(), width="5", anchor="w").grid(padx=1, pady=5, row=0, column=2)
Checkbutton(frame_extensions, text="ZIP", variable=file_organizer_ui.checkbox_value_zip, command=lambda:file_organizer_ui.set_all_to_false(), width="5", anchor="w").grid(padx=1, pady=5, row=1, column=2)
Checkbutton(frame_extensions, text="GIF", variable=file_organizer_ui.checkbox_value_gif, command=lambda:file_organizer_ui.set_all_to_false(), width="5", anchor="w").grid(padx=1, pady=5, row=2, column=2)

frame_filters = LabelFrame(root, text="Select filters",padx=20, pady=20)
frame_filters.grid(row=2, column=0, pady=(10,0), padx=(50,0))

Checkbutton(frame_filters, text="Filter by", variable=file_organizer_ui.checkbox_value_filters, command=lambda:file_organizer_ui.enable_filters(filters), width="18", anchor="w").grid(padx=0, pady=5, row=0, column=0)

Label(frame_filters, fg="#000", font=("Arial Bold", 10), text="Min size in MB: ", width="15", anchor="w").grid(padx=0, pady=0, row=1, column=0)
file_organizer_ui.entry_min_file_size = Entry(frame_filters, bg="#fff", font=("Arial Bold", 10), textvariable=file_organizer_ui.min_file_size, state=DISABLED, width="5")
file_organizer_ui.entry_min_file_size.grid(padx=0, pady=0, row=1, column=1)

Label(frame_filters, fg="#000", font=("Arial Bold", 10), text="Max size in MB: ", width="15", anchor="w").grid(padx=0, pady=0, row=2, column=0)
file_organizer_ui.entry_max_file_size = Entry(frame_filters, bg="#fff", font=("Arial Bold", 10), textvariable=file_organizer_ui.max_file_size, state=DISABLED, width="5")
file_organizer_ui.entry_max_file_size.grid(padx=0, pady=0, row=2, column=1)

filters = [file_organizer_ui.entry_min_file_size, file_organizer_ui.entry_max_file_size]
root.mainloop()

