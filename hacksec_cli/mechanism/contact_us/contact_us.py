<<<<<<< HEAD
from rich.console import Console
from rich.table import Table
from interface.menu.menu import main_menu
import os
import sys
import subprocess

console = Console()


class contact_us():
    """Contact us class"""

    def open_uri(self, url):
        if sys.platform == 'win32':
            os.startfile(url)
        elif sys.platform == 'darwin':
            subprocess.Popen(['open', url])
        else:
            try:
                subprocess.Popen(['xdg-open', url])
            except OSError:
                print('Please open a browser on: '+url)

    def generate_contact(self):
        """Contact us"""
        options = ["facebook", "twitter", "youtube", "email", "instagram"]
        anwser = main_menu("Contact us", options,
                           "Contact us through")
        if anwser == options[0]:
            self.open_uri("https://facebook.com/hacksec42")
        elif anwser == options[1]:
            self.open_uri("https://twitter.com/hacksec42")
        elif anwser == options[2]:
            self.open_uri(
                "https://www.youtube.com/channel/UCYbdEFxzLMTTrh2571Z4cGg")
        elif anwser == options[3]:
            self.open_uri(
                "mailto:script1337x@gmail.com?subject=I have an question&body=[Your questions goes here]")
        elif anwser == options[4]:
            self.open_uri("https://www.instagram.com/hacksec42/")
=======
from rich.console import Console
from rich.table import Table
from interface.menu.menu import main_menu
import os
import sys,subprocess

console = Console()


class contact_us():
    """Contact us class"""

    def open_uri(self, url):
        if sys.platform == 'win32':
            os.startfile(url)
        elif sys.platform == 'darwin':
            subprocess.Popen(['open', url])
        else:
            try:
                subprocess.Popen(['xdg-open', url])
            except OSError:
                print('Please open a browser on: '+url)

    def generate_contact(self):
        """Contact us"""
        options = ["facebook", "twitter", "youtube", "email", "instagram"]
        anwser = main_menu("Contact us", options,
                           "Contact us through")
        if anwser == options[0]:
            self.open_uri("https://facebook.com/hacksec42")
        elif anwser == options[1]:
            self.open_uri("https://twitter.com/hacksec42")
        elif anwser == options[2]:
            self.open_uri(
                "https://www.youtube.com/channel/UCYbdEFxzLMTTrh2571Z4cGg")
        elif anwser == options[3]:
            self.open_uri(
                "mailto:script1337x@gmail.com?subject=I have an question&body=[Your questions goes here]")
        elif anwser == options[4]:
            self.open_uri("https://www.instagram.com/hacksec42/")
>>>>>>> origin/main
