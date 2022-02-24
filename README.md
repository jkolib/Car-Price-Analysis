# Data Set Details
## Origin
This data set is a collection of data on various cars sold from 1990 to 2017 and includes details such as horsepower, body style, mpg, and other points. The data was found on Kaggle can be accessed [here](https://www.kaggle.com/CooperUnion/cardataset). The data itself was sourced from Edmunds and Twitter, according to the data set's author.

## Format
The data set was originally provided as a .csv file.

## Raw Data
Some of the raw data can be seen below:

|Make|Model|Year|Engine Fuel Type|Engine HP|Engine Cylinders|Transmission Type|Driven_Wheels|Number of Doors|Market Category|Vehicle Size|Vehicle Style|highway MPG|city mpg|Popularity|MSRP
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
|BMW|1 Series M|2011|premium unleaded (required)|335|6|MANUAL|rear wheel drive|2|"Factory Tuner|Luxury|High-Performance"|Compact|Coupe|26|19|3916|46135
|BMW|1 Series|2011|premium unleaded (required)|300|6|MANUAL|rear wheel drive|2|"Luxury|Performance"|Compact|Convertible|28|19|3916|40650
|BMW|1 Series|2011|premium unleaded (required)|300|6|MANUAL|rear wheel drive|2|"Luxury|High-Performance"|Compact|Coupe|28|20|3916|36350
|BMW|1 Series|2011|premium unleaded (required)|230|6|MANUAL|rear wheel drive|2|"Luxury|Performance"|Compact|Coupe|28|18|3916|29450
|BMW|1 Series|2011|premium unleaded (required)|230|6|MANUAL|rear wheel drive|2|Luxury|Compact|Convertible|28|18|3916|34500
|BMW|1 Series|2012|premium unleaded (required)|230|6|MANUAL|rear wheel drive|2|"Luxury|Performance"|Compact|Coupe|28|18|3916|31200
|BMW|1 Series|2012|premium unleaded (required)|300|6|MANUAL|rear wheel drive|2|"Luxury|Performance"|Compact|Convertible|26|17|3916|44100
|BMW|1 Series|2012|premium unleaded (required)|300|6|MANUAL|rear wheel drive|2|"Luxury|High-Performance"|Compact|Coupe|28|20|3916|39300
|BMW|1 Series|2012|premium unleaded (required)|230|6|MANUAL|rear wheel drive|2|Luxury|Compact|Convertible|28|18|3916|36900
|BMW|1 Series|2013|premium unleaded (required)|230|6|MANUAL|rear wheel drive|2|Luxury|Compact|Convertible|27|18|3916|37200
|BMW|1 Series|2013|premium unleaded (required)|300|6|MANUAL|rear wheel drive|2|"Luxury|High-Performance"|Compact|Coupe|28|20|3916|39600
|BMW|1 Series|2013|premium unleaded (required)|230|6|MANUAL|rear wheel drive|2|"Luxury|Performance"|Compact|Coupe|28|19|3916|31500
|BMW|1 Series|2013|premium unleaded (required)|300|6|MANUAL|rear wheel drive|2|"Luxury|Performance"|Compact|Convertible|28|19|3916|44400
|BMW|1 Series|2013|premium unleaded (required)|230|6|MANUAL|rear wheel drive|2|Luxury|Compact|Convertible|28|19|3916|37200
|BMW|1 Series|2013|premium unleaded (required)|230|6|MANUAL|rear wheel drive|2|"Luxury|Performance"|Compact|Coupe|28|19|3916|31500
|BMW|1 Series|2013|premium unleaded (required)|320|6|MANUAL|rear wheel drive|2|"Luxury|High-Performance"|Compact|Convertible|25|18|3916|48250
|BMW|1 Series|2013|premium unleaded (required)|320|6|MANUAL|rear wheel drive|2|"Luxury|High-Performance"|Compact|Coupe|28|20|3916|43550
|Audi|100|1992|regular unleaded|172|6|MANUAL|front wheel drive|4|Luxury|Midsize|Sedan|24|17|3105|2000
|Audi|100|1992|regular unleaded|172|6|MANUAL|front wheel drive|4|Luxury|Midsize|Sedan|24|17|3105|2000
|Audi|100|1992|regular unleaded|172|6|AUTOMATIC|all wheel drive|4|Luxury|Midsize|Wagon|20|16|3105|2000

## Data Munging Tasks
Some cleaning of the data was required. For one, the column headings were lengthy and inconsistently written. For example, the column "Driven_Wheels" uses _ to separate words whereas every other column simply uses a space. To fix this, I standardized the headings so that they were all lowercase, used _ to separate words, and also shortened the headings. Additionally, I decided to remove the columns "Engine Fuel Type" and "Market Category" for the reasons that they weren't of much interest and/or were missing values as in the case of Market Category which included several "n/a" values. The data itself also needed some cleaning, which came in the form of standardizing how values were presented. Similar to the headings, I made all values lowercase, stripped any whitespace that they may have had, and replaced all spaces with underscores. Furthermore, there were several datapoints that were missing, namely the horsepower rating and number of cylinders of certain cars. Since these figures are largely unique to a given car, I decided to omit these vehicles from the cleaned data set as filling in said values cannot be done using the values of neighboring cars. I also chose to omit vehicles that were sold before 2000 as the MSRP data on many of the pre-2000 cars was set to 2000 and does not pass the smell test. Finally, I also decided to standardize the MSRP values given by converting them into 2017 dollars so that vehicle prices can be compared more accurately. This was done using the formula provided [here](https://www.usinflationcalculator.com/frequently-asked-questions-faqs/#HowInflationCalculatorWorks) and chart of CPI values found [here](https://www.usinflationcalculator.com/inflation/consumer-price-index-and-annual-percent-changes-from-1913-to-2008/).

# Analysis
## Aggregate Statistics

## Pivot Table
Here's a sampling of the pivot table I created:

|Manufacturers|Max of engine_hp|Average of cylinders|Average of mpg_highway|Average of mpg_city|Average of popularity|Average of msrp
|---|---|---|---|---|---|---
|acura|573|5.32|28.76|20.35|204.00|42501.22
|   2000|195|4.00|28.00|22.00|204.00|5515.30
|       compact|195|4.00|28.00|22.00|204.00|5515.30
|           2dr_hatchback|195|4.00|28.00|22.00|204.00|6144.37
|               integra|195|4.00|28.00|22.00|204.00|6144.37
|                   front_wheel_drive|195|4.00|28.00|22.00|204.00|6144.37
|                       manual|195|4.00|28.00|22.00|204.00|6144.37
|           sedan|170|4.00|28.00|22.00|204.00|4676.54
|               integra|170|4.00|28.00|22.00|204.00|4676.54
|                   front_wheel_drive|170|4.00|28.00|22.00|204.00|4676.54
|                       manual|170|4.00|28.00|22.00|204.00|4676.54
|   2001|225|4.31|27.85|20.92|204.00|31408.96
|       compact|195|4.00|28.00|21.64|204.00|29826.86
|           2dr_hatchback|195|4.00|28.00|21.67|204.00|29815.32
|               integra|195|4.00|28.00|21.67|204.00|29815.32
|                   front_wheel_drive|195|4.00|28.00|21.67|204.00|29815.32
|                       automatic|140|4.00|28.00|21.00|204.00|29100.22
|                       manual|195|4.00|28.00|22.00|204.00|30172.88

I'm not sure how to get it to display like the table in the excel workbook, but this is the best I can do. The pivot table should be included in the clean_data.xlsx workbook in the data folder.

# Extra Credit
## Option 2: Big Data
My original data set has almost 12,000 records, which satisfies the definition of large data set for this assignment.