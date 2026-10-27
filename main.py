# Proyek Membuat Software ATM
 
#Kamus 
# Username, pin : string
# fitur : array [0 ... 5] of string
# saldo : int
# history : array of string


#Algoritma
#Mendefinisikan variabel yang diperlukan
username = "User"
pin = "123456"
fitur = ["Cek Saldo", "Setor Tunai", "Tarik Tunai", "Transfer", "Riwayat Transaksi", "Exit"]
saldo = 1000000
history = []

# Membuat SubProgram yang diperlukan
def login(input_pin):
    # Program Login 
    
    #Kamus 
    # input_pin = string

    #Algoritma
    #Mengecek apakah pin yang dimasukan sudah sesuai
    if input_pin == pin:
        return True
    else:
        return False 

def CekSaldo():
    # Program Fitur CekSaldo

    #Kamus 
    #saldo: int

    #Algoritma
    #Menampilkan saldo
    print("\n=== SALDO ===")
    print("Nominal saldo akhir anda :")
    print(f"Rp {saldo},00\n")

def SetorTunai():
    # Program FiturSetorTunai

    # Kamus
    # saldo   : int
    # nominal : int
    # berhasil : bool
    # history : array of string

    # Inisialisasi saldo awal
    global saldo

    # Algoritma
    # Mencetak tampilan awal
    print("=== SETOR TUNAI ===")
    print("Saldo Anda saat ini: Rp", saldo)
    print("----------------------------------")

    berhasil = False
    
    while berhasil == False:
        #Mengecek apakah nominal yang dimasukkan mengandung selain angka atau tidak 
        try:
            # Input nominal setoran
            nominal = int(input("Masukkan nominal setoran: Rp "))
        except ValueError:
            print("Setor tunai gagal: nomimal harus dalam bentuk angka")
            continue
        # Pengecekan nominal
        if nominal <= 0:
            print("Setor tunai gagal: nominal harus lebih besar dari 0.")
        elif nominal % 50000 != 0:
            print("Setor tunai gagal: masukkan nominal kelipatan Rp50.000.")
        else:
            # Saldo bertambah
            history.append(f"Setor tunai sebesar Rp {nominal}")
            berhasil = True
            saldo = saldo + nominal
            print(">>> SETOR TUNAI BERHASIL <<<")
            print("Uang sebesar Rp", nominal, "berhasil disetor")

def TarikTunai():
    #Program FiturTarikTunai
    
    #Kamus
    #saldo: int
    #nominal : int
    # berhasil : bool
    # history : array of string

    #Algoritma
    print("\n=== TARIK TUNAI ===")
    berhasil = False
    global saldo
    
    while berhasil == False:
        #Mengecek apakah nominal yang dimasukkan mengandung selain angka atau tidak 
        try:
            #Masukkan nominal yang ingin diambil
            nominal = int(input("Masukkan nominal pengambilan: Rp "))
        except ValueError:
            print("Tarik tunai gagal: nominal harus dalam bentuk angka")
            continue
        
        #Pengecekan apakah nominal yang di input bisa diambil atau tidak
        if nominal<=0:
            print("Tarik tunai gagal: nominal harus lebih besar dari 0")
        elif nominal%50000!=0:
            print("Tarik tunai gagal: masukkan nomimal kelipatan Rp50.000 atau Rp100.000")
        elif saldo < nominal:
            print("Tarik tunai gagal: Saldo Anda tidak mencukupi ")
        else:
            history.append(f"Tarik tunai sebesar Rp {nominal}")
            print("\n>>> TARIK TUNAI BERHASIL <<<")
            saldo -= nominal
            print(f"Uang sebesar Rp {nominal},00 berhasil diambil")
            berhasil = True
            

def Transfer():
    # Program FiturTransferBank

    # Kamus
    # saldo          : int
    # norek_tujuan   : str
    # nominal        : int
    # berhasil       : bool

    # Inisialisasi saldo awal
    global saldo

    # Algoritma
    print("\n=== TRANSFER SESAMA BANK ===")
    print("Saldo Anda saat ini: Rp", saldo)
    print("----------------------------------")

    berhasil = False

    while berhasil == False:
        try:
            # Input dari pengguna
            norek_tujuan = input("Masukkan nomor rekening tujuan: ")
        except ValueError:
            print("Transfer gagal: nomor rekening harus dalam bentuk angka")
            continue
        if len(norek_tujuan) != 10:
            print("Transfer Gagal: Nomor rekening tujuan tidak valid.")
            continue

        #Mengecek apakah nominal yang dimasukkan mengandung selain angka atau tidak 
        
        try:
            #Input dari pengguna
            nominal = int(input("Masukkan nominal transfer: Rp "))
        except ValueError:
            print("Transfer gagal: nominal harus dalam bentuk angka")
            continue

        # Pengecekan kondisi sebelum uang dikirim
        if nominal < 10000:
            print("Transfer Gagal: Batas minimal transfer adalah Rp10.000.")

        elif nominal > saldo:
            print("Transfer Gagal: Saldo Anda tidak mencukupi.")
        else:
            # Proses pemotongan saldo 
            history.append(f"Transfer ke rekening {norek_tujuan} sebesar Rp {nominal}")
            berhasil = True
            saldo = saldo - nominal
            print("\n>>> TRANSFER BERHASIL <<<")
            print("Ke Rekening  :", norek_tujuan)
            print("Nominal      : Rp", nominal)
            print("Biaya Admin  : Rp 0 (Sesama Bank)")
            print("--------------------------")

def RiwayatTransaksi():
    # Program untuk Melihat Riwayat Transaksi 
    
    # Kamus
    # history : array of string
    
    global history
    print("\n=== Riwayat Transaksi ===\n")
    
    if len(history) == 0:
        print("Belum ada riwayat Transaksi")
    else:  
        # Mencetak history traksasi jika sudah ada
        i = 1
        for setiap in history:
            print(f"{i}. {setiap}")
            i += 1
    print()

# Sub Program Utama
def main():
    # Sub Program Utama untuk menampung dan menjalankan sub program lain 
    
    # Kamus
    # Kesempatan_login : int
    # sudahLogin, ulang, exit, sesuai, ulang, exit : bool 
    # input_pin, pilihan fitur, input lanjut : string
    # fitur : array [0 ... 5] of string
    
    #Algoritma
    # Mencetak tampilan Awal
    print("\n=======================================")
    print("             Selamat Datang di ATM       ")
    print("=======================================\n")

    # Memberikan Kesempatan Login 3 kali
    kesempatan_login = 3
    sudahLogin = False
    #Mengecek apakah sudah login?
    while sudahLogin == False and kesempatan_login > 0:
        kesempatan_login -= 1
        #Mengecek apakah pin yang dimasukan benar/tidak
        input_pin = input("Silahkan Masukkan Pin Anda: ")
        sudahLogin = login(input_pin)
        if sudahLogin == False:
            #Jika pin yang dimasukan salah, kesempatan berkurang
            print(f"PIN YANG ANDA MASUKKAN SALAH, SISA KESEMPATAN ANDA {kesempatan_login} KALI LAGI")
            
    # Jika sudah 3 kali percobaan dan tetap salah, maka kartu ATM di blokir ( Program langsung selesai)
    if sudahLogin == False:
        print("\n=========================================")
        print("Anda telah salah memasukan PIN sebanyak 3 KALI!")
        print("Kartu ATM anda di BLOKIR!")
        print("TOLONG SEGERA MENGURUS KE CABANG TERDEKAT!")
        print("==========================================\n")
        quit()

    # Mendeklarasikan varibel validasi    
    ulang = True
    exit = False
    # Menampilkan layanan yang tersedia
    while exit == False:
        sesuai = True
        if ulang == True:
            print("\n==========================================================")
            print("                  Silahkan Pilih Layanan!                 ")
            print("Dengan Menekan Angka Sesuai dengan Layanan yang Diinginkan")
            print("==========================================================\n")
            # Mencetak layanan yang tersedia
            i = 1
            for fit in fitur:
                print(f"{i}: {fit}")
                i += 1
                
        # Memilih layanan yang akan digunakan
        pilihan_fitur = input("\nLayanan yang ingin digunakan: ")
        if pilihan_fitur in ["1", "2", "3", "4", "5", "6"]:
            if pilihan_fitur == "1":
                #Layanan CekSaldo
                CekSaldo()
            elif pilihan_fitur == "2":
                #Layanan Setor Tunai
                SetorTunai()
                CekSaldo()
            elif pilihan_fitur == "3":
                #Layanan Tarik Tunai
                TarikTunai()
                CekSaldo()
            elif pilihan_fitur == "4":
                #Layanan Transfer
                Transfer()
                CekSaldo()
            elif pilihan_fitur == "5":
                #RiwayatTransaksi
                RiwayatTransaksi()
            elif pilihan_fitur == "6":
                #Keluar dari ATM
                exit = True
                sesuai = False
        else:
            # Jika masukan tidak sesuai yang di inginkan
            print("Input yang anda masukkan tidak sesuai, Tolong perhatikan instruksinya")
            ulang = False
            sesuai = False

        if sesuai == True:
            ulang = True
            # Apakah ingin melanjutkan transaksi/tidak?
            while True:
                input_lanjut = input("Apakah ingin melanjutkan transaksi? (y/n): ")
                if input_lanjut == "n":
                    exit = True
                    break
                elif input_lanjut=="y":
                    # Jika ya, keluar dari loop dan lanjut transaksi
                    break
                else:
                    print("Jawab dengan y atau n saja. Silahkan coba lagi")
                
    #Mencetak Tampilan Akhir
    print("\n==========================================================")
    print("                      Terima kasih!                       ")
    print("==========================================================\n")

# Memanggil fungsi utama agar program bisa berjalan
main()