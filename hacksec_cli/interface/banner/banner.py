from os import path
from interface.cli import cli


def ShowBanner(**kwargs):
    """Prints the banner"""
    banner_txt = """
                                                              
  __   _  ____    ______  __  __  ______  ______  ______  
 |  |_| ||    \  |   ___||  |/ / |   ___||   ___||   ___| 
 |   _  ||     \ |   |__ |     \  `-.`-. |   ___||   |__  
 |__| |_||__|\__\|______||__|\__\|______||______||______|
                                                          
                                            version : {{version}}
                                            visit our website : {{host}}
    """
    for k, v in kwargs.items():
        banner_txt = banner_txt.replace("{{"+k+"}}", v)
    cli.print_info(banner_txt)
