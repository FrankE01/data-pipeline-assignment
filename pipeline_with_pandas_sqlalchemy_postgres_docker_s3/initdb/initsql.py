import os

data_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/data/"

companies = [d for d in os.listdir(data_folder) if os.path.isdir(data_folder+d)]

init_sql = ""
create_query = "CREATE DATABASE "

for directory in companies:
    full_query = create_query + directory + ";\n"
    init_sql += full_query

file = open("init.sql", "w")
file.write(init_sql)
file.close()