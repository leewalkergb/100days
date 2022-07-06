#----------------------------------------------------------------------------------
# This is the code for the Python Lists: Medical Insurance Costs Project on the 
# DATA SCIENTIST: ANALYTICS SPECIALIST career path on Codeacademy
#
# Date: 06/07/22
#----------------------------------------------------------------------------------

# You are a doctor sorting through medical insurance cost data for some patients.

# Using your knowledge of Python lists, you will store medical data and see what valuable insights you can gain from that data.

#-----------------------------------------------------------------------------------------------------------------------------

names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add prisicilla and her insurance costs to the above lists
names.append("Priscilla")
insurance_costs.append(8320.0)

# Combine the two seperate lists
medical_records = list(zip(insurance_costs,names))
print(medical_records)

#-----------------------------------------------------------------------------------------------------------------------------

# Find the number of records we have
num_medical_records = len(medical_records)
print("There are ", num_medical_records, "medical records.")

# Select the first record
first_medical_record = medical_records[0]
print("Here is the first medical record " + str(first_medical_record))

# Sort the medical records, remeber it auto selects the first element to sort by.
# Remember .sort() alters the list sorted() makes a new one
medical_records.sort()
print("Here are the medical records sorted by insurance cost " + str(medical_records))

#-----------------------------------------------------------------------------------------------------------------------------

# Select the three cheapest records
cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))

# Select the three most expensive records
priciest_three = medical_records[-3:]
print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))

#-----------------------------------------------------------------------------------------------------------------------------
occurences_paul = names.count("Paul")
print("There are " + str(occurences_paul) + " individuals with the name Paul in our medical records")

#-----------------------------------------------------------------------------------------------------------------------------

alphabetical = list(zip(names, insurance_costs))
alphabetical.sort()
print(alphabetical)

middle_five = alphabetical[4:8]