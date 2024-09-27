def readCountries():
    # Open the file to read it
    with open('project/countries.txt', 'r') as countriesFile:
        countries = countriesFile.readlines()  
        countries = [country.strip() for country in countries]
        
    return countries


def findShortest(countries):
    min = len(countries[0])

    for i in range(0, len(countries)):
        if (len(countries[i]) < min):
            return countries[i]
            break

def writeFile(countries):
    with open('project/results.txt', 'w') as newCountriesFile:
        for country in countries:
            if country.startswith('E'):
                newCountriesFile.write(country + '\n')

countries = readCountries()
shortestCountry = findShortest(countries)
writeFile(countries)
