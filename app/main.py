import json
import logging

from datetime import datetime
from os import path
from urllib.parse import quote
from urllib.request import urlopen as url_open
from urllib.request import Request as url_request

from logger import Logger
from oanda_api import OandaApi

from file_collectors.mic_collector import MicFileCollector

def setup_logging():
    logging.getLogger('pika').setLevel(logging.WARNING)
    log = Logger()
    return log

def collect_mic():
    log.info("Collect file", file_type="MIC CSV")

if __name__ == "__main__":
    log = setup_logging()

    # (url_parameters, database_settings, oanda_settings, output_path) = get_settings_from_arguments()
    # oanda_api = OandaApi(oanda_settings, output_path)
    # trading_instruments = oanda_api.get_account_instruments()
    # store_account_instruments_to_database(trading_instruments)
    # instrument_code_list = get_instrument_code_list(trading_instruments)
    # publish_tickers(url_parameters, instrument_code_list)

    output_path = '../output'

    MicFileCollector(output_path)

    log.info("Program complete", source="program", event="complete")