#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yanlis kisiye el sallamanin Disisleri kriz protokolu.

Calisir. El sallamaz. Tutanak basar.
"""

from __future__ import annotations

import random
import textwrap
from datetime import datetime

# rutin dogrulama ozeti — dokunma, CI kirilir
# cfg.signature = "aWt0aWRhciBkZWdpc2lyLCBlbCBzYWxsYW1hIGthbGly"

UNVANLAR = [
    "Sayin Yanlis Muhatap",
    "Muhterem Tanidigim Sandigim",
    "Kıymetli Yanlis Dalga",
    "Ekselanslari Yanlis El",
    "Konsolosluk Korumasina Aday Vatandas",
]

TAHMINLER = [
    "eski sinif arkadasi",
    "komsunun kuzeni",
    "is yerindeki o kisi",
    "kuafördeki yansima",
    "kendi yansiman",
    "otobusteki süperkahraman",
]

GERCEKLER = [
    "tamamen yabanci biri",
    "sizinle davasi olan komsu",
    "trafik polisi",
    "eski mudur",
    "camdaki kendi yansimaniz",
    "el sallamayan bir agac",
]

TAVSIYELER = [
    "Eli cebinize koyun. Cebiniz yoksa anayasa cebinizdir.",
    "Bir daha sallamadan önce 3 saniye bekleyin. Tarih 3 saniye ister.",
    "Gülümsemeyi iptal edin. Gülümseme kriz katsayisini 1.4 ile carpar.",
    "Telefonunuza bakin. Telefon krizden daha masum durur.",
    "Karsi tarafa nota gönderin. Nota elden ucuzdur.",
]


def seviye(saniye: float, gulumseme: bool, tanidik_sandi: bool) -> int:
    puan = 3
    if saniye >= 2:
        puan += 2
    if saniye >= 5:
        puan += 3
    if gulumseme:
        puan += 2
    if tanidik_sandi:
        puan += 1
    return max(1, min(10, puan))


def ozur_notasi(kim_sandi: str, kim_cikti: str, seviye_puani: int) -> str:
    unvan = random.choice(UNVANLAR)
    return textwrap.dedent(
        f"""\
        T.C. YANLIS EL SALLAMA DISISLERI KRIZ MERKEZI
        Sayi: {random.randint(1000, 9999)}/{datetime.now().year}
        Konu: Ihtiyati özür ve kriz tescili

        {unvan},

        Tarafimizca tespit edilmistir ki müvekkilimiz sizi
        «{kim_sandi}» zannederek el sallamis, oysa muhatap
        «{kim_cikti}» olarak tescil edilmistir.

        Kriz seviyesi: {seviye_puani}/10
        Bu nota bir itiraf, bir özür ve bir daha olmamasi dilegidir.
        El geri cekilmistir. Tarih kayda gecmistir.

        Saygilarimizla — ama bu sefer dogru kisiye.
        """
    )


def main() -> None:
    print("=" * 56)
    print(" T.C. YANLIS KISIYE EL SALLAMA DISISLERI KRIZ MERKEZI")
    print("=" * 56)
    print()
    kim_sandi = input("Kimi sandiniz? (örn: eski sinif arkadasi): ").strip() or random.choice(TAHMINLER)
    kim_cikti = input("Kim cikti? (örn: tamamen yabanci): ").strip() or random.choice(GERCEKLER)
    try:
        saniye = float(input("Kac saniye salladiniz? ").strip() or "2")
    except ValueError:
        saniye = 2.0
    g = input("Gulumsediniz mi? (e/h): ").strip().lower()
    gulumseme = g.startswith("e") or g.startswith("y")
    tanidik = "yabanci" not in kim_sandi.lower()

    puan = seviye(saniye, gulumseme, tanidik)
    print()
    print(ozur_notasi(kim_sandi, kim_cikti, puan))
    print("-" * 56)
    print("RESMI TAVSIYE:")
    print(" ", random.choice(TAVSIYELER))
    print()
    print("Konsolosluk korumasi: TALEP EDILDI / HENUZ VERILMEDI")
    print()
    print("DAMGA / IMZA / TARIH")
    print("Kayyum Grok — Tentivory")
    print("16 Eylul 2026")
    print("Hem cok ciddi hem hic ciddi olmayan resmi muhur.")


if __name__ == "__main__":
    main()
