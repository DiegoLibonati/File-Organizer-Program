import os 

from tkinter import messagebox
from shutil import move, rmtree

class FileOrganizer:
    def __init__(
        self, path: str = "", files: list = [], 
        extensions: list = [], extensions_allowed: list = [], filters: dict = {}
    ):
        self.path = path
        self.files = files
        self.extensions = extensions
        self.extensions_allowed = extensions_allowed
        self.filters = filters


    def print_path(
        self
    ) -> None:
        try:
            print(f"The chosen path is: {self.path}")
        except:
            print("No path entered")
    

    def get_path(
        self
    ) -> None:
        try:
            self.path = input("Ingrese un path a ordenar: ")
        except:
            print("An error occurred when entering a path")
    

    def initial_state_reset(
        self
    ) -> None:
        self.path = ""
        self.files = []
        self.extensions = []
        self.extensions_allowed = []


    def get_all_files_from_path(
        self
    ) -> None:
        try:
            files_in_path = os.listdir(self.path)

            if self.filters:
                byte = 1024 * 1024
                filter_min_size = self.filters["min_size"] * byte
                filter_max_size = self.filters["max_size"] * byte

                for file in files_in_path:
                    file_is_file = os.path.isfile(f"{self.path}/{file}")
                    file_size = os.stat(f'{self.path}/{file}').st_size

                    if file_is_file and file_size >= filter_min_size and file_size <= filter_max_size:
                        self.files.append(file)
                return

            self.files = [file for file in files_in_path if os.path.isfile(f"{self.path}/{file}")]
            return
        except:
            print(f"Path not found: {self.path}")


    def get_specific_files_from_path(
        self
    ) -> None:
        try:
            files_in_path = os.listdir(self.path)
            
            if self.filters:
                byte = 1024 * 1024
                filter_min_size = self.filters["min_size"] * byte
                filter_max_size = self.filters["max_size"] * byte
                
                for file in files_in_path:
                    file_is_file = os.path.isfile(f"{self.path}/{file}")
                    file_extension = file.rsplit(".", 1).pop()
                    file_size = os.stat(f'{self.path}/{file}').st_size

                    if file_is_file and file_extension in self.extensions_allowed and file_size >= filter_min_size and file_size <= filter_max_size:
                        self.files.append(file)
                return

            self.files = [file for file in files_in_path if os.path.isfile(f"{self.path}/{file}") and file.rsplit(".", 1).pop() in self.extensions_allowed]
            return
        except:
            print(f"Path not found: {self.path}")
            return
        

    def get_all_extensions_from_path(
        self
    ) -> None:

        if self.files:
            for file in self.files:
                extension = file.rsplit(".", 1).pop()

                if extension not in self.extensions:
                    self.extensions.append(extension)
            return
        
        print(f"There are no files to move in {self.path}")
        return    


    def create_extension_folders(
        self
    ) -> None:
        if self.extensions and self.path:
            for extension in self.extensions:
                folder_name = f"{extension.upper()}_ORGANIZER"

                if not os.path.exists(f"{self.path}/{folder_name}"):
                    directory = os.path.join(self.path, folder_name)
                    os.mkdir(directory)
                    print(f"Directory {folder_name} created")
                else:
                    print(f"The directory: {folder_name} was not created because it already exists.")
            return
        
        print("No extensions or correct path found")
        return


    def move_files_to_their_directory(
        self
    ) -> None:
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
        return 


    def revert_organizer(
        self
    ) -> None:
        try:
            folder_names = [name for name in os.listdir(self.path) if os.path.isdir(f"{self.path}/{name}") and "_ORGANIZER" in name]
            if folder_names:
                for extension in folder_names:
                    directory = f"{self.path}/{extension}"
                    directory_files = os.listdir(directory)
                    
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
            return