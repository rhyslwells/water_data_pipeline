SELECT * FROM location LIMIT 5;

-- -- Retrieve all sampling data for a specific location
-- SELECT sd.*, loc.Sampling_Point_Label
-- FROM sampling_data sd
-- JOIN location loc ON sd.Location_ID = loc.Location_ID
-- WHERE loc.Sampling_Point_Notation = 'NewPoint';

-- -- Retrieve all results for a specific determinand
-- SELECT sd.*, det.Determinand_Label
-- FROM sampling_data sd
-- JOIN determinand det ON sd.Determinand_ID = det.Determinand_ID
-- WHERE det.Determinand_Label = 'New Determinand';

-- -- Aggregate data to find the average result for each determinand
-- SELECT det.Determinand_Label, AVG(sd.Result) AS Average_Result
-- FROM sampling_data sd
-- JOIN determinand det ON sd.Determinand_ID = det.Determinand_ID
-- GROUP BY det.Determinand_Label;
