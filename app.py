from flask import Flask, render_template, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import Pinecone
from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()
os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

embeddings = download_hugging_face_embeddings()
index_name = "medicalbot"

docsearch = Pinecone.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_kwargs={"k": 3})

llm = OpenAI(temperature=0.4, max_tokens=500)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

rag_chain = (
    {
        "context": retriever,
        "input": RunnablePassthrough(),
    }
    | prompt
    | llm
)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    response = rag_chain.invoke(msg)
    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
