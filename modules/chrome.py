import os


def chrome():
    print("Installing Google Chrome")
    os.system("yay -S google-chrome")
    print("Installing ChromeDriver")
    os.system("yay -S chromedriver")
    
