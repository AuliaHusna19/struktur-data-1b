from collections import deque


# ==================================================================
# 1. SISTEM ANTREAN LAYANAN MAHASISWA -> QUEUE (FIFO)
# ==================================================================
class AntreanLayanan:
    def __init__(self):
        self._data = deque()              # <-- STRUKTUR DATA: Queue (deque)

    def enqueue(self, mahasiswa):         # Penambahan data, O(1)
        self._data.append(mahasiswa)      # masuk dari belakang

    def dequeue(self):                    # Penghapusan data, O(1)
        if self.is_empty():
            raise IndexError("Antrean kosong")
        return self._data.popleft()       # keluar dari depan

    def peek(self):                       # Melihat data terdepan, O(1)
        if self.is_empty():
            raise IndexError("Antrean kosong")
        return self._data[0]

    def is_empty(self):                   # Memeriksa kondisi kosong, O(1)
        return len(self._data) == 0

    def tampil(self):                     # daftar nama (depan -> belakang)
        return [m[1] for m in self._data]


# ==================================================================
# 2. FITUR UNDO -> STACK (LIFO)
# ==================================================================
class RiwayatUndo:
    def __init__(self):
        self._data = []                   # <-- STRUKTUR DATA: Stack (list)

    def push(self, aktivitas):            # Penambahan data, O(1)
        self._data.append(aktivitas)      # simpan di puncak (top)

    def pop(self):                        # Penghapusan data (Undo), O(1)
        if self.is_empty():
            raise IndexError("Tidak ada aktivitas untuk di-undo")
        return self._data.pop()           # ambil dari puncak

    def peek(self):                       # Melihat data teratas, O(1)
        if self.is_empty():
            raise IndexError("Tidak ada aktivitas untuk di-undo")
        return self._data[-1]

    def is_empty(self):                   # Memeriksa kondisi kosong, O(1)
        return len(self._data) == 0

    def tampil(self):                     # kode aktivitas (bawah -> atas)
        return [f"A{a[0]}" for a in self._data]


# ==================================================================
# SIMULASI 1: ANTREAN
# ==================================================================
def simulasi_antrean():
    print("=== SIMULASI ANTREAN (QUEUE / FIFO) ===")
    antrean = AntreanLayanan()
    mahasiswa = [(1, "Aulia"), (2, "Budi"), (3, "Citra"),
                 (4, "Dimas"), (5, "Eka")]
    langkah = 0

    def log(operasi, data):
        nonlocal langkah
        langkah += 1
        print(f"Langkah {langkah} | {operasi:<9} | {data:<6} | {antrean.tampil()}")

    # --- LANGKAH 1-5: PENAMBAHAN DATA (enqueue) ---
    for m in mahasiswa:
        antrean.enqueue(m)
        log("enqueue", m[1])

    # --- LANGKAH 6: MELIHAT DATA TERDEPAN (peek) ---
    depan = antrean.peek()
    log("peek", depan[1])

    # --- LANGKAH 7-8: PENGHAPUSAN DATA (dequeue) ---
    for _ in range(2):
        dilayani = antrean.dequeue()
        log("dequeue", dilayani[1])

    # --- LANGKAH 9: MEMERIKSA KONDISI KOSONG (is_empty) ---
    kosong = antrean.is_empty()
    log("is_empty", str(kosong))

    print("Hasil akhir antrean:", antrean.tampil())


# ==================================================================
# SIMULASI 2: UNDO
# ==================================================================
def simulasi_undo():
    print("\n=== SIMULASI UNDO (STACK / LIFO) ===")
    riwayat = RiwayatUndo()
    aktivitas = [
        (1, "06-10-2026 08:00", "Mendaftarkan data mahasiswa baru"),
        (2, "06-10-2026 08:05", "Mencetak surat keterangan aktif"),
        (3, "06-10-2026 08:10", "Memperbarui data alamat mahasiswa"),
        (4, "06-10-2026 08:15", "Menerbitkan legalisir transkrip"),
        (5, "06-10-2026 08:20", "Menghapus data KRS mahasiswa"),
    ]
    langkah = 0

    def log(operasi, data):
        nonlocal langkah
        langkah += 1
        print(f"Langkah {langkah} | {operasi:<8} | {data:<4} | Stack: {riwayat.tampil()}")

    # --- LANGKAH 1-5: PENAMBAHAN DATA (push) ---
    for a in aktivitas:
        riwayat.push(a)
        log("push", f"A{a[0]}")

    # --- LANGKAH 6: MELIHAT DATA TERATAS (peek) ---
    atas = riwayat.peek()
    log("peek", f"A{atas[0]}")

    # --- LANGKAH 7-8: PENGHAPUSAN DATA / UNDO (pop) ---
    for _ in range(2):
        dibatalkan = riwayat.pop()
        log("pop/undo", f"A{dibatalkan[0]}")
        print(f"          Dibatalkan: {dibatalkan[2]}")

    # --- LANGKAH 9: MEMERIKSA KONDISI KOSONG (is_empty) ---
    kosong = riwayat.is_empty()
    log("is_empty", str(kosong))

    print("Hasil akhir stack:", riwayat.tampil())


if __name__ == "__main__":
    simulasi_antrean()
    simulasi_undo()