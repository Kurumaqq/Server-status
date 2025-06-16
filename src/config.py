from dotenv import load_dotenv
from os import getenv
import json

class Config():
    load_dotenv()

    @property
    def token(self) -> str: return getenv('TOKEN')
    
    @property
    def own_chat(self) -> int : return int(getenv('OWN_CHAT_ID'))

    @property
    def ignore_service(self) -> list: 
        with open('ignore-services.json') as f:
            return json.load(f)['services']
