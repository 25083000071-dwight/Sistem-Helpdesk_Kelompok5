# Array of Struct (List of Dictionaries) untuk menyimpan seluruh data tiket
daftar_tiket = []

JENIS_MASALAH_VALID = ["Hardware", "Software", "Jaringan", "Lainnya"]
PRIORITAS_VALID = ["Rendah", "Sedang", "Tinggi"]

def tambah_tiket():
    print("\n=== F1: TAMBAH TIKET BARU ===")
    
    # Validasi kode tiket
    while True:
        kode = input("Masukkan Kode Tiket (cth: TKT001): ").strip()
        if not kode:
            print("Error: Kode tiket tidak boleh kosong!")
            continue
        if any(t['kode_tiket'].lower() == kode.lower() for t in daftar_tiket):
            print(f"Error: Kode tiket '{kode}' sudah digunakan!")
            continue
        break

    # Validasi nama pelapor
    while True:
        nama = input("Masukkan Nama Pelapor: ").strip()
        if not nama:
            print("Error: Nama pelapor tidak boleh kosong!")
            continue
        break

    # Validasi jenis masalah
    print(f"Pilihan Jenis Masalah: {', '.join(JENIS_MASALAH_VALID)}")
    while True:
        jenis_input = input("Masukkan Jenis Masalah: ").strip()
        jenis = jenis_input.capitalize()
        if jenis not in JENIS_MASALAH_VALID:
            print("Error: Jenis masalah tidak valid!")
            continue
        break

    # Validasi deskripsi
    while True:
        deskripsi = input("Masukkan Deskripsi Masalah: ").strip()
        if not deskripsi:
            print("Error: Deskripsi tidak boleh kosong!")
            continue
        break

    # Validasi prioritas
    print(f"Pilihan Prioritas: {', '.join(PRIORITAS_VALID)}")
    while True:
        prioritas_input = input("Masukkan Prioritas: ").strip()
        prioritas = prioritas_input.capitalize()
        if prioritas not in PRIORITAS_VALID:
            print("Error: Prioritas tidak valid!")
            continue
        break

    # Simpan ke dictionary
    tiket_baru = {
        "kode_tiket": kode,
        "nama_pelapor": nama,
        "jenis_masalah": jenis,
        "deskripsi": deskripsi,
        "prioritas": prioritas,
        "status": "Menunggu"
    }
    
    daftar_tiket.append(tiket_baru)
    print(f"\nSukses: Tiket [{kode}] dari [{nama}] berhasil dicatat.")

def tampilkan_semua_tiket():
    print("\n=== F2: DAFTAR TIKET LAYANAN ===")
    if not daftar_tiket:
        print("Pesan: Belum ada tiket dalam sistem.")
        return

    print("-" * 75)
    print(f"{'No':<4} | {'Kode':<8} | {'Nama Pelapor':<18} | {'Jenis':<10} | {'Prioritas':<10} | {'Status':<10}")
    print("-" * 75)
    
    menunggu = diproses = selesai = 0
    for idx, t in enumerate(daftar_tiket, 1):
        prio_str = f"[{t['prioritas']}]"
        stat_str = f"[{t['status']}]"
        print(f"{idx:<4} | {t['kode_tiket']:<8} | {t['nama_pelapor']:<18} | {t['jenis_masalah']:<10} | {prio_str:<10} | {stat_str:<10}")
        
        if t['status'] == "Menunggu":
            menunggu += 1
        elif t['status'] == "Diproses":
            diproses += 1
        elif t['status'] == "Selesai":
            selesai += 1
        
    print("-" * 75)
    print(f"Ringkasan: Total: {len(daftar_tiket)} | Menunggu: {menunggu} | Diproses: {diproses} | Selesai: {selesai}")

    def cari_tiket():
    print("\n=== F3: CARI TIKET ===")
    print("1. Cari berdasarkan Kode Tiket (Exact Match)")
    print("2. Cari berdasarkan Nama Pelapor (Partial Match)")
    pilihan = input("Pilih mode pencarian (1/2): ").strip()

    if pilihan == "1":
        kode = input("Masukkan Kode Tiket: ").strip().lower()
        if not kode:
            print("Error: Kata kunci tidak boleh kosong!")
            return
        
        hasil = [t for t in daftar_tiket if t['kode_tiket'].lower() == kode]
        if hasil:
            t = hasil[0]
            print("\n--- Detail Tiket Ditemukan ---")
            print(f"Kode Tiket    : {t['kode_tiket']}")
            print(f"Nama Pelapor  : {t['nama_pelapor']}")
            print(f"Jenis Masalah : {t['jenis_masalah']}")
            print(f"Deskripsi     : {t['deskripsi']}")
            print(f"Prioritas     : {t['prioritas']}")
            print(f"Status        : {t['status']}")
        else:
            print(f"Pesan: Tiket dengan kode '{kode}' tidak ditemukan.")

    elif pilihan == "2":
        nama = input("Masukkan Kata Kunci Nama Pelapor: ").strip().lower()
        if not nama:
            print("Error: Kata kunci tidak boleh kosong!")
            return
        
        hasil = [t for t in daftar_tiket if nama in t['nama_pelapor'].lower()]
        if hasil:
            print(f"\nMenampilkan {len(hasil)} tiket ditemukan:")
            print("-" * 75)
            print(f"{'No':<4} | {'Kode':<8} | {'Nama Pelapor':<18} | {'Jenis':<10} | {'Prioritas':<10} | {'Status':<10}")
            print("-" * 75)
            for idx, t in enumerate(hasil, 1):
                prio_str = f"[{t['prioritas']}]"
                stat_str = f"[{t['status']}]"
                print(f"{idx:<4} | {t['kode_tiket']:<8} | {t['nama_pelapor']:<18} | {t['jenis_masalah']:<10} | {prio_str:<10} | {stat_str:<10}")
            print("-" * 75)
        else:
            print(f"Pesan: Tiket dengan nama pelapor '{nama}' tidak ditemukan.")
    else:
        print("Error: Pilihan tidak valid.")

def update_status():
    print("\n=== F4: UPDATE STATUS TIKET ===")
    kode = input("Masukkan Kode Tiket yang ingin di-update: ").strip().lower()
    
    tiket_target = None
    for t in daftar_tiket:
        if t['kode_tiket'].lower() == kode:
            tiket_target = t
            break

    if not tiket_target:
        print(f"Pesan: Tiket dengan kode '{kode}' tidak ditemukan.")
        return

    status_saat_ini = tiket_target['status']
    if status_saat_ini == "Selesai":
        print(f"Pesan: Tiket [{tiket_target['kode_tiket']}] sudah berstatus Selesai dan tidak dapat diperbarui lagi.")
        return

    status_berikutnya = "Diproses" if status_saat_ini == "Menunggu" else "Selesai"
    
    print("\nKonfirmasi Perubahan Status:")
    print(f"Kode Tiket       : {tiket_target['kode_tiket']}")
    print(f"Nama Pelapor     : {tiket_target['nama_pelapor']}")
    print(f"Status Saat Ini  : {status_saat_ini}")
    print(f"Status Berikutnya: {status_berikutnya}")

    konfirmasi = input("Apakah Anda yakin ingin memperbarui status? (y/n): ").strip().lower()
    if konfirmasi == 'y':
        tiket_target['status'] = status_berikutnya
        print(f"Sukses: Status tiket [{tiket_target['kode_tiket']}] berhasil diperbarui dari {status_saat_ini} menjadi {status_berikutnya}.")
    else:
        print("Update status dibatalkan.")

def filter_jenis_masalah():
    print("\n=== F5: FILTER TIKET BERDASARKAN JENIS MASALAH ===")
    print(f"Pilihan Kategori: {', '.join(JENIS_MASALAH_VALID)}")
    jenis = input("Masukkan Jenis Masalah: ").strip().capitalize()

    if jenis not in JENIS_MASALAH_VALID:
        print("Error: Pilihan jenis masalah tidak valid.")
        return

    hasil = [t for t in daftar_tiket if t['jenis_masalah'] == jenis]
    if hasil:
        print(f"\nMenampilkan tiket jenis masalah '{jenis}' ({len(hasil)} tiket ditemukan):")
        print("-" * 75)
        print(f"{'No':<4} | {'Kode':<8} | {'Nama Pelapor':<18} | {'Jenis':<10} | {'Prioritas':<10} | {'Status':<10}")
        print("-" * 75)
        for idx, t in enumerate(hasil, 1):
            prio_str = f"[{t['prioritas']}]"
            stat_str = f"[{t['status']}]"
            print(f"{idx:<4} | {t['kode_tiket']:<8} | {t['nama_pelapor']:<18} | {t['jenis_masalah']:<10} | {prio_str:<10} | {stat_str:<10}")
        print("-" * 75)
    else:
        print(f"Pesan: Tidak ada tiket dengan jenis masalah '{jenis}' dalam sistem.")

def hapus_tiket():
    print("\n=== F6: HAPUS TIKET ===")
    kode = input("Masukkan Kode Tiket yang akan dihapus: ").strip().lower()

    tiket_target = None
    for t in daftar_tiket:
        if t['kode_tiket'].lower() == kode:
            tiket_target = t
            break

    if not tiket_target:
        print(f"Pesan: Tiket dengan kode '{kode}' tidak ditemukan.")
        return

    if tiket_target['status'] != "Selesai":
        print(f"Pesan: Tiket [{tiket_target['kode_tiket']}] tidak dapat dihapus karena masih berstatus '{tiket_target['status']}'. Selesaikan penanganan tiket terlebih dahulu.")
        return

    print("\nDetail Tiket Akan Dihapus:")
    print(f"Kode / Pelapor : {tiket_target['kode_tiket']} / {tiket_target['nama_pelapor']}")
    print(f"Jenis / Status : {tiket_target['jenis_masalah']} / {tiket_target['status']}")

    konfirmasi = input("Apakah Anda yakin ingin menghapus tiket ini? (y/n): ").strip().lower()
    if konfirmasi == 'y':
        daftar_tiket.remove(tiket_target)
        print(f"Sukses: Tiket [{tiket_target['kode_tiket']}] dari [{tiket_target['nama_pelapor']}] berhasil dihapus dari sistem.")
    else:
        print("Pesan: Penghapusan dibatalkan.")
