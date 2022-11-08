import requests
import time;
import gzip
import shutil
import os




gmt = time.gmtime()
gmt_year = str(gmt.tm_year)
if gmt.tm_mday < 1:
    if gmt.tm_mon < 11:
        gmt_month = "0"+str(gmt.tm_mon -1)
    else:
        gmt_month = str(gmt.tm_mon -1)


    if gmt.tm_mday < 10:
        gmt_day = "0"+str(gmt.tm_mday)
    else:
        gmt_day = str(gmt.tm_mday)


    if gmt.tm_hour < 10:
        gmt_time = "0"+str(gmt.tm_hour)
    else:
        gmt_time = str(gmt.tm_hour)
else:
    if gmt.tm_mon < 10:
        gmt_month = "0"+str(gmt.tm_mon)
    else:
        gmt_month = str(gmt.tm_mon)


    if gmt.tm_mday < 10:
        gmt_day = "0"+str(gmt.tm_mday - 1)
    else:
        gmt_day = str(gmt.tm_mday - 1)


    if gmt.tm_hour < 10:
        gmt_time = "0"+str(gmt.tm_hour)
    else:
        gmt_time = str(gmt.tm_hour)

download_file = "https://data.gharchive.org/2015-01-01-15.json.gz"
download_file_Update = "https://data.gharchive.org/" + gmt_year +"-" + gmt_month + "-" + gmt_day + "-" + gmt_time + ".json.gz"
print (download_file_Update)



# Downloading file

r = requests.get(download_file_Update, stream = True)
with open("./data/downloadedFile.json.gz","wb") as f:
    for chunk in r.iter_content(chunk_size=1024):
  
         # writing one chunk at a time to pdf file
         if chunk:
             f.write(chunk)


#Unzipping file

with gzip.open('./data/downloadedFile.json.gz', 'rb') as f_in:
    with open('./data/downloadedFile.json', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


print (os.listdir('./data'))
print (os.getcwd())



# Posting data to an endpoint

#url = 'fff' # endpoint for kafka, or HDFS
#files = {'file': open('downloadedFile.json', 'rb')}

#p = requests.post(url, files=files)