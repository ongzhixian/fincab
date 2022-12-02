from logger import setup_logging

from file_collectors.mic_collector import MicFileCollector
from file_collectors.nasdaq_collector import NasdaqCollector
from catalog_builder import CatalogBuilder

if __name__ == "__main__":

    log = setup_logging()

    output_path = '../output'

    # Phase 1: Collect data

    # MicFileCollector(output_path)
    # NasdaqCollector(output_path)

    # Phase 2: ETL data to sqlite database
    catalog = CatalogBuilder(output_path)
    
    log.info("Program complete", source="program", event="complete")