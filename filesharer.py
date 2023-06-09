from filestack import Client
from constants import filestack_api_key


class FileSharer:

    def __init__(self, filepath, api_key=filestack_api_key):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
