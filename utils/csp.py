from datetime import datetime, timedelta

# Fungsi untuk mengubah waktu dari string ke objek datetime
def str_to_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

# Fungsi untuk menghitung rencana perjalanan
def calculate_plan_with_travel(places, start_time, end_time, budget, kecamatan_awal, kecamatan_pulang, dest1, dest2, dest3, travel_time_minutes=15):
    # Filter tempat wisata berdasarkan destinasi yang dipilih
    selected_places = [place for place in places if place['name'] in [dest1, dest2, dest3]]
    
    # Urutkan berdasarkan waktu buka, bukan waktu tutup
    sorted_places = sorted(selected_places, key=lambda x: str_to_time(x['open_time']))  

    plan = []  # Rencana perjalanan
    current_time = str_to_time(start_time)  # Waktu mulai
    end_time_obj = str_to_time(end_time)  # Waktu selesai
    total_cost = 0  # Biaya total

    # Titik awal
    plan.append({
        'name': f"Berangkat dari Kecamatan {kecamatan_awal}",
        'visit_start': current_time.strftime("%H:%M"),
        'visit_end': (current_time + timedelta(minutes=travel_time_minutes)).strftime("%H:%M")
    })
    current_time += timedelta(minutes=travel_time_minutes)  # Waktu ke destinasi pertama

    # Buat rencana untuk destinasi yang dipilih
    for place in sorted_places:
        if total_cost + place['cost'] > budget:  # Jika biaya melebihi budget, lewati destinasi
            continue

        open_time = str_to_time(place['open_time'])
        close_time = str_to_time(place['close_time'])

        # Jika destinasi buka setelah waktu sekarang, tunggu sampai buka
        if current_time < open_time:
            current_time = open_time

        # Cek apakah destinasi bisa dikunjungi dalam waktu yang tersedia
        if current_time <= close_time and current_time + timedelta(hours=1) + timedelta(minutes=travel_time_minutes) <= end_time_obj:
            plan.append({
                'name': place['name'],
                'visit_start': current_time.strftime("%H:%M"),
                'visit_end': (current_time + timedelta(hours=1)).strftime("%H:%M")
            })
            current_time += timedelta(hours=1)  # Tambah waktu kunjungan
            current_time += timedelta(minutes=travel_time_minutes)  # Tambah waktu perjalanan ke destinasi berikutnya
            total_cost += place['cost']  # Tambah biaya ke total

    # Titik pulang
    if current_time + timedelta(minutes=travel_time_minutes) <= end_time_obj:
        plan.append({
            'name': f"Kembali ke Kecamatan {kecamatan_pulang}",
            'visit_start': current_time.strftime("%H:%M"),
            'visit_end': (current_time + timedelta(minutes=travel_time_minutes)).strftime("%H:%M")
        })

    return plan, total_cost



# Data tempat wisata
places = [
    {'name': 'Kebun Binatang Surabaya', 'open_time': '08:00', 'close_time': '16:00', 'cost': 15000},
    {'name': 'Taman Bungkul', 'open_time': '00:00', 'close_time': '23:59', 'cost': 0},
    {'name': 'Tugu Pahlawan', 'open_time': '08:00', 'close_time': '11:00', 'cost': 8000},
    {'name': 'Museum House of Sampoerna', 'open_time': '09:00', 'close_time': '22:00', 'cost': 0},
    {'name': 'Pantai Kenjeran', 'open_time': '07:00', 'close_time': '16:00', 'cost': 10000},
    {'name': 'Jembatan Suramadu', 'open_time': '00:00', 'close_time': '23:59', 'cost': 0},
    {'name': 'Pelabuhan Tanjung Perak', 'open_time': '00:00', 'close_time': '23:59', 'cost': 0},
    {'name': 'Suramadu Park', 'open_time': '00:00', 'close_time': '23:59', 'cost': 0},
    {'name': 'Galaxy Mall', 'open_time': '10:00', 'close_time': '22:00', 'cost': 0},
    {'name': 'Taman Hiburan Pantai Kenjeran', 'open_time': '07:00', 'close_time': '16:00', 'cost': 10000},
    {'name': 'House of Sampoerna', 'open_time': '09:00', 'close_time': '22:00', 'cost': 0},
    {'name': 'Balai Pemuda Surabaya', 'open_time': '07:00', 'close_time': '21:00', 'cost': 0},
    {'name': 'Museum Pendidikan', 'open_time': '08:00', 'close_time': '15:00', 'cost': 5000},
    {'name': 'Tunjungan Plaza', 'open_time': '10:00', 'close_time': '22:00', 'cost': 0},
    {'name': 'Pasar Atom', 'open_time': '09:00', 'close_time': '17:00', 'cost': 0},
    {'name': 'Pasar Genteng', 'open_time': '00:00', 'close_time': '23:59', 'cost': 0},
    {'name': 'Museum 10 Nopember', 'open_time': '08:00', 'close_time': '15:00', 'cost': 8000},
    {'name': 'Monumen Kapal Selam', 'open_time': '08:00', 'close_time': '21:00', 'cost': 15000},
    {'name': 'Kenjeran Park', 'open_time': '09:00', 'close_time': '17:00', 'cost': 15000},
    {'name': 'Klenteng Sanggar Agung', 'open_time': '07:00', 'close_time': '20:00', 'cost': 10000},
    {'name': 'Museum Kanker', 'open_time': '09:00', 'close_time': '21:00', 'cost': 0},
    {'name': 'Mall Ciputra World', 'open_time': '10:00', 'close_time': '22:00', 'cost': 0},
    {'name': 'Pakuwon Mall', 'open_time': '10:00', 'close_time': '22:00', 'cost': 0},
    {'name': 'Ciputra Waterpark', 'open_time': '13:00', 'close_time': '19:00', 'cost': 75000},
]

districts = [
    'Tegalsari', 'Wonokromo', 'Genteng', 'Dukuh Pakis', 'Wiyung', 'Sawahan',
    'Gubeng', 'Simokerto', 'Rungkut', 'Karang Pilang', 'Jambangan',
    'Gayungan', 'Tambaksari', 'Kenjeran', 'Sukolilo', 'Gunung Anyar', 'Balai Kota Surabaya'
]

# Input data dari pengguna
start_time = input("Masukkan waktu berangkat (HH:MM): ")
end_time = input("Masukkan waktu pulang (HH:MM): ")
budget = int(input("Masukkan budget (dalam rupiah): "))
kecamatan_awal = input("Masukkan kecamatan awal keberangkatan: ")
kecamatan_pulang = input("Masukkan kecamatan titik pulang: ")
dest1 = input("Masukkan destinasi 1: ")
dest2 = input("Masukkan destinasi 2: ")
dest3 = input("Masukkan destinasi 3: ")

# Rencana perjalanan otomatis
plan, total_cost = calculate_plan_with_travel(
    places, start_time, end_time, budget, kecamatan_awal, kecamatan_pulang, dest1, dest2, dest3
)

# Output rencana perjalanan
print("\nRencana perjalanan Anda:")
if plan:
    for idx, p in enumerate(plan):
        print(f"{idx + 1}. {p['name']} ({p['visit_start']} - {p['visit_end']})")
    print(f"\nTotal biaya perjalanan: Rp{total_cost:,}")
else:
    print("Tidak ada destinasi yang dapat dikunjungi dalam waktu yang tersedia atau budget tidak mencukupi.")
