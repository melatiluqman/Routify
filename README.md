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
