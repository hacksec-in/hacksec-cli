import aiohttp
import asyncio
import os
from git import Repo
from rich.console import Console
import shutil

console = Console()


async def check_for_update():
    url = "https://raw.githubusercontent.com/hacksec-in/hacksec-cli/main/hacksec_cli/version.txt"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            return await r.read()


def version_verify(current_version):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(check_for_update())
    install_dir = ""
    if float(result.decode()) > float(current_version):
        console.print("There is an upload available", style="bold red")
        with console.status("[bold green]updating...\n") as status:
            if os.name == "nt":
                install_dir = os.path.join(
                    os.path.expanduser('~'), "hacksec-cli")
            else:
                install_dir = os.path.join("/usr/share", "hacksec-cli")
            if os.path.isdir(install_dir):
                try:
                    # os.rmdir(install_dir)
                    shutil.rmtree(install_dir)
                except PermissionError:
                    console.print("[bold red]Please run hacksec as root to update!", style="bold red")
                    exit()
            Repo.clone_from(
                "https://github.com/hacksec-in/hacksec-cli", install_dir)
            console.print("Update successfull", style="bold green")
            console.print("Please restart hacksec-cli", style="bold green")
            exit()
