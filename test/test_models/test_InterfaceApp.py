import logging

import pytest
from unittest.mock import patch
from unittest.mock import MagicMock

from src.models.InterfaceApp import InterfaceApp
from src.utils.constants import BACKGROUND_COLOR


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def test_initial_config_tk_app(interface_app: InterfaceApp) -> None:
    root = interface_app._root
    file_organizer = interface_app.file_organizer
    root.update()

    title = root.title()
    geometry = root.geometry().split("+")[0]
    resizable = root.resizable()
    config_bg = root.cget("bg")

    assert title == "File Organizer V1.0.0"
    assert geometry == "400x600"
    assert resizable == (False, False)
    assert config_bg == BACKGROUND_COLOR

    assert not file_organizer

def test_create_widgets(interface_app: InterfaceApp) -> None:
    interface_app._create_widgets()

    assert interface_app._text_path.get() == "Wait for directory..."
    
    assert interface_app._check_value_all.get() == True
    assert interface_app._check_value_mp4.get() == True
    assert interface_app._check_value_pdf.get() == True
    assert interface_app._check_value_exe.get() == True
    assert interface_app._check_value_jpg.get() == True
    assert interface_app._check_value_jpeg.get() == True
    assert interface_app._check_value_png.get() == True
    assert interface_app._check_value_txt.get() == True
    assert interface_app._check_value_json.get() == True
    assert interface_app._check_value_mp3.get() == True
    assert interface_app._check_value_m3u8.get() == True
    assert interface_app._check_value_zip.get() == True
    assert interface_app._check_value_gif.get() == True

    assert interface_app._extensions_options

    assert interface_app._check_value_filters.get() == False
    
    assert interface_app._filter_min_size.get() == 1
    assert interface_app._filter_max_size.get() == 10

    assert interface_app._filters

    assert interface_app._entry_path
    assert interface_app._button_search
    assert interface_app._button_organize
    assert interface_app._button_revert
    assert interface_app._label_frame_extensions
    assert interface_app._check_button_all
    assert interface_app._check_button_mp4
    assert interface_app._check_button_pdf
    assert interface_app._check_button_exe
    assert interface_app._check_button_jpg
    assert interface_app._check_button_jpeg
    assert interface_app._check_button_png
    assert interface_app._check_button_txt
    assert interface_app._check_button_json
    assert interface_app._check_button_mp3
    assert interface_app._check_button_m3u8
    assert interface_app._check_button_zip
    assert interface_app._check_button_gif
    assert interface_app._label_frame_filters
    assert interface_app._check_button_filter_by
    assert interface_app._label_min_size
    assert interface_app._entry_min_size
    assert interface_app._label_max_size
    assert interface_app._entry_max_size


def test_organize_without_instance(interface_app: InterfaceApp) -> None:
    with patch("tkinter.messagebox.showerror") as showerror:
        interface_app._organize()

        showerror.assert_called_once_with(
            message="You must enter a path in order to organize the folder.", 
            title="File Organizer"
        )
        

def test_reverse_organize_without_instance(interface_app: InterfaceApp) -> None:
    with patch("tkinter.messagebox.showerror") as showerror:
        interface_app._reverse_organize()

        showerror.assert_called_once_with(
            message="You must enter a path in order to reverse organize the folder.", 
            title="File Organizer"
        )


def test_set_path(interface_app: InterfaceApp, folder_test_path: str) -> None:
    path = folder_test_path

    with patch("tkinter.filedialog.askdirectory") as askdirectory:
        askdirectory.return_value = path

        with patch("tkinter.messagebox.showinfo") as showinfo:
            interface_app._set_path()

            assert interface_app._text_path.get() == path
            assert interface_app.file_organizer.path == path

            askdirectory.assert_called_once_with(title="Choose a directory")

            showinfo.assert_called_once_with(
                message=f"Path loaded: {path} successfully.",
                title="File Organizer",
            )


def test_organize_without_extensions_allowed(interface_app: InterfaceApp) -> None:
    for value in interface_app._extensions_options.values():
        value.set(False)

    with patch("tkinter.messagebox.showerror") as showerror:
        interface_app._organize()

        showerror.assert_called_once_with(
            message="Select at least one extension to organize the path.", 
            title="File Organizer"
        )

    
def test_organize(interface_app: InterfaceApp) -> None:
    interface_app._check_value_txt.set(True)

    with patch("tkinter.messagebox.showinfo") as showinfo:
        interface_app._organize()

        showinfo.assert_called_once_with(
            message="Successfully organized.", 
            title="File Organizer"
        )


def test_reverse_organize(interface_app: InterfaceApp) -> None:
    with patch("tkinter.messagebox.showinfo") as showinfo:
        interface_app._reverse_organize()

        showinfo.assert_called_once_with(
            message="Successfully reverted.", 
            title="File Organizer"
        )


def test_select_all_extensions(interface_app: InterfaceApp) -> None:
    interface_app._check_value_all.set(True)

    interface_app._select_all_extensions()

    for option in interface_app._extensions_options.values():
        assert option.get()

    interface_app._check_value_all.set(False)

    interface_app._select_all_extensions()

    for option in interface_app._extensions_options.values():
        assert not option.get()


def test_select_extension(interface_app: InterfaceApp) -> None:
    interface_app._select_extension()

    assert not interface_app._check_value_all.get()


def test_handle_filters(interface_app: InterfaceApp) -> None:
    interface_app._check_value_filters.set(True)

    interface_app._handle_filters()

    interface_app._entry_min_size["state"] == "disabled"
    interface_app._entry_max_size["state"] == "disabled"

    interface_app._check_value_filters.set(False)

    interface_app._handle_filters()

    interface_app._entry_min_size["state"] == "normal"
    interface_app._entry_max_size["state"] == "normal"