# GUI Chess Playing Robot "Chester"

This Python script implements a graphical user interface (GUI) for a chess playing robot. Users can play chess against the robot using the Tkinter library for the interface.

## Description

The GUI Chess Playing Robot allows users to play chess against an automated opponent represented by the script. The robot follows standard chess rules and provides an interactive interface for gameplay.

:exclamation: This version is designed for `Waveshare 7" LCD IPS V4.1 1024x600px` display :exclamation:

## Features

- Graphical chessboard interface.
- Supports legal move validation and pawn promotion (In this version pawns are instantly promoted to queens).
- Automatically detects checkmate and ends the game.
- Responsive design for smooth gameplay experience.

## Requirements

- Python 3.x
- Tkinter library
- [Python-Chess](https://python-chess.readthedocs.io/en/latest/ "https://python-chess.readthedocs.io/en/latest/") library
- board library --> `It should be automatically downloaded with adafruit-circuitpython-motorkit library`
- [adafruit-circuitpython-motorkit](https://docs.circuitpython.org/projects/motorkit/en/latest/ "https://docs.circuitpython.org/projects/motorkit/en/latest/") library

## Usage

1. Clone the repository to your local machine.
2. Install the required Python libraries (Tkinter, python-chess, adafruit-circuitpython-motorkit).

   - For Windows:

   ```bash
   pip install python-chess
   ```
   ```bash
   pip install adafruit-circuitpython-motorkit
   ```

   - For Raspberry Pi:
     
   ```bash
   sudo pip3 install python-chess
   ```
   ```bash
   sudo pip3 install adafruit-circuitpython-motorkit
   ```

4. Navigate to the project directory.
5. Run the `Gui.py` script using Python:
   ```bash
   python Gui.py
