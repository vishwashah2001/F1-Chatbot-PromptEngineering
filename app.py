

#import streamlit as st

#def main():
  #  st.title('Formula 1 Chatbot')
  #  st.write('Welcome to the Formula 1 Chatbot! Ask me anything about Formula 1.')

    # Replace 'YOUR_BOTPRESS_URL' with the provided Botpress chatbot URL
  #  botpress_url = 'https://cdn.botpress.cloud/webchat/v2/shareable.html?botId=a12e7caf-134a-4c19-ba5b-e5d2032ef516'
    
    # Embedding the chatbot iframe directly in the Streamlit app HTML template
 #   iframe_html = f'<iframe src="{botpress_url}" width="100%" height="600" frameborder="0"></iframe>'
  #  st.markdown(iframe_html, unsafe_allow_html=True)

#if __name__ == "__main__":
  #  main()
#1
# import streamlit as st
# from openai import OpenAI

# # OpenAI API key
# # (Replace 'YOUR_API_KEY' with your actual OpenAI API key)
# openai_api_key = "sk-proj-xwUxmOs0ZkUegvZYyBuuT3BlbkFJ4wK9AngasGlQ104aLrDb"
# client = OpenAI(api_key=openai_api_key)

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Page Title
# st.title("F1 Chatbot 🏎️")
# st.caption("Ask me anything about Formula One!")

# # Display chat messages
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # User input
# if prompt := st.chat_input("Your question"):
#     # Store user message
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # Display user message
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Generate response from OpenAI
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",  # or "gpt-4" if available
#         messages=[
#             {"role": m["role"], "content": m["content"]}
#             for m in st.session_state.messages
#         ],
#     )

#     # Store assistant's message
#     assistant_message = response.choices[0].message.content
#     st.session_state.messages.append({"role": "assistant", "content": assistant_message})

#     # Display assistant's response
#     with st.chat_message("assistant"):
#         st.markdown(assistant_message)
#2
# import streamlit as st
# from openai import OpenAI
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time

# # Function to fetch F1 standings (only once per session)
# @st.cache_resource  # Caching to avoid refetching on every interaction
# def get_f1_standings():
#     url = "https://www.formula1.com/en/results.html/2024/drivers.html"  # Assuming 2024 season
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     table = soup.find("table", class_="resultsarchive-table")
#     # Convert the table to a DataFrame
#     df = pd.read_html(str(table))[0]
#     df = df[['Pos', 'Driver', 'Nationality', 'Car', 'PTS']]
#     return df
# # Page Title and Introduction
# st.title("F1 Chatbot 🏎️")
# st.caption("Get the latest F1 news, stats, and chat with me about the races!")
# # Fetch Standings (only once when the app loads)
# with st.spinner("Fetching latest F1 standings..."):
#     df_standings = get_f1_standings()
# # Display Standings
# st.subheader("Current Driver Standings")
# st.dataframe(df_standings.style.hide_index().set_properties(**{'text-align': 'center'}))
# # Initialize the OpenAI client and chat history
# openai_api_key = "sk-proj-xwUxmOs0ZkUegvZYyBuuT3BlbkFJ4wK9AngasGlQ104aLrDb"
# client = OpenAI(api_key=openai_api_key)
# if "messages" not in st.session_state:
#     st.session_state.messages = []
# # Chat Interface
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
# # User Input
# if prompt := st.chat_input("Your question"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # Display user message
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     # Response from OpenAI
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",  
#         messages=[
#             {"role": m["role"], "content": m["content"]}
#             for m in st.session_state.messages
#         ],
#     )
#     # Store assistant's message
#     assistant_message = response.choices[0].message.content
#     st.session_state.messages.append({"role": "assistant", "content": assistant_message})
#     # Display assistant's response
#     with st.chat_message("assistant"):
#         st.markdown(assistant_message)
# SOHAM
# import streamlit as st
# from openai import OpenAI
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # Apply a custom theme and page configuration
# st.set_page_config(page_title="F1 Chatbot", page_icon="🏎️", layout="wide")
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #1e1e1e; /* Dark background */
#         color: white;          /* White text */
#     }
#     .css-18e3th9 {
#         padding: 20px;        /* Add padding */
#         border-radius: 10px;  /* Rounded corners */
#     }
#     .st-ae {
#         border-radius: 10px;  /* Rounded corners for chat bubbles */
#     }
#     .st-emotion-cache-v53 {  
#         font-family: 'Racing Sans One', cursive;  /* Optional: Custom font */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Fetch a random F1 image from Unsplash
# def get_unsplash_image(query="formula one"):
#     base_url = "https://api.unsplash.com/photos/random"
#     params = {
#         "query": query,
#         "client_id": "YOUR_UNSPLASH_ACCESS_KEY"  # Replace with your Unsplash API key
#     }
#     response = requests.get(base_url, params=params)
#     if response.status_code == 200:
#         data = response.json()
#         return data["urls"]["regular"]  # Get the regular-sized image URL
#     else:
#         return None  # Return None if the request fails

# # Display a random F1 image
# image_url = get_unsplash_image()
# if image_url:
#     st.image(image_url, use_column_width=True)

# # Title and Introduction
# st.title("F1 Chatbot 🏎️")
# st.caption("Your pit stop for F1 news, stats, and expert analysis!")

# # Fetch Standings (cache to avoid re-fetching)
# @st.cache_resource
# def get_f1_standings():
#     url = "https://www.formula1.com/en/results.html/2024/drivers.html"  # Assuming 2024 season
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     table = soup.find("table", class_="resultsarchive-table")
#     df = pd.read_html(str(table))[0]
#     df = df[['Pos', 'Driver', 'Nationality', 'Car', 'PTS']]
#     return df

# # Filter Drivers by Nationality
# def filter_drivers_by_nationality(df, nationality):
#     return df[df["Nationality"] == nationality]

# # Fetch and Display Current Standings
# with st.spinner("Analyzing the grid..."): 
#     df_standings = get_f1_standings()

# # Filter options
# selected_nationality = st.selectbox("Filter by Nationality", df_standings["Nationality"].unique())
# filtered_standings = filter_drivers_by_nationality(df_standings, selected_nationality)

# # Remove Index Column before Styling
# filtered_standings = filtered_standings.reset_index(drop=True)

# st.subheader("Current Driver Standings")
# st.dataframe(filtered_standings.style.set_properties(**{'text-align': 'center'}))

# # Chatbot logic
# openai_api_key = "sk-proj-xwUxmOs0ZkUegvZYyBuuT3BlbkFJ4wK9AngasGlQ104aLrDb"  # Replace with your OpenAI API key
# client = OpenAI(api_key=openai_api_key)

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# if prompt := st.chat_input("Your question"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",  
#         messages=[
#             {"role": m["role"], "content": m["content"]}
#             for m in st.session_state.messages
#         ],
#     )
#     assistant_message = response.choices[0].message.content
#     st.session_state.messages.append({"role": "assistant", "content": assistant_message})
#     with st.chat_message("assistant"):
#         st.markdown(assistant_message)

#VISHWA LAST WORKING
# import streamlit as st
# import openai
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from datetime import datetime, timedelta

# # F1-Themed Styling
# st.set_page_config(page_title="F1 Expert", page_icon="🏎️", layout="wide")
# st.markdown("""
# <style>
# body { background-color: #1e1e1e; color: white; }
# header { font-family: 'Racing Sans One', cursive; font-size: 2em; text-align: center; margin-top: 10px; margin-bottom: 10px; }
# footer { font-family: 'Racing Sans One', cursive; font-size: 1em; text-align: center; margin-top: 20px; }
# .css-18e3th9 { padding: 20px; border-radius: 10px; }
# .st-ae { border-radius: 10px; }
# .st-emotion-cache-v53 { font-family: 'Racing Sans One', cursive; }
# h1, h2, h3, h4, h5, h6 { color: #ff1e00; }
# .chat-message { border-radius: 5px; padding: 10px; margin-bottom: 10px; }
# .user-message { background-color: #ffcccb; color: black; }
# .assistant-message { background-color: #d1e7dd; color: black; }
# </style>
# """, unsafe_allow_html=True)

# # Fetch Latest F1 Standings and Schedule (Cache with Expiry)
# @st.cache_data(ttl=3600)  # Cache for 1 hour (adjust as needed)
# def get_f1_data():
#     standings_url = "https://www.formula1.com/en/results/driver-standings.html"
#     schedule_url = "https://www.formula1.com/en/results.html"

#     standings_response = requests.get(standings_url)
#     schedule_response = requests.get(schedule_url)

#     if standings_response.status_code == 200 and schedule_response.status_code == 200:
#         standings_soup = BeautifulSoup(standings_response.content, "html.parser")
#         schedule_soup = BeautifulSoup(schedule_response.content, "html.parser")
        
#         # Extract race schedule data
#         schedule_elements = schedule_soup.find_all("a", class_="event-item")
#         schedule_data = []
#         for element in schedule_elements:
#             race_name = element.find("span", class_="event-title").text
#             race_date_str = element.find("span", class_="start-date").text
#             race_date = datetime.strptime(race_date_str, "%d %b").replace(year=datetime.now().year)
#             if race_date < datetime.now():  # Skip past races
#                 continue
#             schedule_data.append({"name": race_name, "date": race_date})
            
#         # Extract driver standings data
#         standings_table = standings_soup.find("table", class_="resultsarchive-table")
#         standings_df = pd.read_html(str(standings_table))[0]
#         standings_df = standings_df[['Pos', 'Driver', 'Nationality', 'Car', 'PTS']]

#         return standings_df, schedule_data

#     else:
#         return pd.DataFrame(), []

# # Display F1 Standings and Schedule
# standings_df, schedule_data = get_f1_data()

# # Header
# st.markdown('<header>F1 Expert 🏎️</header>', unsafe_allow_html=True)
# st.caption("Your personalized guide to the Formula 1 world!")

# # Layout: Standings and Filters
# st.subheader("Current Driver Standings")
# col1, col2 = st.columns([1, 3])

# # Filter options with "All" option
# nationality_options = ["All"] + standings_df["Nationality"].unique().tolist()
# selected_nationality = col1.selectbox("Filter by Nationality", nationality_options)

# if selected_nationality == "All":
#     filtered_standings = standings_df
# else:
#     filtered_standings = standings_df[standings_df["Nationality"] == selected_nationality]

# filtered_standings = filtered_standings.reset_index(drop=True)
# col2.dataframe(filtered_standings.style.set_properties(**{'text-align': 'center'}))

# # Display Upcoming Races
# st.subheader("Upcoming Races")
# for race in schedule_data:
#     st.markdown(f"**{race['name']}**: {race['date'].strftime('%Y-%m-%d')}")

# # OpenAI Chatbot Integration (F1-Specific with System Message)
# openai.api_key = "sk-proj-xwUxmOs0ZkUegvZYyBuuT3BlbkFJ4wK9AngasGlQ104aLrDb"  # Replace with your ACTUAL API key

# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {"role": "system", "content": "You are an expert in Formula 1 racing. Answer questions about F1 drivers, teams, races, history, rules, and any other relevant F1 topics. Please be concise and informative."}
#     ]

# # Chat container
# st.subheader("Ask the F1 Expert")
# chat_container = st.container()

# # Display messages
# for message in st.session_state.messages:
#     with chat_container:
#         if message["role"] == "user":
#             st.markdown(f"<div class='chat-message user-message'>{message['content']}</div>", unsafe_allow_html=True)
#         else:
#             st.markdown(f"<div class='chat-message assistant-message'>{message['content']}</div>", unsafe_allow_html=True)

# # User input for chat
# if prompt := st.chat_input("Ask me about F1..."):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with chat_container:
#         st.markdown(f"<div class='chat-message user-message'>{prompt}</div>", unsafe_allow_html=True)

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=st.session_state.messages,
#     )

#     assistant_message = response.choices[0].message['content']
#     st.session_state.messages.append({"role": "assistant", "content": assistant_message})
#     with chat_container:
#         st.markdown(f"<div class='chat-message assistant-message'>{assistant_message}</div>", unsafe_allow_html=True)

# # Footer
# st.markdown('<footer>Powered by OpenAI & Streamlit</footer>', unsafe_allow_html=True)# import streamlit as st
# from openai import OpenAI
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time


# # Function to fetch F1 standings (only once per session)
# @st.cache_resource  # Caching to avoid refetching on every interaction
# def get_f1_standings():
#     url = "https://www.formula1.com/en/results.html/2024/drivers.html"  # Assuming 2024 season
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     table = soup.find("table", class_="resultsarchive-table")

#     # Convert the table to a DataFrame
#     df = pd.read_html(str(table))[0]
#     df = df[['Pos', 'Driver', 'Nationality', 'Car', 'PTS']]
#     return df

# # Page Title and Introduction
# st.title("F1 Chatbot 🏎️")
# st.caption("Get the latest F1 news, stats, and chat with me about the races!")

# # Fetch Standings (only once when the app loads)
# with st.spinner("Fetching latest F1 standings..."):
#     df_standings = get_f1_standings()

# # Display Standings
# st.subheader("Current Driver Standings")
# st.dataframe(df_standings.style.hide_index().set_properties(**{'text-align': 'center'}))

# # Initialize the OpenAI client and chat history
# openai_api_key = "sk-proj-xwUxmOs0ZkUegvZYyBuuT3BlbkFJ4wK9AngasGlQ104aLrDb"
# client = OpenAI(api_key=openai_api_key)

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Chat Interface
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # User Input
# if prompt := st.chat_input("Your question"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # Display user message
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Response from OpenAI
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",  
#         messages=[
#             {"role": m["role"], "content": m["content"]}
#             for m in st.session_state.messages
#         ],
#     )

#     # Store assistant's message
#     assistant_message = response.choices[0].message.content
#     st.session_state.messages.append({"role": "assistant", "content": assistant_message})

#     # Display assistant's response
#     with st.chat_message("assistant"):
#         st.markdown(assistant_message)

import streamlit as st
import openai
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
import base64
import streamlit as st
import requests
import base64

# F1-Themed Styling
st.set_page_config(page_title="F1 Expert", page_icon="🏎️", layout="wide")

# Function to fetch an image from Unsplash
def fetch_image():
    client_id = "eWZJSdWEt5x6lfUatkigWFkrTv6r_fR3f4J04Dyuyrk"  # Replace with your Unsplash Access Key
    query = "Formula 1"
    url = f"https://api.unsplash.com/photos/random?query={query}&client_id={client_id}"
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        image_url = json_data['urls']['regular']
        return image_url
    else:
        return "https://fallback_image_url.jpg"  # A fallback image URL in case API fails

# Get the image URL
background_image_url = fetch_image()

# Using the image as a background
st.markdown(f"""
<style>
body {{
    background-image: url("{background_image_url}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color: white;
    font-family: 'Racing Sans One', cursive;
}}
header {{
    font-size: 2em;
    text-align: center;
    margin-top: 10px;
    margin-bottom: 10px;
}}
footer {{
    font-size: 1em;
    text-align: center;
    margin-top: 20px;
}}
.css-18e3th9 {{
    padding: 20px;
    border-radius: 10px;
    background-color: rgba(0, 0, 0, 0.5);  # Semi-transparent background for containers
}}
.st-ae {{
    border-radius: 10px;
}}
h1, h2, h3, h4, h5, h6 {{
    color: #ff1e00;  # Bright red for headings
}}
.chat-message {{
    border-radius: 5px;
    padding: 10px;
    margin-bottom: 10px;
    background-color: rgba(255, 255, 255, 0.8);  # Semi-transparent background for chat
}}
.user-message {{
    color: black;
}}
.assistant-message {{
    color: black;
}}
</style>
""", unsafe_allow_html=True)

# Fetch Latest F1 Standings and Schedule (Cache with Expiry)
@st.cache_data(ttl=3600)  # Cache for 1 hour (adjust as needed)
def get_f1_data():
    standings_url = "https://www.formula1.com/en/results/driver-standings.html"
    schedule_url = "https://www.formula1.com/en/results.html"

    standings_response = requests.get(standings_url)
    schedule_response = requests.get(schedule_url)

    if standings_response.status_code == 200 and schedule_response.status_code == 200:
        standings_soup = BeautifulSoup(standings_response.content, "html.parser")
        schedule_soup = BeautifulSoup(schedule_response.content, "html.parser")
        
        # Extract race schedule data
        schedule_elements = schedule_soup.find_all("a", class_="event-item")
        schedule_data = []
        for element in schedule_elements:
            race_name = element.find("span", class_="event-title").text
            race_date_str = element.find("span", class_="start-date").text
            race_date = datetime.strptime(race_date_str, "%d %b").replace(year=datetime.now().year)
            if race_date < datetime.now():  # Skip past races
                continue
            schedule_data.append({"name": race_name, "date": race_date})
            
        # Extract driver standings data
        standings_table = standings_soup.find("table", class_="resultsarchive-table")
        standings_df = pd.read_html(str(standings_table))[0]
        standings_df = standings_df[['Pos', 'Driver', 'Nationality', 'Car', 'PTS']]

        return standings_df, schedule_data

    else:
        return pd.DataFrame(), []

# Display F1 Standings and Schedule
standings_df, schedule_data = get_f1_data()

# Header
st.markdown('<header>F1 Expert 🏎️</header>', unsafe_allow_html=True)
st.caption("Your personalized guide to the Formula 1 world!")

# Layout: Standings and Filters
st.subheader("Current Driver Standings")
col1, col2 = st.columns([1, 3])

# Filter options with "All" option
nationality_options = ["All"] + standings_df["Nationality"].unique().tolist()
selected_nationality = col1.selectbox("Filter by Nationality", nationality_options)

if selected_nationality == "All":
    filtered_standings = standings_df
else:
    filtered_standings = standings_df[standings_df["Nationality"] == selected_nationality]

filtered_standings = filtered_standings.reset_index(drop=True)
col2.dataframe(filtered_standings.style.set_properties(**{'text-align': 'center'}))

# Display Upcoming Races
st.subheader("Upcoming Races")
for race in schedule_data:
    st.markdown(f"**{race['name']}**: {race['date'].strftime('%Y-%m-%d')}")

# OpenAI Chatbot Integration (F1-Specific with System Message)
openai.api_key = "sk-proj-xwUxmOs0ZkUegvZYyBuuT3BlbkFJ4wK9AngasGlQ104aLrDb"  # Replace with your ACTUAL API key

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are an expert in Formula 1 racing. Answer questions about F1 drivers, teams, races, history, rules, and any other relevant F1 topics. Please be concise and informative."}
    ]

# Chat container
st.subheader("Ask the F1 Expert")
chat_container = st.container()

# Display messages
for message in st.session_state.messages:
    with chat_container:
        if message["role"] == "user":
            st.markdown(f"<div class='chat-message user-message'>{message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-message assistant-message'>{message['content']}</div>", unsafe_allow_html=True)

# User input for chat
if prompt := st.chat_input("Ask me about F1..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with chat_container:
        st.markdown(f"<div class='chat-message user-message'>{prompt}</div>", unsafe_allow_html=True)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages,
    )

    assistant_message = response.choices[0].message['content']
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
    with chat_container:
        st.markdown(f"<div class='chat-message assistant-message'>{assistant_message}</div>", unsafe_allow_html=True)

# Footer
st.markdown('<footer>Powered by OpenAI & Streamlit</footer>', unsafe_allow_html=True)