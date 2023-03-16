import streamlit as st
import os
import json
import pandas as pd
import sqlite3
import plotly_express as px


st.title(':violet[PhonePe Pulse Data Visualization(2018-2022)📈]')


# CREATING CONNECTION WITH SQL SERVER
connection = sqlite3.connect("phonepe pulse.db")
cursor = connection.cursor()


# Creating Options in app

st.balloons()
with st.container():
        st.title("BASIC INSIGHTS")
        #st.write("----")
        st.subheader("Let's know some basic insights about the data")
        options = ["--select--","Top 10 states based on year and amount of transaction","Least 10 states based on type and amount of transaction",
                "Top 10 mobile brands based on percentage of transaction","Top 10 Registered-users based on States and District(pincode)",
                "Top 10 Districts based on states and amount of transaction","Least 10 Districts based on states and amount of transaction",
                "Least 10 registered-users based on Districts and states","Top 10 transactions_type based on states and transaction_amount"]
        select = st.selectbox("Select the option",options)
        if select=="Top 10 states based on year and amount of transaction":
            cursor.execute("SELECT DISTINCT State,Transaction_amount,Year,Quater FROM top_transaction GROUP BY State ORDER BY transaction_amount DESC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_amount','Year','Quater'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Top 10 states based on type and amount of transaction")
                fig=px.bar(df,x="State",y="Transaction_amount")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)

        elif select=="Least 10 states based on type and amount of transaction":
            cursor.execute("SELECT DISTINCT State,Transaction_amount,Year,Quater FROM top_transaction GROUP BY State ORDER BY transaction_amount ASC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_amount','Year','Quater'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Least 10 states based on type and amount of transaction")
                fig=px.bar(df,x="State",y="Transaction_amount")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)

        elif select=="Top 10 mobile brands based on percentage of transaction":
            cursor.execute("SELECT DISTINCT brands,Percentage FROM aggregated_user GROUP BY brands ORDER BY Percentage DESC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['brands','Percentage'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Top 10 mobile brands based on percentage of transaction")
                fig=px.bar(df,x="brands",y="Percentage")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)

        elif select=="Top 10 Registered-users based on States and District(pincode)":
            cursor.execute("SELECT DISTINCT State,District,RegisteredUser FROM top_user GROUP BY State,District ORDER BY RegisteredUser DESC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['State','District','RegisteredUser'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Top 10 Registered-users based on States and District(pincode)")
                fig=px.bar(df,x="State",y="RegisteredUser")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)

        elif select=="Top 10 Districts based on states and amount of transaction":
            cursor.execute("SELECT DISTINCT State,District,amount FROM map_transaction GROUP BY State,District ORDER BY amount DESC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Transaction_amount'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Top 10 Districts based on states and amount of transaction")
                fig=px.bar(df,x="State",y="Transaction_amount")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)

        elif select=="Least 10 Districts based on states and amount of transaction":
            cursor.execute("SELECT DISTINCT State,District,amount FROM map_transaction GROUP BY State,District ORDER BY amount ASC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Transaction_amount'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Least 10 Districts based on states and amount of transaction")
                fig=px.bar(df,x="State",y="Transaction_amount")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)

        elif select=="Least 10 registered-users based on Districts and states":
            cursor.execute("SELECT DISTINCT State,District,RegisteredUser FROM top_user GROUP BY State,District ORDER BY RegisteredUser ASC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['State','District','RegisteredUser'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Least 10 registered-users based on Districts and states")
                fig=px.bar(df,x="State",y="RegisteredUser")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)

        elif select=="Top 10 transactions_type based on states and transaction_amount":
            cursor.execute("SELECT DISTINCT State,Transaction_type,Transaction_amount FROM aggregated_transaction GROUP BY State,Transaction_type ORDER BY Transaction_amount DESC LIMIT 10");
            df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_type','Transaction_amount'])
            col1,col2 = st.columns(2)
            with col1:
                st.write(df)
            with col2:
                st.title("Top 10 transactions_type based on states and transaction_amount")
                fig=px.bar(df,x="State",y="Transaction_amount")
                tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
                with tab1:
                    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                with tab2:
                    st.plotly_chart(fig, theme=None, use_container_width=True)



with st.container():
        st.title("DATA")
        Topic = ["","Brand","District","Registered-users","Top-Transactions","Transaction-Type"]
        choice_topic = st.selectbox("Search by",Topic)

    #creating functions for query search in sqlite to get the data
        def type_(type):
            cursor.execute(f"SELECT DISTINCT State,Quater,Year,Transaction_type,Transaction_amount FROM aggregated_transaction WHERE Transaction_type = '{type}' ORDER BY State,Quater,Year");
            df = pd.DataFrame(cursor.fetchall(), columns=['State','Quater', 'Year', 'Transaction_type', 'Transaction_amount'])
            return df
        def type_year(year,type):
            cursor.execute(f"SELECT DISTINCT State,Year,Quater,Transaction_type,Transaction_amount FROM aggregated_transaction WHERE Year = '{year}' AND Transaction_type = '{type}' ORDER BY State,Quater,Year");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'Transaction_type', 'Transaction_amount'])
            return df
        def type_state(state,year,type):
            cursor.execute(f"SELECT DISTINCT State,Year,Quater,Transaction_type,Transaction_amount FROM aggregated_transaction WHERE State = '{state}' AND Transaction_type = '{type}' And Year = '{year}' ORDER BY State,Quater,Year");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'Transaction_type', 'Transaction_amount'])
            return df
        def district_choice_state(_state):
            cursor.execute(f"SELECT DISTINCT State,Year,Quater,District,amount FROM map_transaction WHERE State = '{_state}' ORDER BY State,Year,Quater,District");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'amount'])
            return df
        def dist_year_state(year,_state):
            cursor.execute(f"SELECT DISTINCT State,Year,Quater,District,amount FROM map_transaction WHERE Year = '{year}' AND State = '{_state}' ORDER BY State,Year,Quater,District");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'amount'])
            return df
        def district_year_state(_dist,year,_state):
            cursor.execute(f"SELECT DISTINCT State,Year,Quater,District,amount FROM map_transaction WHERE District = '{_dist}' AND State = '{_state}' AND Year = '{year}' ORDER BY State,Year,Quater,District");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'amount'])
            return df
        def brand_(brand_type):
            cursor.execute(f"SELECT State,Year,Quater,brands,Percentage FROM aggregated_user WHERE brands='{brand_type}' ORDER BY State,Year,Quater,brands,Percentage DESC");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'brands', 'Percentage'])
            return df
        def brand_year(brand_type,year):
            cursor.execute(f"SELECT State,Year,Quater,brands,Percentage FROM aggregated_user WHERE Year = '{year}' AND brands='{brand_type}' ORDER BY State,Year,Quater,brands,Percentage DESC");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'brands', 'Percentage'])
            return df
        def brand_state(state,brand_type,year):
            cursor.execute(f"SELECT State,Year,Quater,brands,Percentage FROM aggregated_user WHERE State = '{state}' AND brands='{brand_type}' AND Year = '{year}' ORDER BY State,Year,Quater,brands,Percentage DESC");
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'brands', 'Percentage'])
            return df
        def transaction_state(_state):
            cursor.execute(f"SELECT State,Year,Quater,District,Transaction_count,Transaction_amount FROM top_transaction WHERE State = '{_state}' GROUP BY State,Year,Quater")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'Transaction_count', 'Transaction_amount'])
            return df
        def transaction_year(_state,_year):
            cursor.execute(f"SELECT State,Year,Quater,District,Transaction_count,Transaction_amount FROM top_transaction WHERE Year = '{_year}' AND State = '{_state}' GROUP BY State,Year,Quater")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'Transaction_count', 'Transaction_amount'])
            return df
        def transaction_quater(_state,_year,_quater):
            cursor.execute(f"SELECT State,Year,Quater,District,Transaction_count,Transaction_amount FROM top_transaction WHERE Year = '{_year}' AND Quater = '{_quater}' AND State = '{_state}' GROUP BY State,Year,Quater")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'Transaction_count', 'Transaction_amount'])
            return df
        def registered_user_state(_state):
            cursor.execute(f"SELECT State,Year,Quater,District,RegisteredUser FROM map_user WHERE State = '{_state}' ORDER BY State,Year,Quater,District")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'RegisteredUser'])
            return df
        def registered_user_year(_state,_year):
            cursor.execute(f"SELECT State,Year,Quater,District,RegisteredUser FROM map_user WHERE Year = '{_year}' AND State = '{_state}' ORDER BY State,Year,Quater,District")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'RegisteredUser'])
            return df
        def registered_user_district(_state,_year,_dist):
            cursor.execute(f"SELECT State,Year,Quater,District,RegisteredUser FROM map_user WHERE Year = '{_year}' AND State = '{_state}' AND District = '{_dist}' ORDER BY State,Year,Quater,District")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quater", 'District', 'RegisteredUser'])
            return df


        if choice_topic=="Transaction-Type":
            col1,col2,col3 = st.columns(3)
            with col1:
                st.subheader(" TRANSACTION TYPE ")
                transaction_type = st.selectbox("search by", ["Choose an option", "Financial Services",
                                                            "Merchant payments", "Peer-to-peer payments",
                                                            "Recharge & bill payments", "Others"], 0)
            with col2:
                st.subheader(" SELECT THE YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                            'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                            'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 'maharashtra', 'manipur',
                            'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)

            if transaction_type:
                col1,col2,col3, = st.columns(3)
                with col1:
                    st.subheader(f'{transaction_type}')
                    st.write(type_(transaction_type))
            if transaction_type and choice_year:
                with col2:
                    st.subheader(f' in {choice_year}')
                    st.write(type_year(choice_year,transaction_type))
            if transaction_type and choice_state and choice_year:
                with col3:
                    st.subheader(f' in {choice_state}')
                    st.write(type_state(choice_state,choice_year,transaction_type))

        if choice_topic=="District":
            col1,col2,col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                            'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                            'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 'maharashtra', 'manipur',
                            'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT DISTRICT ")
                district = st.selectbox("search by", df_map_transaction["District"].unique().tolist())
            if choice_state:
                col1,col2,col3 = st.columns(3)
                with col1:
                    st.subheader(f'{choice_state}')
                    st.write(district_choice_state(choice_state))
            if choice_year and choice_state:
                with col2:
                    st.subheader(f'in {choice_year} ')
                    st.write(dist_year_state(choice_year,choice_state))
            if district and choice_state and choice_year:
                with col3:
                    st.subheader(f'in {district} ')
                    st.write(district_year_state(district,choice_year,choice_state))

        if choice_topic=="Brand":
            col1,col2,col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT BRAND ")
                mobiles = ['', 'Apple', 'Asus', 'COOLPAD', 'Gionee', 'HMD Global', 'Huawei',
                        'Infinix', 'Lava', 'Lenovo', 'Lyf', 'Micromax', 'Motorola', 'OnePlus',
                        'Oppo','Realme', 'Samsung', 'Tecno', 'Vivo', 'Xiaomi','Others']
                brand_type = st.selectbox("search by",mobiles, 0)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                            'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                            'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 'maharashtra', 'manipur',
                            'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)

            if brand_type:
                col1,col2,col3, = st.columns(3)
                with col1:
                    st.subheader(f'{brand_type}')
                    st.write(brand_(brand_type))
            if brand_type and choice_year:
                with col2:
                    st.subheader(f' in {choice_year}')
                    st.write(brand_year(brand_type,choice_year))
            if brand_type and choice_state and choice_year:
                with col3:
                    st.subheader(f' in {choice_state}')
                    st.write(brand_state(choice_state,brand_type,choice_year))

        if choice_topic=="Top-Transactions":
            col1,col2,col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                            'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                            'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 'maharashtra', 'manipur',
                            'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT Quater ")
                menu_quater = ["", "1", "2", "3", "4"]
                choice_quater = st.selectbox("Quater", menu_quater, 0)

            if choice_state:
                with col1:
                    st.subheader(f'{choice_state}')
                    st.write(transaction_state(choice_state))
            if choice_state and choice_year:
                with col2:
                    st.subheader(f'{choice_year}')
                    st.write(transaction_year(choice_state,choice_year))
            if choice_state and choice_quater:
                with col3:
                    st.subheader(f'{choice_quater}')
                    st.write(transaction_quater(choice_state,choice_year,choice_quater))

        if choice_topic=="Registered-users":
            col1,col2,col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                            'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                            'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 'maharashtra', 'manipur',
                            'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT DISTRICT ")
                district = st.selectbox("search by", df_map_transaction["District"].unique().tolist())

            if choice_state:
                with col1:
                    st.subheader(f'{choice_state}')
                    st.write(registered_user_state(choice_state))
            if choice_state and choice_year:
                with col2:
                    st.subheader(f'{choice_year}')
                    st.write(registered_user_year(choice_state,choice_year))
            if choice_state and choice_year and district:
                with col3:
                    st.subheader(f'{district}')
                    st.write(registered_user_district(choice_state,choice_year,district))

