# place your code to clean up the data file below.

import csv

# method for standardizing keys and values of dictionary-represented rows
def standardize(row: dict):
    # removing uninteresting columns
    row.pop("Engine Fuel Type")
    row.pop("Market Category")

    # creating dictionary to be used to replace old keys with new keys
    old_keys = list(row.keys())
    switch = {"Make":"make", "Model":"model", "Year":"year", "Engine HP":"engine_hp", "Engine Cylinders":"cylinders", "Transmission Type":"transmission", "Driven_Wheels":"driven_wheels", "Number of Doors":"num_doors", "Vehicle Size":"size", "Vehicle Style":"style", "highway MPG":"mpg_highway", "city mpg":"mpg_city", "Popularity":"popularity", "MSRP":"msrp"}
    
    # iterating over old keys
    for key in old_keys:
        # formatting values
        value = row[key].lower()
        value = value.strip()
        value = value.replace(" ","_")
        row[key] = value

        # removing old key, value pair and replacing with pair with updated key
        row[switch[key]] = row.pop(key)

# method for converting vehicle MSRP into 2017 dollars
def convertMSRP(row: dict):
    # below numbers were taken from https://www.usinflationcalculator.com/inflation/consumer-price-index-and-annual-percent-changes-from-1913-to-2008/, provided by the BLS
    avg_cpi = [172.2, 177.1, 179.9, 184.0, 188.9, 195.3, 201.6, 207.3, 215.303, 214.537, 218.056, 224.939, 229.594, 232.957, 236.736, 237.017, 240.007]
    cpi_2017 = 245.120

    # getting which year cpi to use from remainder
    remainder = int(row["Year"]) % 2000

    # calculating equivalent value in 2017 dollars
    current_MSRP = int(row["MSRP"]) * cpi_2017 / avg_cpi[remainder]
    row["MSRP"] = str(format(current_MSRP, ".2f"))

# method for checking if a row has null values
# since each car model and trim is unique in some way, null values cannot be easily filled in from neighbors
# therefore, rows with null values are omitted
def checkForNull(row: dict):
    for val in row.values():
        if val == "":
            return False

    return True

# opening the dirty data
dirty = open("./data/data.csv", "r")
reader = csv.DictReader(dirty)

# creating clean data file
clean = open("./data/clean_data.csv", "w", newline="")
fieldnames = ["make", "model", "year", "engine_hp", "cylinders", "transmission", "driven_wheels", "num_doors", "size", "style", "mpg_highway", "mpg_city", "popularity", "msrp"]
writer = csv.DictWriter(clean, fieldnames=fieldnames)
writer.writeheader()

# iterating over all rows from dirty data
for row in reader:
    # only storing data of MY2000 and up cars
    if int(row["Year"]) >= 2000:
        # only storing data of cars with complete data
        if checkForNull(row):
            # converting MSRP if car is not a MY2017 car
            if int(row["Year"]) != 2017:
                convertMSRP(row)

            # standardizing and writing to clean data file
            standardize(row)
            writer.writerow(row)

dirty.close()
clean.close()