import json
import sqlite3

from os import path

from logger import log

class CatalogBuilder(object):

    def __init__(self, output_path):

        self.output_path = output_path
        
        # Phase 1 - Build tables
        self.build_tables()
        
        # Phase 2 - Parse data and insert
        self.process_nasdaq_data()

    def build_tables(self):
        with sqlite3.connect("instruments.sqlite3") as db_connection:
            db_cursor = db_connection.cursor()
            self.create_table_sb(db_cursor)

    def create_table_sb(self, db_cursor):
        log.info("Create table", table_name="sb")
        db_cursor.execute(
            """
CREATE TABLE IF NOT EXISTS "sb" (
    "exchange"	TEXT UNIQUE,
	"symbol"	TEXT UNIQUE,
	"name"	TEXT,
	"isin"	TEXT,
	"sedol"	TEXT,
	"cusip"	TEXT,
	"yahoo"	TEXT,
	"reuters"	TEXT,
	"bb_ticker"	TEXT,
	"bb_id"	TEXT,
	"figi"	TEXT,
	"valor"	TEXT,
	"wkn"	TEXT,
	"telekurs"	TEXT,
	"mic"	TEXT,
	"create_dt"	TEXT,
	"update_dt"	TEXT,
	PRIMARY KEY("exchange","symbol")
);""")

    def process_nasdaq_data(self):
        log.info("Process data (TODO)", data_type="nasdaq")

        data_file_path = path.join(self.output_path, 'nasdaq-stocks.json')

        log.info("Opening file", file_path=data_file_path)

        with open(data_file_path, 'r', encoding='utf-8') as in_file:
            json_data = json.load(in_file)

        if 'data' in json_data and 'rows' in json_data['data']:
            data_rows = json_data['data']['rows']
        
        insert_data = []
        for row in data_rows:
            insert_data.append((row["symbol"], row["name"], row["symbol"], row["name"]))
        with sqlite3.connect("instruments.sqlite3") as db_connection:
            db_connection.executemany(
                """INSERT INTO sb(symbol, name)
SELECT ?, ?
WHERE NOT EXISTS(SELECT 1 FROM sb WHERE symbol = ? AND name = ?);""", insert_data)