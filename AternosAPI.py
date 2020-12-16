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

  # Returns the content of a HTML tag given the arguments:
  # error: the error message to print
  # name: name of the html tag
  # id_: id atribute to searh for
  # clas: class atribute to search for
  def search(self, name=None, id_=None, clas=None, error=None):
    web = requests.get(url="https://aternos.org/server/", headers=self.aternos_data)
    html = BeautifulSoup(web.content, "html.parser")
    result = html.find(name, id=id_, class_=clas)

    # Check if the result it is correct
    if (not result == None):
      return result.get_text().strip()

    # Error handling
    elif (html.find("span", class_="logout") != None):
      raise UnexpectedError(error)
    else:
      raise InvalidCookie("Error: cannot conect to Aternos. Check the cookie value")
