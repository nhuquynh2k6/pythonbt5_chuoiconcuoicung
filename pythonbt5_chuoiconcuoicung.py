text="Emma la mot nha phan tich du lieu, nguoi biet ve ngon ngu Python. Hien Emma dang lam tai Google"
last_index=text.rfind("Emma")
if last_index!=-1:
    print(f"Chuoi con 'Emma' duoc tim thay cuoi cung bat dau tai vi tri thu {last_index}")
else:
    print(f"Chuoi con 'Emma' khong duoc tim thay trong chuoi")