import os
import shutil
from test.constants import FOLDER_TEST_PATH
from tkinter import Tk

from pytest import fixture

from src.models.file_organizer import FileOrganizer
from src.ui.interface_app import InterfaceApp


@fixture(scope="session")
def interface_app() -> InterfaceApp:
    root = Tk()
    return InterfaceApp(root=root)


@fixture(scope="session")
def file_organizer(folder_test_path: str) -> FileOrganizer:
    file_organizer = FileOrganizer(path=folder_test_path)
    return file_organizer


@fixture(scope="session")
def folder_test_path() -> str:
    return FOLDER_TEST_PATH


def pytest_sessionstart():
    """Se ejecuta antes de que comiencen los tests."""

    if not os.path.exists(FOLDER_TEST_PATH):
        os.mkdir(FOLDER_TEST_PATH)

    # Create files extensions

    file_txt = open(f"{FOLDER_TEST_PATH}/test.txt", "w")
    file_txt.close()

    file_exe = open(f"{FOLDER_TEST_PATH}/test.py", "w")
    file_exe.close()


def pytest_sessionfinish():
    """Se ejecuta después de que todos los tests hayan terminado."""

    shutil.rmtree(path=FOLDER_TEST_PATH)
