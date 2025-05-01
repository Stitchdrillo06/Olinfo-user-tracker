
Rem Pull data from https://github.com/olimpiadi-informatica/stats git repository, specifically perform a sparse checkout from ./data/users subfolder

if exist data\ (

   cd data

   git pull origin master

) else (

   md data
   cd data

   git init

   git remote add origin https://github.com/olimpiadi-informatica/stats

   git sparse-checkout init
   git sparse-checkout set data/users

   git fetch --depth=1 origin master
   git checkout main

   git pull origin master

)

cd ..

Rem launch python script for data organization and conversion

python main.py

Rem Import the csv created by the python script as a DB table in db.sqlite

sqlite3.exe "./db.sqlite" < "./importcsv.sql"
