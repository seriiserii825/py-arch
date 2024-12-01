import os
from rich import print


def chrome():
    print("[red]Setup copyq afer press enter")
    os.system("copyq")
    # wait for user to press enter
    input()
    os.system("yay -S google-chrome")
    print("[blue]Installing ChromeDriver")
    os.system("yay -S chromedriver")
    
