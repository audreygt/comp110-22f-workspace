"""Demonstrations of dictionary capabilities."""


# Declaring the type of dictionary
schools: dict[str, int]

# Initialize to an empty dictionary 
schools = dict()

# Set a key-value pairing in the dictionary 
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation 
print(schools)

#Accessing a value by its key, performing lookup in key-value store 
print(f"UNC has {schools['UNC']} students.")

# Removing a value from the dictionary must be provided with a key 
schools.pop("Duke")

# Test for existence of key 
duke_presence: bool = "Duke" in schools 
print(f"Duke is present: {duke_presence}")
print(schools)

# Updating or reassigning a key-value pair 
schools["UNC"] = 20000
schools["NCSU"] += 200

# Inverting dictionary to use value to look up key 
invert_schools: dict[int, str]
invert_schools = dict()
invert_schools[19400] = "UNC"
print(invert_schools)

# Demonstration of dictionary literals 
# Empty dictionary literal, same as dict()
schools = {}
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# Trying to ask for a key that does not exist 
# print(schools["UNCC"])

# Answering question 21 in LS19 gradescope assignment 
    # Comment out line 46
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

print("Trying a new way to loop through the schools.")
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")