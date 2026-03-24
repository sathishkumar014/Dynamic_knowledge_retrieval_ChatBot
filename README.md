# 📄 Dynamic Knowledge Retrieval ChatBot

## 🚀 Overview
This project is a simple web-based chatbot designed to answer questions about the NextGenHR system.

The chatbot provides information about features, technologies, and working of the NextGenHR AI Interviewer project through a clean and interactive chat interface.

It uses **demo knowledge data that represents the actual NextGenHR project**, allowing users to understand the system in an interactive way.

---

## 🎯 Features

- Simple and interactive chatbot UI
- Built using HTML, CSS, and JavaScript
- Real-time user interaction
- Predefined responses based on NextGenHR project
- Uses demo knowledge representing real project concepts
- Clean chat interface with message bubbles
- Easy to use and lightweight

---

## 🧠 System Architecture

User (Browser)  
        ↓  
HTML Chat Interface  
        ↓  
JavaScript Logic  
        ↓  
Demo Knowledge Base (NextGenHR Data)  
        ↓  
Matching Response  
        ↓  
Display in Chat UI  

---

## 🛠️ Tech Stack

- HTML
- CSS
- JavaScript

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
git clone <your-repo-link>  
cd chatbot  

### 2. Create Virtual Environment (Optional)
python -m venv venv  
venv\Scripts\activate  

### 3. Install Dependencies
pip install flask scikit-learn  

---

## ▶️ Run the Project

python app.py  

Open in browser:  
http://127.0.0.1:5000/  

---

## 📦 Sample Interaction

User:  
What is NextGen HR?  

Bot:  
NextGen HR is an AI-powered virtual interviewer system. (score: 0.82)  

---

## 🧠 How It Works

- Converts text data into numerical vectors using TF-IDF
- Converts user query into vector
- Computes cosine similarity between query and knowledge base
- Returns the most relevant response

---

## ✅ Key Highlights

- Lightweight alternative to full AI chatbots
- No external APIs required
- Fast and efficient retrieval system
- Easy to extend with advanced models (GPT, FAISS)
- Designed for domain-specific knowledge

---

## ⚡ Limitations

- Does not generate new answers (retrieval only)
- Depends on quality of knowledge base
- Limited contextual understanding

---

## 🚀 Future Improvements

- Integrate LLM (GPT) for generative responses
- Add voice input/output support
- Use vector databases (FAISS) for scalability
- Improve context memory

---

## 📌 Note

This project demonstrates a simple yet effective retrieval-based chatbot system, suitable for applications like customer support, FAQ assistants, and domain-specific AI systems.
