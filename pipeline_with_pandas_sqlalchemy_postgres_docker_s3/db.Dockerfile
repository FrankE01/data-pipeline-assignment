FROM library/postgres
COPY ./initdb/init.sql /docker-entrypoint-initdb.d/
