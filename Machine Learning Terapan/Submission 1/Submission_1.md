# Laporan Proyek Machine Learning - Riezqi Dhermatria Rachmadi

## Domain Proyek

Salah satu masalah kesehatan yang sering kali dianggap tidak serius, namun memiliki dampak yang cukup
signifikan karena dapat memicu munculnya kelompok penyakit kronis adalah obesitas [1]. Obesitas kini tengah
menjadi isu kesehatan global dengan prevalensi yang meningkat setiap tahunnya. Tercatat hingga tahun 2022, kasus
obesitas di dunia mencapai angka 890 juta kasus dengan kelompok usia remaja sebagai penyumbang tertinggi. Hal
ini menyebabkan obesitas dikategorikan oleh World Health Organization (WHO) sebagai faktor resiko penyebab
kematian tertinggi ke-5 di dunia. Pada tahun 2018, pravelensi penderita obesitas di Indonesia mencapai angka 28,7%
dan kian meningkat setiap tahunnya dengan persentase kasus kematian tertingginya terjadi pada tahun 2020, yakni
sebesar 80,46% [2].

Adanya peningkatan secara masif, mengindikasikan bahwa obesitas merupakan sinyal utama bagi
resiko komplikasi penyakit kronis, seperti penyakit kardiovaskular. Oleh sebab itu, dibutuhkan langkah-langkah
preventif dini guna mengurangi tingkat resiko kematian dengan memanfaatkan perkembangan teknologi yang ada.
Salah satunya, melalui machine learning sebagai deteksi resiko obesitas. Penelitian ini memanfaatkan algoritma pada
machine learning untuk mengkategorikan jenis-jenis obesitas berdasarkan berbagai faktor yang mempengaruhinya.

[1] [Literature Study: Obesitas sebagai Faktor Risiko pada Kanker Payudara Triple Negative](https://www.researchgate.net/publication/359284669_Literature_Study_Obesitas_sebagai_Faktor_Risiko_pada_Kanker_Payudara_Triple_Negative)

[2] [Anthropometric and body composition analysis in obese and non-obese subjects in three major cities in Indonesia: A cross-sectional study](https://www.sciencedirect.com/science/article/pii/S2666149724000331)

## Business Understanding

Pada bagian ini, kami akan menjelaskan proses klarifikasi masalah terkait obesitas, serta tujuan yang ingin dicapai dalam penelitian ini. Selain itu, akan disajikan juga solusi yang diusulkan untuk meraih tujuan tersebut dengan menggunakan teknologi machine learning untuk mendeteksi resiko obesitas.

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

Dataset ini mencakup data untuk **estimasi tingkat obesitas** pada individu dari negara **Meksiko, Peru, dan Kolombia**, berdasarkan **kebiasaan makan** dan **kondisi fisik** mereka. Data ini terdiri dari **17 atribut** dan **2111 rekaman**, di mana setiap rekaman diberi label dengan variabel kelas **NObesity** (Tingkat Obesitas). Tidak ada missing value, duplicate pada dataset. Variabel ini memungkinkan klasifikasi data ke dalam kategori berikut:

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
- Dataset mengandung **outlier**, namun keberadaannya tidak terlalu berpengaruh karena sebagian besar data dihasilkan menggunakan **SMOTE**, yang bertujuan untuk mengatasi ketidakseimbangan kelas.

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

## Data Preparation

Pada tahap ini, dilakukan beberapa teknik Data Preparation agar data siap digunakan untuk membangun model machine learning. Adapun tahapan yang dilakukan meliputi:

### Label Encoding

- Proses: Label Encoding digunakan untuk mengubah data kategori menjadi bentuk numerik. Teknik ini diterapkan pada fitur yang memiliki nilai kategori non-numerik.

- Alasan: Algoritma machine learning biasanya hanya dapat bekerja dengan data numerik. Oleh karena itu, nilai kategori perlu diubah menjadi angka agar dapat diproses oleh model.

### Normalisasi Data

- Proses: Normalisasi data dilakukan untuk menyelaraskan skala data pada setiap fitur. Teknik normalisasi seperti StandardScaler diterapkan untuk memastikan semua fitur memiliki nilai dalam rentang tertentu.

- Alasan: Normalisasi penting karena algoritma tertentu, seperti Gradient Boosting atau K-Nearest Neighbors (KNN), sensitif terhadap skala data. Jika data memiliki skala yang berbeda jauh, maka model dapat memberikan bobot yang tidak seimbang pada fitur tertentu.

### Split Data

- Proses: Data dibagi menjadi dua bagian: Training Set dan Test Set.

- Alasan: Pemisahan data dilakukan untuk memastikan model dapat diuji dengan data yang belum pernah dilihat sebelumnya. Hal ini bertujuan untuk mengukur performa model dalam memprediksi data baru dan menghindari overfitting.

## Modeling

Pada tahap ini, dilakukan proses pemodelan menggunakan algoritma **Gradient Boosting** dan **Decision Tree** untuk menyelesaikan permasalahan. Setiap model diuji performanya, kemudian dibandingkan untuk memilih model terbaik.

### 1. **Decision Tree**

- **Proses**:  
  Model Decision Tree dibangun menggunakan parameter berikut:

  - `max_depth = 50` → Menentukan kedalaman maksimum pohon keputusan.
  - `min_samples_split = 2` → Menentukan jumlah minimum sampel yang diperlukan untuk membagi node.

- **Kelebihan**:

  - Sederhana, mudah diinterpretasikan, dan cepat untuk dilatih.
  - Dapat menangani fitur numerik dan kategori tanpa memerlukan preprocessing tambahan.

- **Kekurangan**:
  - Rentan terhadap **overfitting**, terutama jika pohon terlalu dalam.
  - Kurang optimal dalam menangani data yang kompleks dibandingkan algoritma ensemble seperti Gradient Boosting.

### 2. **Gradient Boosting**

- **Proses**:  
  Model Gradient Boosting dibangun dengan parameter sebagai berikut:

  - `n_estimators = 200` → Jumlah pohon yang digunakan dalam ensemble.
  - `learning_rate = 0.5` → Mengontrol kontribusi setiap pohon terhadap hasil akhir.
  - `max_depth = 7` → Menentukan kedalaman maksimum pohon di setiap iterasi.

- **Kelebihan**:

  - Lebih akurat dibandingkan dengan Decision Tree karena menggunakan teknik ensemble untuk menggabungkan banyak pohon keputusan.
  - Efektif dalam menangani data kompleks dan menangani overfitting dengan pengaturan hyperparameter yang tepat.

- **Kekurangan**:
  - Proses training lebih lambat dibandingkan dengan Decision Tree.
  - Memerlukan tuning hyperparameter yang lebih kompleks untuk mendapatkan performa terbaik.

## Evaluation

Pada bagian ini, dilakukan evaluasi terhadap performa model menggunakan metrik **akurasi**, **precision**, **recall**, **F1-score**, dan **cross-validation score**. Metrik ini digunakan karena sesuai dengan kasus klasifikasi yang dihadapi.

### **Metrik Evaluasi yang Digunakan**

1. **Akurasi**

   - **Definisi**: Akurasi adalah proporsi prediksi yang benar terhadap total jumlah data.
   - **Alasan**: Akurasi digunakan sebagai metrik dasar untuk melihat seberapa baik model memprediksi secara keseluruhan.

2. **Precision**

   - **Definisi**: Precision mengukur proporsi prediksi positif yang benar dibandingkan dengan total prediksi positif.
   - **Alasan**: Precision penting untuk menghindari **false positives**, terutama jika prediksi positif memiliki konsekuensi serius.

3. **Recall**

   - **Definisi**: Recall mengukur kemampuan model untuk menemukan semua data positif dari keseluruhan data positif yang ada.
   - **Alasan**: Recall penting jika konsekuensi dari **false negatives** cukup tinggi, seperti dalam deteksi penyakit atau fraud.

4. **F1-Score**

   - **Definisi**: F1-Score adalah rata-rata harmonis dari precision dan recall.
   - **Alasan**: F1-Score memberikan gambaran seimbang antara precision dan recall, terutama jika terdapat ketidakseimbangan data.

5. **Cross-Validation (CV) Score**
   - **Definisi**: Cross-validation score digunakan untuk mengevaluasi stabilitas dan generalisasi model dengan membagi data ke dalam beberapa fold (misalnya 5-fold atau 10-fold).
   - **Alasan**: CV score memastikan performa model tidak hanya baik pada satu pembagian data tetapi konsisten pada beberapa iterasi.

### **Hasil Evaluasi Proyek**

Berdasarkan metrik evaluasi yang digunakan, berikut adalah performa dari kedua model (**Decision Tree** dan **Gradient Boosting**):

| Model                 | CV Mean Accuracy | Test Accuracy | Precision | Recall | F1-Score |
| --------------------- | ---------------- | ------------- | --------- | ------ | -------- |
| **Decision Tree**     | 0.9218           | 0.9362        | 0.9367    | 0.9362 | 0.9361   |
| **Gradient Boosting** | 0.9680           | 0.9645        | 0.9647    | 0.9645 | 0.9645   |

#### **Analisis Hasil**

1. **Decision Tree**

   - Model Decision Tree memiliki **CV Mean Accuracy** sebesar **92.18%** dan **Test Accuracy** sebesar **93.62%**.
   - Precision, Recall, dan F1-Score untuk Decision Tree adalah **0.936**.
   - Model menunjukkan **overfitting** karena **Train Accuracy** mencapai **100%**, namun Test Accuracy lebih rendah.

2. **Gradient Boosting**
   - Model Gradient Boosting memiliki **CV Mean Accuracy** sebesar **96.80%** dan **Test Accuracy** sebesar **96.45%**.
   - Precision, Recall, dan F1-Score untuk Gradient Boosting adalah **0.964**.
   - Model ini juga mengalami overfitting, tetapi tingkat akurasi dan metrik evaluasi lainnya lebih tinggi dibandingkan Decision Tree.

#### **Pemilihan Model Terbaik**

Berdasarkan hasil evaluasi, model **Gradient Boosting** dipilih sebagai model terbaik karena:

- Memiliki **Test Accuracy** yang lebih tinggi (**96.45%**) dibandingkan Decision Tree (**93.62%**).
- Menunjukkan performa yang lebih baik pada metrik precision, recall, dan F1-Score.
- **CV Mean Accuracy** yang lebih tinggi menunjukkan model memiliki kemampuan generalisasi yang lebih baik dibandingkan Decision Tree.

Dengan demikian, Gradient Boosting menjadi solusi terbaik untuk kasus ini karena performa yang lebih unggul pada semua metrik evaluasi yang digunakan.
