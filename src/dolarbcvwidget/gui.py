import tkinter as tk
from PIL import Image, ImageTk

from dolarbcvwidget.api import get_bcv_price
from dolarbcvwidget.date import get_datetime_current

"""
This module defines the GUI components for the DolarBCVWidget application using Tkinter.
Classes:
    Text (tk.Label): A custom label class with predefined styles for text display.
    Widget (tk.Tk): The main widget class that creates and manages the application window, including UI configuration, drag events, price display, date display, and image rendering.
Functions:
    Widget.configure_ui(self): Configures the UI elements and styles of the widget.
    Widget.set_events(self): Sets up mouse drag events for moving the window.
    Widget.start_drag(self, event): Initializes drag data when the window is clicked.
    Widget.drag(self, event): Updates the window position during dragging.
    Widget.set_price(self): Displays the current dollar price or an error message.
    Widget.set_date(self): Displays the current date.
    Widget.set_image(self): Loads and displays an image in the widget.
"""


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
        image = Image.open('assets/image.png')
        image = image.resize((100, 100), Image.LANCZOS)
        photo_image = ImageTk.PhotoImage(image)
        image_label = tk.Label(self, image=photo_image, border=0)
        image_label.place(x=280, y=55)
        image_label.image = photo_image
