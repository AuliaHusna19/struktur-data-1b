import unittest
from antrean_undo import AntreanLayanan, RiwayatUndo


# ==================================================================
# PENGUJIAN FITUR ANTREAN (QUEUE)
# ==================================================================
class TestAntrean(unittest.TestCase):
    def setUp(self):
        self.antrean = AntreanLayanan()

    # --- Penambahan data (enqueue) ---
    def test_enqueue_satu_data(self):
        self.antrean.enqueue((1, "Aulia"))
        self.assertEqual(self.antrean.tampil(), ["Aulia"])

    def test_enqueue_tiga_data_urutan_tetap(self):
        for m in [(1, "Aulia"), (2, "Budi"), (3, "Citra")]:
            self.antrean.enqueue(m)
        self.assertEqual(self.antrean.tampil(), ["Aulia", "Budi", "Citra"])

    # --- Penghapusan data (dequeue) ---
    def test_dequeue_keluar_urutan_fifo(self):
        self.antrean.enqueue((1, "Aulia"))
        self.antrean.enqueue((2, "Budi"))
        self.assertEqual(self.antrean.dequeue(), (1, "Aulia"))
        self.assertEqual(self.antrean.tampil(), ["Budi"])

    def test_dequeue_antrean_kosong_error(self):
        with self.assertRaises(IndexError):
            self.antrean.dequeue()

    # --- Melihat data terdepan (peek) ---
    def test_peek_tidak_menghapus_data(self):
        self.antrean.enqueue((1, "Aulia"))
        self.antrean.enqueue((2, "Budi"))
        self.assertEqual(self.antrean.peek(), (1, "Aulia"))
        self.assertEqual(self.antrean.tampil(), ["Aulia", "Budi"])

    def test_peek_antrean_kosong_error(self):
        with self.assertRaises(IndexError):
            self.antrean.peek()

    # --- Memeriksa kondisi kosong (is_empty) ---
    def test_is_empty_antrean_baru(self):
        self.assertTrue(self.antrean.is_empty())

    def test_is_empty_setelah_enqueue(self):
        self.antrean.enqueue((1, "Aulia"))
        self.assertFalse(self.antrean.is_empty())

    def test_is_empty_setelah_semua_dequeue(self):
        self.antrean.enqueue((1, "Aulia"))
        self.antrean.dequeue()
        self.assertTrue(self.antrean.is_empty())


# ==================================================================
# PENGUJIAN FITUR UNDO (STACK)
# ==================================================================
class TestUndo(unittest.TestCase):
    def setUp(self):
        self.riwayat = RiwayatUndo()

    # --- Penambahan data (push) ---
    def test_push_satu_aktivitas(self):
        self.riwayat.push((1, "06-10-2026 08:00", "Daftar mahasiswa"))
        self.assertEqual(self.riwayat.tampil(), ["A1"])

    def test_push_tiga_aktivitas_urutan_tetap(self):
        for a in [(1, "08:00", "X"), (2, "08:05", "Y"), (3, "08:10", "Z")]:
            self.riwayat.push(a)
        self.assertEqual(self.riwayat.tampil(), ["A1", "A2", "A3"])

    # --- Penghapusan data / Undo (pop) ---
    def test_pop_keluar_urutan_lifo(self):
        self.riwayat.push((1, "08:00", "X"))
        self.riwayat.push((2, "08:05", "Y"))
        self.assertEqual(self.riwayat.pop(), (2, "08:05", "Y"))
        self.assertEqual(self.riwayat.tampil(), ["A1"])

    def test_pop_stack_kosong_error(self):
        with self.assertRaises(IndexError):
            self.riwayat.pop()

    # --- Melihat data teratas (peek) ---
    def test_peek_tidak_menghapus_data(self):
        self.riwayat.push((1, "08:00", "X"))
        self.riwayat.push((2, "08:05", "Y"))
        self.assertEqual(self.riwayat.peek(), (2, "08:05", "Y"))
        self.assertEqual(self.riwayat.tampil(), ["A1", "A2"])

    def test_peek_stack_kosong_error(self):
        with self.assertRaises(IndexError):
            self.riwayat.peek()

    # --- Memeriksa kondisi kosong (is_empty) ---
    def test_is_empty_stack_baru(self):
        self.assertTrue(self.riwayat.is_empty())

    def test_is_empty_setelah_push(self):
        self.riwayat.push((1, "08:00", "X"))
        self.assertFalse(self.riwayat.is_empty())

    def test_is_empty_setelah_semua_pop(self):
        self.riwayat.push((1, "08:00", "X"))
        self.riwayat.pop()
        self.assertTrue(self.riwayat.is_empty())


if __name__ == "__main__":
    unittest.main()