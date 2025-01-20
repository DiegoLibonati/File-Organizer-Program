# File Organizer Program

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Execute: `python -m venv venv`
4. Execute in Windows: `venv\Scripts\activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Use `python -m src.app` to execute program

## Description

I made a program that allows to sort the files in a specific path. It will get all the file extensions and create a folder for each extension in that path. Then it will add to each folder the file that corresponds to it. Basically it sorts files depending on the extension. In addition we will be able to choose which extensions to sort or all of them. Filters can also be applied, being able to sort files with a specific size. Finally, if we want to go back we can also do it by clicking on the `Revert ORGANIZE` button, thus returning to the initial state of the path.

## Technologies used

1. Python

## Libraries used

#### Requirements.txt

```
There are no 3rd libraries.
```

#### Requirements.test.txt

```
pytest
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/File-Organizer-Program`](https://www.diegolibonati.com.ar/#/project/File-Organizer-Program)

## Video

https://user-images.githubusercontent.com/99032604/205468137-440a09af-4de6-4179-9cf7-5462b2ae414c.mp4

## Testing

1. Join to the correct path of the clone
2. Execute in Windows: `venv\Scripts\activate`
3. Execute: `pytest --log-cli-level=INFO`