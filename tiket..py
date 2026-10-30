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
    
