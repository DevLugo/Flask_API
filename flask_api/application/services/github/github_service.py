import requests
import json
import os

from dotenv import load_dotenv
from threading import Thread
try: 
    import queue
except ImportError:
    import Queue as queue

from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class GithubService():
    def __init__(self) -> None:
        self.endpoint = os.getenv('GITHUB_API_URL')

    """ In a biggest proyect, it-s recomented to create a class for encapsulate the request logic (try/catch and store the full request information on db dable) """
    def get_users(self, per_page:int = 100, since:int=0):
        #https://api.github.com/users?since=1&per_page=100
        status:bool = False
        url_to_request = '{}users?since={}&per_page={}'.format(self.endpoint,since,per_page)
        print(url_to_request)
        response = requests.get(url_to_request, timeout=120)
        if response.ok:
            return response
        return None
