#!/usr/bin/env python
# coding: utf-8

# # Business problem 

# #### A Southern-Franced based coffee shop chain (named 'Allo Café) reached out to get advice on how to place their planned coffee shops in Paris. 
# They do not have any shop in Paris or near the capital area yet. 
# 
# Main goal: to identify the two best areas that would fit 'allo Café's criteria and where the chain should open their first two shops in Paris. 
# 
# Criteria and aspects learnt upon the first consultation: 
# 
# - 'allo café wants to open two shops but in two distinct districts 
# - Based on their experience, they can achieve higher returns at locations where people like traditional French cuisine and bakery 
# - They do not want to be surrounded by many competing stores from the exact same category, but some 'café culture' is necessary 
# - Eventually they want to open at least three shops in one of the identified areas, so there needs to be enough room for it 
# - For the second store, they seek to 'try out something new', and would prefer to put the shop in the vicinity of parks/outdoor activities (they do not want to expand more in this area) 
# - Price is an important consideration. They are willing to pay more for a better area, but will minimise the price within the area if a given district within the area offers lower rental prices 
# 
# 

# # Data Sources

# The above task will be executed by using location data and analysising the composition of different districts based on already existing venues. 
# 
# To obtain information on nearby venues, Foursquare API will be leveraged. 
# - Based on location data, top 5 venues such restaurants, hotels, parks etc. will be identified for every district. 
# 
# To obtain information on the districts, their names, population etc. the following wikipedia page will be used: https://en.wikipedia.org/wiki/Arrondissements_of_Paris
# - In terms of the location data, certain district names such as Panthéon might be 'confusing'. As these names might be in fact used for other locations as well, adjustments will need to be made and coordinates double-checked. 
# 
# Latitude and longitude data will be gained through GeoPy. As mentioned before, if needed, it will be double-checked and complimented with direct Google searches. 
# 
# To obtain average rental prices for the different districts, the following page will be used:
# https://www.lci.fr/immobilier/video-immobilier-louer-a-paris-coute-de-plus-en-plus-cher-voici-les-prix-dans-chaque-arrondissement-etude-locservice-fr-2116595.html
# 

# # Methodology

# A main table called Paris_district was created by using and clearing the data obtained from the various above described sources. The main remaining columns after data clearing were 
# - District number
# - Name of the district
# - Population
# - Density
# - Latitude
# - Longitude
# - Price per sqm 
# 
# Latitude and Longitude data needed to be added manually for 7 districts. 
# 
# Top 5 venues for all districts were collected using Foursqaure API. Then one-hot encoding was used and rows were grouped by neighborhoods (taking the mean of the frequency of each venue category). 
# 
# K-means clustering was used to obtain similar and clearly district areas composed of one or several Parisian districts. This was crucial for both 
# - obtaining information on which bigger, future expansion-ready area would satisfy the 'traditional' criteria for the first coffee shop
# - identify which single neighborhood (potentially one-district cluster) could be a good candidate for the pilot project, where no expansion is planned 
# 
# 
# 
# 

# # Results and discussion 

# Overall, the most common places in Paris turned out to be French restaurants, followed by hotels and other type of restaurants. 
# - This did not bring us closer to the desired outcome. 
# 
# The clustering created 5 district areas composed of a different number of districts. 
# 
# Cluster one 
# - With only one district, Observatoire, a traditional French area (many French restaurants) yet quite diverse as well with a café culture so a possible candidate
# - However, future expansion is not possible here. Observatoire is too small for that and no strictly similar districts are in the cluster
# 
# Cluster two
# - With as many as 7 districts, it is a traditionally French area with restaurants and hotels but it is also very chic, less homogenous and rather expensive compared to other clusters
# - It could be a second best choice for the first coffee shop, but the profile of this area is more suitable for expensive restaurants that can cater the needs of rich tourists/parisians
# 
# Cluster three 
# - With two districts, Butte-Montmartre and Ménilmontant, this area is clearly for bars, cocktail places and multicultural restaurants. It is not famous for its cafés, bakeries or traditional venues 
# - As such, it is the single cluster that is clearly not recommended 
# 
# Cluster four
# - Distinct area with only one district, Reully, with many recreational and outdoor activities (parks, sport club), a lack of restaurants/cafés but still a bigger population than most more central districts
# - Reully is recommended for the pilot project, as it is distinct, demand is possibly guaranteed due to the big population / people going here for recreational activities from other districts. Competition is also lacking 
# 
# Cluster five 
# - The most populous area with 9 districts such as Panthéon, Gobelins or Bourse. In its composition, it is similar to cluster two, but it is less chich, less expensive, and more heterogeneous. Café culture is also more engrained here. That is the cluster with the most coffee shops in Paris, which means competition. However, the cluster is big and the first store can be easily opened in a district that is crowded with coffee shops. 
# - Based on this criteria and rental price considerations, the absolute winner is Gobelins within Cluster five. Further expansion is also encouraged within this cluster, possibly to a more central location next, such as Panthéon, which is still not overcrowded with coffee shops, but has the right culture and complimentary venues. 
# 
# Recommendations 
# - The first coffee shop is recommended to be opened at Gobelins, 13th district. Further expansion is then possible within Cluster five. 
# - The second coffee shop is recommended to be opened at Reuilly, 12th distict. 
# 

# # Conclusion 

# The above analysis used Foursquare API, Wikipedia and other relevant data sources to analyse the different districts of Paris and to come up with recommendations on where to place two new coffee shops of 'Alo Café, a French coffee shop chain. 
# 
# It used expolatory data analysis and k-means clustering to identify different types of neighborhoods in the city. As the client eventually seeks to open more than one coffee shop in a designated area and is also looking for a very distinct area to open its second store, k-means clustering was used. Districts were clustered based on the already existing venues that describe them the most. Clustering was based on the top 5 venues in each one of them. 
# 
# The first main recommendation of this report is to open the first store at Gobelins in the 13th district. The corresponding cluster has 'traditional French' culture (which was a criteria) yet it is also diverse and less chich than some other districts. The big number of districts in this sector paves the way for opening new shops in the future at very similar locations, based on similar considerations. 
# 
# The second main recommendation of this report is to open the second store at Reuilly in the 12th district. Reuilly is in a very distinct cluster with only one district. As such, it an interesting yet appealing place which could suit well the description for the 'pilot' project provided by 'Alo Café. Outdoor and recreational activities abound here which could attract people from other districts to an already populous neighborhood. At the same tiem, competition is very small and prices are convenient. 

# In[ ]:




