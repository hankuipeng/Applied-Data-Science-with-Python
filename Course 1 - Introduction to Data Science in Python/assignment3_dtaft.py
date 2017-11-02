import numpy as np
import pandas as pd

#energy = pd.ExcelFile('Energy Indicators.xls')
#df = energy.parse(energy.sheet_names[0], skiprows=)
energy = pd.read_excel('Energy Indicators.xls', skiprows=17, skip_footer=38)
energy.drop(energy.columns[[0, 1]], axis=1, inplace=True)
energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

# Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule)
energy.loc[:, 'Energy Supply'] = energy['Energy Supply'] * (10**6)

# For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.
#energy = energy.replace('...', np.nan)


# There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these.
for j,country in enumerate(energy['Country']):
    for i in range(len(country)):
        if (country[i].isdigit()) or (country[i]=='('):
            lastindex = i
            energy['Country'][j] = country[0:lastindex]
            break

energy.iloc[80:100,:]

#### Q1
### FIRST CHUNK
import numpy as np
import pandas as pd

#energy = pd.ExcelFile('Energy Indicators.xls')
#df = energy.parse(energy.sheet_names[0], skiprows=)
energy = pd.read_excel('Energy Indicators.xls', skiprows=17, skip_footer=38)
energy.drop(energy.columns[[0, 1]], axis=1, inplace=True)
energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

# Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule)
energy.loc[:, 'Energy Supply'] = energy['Energy Supply'] * (10**6)

# For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.
#energy = energy.replace('...', np.nan)


# There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these.
for j,country in enumerate(energy['Country']):
    for i in range(len(country)):
        if (country[i].isdigit()) or (country[i]=='('):
            lastindex = i
            energy['Country'][j] = country[0:lastindex].rstrip()
            break
            

# Rename the following list of countries (for use in later questions)
energy = energy.replace({'...': np.nan,
                         "Republic of Korea": "South Korea",
                         'United States of America': 'United States', 
                         'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom', 
                         'China, Hong Kong Special Administrative Region': 'Hong Kong'})
            

#energy.loc[98,'Country']
#energy['Country']


### SECOND CHUNK

#  load the GDP data from the file world_bank.csv
GDP = pd.read_csv('world_bank.csv', skiprows=4)

# rename the following list of countries
GDP = GDP.replace({"Korea, Rep.": "South Korea", 
                             "Iran, Islamic Rep.": "Iran",
                             "Hong Kong SAR, China": "Hong Kong"})

# Use only the last 10 years (2006-2015) of GDP data
GDP.rename(columns={'Country Name':'Country'}, inplace=True)

df_a = GDP.loc[:,'Country']
df_b = GDP.loc[:,'2006':'2015']
GDP = pd.concat([df_a.reset_index(drop=True), df_b], axis=1)

#GDP.iloc[100:150,:]


###### THRID CHUNK
   
# load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file scimagojr-3.xlsx
ScimEn = pd.read_excel('scimagojr-3.xlsx')

# use only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15)
ScimEn = ScimEn.iloc[:15,:]

#ScimEn.loc[12,'Country']
#energy.loc[98,'Country']
# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). 
# Use only the last 10 years (2006-2015) of GDP data and 
# only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).

newDat = ScimEn.merge(energy, on='Country').merge(GDP, on='Country')
newdat = newDat.set_index('Country')








def answer_one():
    import numpy as np
    import pandas as pd
    
    ###### CHUNK 1
    
    #energy = pd.ExcelFile('Energy Indicators.xls')
    #df = energy.parse(energy.sheet_names[0], skiprows=)
    energy = pd.read_excel('Energy Indicators.xls', skiprows=17, skip_footer=38)
    energy.drop(energy.columns[[0, 1]], axis=1, inplace=True)
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

    # Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule)
    energy.loc[:, 'Energy Supply'] = energy['Energy Supply'] * (10**6)

    # For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.
    #energy = energy.replace('...', np.nan)


    # There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these.
    for j,country in enumerate(energy['Country']):
        for i in range(len(country)):
            if (country[i].isdigit()) or (country[i]=='('):
                lastindex = i
                energy['Country'][j] = country[0:lastindex].rstrip()
                break
            

    # Rename the following list of countries (for use in later questions)
    energy = energy.replace({'...': np.nan,
                             "Republic of Korea": "South Korea",
                             'United States of America': 'United States', 
                             'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom', 
                             'China, Hong Kong Special Administrative Region': 'Hong Kong'})
            

    #energy.loc[98,'Country']
    #energy['Country']
    
    
    ###### CHUNK 2
    #  load the GDP data from the file world_bank.csv
    GDP = pd.read_csv('world_bank.csv', skiprows=4)

    # rename the following list of countries
    GDP = GDP.replace({"Korea, Rep.": "South Korea", 
                             "Iran, Islamic Rep.": "Iran",
                             "Hong Kong SAR, China": "Hong Kong"})

    # Use only the last 10 years (2006-2015) of GDP data
    GDP.rename(columns={'Country Name':'Country'}, inplace=True)

    df_a = GDP.loc[:,'Country']
    df_b = GDP.loc[:,'2006':'2015']
    GDP = pd.concat([df_a.reset_index(drop=True), df_b], axis=1)

    #GDP.iloc[100:150,:]
    
    
    ###### CHUNK 3
    
    # load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file scimagojr-3.xlsx
    ScimEn = pd.read_excel('scimagojr-3.xlsx')

    # use only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15)
    ScimEn = ScimEn.iloc[:15,:]

    #ScimEn.loc[12,'Country']
    #energy.loc[98,'Country']
    # Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). 
    # Use only the last 10 years (2006-2015) of GDP data and 
    # only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).

    newDat = ScimEn.merge(energy, on='Country').merge(GDP, on='Country')
    newdat = newDat.set_index('Country')
    
    return newdat

