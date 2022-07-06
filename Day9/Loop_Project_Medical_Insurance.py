#----------------------------------------------------------------------------------
# This is the code for the Python loops: Medical Insurance estimates vs Costs Project on the 
# DATA SCIENTIST: ANALYTICS SPECIALIST career path on Codeacademy
#
# Date: 06/07/22
#----------------------------------------------------------------------------------

# You are interested in analyzing medical insurance cost data efficiently without writing repetitive code.

# In this project, you will use your new knowledge of Python loops to iterate through and analyze medical insurance cost data.

#-----------------------------------------------------------------------------------------------------------------------------
names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

total_cost = 0

# Find the sum of all actual insurance costs
for cost in actual_insurance_costs:
    total_cost += cost

# Find the average cost
average_cost = total_cost / len(actual_insurance_costs)

print("Average insurance cost:", average_cost,"dollars.")

# For all individuals in name figure out if their cost is above the average cost
for i in range(0,len(names)):
    name = names[i]
    insurance_cost = actual_insurance_costs[i]
    if insurance_cost > average_cost:
        print("The insurance cost for", name, "is above average.")
    elif insurance_cost < average_cost:
        print("The insurance cost for", name, "is below average.")
    else:
         print("The insurance cost for", name, "is the average.")
    #print("The insurance cost for " + str(name) + " is " + str(insurance_cost) + " dollars.")

#Update the insurance costs using a list comprehension
updated_insurance_costs = [cost*11/10 for cost in estimated_insurance_costs]
print(updated_insurance_costs)