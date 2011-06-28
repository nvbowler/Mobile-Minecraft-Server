import ftplib                                          # We import the FTP module
#The reason MMS uses FTP is because it is a secure protocol to use to upload files. If the files could be edited publicly, hackers would start "griefing" the server.
session = ftplib.FTP('FTP Domain','FTP Username','FTP Passsword') # Connect to the FTP server
session.cwd("./mcserver/")
myfile = open('current.zip','rb')                         # Open the file to send
session.storbinary('STOR current.zip', myfile)            # Send the file
myfile.close()                                         # Close the file
session.quit()                                         # Close FTP session
