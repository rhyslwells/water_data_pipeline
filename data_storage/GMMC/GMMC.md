GMMC: Greater Manchester, Merseyside, and Cheshire
## Summary

We have collected monitoring data spanning from the years 2020 to 2024 for the Greater Manchester, Merseyside, and Cheshire regions. This data was obtained from the Water Quality Archive, accessible at https://environment.data.gov.uk/water-quality/view/landing.

About this service:

The Water Quality Archive offers comprehensive data on water quality measurements. Samples are systematically collected from various sampling points across England, encompassing coastal or estuarine waters, rivers, lakes, ponds, canals, or groundwaters. These samples serve multiple purposes, including compliance assessment against discharge permits, investigation of pollution incidents, or environmental monitoring. The dataset exclusively includes complete samples, indicating instances where all analyses have been conducted. Currently, the dataset does not encompass all groundwater or third-party data.

For developers and researchers, there is an API available to access the water quality data. For detailed documentation and reference, please visit: https://environment.data.gov.uk/water-quality/view/doc/reference#api-data-reference

## Database schema

Creating a normalized database schema by introducing additional tables for locations and determinands can improve data organization, reduce redundancy, and enhance query performance. Here is a revised schema with separate tables for `location` and `determinand`, and a main `sampling_data` table that references these.

### Schema Definition

1. **Location Table**
2. **Determinand Table**
3. **Sampling Data Table**

