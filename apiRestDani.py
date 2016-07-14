from pymongo import MongoClient
import gridfs

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
import ast

from tornado.options import define, options

# Comment this!
class Application(tornado.web.Application,dict):
    def __init__(self,conf=None):
        dataJsonConf = conf
        if dataJsonConf == None:
            print "Error: No config read"
            exit()

        handlers = [
            (r"/json", UploadJSONHandler,dict(conf=dataJsonConf)),
            (r"/photo", UploadPhotoHandler,dict(conf=dataJsonConf))
        ]

        settings = dict(
            autoescape=None,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        
        
        import os
        hostname = dataJsonConf["machineParams"]["ip"]
        response = os.system("ping -c 1 " + hostname)

        if response == 0:
            # TODO: check this!
            try:
                self.con = MongoClient(dataJsonConf["databaseParams"]["ip"], int(dataJsonConf["databaseParams"]["port"]))
                if self.con == None:
                    self.con = MongoClient("mongodb://"+dataJsonConf["databaseParams"]["uri"]+"/")
                self.dbname = self.con[dataJsonConf["databaseParams"]["name"]]
                
            except:
                print "Error: No database located with name",dataJsonConf["databaseParams"]["name"]
                exit()
        else:
            print "Error: No database located!"
            exit()
        print "STATE OK: SGBD connect"
        print "STATE OK: Database located"


# Comment this!
class UploadJSONHandler(tornado.web.RequestHandler):
    def initialize(self, conf):
        if conf == None:
            print "Error: No config read"
            exit()
        self.dataJsonConf = conf
        
    def get(self):
        self.write("Hello from uploadJson")

    def post(self):
        db = self.application.dbname
        try:
            data = str(json.loads(self.request.body.decode(self.dataJsonConf["databaseParams"]["codingJson"])))
        except:
            print  "Error: json invalid"

        d = ast.literal_eval(data)
        # TODO: check insert OK with try catch
        db[self.dataJsonConf["collections"]["jsons"]].insert(d)
        self.write("200")


# Comment this!
class UploadPhotoHandler(tornado.web.RequestHandler):
    def initialize(self, conf):
        if conf == None:
            print "Error: No config read"
            exit()
        self.dataJsonConf = conf

    def get(self):
        self.write("Hello from uploadPhoto")

    def post(self):
        picture_file = self.request.files['picture'][0]
        filepath = picture_file['filename']
	filename = filepath.split('/')
        filename = filename[len(filename)-1]
	output_file = open( filename, 'w')
        output_file.write(picture_file['body'])



def readFileConf(filename):
    json_data=open(filename).read()
    return json.loads(json_data)



if __name__ == "__main__":
    configParams = readFileConf("jsonConf.json")
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(configParams))
    http_server.dataJsonConf = configParams
    try:
        port = int(configParams["machineParams"]["port"])
    except:
        print "Error: Port must be a number!"
        exit()
    http_server.listen(port)
    print "STATE OK: Listening",configParams["machineParams"]["ip"]," at port:",configParams["machineParams"]["port"]
    tornado.ioloop.IOLoop.instance().start()
