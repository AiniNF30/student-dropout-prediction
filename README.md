# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
**Jaya Jaya Institut** merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
**Jaya Jaya Institute** menghadapi masalah serius dengan tingginya angka dropout, yang tidak hanya merugikan siswa yang kehilangan kesempatan untuk menyelesaikan pendidikan, tetapi juga berdampak pada reputasi institusi. Angka dropout yang tinggi memberi kesan bahwa **Jaya Jaya Institute** kurang mampu memberikan dukungan yang memadai bagi keberhasilan siswa. Hal ini dapat menurunkan daya tarik institusi bagi calon mahasiswa dan berisiko menurunkan jumlah pendaftar serta pendapatan institusi.

### Cakupan Proyek
- Pengumpulan dan persiapan data: Mengumpulkan data siswa yang mencakup berbagai faktor yang dapat mempengaruhi keputusan mereka untuk dropout, serta melakukan pembersihan data.
- Eksplorasi Data: Menganalisis data untuk memahami pola-pola yang ada serta hubungan antara fitur-fitur yang ada dengan status dropout.
- Pengembangan Model Prediksi: Menggunakan teknik machine learning untuk membangun model prediksi yang dapat mengidentifikasi siswa dengan kemungkinan tinggi untuk dropout.

### Persiapan

Sumber data:https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:
1. Buka terminal atau PowerShell.
2. Jalankan perintah berikut.
    ```
     conda create --name prediksi_dropout python=3.9
    ```
3. Aktifkan virtual environment dengan menjalankan perintah berikut.
    ```
    conda activate prediksi_dropout
    ```
4. Instal semua library yang dibutuhkan menggunakan perintah berikut.
    ```
   pip install -r requirements.txt
    ```
5. Buka jupyter-notebook dengan menjalankan perintah berikut.
    ```
    jupyter-notebook
    ```
## Business Dashboard
Dashboard ini dirancang untuk memberikan gambaran visual mengenai analisis data dropout di Jaya Jaya Institut. Tujuan utamanya adalah untuk menyediakan informasi yang mudah dipahami dan dapat digunakan oleh manajemen dan pihak terkait dalam institusi untuk mengidentifikasi pola dan tren dropout, serta untuk mengambil langkah-langkah proaktif dalam memberikan dukungan kepada siswa yang berisiko dropout.

**link Looker :** https://lookerstudio.google.com/reporting/c1eaea00-ab14-4cc9-b74e-44c006790a2c

## Menjalankan Sistem Machine Learning

1. **Pastikan Python terinstal**
   - Pastikan Python versi 3.x terinstal di sistem Anda. Anda dapat mengunduh dan menginstalnya dari [python.org](https://www.python.org/).

2. **Buat lingkungan virtual**
   - Buat lingkungan virtual untuk mengisolasi dependensi proyek. Jalankan perintah berikut di terminal Anda:
     ```bash
     python -m venv env
     ```
     
3. **Aktifkan lingkungan virtual**
   - Untuk Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - Untuk macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Pasang dependensi menggunakan `requirements.txt`**
   - Pastikan Anda berada di direktori proyek yang sama dengan file `requirements.txt`, lalu jalankan perintah berikut:
     ```bash
     pip install -r requirements.txt
     ```

5. Running Streamlit
```
streamlit run app.py
```
**link Streamlite :** https://aininf30-student-dropout-prediction-app-uaf1vu.streamlit.app/

## Conclusion
Berdasarkan permasalahan diatas dapat disimpulkan bawah ada beberapa faktor yang mempengaruhi mahasiswa di dropout yaitu :
- Mahasiswa yang lebih muda saat pertama kali mendaftar memiliki risiko dropout yang lebih tinggi. Hal ini mungkin dikarenakan kurangnya kesiapan dalam menghadapi tantangan akademis maupun aspek kehidupan kampus yang kompleks.
- Mahasiswa yang mendaftar melalui jalur "over 23 years old" memiliki tingkat dropout tertinggi. Ini menunjukkan bahwa mahasiswa dalam kategori ini cenderung memiliki risiko lebih besar untuk keluar dari studi dibandingkan jalur pendaftaran lainnya.
- Jurusan Manajemen, baik untuk kelas malam maupun siang, memiliki jumlah mahasiswa dropout yang signifikan. Ini menunjukkan bahwa mahasiswa di jurusan ini mungkin menghadapi tantangan khusus yang perlu strategi khusus untuk mengurangi tingkat dropout.
- Mahasiswa yang gagal menyelesaikan banyak mata kuliah dan mendapatkan nilai rendah di semester pertama dan kedua lebih rentan terhadap risiko dropout. Ini menunjukkan bahwa performa akademis awal memiliki pengaruh signifikan terhadap keberlanjutan studi mahasiswa.
- Mahasiswa yang memiliki tunggakan cenderung lebih rentan untuk keluar dari studi. Sementara itu, mahasiswa yang menerima beasiswa memiliki risiko dropout yang lebih rendah, menunjukkan bahwa dukungan finansial dapat membantu menjaga keberlanjutan studi mahasiswa.


### Rekomendasi Action Items
Berikut beberapa rekomendasi action items yang harus dilakukan guna menyelesaikan permasalahan :

1. Fokus pada mahasiswa dengan performa akademis rendah dengan bimbingan tambahan.
2. Meningkatkan dukungan finansial melalui beasiswa dan bantuan.
3. Menyediakan program orientasi yang lebih mendalam untuk mahasiswa muda.
4. Evaluasi kurikulum jurusan Manajemen untuk mengurangi angka dropout.
5. Menawarkan program studi fleksibel untuk mahasiswa lebih tua.
