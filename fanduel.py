from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///db_files/NFL.db')
engine.echo = True


Session = sessionmaker(bind=engine)



class Fanduel(Base):
	__tablename__ = 'player_info'
	id = Column(Integer, primary_key=True)
	firstname = Column(String)
	lastname = Column(String)
	salary = Column(Integer)
	position = Column(String)
	projected_points = Column(Integer)


Base.metadata.create_all(engine) 


session = Session()

import csv
with open('///player_info.csv','rb') as csvfile:
	reader = csv.DictReader(csvfile)
	def create_players(player_dicts):
		for row in reader:
			player_info = Fanduel(id=row['Id'], firstname=row['First Name'], lastname=row['Last Name'], salary=row['Salary'], position=row['Position'], projected_points=row['FPPG'])
			session.add(player_info)



session.commit()



























