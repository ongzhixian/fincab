from os import path, makedirs
from urllib.request import urlopen as url_open
from urllib.request import Request as url_request

from logger import Logger
log = Logger()

class AbstractFileDownloader(object):
    def download_text(self, url):
        request = self.make_url_request(url)
        with url_open(request) as response:
            response_data = response.read()
        return response_data

    def make_url_request(self, url):
        return url_request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
            }
        )

    def save_text_file(self, data, file_path_name):
        self.ensure_file_path_directory_exists(file_path_name)
        with open(file_path_name, 'wb') as out_file:
            out_file.write(data)

    def ensure_file_path_directory_exists(self, file_path_name):
        file_dir_name = path.dirname(file_path_name)
        makedirs(file_dir_name, exist_ok=True)