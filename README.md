# File Organizer Program

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Use `python ./src/app.py` to execute script

## Description

I made a program that allows to sort the files in a specific path. It will get all the file extensions and create a folder for each extension in that path. Then it will add to each folder the file that corresponds to it. Basically it sorts files depending on the extension. In addition we will be able to choose which extensions to sort or all of them. Filters can also be applied, being able to sort files with a specific size. Finally, if we want to go back we can also do it by clicking on the `Revert ORGANIZE` button, thus returning to the initial state of the path.

## Technologies used

1. Python

## Libraries used

1. tkinter
2. os
3. shutil

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/File-Organizer-Program`](https://www.diegolibonati.com.ar/#/project/File-Organizer-Program)

## Video

https://user-images.githubusercontent.com/99032604/205468137-440a09af-4de6-4179-9cf7-5462b2ae414c.mp4

## Documentation

### file_organizer.py

The available attributes are as follows in the sorted list. `path` will store the path, `files` will store the files to move, `extensions` will store the extensions available on that `path`, `extensions_allowed` will store the extensions allowed if any particular extension was chosen and not all of them and `filters` refers to the filters to apply when sorting.

1. path
2. files
3. extensions
4. extensions_allowed
5. filters

The `print_path()` method is in charge of printing the path chosen by console.

The `get_path()` method is in charge of obtaining the path of the folder to order.

The `initial_state_reset()` method is in charge of resetting the class attributes to their initial state.

The `get_all_files_from_path()` method is in charge of getting all the files from the chosen `path` and all the extensions are selected.

The `get_specific_files_from_path()` method is in charge of getting all files from the chosen `path` and some extensions are selected.

The `get_all_extensions_from_path()` method is in charge of getting all available extensions from the chosen `path`.

The `create_extension_folders()` method is in charge of creating the necessary folders depending on the available extensions in `extensions`.

The `move_files_to_their_directory()` method is in charge of moving the files to their relevant folders.

The `revert_organizer()` method is in charge of reverting everything back once a folder is organized, it will return the folder to its initial unorganized state.
