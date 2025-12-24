# End-to-end Medical Chatbot (Generative AI + RAG)

A production-ready **Medical Chatbot** built using **Retrieval-Augmented Generation (RAG)** to answer medical questions from your knowledge base.  
It embeds your medical documents, stores vectors in **Pinecone**, and uses an **OpenAI GPT model** to generate grounded answers.

> ⚠️ **Disclaimer:** This project is for educational purposes only and does not provide medical advice.

---

## Features

- ✅ RAG pipeline (retrieve relevant chunks → generate answer)
- ✅ Pinecone vector store for scalable search
- ✅ Environment-based secrets management via `.env`
- ✅ Easy setup: build index once, then run the app
- ✅ Clean project workflow: `store_index.py` → `app.py`

---

## Project Structure

```bash
.
MEDICAL-CHATBOT/
│
├── Data/
│   └── Medical_book.pdf
│
├── research/
│   └── trials.ipynb
│
├── src/
│   ├── __init__.py
│   ├── helper.py        
│   └── prompt.py       
│
├── templates/
│   └── chat.html
│
├── static/
│   └── style.css
│
├── app.py               
├── storeindex.py        
├── template.py          
├── setup.py
├── requirements.txt
└── .env                


```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```
