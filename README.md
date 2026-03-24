# 📄 Chatbot (Dynamic Knowledge Retrieval)

## 🚀 Overview
This project implements a retrieval-based AI chatbot that answers user queries using a predefined knowledge base.

The system uses TF-IDF vectorization and cosine similarity to find the most relevant response from stored data, simulating a lightweight RAG (Retrieval-Augmented Generation) pipeline.

---

## 🎯 Features

- Interactive chatbot UI (modern chat interface)
- Real-time user input handling
- Retrieval-based response generation
- TF-IDF vectorization for text understanding
- Cosine similarity for matching queries
- Top-k response selection
- Confidence score for explainability
- Context-aware responses (basic memory)
- Handles unknown queries gracefully

---

## 🧠 System Architecture

User Input (Browser UI)  
        ↓  
Flask Backend API  
        ↓  
Query Processing  
        ↓  
TF-IDF Vectorization  
        ↓  
Cosine Similarity Matching  
        ↓  
Top-K Relevant Responses  
        ↓  
Return Best Answer  
        ↓  
Display in Chat UI  

---

## 🛠️ Tech Stack

- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript
- NLP Processing: scikit-learn (TF-IDF)
- Similarity: Cosine Similarity
- Language: Python

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
