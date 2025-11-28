📊 Live Stock Dashboard (Python + Streamlit + Pandas + Plotly + yFinance)

A real-time Stock Price Dashboard that fetches live market data, visualizes stock trends, and displays key financial insights using Python.
This project is beginner-friendly yet portfolio-worthy, showcasing real-world data handling and interactive dashboards.

🚀 Features

✨ Fetches live stock market data using yFinance
✨ Shows line chart & candlestick chart
✨ Displays summary metrics:

Open

Close

High

Low

Volume

Change %

✨ Built with clean modular structure (industry style)
✨ Fully interactive Streamlit dashboard
✨ Works for any stock symbol (AAPL, TSLA, RELIANCE.NS, TCS.NS etc.)

📂 Project Structure
Live_Stock_Dashboard/
│
├── stock_dashboard.py         # Main Streamlit dashboard UI
├── requirements.txt           # Required Python libraries
├── README.md                  # Project documentation
└── utils/
     └── stock_functions.py    # Functions for data fetching and processing

🧩 Why This Structure?
📌 stock_dashboard.py

This is the main dashboard file.
It handles:

UI layout

Input box for stock ticker

Displaying charts

Showing summary metrics

👉 Acts as the presentation layer (front-end).

📌 utils/stock_functions.py

Contains all the backend logic:

Fetch stock data

Clean/format data

Create summary stats

Handle empty data safely

👉 Acts as the brain (business logic layer), keeping the project clean and modular.

📌 requirements.txt

Includes all libraries needed to run the project:

pandas
yfinance
plotly
streamlit


👉 Helps others install everything quickly using:

pip install -r requirements.txt

📌 README.md

This file (you’re reading it!) explains the project clearly for:

Recruiters

Developers

Students

GitHub visitors

👉 Think of it as your project brochure.

⚙️ Technologies Used
Technology	Purpose
🐍 Python	Core programming
📦 Pandas	Data cleaning & manipulation
💹 yFinance	Fetch live stock data
📈 Plotly	Data visualization
🌐 Streamlit	Build interactive dashboard
▶️ How to Run the Dashboard
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit Dashboard
streamlit run stock_dashboard.py

📈 Dashboard Preview (Description)
📉 Line Chart

Shows closing price trend for the selected stock.

🕯 Candlestick Chart

Shows Open, High, Low, Close for deeper analysis (used by traders).

📊 Summary Metrics

Highlights the most important numbers:

Today's change

Volume

High/Low

Last Open/Close

🧠 What You Learn From This Project

✔ How to fetch real-time data using APIs
✔ How to build dashboards using Streamlit
✔ How to visualize datasets with Plotly
✔ Clean folder structure & modular programming
✔ How to calculate summary statistics
✔ How to handle errors safely

This adds huge value to your portfolio and interview preparation.

🔮 Future Enhancements

🟦 Add SMA / EMA trend indicators
🟦 Add multiple stock comparison
🟦 Add buy/sell signals
🟦 Deploy the dashboard online
🟦 Add SQL / NoSQL database integration

🤝 Contributing

Pull requests are welcome!
Feel free to fork, modify, and enhance this project.

⭐ Support

If you find this project useful, please star ⭐ the repository — it motivates me to build more amazing projects.

🙏 Thank You

Made with ❤️ using Python, Pandas, Plotly & Streamlit.
Happy Coding! 🚀