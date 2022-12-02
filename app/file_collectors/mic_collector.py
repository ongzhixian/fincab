from os import path

from file_collectors import AbstractFileDownloader
from logger import Logger
log = Logger()


class MicFileCollector(AbstractFileDownloader):
    def __init__(self, output_path):
        self.output_path = output_path
        self.collect_mic_csv()

    def collect_mic_csv(self):
        log.info("Collecting file", file_type="MIC CSV")
        
        save_file_path = path.join(self.output_path, "mic", "ISO10383_MIC.csv")

        response_text_data = self.download_text('https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.csv')

        self.save_text_file(response_text_data, save_file_path)
        
        log.info("Collected file", file_type="MIC CSV")
