#Download and place the current settings.
import urllib
##urllib.urlretrieve ("http://nvbowler.com/mcserver/current.zip", "./current.zip")
fileHandleLocal = open("current.zip","wb")
fileHandleWeb = urllib.urlopen("Zip File Location", "rb").read()
fileHandleLocal.write(fileHandleWeb)
fileHandleLocal.close()
import zipfile
fileHandle=zipfile.ZipFile("./current.zip", "r")
fileHandle.extractall("./mobile")
fileHandle.close()
print "Downloading finished. Starting server..."
