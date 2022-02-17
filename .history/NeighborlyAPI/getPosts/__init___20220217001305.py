import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://neighborlyappcdb:bZOrwNtxyzVfuY6vUAkhVYc13GrFbLXKSuYcKnxLKzd9PrhYAY63geOF5YT1U7ddghwhk8l3CD7wVrqsicINmg==@neighborlyappcdb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborlyappcdb@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['neighborlyappdb']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)