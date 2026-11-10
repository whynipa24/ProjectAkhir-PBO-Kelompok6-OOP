from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from anggota import Anggota
    from kegiatan import Kegiatan


class Absensi:
    STATUS_VALID = ("Hadir", "Izin", "Sakit", "Alpa")

    def __init__(self, kegiatan: Kegiatan, anggota: Anggota, status: str):
        if kegiatan is None:
            raise ValueError("Kegiatan tidak boleh kosong.")
        if anggota is None:
            raise ValueError("Anggota tidak boleh kosong.")
        self._cek_status(status)

        self._kegiatan = kegiatan
        self._anggota = anggota
        self._status = status

    @staticmethod
    def _cek_status(status) -> None:
        if status not in Absensi.STATUS_VALID:
            raise ValueError(
                f"Status '{status}' tidak valid. "
                f"Status yang diizinkan: {', '.join(Absensi.STATUS_VALID)}."
            )

    @property
    def kegiatan(self) -> Kegiatan:
        return self._kegiatan

    @property
    def anggota(self) -> Anggota:
        return self._anggota

    @property
    def status(self) -> str:
        return self._status

    def ubah_status(self, status_baru: str) -> None:
        self._cek_status(status_baru)
        self._status = status_baru

    def info(self) -> str:
        return (
            f"Kegiatan: {self._kegiatan.nama} | "
            f"Anggota: {self._anggota.nama} | "
            f"Status: {self._status}"
        )


if __name__ == "__main__":

    class _Palsu:
        def __init__(self, nama):
            self.nama = nama

    seminar = _Palsu("Seminar Nasional")
    budi = _Palsu("Budi")

    a = Absensi(seminar, budi, "Hadir")
    print(a.info())
    a.ubah_status("Izin")
    assert a.status == "Izin"
    print(a.info())

    try:
        a.ubah_status("Telat")
    except ValueError as e:
        print(f"OK ditolak: {e}")
    else:
        raise AssertionError("Status 'Telat' seharusnya ditolak")
    assert a.status == "Izin"

    try:
        Absensi(seminar, budi, "Telat")
    except ValueError as e:
        print(f"OK ditolak di constructor: {e}")
    else:
        raise AssertionError("Constructor seharusnya menolak 'Telat'")

    for salah in ("Alfa", "hadir", "", None):
        try:
            Absensi(seminar, budi, salah)
        except ValueError:
            pass
        else:
            raise AssertionError(f"{salah!r} seharusnya ditolak")
    print("OK: 'Alfa', 'hadir', kosong, dan None ditolak")

    for k, ang in ((None, budi), (seminar, None)):
        try:
            Absensi(k, ang, "Hadir")
        except ValueError:
            pass
        else:
            raise AssertionError("None seharusnya ditolak")

    try:
        a.status = "Hadir"
    except AttributeError:
        print("OK: property status read-only")

    assert Absensi.STATUS_VALID == ("Hadir", "Izin", "Sakit", "Alpa")
    print({s: 0 for s in Absensi.STATUS_VALID})

    print("Semua uji absensi.py lolos.")
