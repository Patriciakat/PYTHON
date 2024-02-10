import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["restaurant_database"]
collection = db["restaurants"]

# Read JSON data from file and insert into MongoDB
with open("C://Users//37060//Desktop//PYTHON//restaurants.json") as file:
    for line in file:
        data = json.loads(line)
        collection.insert_one(data)

# 2. Parašykite užklausą, atvaizduojančią visus dokumentus iš restoranų rinkinio
all_doc = collection.find()
for data in all_doc:
    print(data)

# 3. Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine - visiems dokumentams
specific_fields = collection.find({}, {"restaurant_id" : 1, "name" : 1, "borough" : 1, "cuisine" : 1})
for data in specific_fields:
    print(data)

# 4. Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine -, bet nerodytų lauko _id visiems dokumentams
specific_fields = collection.find({}, {"_id" : 0, "restaurant_id" : 1, "name" : 1, "borough" : 1, "cuisine" : 1})
for data in specific_fields:
    print(data)

# 5. Parašykite užklausą, kuri parodytų visus miestelio Bronx restoranus
bronx_restaurants = collection.find({"borough" : 'Bronx'})
for data in bronx_restaurants:
    print(data)

# 6. Parašykite užklausą, kuri parodytų restoranus su įvertinimu tarp 80 ir 100 (duomenis gali reikėti agreguoti).
between_80_and_100 = collection.aggregate([
    {"$unwind": "$grades"},
    {"$match": {"grades.score": {"$gte": 80, "$lte": 100}}},
    {"$group": {"_id": "$_id", "restaurant_id": {"$first": "$restaurant_id"},
                "name": {"$first": "$name"}, "borough": {"$first": "$borough"},
                "cuisine": {"$first": "$cuisine"}}}
])
for restaurant in between_80_and_100:
    print(restaurant)

# 7. Parašykite užklausą, kad cuisine būtų išdėstyta didėjimo tvarka, o borough - mažėjimo.
sorted_restaurants = collection.find().sort([("cuisine", 1), ("borough", -1)])
for restaurant in sorted_restaurants:
    print(restaurant)
