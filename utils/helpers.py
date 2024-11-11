import datetime
from datetime import timezone
import yaml
from pathlib import Path
import os

def saveConfig(fileName: str(), data: dict()) -> None:
	formattedPath = Path("config/" + fileName) #Converts file path to OOP path
	if formattedPath.exists():
		formattedPath.unlink()
		print("Config file has been deleted for replacement [saveConfig]")
	
	with open(formattedPath, "w") as file:
		yaml.dump(data,file)
		print("Written config file [saveConfig]")
		
def loadConfig(fileName: str()) -> dict():
	data = dict() #variable used to store config from file
	formattedPath = Path("config/" + fileName)	#Converts file path to OOP path
	if formattedPath.exists():
		with open(formattedPath, "r") as file:
			data = yaml.safe_load(file)
			print("Data loaded from config for " + fileName + " successfully [loadConfig]")
	else:
		print("Config file does not exist [loadConfig]")
		
	return data
	
def saveCache(fileName: str(), dirName: str(), data: dict()) -> None:
	formattedPath = Path("cache/" + dirName + "/" + fileName)
	cachePath = Path("cache/" + dirName)
	if dirName not in os.listdir("cache"):
		os.mkdir(cachePath)
		
	with open(formattedPath, "w") as file:
		yaml.dump(data,file)
		print("Wrote cache file " + fileName + " [saveCache]")
		
def loadCache(fileName: str(), dirName: str()) -> dict():
	data = dict() #variable used to store config from file
	path = Path("cache/" + dirName + "/" + fileName)
	
	if path.exists():
		with open(path, "r") as file:
			data = yaml.safe_load(file)
			print("Data loaded from " + str(path) + " [loadCache]")
	else:
		print("Error: Data was not able to be loaded from " + str(path) + " [loadCache]")
		
	return data
	
def getTimeStamp(value: datetime = None):
	#Generate current time object
	now = datetime.datetime.now()
	if value == None:
		unix_timestamp = int(now.timestamp())
	else:
		unix_timestamp = int(value.timestamp())

	discord_timestamp = f"<t:{unix_timestamp}:f>"

	return discord_timestamp

def convertTime(date: str() = None) -> datetime:
	fields = list()
	data = None

	if "/" in date:
		fields = date.split("/")
	elif "-" in date:
		fields = date.split("-")
	else:
		print("Error: Invalid time formate given [helpers::convertTime]")

	try:
		#takes year month day as args
		data = datetime.datetime(int(fields[0]), int(fields[1]), int(fields[2]), tzinfo=timezone.utc)
	except:
		print("Error: Unable to create datetime object [helpers::convertTime]")

	return data
	
def checkAuth(author) -> bool():
	authorizedRoles = ["moderator", "team leader"] #CHECK LATER WHEN MORE ROLES ARE ADDED
			
	for role in author.roles:
		if str(role).lower() in authorizedRoles:
			return True
			
	return False
