from os import listdir, mkdir
from os.path import join, isdir, isfile, exists
from shutil import move, rmtree

class FileOrganizer():

    def __init__(self, path: str = "", files: list = [], extensions: list = [], extensions_allowed: list = []):
        self.path = path
        self.files = files
        self.extensions = extensions
        self.extensions_allowed = extensions_allowed

    def print_path(self):
        
        if self.path:
            print(self.path)
    
    def get_path(self):

        if not self.path:
            self.path = input("Ingrese un path a ordenar: ")

    def get_all_files_from_path(self):
        
        try:
            self.files = [file for file in listdir(self.path) if isfile(f"{self.path}/{file}")]
        except:
            print(f"No se encontro el path: {self.path}")
            return False

    def get_specific_files_from_path(self):
        try:
            self.files = [file for file in listdir(self.path) if isfile(f"{self.path}/{file}") and file.rsplit(".", 1).pop() in self.extensions_allowed]
        except:
            print(f"No se encontro el path: {self.path}")
            return False
        
    def get_all_extensions_from_path(self):

        if self.files:
            for file in self.files:
                extension = file.rsplit(".", 1).pop()

                if extension not in self.extensions:
                    self.extensions.append(extension)
        else:
            print(f"No hay archivos para mover en {self.path}")
            

    def create_extension_folders(self):
        if self.extensions and self.path:
            for extension in self.extensions:
                extension = f"{extension.upper()}_ORGANIZER"

                if not exists(f"{self.path}/{extension}"):
                    directory = join(self.path, extension)
                    mkdir(directory)
                    print(f"Directory {extension} created")
                else:
                    print(f"No se creo el directory: {extension} porque ya existe")

    def move_files_to_their_directory(self):
        if self.files:
            for file in self.files:
                extension = file.rsplit(".", 1).pop().upper()
                last_path = f"{self.path}/{file}"
                new_path = f"{self.path}/{extension}_ORGANIZER/{file}"

                move(last_path, new_path)

                print(f"{file} moved to {new_path}")

        self.success = True

    def go_back(self):
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
            
            self.path = ""
            self.files = []
            self.extensions = []
        except:
            print("Ocurrio un error al intentar revertir ORGANIZER.")
            return False

                


# test = FileOrganizer()

# test.print_path()

# test.get_path()

# test.get_all_files_from_path()

# test.get_all_extensions_from_path()

# test.create_extension_folders()

# test.move_files_to_their_directory()

#test.go_back()