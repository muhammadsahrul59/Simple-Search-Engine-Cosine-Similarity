# <div align="center">🔎 Simple Search Engine with Cosine Similarity ✨</div>

## Preview

![demo_gui](https://github.com/user-attachments/assets/c2804b8c-37c9-4ec9-8ad6-0d9cb86b9697)

## Description

Sebuah mesin pencari sederhana yang menggunakan Cosine Similarity.

## Directory

- `/dataset`: stores dataset hadits.
- `README.md`: file that provides information about this GitHub project
- `app.py`: main file to run the GUI on local.
- `notebook.ipynb`: interactive jupyter notebook files to analyze data
- `requirements.txt`: file that stores information about the libraries used in this project

## Setup environment
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install streamlit scikit-learn nltk
```

## Run streamlit app
```
streamlit run app.py
```
or
```
python -m streamlit run app.py
```
