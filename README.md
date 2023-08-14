
## Introduction

Nama     : Muhammad Aji Satrio Wiyogo

Batch    : RMT - 20 


## Deployment Link
https://huggingface.co/spaces/recognize96/Final_Project_Customer_Churn

## Project Title
Prediksi churn terhadap pelanggan kartu kredit

## Project Description
Problem Statement   : Manajer bank menghadapi tantangan penurunan jumlah pelanggan kartu kredit di bank mereka. Untuk mengatasi hal tersebut, perlu dilakukan analisis terhadap faktor-faktor yang berkontribusi pada penurunan ini. Selain itu, penting juga untuk memprediksi pelanggan mana yang mungkin akan keluar dari layanan, sehingga langkah-langkah pencegahan yang tepat dapat diambil. Dengan melakukan prediksi churn, bank dapat menyediakan layanan khusus dan penawaran yang lebih menarik kepada pelanggan yang memiliki risiko tinggi untuk keluar, dengan tujuan menjaga pelanggan tetap loyal dan puas.

Dari problem statement diatas, maka kita dapat membuat point point pertanyaan.

- Karakteristik pelanggan manakah yang lebih cenderung untuk keluar dari layanan kartu kredit bank ?
- Apakah model yang dibentuk sudah baik dalam memprediksi pelanggan yang akan keluar ?
- Apa kelebihan dan kelemahan dari model yang sudah dibuat dalam memprediksi pelanggan yang akan keluar ?
- Apa dampak positif yang dapat diberikan dari segi bisnis dalam pembuatan model ?


## Conclusion

Dari hasil EDA ada beberapa insight yang dapat diperoleh, customer dengan gender perempuan, tingkat edukasi yang rendah, status perkawinan sudah menikah, pendapatan dibawah $40k, kartu tipe blue, dan customer yang memiliki 3 produk memiliki total pelanggan churn yang lebih tinggi. Dari hasil lainnya, customer dengan jumlah dependent sebanyak 3 orang, total produk yang lebih sedikit, tidak aktif lebih dari 4 bulan , dan sudah lebh dari 5kali dikontak oleh bank memiliki tingkat persentase churn yang lebih tinggi. Selain itu didapatkan dari hasil historgram, customer dengan umur 48 tahun, customer yang sudah bersama dengan bank selama 36 bulan, credit limit yang rendah, total revolving rendah, rata rata open to buy yang rendah, total balance yang sebesar 0.6,  total transaskinya sebesar 2216, jumlah total transaksi sebesar 43, total change sebesar 0.5 dan avg utilization ratio sebesar 0 memiliki tingkat churn yang tinggi.

Dari hasil model yang sudah dibuat,  model Functional API menunjukkan kinerja terbaik dengan nilai precision sebesar 0.84 dan roc auc sebesar 0.88. Model tersebut memiliki kemampuan yang baik dalam mengidentifikasi pelanggan yang berpotensi churn. Dengan menggunakan model ini, bisnis dapat memfokuskan strategi pemasaran pada pelanggan yang memiliki risiko churn yang lebih tinggi, serta meningkatkan retensi pelanggan dan memberikan layanan yang lebih efektif.
