from os import path

from file_collectors import AbstractFileDownloader
from logger import Logger
log = Logger()


class MicFileCollector(AbstractFileDownloader):

    def __init__(self, output_path):

        self.output_path = output_path

        self.collect_mic_csv()
        
        self.collect_mic_excel()

    def collect_mic_csv(self):

        log.info("Collecting file", file_type="MIC CSV")
        
        save_file_path = path.join(self.output_path, "mic", "ISO10383_MIC.csv")

        if path.exists(save_file_path):
            log.info("Skip collecting file", file_type="MIC CSV")
            return

        response_data = self.download('https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.csv')

        self.save_data_to_file(response_data, save_file_path)
        
        log.info("Collected file", file_type="MIC CSV")


    def collect_mic_excel(self):

        log.info("Collecting file", file_type="MIC Excel")
        
        save_file_path = path.join(self.output_path, "mic", "ISO10383_MIC.xlsx")

        if path.exists(save_file_path):
            log.info("Skip collecting file", file_type="MIC Excel")
            return

        response_data = self.download('https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.xlsx')

        self.save_data_to_file(response_data, save_file_path)
        
        log.info("Collected file", file_type="MIC Excel")
    