import os
import json
import pandas as pd
import sqlite3
import plotly_express as px


st.title(':violet[PhonePe Pulse Data Visualization(2018-2022)📈]')


#Agg_state_list--> to get the list of states in India
path="F:/python/phonepe/pulse/data/aggregated/transaction/country/india/state/"
Agg_state_list=os.listdir(path)
#Agg_state_list

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

#This is to extract the data's to create a dataframe

clm={'State':[], 'Year':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm['Transaction_type'].append(Name)
              clm['Transaction_count'].append(count)
              clm['Transaction_amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))

# Successfully created a dataframe
df_aggregated_transaction=pd.DataFrame(clm)
# print(df_aggregated_transaction)

# TO GET THE DATA-FRAME OF AGGREGATED <--> USER

path2 = "F:/python/phonepe/pulse/data/aggregated/user/country/india/state/"
user_list = os.listdir(path2)

col2 = {'State': [], 'Year': [], 'Quater': [], 'brands': [], 'Count': [],
        'Percentage': []}
for i in user_list:
    p_i = path2 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            B = json.load(Data)
            try:
                for w in B["data"]["usersByDevice"]:
                    brand_name = w["brand"]
                    count_ = w["count"]
                    ALL_percentage = w["percentage"]
                    col2["brands"].append(brand_name)
                    col2["Count"].append(count_)
                    col2["Percentage"].append(ALL_percentage)
                    col2["State"].append(i)
                    col2["Year"].append(j)
                    col2["Quater"].append(int(k.strip('.json')))
            except:
                pass
df_aggregated_user = pd.DataFrame(col2)
# print(df_aggregated_user)

# TO GET THE DATA-FRAME OF MAP <--> TRANSACTION

path3 = "F:/python/phonepe/pulse/data/map/transaction/hover/country/india/state/"
hover_list = os.listdir(path3)

col3 = {'State': [], 'Year': [], 'Quater': [], 'District': [], 'count': [],
        'amount': []}
for i in hover_list:
    p_i = path3 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            C = json.load(Data)
            for x in C["data"]["hoverDataList"]:
                District = x["name"]
                count = x["metric"][0]["count"]
                amount = x["metric"][0]["amount"]
                col3["District"].append(District)
                col3["count"].append(count)
                col3["amount"].append(amount)
                col3['State'].append(i)
                col3['Year'].append(j)
                col3['Quater'].append(int(k.strip('.json')))
df_map_transaction = pd.DataFrame(col3)
# print(df_map_transaction)

# TO GET THE DATA-FRAME OF MAP <--> USER

path4 = "F:/python/phonepe/pulse/data/map/user/hover/country/india/state/"
map_list = os.listdir(path4)

col4 = {"State": [], "Year": [], "Quater": [], "District": [],
        "RegisteredUser": []}
for i in map_list:
    p_i = path4 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            D = json.load(Data)

            for u in D["data"]["hoverData"].items():
                district = u[0]
                registereduser = u[1]["registeredUsers"]
                col4["District"].append(district)
                col4["RegisteredUser"].append(registereduser)
                col4['State'].append(i)
                col4['Year'].append(j)
                col4['Quater'].append(int(k.strip('.json')))
df_map_user = pd.DataFrame(col4)
# print(df_map_user)

# TO GET THE DATA-FRAME OF TOP <--> TRANSACTION

path5 = "F:/python/phonepe/pulse/data/top/transaction/country/india/state/"
TOP_list = os.listdir(path5)

col5 = {'State': [], 'Year': [], 'Quater': [], 'District': [], 'Transaction_count': [],
        'Transaction_amount': []}
for i in TOP_list:
    p_i = path5 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            E = json.load(Data)
            for z in E['data']['pincodes']:
                Name = z['entityName']
                count = z['metric']['count']
                amount = z['metric']['amount']
                col5['District'].append(Name)
                col5['Transaction_count'].append(count)
                col5['Transaction_amount'].append(amount)
                col5['State'].append(i)
                col5['Year'].append(j)
                col5['Quater'].append(int(k.strip('.json')))
df_top_transaction = pd.DataFrame(col5)
# print(df_top_transaction)

# TO GET THE DATA-FRAME OF TOP <--> USER

path6 = "F:/python/phonepe/pulse/data/top/user/country/india/state/"
USER_list = os.listdir(path6)

col6 = {'State': [], 'Year': [], 'Quater': [], 'District': [],
        'RegisteredUser': []}
for i in USER_list:
    p_i = path6 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            F = json.load(Data)
            for t in F['data']['pincodes']:
                Name = t['name']
                registeredUser = t['registeredUsers']
                col6['District'].append(Name)
                col6['RegisteredUser'].append(registeredUser)
                col6['State'].append(i)
                col6['Year'].append(j)
                col6['Quater'].append(int(k.strip('.json')))
df_top_user = pd.DataFrame(col6)
# print(df_top_user)

# CHECKING FOR MISSING VALUES,NULL VALUES

# df_aggregated_transaction.info()
# df_aggregated_user.info()
# df_map_transaction.info()
# df_map_user.info()
# df_top_transaction.info()
# df_top_user.info()

# CREATING CONNECTION WITH SQL SERVER
connection = sqlite3.connect("phonepe pulse.db")
cursor = connection.cursor()

# Inserting each Data frame into sql server
df_aggregated_transaction.to_sql('aggregated_transaction', connection, if_exists='replace')
df_aggregated_user.to_sql('aggregated_user', connection, if_exists='replace')
df_map_transaction.to_sql('map_transaction', connection, if_exists='replace')
df_map_user.to_sql('map_user', connection, if_exists='replace')
df_top_transaction.to_sql('top_transaction', connection, if_exists='replace')
df_top_user.to_sql('top_user', connection, if_exists='replace')



