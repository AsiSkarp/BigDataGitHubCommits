# BigDataGitHubCommits
7. Semester group project. 


## How to connect to HDFS and Hive
### HDFS
Connect to the hdfs container with: "docker exec -ti x bash"
x is the name of the namenode container (in our case namenode)

### Hive
Connect to the hive container with: "docker exec -ti x beeline"
x is the name of the namenode container (in our case hive-server)
Once inside, we need to connect to hive. This is done by: "!connect jdbc:hive2://localhost:10000". After this you will be prompted with the username and password before connecting