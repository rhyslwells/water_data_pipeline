
## Notes

Future proofing.
Standards in code.
Understand the requirements to ensure longevity.
Flexible: Can take on many roles: Programming, Existing tools, analytics, Data migration. Software engineer.
Lots of tools to learn: Tech is changing.
Maintainable code.
Source of true - syncing issues - use a data warehouse.
Data workflow - design.
Version control design.
Good to understand when data needs to be ready for reports.
Optimising queries for speed. 

### Gathering data from clients

Understanding business requirements.

1) Get problem statement. What do you want. Overlap of business and technical techniques
	1) Ask WHY: 
	2) How often is this report, who is it for. Need to understand what they need.
2) During asking why: Get an understanding of the business case. What decisions are being made from the data.
	1) Need to understand the problems. What does success look like. What needs to exist.
3) Who are the stakeholders. What are you going to do with the data. Is it important enough to do.
4) What is the value added.

### Vocab of data engineer

DAG: Direct acyclic graph: 
Data Pipeline: Bath ETL pipeline
data warehouse: Ridgid schema: model of buisness: so can ask questions of multiple systems. Historical queries:
FACTS, Dimensions
Slowly changing dimensions : change of historical data.
SLA : Service level agreement: commitemtn between client and provider. 

Data Lake: Storing raw data: Less structured: Cost / time requirement to model into data warehouse. 



### Small business notes:
1. Their data is likely going to be messier than what you're used to
    
2. You will have to give them recommendations even if they have an internal "IT guy" as they might not have the right expertise.
    
3. Be wary of any data models they produce -- you need to reexamine them under a microscope because oftentimes clients will require things that are inefficient given the data model they have provided
    
4. Manage their expectations and let them know that developing data pipelines is no easy feat especially because you are likely to be the only DE they have contracted. It will take time and money.





