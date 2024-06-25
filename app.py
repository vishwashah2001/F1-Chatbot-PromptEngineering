import streamlit as st
import openai
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

# --- App Configuration ---
st.set_page_config(page_title="F1 Chatbot", page_icon="🏎️", layout="wide")

# --- Custom CSS Styling ---
st.markdown(
    """
    <style>
    /* ... your existing CSS styles ... */

    /* Additional/Modified CSS Rules for Responsiveness and Visuals */
    .chat-container {
        height: 60vh; /* Dynamic height based on viewport */
    }

    .message {
        max-width: 85%; /* More responsive on various screens */
        word-wrap: break-word; /* Prevent text from overflowing */
        margin-bottom: 15px; /* Better spacing between messages */
    }

    .sidebar {
        background-color: #fff; /* Match sidebar background to main content */
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Data Fetching (with Caching) ---
@st.cache_data(ttl=3600)  # Cache data for 1 hour (adjust as needed)
def get_f1_standings(year=None):
    year = year or datetime.datetime.now().year
    url = f"https://www.formula1.com/en/results.html/{year}/drivers.html"

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", class_="resultsarchive-table")
        if table:
            df = pd.read_html(str(table))[0]
            return df[['Pos', 'Driver', 'Nationality', 'Car', 'PTS']]
        else:
            st.sidebar.warning("Could not find F1 standings table on the page.")

    except (requests.exceptions.RequestException, ValueError) as e:
        st.sidebar.error(f"Error fetching F1 standings: {e}")
        return None  

# --- OpenAI API Setup ---
openai.api_key = "sk-proj-xwUxmOs0ZkUegvZYyBuuT3BlbkFJ4wK9AngasGlQ104aLrDb"  # Replace with your actual API key

# --- Function to Check F1 Relevance ---
def is_f1_related(prompt):
    f1_keywords = [
        "f1", "formula 1", "formula one", "race", "driver", "team",
        "grand prix", "pit stop", "qualifying", "standings", "circuit",
        "pole position", "constructor", "championship", "grid", "lap", 
        "pit lane", "fastest lap", "race engineer", "aerodynamics", "downforce"
    ]
    return any(keyword in prompt.lower() for keyword in f1_keywords)

# --- Sidebar Content ---
st.sidebar.title("F1 Driver Standings")
df_standings = get_f1_standings()

if df_standings is not None:
    selected_nationality = st.sidebar.selectbox("Filter by Nationality", ["All"] + df_standings["Nationality"].unique().tolist())
    filtered_standings = df_standings if selected_nationality == "All" else df_standings[df_standings["Nationality"] == selected_nationality]
    st.sidebar.dataframe(filtered_standings.style.set_properties(**{'text-align': 'center'}))
else:
    st.sidebar.warning("F1 standings are currently unavailable. Please try again later.")


# --- Main Chat Interface ---
st.title("F1 Chatbot 🏎️")
st.caption("Your pit stop for F1 news, stats, and expert analysis!")

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.sidebar.button("Restart Chat"):
    st.session_state.messages = []
    st.experimental_rerun()

# Display chat messages
for message in st.session_state.messages:
    st.markdown(f'<div class="message {"user-message" if message["role"] == "user" else "assistant-message"}">{message["content"]}</div>', unsafe_allow_html=True)

# --- Input Box and Send Button ---
prompt = st.text_input("", key="input", placeholder="Type your message here...")
send_disabled = not bool(prompt.strip())

if st.button("Send", key="send", disabled=send_disabled):
    if is_f1_related(prompt):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Send message to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
        )
        assistant_message = response.choices[0].message["content"]
        
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})
        st.experimental_rerun()
    else:
        st.warning("This chatbot only answers F1-related questions.")
