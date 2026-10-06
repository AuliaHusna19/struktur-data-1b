from collections import deque


class AntreanLayanan:
    def __init__(self):
        self._data = deque()

    def enqueue(self, mahasiswa):
        self._data.append(mahasiswa)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Antrean kosong")
        return self._data.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Antrean kosong")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def tampil(self):
        return [m[1] for m in self._data]


class RiwayatUndo:
    def __init__(self):
        self._data = []

    def push(self, aktivitas):
        self._data.append(aktivitas)

    def pop(self):
        if self.is_empty():
            raise IndexError("Tidak ada aktivitas untuk di-undo")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Tidak ada aktivitas untuk di-undo")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def tampil(self):
        return [f"A{a[0]}" for a in self._data]


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

    for m in mahasiswa:
        antrean.enqueue(m)
        log("enqueue", m[1])

    depan = antrean.peek()
    log("peek", depan[1])

    for _ in range(2):
        dilayani = antrean.dequeue()
        log("dequeue", dilayani[1])

    kosong = antrean.is_empty()
    log("is_empty", str(kosong))

    print("Hasil akhir antrean:", antrean.tampil())


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

    for a in aktivitas:
        riwayat.push(a)
        log("push", f"A{a[0]}")

    atas = riwayat.peek()
    log("peek", f"A{atas[0]}")

    for _ in range(2):
        dibatalkan = riwayat.pop()
        log("pop/undo", f"A{dibatalkan[0]}")
        print(f"          Dibatalkan: {dibatalkan[2]}")

    kosong = riwayat.is_empty()
    log("is_empty", str(kosong))

    print("Hasil akhir stack:", riwayat.tampil())


if __name__ == "__main__":
    simulasi_antrean()
    simulasi_undo()