chuoi=input("Nhap chuoi")
digits=[int(ch) for ch in chuoi if ch.isdigit()]
tong=sum(digits)
trung_binh=tong/len(digits) if digits else 0
print(f"Tong la {tong} va trung binh la {trung_binh}")