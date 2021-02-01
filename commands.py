from globals import config
import sqlalchemy as sa
from flask import Flask


def create_engine():
	return sa.create_engine(config.DATABASE_URL)


def register_commands(app: Flask):

	@app.cli.command('load_data')
	def load_data():
		engine = create_engine()
		try:
			engine.execute( """ LOAD DATA LOCAL INFILE  "./ml-latest-small/movies.csv" into table movies FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;  """)
			engine.execute(""" LOAD DATA LOCAL INFILE  "./ml-latest-small/tags.csv" into table tags FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;  """)
			engine.execute(""" LOAD DATA LOCAL INFILE  "./ml-latest-small/ratings.csv" into table ratings FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES;  """)
		except Exception as e:
			print(e)
