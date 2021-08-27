from os import path
from interface.cli import cli


def ShowBanner(**kwargs):
    """Prints the banner"""
    banner_txt = ""
    with open(path.join("interface", "banner", "home.txt"), 'r') as banner:
        banner_txt = banner.read()
    for k, v in kwargs.items():
        banner_txt = banner_txt.replace("{{"+k+"}}", v)
    cli.print_info(banner_txt)
