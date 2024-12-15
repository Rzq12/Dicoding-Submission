# Laporan Proyek Machine Learning - Nama Anda

## Domain Proyek

Salah satu masalah kesehatan yang sering kali dianggap tidak serius, namun memiliki dampak yang cukup
signifikan karena dapat memicu munculnya kelompok penyakit kronis adalah obesitas [1]. Obesitas kini tengah
menjadi isu kesehatan global dengan prevalensi yang meningkat setiap tahunnya. Tercatat hingga tahun 2022, kasus
obesitas di dunia mencapai angka 890 juta kasus dengan kelompok usia remaja sebagai penyumbang tertinggi. Hal
ini menyebabkan obesitas dikategorikan oleh World Health Organization (WHO) sebagai faktor resiko penyebab
kematian tertinggi ke-5 di dunia. Pada tahun 2018, pravelensi penderita obesitas di Indonesia mencapai angka 28,7%
dan kian meningkat setiap tahunnya dengan persentase kasus kematian tertingginya terjadi pada tahun 2020, yakni
sebesar 80,46% [2]. Adanya peningkatan secara masif, mengindikasikan bahwa obesitas merupakan sinyal utama bagi
resiko komplikasi penyakit kronis, seperti penyakit kardiovaskular. Oleh sebab itu, dibutuhkan langkah-langkah
preventif dini guna mengurangi tingkat resiko kematian dengan memanfaatkan perkembangan teknologi yang ada.
Salah satunya, melalui machine learning sebagai deteksi resiko obesitas. Penelitian ini memanfaatkan algoritma pada
machine learning untuk mengkategorikan jenis-jenis obesitas berdasarkan berbagai faktor yang mempengaruhinya.

[1] [Literature Study: Obesitas sebagai Faktor Risiko pada Kanker Payudara Triple Negative](https://www.researchgate.net/publication/359284669_Literature_Study_Obesitas_sebagai_Faktor_Risiko_pada_Kanker_Payudara_Triple_Negative)

[2] [Anthropometric and body composition analysis in obese and non-obese subjects in three major cities in Indonesia: A cross-sectional study](https://www.sciencedirect.com/science/article/pii/S2666149724000331)

## Business Understanding

Pada bagian ini, kamu perlu menjelaskan proses klarifikasi masalah.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:

- Obesitas telah menjadi masalah kesehatan global dengan prevalensi yang terus meningkat, baik di dunia maupun di Indonesia, yang berkontribusi terhadap meningkatnya resiko penyakit kronis, seperti penyakit kardiovaskular, yang menjadi penyebab kematian utama.
- Meskipun obesitas menjadi masalah kesehatan yang serius, belum ada sistem yang efektif dan otomatis untuk mengidentifikasi resiko obesitas pada individu berdasarkan berbagai faktor yang mempengaruhinya, sehingga pencegahan dan intervensi dini terhadap obesitas masih terbatas.

### Goals

Menjelaskan tujuan dari pernyataan masalah:

- Meningkatkan kesadaran tentang obesitas sebagai faktor risiko utama untuk penyakit kronis dan mengurangi prevalensinya melalui program-program pencegahan dan intervensi dini.
- Mengembangkan sistem berbasis machine learning yang dapat memprediksi resiko obesitas pada individu berdasarkan data faktor-faktor seperti usia, pola makan, aktivitas fisik, dan faktor genetik untuk memungkinkan deteksi lebih dini dan upaya pencegahan.

### Solution statements

- Solution Statement 1: Menggunakan algoritma machine learning seperti Decision Tree dan Random Forest untuk mengkategorikan individu berdasarkan faktor-faktor yang mempengaruhi obesitas. Algoritma ini dapat memberikan prediksi yang akurat tentang apakah seseorang berisiko mengembangkan obesitas, serta faktor apa saja yang paling berkontribusi terhadap kondisi tersebut.

- Solution Statement 2: Menggunakan Gradient Boosting untuk meningkatkan akurasi prediksi obesitas dengan mempertimbangkan kompleksitas data dan hubungan antar faktor yang lebih dalam. S

### Metrik evaluasi

Untuk mengevaluasi kinerja model dalam mendeteksi resiko obesitas, beberapa metrik yang dapat digunakan meliputi:

- CV Mean Akurasi: Rata-rata akurasi dari setiap lipatan cross-validation. Ini akan memastikan bahwa model tidak overfitting dan dapat bekerja baik pada data baru.
- Akurasi: Persentase prediksi yang benar dibandingkan dengan total data yang diuji.
- Precision dan Recall: Metrik ini akan memberikan gambaran seberapa baik model dalam mengidentifikasi individu dengan obesitas (recall) serta seberapa akurat prediksi tersebut (precision).
- F1-Score: Kombinasi dari precision dan recall, memberikan gambaran tentang keseimbangan antara keduanya.

## Data Understanding

Dataset ini mencakup data untuk **estimasi tingkat obesitas** pada individu dari negara **Meksiko, Peru, dan Kolombia**, berdasarkan **kebiasaan makan** dan **kondisi fisik** mereka. Data ini terdiri dari **17 atribut** dan **2111 rekaman**, di mana setiap rekaman diberi label dengan variabel kelas **NObesity** (Tingkat Obesitas). Variabel ini memungkinkan klasifikasi data ke dalam kategori berikut:

- **Berat Badan Kurang** (Insufficient Weight)
- **Berat Badan Normal** (Normal Weight)
- **Kelebihan Berat Badan Tingkat I** (Overweight Level I)
- **Kelebihan Berat Badan Tingkat II** (Overweight Level II)
- **Obesitas Tipe I** (Obesity Type I)
- **Obesitas Tipe II** (Obesity Type II)
- **Obesitas Tipe III** (Obesity Type III)

### Sumber Data:

- **77%** data dihasilkan secara **sintetis** menggunakan alat **Weka** dengan filter **SMOTE**.
- **23%** data dikumpulkan secara langsung dari pengguna melalui **platform web**.

[Estimation of Obesity Levels Based On Eating Habits and Physical Condition](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition).

### Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:

- **Gender**: Jenis kelamin individu.
- **Age**: Usia individu dalam tahun.
- **Height**: Tinggi badan individu dalam meter.
- **Weight**: Berat badan individu dalam kilogram.
- **family_history_with_overweight**: Riwayat anggota keluarga yang pernah atau sedang mengalami kelebihan berat badan.
- **FAVC**: Kebiasaan individu dalam mengonsumsi makanan berkalori tinggi.
- **FCVC**: Frekuensi individu mengonsumsi sayuran dalam setiap makan.
- **NCP**: Jumlah makanan utama yang dikonsumsi individu setiap hari.
- **CAEC**: Kebiasaan individu mengonsumsi makanan di antara waktu makan utama.
- **SMOKE**: Kebiasaan merokok individu.
- **CH2O**: Jumlah air yang dikonsumsi individu setiap hari.
- **SCC**: Kebiasaan individu memantau asupan kalori harian.
- **FAF**: Frekuensi individu melakukan aktivitas fisik.
- **TUE**: Waktu yang dihabiskan individu untuk menggunakan perangkat teknologi seperti ponsel, video game, televisi, dan komputer.
- **CALC**: Frekuensi individu mengonsumsi minuman beralkohol.
- **MTRANS**: Jenis transportasi yang biasanya digunakan oleh individu.
- **NObeyesdad**: Tingkat obesitas individu.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data atau exploratory data analysis.

## Data Preparation

Pada tahap ini, dilakukan beberapa teknik Data Preparation agar data siap digunakan untuk membangun model machine learning. Adapun tahapan yang dilakukan meliputi:

### Label Encoding

- Proses: Label Encoding digunakan untuk mengubah data kategori menjadi bentuk numerik. Teknik ini diterapkan pada fitur yang memiliki nilai kategori non-numerik.

- Alasan: Algoritma machine learning biasanya hanya dapat bekerja dengan data numerik. Oleh karena itu, nilai kategori perlu diubah menjadi angka agar dapat diproses oleh model.

### Normalisasi Data

- Proses: Normalisasi data dilakukan untuk menyelaraskan skala data pada setiap fitur. Teknik normalisasi seperti Min-Max Scaling diterapkan untuk memastikan semua fitur memiliki nilai dalam rentang tertentu, misalnya [0, 1].

- Alasan: Normalisasi penting karena algoritma tertentu, seperti Gradient Boosting atau K-Nearest Neighbors (KNN), sensitif terhadap skala data. Jika data memiliki skala yang berbeda jauh, maka model dapat memberikan bobot yang tidak seimbang pada fitur tertentu.

### Split Data

- Proses: Data dibagi menjadi dua bagian: Training Set dan Test Set.

- Alasan: Pemisahan data dilakukan untuk memastikan model dapat diuji dengan data yang belum pernah dilihat sebelumnya. Hal ini bertujuan untuk mengukur performa model dalam memprediksi data baru dan menghindari overfitting.

## Modeling

Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation

Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:

- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:

- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_

- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
