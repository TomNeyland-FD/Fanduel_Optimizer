from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///db_files/NFL.db')
engine.echo = True


Session = sessionmaker(bind=engine)



class PlayerInfo(Base):
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

	def create_players(player_dicts):
		for player_dict in player_dicts: 
			player_info = PlayerInfo(id=row['Id'],
			firstname=row['First Name'],
			lastname=row['Last Name'],
			salary=row['Salary'],
			position=row['Position'],
			projected_points=row['FPPG'])
			session.add(player_info)

	with open('///player_info.csv','rb') as csvfile:
		reader = csv.DictReader(csvfile)
 		create_players(reader)
session.commit()



below is temporary

#HELLO sqlite! 
for position in positions: #I guess i need to define positions array or whatever you call those [postiona,positionb]
	"Give me player WHERE 'position' = "+position+" AND 'salary' is MIN;"




for name, fullname in session.query(player_info., player_info.fullname): 






















