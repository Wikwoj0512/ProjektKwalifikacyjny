import tkinter as tk
from unittest import TestCase

from Entities import Entities


class MockApplication(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Application")
        self.geometry("500x500")
        self.entities = Entities(self)

    def start_analysis(self) -> None:
        pass


class TestEntities(TestCase):
    app = MockApplication()

    def test_get_entities(self):  # Test if the entities are created properly

        self.assertIsInstance(self.app.entities, Entities)
        self.assertIsInstance(self.app.entities.button, tk.Button)
        self.assertIsInstance(self.app.entities.entry_label, tk.Label)
        self.assertIsInstance(self.app.entities.url_entry, tk.Entry)
        self.assertIsInstance(self.app.entities.results, tk.Frame)

    def test_display_error(self):  # Test if the error is displayed properly
        self.app.entities.display_error("Test")
        self.assertEqual(self.app.entities.entry_label.cget("text"), "Test")
        self.assertEqual(self.app.entities.entry_label.cget("fg"), "red")

    def test_display_content(self):  # Test if the content is displayed properly
        self.app.entities.display_content({"test": "1"})
        self.assertEqual(self.app.entities.results.winfo_children()[0].cget("text"), "Word")
        self.assertEqual(self.app.entities.results.winfo_children()[1].cget("text"), "Count")
        self.assertEqual(self.app.entities.results.winfo_children()[2].cget("text"), "test")
        self.assertEqual(self.app.entities.results.winfo_children()[3].cget("text"), "1")

    def test_clear(self):  # Test if the results and errors are cleared properly
        self.app.entities.display_error("Test")
        self.app.entities.display_content({"test": "1"})
        self.app.entities.clear()
        self.assertEqual(self.app.entities.entry_label.cget("text"), "Enter url")
        self.assertEqual(self.app.entities.entry_label.cget("fg"), "black")
        self.assertEqual(self.app.entities.results.winfo_children(), [])
