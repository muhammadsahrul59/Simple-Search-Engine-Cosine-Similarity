import os
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

# Definisikan stopwords bahasa Indonesia
stop_words = stopwords.words("indonesian")


# Fungsi untuk membaca dokumen dari folder "hadits"
def load_documents_from_folder(folder_path):
    documents = []
    filenames = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(
                os.path.join(folder_path, filename), "r", encoding="utf-8"
            ) as file:
                documents.append(file.read())
                filenames.append(filename)
    return documents, filenames


# Load dokumen dari folder 'hadits'
folder_path = "dataset/hadits"  # Path folder tempat file txt berada
documents, filenames = load_documents_from_folder(folder_path)


# Fungsi untuk menghitung cosine similarity
def get_cosine_similarity(query, documents):
    vectorizer = TfidfVectorizer(stop_words=stop_words, max_features=5000)
    # Gabungkan query dan documents
    all_texts = [query] + documents
    # Transformasi teks menjadi matriks TF-IDF
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    # Hitung cosine similarity antara query dan dokumen
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    return cosine_sim[0]  # Kembalikan skor kesamaan untuk setiap dokumen


# Buat title
st.title("Search Engine Sederhana Hadits")

# Input untuk pertanyaan dari pengguna
query = st.text_input("Masukkan pertanyaan:")

# Tombol untuk mencari
if st.button("Cari"):
    if query:
        # Hitung cosine similarity
        similarity_scores = get_cosine_similarity(query, documents)
        # Gabungkan hasil dengan nama dokumen
        results = zip(filenames, similarity_scores, documents)
        # Urutkan hasil berdasarkan similarity score dari terbesar ke terkecil
        sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
        # Tampilkan hasil
        st.write("Hasil Pencarian:")
        for i, (filename, score, content) in enumerate(sorted_results):
            st.write(f"Hasil {i+1}:")
            st.write(f"Dokumen: {filename}")
            st.write(f"Similarity Score: {score:.4f}")
            st.write(
                f"Isi Dokumen: {content[:200]}..."
            )  # Potong isi dokumen untuk tampilan ringkas
    else:
        st.write("Silakan masukkan pertanyaan terlebih dahulu.")
