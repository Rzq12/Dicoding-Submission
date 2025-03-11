# Laporan Proyek Machine Learning - Riezqi D R

## Project Overview

Netflix adalah salah satu platform streaming terbesar di dunia yang memiliki ribuan film dan acara TV. Dengan banyaknya pilihan, pengguna sering kesulitan menemukan konten yang sesuai dengan minat mereka. Oleh karena itu, sistem rekomendasi menjadi solusi penting untuk meningkatkan pengalaman pengguna dengan menyarankan film atau acara TV yang relevan.

Sistem rekomendasi yang dibangun dalam proyek ini menggunakan **TF-IDF Vectorization** dan **Cosine Similarity** untuk menghitung kesamaan antar film berdasarkan fitur teks seperti genre, deskripsi, sutradara, dan pemeran.

Referensi terkait:

- [Recommender systems](https://www.sciencedirect.com/science/article/abs/pii/S0370157312000828)

## Business Understanding

### Problem Statements

- Bagaimana cara merekomendasikan film yang relevan kepada pengguna berdasarkan film yang telah mereka tonton?
- Bagaimana cara mengukur kesamaan antar film secara efektif menggunakan metode berbasis konten?

### Goals

- Mengembangkan sistem rekomendasi berbasis konten menggunakan TF-IDF dan Cosine Similarity.
- Menghasilkan daftar film yang memiliki kemiripan tinggi dengan film yang dipilih oleh pengguna.

### Solution Approach

- **Pendekatan TF-IDF dan Cosine Similarity**: Mengubah teks deskriptif menjadi vektor dan menghitung kesamaan antar film berdasarkan fitur teks.

## Data Understanding

Dataset yang digunakan dalam proyek ini merupakan data film dari **Netflix**. Data ini berisi informasi tentang judul film, jenis (film atau acara TV), sutradara, pemeran, genre, dan deskripsi singkat.

### Sumber Data

- Dataset: [Netflix Movies & Shows Dataset](https://www.kaggle.com/datasets/ashfakyeafi/netflix-movies-and-shows-dataset)
- Pada dataset terdapat 8807 data film, dan 12 variabel.
- Terdapat beberapa missing value yang telah ditangani dengan teknik data preprocessing.

**Variabel dalam dataset:**

- `title` : Judul film atau acara TV.
- `type` : Jenis konten (Movie/TV Show).
- `director` : Nama sutradara.
- `cast` : Daftar pemeran utama.
- `rating` : Klasifikasi rating film/acara TV.
- `listed_in` : Genre film/acara TV.
- `description` : Deskripsi singkat tentang film/acara TV.

**Analisis Data:**

- **Distribusi Film Berdasarkan Tahun**: Visualisasi jumlah film yang dirilis setiap tahun menggunakan **bar chart**.
- **Negara dengan Produksi Film Terbanyak**: Treemap untuk menunjukkan negara dengan jumlah film terbanyak.

## Data Preparation

Langkah-langkah persiapan data meliputi:

1. **Mengisi nilai yang hilang** menggunakan `fillna('')` untuk menghindari error saat pemrosesan teks.
2. **Menggabungkan fitur teks** dari beberapa kolom menjadi satu **Bag of Words (BoW)**.
3. **Preprocessing Teks** menggunakan class `TextCleaner`, yang mencakup:
   - Menghapus tanda baca.
   - Mengonversi teks menjadi huruf kecil.
   - Menghapus spasi yang tidak perlu.
4. **Ekstraksi fitur teks menggunakan TF-IDF Vectorization** Mengubah teks menjadi representasi numerik menggunakan `TfidfVectorizer()`.
5. **Membangun matriks kesamaan menggunakan Cosine Similarity** untuk mengukur hubungan antar film.

## Model and Results

### Model yang Digunakan

Model yang digunakan dalam proyek ini adalah **Content-Based Filtering**, dengan tahapan sebagai berikut:

1. **Perhitungan Cosine Similarity**: Menghitung kesamaan antar film berdasarkan vektor TF-IDF.
2. **Pembuatan fungsi rekomendasi**: Mencari film yang memiliki kesamaan tinggi dengan film yang dipilih.

### Hasil Rekomendasi

Hasil rekomendasi disajikan dalam bentuk tabel berikut:

| **Film Input**  | **Rekomendasi 1**    | **Rekomendasi 2**      | **Rekomendasi 3**    | **Rekomendasi 4**    | **Rekomendasi 5** |
| --------------- | -------------------- | ---------------------- | -------------------- | -------------------- | ----------------- |
| Back to 1989    | See You in Time      | Little Big Women       | The Devil Punisher   | Queen of No Marriage | My MVP Valentine  |
| Stranger Things | Ant-Man and the Wasp | Beyond Stranger Things | The Umbrella Academy | Good Witch           | Safe Haven        |

Hasil rekomendasi di atas menunjukkan bahwa sistem mampu mengusulkan film dan acara TV yang relevan berdasarkan kesamaan fitur teks.

## Evaluation

### Metrik Evaluasi

Untuk mengevaluasi sistem rekomendasi berbasis konten, digunakan metrik **precision** dan **recall**. Metrik ini mengukur relevansi dan cakupan rekomendasi yang dihasilkan oleh sistem.

- **Precision** mengukur seberapa banyak rekomendasi yang diberikan oleh sistem benar-benar relevan bagi pengguna.
- **Recall** mengukur sejauh mana sistem berhasil menemukan semua film yang relevan berdasarkan data input.

![Rumus](image/Screenshot%202025-03-11%20105401.png)

Dalam implementasi Python, precision dan recall dapat dihitung dengan membandingkan hasil rekomendasi dengan daftar film yang benar-benar relevan.

### Hasil Evaluasi

Precision: 0.60 → Dari semua rekomendasi yang diberikan, 60% di antaranya relevan bagi pengguna. Ini menunjukkan bahwa ada beberapa rekomendasi yang kurang sesuai.

Recall: 0.67 → Dari semua film yang relevan, sistem berhasil merekomendasikan 67% di antaranya. Ini berarti sistem telah menemukan sebagian besar film yang sesuai, tetapi masih ada beberapa film relevan yang tidak direkomendasikan.

## Kesimpulan dan Saran

- Sistem rekomendasi berbasis konten berhasil dibuat menggunakan **TF-IDF dan Cosine Similarity**.
- Model dapat memberikan rekomendasi yang relevan berdasarkan kesamaan fitur teks.
- Alternatif model seperti **Matrix Factorization** atau **Deep Learning** dapat dipertimbangkan untuk meningkatkan akurasi rekomendasi.
