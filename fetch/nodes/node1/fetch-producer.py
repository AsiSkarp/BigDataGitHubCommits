import requests
import time
import datetime
import gzip
import shutil
import json
import os
from kafka import KafkaProducer


yesterday = datetime.datetime.utcnow().date() - datetime.timedelta(days=1)

gmt = time.gmtime()
gmt_year = str(gmt.tm_year)
gmt_time = str(gmt.tm_hour)

if gmt.tm_mon < 10:
    gmt_month = "0" + str(yesterday.month)
else:
    gmt_month = str(yesterday.month)

if gmt.tm_mday < 10:
    gmt_day = "0" + str(yesterday.day)
else:
    gmt_day = str(yesterday.day)

# download_file = "https://data.gharchive.org/2015-01-01-15.json.gz"
download_file = (
    "https://data.gharchive.org/"
    + gmt_year
    + "-"
    + gmt_month
    + "-"
    + gmt_day
    + "-"
    + gmt_time
    + ".json.gz"
)

# download the file and get the path to it
r = requests.get(download_file, allow_redirects=True)
open("data.json.gz", "wb").write(r.content)

# unzip the file
with gzip.open("data.json.gz", "rb") as f_in:
    with open("data.json", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

# delete the zip file
os.remove("data.json.gz")

# send the data to kafka
with open("data.json", encoding="utf-8") as f:
    producer = KafkaProducer(bootstrap_servers="bddst-g04-Node1.uvm.sdu.dk:9092")
    for line in f:
        producer.send("alice-test", line.encode("utf-8"))
