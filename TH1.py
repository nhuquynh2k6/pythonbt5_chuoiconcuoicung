#Cau 1
a=5
print("Gia tri cua a la: ",a)
print(f"Gia tri cua a la: {a}")
print("Gia tri cua a la: {}".format(a))
a=1+3j;
print(a)
#Cau 2
a=float(input("Nhap gia tri cua a (a khac 0): "))
b=float(input("Nhap gia tri cua b: "))
x=-b/a
print(x)
#Cau 3
import math
r=float(input("Nhap ban kinh r: "))
if r<=0:
    print("Ban kinh phai la mot so duong")
cv=2*math.pi*r
print(f"Chu vi: {cv}")
dt=math.pi*r*r
print(f"Dien tich: {dt}")
#Cau 4
a=float(input("Nhap so nguyen a: "))
if a%2==0:
    print(f"{a} la so chan")
else:
    print(f"{a} la so le")
#Cau 5
a=float(input("Nhap so nguyen a: "))
b=float(input("Nhap so nguyen b: "))
cong=a+b
print("a+b=",cong)
tru=a-b
print("a-b=",tru)
nhan=a*b
print("axb=",nhan)
chia=a/b
print("a/b=",chia)
#Cau 6
ten=input("Nhap vao ten cua ban: ")
print("Xin chao "+ten)
dem_chu_cai={}
for chu in ten:
    if chu !=" ":
        dem_chu_cai[chu]=dem_chu_cai.get(chu,0)+1
for chu,sl in dem_chu_cai.items():
    print(f"Chu '{chu}' xuat hien {sl} lan")
#Cau 7
import math
a=float(input("Nhap so nguyen a: "))
b=float(input("Nhap so nguyen b: "))
c=float(input("Nhap so nguyen c: "))
delta=b*b-4*a*c
if a==0:
    print("Khong the tinh")
else:
     if delta<0:
        print("Phuong trinh vo nghiem")
     elif delta==0:
        print(f"Phuong trinh co nghiem kep x1=x2={-b/(2*a)}")
     else:
        print(f"Phuong trinh co 2 nghiem phan biet x1={-b+math.sqrt(delta)/(2*a)}, x2={-b-math.sqrt(delta)/(2*a)}")
#Cau 8
s = input("Nhap vao chuoi bat ki: ")
def sap_xep_chuoi(s):
    chu_thuong = ''.join([c for c in s if c.islower()])
    chu_hoa = ''.join([c for c in s if c.isupper()])
    return chu_thuong + chu_hoa
print(sap_xep_chuoi(s))
#Cau 9
chuoi=input("Nhap noi dung chuoi: ")
chuoi_moi=chuoi.title()
print("Ket qua: ",chuoi_moi)
#Cau 10
i=int(input("Nhap vi tri i (bat dau tu 0): "))
s=input("Nhap vao mot chuoi: ")
s_list=list(s)
for index in range(i, len(s_list),3):
    s_list[index]=s_list[index].upper()
result=''.join(s_list)
print("Ket qua: ",result)
#Cau 11
i=int(input("Nhap vi tri i (bat dau tu 0): "))
s=input("Nhap vao mot chuoi: ")
s_list=list(s)
for index in range(len(s_list)):
    if index==i:
        s_list[index]=s_list[index].lower()
else:
    s_list[index]=s_list[index].upper()
    result=''.join(s_list)
print("Ket qua: ",result)
 
  
 

