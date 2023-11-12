import random

# Farklı bölgelerdeki rastgele nüfusları belirleyen fonksiyon
def get_population():
    gaza_population = random.randint(500000, 600000)
    refah_population = random.randint(200000, 250000)
    han_yunus_population = random.randint(150000, 200000)
    sderot_population = random.randint(25000, 30000)
    ashkelon_population = random.randint(140000, 150000)
    beersheba_population = random.randint(200000, 220000)

    total_population = gaza_population + refah_population + han_yunus_population + sderot_population + ashkelon_population + beersheba_population

    return gaza_population, refah_population, han_yunus_population, sderot_population, ashkelon_population, beersheba_population, total_population

# Füzelerin isimlerini, sapma açılarını, hızlarını, menzillerini, patlama yarıçaplarını ve etkilerini tanımlayan fonksiyon
def define_missiles(missile_count, missile_names, missile_angles, missile_speeds, missile_ranges, missile_radii, missile_effects):
    missiles = []
    for i in range(missile_count):
        missile = {
            "Name": missile_names[i],
            "Deviation Angle": missile_angles[i],
            "Speed": missile_speeds[i],
            "Range": missile_ranges[i],
            "Blast Radius": missile_radii[i],
            "Effect": missile_effects[i]
        }
        missiles.append(missile)
    return missiles

# Füzelerin fırlatıldığı araçları ve zamanları kontrol eden ve kullanıcıdan alan fonksiyon
def get_inputs(missile):
    launch_vehicle = input(f"{missile['Name']} füzesinin fırlatıldığı aracı girin: ")
    while launch_vehicle not in ["Gazze Şeridi", "İsrail Sınırı"]:
        print("Lütfen geçerli bir araç girin. Gazze Şeridi veya İsrail Sınırı olmalı.")
        launch_vehicle = input(f"{missile['Name']} füzesinin fırlatıldığı aracı girin: ")
    
    launch_time = input(f"{missile['Name']} füzesinin hangi zamanda fırlatıldığını girin: ")
    while not launch_time.endswith("saat"):
        print("Lütfen geçerli bir zaman girin. Saat cinsinden olmalı. Örneğin: 12:00 saat")
        launch_time = input(f"{missile['Name']} füzesinin hangi zamanda fırlatıldığını girin: ")
    
    return launch_vehicle, launch_time

# Füzelerin düşeceği konumu hesaplayan fonksiyon
def calculate_impact(missile, launch_vehicle, gaza_population, refah_population, han_yunus_population, sderot_population, ashkelon_population, beersheba_population):
    if launch_vehicle == "Gazze Şeridi":
        target_population = gaza_population + refah_population + han_yunus_population
        target_distance = random.randint(0, 100)  # Gazze Şeridi'nin İsrail sınırına olan uzaklığı
    elif launch_vehicle == "İsrail Sınırı":
        target_population = sderot_population + ashkelon_population + beersheba_population
        target_distance = random.randint(0, 50)  # İsrail sınırının Gazze Şeridi'ne olan uzaklığı

    deviation_distance = (missile["Speed"] * missile["Deviation Angle"]) / 1000  # Füzenin sapma mesafesi
    impact_distance = target_distance + deviation_distance  # Füzenin düştüğü mesafe
    impact_range = abs(impact_distance - missile["Range"])  # Füzenin menzilinden sapma miktarı
    
    return target_population, target_distance, deviation_distance, impact_distance, impact_range

# Füzelerin etkilediği nüfusu ve saldırı sonucunda tahmini can kaybını hesaplayan fonksiyon
def calculate_damage(missile, target_population, impact_range):
    if impact_range <= missile["Blast Radius"]:
        affected_population = target_population  # Füze tam isabet ettiyse, hedeflenen bölgedeki tüm nüfus etkilendi
    else:
        affected_population = target_population * (missile["Blast Radius"] / impact_range)  # Füze isabet etmediyse, hedeflenen bölgedeki nüfusun bir kısmı etkilendi

    # Füzelerin etkilerini de dikkate alarak, saldırı sonucunda tahmini can kaybını hesapla
    damage = (missile["Speed"] * missile["Deviation Angle"] * missile["Effect"] * affected_population) / 100000
    return affected_population, damage

# Sonuçları ekrana yazdıran fonksiyon
def print_results(missile, launch_vehicle, launch_time, target_population, target_distance, deviation_distance, impact_distance, impact_range, affected_population, damage):
    print(f"{missile['Name']} füzesi {launch_vehicle} tarafından saat {launch_time} fırlatıldı.")
    print(f"Hedeflenen bölgedeki tahmini nüfus: {target_population}")
    print(f"Füzenin düştüğü mesafe: {impact_distance} km")
    print(f"Füzenin menzilinden sapma miktarı: {impact_range} km")
    print(f"Füzenin etkilediği tahmini nüfus: {affected_population}")
    print(f"Bu saldırı sonucunda tahmini can kaybı: {damage}\n")

# Ana fonksiyon
def simulate_missile_attack():
    # Farklı bölgelerdeki rastgele nüfusları al 
    gaza_population, refah_population, han_yunus_population, sderot_population, ashkelon_population, beersheba_population, total_population = get_population()

    # Füzelerin isimlerini, sapma açılarını, hızlarını, menzillerini, patlama yarıçaplarını ve etkilerini tanımla
    missile_count = 10  # Füze sayısı
    missile_names = ["Patriot-1", "Tomahawk-2", "Scud-3", "Spear-4", "Trident-5", "Hellfire-6", "Harpoon-7", "Maverick-8", "Exocet-9", "Javelin-10"]  # Füze isimleri
    missile_angles = [3, 5, 2, 4, 6, 3.5, 4.5, 2.5, 5.5, 3.8]  # Füze sapma açıları
    missile_speeds = [1200, 900, 1500, 1000, 1100, 1300, 950, 1400, 850, 1250]  # Füze hızları
    missile_ranges = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]  # Füze menzilleri
    missile_radii = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]  # Füze patlama yarıçapları
    missile_effects = [50, 80, 40, 70, 60, 55, 75, 45, 85, 65]  # Füze etkileri
    missiles = define_missiles(missile_count, missile_names, missile_angles, missile_speeds, missile_ranges, missile_radii, missile_effects)

    total_damage = 0

    for missile in missiles:
        # Füzelerin fırlatıldığı araçları ve zamanları al
        launch_vehicle, launch_time = get_inputs(missile)

        # Füzelerin düşeceği konumu hesapla
        target_population, target_distance, deviation_distance, impact_distance, impact_range = calculate_impact(missile, launch_vehicle, gaza_population, refah_population, han_yunus_population, sderot_population, ashkelon_population, beersheba_population)

        # Füzelerin etkilediği nüfusu ve saldırı sonucunda tahmini can kaybını hesapla
        affected_population, damage = calculate_damage(missile, target_population, impact_range)
        total_damage += damage  # Bu satırı ekledim

        # Sonuçları ekrana yazdır
        print_results(missile, launch_vehicle, launch_time, target_population, target_distance, deviation_distance, impact_distance, impact_range, affected_population, damage)  # Bu fonksiyonu çağırdım

    # Toplam sonuçları ekrana yazdır
    print(f"Toplam tahmini can kaybı: {total_damage}")
    print(f"Toplam nüfus: {total_population}")
    print(f"Yüzdeye göre tahmini can kaybı: {total_damage / total_population * 100}%")

# Hava savunma sistemini simüle et
simulate_missile_attack()
