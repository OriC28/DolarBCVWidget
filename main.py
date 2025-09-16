from src.dolarbcvwidget.gui import Widget

"""
This script serves as the entry point for the DolarBCVWidget application.
It imports the Widget class from the GUI module and initializes the main window
when executed as the main program.
Usage:
    Run this script directly to launch the DolarBCVWidget GUI.
Modules:
    - src.dolarbcvwidget.gui: Contains the Widget class for the application's GUI.
Classes:
    - Widget: The main window class for the DolarBCVWidget application.
Execution:
    If run as the main module, creates an instance of Widget and starts the main event loop.
"""

if __name__ == "__main__":
    window = Widget()
    window.mainloop()
