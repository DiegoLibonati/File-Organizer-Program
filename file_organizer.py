from tkinter import messagebox
from os import listdir, mkdir, stat
from os.path import join, isdir, isfile, exists
from shutil import move, rmtree

class FileOrganizer():

    def __init__(self, path: str = "", files: list = [], extensions: list = [], extensions_allowed: list = [], filters: dict = {}):
        self.path = path
        self.files = files
        self.extensions = extensions
        self.extensions_allowed = extensions_allowed
        self.filters = filters

    def print_path(self):
        
        try:
            print(f"The chosen path is: {self.path}")
        except:
            print("No path entered")
            return False
    
    def get_path(self):

        try:
            self.path = input("Ingrese un path a ordenar: ")
        except:
            print("An error occurred when entering a path")
            return False
    
    def initial_state_reset(self):
            self.path = ""
            self.files = []
            self.extensions = []
            self.extensions_allowed = []

    def get_all_files_from_path(self):
        try:
            files_in_path = listdir(self.path)

            if self.filters:
                byte = 1024 * 1024
                filter_min_size = self.filters["min_size"] * byte
                filter_max_size = self.filters["max_size"] * byte

                for file in files_in_path:
                    file_is_file = isfile(f"{self.path}/{file}")
                    file_size = stat(f'{self.path}/{file}').st_size

                    if file_is_file and file_size >= filter_min_size and file_size <= filter_max_size:
                        self.files.append(file)
                return

            self.files = [file for file in files_in_path if isfile(f"{self.path}/{file}")]
            return
        except:
            print(f"Path not found: {self.path}")
            return False

    def get_specific_files_from_path(self):
        try:
            files_in_path = listdir(self.path)
            
            if self.filters:
                byte = 1024 * 1024
                filter_min_size = self.filters["min_size"] * byte
                filter_max_size = self.filters["max_size"] * byte
                
                for file in files_in_path:
                    file_is_file = isfile(f"{self.path}/{file}")
                    file_extension = file.rsplit(".", 1).pop()
                    file_size = stat(f'{self.path}/{file}').st_size

                    if file_is_file and file_extension in self.extensions_allowed and file_size >= filter_min_size and file_size <= filter_max_size:
                        self.files.append(file)
                return

            self.files = [file for file in files_in_path if isfile(f"{self.path}/{file}") and file.rsplit(".", 1).pop() in self.extensions_allowed]
            return
        except:
            print(f"Path not found: {self.path}")
            return False
        
    def get_all_extensions_from_path(self):

        if self.files:
            for file in self.files:
                extension = file.rsplit(".", 1).pop()

                if extension not in self.extensions:
                    self.extensions.append(extension)
            return
        
        print(f"There are no files to move in {self.path}")
        return False    

    def create_extension_folders(self):
        if self.extensions and self.path:
            for extension in self.extensions:
                folder_name = f"{extension.upper()}_ORGANIZER"

                if not exists(f"{self.path}/{folder_name}"):
                    directory = join(self.path, folder_name)
                    mkdir(directory)
                    print(f"Directory {folder_name} created")
                else:
                    print(f"The directory: {folder_name} was not created because it already exists.")
            return
        
        print("No extensions or correct path found")
        return False

    def move_files_to_their_directory(self):
        if self.files:
            for file in self.files:
                extension = file.rsplit(".", 1).pop().upper()
                last_path = f"{self.path}/{file}"
                new_path = f"{self.path}/{extension}_ORGANIZER/{file}"

                move(last_path, new_path)

                print(f"{file} moved to {new_path}")
            messagebox.showinfo(message="Successfully organized", title="File Organizer")
            return

        print(f"There are no files to move in this path")
        return False 

    def revert_organizer(self):
        try:
            folder_names = [name for name in listdir(self.path) if isdir(f"{self.path}/{name}") and "_ORGANIZER" in name]
            if folder_names:
                for extension in folder_names:
                    directory = f"{self.path}/{extension}"
                    directory_files = listdir(directory)
                    
                    if directory_files:
                        for file in directory_files:
                            last_path = f"{self.path}/{extension}/{file}"
                            new_path = f"{self.path}/{file}"

                            move(last_path, new_path)

                            print(f"{file} moved to {new_path}")

                    rmtree(directory)
                messagebox.showinfo(message="Successfully reverted", title="File Organizer")
            self.initial_state_reset()
        except:
            print("An error occurred while trying to revert ORGANIZER.")
            return False