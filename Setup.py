import os

def print_logo():
    print("""  
     /$$$$$$$$ /$$         /$$ /$$$$$$$$ /$$$$$$ 
    | $$_____/| $$       /$$$$|__  $$__//$$__  $$
    | $$      | $$      |_  $$   | $$  |__/  \ $$
    | $$$$$   | $$        | $$   | $$     /$$$$$/
    | $$__/   | $$        | $$   | $$    |___  $$
    | $$      | $$        | $$   | $$   /$$  \ $$
    | $$$$$$$$| $$$$$$$$ /$$$$$$ | $$  |  $$$$$$/
    |________/|________/|______/ |__/   \______/

    https://github.com/Its-Vichy/EL1T3 | ιтѕ_Ѵιcнч#1337                                      
    """)

def install(name):
    os.system(f'pip install {name}')

def install_python():
    try:
        import colorama
    except:
        install("colorama")
    try:
        import requests
    except:
        install("requests")
    try:
        import EL1T3
    except:
        install("EL1T3")
    try:
        import flask
    except:
        install("flask")
    try:
        import tinydb
    except:
        install("tinydb")
    try:
        import asyncio
    except:
        install("asyncio")

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    print_logo()
    install_python()