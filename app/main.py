from logger import setup_logging

from file_collectors.mic_collector import MicFileCollector
from file_collectors.nasdaq_collector import NasdaqCollector

if __name__ == "__main__":

    log = setup_logging()

    output_path = '../output'

    MicFileCollector(output_path)
    # NasdaqCollector(output_path)
    

    log.info("Program complete", source="program", event="complete")