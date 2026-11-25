#NAMA: MUHAMMAD FAIZALL
#NPM : 2615061083
#KELAS: TI-D

transaksi_list = []

def format_rupiah(nominal):
    """Mengformat angka integer menjadi format tampilan Rupiah (misal: Rp 50.000)."""
    return f"Rp {nominal:,}".replace(",", ".")

def input_nominal():
    """
    Meminta input nominal berupa bilangan bulat > 0.
    Memiliki validasi perulangan sampai user memasukkan input yang valid (bebas error/crash).
    """
    while True:
        try:
            val_input = input("Masukkan nominal (angka bulat > 0): ").strip()
            nominal = int(val_input)
            if nominal > 0:
                return nominal
            else:
                print("[!] Error: Nominal harus bilangan bulat lebih besar dari 0.")
        except ValueError:
            print("[!] Error: Input tidak valid! Masukkan hanya angka bulat (tanpa huruf/desimal).")

def hitung_total_pemasukan():
    """Menghitung total seluruh transaksi bertipe 'Masuk'."""
    total = 0
    for t in transaksi_list:
        if t['jenis'] == 'Masuk':
            total += t['nominal']
    return total

def hitung_total_pengeluaran():
    """Menghitung total seluruh transaksi bertipe 'Keluar'."""
    total = 0
    for t in transaksi_list:
        if t['jenis'] == 'Keluar':
            total += t['nominal']
    return total

def hitung_saldo():
    """Menghitung saldo saat ini (Total Pemasukan - Total Pengeluaran)."""
    return hitung_total_pemasukan() - hitung_total_pengeluaran()

def tambah_transaksi():
    """Fitur 1: Menambah transaksi baru (Pemasukan atau Pengeluaran)."""
    print("\n--- TAMBAH TRANSAKSI ---")
    
    # 1. Validasi Jenis Transaksi (Case-insensitive & strip whitespace)
    jenis_input = input("Masukkan jenis transaksi (masuk/keluar): ").strip().lower()
    if jenis_input not in ['masuk', 'keluar']:
        print("[!] Error: Jenis transaksi hanya boleh 'masuk' atau 'keluar'. Kembali ke menu utama.")
        return

    # 2. Input Nominal Transaksi
    nominal = input_nominal()

    # 3. Validasi Saldo untuk Pengeluaran
    if jenis_input == 'keluar':
        saldo_saat_ini = hitung_saldo()
        if nominal > saldo_saat_ini:
            print(f"[!] Transaksi ditolak: Nominal pengeluaran ({format_rupiah(nominal)}) melebihi saldo saat ini ({format_rupiah(saldo_saat_ini)}).")
            return

    # 4. Penentuan Kategori
    if jenis_input == 'masuk':
        jenis_str = 'Masuk'
        kategori = 'Pemasukan'
    else:
        jenis_str = 'Keluar'
        print("\nPilih Kategori Pengeluaran:")
        print("1. Makan")
        print("2. Transport")
        print("3. Hiburan")
        print("4. Lainnya")
        pilihan_kat = input("Pilih nomor kategori (1-4): ").strip()
        
        if pilihan_kat == '1':
            kategori = 'Makan'
        elif pilihan_kat == '2':
            kategori = 'Transport'
        elif pilihan_kat == '3':
            kategori = 'Hiburan'
        else:
            kategori = 'Lainnya'

    # 5. Input Keterangan/Catatan
    catatan_raw = input("Masukkan catatan/keterangan: ").strip()
    if catatan_raw == "":
        catatan = "-"
    else:
        catatan = catatan_raw.title()

    # 6. Simpan Transaksi ke List
    transaksi = {
        'jenis': jenis_str,
        'nominal': nominal,
        'kategori': kategori,
        'catatan': catatan
    }
    transaksi_list.append(transaksi)
    print(f"[✓] Berhasil: Transaksi {jenis_str} sebesar {format_rupiah(nominal)} berhasil dicatat.")

def lihat_riwayat():
    """Fitur 2: Menampilkan seluruh riwayat transaksi bernomor urut."""
    print("\n--- RIWAYAT TRANSAKSI ---")
    if not transaksi_list:
        print("Belum ada transaksi yang tercatat.")
        return

    print(f"{'No.':<4} | {'Jenis':<8} | {'Kategori':<12} | {'Nominal':<14} | {'Catatan'}")
    print("-" * 65)
    for idx, t in enumerate(transaksi_list, start=1):
        print(f"{idx:<4} | {t['jenis']:<8} | {t['kategori']:<12} | {format_rupiah(t['nominal']):<14} | {t['catatan']}")

def rekap_kategori():
    """Fitur 3: Menampilkan total pengeluaran untuk tiap kategori."""
    print("\n--- REKAP PENGELUARAN PER KATEGORI ---")
    rekap = {
        'Makan': 0,
        'Transport': 0,
        'Hiburan': 0,
        'Lainnya': 0
    }

    for t in transaksi_list:
        if t['jenis'] == 'Keluar':
            kat = t['kategori']
            if kat in rekap:
                rekap[kat] += t['nominal']
            else:
                rekap['Lainnya'] += t['nominal']

    for kat, total in rekap.items():
        print(f"- {kat:<10} : {format_rupiah(total)}")
    print("-" * 35)
    print(f"Total Pengeluaran : {format_rupiah(hitung_total_pengeluaran())}")

def cek_status_keuangan():
    """Fitur 4: Menampilkan rincian keuangan dan status keuangan (Hemat/Wajar/Boros)."""
    print("\n--- STATUS KEUANGAN ---")
    pemasukan = hitung_total_pemasukan()
    pengeluaran = hitung_total_pengeluaran()
    saldo = hitung_saldo()

    print(f"Total Pemasukan   : {format_rupiah(pemasukan)}")
    print(f"Total Pengeluaran : {format_rupiah(pengeluaran)}")
    print(f"Saldo Saat Ini    : {format_rupiah(saldo)}")

    if pemasukan == 0:
        status = "Belum ada pemasukan"
        persentase_str = "0.00%"
    else:
        persentase = (pengeluaran / pemasukan) * 100
        persentase_str = f"{persentase:.2f}%"
        if persentase > 90:
            status = "Boros"
        elif persentase > 60:
            status = "Wajar"
        else:
            status = "Hemat"

    print(f"Persentase Sebar  : {persentase_str}")
    print(f"Status Keuangan   : {status}")

def main():
    """Fungsi utama pengendali alur program (Menu Utama)."""
    while True:
        print("\n=== PENCATAT KEUANGAN ===")
        print("1. Tambah transaksi")
        print("2. Lihat riwayat")
        print("3. Rekap pengeluaran per kategori")
        print("4. Cek status keuangan")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == '1':
            tambah_transaksi()
        elif pilihan == '2':
            lihat_riwayat()
        elif pilihan == '3':
            rekap_kategori()
        elif pilihan == '4':
            cek_status_keuangan()
        elif pilihan == '0':
            print("\nTerima kasih!")
            break
        else:
            print("[!] Pilihan menu tidak valid. Silakan pilih nomor yang tersedia.")

if __name__ == "__main__":
    main()