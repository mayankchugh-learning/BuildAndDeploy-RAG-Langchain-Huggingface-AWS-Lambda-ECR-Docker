from setuptools import find_packages, setup

setup(
    name="qasystem",
    version="0.0.1",
    author="Mayank Chugh",
    author_email="mayankchugh.learning@gmail.com",
    packages=find_packages(),
    install_requires=["langchain","langchainhub","bs4","tiktoken","openai","boto3==1.34.37","langchain_community","chromadb","awscli",
"streamlit",
"pypdf",
"faiss-cpu"]
)
    