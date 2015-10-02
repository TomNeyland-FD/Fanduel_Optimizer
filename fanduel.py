from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///db_files/NFL.db')
engine.echo = False


Session = sessionmaker(bind=engine)



class PlayerInfo(Base):
	__tablename__ = 'player_info'
	id = Column(Integer, primary_key=True)
	player_id = Column(Integer)	
	firstname = Column(String)
	lastname = Column(String)
	salary = Column(Integer)
	position = Column(String)
	projected_points = Column(Integer)


Base.metadata.create_all(engine) 


session = Session()

import csv

def create_players(player_dicts):
	for player in player_dicts: 
		player_info = PlayerInfo(player_id=player['Id'],
		firstname=player['First Name'],
		lastname=player['Last Name'],
		salary=player['Salary'],
		position=player['Position'],
		projected_points=player['FPPG'])
		session.add(player_info)

with open('player_info.csv','rb') as csvfile:
	reader = csv.DictReader(csvfile)
	create_players(reader)


session.commit()



###below is temporary

#HELLO sqlite! 
#for position in positions: #I guess i need to define positions array or whatever you call those [postiona,positionb]
#	"Give me player WHERE 'position' = "+position+" AND 'salary' is MIN;"

player_positions = ['QB', 'RB', 'RB', 'WR', 'WR', 'WR', 'TE', 'K', 'D']

for player_position in player_positions:
	for terrible_player in session.query(PlayerInfo.id, PlayerInfo.firstname, PlayerInfo.lastname, func.min(PlayerInfo.salary), PlayerInfo.position).\
    	filter(PlayerInfo.salary < 5000).\
    	filter(PlayerInfo.position = player_position): 
			print terrible_player.firstname, terrible_player.lastname, terrible_player.salary, terrible_player.position






















