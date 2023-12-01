import json
import os

from models.user import UserModel
from models.item import ItemModel
from typing import List

_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class KslContent:
    """
    KSL seems to work off the same content base and adds features to their app as you navigate through pages. This makes it easy to automate as you can add more variables
    depending on whats needed and navigate with these locators pretty well. 
    """
    _content = "#__next div [class='jsx-959004977 ksl-header-menu-container__content']"
    _form = _content + " main [class] div [class='jsx-2408500200 root'] div div form"
    input_wrapper = _form + " [data-testid='input-wrapper']"
    login_button = _form + " [class='Button__Wrapper-hsu6mt-16 hGRPtK'] button"
    add_listing = _content + " button"



def get_user() -> UserModel:
    """
    Get the UserModel from users.json
    """
    with open(_ROOT_DIR + '/users.json', 'r') as json_file:
        _json = json.loads(json_file.read())
        return UserModel(**_json)
    

def get_items() -> List[ItemModel]:
    """
    Get the list of items and their photo paths from items.json
    """
    with open(os.path.join(_ROOT_DIR, 'items.json'), 'r') as json_file:
        items_json = json.load(json_file)
        return [ItemModel(**item) for item in items_json.get("items", [])]