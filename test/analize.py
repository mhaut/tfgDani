#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np
import matplotlib.pyplot as plt

#622

fp = open("log.txt")
timePhotos = np.array([])
timeJsons  = np.array([])
times      = np.array([])
typeEvents = np.array([])

for line in fp:
	line = line.strip().split(" ")
	time       = float(line[len(line)-1][:-2])
	event      = line[len(line)-3].replace("/","")
	
	times      = np.append(times,time)
	typeEvents = np.append(typeEvents,event)
	if (event == "photo"):
		timePhotos = np.append(timePhotos,time)
	elif (event == "json"):
		timeJsons  = np.append(timeJsons,time)
	else:
		print "FATAL ERROR: Type of event not found!"

print "---------------------------------------------------"
print "---------------------------------------------------"
print "Size Image: "               , os.stat('gatitos.jpg').st_size, "bytes"
print "Size Jsons Image: "         , os.stat('gatitos.json').st_size, "bytes"
print "Size Jsons Package: "       , os.stat('package.json').st_size, "bytes"
print "---------------------------------------------------"
print "Average Jsons: "            , np.average(timeJsons), "ms"
print "Standar Desviation Jsons: " , np.std(timeJsons), "ms"
print "---------------------------------------------------"
print "Average Photos: "           , np.average(timePhotos), "ms"
print "Standar Desviation Photos: ", np.std(timePhotos), "ms"
print "---------------------------------------------------"
print "---------------------------------------------------"
print "Total Average: "           , np.average(times), "ms"
print "Total Standar Desviation: ", np.std(times), "ms"
print "---------------------------------------------------"
print "---------------------------------------------------"


plt.plot(np.arange(0,timePhotos.size),timePhotos,'o',linewidth=2,color='red',label='Time')
plt.plot(np.arange(0,timePhotos.size),[np.average(timePhotos)]*timePhotos.size,'-',linewidth=2,color='blue',label='Average')
plt.title("Store Delay")
plt.xlabel("Atemps")
plt.ylabel("Delay (ms)")
plt.xlim(0,1002)
plt.grid()
#plt.show()
plt.savefig('imageStoreDelay.png')


plt.clf()
plt.plot(np.arange(0,timeJsons.size),timeJsons,'o',linewidth=2,color='red',label='Time')
plt.plot(np.arange(0,timeJsons.size),[np.average(timeJsons)]*timeJsons.size,'-',linewidth=2,color='blue',label='Average')
plt.title("JSONS Store Delay")
plt.grid()
plt.xlabel("Atemps")
plt.ylabel("Delay (ms)")
plt.xlim(0,1002)
#plt.show()
plt.savefig('jsonsStoreDelay.png')


plt.clf()
plt.plot(np.arange(0,times.size),times,'o',linewidth=2,color='red',label='Time')
plt.plot(np.arange(0,times.size),[np.average(times)]*times.size,'-',linewidth=2,color='blue',label='Average')
plt.title("JSONS and IMAGE Store Delay")
plt.grid()
plt.xlabel("Atemps")
plt.ylabel("Delay (ms)")
plt.xlim(0,1002)
#plt.show()
plt.savefig('imageAndJsonsStoreDelay.png')


labels = ['JSONS', 'Photos']
sizes = list()
totalLines = timeJsons.size + timePhotos.size
colors = ['lightskyblue', 'lightcoral']
fig = plt.figure()
ax = fig.gca()

ax.pie([100*timeJsons.size/totalLines,100-100*timeJsons.size/totalLines], labels=labels, colors=colors,
       autopct='%1.1f%%', shadow=True, startangle=90)
ax.set_title("Percent of events JSONS vs Photos")
# Set aspect ratio to be equal so that pie is drawn as a circle.
ax.set_aspect('equal')
#plt.show()
fig.savefig('percentJSONvsPhotosEvents.png')


labels          = ['JSONS', 'Photos']
sizes           = list()
totalTime       = times.sum()
totalTimeJSONS  = timeJsons.sum()
totalTimePhotos = timePhotos.sum()

colors = ['lightskyblue', 'lightcoral']
fig = plt.figure()
ax = fig.gca()
ax.pie([100*totalTimePhotos.size/totalTime,100-100*totalTimePhotos.size/totalTime], labels=labels, colors=colors,
       autopct='%1.1f%%', shadow=True, startangle=90)
ax.set_title("Percent of time by JSONS vs Photos")
# Set aspect ratio to be equal so that pie is drawn as a circle.
ax.set_aspect('equal')
#plt.show()
fig.savefig('percentJSONvsPhotosTime.png')
