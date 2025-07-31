# Admin Finder

Skrip Python sederhana dan cepat untuk menemukan panel admin potensial pada sebuah website target menggunakan wordlist dan multithreading.

## Fitur
- Pemindaian multithread untuk hasil yang cepat
- Wordlist dapat dikustomisasi
- Deteksi kode status HTTP (200, 301, 302, 403, 401)
- Include dengan wordlist

## Persyaratan
- Python 3.x
- Library `requests`

Instal dependensi:
```
pip install -r requirements.txt
```

## Penggunaan

Jalankan skrip:
```
python main.py
```

Anda akan diminta untuk mengisi:
- URL target (misal: https://example.com)
- File wordlist (default: wordlist.txt)
- Jumlah thread (default: 10)
## Contoh
```
🔍 ADMIN PANEL FINDER
Script by @yogakokxd
==============================
Masukkan URL target (misal: https://example.com): https://example.com
Masukkan file wordlist (default: wordlist.txt):
Masukkan jumlah thread (default: 10):
🎯 Target: https://example.com
📁 Wordlist: wordlist.txt
🧵 Threads: 10
==================================================
📋 Memuat 100 path untuk dicek
🔍 Memulai scan...

✅ Ditemukan: admin - Status: 200
🔄 Ditemukan: login - Status: 301
...

📊 HASIL SCAN
==================================================
⏱️  Durasi: 2.34 detik
📈 Dicek: 100/100 path
🎯 Ditemukan: 3 panel admin potensial

🔍 PANEL ADMIN POTENSIAL:
--------------------------------------------------
✅ admin
   URL: https://example.com/admin
   Status: 200
...
```
```

## Wordlist
Edit atau ganti `wordlist.txt` dengan daftar path admin potensial milik Anda sendiri. Baris yang diawali `#` akan diabaikan.

## Repo & Kontak
- Repo: [github.com/yogaxdd/admin-finder](https://github.com/yogaxdd/admin-finder)
- Sosial Media: [@yogakokxd](https://t.me/yogakokxd)
