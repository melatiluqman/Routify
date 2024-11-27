# Routify

### Folder Structur Plan
```
Routify/
├── __pycache__/        # (dibuat secara otomatis setelah menjalankan program)
├── env/                # Virtual environment (dibuat secara otomatis setelah membuat virtualenv)
├── instance/           # Folder untuk file sensitif (dibuat secara otomatis setelah menjalankan program, dan berhasil create akun di webnya)
│   └── db.sqlite       # File database
├── migrations/         # Folder untuk file migrasi database (opsional)
├── models/             # Folder untuk model database (opsional??)
│   ├── __init__.py     # Database initialization
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
│   └── sign_up.html    # Halaman registrasi
├── tests/              # Folder untuk pengujian (opsional)
│   └── test_app.py     # Contoh file unit test
├── utils/              # Folder untuk fungsi tambahan 
│   ├── a_star.py       # Algoritma A*
│   └── csp.py          # Algoritma CSP
├── .gitignore          # File untuk mengabaikan file tertentu di Git
├── app.py              # Main file untuk menjalankan aplikasi Flask
├── config.py           # File konfigurasi aplikasi
└── requirements.txt    # Daftar dependensi Python

```
