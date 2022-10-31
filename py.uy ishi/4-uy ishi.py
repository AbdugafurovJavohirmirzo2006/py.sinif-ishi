isimlar = ['Dilshod', 'Anvr', 'Sardor', 'Dilmurod', 'Bobojon','Husan']

print(f'Salom {isimlar[0]}, {isimlar[1]}, {isimlar[2]}, {isimlar[3]}, {isimlar[4]}, {isimlar[5]} dostlarim ishlaring yahshimi?')

# ...............................................................................

sonlar = [11, 27, 648, 749, 7584, 657_688_678, 17.]

sonlar[0] = sonlar[0] + sonlar[-1]
sonlar[1] = -99.7
sonlar[4] = sonlar[4] + 89
del sonlar[5]
del sonlar[0]
print(sonlar)
print(sonlar[2])

# ...............................................................................

t_shaxslar = ["Vanderbit", "Jeypi Morgan", "Napalion"]

z_shaxslar = ["Bill Gets", "Del karnegi", "Stif Jobs"]


print(f"""Men tarixiy shaxslardan {t_shaxslar.pop(0).title()} bilan
zamonaviy shaxslardan esa {z_shaxslar.pop(1).title()} bilan
suhbat qurishni va ular bilan ishlashni juda istardim""")

# ...............................................................................

friends = []
friends.append("Jamshid")
friends.append("Sardor")
friends.append("Axmat")
friends.append("Ali")
friends.append("Eshon")
friends.append("Abdulazis")
print(f"To'liq list-{friends}")

friends.remove("Jamshid")
friends.remove("Sardor")
friends.remove("Axmat")
print(f"Kelganlar-{friends}")

friends.append("Hasan")
friends.insert(0, "Husan")
friends.insert(2, "Ivan")
print(friends)

mehmonlar = ["Alisher","Anvar","Jamshid","Dilshod"]
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)






