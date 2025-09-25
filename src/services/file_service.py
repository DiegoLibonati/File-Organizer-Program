import os

from src.models.file_organizer import FileOrganizer


class FileService:
    def __init__(self):
        self._file_organizer: FileOrganizer | None = None

    def set_path(self, path: str) -> tuple[str, bool]:
        if not path or not os.path.exists(path):
            return "Could not load path: invalid or non-existent.", False

        self._file_organizer = FileOrganizer(path=path)
        return f"Path loaded: {path} successfully.", True

    def organize(self, extensions: list[str], filters: dict) -> tuple[str, bool]:
        if not self._file_organizer:
            return "You must enter a path in order to organize the folder.", False

        self._file_organizer.extensions_allowed = extensions
        self._file_organizer.filters = filters

        return self._file_organizer.organizer()

    def revert(self) -> tuple[str, bool]:
        if not self._file_organizer:
            return (
                "You must enter a path in order to reverse organize the folder.",
                False,
            )
        return self._file_organizer.revert_organizer()
