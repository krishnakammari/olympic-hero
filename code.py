# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data=pd.read_csv(path)
data=data.rename(columns={"Total":"Total_Medals"})
print(data.head(10))

#Code starts here



# --------------
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',data['Better_Event'])
print(data.head(10))
better_event='Summer'


# --------------
#Code starts here

#Subsetting the dataframe
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

#Dropping the last row
top_countries=top_countries[:-1]

#Function for top 10
def top_ten(data, col):
    
    #Creating a new list
    country_list=[]
    
    #Finding the top 10 values of 'col' column
    country_list= list((data.nlargest(10,col)['Country_Name']))
    
    #Returning the top 10 list
    return country_list



#Calling the function for Top 10 in Summer
top_10_summer=top_ten(top_countries,'Total_Summer')
print("Top 10 Summer:\n",top_10_summer, "\n")

#Calling the function for Top 10 in Winter
top_10_winter=top_ten(top_countries,'Total_Winter')
print("Top 10 Winter:\n",top_10_winter, "\n")

#Calling the function for Top 10 in both the events
top_10=top_ten(top_countries,'Total_Medals')
print("Top 10:\n",top_10, "\n")

#Extracting common country names from all three lists
common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))

print('Common Countries :\n', common, "\n")

#Code ends here


# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]
# print(summer_df)
winter_df=data[data['Country_Name'].isin(top_10_winter)]
# print(winter_df)
top_df=data[data['Country_Name'].isin(top_10)]

res1=summer_df.groupby(['Country_Name','Total_Summer']).size().unstack()
res1.plot(kind='bar',stacked=True,figsize=(15,10))

res2=winter_df.groupby(['Country_Name','Total_Winter']).size().unstack()
res2.plot(kind='bar',stacked=True,figsize=(15,10))

res3=top_df.groupby(['Country_Name','Total_Medals']).size().unstack()
res3.plot(kind='bar',stacked=True,figsize=(15,10))

plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
print(summer_df)
summer_max_ratio=round(summer_df['Golden_Ratio'].max(),2)
print(summer_max_ratio)
summer_country_gold='China'
print(summer_country_gold)

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']

winter_max_ratio=round(winter_df['Golden_Ratio'].max(),2)

winter_country_gold='Soviet Union'

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=round(top_df['Golden_Ratio'].max(),2)
top_country_gold='China'


# --------------
#Code starts here
# print(data.tail(5))
data_1=data.drop(data.index[len(data)-1])
# print(data_1.tail(5))
data_1['Total_Points']=3*data_1['Gold_Total']+2*data_1['Silver_Total']+data_1['Bronze_Total']

most_points=max(data_1['Total_Points'])
best_country=data_1.loc[data_1['Total_Points'].idxmax(),"Country_Name"]
print(most_points)
print(best_country)


# --------------
#Code starts here
best=data[data['Country_Name']==best_country]
print(best)
best=best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


