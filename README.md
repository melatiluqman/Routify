# Routify

### Folder Structur Plan
```
Routify/
├── env/                # Virtual environment (tidak dibuat secara manual, dibuat setelah membuat virtualenv)
├── migrations/         # Folder untuk file migrasi database
├── models/             # Folder untuk model database
│   └── user.py         # Contoh model database
├── static/             # Folder untuk file statis (CSS, JS, gambar)
│   ├── css/            # Folder untuk file CSS
│   │   └── style.css   # File CSS utama
│   ├── images/         # Folder untuk gambar
│   └── js/             # Folder untuk file JavaScript
│       └── script.js   # File JavaScript utama
├── templates/          # Folder untuk file HTML
│   ├── base.html       # Template dasar untuk inheritance
│   └── index.html      # Halaman utama
├── tests/              # Folder untuk pengujian
│   └── test_app.py     # Contoh file unit test
├── utils/              # Folder untuk fungsi atau algoritma tambahan
│   ├── a_star.py       # Algoritma A*
│   └── csp.py          # Algoritma CSP
├── .gitignore          # File untuk mengabaikan file tertentu di Git
├── app.py              # Main file untuk menjalankan aplikasi Flask
├── config.py           # File konfigurasi aplikasi
└── requirements.txt    # Daftar dependensi Python anggota per-team (disarankan memiliki dependensi python yang sama)
```
