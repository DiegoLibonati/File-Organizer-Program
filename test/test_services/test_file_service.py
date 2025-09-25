from pathlib import Path

from src.services.file_service import FileService


def test_set_path(tmp_path: Path):
    service = FileService()
    message, status = service.set_path(str(tmp_path))
    assert status is True
    assert "Path loaded" in message


def test_set_path_invalid():
    service = FileService()
    message, status = service.set_path("")
    assert status is False
    assert "Path loaded" not in message


def test_organize_without_path():
    service = FileService()
    message, status = service.organize(["txt"], {})
    assert status is False
    assert message == "You must enter a path in order to organize the folder."


def test_organize_with_extensions_and_filters(tmp_path: Path):
    test_file = tmp_path / "file.txt"
    test_file.write_text("hola")

    service = FileService()
    service.set_path(str(tmp_path))
    message, status = service.organize(["txt"], {"min_size": 0, "max_size": 10})
    assert isinstance(message, str)
    assert isinstance(status, bool)


def test_revert_without_path():
    service = FileService()
    message, status = service.revert()
    assert status is False
    assert message == "You must enter a path in order to reverse organize the folder."


def test_revert_with_path(tmp_path: Path):
    test_file = tmp_path / "file.txt"
    test_file.write_text("hola")

    service = FileService()
    service.set_path(str(tmp_path))
    service.organize(["txt"], {"min_size": 0, "max_size": 10})
    message, status = service.revert()
    assert isinstance(message, str)
    assert isinstance(status, bool)
