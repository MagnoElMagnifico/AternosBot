import requests
from bs4 import BeautifulSoup

# Errors throw by this API
class AternosError(Exception):
  pass
class InvalidCookie(AternosError):
  pass
class UnexpectedError(AternosError):
  pass

class AternosServer:
  def __init__(self, cookie):
    # Data needed to send the request (see README)
    self.aternos_data = {}
    self.aternos_data["Cookie"] = cookie

    # Check if it is a valid request
    if (not self.is_valid_cookie()):
      raise InvalidCookie("Error: cannot conect to Aternos. Check the cookie value")

  # Return True whether the cookie is valid
  def is_valid_cookie(self):
    # Try finding the logout button (it means we open a session)
    web = requests.get(url="https://aternos.org/server/", headers=self.aternos_data)
    html = BeautifulSoup(web.content, "html.parser")
    result = html.find("span", class_="logout")
    return not result == None
