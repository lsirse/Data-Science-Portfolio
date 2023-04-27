#!/usr/bin/env python
# coding: utf-8

import os
import ast
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from config import *

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


# Let's load the letters to shareholders
print("Loading letters to shareholders...")
loader = DirectoryLoader("data/")
docs = loader.load()


# Setting the embeddings model

embeddings = OpenAIEmbeddings(model=EMBEDDINGS_MODEL)


# Let's split all the letters to shareholders into separate files
print("Splitting data into chunks...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20,
    length_function=len,
)

texts = []
metadatas = []
for single_doc in docs:
    for single_part in text_splitter.split_text(single_doc.page_content):
        # Storing all split docs in single variable
        texts += [single_part]
        # Metadata is saved in order to understand which letters the answer was synthesized from
        metadatas += [ast.literal_eval(single_doc.json())["metadata"]]

print("Generating embeddings...")
# Let's generate embeddings and store them in the chromadb
docsearch = Chroma.from_texts(texts, embeddings, metadatas=metadatas)

print("Emeddings successfully generated...")

def answer_question_from_letters(
    query, k_docs_to_generate_answer_from=K_DOCS_TO_GENERATE_ANSWER_FROM
):
    docs = docsearch.similarity_search(query, k=k_docs_to_generate_answer_from)
    chain = load_qa_with_sources_chain(OpenAI(temperature=0), chain_type="refine")

    return chain({"input_documents": docs, "question": query}, return_only_outputs=True)

print("─────────███─────────")
print("─────────█$█─────────")
print("─────█████$██████────")
print("───███████$████████──")
print("──████████$████████──")
print("─█████████$████████──")
print("─███████─█$█──████───")
print("─███████─█$█─────────")
print("─█████████$█─────────")
print("─█████████$█████─────")
print("──████████$███████───")
print("────██████$█████████─")
print("───────███$█████████─")
print("─────────█$█─████████")
print("─────────█$█──███████")
print("──████───█$█──███████")
print("─█████████$█████████─")
print("██████████$█████████─")
print("─█████████$████████──")
print("───███████$██████────")
print("─────────█$█─────────")
print("─────────███─────────")


while True:
    query = input(
        "Please enter (another) question to answer from the content of Warren Buffett's letters to shareholders (years 1978 - 2022) or type 'exit' to quit: "
    )

    if query.lower() == "exit":
        print("Goodbye!")
        break
    else:
        print(f"You entered: {query}")
        print("Generating the answer, it may take some time...")
        result = answer_question_from_letters(query)
        
        print("Here's the answer generated:")
        print(result)
