from datetime import datetime

def runMenu1():
    subMenu = input("""
========== Sub Menu Tambah Data Karyawan ========
1. Tambah Data
2. Kembali ke Menu Utama
Silahkan pilih sub Menu Tambah Data [1-2]:""")
    
    while not validasiMenu(subMenu,2):
        print("""Oops! Inputan anda salah,
Mohon masukkan angka/bilangan bulat [1-2]
""") 
        runMenu1()
    if int(subMenu) == 1:
        nama = input("Masukkan Nama:")
        while not validateBlank(nama.strip()):
            print("Inputan Salah!, inputan masih kosong")
            nama = input("Masukkan Nama:")

        phone = input("Masukkan Nomor Telp:")
        while not validasiPhone(phone.strip()):
            phone = input("Masukkan Nomor Telp:")

        gender = input("Masukkan Jenis kelamin (L/P):")
        while not validasiGender(gender.strip()):
            print("Inputan Salah!, mohon masukan huruf L atau P")
            gender = input("Masukkan Jenis kelamin (L/P):")

        jabatan = input("Masukkan Jabatan:")
        while not validateBlank(jabatan.strip()):
            print("Inputan Salah!, inputan masih kosong")
            jabatan = input("Masukkan Jabatan:")

        divisi = input("Masukkan Divisi:")
        while not validateBlank(divisi.strip()):
            print("Inputan Salah!, inputan masih kosong")
            divisi = input("Masukkan Divisi:")

        joinDate = input("Masukkan Tanggal Bergabung (dd-MM-YYYY -> contoh: 31-01-2024):")
        while not validasiDate(joinDate.strip()):
            joinDate = input("Masukkan Tanggal Bergabung (dd-MM-YYYY -> contoh: 31-01-2024):")

        #add new emp to list
        if validasiDuplicateEmp(phone) :
            newEmp = {
                "name" : nama.strip(),
                "phone" : phone.strip(),
                "gender" : gender.strip().upper(),
                "jabatan" : jabatan.strip(),
                "divisi" : divisi.strip(),
                "joinDate" : joinDate.strip()
            } 
            employees.append(newEmp)
            print(f"Data {nama} berhasil disimpan")
            runMenu1()
        else:
            print(f"Maaf, Data karyawan dengan telp {phone} sudah ada!")
            runMenu1()   
    else: 
        pilihMenu()
         
def runMenu2():
    if len(employees) > 0:
        subMenu = input("""
========== Sub Menu Lihat Data Karyawan ========
1. Lihat Semua Data
2. Lihat Data Tertentu
3. Lihat & Urutkan Data
4. Kembali ke Menu Utama
Silahkan pilih sub Menu Lihat Data [1-4]:""")
        
        while not validasiMenu(subMenu,4):
            print("""Oops! Inputan anda salah,
Mohon masukkan angka/bilangan bulat [1-4]
""") 
            runMenu2()
        
        if int(subMenu) == 1:
            printEmployess(employees)
            runMenu2()
        elif int(subMenu) == 2:
            findData()  
        elif int(subMenu) == 3:
            sortData()
        else:
            pilihMenu()   
    else:
        print("""Maaf data karyawan masih kosong!, 
Silahkan tambah data untuk melanjutakn!
""")
        
def runMenu3():
    subMenu = input("""========== Sub Menu Ubah Data Karyawan ========
1. Ubah Data
2. Kembali ke Menu Utama
Silahkan pilih sub Menu Ubah Data [1-2]:""")
    while not validasiMenu(subMenu,2):
        print("""Oops! Inputan anda salah,
Mohon masukkan angka/bilangan bulat [1-2]
""")
        runMenu3()
    
    if int(subMenu) == 1:
        ubahData()
    else:
        pilihMenu()

def runMenu4():
    subMenu = input("""========== Sub Menu Hapus Data Karyawan ========
1. Hapus Data
2. Kembali ke Menu Utama
Silahkan pilih sub Menu Hapus Data [1-2]:""")
    while not validasiMenu(subMenu,2):
        print("""Oops! Inputan anda salah,
Mohon masukkan angka/bilangan bulat [1-2]
""") 
        runMenu4()

    if int(subMenu) == 1:
        printEmployess(employees)
        range = "0" if len(employees) == 1 else f"0-{len(employees)-1}"
        idEmp = input(f"""Masukkan index karyawan yang akan dihapus [{range}]:""")
        while not validasiMenu(idEmp,len(employees)-1,0):
            print(f"""Oops! Inputan anda salah,
Mohon masukkan angka/bilangan bulat [{range}]
""")
            idEmp = input(f"""Masukkan index karyawan yang akan dihapus [{range}]:""")

            
        hapusData(int(idEmp))
    else:
        pilihMenu()

def hapusData(index):
    print("""
================= Konfirmasi Hapus Data =================""")
    dataHapus = []
    dataHapus.append(employees[index])
    printEmployess(dataHapus)
    action = input('Yakin menghapus data? [Y/N]:')
    if action in ['y','n','Y','N']:
        if action in ['y','Y']:
            del employees[index]
            print('Data berhasil dihapus!')
            runMenu4()
        else:
            runMenu4()    
    else:
        print('Inputan salah, Mohon masukkan hanya alfabet Y atau N')
        hapusData(index)        

def ubahData():
    printEmployess(employees)
    range = "0" if len(employees) == 1 else f"0-{len(employees)-1}"
    idEmp = input(f"Masukkan index karyawan yang akan diubah [{range}]:")
    while not validasiMenu(idEmp,len(employees)-1,0):
        print(f"""Oops! Inputan anda salah,
Mohon masukkan angka/bilangan bulat [{range}]
""")
        ubahData()
    
    updateKey = input("""================== Pilih Kolom Ubah ==================
1. Nama Karyawan
2. No. Telp
3. Jenis Kelamin
4. Jabatan
5. Divisi
6. Tgl Bergabung
7. Semua kolom
Masukkan kolom yang ingin diubah, dalam angka [1-7]:""")
    while not validasiMenu(updateKey,7):
        print("""Oops! Inputan anda salah,
Mohon masukkan angka/bilangan bulat [1-7]
""")
        updateKey = input("""================ Pilih Kolom Ubah ================
1. Nama Karyawan
2. No. Telp
3. Jenis Kelamin
4. Jabatan
5. Divisi
6. Tgl Bergabung
7. Semua kolom
Masukkan kolom yang ingin diubah, dalam angka [1-7]:""")
    if int(updateKey) == 1:
        name = input('Masukkan Nama baru:')
        while not validateBlank(name.strip()):
            print("Inputan Salah!, inputan masih kosong")
            name = input("Masukkan Nama baru:")

        employees[int(idEmp)]['name'] = name.strip()
    elif int(updateKey) == 2:
        phone = input('Masukkan No. Telp baru:')
        while not validasiPhone(phone.strip()):
            phone = input("Masukkan Nomor Telp baru:")

        employees[int(idEmp)]['phone'] = phone.strip()
    elif int(updateKey) == 3:
        gender = input('Masukkan Jenis Kelamin baru (L/P):')
        while not validasiGender(gender.strip()):
            print("Inputan Salah!, mohon masukan huruf L atau P")
            gender = input("Masukkan Jenis kelamin baru (L/P):")

        employees[int(idEmp)]['gender'] = gender.strip().upper()
    elif int(updateKey) == 4:
        jabatan = input('Masukkan Jabatan baru:')
        while not validateBlank(jabatan.strip()):
            print("Inputan Salah!, inputan masih kosong")
            jabatan = input("Masukkan Jabatan baru:")
        
        employees[int(idEmp)]['jabatan'] = jabatan.strip()
    elif int(updateKey) == 5:
        divisi = input('Masukkan Divisi baru:')
        while not validateBlank(divisi.strip()):
            print("Inputan Salah!, inputan masih kosong")
            divisi = input("Masukkan Divisi baru:")

        employees[int(idEmp)]['divisi'] = divisi.strip()
    elif int(updateKey) == 6:
        joinDate = input('Masukkan Tgl. Bergabung baru:')
        while not validasiDate(joinDate.strip()):
            joinDate = input("Masukkan Tgl Bergabung baru (dd-MM-YYYY -> contoh: 31-01-2024):")

        employees[int(idEmp)]['joinDate'] = joinDate.strip()
    else:
        name = input('Masukkan Nama baru:')
        while not validateBlank(name.strip()):
            print("Inputan Salah!, inputan masih kosong")
            name = input("Masukkan Nama baru:")

        phone = input('Masukkan No. Telp baru:')
        while not validasiPhone(phone.strip()):
            phone = input("Masukkan Nomor Telp baru:")

        gender = input('Masukkan Jenis Kelamin baru:')
        while not validasiGender(gender.strip()):
            print("Inputan Salah!, mohon masukan huruf L atau P")
            gender = input("Masukkan Jenis kelamin baru (L/P):")

        jabatan = input('Masukkan Jabatan baru:')
        while not validateBlank(jabatan.strip()):
            print("Inputan Salah!, inputan masih kosong")
            jabatan = input("Masukkan Jabatan baru:")

        divisi = input('Masukkan Divisi baru:')
        while not validateBlank(divisi.strip()):
            print("Inputan Salah!, inputan masih kosong")
            divisi = input("Masukkan Divisi baru:")

        joinDate = input('Masukkan Tgl. Bergabung baru (dd-MM-YYYY -> contoh: 31-01-2024):')
        while not validasiDate(joinDate.strip()):
            joinDate = input("Masukkan Tgl Bergabung baru (dd-MM-YYYY -> contoh: 31-01-2024):")

        updateEmp = {'name':name.strip(),
                     'phone':phone.strip(),
                     'gender':gender.strip().upper,
                     'jabatan':jabatan.strip(),
                     'divisi':divisi.strip(),
                     'joinDate':joinDate.strip()}
        del employees[int(idEmp)]
        employees.insert(int(idEmp),updateEmp)

    print("Data Karyawan berhasil diubah")
    runMenu3()
     
def findData():
    key = input("""================ Pilih Kolom Pencarian ===============
1. Nama Karyawan
2. No. Telp
3. Jenis Kelamin
4. Jabatan
5. Divisi
6. Tgl Bergabung
Masukkan jenis pencarian, dalam angka [1-6]:""")
    while not validasiMenu(key,6):
        print("""Oops! Inputan anda salah,
Mohon masukkan angka/bilangan bulat [1-6]
""")
        findData()

    listResult = []
    if int(key) == 1:
        value = input('Masukkan Nama:')
        for d in employees:
            if value.lower() in d['name'].lower():
                listResult.append(d)
                keyAlias = 'Nama'
    elif int(key) == 2:
        value = input('Masukkan No Telp:')
        for d in employees:
            if value in d['phone']:
                listResult.append(d)
                keyAlias = 'No. Telp'
    elif int(key) == 3:
        value = input('Masukkan Jenis Kelamin [L/P]:')
        for d in employees:
            if value.lower() in d['gender'].lower():
                listResult.append(d)
                keyAlias = 'Jenis Kelamin'
    elif int(key) == 4:
        value = input('Masukkan Jabatan:')
        for d in employees:
            if value.lower() in d['jabatan'].lower():
                listResult.append(d)
                keyAlias = 'Jabatan'
    elif int(key) == 5:
        value = input('Masukkan Divisi:')
        for d in employees:
            if value.lower() in d['divisi'].lower():
                listResult.append(d)
                keyAlias = 'Divisi'
    else:
        value = input('Masukkan Tgl Bergabung:')
        for d in employees:
            if value in d['joinDate']:
                listResult.append(d)
                keyAlias = 'Tgl Bergabung'
                
    if len(listResult) > 0:
        print(f"Berikut Data Karyawan dengan '{keyAlias}' serupa '{value}'")
        printEmployess(listResult)
    else :
        print("Maaf, data tidak ditemukan!\n")
    runMenu2()

def sortData():
    key = input("""
=================== Pilih Kolom Urut =================
1. Nama Karyawan
2. No. Telp
3. Jenis Kelamin
4. Jabatan
5. Divisi
6. Tgl Bergabung
Masukkan kolom yang diurutkan, dalam angka [1-6]:""")
    while not validasiMenu(key,6):
        print("""Oops! Inputan anda salah,
Mohon masukkan angka/bilangan bulat [1-6]
""")
        sortData()
    orderType = input("""
=================== Pilih Jenis Urutan =================
1. Meningkat
2. Menurun
3. Kembali pilih kolom
Masukkan Jenis Urutan, dalam angka [1-3]:""")
    
    while not validasiMenu(orderType,3):
        print("""Oops! Inputan anda salah,
Mohon masukkan angka/bilangan bulat [1-3]
""")
        orderType = input("""
=================== Pilih Jenis Urutan =================
1. Meningkat
2. Menurun
3. Kembali pilih kolom
Masukkan Jenis Urutan, dalam angka [1-3]:""")
    
    keys = list(employees[0].keys())
    if int(orderType) == 1: #asc
        if int(key) != 6: 
            sortedEmp = sorted(employees, key=lambda x: x[keys[int(key)-1]])
        else:
            sortedEmp = sorted(employees, key=lambda x: datetime.strptime(x[keys[int(key)-1]], '%d-%m-%Y'))
        printEmployess(sortedEmp)
        runMenu2()
    elif int(orderType) == 2: #desc
        if int(key) != 6:
            sortedEmp = sorted(employees, key=lambda x: x[keys[int(key)-1]],reverse=True)
        else:
            sortedEmp = sorted(employees, key=lambda x: datetime.strptime(x[keys[int(key)-1]], '%d-%m-%Y'), reverse=True)
        printEmployess(sortedEmp)
        runMenu2()
    else:
        sortData()

def validateBlank(input):
    return len(input) > 0
    
##Validasi Menu
def validasiMenu(input, max, start = 1):
    if not input.isdigit():
        return False
    elif not (start <= int(input) <= max):
        return False
    return True

#Validasi Duplicate Employee
def validasiDuplicateEmp(phone):
    return not any(d['phone'] == phone for d in employees)
    
def validasiPhone(phone):
    #minimal 11-13 char 
    if not (10 < len(phone) <= 13):
        print('Inputan Salah!, no telp. min 11 dan max 13 karakter (hanya angka)!')
        return False
    #hanya angka 
    elif not phone.isdigit():
        print('Inputan Salah!, terdapat karakter bukan angka')
        return False
    elif not phone[0:2] == "08":
        print("Inputan Salah!, telp harus diawali angka '08'")
        return False
    return True

def validasiGender(gender):
    return gender in ["p","l","P","L"]

def validasiDate(date):
    parts = date.split('-')
    if len(parts) != 3:
        print('Inputan Salah!, format tidak sesuai contoh')
        return False
    
    day, month, year = parts
    
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        print('Inputan Salah!, terdapat karakter bukan angka')
        return False
    
    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        print('Inputan Salah!, tanggal & bulan min 2 karakter, tahun min 4 karakter')
        return False
    
    if not (1 <= int(day) <= 31 and 1 <= int(month) <= 12):
        print('Inputan Salah!, range tgl 1-31, range bulan 1-12')
        return False
    
    return True

def tableFormting(listDict):
    global nameMax ,divisiMax ,jabatanMax
    nameMax = len(max([d['name'] for d in listDict if 'name' in d], key=len))+3
    divisiMax = len(max([d['divisi'] for d in listDict if 'divisi' in d], key=len))+3
    jabatanMax = len(max([d['jabatan'] for d in listDict if 'jabatan' in d], key=len))+3
    nameMax = nameMax if nameMax > 13 else 18 
    divisiMax = divisiMax if divisiMax > 6 else 9 
    jabatanMax = jabatanMax if jabatanMax > 7 else 10 

def printEmployess(listDict):
    print('')
    if len(listDict) > 0:
        tableFormting(listDict)
        print("{:<7}| {:<{nameMax}}| {:<15}| {:<15}| {:<{jabatanMax}}| {:<{divisiMax}}| {:13}".format("Index","Nama Karyawan","No. Telp","Jenis Kelamin","Jabatan","Divisi","Tgl Bergabung",nameMax=nameMax, jabatanMax=jabatanMax, divisiMax=divisiMax))
        for i in range(len(listDict)):
            print("{:<7}| {:<{nameMax}}| {:<15}| {:<15}| {:<{jabatanMax}}| {:<{divisiMax}}| {:13}".format(i,listDict[i]['name'],listDict[i]['phone'],listDict[i]['gender'],listDict[i]['jabatan'],listDict[i]['divisi'],listDict[i]['joinDate'],nameMax=nameMax, jabatanMax=jabatanMax, divisiMax=divisiMax))
    else:
        print("""============================
Data Karyawan masih kosong
============================""")

def pilihMenu():
    menu = input("""
================ Menu Aplikasi ==============
1. Tambah Data Karyawan
2. Lihat Data Karyawan
3. Ubah Data Karyawan
4. Hapus Data Karyawan
5. Keluar
Silahkan pilih menu: """)
    while not validasiMenu(menu,5):
        print("""Oops! Inputan anda salah,
Mohon masukkan angka/bilangan bulat [1-6]
""")
        pilihMenu()

    if int(menu) == 1:
        runMenu1()
    elif int(menu) == 2:
        runMenu2()
    elif int(menu) == 3:
        runMenu3()
    elif int(menu) == 4:
        runMenu4()
    else :
        print("""
Terimakasih Telah Menggunakan Aplikasi Data Karyawan,
Sampai Jumpa!""")
        
def initData():
    global employees 
    employees = [{
        "name" : "Lintang Tiara ",
        "phone" : "085333339340",
        "gender" : "P",
        "jabatan" : "Staff",
        "divisi" : "IT Dev",
        "joinDate" : "21-12-2014"
    },
    {
        "name" : "Bulan Dewi",
        "phone" : "085333339340",
        "gender" : "L",
        "jabatan" : "Staff",
        "divisi" : "IT Dev",
        "joinDate" : "11-05-2021"
    },{
        "name" : "Amanda Siahaan",
        "phone" : "085333339340",
        "gender" : "L",
        "jabatan" : "Staff",
        "divisi" : "IT Dev",
        "joinDate" : "09-12-2024"
    },
    {
        "name" : "Meliana",
        "phone" : "085333339340",
        "gender" : "P",
        "jabatan" : "Staff",
        "divisi" : "IT Dev",
        "joinDate" : "31-05-2020"
    }]

print("Selamat Datang di Aplikasi Data Karyawan!")
initData()
pilihMenu()

