import urllib.request
...
# Download the file from `url` and save it locally under `file_name`:
urllib.request.urlretrieve("http://google.com", "backup.txt")
