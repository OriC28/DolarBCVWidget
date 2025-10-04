from PIL import Image, ImageTk
import tkinter as tk
import sys
import os

from dolarbcvwidget.api import get_bcv_price
from dolarbcvwidget.date import get_datetime_current

"""
This module defines the GUI for the DolarBCVWidget application using Tkinter.
    Text (tk.Label): Custom label widget with predefined styles for displaying text.
    Widget (tk.Tk): Main application window, manages UI configuration, drag events, price and date display, and image rendering.
    resource_path(relative_path): Returns the absolute path to a resource, compatible with PyInstaller and development environments.
Widget Methods:
    configure_ui(self): Configures the UI elements and styles of the widget.
    set_events(self): Sets up mouse drag events for moving the window.
    start_drag(self, event): Initializes drag data when the window is clicked.
    drag(self, event): Updates the window position during dragging.
    set_price(self): Displays the current dollar price or an error message.
    set_date(self): Displays the current date.
    set_image(self): Loads and displays an image in the widget.
"""


def resource_path(relative_path):
    """Gets the absolute path to a resource, works for development and PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class Text(tk.Label):
    """Custom label class with specific styles."""

    def __init__(self, master: tk.Tk, text: str, text_size: int):
        super().__init__(master=master)
        self.master = master
        self.text = text
        self.font = ('Arial', text_size)
        self.bg = "#312f2f"
        self.fg = "#ffffff"

        self.config(
            text=self.text,
            font=self.font,
            bg=self.bg,
            fg=self.fg
        )


class Widget(tk.Tk):
    """Main widget class for the application."""

    def __init__(self):
        super().__init__()
        self.drag_data = {"x": 0, "y": 0}
        self.configure_ui()
        Text(self, "Dolar del momento", 14).place(x=25, y=40)

    def configure_ui(self):
        """Configure the UI's element and styles of the widget."""
        self.overrideredirect(True)
        self.geometry("400x200")
        self.resizable(False, False)
        self.configure(bg="#312f2f")
        self.set_events()
        self.set_price()
        self.set_date()
        self.set_image()
        self.set_button_refresh()

    def set_button_refresh(self):
        button = tk.Button(self, text="Actualizar", command=self.set_price)
        button.config(bg="#49cc90", fg="#ffffff", font=("Arial", 12, "bold"),
                      border=0, cursor="hand2", activebackground="#258358")
        button.place(x=290, y=160)

    def set_events(self):
        """Sets the drag events for the program window."""
        self.bind('<Button-1>', self.start_drag)
        self.bind('<B1-Motion>', self.drag)

    def start_drag(self, event):
        """Starts window drag events when the window is clicked."""
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def drag(self, event):
        """Updates the coordinates of the window position as it is dragged."""
        x = self.winfo_x() + (event.x - self.drag_data["x"])
        y = self.winfo_y() + (event.y - self.drag_data["y"])
        self.geometry(f"+{x}+{y}")

    def set_price(self):
        """Set dolar price or error message if it fails in widget."""
        result = get_bcv_price()
        if result.get('error'):
            Text(self, f"{result['error'], 20}").place(x=20, y=65)
            return
        Text(self, f"{result['price']}Bs.", 32).place(x=20, y=65)

    def set_date(self):
        """Set current date in widget."""
        date_label = Text(self, f"{get_datetime_current()}", 12)
        date_label.config(fg="#c7c5c5")
        date_label.place(
            x=26, y=150)

    def set_image(self):
        """Set image in widget."""
        image = Image.open(resource_path('assets/image.png'))
        image = image.resize((100, 100), Image.LANCZOS)
        photo_image = ImageTk.PhotoImage(image)
        image_label = tk.Label(self, image=photo_image, border=0)
        image_label.place(x=280, y=55)
        image_label.image = photo_image
