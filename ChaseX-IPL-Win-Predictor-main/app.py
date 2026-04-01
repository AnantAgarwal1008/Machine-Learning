import streamlit as st
import pickle
import pandas as pd

st.title("IPL Win Predictor")
teams=['Sunrisers Hyderabad', 'Punjab Kings', 'Delhi Capitals',
       'Kolkata Knight Riders', 'Mumbai Indians',
       'Royal Challengers Bangalore', 'Chennai Super Kings',
       'Rajasthan Royals']
cities= ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah']
pipe=pickle.load(open('pipe.pkl', 'rb'))
col1,col2=st.columns(2)
with col1:
    batting_team=st.selectbox('Select the batting team', sorted(teams))

with col2:
    bowling_team=st.selectbox('Select the bowling team', sorted(teams))

selected_city=st.selectbox('Select the city', sorted(cities))
target=st.number_input('Enter the target score')

col3,col4,col5=st.columns(3)
with col3:
    score=st.number_input('Enter the current score')
with col4:
    overs=st.number_input('Enter the number of overs completed')
with col5:
    wickets= st.number_input('Enter the number of wickets fallen')

if st.button('Predict Win Probability'):
    runs_left=target-score
    balls_left= 120-(overs*6)
    wickets_left= 10-wickets
    current_run_rate=score/overs
    required_run_rate=(runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [selected_city], 'current_score':[score],
                             'runs_left': [runs_left], 'balls_left': [balls_left],'wickets_left': [wickets_left],
                             'target': [target], 'current_run_rate': [current_run_rate], 'required_run_rate': [required_run_rate]})

    # st.table(input_df)
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win * 100)) + "%")
    st.header(bowling_team + "- " + str(round(loss * 100)) + "%")
st.markdown(
    "<hr style='margin-top:50px;margin-bottom:10px;'>"
    "<div style='text-align:center; color:grey;'>"
    "</div>",
    unsafe_allow_html=True)