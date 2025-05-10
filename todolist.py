todolistdata = []

def todolist(data):
    if not data:
        return []
    result = []
    for idx, item in enumerate(data, start=1):
        status = "Selesai" if item["selesai"] == "selesai" else "belum selesai"
        result.append(f"{idx}. {item['tugas']} ({status})")
    return result

def inputuser():
    tugas = input("Masukkan tugas yang ingin kamu lakukan: ")
    selesai = "belum selesai"
    todolistdata.append({'tugas': tugas, 'selesai': selesai})

def ubahstatus(data):
    if not data:
        print()
        print("To Do list masih kosong")
        print()
        return
    for item in todolist(data):
        print()
        print(item)
    try:
        pilihan = int(input("Masukkan nomor tugas: "))
        if 1 <= pilihan <= len(data):
            data[pilihan -1]['selesai'] = (
                'selesai' if data[pilihan -1]['selesai'] == 'belum selesai' else 'belum selesai'
            )
            print()
            print("Nomor Berhasil Diubah")
            print()
        else:
            print("Nomor Tidak Valid")
    except ValueError:
        print()
        print("Input Harus Berupa Angka")
        print()

while True:
    print()
    print()
    print("To-Do List")
    print()
    print()
    print("============================================================================================================================")
    for item in todolist(todolistdata):
        print(item)
    print()
    print("============================================================================================================================")
    print()
    print("1. Tambahkan Tugas")
    print("2. Ubah Status Tugas")
    user = input("Pilih Perintah (1/2): ")

    if user == "1":
        inputuser()
    elif user == "2":
        ubahstatus(todolistdata)
    else:
        print()
        print("Pilihan Tidak Tersedia")
        print()