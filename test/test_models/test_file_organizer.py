import logging
import os

from src.models.file_organizer import FileOrganizer

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def test_initial_file_organizer(
    file_organizer: FileOrganizer, folder_test_path: str
) -> None:
    assert file_organizer.path == folder_test_path
    assert file_organizer.folder_name == "ORGANIZER"
    assert file_organizer.all_path_extensions == ["py", "txt"]
    assert not file_organizer.filters
    assert not file_organizer.extensions_allowed


def test_reset_state(file_organizer: FileOrganizer) -> None:
    file_organizer.filters = {"min_size": 12, "max_size": 15}
    file_organizer.all_path_extensions == []

    file_organizer._reset_state()

    assert not file_organizer.filters
    assert file_organizer.all_path_extensions == ["py", "txt"]


def test_get_extensions_not_files(file_organizer: FileOrganizer) -> None:
    extensions = file_organizer._get_extensions(files=[])

    assert not extensions


def test_get_extensions(file_organizer: FileOrganizer) -> None:
    files = ["pepe.txt", "carlos.txt", "p.exe", "index.html"]

    extensions = file_organizer._get_extensions(files=files)

    assert extensions == ["txt", "exe", "html"]


def test_get_files_without_filters_and_extensions_allowed(
    file_organizer: FileOrganizer,
) -> None:
    files = file_organizer._get_files()

    assert files == ["test.py", "test.txt"]


def test_get_files_with_extensions_allowed_and_without_filters(
    file_organizer: FileOrganizer,
) -> None:
    file_organizer.extensions_allowed = ["txt"]

    files = file_organizer._get_files()

    assert files == ["test.txt"]


def test_get_files_with_filters_and_without_extensions_allowed(
    file_organizer: FileOrganizer,
) -> None:
    file_organizer.filters = {"min_size": 0, "max_size": 15}
    file_organizer.extensions_allowed = []

    files = file_organizer._get_files()

    assert files == ["test.py", "test.txt"]


def test_get_files_with_extensions_allowed_filters(
    file_organizer: FileOrganizer,
) -> None:
    file_organizer.filters = {"min_size": 0, "max_size": 15}
    file_organizer.extensions_allowed = ["txt"]

    files = file_organizer._get_files()

    assert files == ["test.txt"]


def test_organizer_not_path_or_extensions_allowed(
    file_organizer: FileOrganizer,
) -> None:
    file_organizer.all_path_extensions = []

    message, status = file_organizer.organizer()

    assert not status
    assert (
        message
        == "It could not be organized because there is no path or there are no extensions."
    )


def test_organizer_not_files(file_organizer: FileOrganizer) -> None:
    file_organizer._reset_state()
    file_organizer.extensions_allowed = ["exe"]

    message, status = file_organizer.organizer()

    assert not status
    assert message == "There are no files to organize. Adjust filters or change path."


def test_revert_organizer_not_folders(file_organizer: FileOrganizer) -> None:
    message, status = file_organizer.revert_organizer()

    assert not status
    assert message == "There are no folders to revert."


def test_organizer_all_files(
    file_organizer: FileOrganizer, folder_test_path: str
) -> None:
    file_organizer.extensions_allowed = []
    file_organizer._reset_state()

    message, status = file_organizer.organizer()

    assert status
    assert message == "Successfully organized."

    folder_names = [
        name
        for name in os.listdir(folder_test_path)
        if os.path.isdir(f"{folder_test_path}/{name}")
    ]

    assert f"TXT_{file_organizer.folder_name}" in folder_names
    assert f"PY_{file_organizer.folder_name}" in folder_names


def test_revert_organizer(file_organizer: FileOrganizer) -> None:
    message, status = file_organizer.revert_organizer()

    assert status
    assert message == "Successfully reverted."


def test_organizer_with_extensions_allowed(
    file_organizer: FileOrganizer, folder_test_path: str
) -> None:
    file_organizer.extensions_allowed = ["txt"]
    file_organizer._reset_state()

    message, status = file_organizer.organizer()

    assert status
    assert message == "Successfully organized."

    folder_names = [
        name
        for name in os.listdir(folder_test_path)
        if os.path.isdir(f"{folder_test_path}/{name}")
    ]

    assert f"TXT_{file_organizer.folder_name}" in folder_names
    assert f"PY_{file_organizer.folder_name}" not in folder_names

    file_organizer.revert_organizer()
