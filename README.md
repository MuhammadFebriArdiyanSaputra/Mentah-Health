# 🧠 Mental Health Prediction AI & Dashboard

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange.svg)
![Looker Studio](https://img.shields.io/badge/Visualization-Looker_Studio-4285F4.svg)

## Overview

Proyek ini adalah sistem **Deteksi Dini Kesehatan Mental** berbasis Web. Aplikasi ini menggabungkan kekuatan **Machine Learning (XGBoost)** untuk memprediksi kebutuhan perawatan mental seseorang dan **Business Intelligence (Google Looker Studio)** untuk memvisualisasikan tren kesehatan mental global.

Tujuan utama proyek ini adalah membantu individu melakukan _self-screening_ awal berdasarkan faktor demografis, riwayat keluarga, dan kebiasaan sehari-hari.

## About the Dataset

Model dilatih menggunakan dataset berskala besar yang mencakup responden dari 35+ negara.

- **Sumber Data:** Mental Health Dataset (Global) https://www.kaggle.com/datasets/bhavikjikadara/mental-health-dataset.
- **Volume:** 292,364 Baris data.
- **Target Prediksi:** `treatment` (Yes/No) - Apakah seseorang disarankan mencari bantuan profesional?
- **Keseimbangan Data:** Dataset sangat seimbang (50% Yes : 50% No), menjadikan model tidak bias.

## Machine Learning Model

Proyek ini menggunakan algoritma **XGBoost Classifier** yang telah dioptimasi.

- **Preprocessing:**
  - **Cleaning:** Imputasi nilai _null_ pada kolom `self_employed` menggunakan modus.
  - **Ordinal Encoding:** Pemetaan manual untuk fitur bertingkat (misal: _Days Indoors_, _Mood Swings_) agar urutan logikanya terjaga (0 < 1 < 2).
  - **Label Encoding:** Untuk fitur nominal seperti _Gender_ dan _Country_.
- **Performa Model:**
  - **Akurasi:** ~80% pada data uji.
  - **Metric:** Menggunakan Logloss metric untuk evaluasi.

## Features

### 1. Interactive Dashboard

Terintegrasi dengan **Google Looker Studio** untuk menampilkan:

- Total Responden & Treatment Rate.
- Peta sebaran global.
- Hubungan antara tingkat stress, pekerjaan, dan riwayat keluarga.

### 2. AI Prediction Form

Formulir interaktif untuk pengguna melakukan tes mandiri.

- **Real-time Prediction:** Hasil langsung muncul (Disarankan Perawatan / Kondisi Aman).
- **Demo Mode:** Tombol skenario otomatis untuk simulasi kasus "Risk" (Bahaya) dan "Safe" (Aman) tanpa perlu input manual.
- **Randomizer:** Fitur pengacak input untuk keperluan testing cepat.

### 3. History Logging

Setiap prediksi yang dilakukan pengguna akan otomatis tercatat dalam file `riwayat_prediksi.csv` (Timestamp, Input Data, Hasil Prediksi) sebagai pengganti sistem tracking yang kompleks.

## Tech Stack

- **Language:** Python 3.x
- **Backend Framework:** Flask
- **Frontend:** HTML5, CSS3 (Flexbox, Responsive Design), JavaScript
- **Machine Learning:** XGBoost, Scikit-Learn, Pandas, NumPy
- **Deployment:** Localhost

## Setup

1. Install Python 3.10 or higher.
2. Install virtualenv: `pip install virtualenv`
3. Create a virtual environment: `virtualenv env`
4. Activate the environment: `env\Scripts\activate` (Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Run the app: `python app.py`
