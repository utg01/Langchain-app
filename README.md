🌐 LangChain Health Assistant

A simple AI-powered health Q&A app built with Streamlit, LangChain, and Google Gemini API.

✨ Features

🤖 Health-focused AI Assistant – Answers only health-related queries.

⚡ Powered by Google Gemini via langchain-google-genai.

🧩 LangChain Integration – Prompt templates & output parsing.

📊 LangSmith Tracing – Debug and monitor your LLM chains.

🌍 Deployable on Streamlit Cloud – Share with anyone instantly.

📂 Project Structure
langchain-health-demo/
│── app.py              # Main Streamlit app
│── requirements.txt    # Dependencies
│── .gitignore          # Ignore venv, .env, cache files
│── README.md           # Project documentation

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/utg01/langchain-health-demo.git
cd langchain-health-demo

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Environment Variables

Create a .env file locally (⚠️ don’t upload this to GitHub):

GOOGLE_API_KEY=your_google_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=langchain-health-demo

▶️ Run Locally
streamlit run app.py


Then open 👉 http://localhost:8501
 in your browser.

🌍 Deploy to Streamlit Cloud

Push this repo to GitHub.

Go to Streamlit Community Cloud
.

Connect your repo → choose app.py.

In App Settings → Secrets, add:

GOOGLE_API_KEY="your_google_api_key_here"
LANGCHAIN_API_KEY="your_langsmith_api_key_here"
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_PROJECT="langchain-health-demo"


Deploy 🚀

🛠 Tech Stack

Streamlit
 – Web UI

LangChain
 – Prompt & chain management

LangSmith
 – Tracing & monitoring

Google Gemini API
 – LLM backend

📸 Preview

(You can add a screenshot/gif of your app here once it runs)

🙌 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

📜 License

This project is licensed under the MIT License.
