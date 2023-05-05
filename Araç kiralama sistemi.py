import mysql.connector as SQLC

DataBase = SQLC.connect(
host="127.0.0.1",
user="root",
password="1234"
)
# Cursor to the database
Cursor = DataBase.cursor()

Cursor.execute("CREATE DATABASE `90210000202`")
print("90210000202 adlı veritabanı yaratıldı")

import mysql.connector
dataBase = mysql.connector.connect(
host="127.0.0.1",
user="root",
passwd="1234",
database="90210000202")
cursorObject = dataBase.cursor()
kullanıcıRecord = """CREATE TABLE admin (
ad VARCHAR(20) ,
soyad VARCHAR(20),
tc VARCHAR(20) ,
doğum_yılı VARCHAR(20)  ,
adres VARCHAR(20),
telefon DECIMAL(20) ,
meslek VARCHAR(20),
ehliyet_sınıfı VARCHAR(4),
medeni_durumu VARCHAR(10),
eğitim_durumu VARCHAR(20)
)"""
araçRecord = """CREATE TABLE car_info (
araç_türü VARCHAR(25) ,
marka VARCHAR(25),
model VARCHAR(25),
üretim_yılı VARCHAR(25) ,
yakıt_türü VARCHAR(25),
vites VARCHAR(25),
motor_gücü VARCHAR(25),
kasa_tipi VARCHAR(25),
motor_hacmi VARCHAR(25),
çekiş VARCHAR(25),
kapı VARCHAR(25),
renk VARCHAR(25),
motor_no VARCHAR(25),
şase_no VARCHAR(25),
günlük_kiralama_bedeli VARCHAR(25)
)"""
kiralamaRecord = """CREATE TABLE rental_info (
ad VARCHAR(25),
model VARCHAR(25),
kaç_gün VARCHAR(25),
nereye VARCHAR(25)
)"""
listeRecord = """CREATE TABLE rental_list (
ad VARCHAR(25),
model VARCHAR(25),
kaç_gün VARCHAR(25)
)"""
cursorObject.execute(kullanıcıRecord)
cursorObject.execute(araçRecord)
cursorObject.execute(kiralamaRecord)
cursorObject.execute(listeRecord)
dataBase.close()

import mysql.connector

con=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="90210000202")

mycursor = con.cursor()

sql = "INSERT INTO car_info (araç_türü, marka, model, üretim_yılı, yakıt_türü, vites, motor_gücü, kasa_tipi, motor_hacmi, çekiş, kapı, renk, motor_no, şase_no, günlük_kiralama_bedeli) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = ("otomobil", "BMW", "520i", "2018", "benzin", "otomatik", "170 hp", "sedan", "1597 cc", "arka", "4", "siyah", "35HLK29080", "7HBYI57GRTJG279549", "1000")

sql1 = "INSERT INTO car_info  (araç_türü, marka, model, üretim_yılı, yakıt_türü, vites, motor_gücü, kasa_tipi, motor_hacmi, çekiş, kapı, renk, motor_no, şase_no, günlük_kiralama_bedeli) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val1 = ("otomobil", "Renault", "megane", "2017", "dizel", "yarı oto", "110 hp", "sedan", "1461 cc", "ön", "4", "beyaz", "29IRC67924", "1WONT68GOKH297364", "700")

sql2 = "INSERT INTO car_info  (araç_türü, marka, model, üretim_yılı, yakıt_türü, vites, motor_gücü, kasa_tipi, motor_hacmi, çekiş, kapı, renk, motor_no, şase_no, günlük_kiralama_bedeli) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val2 = ("otomobil", "Opel", "Corsa", "2006", "dizel", "manuel", "70 hp", "Hatchback", "1248 cc", "ön", "2", "kırmızı", "68MBY60975", "4BYRD20LEBA960482", "400")

sql3 = "INSERT INTO car_info  (araç_türü, marka, model, üretim_yılı, yakıt_türü, vites, motor_gücü, kasa_tipi, motor_hacmi, çekiş, kapı, renk, motor_no, şase_no, günlük_kiralama_bedeli) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val3 = ("otomobil", "Ford", "Focus", "2014", "dizel", "manuel", "115 hp", "Sedan", "1560 cc", "ön", "4", "beyaz", "52WVC10338", "1HGBH41JXMN109186", "600")


mycursor.execute(sql, val)
mycursor.execute(sql1, val1)
mycursor.execute(sql2, val2)
mycursor.execute(sql3, val3)
con.commit()
print(mycursor.rowcount, "Ayrıntılar eklendi")
con.close()

from tkinter import *
import mysql.connector
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
con=mysql.connector.connect(host="127.0.0.1",user="root",password="1234",database="90210000202")

    


window=tk.Tk()
window.title("Araç Kiralama Sistemi")
window.geometry("600x400")




ent1=StringVar()
ent2=StringVar()
ent3=IntVar() 
ent4=IntVar() 
ent5=StringVar()
ent6=StringVar()
ent7=StringVar()
ent8=StringVar()
ent9=StringVar()
ent10=StringVar()
ent11=StringVar()
ent12=StringVar()
ent13=IntVar()
ent14=StringVar()
ent15=StringVar()
ent16=StringVar()
ent17=StringVar()
car1=StringVar()
car2=StringVar()
car3=StringVar()    
car4=IntVar()  
car5=StringVar()
car6=StringVar()
car7=StringVar()
car8=StringVar()    
car9=StringVar()  
car10=StringVar()
car11=IntVar()
car12=StringVar()
car13=StringVar()    
car14=StringVar()  
car15=IntVar()


def customer_info():
 customer_screen = tk.Toplevel(window)
 customer_screen.title("Müşteri Bilgileri Giriş")
 customer_screen.geometry("600x400")   

 


 
    
 ad = tk.Label(customer_screen, text="Ad:").place(x=50,y=50)
 ad = Entry(customer_screen,textvariable=ent1).place(x=150,y=50)
 soyad= tk.Label(customer_screen, text="Soyad:").place(x=50,y=80)
 soyad = Entry(customer_screen,textvariable=ent2).place(x=150,y=80)
 tc= tk.Label(customer_screen, text="TC Kimlik No:").place(x=50,y=110)
 tc = Entry(customer_screen,textvariable=ent3).place(x=150,y=110)
 doğum_yılı= tk.Label(customer_screen, text="Doğum Yılı:").place(x=50,y=140)
 doğum_yılı = Entry(customer_screen,textvariable=ent4).place(x=150,y=140)
 adres= tk.Label(customer_screen, text="Adres:").place(x=50,y=170)
 adres = Entry(customer_screen,textvariable=ent5).place(x=150,y=170)
 telefon= tk.Label(customer_screen, text="Telefon:").place(x=50,y=200)
 telefon = Entry(customer_screen,textvariable=ent6).place(x=150,y=200)
 meslek= tk.Label(customer_screen, text="Meslek:").place(x=50,y=230)
 meslek = Entry(customer_screen,textvariable=ent7).place(x=150,y=230)
 ehliyet_sınıfı= tk.Label(customer_screen, text="Ehliyet Sınıfı:").place(x=50,y=260)
 ehliyet_sınıfı = Entry(customer_screen,textvariable=ent8).place(x=150,y=260)
 medeni_durumu= tk.Label(customer_screen, text="Medeni Durum:").place(x=50,y=290)
 medeni_durumu = Entry(customer_screen,textvariable=ent9).place(x=150,y=290)
 eğitim_durumu= tk.Label(customer_screen, text="Eğitim Durumu:").place(x=50,y=320)
 eğitim_durumu = Entry(customer_screen,textvariable=ent10).place(x=150,y=320)
 

 def giriş():
    
    e1=ent1.get()
    e2=ent2.get()
    e3=ent3.get()
    e4=ent4.get()
    e5=ent5.get()
    e6=ent6.get()
    e7=ent7.get()
    e8=ent8.get()
    e9=ent9.get()
    e10=ent10.get()
    cur=con.cursor()
    x='y'
    cur.execute("INSERT INTO admin(ad,soyad,tc,doğum_yılı,adres,telefon,meslek,ehliyet_sınıfı,medeni_durumu,eğitim_durumu) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10))
    con.commit()

    messagebox.showinfo('bilgi',"kullanıcı eklendi")
 
 giriş_button= tk.Button(customer_screen, text="KAYIT",bg="orange", height="2", width="10",command=giriş).place(x=400,y=150)
 def silme():
    
    e1=ent1.get()
    e2=ent2.get()
    e3=ent3.get()
    e4=ent4.get()
    e5=ent5.get()
    e6=ent6.get()
    e7=ent7.get()
    e8=ent8.get()
    e9=ent9.get()
    e10=ent10.get()
    cur=con.cursor()
    x='y'
    cur.execute("delete from admin where ad=%s and telefon=%s",(e1,e6))
    con.commit()

    messagebox.showinfo('bilgi',"kullanıcı silidi")
 silme_button= tk.Button(customer_screen, text="SİL",bg="orange", height="2", width="10",command=silme).place(x=400,y=220)  
 
def car_info():
 car_screen = tk.Toplevel(window)
 car_screen.title("Araç Bilgileri Giriş")
 car_screen.geometry("1200x1000")
 
 
 notebook=ttk.Notebook(car_screen)
 notebook.pack()    
 frame2=Frame(notebook,width=100,height=100)  
 frame2.pack(fill="both",expand=1)
 labf=Label(frame2,text="ARABALAR",bg="grey", width=300, height=2, font=("Calibri", 13)).pack()
 treescroll=Frame(frame2)
 treescroll.pack()
 scroll=Scrollbar(frame2)
 scroll.pack(side=RIGHT,fill=Y)
 tree=ttk.Treeview(frame2,yscrollcommand=scroll.set) 
 scroll.config(command=tree.yview)
 tree['show']='headings'
 s=ttk.Style(car_screen)
 s.theme_use("clam")
 tree.pack() 
 tree['columns']=("araç_türü", "marka", "model", "üretim_yılı", "yakıt_türü", "vites", "motor_gücü", "kasa_tipi", "motor_hacmi", "çekiş", "kapı", "renk", "motor_no", "şase_no", "günlük_kiralama_bedeli") 
 cur=con.cursor()
 y='y'
 cur.execute("select araç_türü, marka, model, üretim_yılı, yakıt_türü, vites, motor_gücü, kasa_tipi, motor_hacmi, çekiş, kapı, renk, motor_no, şase_no, günlük_kiralama_bedeli from car_info ")


 tree.column("araç_türü",width=70,minwidth=70,anchor=CENTER)
 tree.column("marka",width=70,minwidth=70,anchor=CENTER)
 tree.column("model",width=70,minwidth=70,anchor=CENTER)
 tree.column("üretim_yılı",width=70,minwidth=70,anchor=CENTER)
 tree.column("yakıt_türü",width=70,minwidth=70,anchor=CENTER)
 tree.column("vites",width=70,minwidth=70,anchor=CENTER)
 tree.column("motor_gücü",width=70,minwidth=70,anchor=CENTER)
 tree.column("kasa_tipi",width=70,minwidth=70,anchor=CENTER)
 tree.column("motor_hacmi",width=70,minwidth=70,anchor=CENTER)
 tree.column("çekiş",width=70,minwidth=70,anchor=CENTER)
 tree.column("kapı",width=70,minwidth=70,anchor=CENTER)
 tree.column("renk",width=70,minwidth=70,anchor=CENTER)
 tree.column("motor_no",width=70,minwidth=70,anchor=CENTER)
 tree.column("şase_no",width=70,minwidth=70,anchor=CENTER)
 tree.column("günlük_kiralama_bedeli",width=70,minwidth=70,anchor=CENTER)

 tree.heading("araç_türü",text="araç_türü",anchor=CENTER)
 tree.heading("marka",text="marka",anchor=CENTER)
 tree.heading("model",text="model",anchor=CENTER)
 tree.heading("üretim_yılı",text="üretim_yılı",anchor=CENTER)
 tree.heading("yakıt_türü",text="yakıt_türü",anchor=CENTER)
 tree.heading("vites",text="vites",anchor=CENTER)
 tree.heading("motor_gücü",text="motor_gücü",anchor=CENTER)
 tree.heading("kasa_tipi",text="kasa_tipi",anchor=CENTER)
 tree.heading("motor_hacmi",text="motor_hacmi",anchor=CENTER)
 tree.heading("çekiş",text="çekiş",anchor=CENTER)
 tree.heading("kapı",text="kapı",anchor=CENTER)
 tree.heading("renk",text="renk",anchor=CENTER)
 tree.heading("motor_no",text="motor_no",anchor=CENTER)
 tree.heading("şase_no",text="şase_no",anchor=CENTER)
 tree.heading("günlük_kiralama_bedeli",text="günlük_kiralama_bedeli",anchor=CENTER)

 i=0
 for row in cur:
        tree.insert('',i,text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        i+=1
 con.commit()

 araç_türü = tk.Label(car_screen, text="araç türü:").place(x=50,y=300)
 araç_türü = Entry(car_screen,textvariable=car1).place(x=110,y=300)
 marka= tk.Label(car_screen, text="marka:").place(x=250,y=300)
 marka = Entry(car_screen,textvariable=car2).place(x=300,y=300)
 model= tk.Label(car_screen, text="model:").place(x=440,y=300)
 model = Entry(car_screen,textvariable=car3).place(x=490,y=300)
 üretim_yılı= tk.Label(car_screen, text="üretim yılı:").place(x=630,y=300)
 üretim_yılı = Entry(car_screen,textvariable=car4).place(x=710,y=300)
 yakıt_türü= tk.Label(car_screen, text="yakıt türü:").place(x=850,y=300)
 yakıt_türü = Entry(car_screen,textvariable=car5).place(x=920,y=300)
 vites= tk.Label(car_screen, text="vites:").place(x=1060,y=300)
 vites = Entry(car_screen,textvariable=car6).place(x=1110,y=300)
 motor_gücü= tk.Label(car_screen, text="motor gücü:").place(x=40,y=350)
 motor_gücü = Entry(car_screen,textvariable=car7).place(x=110,y=350)
 kasa_tipi= tk.Label(car_screen, text="kasa tipi:").place(x=250,y=350)
 kasa_tipi = Entry(car_screen,textvariable=car8).place(x=300,y=350)
 motor_hacmi= tk.Label(car_screen, text="motor hacmi:").place(x=440,y=350)
 motor_hacmi = Entry(car_screen,textvariable=car9).place(x=520,y=350)
 çekiş= tk.Label(car_screen, text="çekiş:").place(x=660,y=350)
 çekiş = Entry(car_screen,textvariable=car10).place(x=710,y=350)
 kapı= tk.Label(car_screen, text="kapı:").place(x=850,y=350)
 kapı = Entry(car_screen,textvariable=car11).place(x=920,y=350)
 renk= tk.Label(car_screen, text="renk:").place(x=1060,y=350)
 renk = Entry(car_screen,textvariable=car12).place(x=1110,y=350)
 motor_no= tk.Label(car_screen, text="motor no:").place(x=50,y=400)
 motor_no = Entry(car_screen,textvariable=car13).place(x=110,y=400)
 şase_no= tk.Label(car_screen, text="şase no:").place(x=250,y=400)
 şase_no = Entry(car_screen,textvariable=car14).place(x=300,y=400)
 günlük_kiralama_bedeli= tk.Label(car_screen, text="günlük kiralama bedeli:").place(x=440,y=400)
 günlük_kiralama_bedeli = Entry(car_screen,textvariable=car15).place(x=570,y=400)
 
 def ekle():
    
    c1=car1.get()
    c2=car2.get()
    c3=car3.get()
    c4=car4.get()
    c5=car5.get()
    c6=car6.get()
    c7=car7.get()
    c8=car8.get()
    c9=car9.get()
    c10=car10.get()
    c11=car11.get()
    c12=car12.get()
    c13=car13.get()
    c14=car14.get()
    c15=car15.get()
    cur=con.cursor()
    x='y'
    cur.execute("INSERT INTO car_info (araç_türü, marka, model, üretim_yılı, yakıt_türü, vites, motor_gücü, kasa_tipi, motor_hacmi, çekiş, kapı, renk, motor_no, şase_no, günlük_kiralama_bedeli) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15))
    con.commit()
    messagebox.showinfo('bilgi',"araç eklendi")
 giriş_button= tk.Button(car_screen, text="EKLE",bg="orange", height="2", width="10",command=ekle).place(x=600,y=450)

 def sil():
    
    c1=car1.get()
    c2=car2.get()
    c3=car3.get()
    c4=car4.get()
    c5=car5.get()
    c6=car6.get()
    c7=car7.get()
    c8=car8.get()
    c9=car9.get()
    c10=car10.get()
    c11=car11.get()
    c12=car12.get()
    c13=car13.get()
    c14=car14.get()
    c15=car15.get()
    cur=con.cursor()
    cur=con.cursor()
    x='y'
    cur.execute("delete from car_info where marka=%s and model=%s",(c2,c3))
    con.commit()

    messagebox.showinfo('bilgi',"araç silidi")
 silme_button= tk.Button(car_screen, text="SİL",bg="orange", height="2", width="10",command=sil).place(x=700,y=450)  
 
 
 



def rental_info():
 rental_screen = tk.Toplevel(window)
 rental_screen.title("Araç Kiralama Bilgileri Giriş")
 rental_screen.geometry("1200x1000")

 notebook=ttk.Notebook(rental_screen)
 notebook.pack()    
 frame2=Frame(notebook,width=100,height=100)  
 frame2.pack(fill="both",expand=1)
 labf=Label(frame2,text="ARABALAR",bg="grey", width=300, height=1, font=("Calibri", 13)).pack()
 treescroll=Frame(frame2)
 treescroll.pack()
 scroll=Scrollbar(frame2)
 scroll.pack(side=RIGHT,fill=Y)
 tree=ttk.Treeview(frame2,yscrollcommand=scroll.set) 
 scroll.config(command=tree.yview)
 tree['show']='headings'
 s=ttk.Style(rental_screen)
 s.theme_use("clam")
 tree.pack() 
 tree['columns']=("araç_türü", "marka", "model", "üretim_yılı", "yakıt_türü", "vites", "motor_gücü", "kasa_tipi", "motor_hacmi", "çekiş", "kapı", "renk", "motor_no", "şase_no", "günlük_kiralama_bedeli") 
 cur=con.cursor()
 y='y'
 cur.execute("select araç_türü, marka, model, üretim_yılı, yakıt_türü, vites, motor_gücü, kasa_tipi, motor_hacmi, çekiş, kapı, renk, motor_no, şase_no, günlük_kiralama_bedeli from car_info ")


 tree.column("araç_türü",width=70,minwidth=70,anchor=CENTER)
 tree.column("marka",width=70,minwidth=70,anchor=CENTER)
 tree.column("model",width=70,minwidth=70,anchor=CENTER)
 tree.column("üretim_yılı",width=70,minwidth=70,anchor=CENTER)
 tree.column("yakıt_türü",width=70,minwidth=70,anchor=CENTER)
 tree.column("vites",width=70,minwidth=70,anchor=CENTER)
 tree.column("motor_gücü",width=70,minwidth=70,anchor=CENTER)
 tree.column("kasa_tipi",width=70,minwidth=70,anchor=CENTER)
 tree.column("motor_hacmi",width=70,minwidth=70,anchor=CENTER)
 tree.column("çekiş",width=70,minwidth=70,anchor=CENTER)
 tree.column("kapı",width=70,minwidth=70,anchor=CENTER)
 tree.column("renk",width=70,minwidth=70,anchor=CENTER)
 tree.column("motor_no",width=70,minwidth=70,anchor=CENTER)
 tree.column("şase_no",width=70,minwidth=70,anchor=CENTER)
 tree.column("günlük_kiralama_bedeli",width=70,minwidth=70,anchor=CENTER)

 tree.heading("araç_türü",text="araç_türü",anchor=CENTER)
 tree.heading("marka",text="marka",anchor=CENTER)
 tree.heading("model",text="model",anchor=CENTER)
 tree.heading("üretim_yılı",text="üretim_yılı",anchor=CENTER)
 tree.heading("yakıt_türü",text="yakıt_türü",anchor=CENTER)
 tree.heading("vites",text="vites",anchor=CENTER)
 tree.heading("motor_gücü",text="motor_gücü",anchor=CENTER)
 tree.heading("kasa_tipi",text="kasa_tipi",anchor=CENTER)
 tree.heading("motor_hacmi",text="motor_hacmi",anchor=CENTER)
 tree.heading("çekiş",text="çekiş",anchor=CENTER)
 tree.heading("kapı",text="kapı",anchor=CENTER)
 tree.heading("renk",text="renk",anchor=CENTER)
 tree.heading("motor_no",text="motor_no",anchor=CENTER)
 tree.heading("şase_no",text="şase_no",anchor=CENTER)
 tree.heading("günlük_kiralama_bedeli",text="günlük_kiralama_bedeli",anchor=CENTER)

 i=0
 for row in cur:
        tree.insert('',i,text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        i+=1
 con.commit()

 notebook=ttk.Notebook(rental_screen)
 notebook.pack()    
 frame2=Frame(notebook,width=100,height=100)  
 frame2.pack(fill="both",expand=1)
 labf=Label(frame2,text="KULLANICILAR",bg="grey", width=300, height=1, font=("Calibri", 13)).pack()
 treescroll=Frame(frame2)
 treescroll.pack()
 scroll=Scrollbar(frame2)
 scroll.pack(side=RIGHT,fill=Y)
 tree=ttk.Treeview(frame2,yscrollcommand=scroll.set) 
 scroll.config(command=tree.yview)
 tree['show']='headings'
 s=ttk.Style(rental_screen)
 s.theme_use("clam")
 tree.pack() 
 tree['columns']=("ad","soyad","tc","doğum_yılı","adres","telefon","meslek","ehliyet_sınıfı","medeni_durumu","eğitim_durumu") 
 cur=con.cursor()
 y='y'
 cur.execute("select ad,soyad,tc,doğum_yılı,adres,telefon,meslek,ehliyet_sınıfı,medeni_durumu,eğitim_durumu from admin ")


 tree.column("ad",width=70,minwidth=70,anchor=CENTER)
 tree.column("soyad",width=70,minwidth=70,anchor=CENTER)
 tree.column("tc",width=70,minwidth=70,anchor=CENTER)
 tree.column("doğum_yılı",width=70,minwidth=70,anchor=CENTER)
 tree.column("adres",width=70,minwidth=70,anchor=CENTER)
 tree.column("telefon",width=70,minwidth=70,anchor=CENTER)
 tree.column("meslek",width=70,minwidth=70,anchor=CENTER)
 tree.column("ehliyet_sınıfı",width=70,minwidth=70,anchor=CENTER)
 tree.column("medeni_durumu",width=70,minwidth=70,anchor=CENTER)
 tree.column("eğitim_durumu",width=70,minwidth=70,anchor=CENTER)

 tree.heading("ad",text="ad",anchor=CENTER)
 tree.heading("soyad",text="soyad",anchor=CENTER)
 tree.heading("tc",text="tc",anchor=CENTER)
 tree.heading("doğum_yılı",text="doğum_yılı",anchor=CENTER)
 tree.heading("adres",text="adres",anchor=CENTER)
 tree.heading("telefon",text="telefon",anchor=CENTER)
 tree.heading("meslek",text="meslek",anchor=CENTER)
 tree.heading("ehliyet_sınıfı",text="ehliyet_sınıfı",anchor=CENTER)
 tree.heading("medeni_durumu",text="medeni_durumu",anchor=CENTER)
 tree.heading("eğitim_durumu",text="eğitim_durumu",anchor=CENTER)


 i=0
 for row in cur:
        tree.insert('',i,text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
        i+=1
 con.commit()

 lab4=Label(rental_screen,text="AD:").place(x=200,y=550)
 carbook=Entry(rental_screen,textvariable=ent11).place(x=240,y=550)

 lab5=Label(rental_screen,text="MODEL:").place(x=400,y=550)
 carname=Entry(rental_screen,textvariable=ent12).place(x=460,y=550)

 lab6=Label(rental_screen,text="KAÇ GÜN:").place(x=600,y=550)
 carmail=Entry(rental_screen,textvariable=ent13).place(x=660,y=550)

 lab7=Label(rental_screen,text="NEREYE:").place(x=800,y=550)
 cardate=Entry(rental_screen,textvariable=ent14).place(x=860,y=550)

 def listele():
        a=ent11.get()
        b=ent12.get()
        c=ent13.get()
        d=ent14.get()
        cur=con.cursor()
        cur.execute("insert into rental_list (ad,model,kaç_gün) values(%s,%s,%s)",(a,b,c))
        con.commit()
        cur=con.cursor()
        n='n'
        cur.execute("insert into rental_info (ad,model,kaç_gün,nereye) values(%s,%s,%s,%s)",(a,b,c,d))
        con.commit()
        messagebox.showinfo('bilgi',"bilgiler ekledi")

 liste_button=tk.Button(rental_screen,text="LİSTELE",bg="orange",command=listele).place(x=600,y=600)       
 

def rental_list():
 rental_list = tk.Toplevel(window)
 rental_list.title("Kirada Olan Araçları Listele")
 rental_list.geometry("800x500")


 lab=tk.Label(rental_list,text="KİRADA OLANLAR",bg="grey", width=300, height=1, font=("Calibri", 13)).pack()
 notebook=ttk.Notebook(rental_list)
 notebook.pack()    
 
 frame2=Frame(notebook,width=100,height=100)  
 frame2.pack(fill="both",expand=1)
 treescroll=Frame(frame2)
 treescroll.pack()
 scroll=Scrollbar(frame2)
 scroll.pack(side=RIGHT,fill=Y)
 tree1=ttk.Treeview(frame2,yscrollcommand=scroll.set) 
 scroll.config(command=tree1.yview)
 tree1['show']='headings'
 s=ttk.Style(rental_list)
 s.theme_use("clam")
 tree1.pack() 
 tree1["columns"]=("ad","model","kaç_gün")
 cur=con.cursor()
 y='y'
 cur.execute("select ad,model,kaç_gün from rental_list ")

 tree1.column("ad",width=70,minwidth=70,anchor=CENTER)
 tree1.column("model",width=70,minwidth=70,anchor=CENTER)
 tree1.column("kaç_gün",width=150,minwidth=150,anchor=CENTER)
 

 tree1.heading("ad",text="ad",anchor=CENTER)
 tree1.heading("model",text="model",anchor=CENTER)
 tree1.heading("kaç_gün",text="kaç_gün",anchor=CENTER)
 
 i=0
 for row in cur:
     tree1.insert('',i,text='',values=(row[0],row[1],row[2]))
     i+=1
 con.commit()
 
 lab15=Label(rental_list,text="AD").place(x=200,y=300)
 carbook=Entry(rental_list,textvariable=ent15).place(x=240,y=300)

 lab16=Label(rental_list,text="MODEL").place(x=400,y=300)
 carname=Entry(rental_list,textvariable=ent16).place(x=460,y=300)


 def geri_teslim ():
    
    e15=ent15.get()
    e16=ent16.get()
    cur=con.cursor()
    x='y'
    cur.execute("delete from rental_list where ad=%s and model=%s",(e15,e16))
    con.commit()

    messagebox.showinfo('bilgi',"bilgiler silidi")
 silme_button= tk.Button(rental_list, text="GERİ TESLİM",bg="orange",command=geri_teslim).place(x=350,y=350)
 
    







Label(text="Araç Kiralama Sistemi", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
button=tk.Button(text="Müşteri Bilgileri Giriş",bg="orange", height="3", width="30", command = customer_info)
button.pack()
button=tk.Button(text="Araç Bilgileri Giriş",bg="orange", height="3", width="30", command = car_info)
button.pack()
button=tk.Button(text="Araç Kiralama Bilgileri Giriş",bg="orange", height="3", width="30", command = rental_info)
button.pack()
button=tk.Button(text="Kirada Olan Araçları Listele",bg="orange", height="3", width="30", command = rental_list)
button.pack()






window.mainloop()