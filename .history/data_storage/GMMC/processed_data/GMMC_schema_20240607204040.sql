-- Step 1: Alter the existing table to drop the "Is Compliance Sample" column
-- ALTER TABLE "GMMC-2020-M" DROP COLUMN "Is Compliance Sample";



-- Step 3: Create the new tables

-- Create the location table
-- CREATE TABLE location (
--     Location_ID INTEGER PRIMARY KEY AUTOINCREMENT,
--     Sampling_Point_Notation TEXT NOT NULL UNIQUE,
--     Sampling_Point_Label TEXT NOT NULL,
--     Easting INTEGER,
--     Northing INTEGER
-- );

-- -- Create the determinand table
-- CREATE TABLE determinand (
--     Determinand_ID INTEGER PRIMARY KEY AUTOINCREMENT,
--     Determinand_Label TEXT NOT NULL,
--     Determinand_Definition TEXT,
--     Determinand_Notation TEXT
-- );

-- -- Create the sampling_data table
-- CREATE TABLE sampling_data (
--     ID TEXT PRIMARY KEY,
--     Location_ID INTEGER NOT NULL,
--     Determinand_ID INTEGER NOT NULL,
--     Sample_Date_and_Time DATETIME NOT NULL,
--     Result REAL,
--     Unit TEXT,
--     Sample_Material_Type TEXT,
--     Is_Compliance_Sample BOOLEAN,
--     Sample_Purpose TEXT,
--     FOREIGN KEY (Location_ID) REFERENCES location(Location_ID),
--     FOREIGN KEY (Determinand_ID) REFERENCES determinand(Determinand_ID)
-- );


-- -- Step 4: Insert unique locations into the location table
-- INSERT INTO location (Sampling_Point_Notation, Sampling_Point_Label, Easting, Northing)
-- SELECT DISTINCT 
--     Sampling_Point_Notation, 
--     Sampling_Point_Label, 
--     Easting, 
--     Northing
-- FROM "GMMC-2020-M";

-- -- Step 5: Insert unique determinands into the determinand table
-- INSERT INTO determinand (Determinand_Label, Determinand_Definition, Determinand_Notation)
-- SELECT DISTINCT 
--     Determinand_Label, 
--     Determinand_Definition, 
--     Determinand_Notation
-- FROM "GMMC-2020-M";

-- -- Step 6: Insert data into the sampling_data table
-- INSERT INTO sampling_data (
--     ID,
--     Location_ID,
--     Determinand_ID,
--     Sample_Date_and_Time,
--     Result,
--     Unit,
--     Sample_Material_Type,
--     Is_Compliance_Sample,
--     Sample_Purpose
-- )
-- SELECT 
--     gm.ID,
--     loc.Location_ID,
--     det.Determinand_ID,
--     gm.Sample_Date_and_Time,
--     gm.Result,
--     gm.Unit,
--     gm.Sample_Material_Type,
--     gm.Is_Compliance_Sample,
--     gm.Sample_Purpose
-- FROM "GMMC-2020-M" gm
-- JOIN location loc ON gm.Sampling_Point_Notation = loc.Sampling_Point_Notation
-- JOIN determinand det ON gm.Determinand_Label = det.Determinand_Label;

.tables

-- Step 2: Select the first 5 rows to verify the current table structure
SELECT * FROM "GMMC-2020-M" LIMIT 5;

SELECT * FROM location LIMIT 5;

SELECT * FROM "determinand" LIMIT 5;

SELECT * FROM sampling_data LIMIT 5;