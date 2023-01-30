import tkinter as tk


class Entities:  # This is a class to store all the entities
    def __init__(self, root) -> None:
        """
        Initialise the entities class and create the widgets
        :param root: tk.Tk
        """
        self.button = tk.Button(root, text="Analyse", command=root.start_analysis)  # Create the button
        self.entry_label = tk.Label(root, text="Enter url: ")  # Create the label
        self.url_entry = tk.Entry(root, width=45)  # Create the entry field
        self.results = tk.Frame(root)  # Create a frame to store the results

        self.entry_label.grid(row=0, column=0)  # Place elements on the grid
        self.url_entry.grid(row=0, column=1)
        self.button.grid(row=0, column=2)
        self.results.grid(row=1, column=0, columnspan=3)

    def display_error(self, message: str) -> None:
        """
        Displays an error message if something goes wrong
        :param message: Message to display
        :return: None
        """
        self.entry_label.config(
            foreground="red",
            text=message
        )  # Change the label to red and display the error message

    def display_content(self, content: dict) -> None:
        """
        Displays the content of the analysis
        :param content: Content of the page
        :return: None
        """
        frame = self.results
        word_label = tk.Label(frame, text="Word")
        word_label.grid(row=0, column=0, columnspan=2)
        count_label = tk.Label(frame, text="Count")
        count_label.grid(row=0, column=2, columnspan=1)  # Display the table headers

        for i, (word, count) in enumerate(content.items()):  # Loop through the content and display it
            word_label = tk.Label(frame, text=word)
            word_label.grid(row=i + 1, column=0, columnspan=2)
            count_label = tk.Label(frame, text=count)
            count_label.grid(row=i + 1, column=2, columnspan=1)

    def clear(self) -> None:
        """
        Clear the results frame and errors
        :return: None
        """
        self.entry_label.config(
            foreground="black",
            text="Enter url"
        )  # Reset the label to black and display the default message

        for widget in self.results.winfo_children():
            widget.destroy()  # Clear the results frame
