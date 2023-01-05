import pymongo
import os

myclient = pymongo.MongoClient("mongodb://scraperProd:mqCCwVtv4dw3ec76@mongo-db.advarisk.com:27110/?ssl=true")
# mydb = myclient["scrape_data"]
# temp = mydb["wb_data"]
# main = mydb["wb_igr"]
# main_copy = mydb["wb_igr_copy"]

# **************************************add status 1 in temp coll*******************************************

# myquery = {}
# newvalues = { "$set": { "mongodb_status":0 } }
# x = temp.update_many(myquery, newvalues)
# print(x.modified_count, "documents updated.")

# ***************************************export data from temporary collection*****************************

# os.system('mongoexport -u administrator -p ufQyqR9xF9BG8jdm --authenticationDatabase admin --port 27110 --ssl --host mongo-db.advarisk.com --db scrape_data --collection wb_data --out wb_data.json')

# ***************************************copy main collection*********************************************

# mydb.wb_igr.aggregate([{'$match':{} },{'$out':"wb_igr_copy"}])


# ***************************************make old data status 0*******************************************

# query = {}
# values = { "$set": { "mongo_status": 0 } }
# y = main.update_many(query, values)
# print(y.modified_count, "documents updated.")


# *************************************create index in main copy collection********************************

# mydb.mp_meta_data_copy.create_index('district_code')
# mydb.mp_meta_data_copy.create_index('taluka_code')
# mydb.wb_igr.create_index('unique_key')
# mydb.mp_meta_data_copy.create_index('village_code')
# mydb.mp_meta_data_copy.create_index('migration_info.migrated')
# mydb.mp_meta_data_copy.create_index('status')


# *************************************importing data in main collection***********************************

os.system('mongoimport -u administrator -p ufQyqR9xF9BG8jdm --authenticationDatabase admin --port 27110 --ssl --host mongo-db.advarisk.com --db scrape_data --collection wb_igr --file wb_data.json')


# *************************************drop main copy collection********************************************

# main.drop()

# *************************************rename collection****************************************************

# mydb.mp_meta_data_copy.rename('mp_meta_data')










