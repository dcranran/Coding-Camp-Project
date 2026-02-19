# Laporan Proyek Machine Learning - Dwi Cahya Nurani

## Project Overview
Dewasa ini, jumlah konten hiburan, khususnya film, berkembang semakin pesat seiring dengan pertumbuhan *platform streaming* digital seperti Netflix, Viu, Disney+, dan Amazon Prime Video. Ribuan judul baru ditambahkan setiap tahunnya, menciptakan tantangan tersendiri bagi pengguna dalam memilih konten yang sesuai dengan minat dan preferensi pribadi. Fenomena ini dikenal sebagai *information overload*, di mana banyaknya pilihan justru menyulitkan pengguna dalam mengambil keputusan.
Akibatnya, ketika pengguna kesulitan menemukan konten yang relevan, mereka cenderung merasa frustrasi dan berpotensi beralih ke platform lain.

Untuk mengatasi tantangan *information overload* tersebut, sistem rekomendasi telah menjadi komponen krusial dalam membantu pengguna menemukan informasi atau produk yang relevan dengan preferensi mereka. Sistem rekomendasi merupakan sistem penyaringan informasi yang menjadi solusi dengan cara menyaring sebagian informasi penting dari banyaknya informasi yang ada dan bersifat dinamis sesuai dengan preferensi, minat, atau perilaku pengguna terhadap suatu produk (Fajriansyah et al., 2021). Secara umum, sistem ini dirancang untuk memahami dan memprediksi preferensi pengguna berdasarkan perilaku mereka. Terdapat dua pendekatan utama dalam membangun sistem rekomendasi, yaitu *Content-Based Filtering* dan *Collaborative Filtering*. *Content-Based Filtering* menyarankan film berdasarkan kemiripan konten dengan film yang disukai pengguna sebelumnya, sementara *Collaborative Filtering* yang merekomendasikan film berdasarkan kesamaan preferensi antar pengguna (Ricci et al., 2011). 

Dalam konteks industri film, penerapan teknik-teknik ini bertujuan untuk menyajikan daftar film yang dipersonalisasi kepada pengguna, baik berdasarkan riwayat interaksi mereka maupun kesamaan atribut antar film. Dengan menyediakan rekomendasi yang akurat dan relevan, platform tidak hanya mengatasi masalah kelebihan informasi tetapi juga dapat meningkatkan loyalitas pengguna, waktu yang dihabiskan di platform, dan pada akhirnya, potensi pendapatan. Oleh karena itu, proyek ini bertujuan untuk mengembangkan sistem rekomendasi film yang efektif, dengan memanfaatkan pendekatan yang relevan, untuk memberikan solusi nyata terhadap tantangan *information overload* dan meningkatkan pengalaman pengguna dalam menemukan film yang sesuai.


## Business Understanding
### Problem Statements
Berdasarkan latar belakang yang telah diuraikan, berikut adalah beberapa masalah utama yang akan menjadi fokus dalam proyek ini:
- Pengguna seringkali merasa kewalahan (*information overload*) ketika dihadapkan pada katalog film yang sangat besar di platform digital, sehingga kesulitan menemukan film yang benar-benar sesuai dengan selera dan preferensi pribadi mereka secara efisien. 
- Proses pencarian manual film tanpa panduan yang dipersonalisasi cenderung tidak efisien, memakan waktu, dan berpotensi menurunkan tingkat kepuasan pengguna akibat kesulitan memperoleh konten yang relevan.
- Ketiadaan sistem rekomendasi yang efektif dapat menyebabkan pengguna melewatkan film-film yang sebenarnya berpotensi mereka sukai, terutama karya yang kurang populer atau tidak terekspos secara luas.

### Goals
Berdasarkan pernyataan masalah di atas, tujuan utama dari proyek analisis prediksi ini adalah:
- Mengembangkan sistem rekomendasi yang mampu menyajikan daftar film yang telah disaring dan disesuaikan dengan profil preferensi masing-masing pengguna, sehingga mempermudah pengambilan keputusan.
- Membangun model prediktif yang dapat secara akurat menganalisis dan memahami preferensi unik pengguna berdasarkan data historis, guna menghasilkan rekomendasi film yang lebih relevan dan memuaskan.
- Mengimplementasikan sistem rekomendasi yang dapat membantu pengguna menemukan film-film baru yang sesuai dengan minat mereka, sehingga meningkatkan pengalaman pengguna.

### Solution Statements
- Pendekatan pertama adalah mengembangkan sistem rekomendasi menggunakan metode *Content-Based Filtering*. Solusi ini akan merekomendasikan film dengan cara menganalisis kemiripan atribut intrinsik antar film, dengan fokus utama pada genre sebagai fitur penentu. Dengan demikian, film yang memiliki profil genre serupa dengan yang pernah dinikmati pengguna akan memiliki probabilitas rekomendasi yang lebih tinggi.
- Pendekatan kedua adalah menerapkan metode *Collaborative Filtering*, secara spesifik menggunakan varian *Item-Based*. Sistem ini akan menghasilkan rekomendasi dengan mengidentifikasi dan mengukur kemiripan antar film berdasarkan pola rating yang diberikan oleh keseluruhan basis pengguna. Artinya, film-film yang cenderung mendapatkan penilaian serupa dari banyak pengguna akan dianggap memiliki kedekatan dan dapat direkomendasikan secara bergantian.

## Data Understanding
Data yang digunakan dalam proyek sistem rekomendasi ini adalah **Movies & Ratings for Recommendation System**. Dataset ini bersumber dari platform Kaggle yang dapat diakses pada tautan [Movies & Ratings for Recommendation System](https://www.kaggle.com/datasets/nicoletacilibiu/movies-and-ratings-for-recommendation-system). Dataset terdiri dari dua *file* yaitu `movies.csv` dan `ratings.csv`. Dataset ini dirancang untuk membangun sistem rekomendasi film. 

### Variabel
- Pada *file* `movies.csv`
  - `movieId` : ID unik untuk setiap film.
  - `title` : Judul film (beserta tahun rilis).
  - `genres` : Genre film.
- Pada *file* `ratings.csv`
  - `userId` : ID unik untuk setiap pengguna.
  - `movieId` : ID unik untuk setiap film.
  - `rating` : Rating yang diberikan oleh pengguna untuk suatu film.
  - `timestamp` : Waktu saat rating diberikan.

### Exploratory Data Analysis (EDA)
1. **Dataset `movies.csv`** \
   Data ini terdiri dari 9742 film dengan 3 fitur/kolom, yaitu  `movieId` (numerik), `title` (objek/string), dan `genres` (objek/string). Data tidak mengandung *missing value*, tetapi terdapat 5 judul film yang terduplikat karena perbedaan pada kolom `genres`, sehingga `movieId` menjadi berbeda. 
2. **Dataset `ratings.csv`** \
   Data ini terdiri dari 100.836 rating dengan 4 fitur/kolom, yaitu `userId` (numerik), `movieId` (numerik), `rating` (numerik/float), dan `timestamp` (numerik). Data tidak mengandung *missing value* dan nilai terduplikat. 
   ![alt text](c300fda7-57c8-4ef1-9f75-235727037b76.png)
   Rating berkisar antara 0,5 hingga 5, dengan peningkatan 0,5. Semakin tinggi nilai rating menandakan user semakin menyukai film, dengan rating yang paling banyak diberikan oleh user adalah 4. 

## Data Preparation
Proses persiapan data dilakukan secara terpisah untuk dua pendekatan sistem rekomendasi yang berbeda, yaitu *Content-Based Filtering* dan *Collaborative Filtering*.
1. **Data untuk *Content-Based Filtering***
   - Data `movies.csv` disalin ke DataFrame baru yang dinamakan `df_content` untuk memudahkan pengenalan pada analisis selanjutnya. 
   - Salah satu dari judul film yang terduplikat dihapus dengan mempertahankan baris judul film dengan genre lebih banyak karena perbedaan terdapat pada kolom `genres`.
   - Kolom `genres` yang awalnya berisi string genre yang dipisahkan oleh tanda (|) diubah menjadi format string tunggal di mana setiap genre dipisahkan oleh spasi, kemudian kolom tersebut dinamakan `genre`. Langkah ini bertujuan untuk memudahkan proses vektorisasi teks (TF-IDF) yang akan digunakan pada tahap *modeling*. Proses pemisahan dilakukan dengan membuat kolom `genre_list` yang berisi list genre. Selanjutnya kolom `genres` dan`genre_list` dihapus. 
   - Setelah dilakukan pemrosesan, diperoleh 22 genre unik  (termasuk '(no genres listed)').
   - Kolom `genre` dari `df_content` divektorisasi menggunakan TfidfVectorizer yang mengubah teks genre menjadi representasi numerik dalam bentuk matriks TF-IDF.
     Matriks ini memiliki dimensi 
       $$
       \frac{\text{jumlah film} \times \text{jumlah fitur TF-IDF}}{\text{kata unik dalam genre}}
       $$
     Dalam kasus ini, diperoleh matriks berukuran (9737, 24).
2. **Data untuk *Collaborative Filtering***
   - Data `ratings.csv` disalin ke DataFrame baru yang dinamakan `df_collab` untuk memudahkan pengenalan pada analisis selanjutnya. 
   - Kolom `timestamp` dihapus dari `df_collab` karena tidak akan digunakan dalam model.
   - Dilakukan encoding `userId` dan `movieId` menjadi indeks numerik sekuensial (dimulai dari 0) agar dapat digunakan sebagai input pada lapisan Embedding di model. Lapisan Embedding memerlukan input berupa integer positif yang merepresentasikan indeks kategori. Proses dilakukan dengan langkah berikut:
     - Dibuat daftar unik untuk `userId` dan `movieId`.
     - Dilakukan pemetaan (*mapping*) dari `userId` asli ke representasi numerik yang dimulai dari 0 (`user_to_user_encoded`), dan sebaliknya (`user_encoded_to_user`).
     - Hal yang sama dilakukan untuk `movieId` menjadi `movie_to_movie_encoded` dan `movie_encoded_to_movie`.
     - Nilai `userId` dan `movieId` pada `df_collab` diperbarui dengan nilai hasil encoding tersebut, disimpan dalam kolom baru `user` dan `movie`.
   - Ditampilkan jumlah user, jumlah film, sebaran nilai rating, jumlah rating untuk setiap film, dan jumlah rating yang pernah diberikan oleh user, untuk lebih memahami data setelah diproses. Diperoleh terdapat 610 user dan 9724 film setelah encoding. Film yang memiliki rating terbanyak adalah film dengan ID 356 dengan total 329 rating, dan user yang memberi rating terbanyak adalah user dengan ID 414 dengan total 2698 rating.
   - Fitur `user` dan `movie` sebagai X, dan `rating` yang sebagai y.
   - Normalisasi/scaling rating ke rentang 0-1 (normalisasi min-max) karena model akan menggunakan fungsi aktivasi sigmoid pada lapisan output, yang menghasilkan nilai antara 0 dan 1.
   -  Data dibagi menjadi data latih (X_train, y_train) dan data validasi (X_val, y_val) dengan proporsi 80:20.

## Modeling
Pada proyek ini dikembangkan dua jenis model sistem rekomendasi. 
1. ***Content-Based Filtering*** \
   Pendekatan ini merekomendasikan film berdasarkan kemiripan genre antar film. 
   - <ins> Proses </ins>: 
     - Perhitungan Kemiripan \
       Dihitung *cosine similarity* antar semua pasangan film berdasarkan matriks TF-IDF mereka. Proses ini menghasilkan matriks kemiripan (9737 x 9737) di mana setiap sel (i,j) berisi skor kemiripan antara film i dan film j. Matriks kemiripan ini disimpan dalam DataFrame `cosine_sim_df` dengan judul film sebagai indeks dan kolom.
     - Pembuatan Fungsi Rekomendasi \
       Dibuat fungsi yang menerima judul film sebagai input dan mengembalikan Top-N (default N=5) film yang paling mirip, tidak termasuk film input itu sendiri. Fungsi ini mencari film dengan skor kemiripan kosinus tertinggi terhadap film input.
    - <ins> Output </ins>: 
      Top-N rekomendasi film. Misalnya untuk film 'Red Dragon (2002)', rekomendasinya adalah 
      ![alt text]({40E00B07-0237-4FA9-9B36-B3FC325F5BAC}.png)
      Semua film yang direkomendasikan memiliki genre "Crime Mystery Thriller" sama seperti 'Red Dragon (2002)'.
    - <ins> Kelebihan </ins>: 
      - Dapat merekomendasikan item baru yang memiliki deskripsi fitur yang baik.
      - Tidak memerlukan data riwayat pengguna lain (*cold start* untuk item baru tidak terlalu bermasalah).
      - Dapat memberikan penjelasan mengapa suatu item direkomendasikan (berdasarkan kesamaan fitur).
    - <ins> Kekurangan </ins>: 
      - Terbatas pada fitur item yang ada, jika fitur tidak deskriptif maka rekomendasi kurang baik.
      - Cenderung menghasilkan rekomendasi yang seragam (kurang *serendipity*), karena hanya merekomendasikan item yang mirip dengan yang sudah disukai.

2. ***Collaborative Filtering*** \
   Pendekatan ini menggunakan teknik *Neural Collaborative Filtering* (berbasis *Deep Learning*) untuk memprediksi rating yang mungkin diberikan pengguna terhadap film.
   - <ins> Proses </ins>:
     - Pembangunan Arsitektur Model \
       Dibangun model *neural network* menggunakan TensorFlow Keras dan dinamakan RecommenderNet. Model terdiri dari:
       - Lapisan Embedding untuk pengguna (`user_embedding`): Mempelajari representasi vektor laten (sebesar embedding_size=50) untuk setiap pengguna.
       - Lapisan Bias untuk pengguna (`user_bias`): Mempelajari bias atau kecenderungan rating dari setiap pengguna.
       - Lapisan Embedding untuk film (`movie_embedding`): Mempelajari representasi vektor laten (sebesar embedding_size=50) untuk setiap film.
       - Lapisan Bias untuk film (`movie_bias`): Mempelajari bias atau kecenderungan rating dari setiap film.
       Cara kerja model ini yaitu vektor embedding pengguna dan film dikalikan (operasi *dot product*) untuk menangkap interaksi antara pengguna dan film. Kemudian, hasil *dot product* ditambahkan dengan bias pengguna dan bias film. Hasil akhir dilewatkan ke fungsi aktivasi sigmoid untuk menghasilkan prediksi rating antara 0 dan 1 (karena rating target sudah dinormalisasi).
     - Training 
       - Model dikompilasi dengan loss function BinaryCrossentropy (karena output sigmoid mirip probabilitas), optimizer Adam dengan learning rate 0.001, dan metrik RootMeanSquaredError.
       - Digunakan callback EarlyStopping untuk menghentikan training jika val_root_mean_squared_error tidak membaik selama 3 epoch, dan mengembalikan bobot terbaik.
       - Model dilatih menggunakan data latih (X_train, y_train) dengan ukuran batch 8, selama maksimal 100 epoch, dan divalidasi menggunakan data validasi (X_val, y_val). Training berhenti pada epoch ke-12 karena *early stopping* dengan metriks terakhir dan plot metriks sebagai berikut. 
       ![alt text]({58A73F89-1C1B-4469-91D5-797556BF5C7E}.png)
       ![alt text](0c1823a4-93eb-47a7-a95c-433de946b6dd.png)
       Hasil *modeling* menunjukkan bahwa model berhasil mempelajari pola dari data latih, sebagaimana tercermin dari penurunan kurva Train RMSE yang konsisten pada plot metrik. Meskipun demikian, kurva Val RMSE mengalami penurunan hanya pada epoch-epoch awal (sekitar epoch 0-2) sebelum akhirnya mendatar di sekitar nilai 0,1999. Perilaku Val RMSE yang mendatar ini, ditambah dengan adanya kesenjangan antara nilai akhir Train RMSE (0,1815) yang lebih rendah dibandingkan Val RMSE (0,1989), serta Train Loss (0,5911) yang lebih rendah dari Val Loss (0,6057), mengindikasikan terjadinya gejala *overfitting*. 
     - Pembuatan Fungsi Rekomendasi 
       - Diambil satu userId secara acak kemudian diidentifikasi film-film yang sudah ditonton oleh pengguna tersebut.
       - Diambil daftar film yang belum ditonton oleh pengguna tersebut.
       - Model RecommenderNet digunakan untuk memprediksi rating yang mungkin diberikan oleh pengguna tersebut terhadap film-film yang belum ditonton.
       - Direkomendasikan 10 film dengan prediksi rating tertinggi kepada pengguna.
   - <ins> Output </ins>: \
     Top-10 rekomendasi film untuk pengguna yang dipilih, beserta daftar film favorit pengguna tersebut (dengan rating tertinggi). Misalnya hasil rekomendasi untuk user dengan ID 534 berikut.
     ![alt text]({45FE626D-C963-40E5-940A-51FF2240D68D}.png)
     ![alt text]({4B418F7A-0959-4E0F-85F1-C73E78A728BA}.png)
   - <ins> Kelebihan </ins>: 
     - Mampu menangkap pola dan preferensi yang kompleks dari interaksi pengguna-item.
     - Tidak bergantung pada fitur item secara eksplisit (dapat menemukan *serendipity*).
     - Dapat bekerja dengan baik pada data rating implisit maupun eksplisit.
   - <ins> Kekurangan </ins>: 
     - Mengalami masalah *cold start* (sulit memberikan rekomendasi untuk pengguna baru atau item baru tanpa riwayat interaksi).
     - Membutuhkan data interaksi yang cukup banyak untuk performa yang baik.
     - Proses *training* model *deep learning* membutuhkan sumber daya komputasi. 

## Evaluation
Metrik evaluasi yang digunakan berbeda untuk kedua pendekatan.
1. ***Content-Based Filtering***
   - Precision@K: Mengukur proporsi item yang relevan di antara top-K rekomendasi. Dengan kata lain, dari k item yang ditampilkan kepada pengguna, berapa banyak yang benar-benar menarik atau sesuai dengan preferensi pengguna tersebut.
   $$
   Precision@K = \frac{\text{Jumlah item relevan dalam top-K}}{K}
   $$
   - Recall@K: Mengukur seberapa banyak item relevan yang berhasil ditemukan dari semua item relevan yang ada.
   $$
   Recall@K = \frac{\text{Jumlah item relevan dalam top-K}}{\text{Total jumlah item relevan untuk pengguna}}
   $$

2. ***Collaborative Filtering***
   - Root Mean Squared Error (RMSE) : Akar dari rata-rata kuadrat perbedaan antara nilai rating aktual dan nilai rating prediksi. Semakin kecil RMSE, semakin baik model dalam memprediksi rating.
   $$
   RMSE = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(y_i-\hat{y_i})^2}
   $$
   - Mean Absolute Error (MAE) : Rata-rata dari nilai absolut perbedaan antara rating aktual dan rating prediksi.
   $$
   MAE = \frac{1}{N}\sum_{i=1}^{N}|y_i-\hat{y_i}|
   $$
   Metrik ini dihitung pada data validasi setelah nilai prediksi dan nilai aktual dikembalikan ke skala rating asli (0.5 - 5.0).

### Hasil Evaluasi Proyek
1. ***Content-Based Filtering*** \
   Diperoleh hasil sebagai berikut. 
   - Precision@10: 0,000 \
     Nilai ini menunjukkan bahwa dari 10 film teratas yang direkomendasikan oleh model *Content-Based Filtering*, tidak ada satupun yang dianggap relevan bagi pengguna
   - Recall@10: 0,000\
     Nilai ini menunjukkan bahwa dari keseluruhan film yang relevan bagi pengguna, tidak ada satupun yang berhasil ditemukan dan direkomendasikan oleh model dalam 10 rekomendasi teratasnya.

   Hasil 0,0 untuk Precision@10 dan Recall@10 menunjukkan bahwa model *Content-Based Filtering* yang diimplementasikan, dengan fokus utama pada genre sebagai fitur penentu, tidak berhasil menghasilkan rekomendasi yang relevan untuk pengguna dalam konteks evaluasi yang dilakukan. Pengguna tidak menemukan film yang mereka sukai dalam 10 rekomendasi teratas yang diberikan oleh sistem ini.

2. ***Collaborative Filtering*** \
   Diperoleh hasil sebagai berikut. 
   - RMSE: 0,9531 \
     Nilai 0,9531 menunjukkan bahwa secara rata-rata prediksi rating yang dihasilkan model memiliki deviasi sekitar 0,95 poin dari rating sebenarnya pada skala rating 0,5 hingga 5,0. Halni mengindikasikan tingkat akurasi yang cukup baik, di mana model umumnya dapat memperkirakan rating pengguna, meskipun terkadang bisa meleset hampir satu poin rating penuh.
   - MAE : 0,7320 \
     Nilai 0.7320 menunjukkan bahwa rata-rata prediksi rating model berbeda sekitar 0,73 poin dari rating yang sebenarnya diberikan oleh pengguna.
   
   Secara keseluruhan, model *Collaborative Filtering* menunjukkan kemampuan yang cukup baik dalam memprediksi preferensi rating pengguna. Dengan MAE sekitar 0,73, model ini rata-rata dapat memprediksi rating dengan kesalahan kurang dari satu poin pada skala rating yang ada. Perbedaan antara nilai RMSE dan MAE (RMSE > MAE) menyiratkan bahwa ada beberapa prediksi yang memiliki kesalahan yang relatif besar, yang lebih signifikan dipenalti oleh RMSE. Meskipun demikian, performa ini dianggap cukup baik dan menunjukkan bahwa model telah berhasil menangkap sebagian besar pola preferensi pengguna dari data rating historis.  

### Implementasi Hasil Evaluasi
1. **Terhadap *Problem Statements***
   - Model *Content-Based Filtering* berlum berhasil menjawab masalah. Pengguna justru tidak menemukan film yang sesuai sama sekali dalam rekomendasi teratas, sehingga tidak membantu mengurangi *information overload* dengan cara yang efektif. Model gagal menyediakan panduan yang relevan (berdasarkan hasil evaluasi), sehingga pengguna kemungkinan masih akan merasa tidak puas. Dengan performa 0.0, model ini tidak efektif dan justru akan membuat pengguna tetap melewatkan film yang relevan.
   - Model *Collaborative Filtering* memiliki potensi sedang untuk membantu pengguna menemukan film yang sesuai dan membuat proses penemuan lebih efisien. Dengan prediksi rating yang cukup akurat, saran yang diberikan bisa lebih personal dan relevan, sehingga mengurangi waktu pencarian manual dan meningkatkan kepuasan. Model  berpoteni untuk membantu menemukan film  yang kurang populer jika film tersebut memiliki pola rating yang mirip dengan film lain yang disukai pengguna. Dengan akurasi prediksi rating yang moderat, ada kemungkinan sedang model ini dapat membantu pengguna menemukan film yang tersembunyi tersebut, asalkan film-film tersebut memiliki cukup data rating untuk dianalisis kemiripannya.
2. **Terhadap *Goals***
   - Model *Content-Based Filtering* tidak berhasil mencapai goal karena model belum menunjukkan kemampuan menghasilkan rekomendasi relevan berdasarkan preferensi (genre yang disukai). 
   - Model *Collaborative Filtering* hampir berhasil mencapai goal karena nilai RMSE dan MAE menunjukkan model dapat menganalisis preferensi rating dengan akurasi moderat. Model berpoteni merekomendasikan film berdasarkan kemiripan pola rating antar film, yang bisa saja mencakup film baru atau kurang populer bagi pengguna, selama film tersebut dinilai mirip dengan film lain yang disukai pengguna.
3. **Terhadap *Solution Statements***
   - Berdasarkan hasil evaluasi, model *Content-Based Filtering* belum memberikan dampak positif yang diharapkan. Penggunaan genre saja sebagai fitur mungkin tidak cukup untuk menangkap kompleksitas preferensi pengguna atau dataset yang digunakan mungkin memiliki keterbatasan dalam hal informasi genre yang bisa dieksploitasi secara efektif oleh model ini. Rekomendasi yang dihasilkan tidak relevan bagi pengguna dalam pengujian yang dilakukan.
   - Berdasarkan hasil evaluasi, model *Collaborative Filtering* memberikan dampak yang cukup positif dalam hal memprediksi rating pengguna. Jika prediksi rating ini digunakan untuk menghasilkan daftar rekomendasi top-N, ada potensi besar bahwa rekomendasi tersebut akan lebih relevan dan bermanfaat bagi pengguna dibandingkan pendekatan *Content-Based Filtering* yang pertama. Model ini lebih berhasil dalam memahami pola dari data interaksi pengguna (rating).
  
Model *Collaborative Filtering* menunjukkan hasil yang lebih menjanjikan dalam menjawab *problem statements* dan mencapai *goals* dibandingkan model *Content-Based Filtering* (yang menggunakan genre saja) berdasarkan evaluasi yang disajikan. Model CF memiliki potensi untuk mengurangi *information overload*, mempersonalisasi penemuan film, dan membantu pengguna menemukan film baru dengan akurasi prediksi rating yang moderat. Model CBF dengan hanya menggunakan genre tampaknya tidak cukup efektif untuk dataset ini atau memerlukan *feature engineering* yang lebih mendalam untuk bisa memberikan dampak positif.

## Referensi
- Fajriansyah, M., Adikara, P. P., & Widodo, A. A. (2021). Sistem Rekomendasi Film Menggunakan *Content-Based Filtering*. Jurnal Pengembangan Teknologi Informasi dan Ilmu Komputer, 5(6), 2188-2199.

- Ricci, F., Rokach, L., & Shapira, B. (2015). Recommender Systems Handbook. Springer.
