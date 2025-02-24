# Breast Cancer Classification

## Background Problem
Kanker payudara merupakan salah satu jenis kanker yang paling umum terjadi pada wanita di seluruh dunia. Deteksi dini sangat penting untuk meningkatkan peluang kesembuhan dan mengurangi angka kematian. Oleh karena itu, diperlukan model machine learning yang dapat mengklasifikasikan kanker payudara berdasarkan fitur-fitur yang tersedia dalam dataset.

**Situation**:
- Kanker payudara sulit dideteksi pada tahap awal tanpa alat diagnostik yang tepat.
- Data medis sering kali memiliki banyak fitur yang kompleks dan sulit dianalisis secara manual.
- Membutuhkan metode otomatis untuk mengklasifikasikan kanker payudara menjadi kategori jinak atau ganas.

**Task**:
- Menganalisis dataset kanker payudara.
- Melakukan preprocessing data.
- Melatih model klasifikasi untuk mendeteksi kanker payudara.
- Mengevaluasi performa model.

Dataset yang digunakan memiliki jumlah fitur yang cukup besar dan dapat diakses melalui link berikut: [https://scikit-learn.org/1.5/datasets/toy_dataset.html](#) 

---

## Version Libraries
- pandas 
- numpy 
- scikit-learn 
- matplotlib 
- seaborn 


## Insight
Dari analisis yang telah dilakukan, beberapa insight yang diperoleh antara lain:

1. **Fitur-fitur tertentu memiliki korelasi tinggi terhadap label kanker ganas**, seperti ukuran tumor dan kepadatan jaringan.
2. **Distribusi data menunjukkan adanya perbedaan signifikan antara kelas jinak dan ganas**, yang membantu dalam proses klasifikasi.
3. **Model yang digunakan mampu mencapai akurasi yang tinggi** dengan metode klasifikasi tertentu, menunjukkan bahwa pendekatan machine learning cukup efektif dalam mendeteksi kanker payudara.


## Advice
Proyek ini masih dapat dikembangkan lebih lanjut dalam berbagai aspek, seperti:

1. **Meningkatkan akurasi model** dengan melakukan hyperparameter tuning.
2. **Menerapkan teknik feature engineering** untuk mengurangi dimensi dataset tanpa mengurangi informasi penting.
3. **Mengembangkan aplikasi berbasis web atau mobile** untuk membantu tenaga medis dalam mendeteksi kanker payudara secara otomatis.


