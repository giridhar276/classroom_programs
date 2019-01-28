import pysftp

sftp =  pysftp.Connection('192.168.159.131', username='user', password='password')
sftp.cd('/home/user/Desktop/files')

sftp.get('a.txt') 
