from tkinter import Tk
from tkinter import Entry
from tkinter import Button
from tkinter import Label
from tkinter import LabelFrame
from tkinter import Checkbutton
from tkinter import StringVar
from tkinter import BooleanVar
from tkinter import IntVar
from tkinter import filedialog
from tkinter import messagebox

from src.models.FileOrganizer import FileOrganizer
from src.utils.constants import BACKGROUND_COLOR
from src.utils.constants import PRIMARY_COLOR
from src.utils.constants import WHITE_COLOR
from src.utils.constants import BLACK_COLOR
from src.utils.constants import ARIAL_BOLD_FONT_10
from src.utils.constants import STATE_NORMAL
from src.utils.constants import STATE_DISABLED
from src.utils.constants import RELIEF_FLAT
from src.utils.constants import CURSOR_HAND2
from src.utils.constants import ANCHOR_W

class InterfaceApp:
    def __init__(self, root: Tk, bg_color: str = BACKGROUND_COLOR) -> None:
        self._root = root
        self._root.title("File Organizer V1.0.0")
        self._root.geometry('400x600')
        self._root.resizable(False, False)
        self._root.config(bg=bg_color)

        self._file_organizer: FileOrganizer = None

        self._create_widgets()

    @property
    def file_organizer(self) -> FileOrganizer:
        return self._file_organizer
    
    @file_organizer.setter
    def file_organizer(self, value: FileOrganizer) -> None:
        self._file_organizer = value
        
    def _create_widgets(self) -> None:
        # Search Vars
        self._text_path = StringVar(None, value="Wait for directory...")

        # Extensions Vars
        self._check_value_all = BooleanVar(value=True)
        self._check_value_mp4 = BooleanVar(value=True)
        self._check_value_pdf = BooleanVar(value=True)
        self._check_value_exe = BooleanVar(value=True)
        self._check_value_jpg = BooleanVar(value=True)
        self._check_value_jpeg = BooleanVar(value=True)
        self._check_value_png = BooleanVar(value=True)
        self._check_value_txt = BooleanVar(value=True)
        self._check_value_json = BooleanVar(value=True)
        self._check_value_mp3 = BooleanVar(value=True)
        self._check_value_m3u8 = BooleanVar(value=True)
        self._check_value_zip = BooleanVar(value=True)
        self._check_value_gif = BooleanVar(value=True)

        self._extensions_options = {
            "mp4":self._check_value_mp4, 
            "pdf":self._check_value_pdf, 
            "exe":self._check_value_exe,
            "png":self._check_value_png, 
            "jpg":self._check_value_jpg, 
            "jpeg":self._check_value_jpeg,
            "txt": self._check_value_txt,
            "json": self._check_value_json,
            "mp3": self._check_value_mp3,
            "m3u8": self._check_value_m3u8,
            "zip": self._check_value_zip,
            "gif": self._check_value_gif
        }

        # Filters Vars
        self._check_value_filters = BooleanVar(value=False)
        
        self._filter_min_size = IntVar(None, value=1)
        self._filter_max_size = IntVar(None, value=10)

        self._filters = {
            "min_size": self._filter_min_size,
            "max_size": self._filter_max_size
        }

        # Search
        self._entry_path = Entry(master=self._root, bg=WHITE_COLOR, fg=BLACK_COLOR, font=ARIAL_BOLD_FONT_10, textvariable=self._text_path, state=STATE_DISABLED)
        self._entry_path.place(x=50, y=25,  width=225, height=25)

        self._button_search = Button(master=self._root, text="Search", relief=RELIEF_FLAT, bg=PRIMARY_COLOR, fg=WHITE_COLOR, cursor=CURSOR_HAND2, command=lambda:self._set_path())
        self._button_search.place(x=300, y=25, width=50, height=25)

        # Buttons Actions
        self._button_organize = Button(master=self._root, text="ORGANIZE", relief=RELIEF_FLAT, bg=PRIMARY_COLOR, fg=WHITE_COLOR, cursor=CURSOR_HAND2, command=lambda:self._organize())
        self._button_organize.place(x=50, y=75, width=125, height=25)

        self._button_revert = Button(master=self._root, text="Revert ORGANIZE", relief=RELIEF_FLAT, bg=PRIMARY_COLOR, fg=WHITE_COLOR, cursor=CURSOR_HAND2, command=lambda:self._reverse_organize())
        self._button_revert.place(x=50, y=110, width=125, height=25)

        # Extensions
        self._label_frame_extensions = LabelFrame(master=self._root, text="Select extensions", padx=20, pady=20)
        self._label_frame_extensions.grid(row=1, column=0, pady=(150,0), padx=(50,0))

        self._check_button_all = Checkbutton(master=self._label_frame_extensions, text="ALL", variable=self._check_value_all, command=lambda:self._select_all_extensions(), width="5", anchor=ANCHOR_W)
        self._check_button_all.grid(padx=1, pady=5, row=0, column=0)

        self._check_button_mp4 = Checkbutton(master=self._label_frame_extensions, text="MP4", variable=self._check_value_mp4, command=lambda:self._select_extension(), width="5", anchor=ANCHOR_W)
        self._check_button_mp4.grid(padx=1, pady=5, row=1, column=0)

        self._check_button_pdf = Checkbutton(master=self._label_frame_extensions, text="PDF", variable=self._check_value_pdf, command=lambda:self._select_extension(), width="5", anchor=ANCHOR_W)
        self._check_button_pdf.grid(padx=1, pady=5, row=2, column=0)

        self._check_button_exe = Checkbutton(master=self._label_frame_extensions, text="EXE", variable=self._check_value_exe, command=lambda:self._select_extension(), width="5", anchor=ANCHOR_W)
        self._check_button_exe.grid(padx=1, pady=5, row=3, column=0)

        self._check_button_jpg = Checkbutton(master=self._label_frame_extensions, text="JPG", variable=self._check_value_jpg, command=lambda:self._select_extension(), width="5", anchor=ANCHOR_W)
        self._check_button_jpg.grid(padx=1, pady=5, row=4, column=0)

        self._check_button_jpeg = Checkbutton(master=self._label_frame_extensions, text="JPEG", variable=self._check_value_jpeg, command=lambda:self._select_extension(), width="5", anchor=ANCHOR_W)
        self._check_button_jpeg.grid(padx=1, pady=5, row=0, column=1)

        self._check_button_png = Checkbutton(master=self._label_frame_extensions, text="PNG", variable=self._check_value_png, command=lambda:self._select_extension(), width="5", anchor=ANCHOR_W)
        self._check_button_png.grid(padx=1, pady=5, row=1, column=1)

        self._check_button_txt = Checkbutton(master=self._label_frame_extensions, text="TXT", variable=self._check_value_txt, command=lambda:self._select_extension(), width="5", anchor=ANCHOR_W)
        self._check_button_txt.grid(padx=1, pady=5, row=2, column=1)

        self._check_button_json = Checkbutton(master=self._label_frame_extensions, text="JSON", variable=self._check_value_json, command=lambda:self._select_extension(), width="5", anchor=ANCHOR_W)
        self._check_button_json.grid(padx=1, pady=5, row=3, column=1)

        self._check_button_mp3 = Checkbutton(master=self._label_frame_extensions, text="MP3", variable=self._check_value_mp3, command=lambda:self._select_extension(), width="5", anchor=ANCHOR_W)
        self._check_button_mp3.grid(padx=1, pady=5, row=4, column=1)

        self._check_button_m3u8 = Checkbutton(master=self._label_frame_extensions, text="M3U8", variable=self._check_value_m3u8, command=lambda:self._select_extension(), width="5", anchor=ANCHOR_W)
        self._check_button_m3u8.grid(padx=1, pady=5, row=0, column=2)

        self._check_button_zip = Checkbutton(master=self._label_frame_extensions, text="ZIP", variable=self._check_value_zip, command=lambda:self._select_extension(), width="5", anchor=ANCHOR_W)
        self._check_button_zip.grid(padx=1, pady=5, row=1, column=2)

        self._check_button_gif = Checkbutton(master=self._label_frame_extensions, text="GIF", variable=self._check_value_gif, command=lambda:self._select_extension(), width="5", anchor=ANCHOR_W)
        self._check_button_gif.grid(padx=1, pady=5, row=2, column=2)

        # Filters
        self._label_frame_filters = LabelFrame(master=self._root, text="Select filters", padx=20, pady=20)
        self._label_frame_filters.grid(row=2, column=0, pady=(10,0), padx=(50,0))

        self._check_button_filter_by = Checkbutton(master=self._label_frame_filters, text="Filter by", variable=self._check_value_filters, command=lambda:self._handle_filters(), width="18", anchor=ANCHOR_W)
        self._check_button_filter_by.grid(padx=0, pady=5, row=0, column=0)

        self._label_min_size = Label(master=self._label_frame_filters, fg=BLACK_COLOR, font=ARIAL_BOLD_FONT_10, text="Min size in MB: ", width="15", anchor=ANCHOR_W)
        self._label_min_size.grid(padx=0, pady=0, row=1, column=0)

        self._entry_min_size = Entry(master=self._label_frame_filters, bg=WHITE_COLOR, font=ARIAL_BOLD_FONT_10, textvariable=self._filter_min_size, state=STATE_DISABLED, width="5")
        self._entry_min_size.grid(padx=0, pady=0, row=1, column=1)

        self._label_max_size = Label(master=self._label_frame_filters, fg=BLACK_COLOR, font=ARIAL_BOLD_FONT_10, text="Max size in MB: ", width="15", anchor=ANCHOR_W)
        self._label_max_size.grid(padx=0, pady=0, row=2, column=0)

        self._entry_max_size = Entry(master=self._label_frame_filters, bg=WHITE_COLOR, font=ARIAL_BOLD_FONT_10, textvariable=self._filter_max_size, state=STATE_DISABLED, width="5")
        self._entry_max_size.grid(padx=0, pady=0, row=2, column=1)

    def _set_path(self) -> None:
        path = filedialog.askdirectory(title="Choose a directory")

        self._text_path.set(path)
        self.file_organizer = FileOrganizer(path=path)

        messagebox.showinfo(message=f"Path loaded: {path} successfully.", title="File Organizer")

    def _organize(self) -> None:
        if not self.file_organizer:
            messagebox.showerror(message="You must enter a path in order to organize the folder.", title="File Organizer")
            return
        
        filters_enabled = self._check_value_filters.get()

        self.file_organizer.extensions_allowed = [extension for extension, value in self._extensions_options.items() if value.get()]

        if not self.file_organizer.extensions_allowed:
            messagebox.showerror(message="Select at least one extension to organize the path.", title="File Organizer")
            return

        self.file_organizer.filters = {
            "min_size": self._filters["min_size"].get(),
            "max_size": self._filters["max_size"].get()
        } if filters_enabled else {}

        message, status = self.file_organizer.organizer()

        if not status:
            messagebox.showerror(message=message, title="File Organizer")
            return

        messagebox.showinfo(message=message, title="File Organizer")

    def _reverse_organize(self) -> None:
        if not self.file_organizer:
            messagebox.showerror(message="You must enter a path in order to reverse organize the folder.", title="File Organizer")
            return

        message, status = self.file_organizer.revert_organizer()

        if not status:
            messagebox.showerror(message=message, title="File Organizer")
            return

        messagebox.showinfo(message=message, title="File Organizer")

    def _select_all_extensions(self) -> None:
        check_all = self._check_value_all.get()

        if check_all:
            for extension_option in self._extensions_options.values():
                extension_option.set(True)
            return

        for extension_option in self._extensions_options.values():
            extension_option.set(False)

    def _select_extension(self) -> None:
        self._check_value_all.set(False)

    def _handle_filters(self) -> None:
        filters_enabled = self._check_value_filters.get()

        if not filters_enabled:
            self._entry_min_size.config(state=STATE_DISABLED)
            self._entry_max_size.config(state=STATE_DISABLED)
            return
        
        self._entry_min_size.config(state=STATE_NORMAL)
        self._entry_max_size.config(state=STATE_NORMAL)