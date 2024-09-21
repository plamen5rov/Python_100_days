from selenium import webdriver
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the environment variables
SIMILAR_ACCOUNT = os.getenv('SIMILAR_ACCOUNT')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

# print(f"Similar Account: {SIMILAR_ACCOUNT}")
# print(f"Username: {USERNAME}")
# print(f"Password: {PASSWORD}")



class InstaFollower:

    def __init__(self):
        # Optional - Keep browser open (helps diagnose issues during a crash)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()