#------------------------------------------------------------------------
# Working with files
#------------------------------------------------------------------------
# We can read files using the following syntax

# STep 1: Teel it what file to open and as what object
with open('practice.txt') as cool_doc:
# Read the contents and save them to the variable cool_contents
    cool_contents = cool_doc.read() 

# Print out the file contents
print(cool_contents)