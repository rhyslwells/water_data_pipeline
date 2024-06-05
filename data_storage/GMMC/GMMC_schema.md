CREATE TABLE SamplingPoint (
    notation VARCHAR(255) PRIMARY KEY,
    label VARCHAR(255),
    easting INT,
    northing INT
);

CREATE TABLE Determinand (
    notation VARCHAR(255) PRIMARY KEY,
    label VARCHAR(255),
    definition TEXT,
    unitLabel VARCHAR(255)
);

CREATE TABLE Sample (
    id VARCHAR(255) PRIMARY KEY,
    samplingPoint VARCHAR(255),
    sampleDateTime DATETIME,
    isComplianceSample BOOLEAN,
    purposeLabel VARCHAR(255),
    sampledMaterialTypeLabel VARCHAR(255),
    FOREIGN KEY (samplingPoint) REFERENCES SamplingPoint(notation)
);

CREATE TABLE Result (
    resultID INT PRIMARY KEY AUTO_INCREMENT,
    sampleID VARCHAR(255),
    determinandNotation VARCHAR(255),
    resultQualifierNotation VARCHAR(255),
    codedResultInterpretation VARCHAR(255),
    result FLOAT,
    FOREIGN KEY (sampleID) REFERENCES Sample(id),
    FOREIGN KEY (determinandNotation) REFERENCES Determinand(notation)
);
