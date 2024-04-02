from colorama import Fore
from aiohttp import ClientSession
import sys
import pyfiglet
import asyncio


def main():
    print(Fore.BLUE, pyfiglet.figlet_format("BRUTE", font="slant"), end="")
    print(Fore.BLUE, "path brute-forcing script", Fore.RESET, sep="")
    if len(sys.argv) < 3:
        print("\nUSAGE: BRUTE.py [URL] [filename | wordlist]")
        return
    try:
        url = sys.argv[1]
        if not url.startswith("http"):
            url = "https://" + url
        path = sys.argv[2]
        with open(path, 'r') as file:
            asyncio.run(fetch_paths(url, file.readlines()))
    except OSError:
        print("File doesn't exist")


async def fetch_paths(url, paths):
    session = ClientSession()
    for path in paths:
        path = path.strip()
        link = await session.get(url + "/" + path + ".html")
        if link.status != 404:
            print(Fore.GREEN, f">> OK[{str(link.status)}]:   ", link.url.human_repr(), Fore.RESET, sep="")
        if link.status == 404:
            print(Fore.RED, ">> ERROR:   ", link.url.human_repr(), Fore.RESET, sep="")



if __name__ == "__main__":
    main()