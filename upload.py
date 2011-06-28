import ftplib                                          # We import the FTP module
#The reason MMS uses FTP is because it is a secure protocol to use to upload files. If the files could be edited publicly, hackers would start "griefing" the server.
session = ftplib.FTP('FTP Domain','FTP Username','FTP Passsword') # Connect to the FTP server
session.cwd("Folder where files are stored") #This command is optional, it's only if the FTP account root folder doesn't house the current.zip file.
myfile = open('current.zip','rb')                         # Open the file to send
session.storbinary('STOR current.zip', myfile)            # Send the file
myfile.close()                                         # Close the file
session.quit()                                         # Close FTP session
