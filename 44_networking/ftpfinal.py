import os
import pysftp
sftp =  pysftp.Connection('192.168.159.131', username='user', password='password')

sftp.cd('/home/user/Desktop')

# ftp the hello.csv to the remote home directory

sftp.put('/home/user/Desktop/hello.csv')

