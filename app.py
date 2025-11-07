import streamlit as st

from dotenv import load_dotenv
from src.core.planner import TravelPlanner

st.set_page_config(page_title='AI Travel Planner')
st.title('AI Travel Itinerary Planner')
st.write('Enter your city and interests to plan your trip.')

load_dotenv()

with st.form('planner'):
    city = st.text_input('Enter the city name for your trip: ')
    interests = st.text_input('Enter your interests (comma-separated)')
    submitted = st.form_submit_button('Generate Itinerary')

    if submitted:
        if city and interests:
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_interest(interests)
            itinerary = planner.create_itinerary()

            st.subheader('📝 Your Itinerary ')
            st.markdown(itinerary)

        else:
            st.warning('Please fill city or interest to move forward')
