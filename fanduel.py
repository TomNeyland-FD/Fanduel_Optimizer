from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, func, asc
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



player_positions = ['QB', 'RB', 'WR', 'TE', 'K', 'D']
for player_position in player_positions:
	if player_position == 'RB':
		for terrible_player in session.query(PlayerInfo.id, PlayerInfo.firstname, PlayerInfo.lastname, PlayerInfo.salary, PlayerInfo.position).\
    		filter(PlayerInfo.position == player_position).\
    		order_by(PlayerInfo.salary.asc()).\
    		limit(2):
				print terrible_player.firstname, terrible_player.lastname, terrible_player.position, terrible_player.salary
	

	elif player_position == 'WR':			
		for terrible_player in session.query(PlayerInfo.id, PlayerInfo.firstname, PlayerInfo.lastname, PlayerInfo.salary, PlayerInfo.position).\
    		filter(PlayerInfo.position == player_position).\
    		order_by(PlayerInfo.salary.asc()).\
    		limit(3):
				print terrible_player.firstname, terrible_player.lastname, terrible_player.position, terrible_player.salary


	else:			
		for terrible_player in session.query(PlayerInfo.id, PlayerInfo.firstname, PlayerInfo.lastname, func.min(PlayerInfo.salary).label("salary"), PlayerInfo.position).\
    		filter(PlayerInfo.position == player_position):
				print terrible_player.firstname, terrible_player.lastname, terrible_player.position, terrible_player.salary


















