values = []

def readFile():
    # Open the file for reading
    with open("./mammals.txt", "r") as filePath:
        # Read in the data one line at a time
        lines = filePath.readlines()

        # Loop through the mammals, one at a time
        for line in lines:
            mammals = line.strip() 
            parts = mammals.split(",")

            # Save the data
            town = parts[0]
            mammal = parts[1]
            date = parts[2]
            age = parts[3]

            # Add the values to the array
            values.append((town, mammal, date, age))

def findOldestMammal():
    # Set the max_age to -1 for linear search
    max_age = -1
    oldest_mammal = None

    # Loop through each entry / line stored in the array
    for entry in values:
        town, mammal, date, age = entry
        try:
            # Convert age (str) -> age (int)
            age = int(age)

            # Check if the current age recorded is > max_age so far
            if age > max_age:
                # Set the new max with the current age
                max_age = age
                oldest_mammal = (town, mammal, date, age)

        except ValueError:
            print("Invalid age", age, "for mammal", mammal, "in", town)
    
    # Check if oldest_mammal is a truthy value
    if oldest_mammal:
        town, mammal, date, age = oldest_mammal
        print("The oldest mammal is a", mammal, "from", town, "seen on", date, "with an age of:", age)
    else:
        print("No valid entries found.")

def displaySighting(mammal_name, town_name):
    # Find and display the dates of sightings of a chosen mammal in a particular town
    sightings = [(town, mammal, date) for town, mammal, date in values if mammal == mammal_name and town == town_name]
    
    if sightings:
        print("Sightings of", mammal_name, "in", town_name, ":")
        for sighting in sightings:
            print(sighting[2])  
    else:
        print("No sightings of", mammal_name, "found in", town_name)

# Read the data from the file
readFile()

# Find and display the age of the oldest mammal
findOldestMammal()

displaySighting("Squirrel", "Culross")
