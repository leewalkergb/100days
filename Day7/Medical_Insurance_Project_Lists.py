#----------------------------------------------------------------------------------
# This is the code for the Python Lists: Medical Insurance Estimation Project on the 
# DATA SCIENTIST: ANALYTICS SPECIALIST career path on Codeacademy
#
# Date: 03/07/22
#----------------------------------------------------------------------------------

# In this project, you will examine how factors such as age, sex, BMI, number of children, and smoking status contribute to medical insurance costs.

# You will apply your new knowledge of Python Lists to store insurance cost data in a list as well as compare estimated insurance costs to actual insurance costs.

#-----------------------------------------------------------------------------------------------------------------------------

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Create a list for the actual insurance costs
names = ["Maria", "Rohan", "Valentina"]
insurance_costs = [4150.0, 5320.0, 35210.0]

# Combine the above two lists using zip and convert to a list
insurance_data = list(zip(names, insurance_costs))

# Create a list for the estimated insurance costs
estimated_insurance_data = []
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))

# Print out the actual and estimated insurance costs in a nice string
print("Here is the actual insurance cost data: ", str(insurance_data))
print("Here is the estimated insurance cost data: ", str(estimated_insurance_data))