# base image
FROM postgres:11.1-alpine

# run the create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
