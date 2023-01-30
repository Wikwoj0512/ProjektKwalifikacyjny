import tkinter as tk
from analysis import analyse_article
from utils import UrlException, ContentException, ConnectionException, validate_url
from Entities import Entities


class Application(tk.Tk):  # This is the main application class
    def __init__(self) -> None:
        """
        Initialise the main application class
        """
        super().__init__()  # Initialise the tkinter class
        self.title("Aplikacja")  # Set the title of the window
        self.geometry("500x500")  # Set the size of the window
        self.entities = Entities(self)  # Create the entities

    def start_analysis(self) -> None:
        """
        Starts the analysis of the url and displays the results or an error message
        :return: None
        """
        self.entities.clear()  # Clear the results frame and errors
        url = self.entities.url_entry.get()  # Get the url from the entry

        if not url:  # If the url is empty
            self.entities.display_error("Please enter a url")
            return

        if not validate_url(url):  # If the url is invalid
            self.entities.display_error("Error - invalid url address")
            return
        try:  # Try to get the content of the url
            result = analyse_article(url)
            self.entities.display_content(result)
        except ConnectionException as e:  # If there is a connection error
            self.entities.display_error(str(e))
        except UrlException as e:  # If there is a problem with the url
            self.entities.display_error(str(e))
        except ContentException as e:  # If there is a problem with the content
            self.entities.display_error(str(e))


app = Application()  # Create the application
app.mainloop()  # Start the application
