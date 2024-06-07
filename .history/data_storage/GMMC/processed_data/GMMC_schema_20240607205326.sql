-- Step 1: Verify the current table structure by selecting the first 5 rows
-- SELECT * FROM "GMMC-2020-M" LIMIT 5;

-- Step 2: Create the new tables

-- Drop the tables if they already exist
DROP TABLE IF EXISTS location;
-- Create the location table
CREATE TABLE location (
    Location_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Sampling_Point_Notation TEXT NOT NULL UNIQUE,
    Sampling_Point_Label TEXT NOT NULL,
    Easting INTEGER,
    Northing INTEGER
);

-- Drop the tables if they already exist
DROP TABLE IF EXISTS determinand;
-- Create the determinand table
CREATE TABLE determinand (
    Determinand_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Determinand_Label TEXT NOT NULL,
    Determinand_Definition TEXT,
    Determinand_Notation TEXT
);

-- Drop the tables if they already exist
DROP TABLE IF EXISTS sampling_data;
-- Create the sampling_data table
CREATE TABLE sampling_data (
    ID TEXT PRIMARY KEY,
    Location_ID INTEGER NOT NULL,
    Determinand_ID INTEGER NOT NULL,
    Sample_Date_and_Time DATETIME NOT NULL,
    Result REAL,
    Unit TEXT,
    Sample_Material_Type TEXT,
    Is_Compliance_Sample BOOLEAN,
    Sample_Purpose TEXT,
    FOREIGN KEY (Location_ID) REFERENCES location(Location_ID),
    FOREIGN KEY (Determinand_ID) REFERENCES determinand(Determinand_ID)
);

-- Step 3: Insert unique locations into the location table
INSERT INTO location (Sampling_Point_Notation, Sampling_Point_Label, Easting, Northing)
SELECT DISTINCT 
    "Sampling Point Notation", 
    "Sampling Point Label", 
    Easting, 
    Northing
FROM "GMMC-2020-M";

-- Verify insertion into location table
SELECT * FROM location LIMIT 5;

-- Step 4: Insert unique determinands into the determinand table
INSERT INTO determinand (Determinand_Label, Determinand_Definition, Determinand_Notation)
SELECT DISTINCT 
    "Determinand Label", 
    "Determinand Definition", 
    "Determinand Notation"
FROM "GMMC-2020-M";

-- Verify insertion into determinand table
SELECT * FROM determinand LIMIT 5;

-- Step 5: Insert data into the sampling_data table
INSERT INTO sampling_data (
    ID,
    Location_ID,
    Determinand_ID,
    Sample_Date_and_Time,
    Result,
    Unit,
    Sample_Material_Type,
    Is_Compliance_Sample,
    Sample_Purpose
)
SELECT 
    gm.ID,
    loc.Location_ID,
    det.Determinand_ID,
    gm."Sample Date and Time",
    gm.Result,
    gm.Unit,
    gm."Sample Material Type",
    gm."Is Compliance Sample",
    gm."Sample Purpose"
FROM "GMMC-2020-M" gm
JOIN location loc ON gm."Sampling Point Notation" = loc.Sampling_Point_Notation
JOIN determinand det ON gm."Determinand Label" = det.Determinand_Label;

-- Verify insertion into sampling_data table
SELECT * FROM sampling_data LIMIT 5;

-- List all tables in the database
.tables;

-- Verify the new tables
SELECT * FROM location LIMIT 5;
SELECT * FROM determinand LIMIT 5;
SELECT * FROM sampling_data LIMIT 5;
