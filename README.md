# Routify

## Folder Structur Plan
```
Routify/
├── __pycache__/        # 
├── env/                # Virtual environment (dibuat secara otomatis setelah membuat virtualenv)
├── instance/           # Folder untuk file sensitif 
│   └── db.sqlite       # File database
├── models/             # Folder untuk model database (opsional??)
│   └── users.py        # Contoh model database
├── static/             # Folder untuk file statis (CSS, JS, gambar)
│   ├── css/            # Folder untuk file CSS
│   │   └── style.css   # File CSS utama
│   ├── images/         # Folder untuk gambar
│   └── js/             # Folder untuk file JavaScript
│       └── script.js   # File JavaScript utama
├── templates/          # Folder untuk file HTML
│   ├── base.html       # Template dasar untuk inheritance
│   ├── home.html       # Halaman utama
│   ├── login.html      # Halaman login
│   └── register.html   # Halaman registrasi
├── tests/              # Folder untuk pengujian (opsional)
│   └── test_app.py     # Contoh file unit test
├── utils/              # Folder untuk fungsi tambahan 
│   ├── a_star.py       # Algoritma A*
│   └── csp.py          # Algoritma CSP
├── .gitignore          # File untuk mengabaikan file tertentu di Git
├── app.py              # Main file untuk menjalankan aplikasi Flask
├── config.py           # File konfigurasi aplikasi
└── requirements.txt    # Daftar dependensi Python (anggota team lain bisa mengisntal dependensi yang sama dengan cara: membuat virtualenv, mengaktifkan virtualenv, menjalakan perintah (pip install -r requirements.txt), menjalankan flask dengan perintah (flask run))

```

## Halaman login dan register

- Database user

  ![image](https://github.com/user-attachments/assets/5c6ecf0f-a9c0-4c15-ae82-3c2feb966868)

- Tampilan login

  ![image](https://github.com/user-attachments/assets/4822be38-a926-4f0d-8e6b-39eda9602e22)

- Tampilan Register

  ![image](https://github.com/user-attachments/assets/00c4cb3c-a5ee-40f4-90f8-163842c5c3d7)


