# GUI Chess Playing Robot "Chester"

This Python script implements a graphical user interface (GUI) for a chess playing robot. Users can play chess against the robot using the Tkinter library for the interface.

## Description

The GUI Chess Playing Robot allows users to play chess against an automated opponent represented by the script. The robot follows standard chess rules and provides an interactive interface for gameplay.

:exclamation:
This version is designed for 1024x600px resolution display
:exclamation:

## Features

- Graphical chessboard interface.
- Supports legal move validation and pawn promotion (In this version pawns are instantly promoted to queens).
- Automatically detects checkmate and ends the game.
- Responsive design for smooth gameplay experience.

## Requirements

- Python 3.x
- Tkinter library
- Python-Chess library
- board library --> `It should be downloaded with adafruit-circuitpython-motorkit library`
- adafruit-circuitpython-motorkit library

## Usage

1. Clone the repository to your local machine.
2. Install the required Python libraries (Tkinter, python-chess, adafruit-circuitpython-motorkit).
   ```bash
   pip install python-chess;
   adafruit-circuitpython-motorkit

3. Navigate to the project directory.
4. Run the `Gui.py` script using Python:
   ```bash
   python Gui.py