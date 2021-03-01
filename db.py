from pymongo import MongoClient
from umongo.frameworks import PyMongoInstance

# connect to the mongo database on our local machine
client = MongoClient(host="localhost", port=27017)

# we are defining the database we are going to be using
db = client["junior_design"]

# create the instance of the umongo db connection
instance = PyMongoInstance(db)
