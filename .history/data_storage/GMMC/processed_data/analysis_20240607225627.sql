-- SELECT * FROM location;
SELECT * FROM determinand LIMIT 5;
-- SELECT * FROM sampling_data LIMIT 1;

-- -- Retrieve all sampling data times for a specific location
-- SELECT sd."Sample_Date_and_Time"
-- FROM sampling_data sd
-- JOIN location loc ON sd.Location_ID = loc.Location_ID
-- WHERE loc.Sampling_Point_Notation = 'NW-1130';

-- -- -- Retrieve all results for a specific determinand
-- SELECT sd.*, det.*
-- FROM sampling_data sd
-- JOIN determinand det ON sd.Determinand_ID = det.Determinand_ID
-- WHERE det.Determinand_Label = 'Sld Sus@105C'
-- -- AND sd.Location_ID = 
-- ;

-- could graph Results vs. Sample_Date_and_Time for a given location?


-- -- Aggregate data to find the average result for each determinand
SELECT det.Determinand_Label, AVG(sd.Result) AS Average_Result
FROM sampling_data sd
JOIN determinand det ON sd.Determinand_ID = det.Determinand_ID;
GROUP BY det.Determinand_Notation;
