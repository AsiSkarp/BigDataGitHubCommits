FROM postgres:latest

COPY hive-schema-2.3.0.postgres.sql /hive/hive-schema-2.3.0.postgres.sql
COPY hive-txn-schema-2.3.0.postgres.sql /hive/hive-txn-schema-2.3.0.postgres.sql

COPY init-hive-db.sh /docker-entrypoint-initdb.d/init-user-db.sh
