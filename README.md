# 🚀 DataPilot

**DataPilot** is a lightweight, local-first analytics engine that lets you query spreadsheets using plain English.

Upload a CSV or Excel → ask a question → AI generates SQL → DuckDB executes → results show as tables **and charts**.

Think:

**ChatGPT + SQL + DuckDB + Charts**  
All running locally. No cloud. No external APIs. No heavy BI tools.

---

## ✨ What you can ask

Try queries like:

- total revenue by year  
- sum of sales by region  
- average price per product  
- top 5 rows  
- group by month  
- average talk time per agent  

---

## ⚙️ How it works

```
file → pandas → DuckDB table
question → embeddings → FAISS → reranker → prompt → LLM → SQL
SQL → DuckDB → JSON → table + charts
```

Natural language in.  
SQL + charts out.

---

## 🧠 Architecture

```
Frontend (Vite + JS)
        ↓
FastAPI Backend (REST API)
        ↓
RAG SQL Engine (Embeddings + FAISS + Reranker + LLM)
        ↓
Generated SQL
        ↓
DuckDB execution
        ↓
Tables + Charts
```

---

## 🧩 Tech Stack

### Backend
- FastAPI
- DuckDB
- Pandas

### AI / ML
- Sentence Transformers (bi-encoder embeddings)
- FAISS (vector similarity search)
- Cross-encoder reranker
- Local LLM (TinyLlama / Mistral)
- Retrieval-Augmented Generation (RAG)

### Frontend
- Vite
- Vanilla JavaScript
- Chart.js

---

## 🔥 Core Feature

### Natural Language → SQL

**Input**
```
average revenue by region
```

**Generated automatically**
```sql
SELECT region, AVG(revenue)
FROM sales
GROUP BY region;
```

Executed instantly inside DuckDB.

---

## ✨ Features

- CSV + Excel upload
- automatic schema detection
- column normalization
- safe SQL generation (SELECT only)
- semantic schema retrieval
- DuckDB OLAP queries (very fast)
- automatic table rendering
- automatic chart creation
- fully local inference
- zero cloud dependencies

---

## 📂 Project Structure

```
app/        API + ingestion + endpoints
rag/        embeddings + retriever + SQL generator
frontend/   UI + charts
tests_rag/  model tests
```

---

# 🚀 Run Locally

## 1. Clone the repo

```bash
git clone https://github.com/<not-aryan7>/DataPilot.git
cd DataPilot
```

---

## 2. Backend (FastAPI + DuckDB)

### Create virtual environment
```bash
python -m venv venv
```

### Activate

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Start API
```bash
uvicorn app.main:app --reload
```

Backend → http://127.0.0.1:8000  
Docs → http://127.0.0.1:8000/docs

---

## 3. Frontend (Vite)

Open a **new terminal**

```bash
cd frontend
npm install
npm run dev
```

Frontend → http://localhost:5173

---

## 4. Use the app

1. Upload CSV or Excel  
2. Ask questions in plain English  
3. Get SQL + tables + charts instantly  

---

## 5. Stop everything

```bash
CTRL + C
deactivate
```

---

## 🛡 Safety

- SELECT queries only  
- no DROP / DELETE / UPDATE  
- runs fully offline  
- designed for small/medium datasets  

---

## 🎯 Why we built this

To practice building complete **end-to-end AI systems** that combine:

- backend APIs
- analytical databases
- vector search
- LLM pipelines
- frontend visualization

Instead of cloud tools, everything runs locally for privacy, speed, and zero cost.

---

## 👨‍💻 Authors

**Ayush Neupane**  
**Aryan RajBhandari**  

Computer Science + Economics  
Building applied AI & data engineering systems
