from tiket import (
    tambah_tiket, 
    tampilkan_semua_tiket, 
    cari_tiket, 
    update_status, 
    filter_jenis_masalah, 
    hapus_tiket
)

def menu_utama():
    while True:
        print("\n==============================================")
        print("   SISTEM HELPDESK / TIKET LAYANAN (CLI)     ")
        print("==============================================")
        print("1. Tambah Tiket Baru (F1)")
        print("2. Tampilkan Semua Tiket (F2)")
        print("3. Cari Tiket (F3)")
        print("4. Update Status Tiket (F4)")
        print("5. Filter Tiket by Jenis Masalah (F5)")
        print("6. Hapus Tiket Selesai (F6)")
        print("0. Keluar Sistem")
        print("==============================================")
        
        pilihan = input("Pilih menu (0-6): ").strip()
        
        if pilihan == "1":
            tambah_tiket()
        elif pilihan == "2":
            tampilkan_semua_tiket()
        elif pilihan == "3":
            cari_tiket()
        elif pilihan == "4":
            update_status()
        elif pilihan == "5":
            filter_jenis_masalah()
        elif pilihan == "6":
            hapus_tiket()
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan Sistem Helpdesk!")
            break
        else:
            print("\nPilihan menu tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu_utama()