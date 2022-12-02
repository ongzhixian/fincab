from os import path

from urllib.request import urlopen as url_open
from urllib.request import Request as url_request

from file_collectors import AbstractFileDownloader
from logger import Logger
log = Logger()


class NasdaqCollector(AbstractFileDownloader):

    def __init__(self, output_path):

        self.output_path = output_path

        self.collect_nasdaq_json()
        
        

    def collect_nasdaq_json(self):

        FILE_TYPE = "NASDAQ JSON"

        log.info("Collecting file", file_type=FILE_TYPE)
        
        save_file_path = path.join(self.output_path, "symbols", "NASDAQ.json")

        if path.exists(save_file_path):
            log.info("Skip collecting file", file_type=FILE_TYPE)
            return

        # GET /api/screener/stocks?download=true HTTP/2
        # Host: api.nasdaq.com
        # User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0
        # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
        # Accept-Language: en-US,en;q=0.5
        # Accept-Encoding: gzip, deflate, br
        # Connection: keep-alive
        # Upgrade-Insecure-Requests: 1
        # Sec-Fetch-Dest: document
        # Sec-Fetch-Mode: navigate
        # Sec-Fetch-Site: none
        # Sec-Fetch-User: ?1
        # TE: trailers

        # response_data = self.download('https://api.nasdaq.com/api/screener/stocks')

        request = url_request(
            'https://api.nasdaq.com/api/screener/stocks?exchange=NYSE&download=true&tableonly=true', 
            data=None, 
            headers={
                'Host': 'api.nasdaq.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive'
            }
        )

        log.info("Opening request")
        with url_open(request) as response:
            response_data = response.read()

        log.info("Saving request")
        self.save_data_to_file(response_data, save_file_path)
        
        log.info("Collected file", file_type=FILE_TYPE)
