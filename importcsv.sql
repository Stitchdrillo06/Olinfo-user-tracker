
-- Delete table Users

DROP TABLE IF EXISTS Users;

-- Create new Users table with specific fields

CREATE TABLE Users (

    "idx" INTEGER,
    "Best Rank" INTEGER,
    "Participations" BLOB,
    "OlinfoId" TEXT,
    "Username" TEXT,
    "First Name" TEXT,
    "Last Name" TEXT,
    "Gold" INTEGER,
    "Silver" INTEGER,
    "Bronze" INTEGER
);

-- Setup

.separator ,

.mode csv

-- Import data from out.csv in Users table

.import --skip 1 "C:/Olinfo/app/userdb/out.csv" Users
