import pip
import os


def install():
    if hasattr(pip, 'main'):
        pip.main(['install', "-r", "requirements.txt"])
    else:
        pip._internal.main(['install',  "-r", "requirements.txt"])


install()


def setup():
    from git import Repo
    install_dir = os.path.join(
        os.path.expanduser('~'), "hacksec-cli")
    if install_dir.isdir(install_dir):
        os.remove(install_dir)
    Repo.clone_from(
        "https://github.com/ScRiPt1337/hacksec-cli", install_dir)
    print("hacksec-cli install successfully")
    print("add this path to your system variable " +
          os.path.join(install_dir, "hacksec_cli"))


setup()
