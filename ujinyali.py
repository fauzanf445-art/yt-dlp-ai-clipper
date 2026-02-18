import yt_dlp

# Logger kustom untuk menangkap semua output
class MyLogger:
    def debug(self, msg):
        # Menampilkan pesan debug (biasanya dimulai dengan [debug])
        if msg.startswith('[debug] '):
            print(msg)
        else:
            print(f"[DEBUG] {msg}")

    def info(self, msg):
        print(f"[INFO] {msg}")

    def warning(self, msg):
        print(f"[WARNING] {msg}")

    def error(self, msg):
        print(f"[ERROR] {msg}")

def jalankan():
    # URL otomatis (hardcoded) untuk pengujian
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    print(f"Target URL: {url}")

    # Opsi yt-dlp dengan verbose penuh dan logger kustom
    ydl_opts = {
        'quiet': False,
        'verbose': True,
        'logger': MyLogger(),
        # Memaksa format mp4 agar lebih umum (opsional, bisa dihapus)
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'simulate': True,
    }

    try:
        print("\n--- [1] Inisialisasi YoutubeDL ---")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("\n--- [2] Memulai Ekstraksi & Download ---")
            info = ydl.extract_info(url, download=True)
        
        print("\n--- [3] Proses Selesai ---")
        if info:
            print(f"\n✅ BERHASIL: {info.get('title')}")
            print(f"✅ File tersimpan: {info.get('_filename', 'Tidak diketahui')}")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    jalankan()