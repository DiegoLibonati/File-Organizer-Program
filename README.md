# File Organizer Program

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Execute: `python -m venv venv`
4. Execute in Windows: `venv\Scripts\activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Use `python -m src.app` to execute program

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Description

I made a program that allows to sort the files in a specific path. It will get all the file extensions and create a folder for each extension in that path. Then it will add to each folder the file that corresponds to it. Basically it sorts files depending on the extension. In addition we will be able to choose which extensions to sort or all of them. Filters can also be applied, being able to sort files with a specific size. Finally, if we want to go back we can also do it by clicking on the `Revert ORGANIZE` button, thus returning to the initial state of the path.

## Technologies used

1. Python >= 3.11

## Libraries used

#### Requirements.txt

```
pre-commit==4.3.0
```

#### Requirements.test.txt

```
pytest==8.4.2
```

#### Requirements.build.txt

```
pyinstaller==6.16.0
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/File-Organizer-Program`](https://www.diegolibonati.com.ar/#/project/File-Organizer-Program)

## Video

https://user-images.githubusercontent.com/99032604/205468137-440a09af-4de6-4179-9cf7-5462b2ae414c.mp4

## Testing

1. Join to the correct path of the clone
2. Execute in Windows: `venv\Scripts\activate`
3. Execute: `pytest --log-cli-level=INFO`

## Build

You can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Join to the correct path of the clone
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec"`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Join to the correct path of the clone
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec"`

Alternatively, you can run the helper script: `./build.sh`

## Known Issues
