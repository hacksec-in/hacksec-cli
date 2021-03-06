import os
import json


class user_configure():
    """user class this will hold all user_information"""

    def __init__(self):
        self.username = "hacksec"
        self.isLogin = False
        self.access_token = None
        self.user_file = None

    def logout(self):
        """Logout the user"""
        os.remove(self.user_file)
        self.username = "hacksec"
        self.isLogin = False
        self.access_token = None


class configure():
    """this is configure class which set all values from env to and set all required values"""

    def __init__(self):
        self.isLinux = True
        self.host = "https://api.hacksec.in"
        self.website = "https://hacksec.in"
        self.cmd_prefix = "@hacksec#"
        self.version = "0.0"



def load_user(DATA_FILE, user):
    """load user from user.json"""
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        user.username = data["username"]
        user.isLogin = True
        user.access_token = data["access_token"]
        return user

def get_version():
    """get version of the app"""
    version_txt = os.path.join(os.path.dirname(__file__), "version.txt")
    with open(version_txt,"r") as file:
        return file.read()

def app_config():
    """init configure"""
    DATA_FOLDER = os.path.join(os.path.expanduser(
        '~'), ".config", "hacksec")
    DATA_FILE = os.path.join(DATA_FOLDER, "user.json")
    config = configure()
    user = user_configure()
    user.user_file = DATA_FILE
    config.version = get_version()
    if os.name == "nt":
        config.isLinux = False
    if os.path.isdir(DATA_FOLDER):
        if os.path.isfile(DATA_FILE):
            user = load_user(DATA_FILE, user)
    else:
        os.makedirs(DATA_FOLDER)
    return config, user
