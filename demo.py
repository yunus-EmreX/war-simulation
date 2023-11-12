import random
import math

# Farklı bölgelerdeki rastgele nüfusları belirle
gaza_population = random.randint(500000, 600000)
refah_population = random.randint(200000, 250000)
han_yunus_population = random.randint(150000, 200000)
sderot_population = random.randint(25000, 30000)
ashkelon_population = random.randint(140000, 150000)
beersheba_population = random.randint(200000, 220000)

total_population = gaza_population + refah_population + han_yunus_population + sderot_population + ashkelon_population + beersheba_population

# Füzelerin isimlerini, sapma açılarını, hızlarını, menzillerini, patlama yarıçaplarını ve etkilerini tanımla
missiles = [
    {"Name": "Patriot-1", "Deviation Angle": 3, "Speed": 1200, "Range": 100, "Blast Radius": 10, "Effect": 50},
    {"Name": "Tomahawk-2", "Deviation Angle": 5, "Speed": 900, "Range": 150, "Blast Radius": 15, "Effect": 80},
    {"Name": "Scud-3", "Deviation Angle": 2, "Speed": 1500, "Range": 200, "Blast Radius": 20, "Effect": 40},
    {"Name": "Spear-4", "Deviation Angle": 4, "Speed": 1000, "Range": 250, "Blast Radius": 25, "Effect": 70},
    {"Name": "Trident-5", "Deviation Angle": 6, "Speed": 1100, "Range": 300, "Blast Radius": 30, "Effect": 60},
    {"Name": "Hellfire-6", "Deviation Angle": 3.5, "Speed": 1300, "Range": 350, "Blast Radius": 35, "Effect": 55},
    {"Name": "Harpoon-7", "Deviation Angle": 4.5, "Speed": 950, "Range": 400, "Blast Radius": 40, "Effect": 75},
    {"Name": "Maverick-8", "Deviation Angle": 2.5, "Speed": 1400, "Range": 450, "Blast Radius": 45, "Effect": 45},
    {"Name": "Exocet-9", "Deviation Angle": 5.5, "Speed": 850, "Range": 500, "Blast Radius": 50, "Effect": 85},
    {"Name": "Javelin-10", "Deviation Angle": 3.8, "Speed": 1250, "Range": 550, "Blast Radius": 55, "Effect": 65},
]

total_damage = 0

for missile in missiles:
    # Füzelerin fırlatıldığı araçları ve zamanları kullanıcıdan al
    launch_vehicle = input(f"{missile['Name']} füzesinin fırlatıldığı aracı girin: ")
    launch_time = input(f"{missile['Name']} füzesinin hangi zamanda fırlatıldığını girin: ")

    # Füzelerin düşeceği konumu hesapla
    if launch_vehicle == "Gazze Şeridi":
        target_population = gaza_population + refah_population + han_yunus_population
        target_distance = random.randint(0, 100) # Gazze Şeridi'nin İsrail sınırına olan uzaklığı
    elif launch_vehicle == "İsrail Sınırı":
        target_population = sderot_population + ashkelon_population + beersheba_population
        target_distance = random.randint(0, 50) # İsrail sınırının Gazze Şeridi'ne olan uzaklığı

    deviation_distance = (missile["Speed"] * missile["Deviation Angle"]) / 1000 # Füzenin sapma mesafesi
    impact_distance = target_distance + deviation_distance # Füzenin düştüğü mesafe
    impact_range = abs(impact_distance - missile["Range"]) # Füzenin menzilinden sapma miktarı

    # Füzelerin düştüğü bölgedeki nüfusu belirle
    if impact_range <= missile["Blast Radius"]:
        affected_population = target_population # Füze tam isabet ettiyse, hedeflenen bölgedeki tüm nüfus etkilendi
    else:
        affected_population = target_population * (missile["Blast Radius"] / impact_range) # Füze isabet etmediyse, hedeflenen bölgedeki nüfusun bir kısmı etkilendi

    # Füzelerin etkilerini de dikkate alarak, saldırı sonucunda tahmini can kaybını hesapla
    damage = (missile["Speed"] * missile["Deviation Angle"] * missile["Effect"] * affected_population) / 100000
    total_damage += damage

    # Sonuçları ekrana yazdır
    print(f"{missile['Name']} füzesi {launch_vehicle} tarafından saat {launch_time} fırlatıldı.")
    print(f"Hedeflenen bölgedeki tahmini nüfus: {target_population}")
    print(f"Füzenin düştüğü mesafe: {impact_distance} km")
    print(f"Füzenin menzilinden sapma miktarı: {impact_range} km")
    print(f"Füzenin etkilediği tahmini nüfus: {affected_population}")
    print(f"Bu saldırı sonucunda tahmini can kaybı: {damage}\n")

# Toplam sonuçları ekrana yazdır
print(f"Toplam tahmini can kaybı: {total_damage}")
print(f"Toplam nüfus: {total_population}")
print(f"Yüzdeye göre tahmini can kaybı: {total_damage / total_population * 100}%")
