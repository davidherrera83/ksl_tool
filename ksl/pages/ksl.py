import time
import fw

from pylenium.driver import Pylenium
from models.user import UserModel
from models.item import ItemModel

class KSL:
    """
    KSL Wrapper
    Args:
        py: Instance of Pylenium Driver to use for this session.
    """
    def __init__(self, py: Pylenium, user: UserModel):
        self.py = py
        self.user = user

    def login(self):
        self.py.visit('https://myaccount.ksl.com/login?forward=https://myaccount.ksl.com/listings?vertical=Classifieds')
        self.py.find(fw.KslContent.input_wrapper)[0].get("input").type(self.user.username)
        self.py.find(fw.KslContent.input_wrapper)[1].get("input").type(self.user.password)
        self.py.get(fw.KslContent.login_button).click()

        return self

    def create_new_listing(self):
        time.sleep(5) # Wait for page load
        self.py.get(fw.KslContent.add_listing).click()
        self.py.get("reach-portal div div div [data-testid='modal-main'] [tabindex='0']").click()

        return self

    def upload_photos(self, item: ItemModel):
        for file_path in item.photoPaths:
            self.py.get("input[class*='photo']").upload(f'{file_path}')
        return self
    