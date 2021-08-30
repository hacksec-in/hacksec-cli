import aiohttp
import asyncio
import os
from git import Repo
from rich.console import Console

console = Console()


async def check_for_update():
    url = "https://raw.githubusercontent.com/ScRiPt1337/hacksec-cli/main/hacksec_cli/version.txt"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            return await r.read()


def version_verify(current_version):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(check_for_update())
    if result.decode() > current_version:
        console.print("there is an upload available", style="bold red")
    with console.status("[bold green]updating...\n") as status:
        install_dir = os.path.join(
            os.path.expanduser('~'), "hacksec-cli")
        os.remove(install_dir)
        Repo.clone_from(
            "https://github.com/ScRiPt1337/hacksec-cli", install_dir)
        console.print("Please restart hacksec-cli", style="bold red")
