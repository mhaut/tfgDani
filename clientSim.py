
import ast
import json
import time
import urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from PyQt4 import QtCore


class FileThread(QtCore.QThread):
	def __init__(self,pathFiles=None,fileName=None):
		QtCore.QThread.__init__(self, None)
		self.jsonImageSim = '{"md5":"1307e461d318b42fce286ba3e9cf9f43","metadata":{"X Resolution":"72 dots per inch","Y Resolution":"72 dots per inch","Resolution Unit":"Inch","Model":"Nexus 5","Date/Time":"2016:04:16 01:08:23","Image Height":"2448 pixels","Image Width":"3264 pixels","File Name":"JPEG_20160416_010818_1525679884.jpg","File Size":"1844706 bytes",},"location":{"lat":"39.45921064","lng":"-6.38312189"},"tags":[{"name":"cojin"},{"name":"salon"}]}'
		self.ipDirection = "http://localhost:12342"
		self.fileUpload = pathFiles+fileName

	def setProcessImageCounter(self, counter):
		self.cont = counter

	def __del__(self):
		self.wait()

	def run(self):
		# Register the streaming http handlers with urllib2
		register_openers()
		datagen, headers = multipart_encode({"picture": open(self.fileUpload, "rb")})
		# Create the Request object
		request = urllib2.Request(self.ipDirection+"/photo", datagen, headers)
		urllib2.urlopen(request)

		req = urllib2.Request(self.ipDirection+"/json")
		req.add_header('Content-Type', 'application/json')
		response = urllib2.urlopen(req, json.dumps(ast.literal_eval(self.jsonImageSim)))
		print "ENVIADO"
		self.terminate()


if __name__ == '__main__':
	filesInPackage = 1
	jsonPkgSim   = '{"session": {"date": "01072016,19:16","model": "Nexus5","location": {"lat": "39.4783691","lng": "-6.3421245"},"id": "1467393396324","name": "nombredelpaquete"}}'
	allThreads = [None for i in range(filesInPackage)]

	for i in range(filesInPackage):
		allThreads[i] = FileThread(pathFiles="gatitos/",fileName="gatitos"+str(i)+".jpg")

	for i in range(filesInPackage):
		if allThreads[i].isRunning() == False:
			print "Arrancando hilo", i, "imagen", cont
			allThreads[i].start()

	while True:
		running = 0
		for i in range(len(allThreads)):
			running += allThreads[i].isRunning()
		if running == 0: # 
			break

	req = urllib2.Request("http://localhost:12342/json")
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(ast.literal_eval(jsonPkgSim)))
	print "TODO SUBIDO"