
# 🏎️ F1 Expert Streamlit App

## 📋 Introduction
The **F1 Expert** is a Streamlit-based web application designed to provide users with real-time information about Formula 1, including the latest driver standings, race schedules, and interactive Q&A sessions powered by OpenAI’s GPT-3.5 model. This app is a go-to resource for Formula 1 fans who want a quick, informative, and interactive way to stay updated on the sport they love.

## ✨ Features
- 🏆 **Current Driver Standings**: Get the latest standings of Formula 1 drivers in the ongoing championship.
- 📅 **Upcoming Races**: Stay informed about upcoming F1 races with details on dates and venues.
- 🤖 **Interactive F1 Q&A**: Ask F1-related questions and receive AI-generated answers using OpenAI’s GPT-3.5.
- 🌄 **Dynamic Backgrounds**: Enjoy visually appealing background images related to F1, dynamically fetched from Unsplash.

## ⚙️ Installation

### 🛠️ Prerequisites
Ensure you have the following installed on your system:
- **Python** 3.7 or higher
- **Pip** (Python package manager)
- **API key from OpenAI** (for GPT-3.5)
- **API key from Unsplash** (for fetching background images)

### 📝 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/f1-expert-app.git
   cd f1-expert-app
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API keys:**
   - Create a `.env` file in the root directory.
   - Add your OpenAI and Unsplash API keys in the following format:
     ```bash
     OPENAI_API_KEY=your_openai_api_key_here
     UNSPLASH_ACCESS_KEY=your_unsplash_access_key_here
     ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## 🚀 Usage
Once the app is running, open your browser and navigate to [http://localhost:8501](http://localhost:8501).

- **View F1 Standings**: Check the latest driver standings.
- **Explore Upcoming Races**: Discover upcoming races, including dates and locations.
- **Interact with F1 Expert**: Ask questions about F1, and the app will provide AI-generated responses.
- **Nationality Filter**: Filter driver standings by nationality to focus on specific drivers from different countries.

## 🛠️ Troubleshooting
- **🖼️ Image Not Displaying**: Ensure that your Unsplash API key is correct, valid, and hasn't exceeded the usage limit. Check your network settings if the background images do not load.
- **🔑 API Errors**: Double-check that both OpenAI and Unsplash API keys are properly set in the `.env` file. Ensure you have not hit any API usage limits.
- **🔄 Local Development Issues**: If the changes you make in the UI aren’t reflecting, try clearing your browser cache or restarting the Streamlit server.
