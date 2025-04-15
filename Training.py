from langchain.document_loaders import DirectoryLoader
import os
DATA_PATH = os.getcwd()

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob='*.md')
    documents = loader.load()
    return documents

