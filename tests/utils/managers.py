import requests


# Make a GET request to the /get-data route
def send_get_request(_url: str) -> requests.Response:
    """a simple get request to the backend app.py

    Args:
        _url (str): the complete url including root and path

    Returns:
        requests.Response: a Response type object from the requests library
    """

    return requests.get(_url)


"""
def form_post_request(_url):

def send_post_request(_url):
"""
