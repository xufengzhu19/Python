import pymongo
conn=pymongo.MongoClient(host='localhost', port=27017)
db=conn.spiderdb
myset=db.t1
myset.insert_one()