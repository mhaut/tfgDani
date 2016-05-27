
import ast
import json
import urllib2


jsonSim = '{"md5":"1307e461d318b42fce286ba3e9cf9f43","metadata":{"X Resolution":"72 dots per inch","Y Resolution":"72 dots per inch","Resolution Unit":"Inch","Model":"Nexus 5","Date/Time":"2016:04:16 01:08:23","Image Height":"2448 pixels","Image Width":"3264 pixels","File Name":"JPEG_20160416_010818_1525679884.jpg","File Size":"1844706 bytes",},"location":{"lat":"39.45921064","lng":"-6.38312189"},"tags":[{"name":"cojin"},{"name":"salon"}]}'



req = urllib2.Request('http://localhost:12342/json')
req.add_header('Content-Type', 'application/json')
for i in range(10000):
    response = urllib2.urlopen(req, json.dumps(ast.literal_eval(jsonSim)))