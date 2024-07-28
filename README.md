# Snap Tap Controller

This project provides a simple graphical interface to enable and disable the Snap Tap functionality for keyboards. Snap Tap allows for instantaneous directional changes without lifting the initial key, enhancing gaming performance, especially in competitive environments.

## Features

- **Activate/Deactivate Snap Tap**: Easily toggle the Snap Tap mode using a graphical button.
- **Keyboard Monitoring**: Monitors specific key combinations and simulates key presses to achieve Snap Tap behavior.
- **User-Friendly Interface**: Built with Tkinter for a simple and intuitive user experience.

## Requirements

- Python 3.x
- Pynput library for keyboard control
- Tkinter for the graphical user interface (included with Python)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/RodCas11/RZRSnap.git
    cd RZRSnap
    ```

2. **Install the required libraries**:
    ```sh
    pip install pynput
    ```

3. **Run the application**:
    ```sh
    python snap_tap_controller.py
    ```

## Usage

1. **Launch the Application**: Run `python snap_tap_controller.py` to start the graphical interface.
2. **Activate Snap Tap**: Click the "Activate Snap Tap" button to enable the Snap Tap functionality. The button will change to "Deactivate Snap Tap".
3. **Deactivate Snap Tap**: Click the "Deactivate Snap Tap" button to disable the Snap Tap functionality.

## Code Explanation

### Main Components

- **toggle_snap_tap**: Toggles the Snap Tap mode on and off.
- **start_listener**: Starts the keyboard listener to monitor key presses and releases.
- **stop_listener**: Stops the keyboard listener.
- **on_press / on_release**: Handles the key press and release events.
- **monitor_keys**: Monitors key states and simulates key presses to achieve Snap Tap behavior.
- **Tkinter GUI**: Provides a simple graphical interface with a button to control the Snap Tap functionality.
