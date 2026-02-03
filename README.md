# 📰 News Aggregator & Bias Detection Agent

An AI-powered **News Aggregation and Political Bias Detection System** built using **Flask**, **CrewAI**, and **Transformer-based NLP models**.  
The system fetches live news from **The Guardian API**, summarizes articles, and detects potential political bias.

---
## 🌐 Live Demo

🔗 **Deployed Application:**  
https://news-aggregator-bias-detection.onrender.com

## 🚀 Features

- 🔍 Fetches latest news articles (Politics, Technology, World)
- 🧠 AI-based news summarization
- ⚖️ Political bias detection (Right Bias / Neutral)
- 🤖 Multi-agent architecture using CrewAI
- 🌐 Web interface built with Flask
- 🖥️ Optimized for CPU-only execution (macOS safe)

---

## 🧠 System Architecture

The project follows a **multi-agent AI workflow**:

| Agent Name | Responsibility |
|----------|----------------|
| News Data Collector | Fetches real-time news from The Guardian |
| News Summarizer | Generates concise and neutral summaries |
| Bias Analyzer | Detects political bias with confidence score |

Agents are executed sequentially using **CrewAI**.

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Backend Framework:** Flask  
- **AI Framework:** CrewAI  
- **NLP Models:**  
  - `facebook/bart-large-cnn` – Summarization  
  - `facebook/bart-large-mnli` – Bias Detection  
- **API Used:** The Guardian Open API  
- **Frontend:** HTML (Jinja2 Templates)

---

## 📂 Project Structure

```text
news-aggregator-bias-detection/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── .env                # not uploaded
└── README.md

---

⚙️ Installation & Setup

1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/news-aggregator-bias-detection.git
cd news-aggregator-bias-detection

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Environment Variables
Create a .env file in the root directory and add:

GUARDIAN_API_KEY=your_guardian_api_key_here

You can generate your API key from:

https://open-platform.theguardian.com/

4️⃣ Run the Application
python3.11 app.py
```
📊 Output Example

For each news article, the system displays:

- Headline**
- AI-generated Summary
- Detected Political Bias
  - Right Bias
  - Neutral
- Confidence Score (visual indicator)

## 🎓 Educational Use

This project is intended **strictly for educational and academic purposes**, including:

- Understanding news aggregation using public APIs  
- Applying NLP models for text summarization  
- Exploring political bias detection with transformer models  
- Learning multi-agent orchestration using CrewAI  
- Building and deploying Flask-based AI applications  








