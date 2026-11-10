from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from divisi import Divisi


class Anggota:
    def __init__(self, id_anggota: str, nama: str, divisi: Divisi):
        if not isinstance(id_anggota, str) or not id_anggota.strip():
            raise ValueError("ID anggota tidak boleh kosong.")
        if not isinstance(nama, str) or not nama.strip():
            raise ValueError("Nama anggota tidak boleh kosong.")
        if divisi is None:
            raise ValueError("Divisi anggota tidak boleh kosong.")

        self._id_anggota = id_anggota
        self._nama = nama
        self._divisi = divisi

    @property
    def id_anggota(self) -> str:
        return self._id_anggota

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def divisi(self) -> Divisi:
        return self._divisi

    def info(self) -> str:
        return (
            f"ID: {self._id_anggota} | Nama: {self._nama} | "
            f"Divisi: {self._divisi.nama_divisi}"
        )


if __name__ == "__main__":

    class _DivisiPalsu:
        def __init__(self, nama_divisi):
            self.nama_divisi = nama_divisi

    humas = _DivisiPalsu("Divisi Humas")

    heisenberg = Anggota("A01", "Heisenberg", humas)
    print(heisenberg.info())
    assert heisenberg.id_anggota == "A01"
    assert heisenberg.nama == "Heisenberg"
    assert heisenberg.divisi is humas

    kasus_salah = [
        ("ID kosong", ("", "Heisenberg", humas)),
        ("Nama kosong", ("A02", "   ", humas)),
        ("Divisi None", ("A03", "Bowo", None)),
    ]
    for label, args in kasus_salah:
        try:
            Anggota(*args)
        except ValueError as e:
            print(f"OK ditolak ({label}): {e}")
        else:
            raise AssertionError(f"{label} seharusnya ditolak")

    try:
        heisenberg.nama = "Lain"
    except AttributeError:
        print("OK: property nama read-only")

    print("Semua uji anggota.py lolos.")
