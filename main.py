# C:\Users\Maninder\AppData\Local\Programs\Python\Python39
# C:\Users\Maninder\AppData\Local\Programs\Python\Python39\Scripts

# pip install plotly streamlit pandas Pillow

# import openpyxl
import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title='Employee Survey')
# st.header('Employee Survey 2.0')
# st.subheader('Includes previous survey data')

st.title("Employee Survey 2.0")

###Load Excel data
surveyData = pd.read_excel(
                    "Employee_Data.xlsx", 
                    sheet_name = "Skills",
                    usecols = 'A:F',
                    header = 0 #starting row_count
                    )
skillsData = pd.read_excel(
                    "Team_Info.xlsx", 
                    sheet_name = "Skills",
                    )
teamData = pd.read_excel(
                    "Team_Info.xlsx", 
                    sheet_name = "Teams",
                    )

# st.write(df2["Skill"][0])

team = st.selectbox("Select team", teamData["Team"].unique())
name = st.selectbox("Enter name", teamData.loc[teamData["Team"]==team, "Name"])       #input you want too collect

# pd_arr = pandas.array(data=[1,2,3,4,5],dtype=str)
# skill_value = pd.array(skillsData.index)
skill_value = [0]*skillsData.shape[0]
idx1 = 0

serachedValues = surveyData['Name'].where(surveyData["Name"]==name)
if not serachedValues.notnull().values.any():
    new_row = surveyData[surveyData['Name']!=name].iloc[0]
    new_row[2 :] = 0
    new_row["Name"] = name
    new_row["Team"] = team
    surveyData = surveyData.append(new_row, ignore_index=True)
    # st.write(surveyData)

with st.form(key="form1"): 
    for skill_name in skillsData["Skill"]:
        skill_value[idx1] = st.radio(skill_name, [0,1,2,3], index = int(surveyData.loc[surveyData["Name"]==name, skill_name]), horizontal=True)
        idx1+=1
    
    submit_data = st.form_submit_button(label = "Submit")

if submit_data:
    # new_data = {"Name":name, "Head 1":h1, "Head 2":h2, "Head 3":op3, "Head 4":op4}
    # st.write(new_data)
    #     df = df.append(new_data, ignore_index=True)
    # surveyData.loc[surveyData["Name"]==name, ["Head 1","Head 2","Head 3","Head 4"]] = [h1,h2,h3,h4]
    idx2=0
    for skill_name in skillsData["Skill"]:
        surveyData.loc[surveyData["Name"]==name, skill_name] = skill_value[idx2]
        idx2+=1

    surveyData.to_excel("Employee_Data.xlsx", sheet_name="Skills", index=False)    #overriding intial excel file data
    # st.write(surveyData)
    st.markdown('<a href="/thankyou" target="_self">Next page</a>', unsafe_allow_html=True)


