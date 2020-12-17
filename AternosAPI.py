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
    if not self.is_valid_cookie():
      raise InvalidCookie("Error: cannot conect to Aternos. Check the cookie value")

  # Return True whether the cookie is valid
  def is_valid_cookie(self):
    # Try finding the logout button (it means we open a session)
    web = requests.get(url="https://aternos.org/server/", headers=self.aternos_data)
    html = BeautifulSoup(web.content, "html.parser")
    result = html.find("span", class_="logout")
    return not result == None

  def __search(self, name=None, id_=None, clas=None, error=None):
    """
    Returns the content of a HTML tag on the Aternos page given the arguments:
    :param name: name of the html tag
    :param id_: id atribute to searh for
    :param clas: class atribute to search for
    :param error: the error message to print
    :return the content of the HTML tag of the web
    """
    web          = requests.get(url = "https://aternos.org/server/", headers = self.aternos_data)
    html         = BeautifulSoup(web.content, "html.parser")
    html_element = html.find(name, id = id_, class_ = clas)

    # Check if the result it is correct
    if not html_element == None:
      result = html_element.get_text().replace("\n", "").strip()
      return result

    # Error handling
    elif html.find("span", class_="logout") != None:
      raise UnexpectedError(error)
    else:
      raise InvalidCookie("Error: Cannot conect to Aternos. Check the cookie value")

  def get_server_name(self):
    return self.__search(
      name  = "div",
      clas  = "server-ip mobile-full-width",
      error = "Error: Cannot load the server name")

  def get_online_status(self):
    return self.__search(
      name  = "span",
      clas  = "statuslabel-label",
      error = "Error: Cannot load the online status")

  def get_online_players(self):
    return self.__search(
      name  = "span",
      id_   = "players",
      error ="Error: Cannot load the online players")

  def get_server_software(self):
    return self.__search(
      name  = "span",
      id_   = "software",
      error = "Error: Cannot load the server software")

  def get_server_version(self):
    return self.__search(
      name  = "span",
      id_   = "version",
      error = "Error: Cannot load the server version")

  def get_queue_number(self):
    return self.__search(
      name  = "span",
      clas  = "server-status-label-right queue-position hidden",
      error = "Error: Cannot read the queue because the server it is not on the queue")

  def get_queue_time_left(self):
    return self.__search(
      name  = "span",
      clas  = "server-status-label-left queue-time hidden",
      error = "Error: Cannot read the queue because the server it is not on the queue")

  def start_server(self):
    pass

  def stop_server(self):
    pass
