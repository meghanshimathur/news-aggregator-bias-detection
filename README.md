# 📰 News Aggregator & Bias Detection Agent

An AI-powered **News Aggregation and Political Bias Detection System** built using **Flask**, **CrewAI**, and **Transformer-based NLP models**.

The system fetches live news from **The Guardian API**, generates concise summaries, and detects potential political bias.

---

## 💡 Problem Statement

With the growing volume of online news, users often struggle to quickly understand content and identify political bias.

This project aims to:

- Aggregate real-time news articles
- Automatically summarize long-form content
- Detect political bias using NLP models
- Present insights through a simple web interface

---

## 🌐 Live Demo

🔗 **Deployed Application:**  
https://news-aggregator-bias-detection.onrender.com

---

## 🚀 Features

- 🔍 Fetches latest news articles (Politics, Technology, World)
- 🧠 AI-based news summarization
- ⚖️ Political bias detection (Right Bias / Neutral)
- 🤖 Multi-agent architecture using CrewAI
- 🌐 Flask-based web interface
- 🖥️ Optimized for CPU-only execution (macOS compatible)

---

## 🧠 System Architecture

The project follows a **multi-agent AI workflow**:

| Agent Name | Responsibility |
|------------|----------------|
| News Data Collector | Fetches real-time news from The Guardian |
| News Summarizer | Generates concise summaries |
| Bias Analyzer | Detects political bias with confidence score |

Agents are executed sequentially using **CrewAI**.

Flow:

User → Flask App → Guardian API → NLP Models → Bias Detection → Web Output

---

## 🛠 Tech Stack

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
---
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

---
🚀 Future Improvements

- Add support for multiple news sources
- Improve bias classification accuracy
- Add user authentication
- Store historical summaries
- Deploy with scalable cloud infrastructure
---
📌 Resume Highlight

Built an AI-powered Flask web application integrating The Guardian API and transformer-based NLP models for automated news summarization and political bias detection using multi-agent orchestration.


