class Node: #untuk membuat struktur dasar dari sebuah simpul dalam node
    def __init__(self, data): #ntuk mengatur data awal saat node baru 
        dibuat
        
        self.data = data #untuk menyimpan nilai yang dimasukan dalam node
        self.prev = None #self prev adalah reverensi  ke node  sebelumnya
        self.next = None # self next adalah reverensi ke node berikutnya

class DoubleLinkedList: #membuat class doble linklst yaitu kumpulan node
    yang saling terhubung dua arah
    def __init__(self): #metode khusus untuk inisialisasi ketika objek linklist dibuat
        self.head = None #head adalah simpul pertama atau kepala dari linklist

    def tambah_di_akhir(self, data): #untuk menambahkan node baru di akhir linklist
        new_node = Node(data) #membuat node baru berisi data yang ingin dimasukan 
        if self.head is None: #untuk cek jika list masih kosong
            self.head = new_node # maka node baru dibuat untuk menjadi kepala
            return #untuk menghentikan proses karna node sudah ditambahkan
        curr = self.head #jika list tidak kosong, mulai dari node kepala
        while curr.next: #selama masih ada node berikutnya maka lanjut ke node berikutnya
            curr = curr.next  #hingga sampai ke node terakhir
        curr.next = new_node #untuk menghubungkan node terakhir
        new_node.prev = curr #untuk menghubungkan node baru ke node sebelumnya

    def hapus_node_awal(self): #untuk menghapus node pertama (head) dari linklist
        if self.head is None: #jika list kosong maka tidak ada yang bisa dihapus
            print("Linked list kosong. Tidak ada yang bisa dihapus.") #untuk menampilkan pesan bahwa list kosong
            return #menghentikan fungsi
        print(f"Menghapus node dengan data: {self.head.data}") #untuk menampilkan data node yang akan dihapus
        if self.head.next is None: #untuk cek jika hanya ada satu node yang dihapus
            self.head = None  # List jadi kosong
        else:
            self.head = self.head.next #untuk menggeser head ke node berikutnya
            self.head.prev = None #untuk menghapus hubungan balik ke node lama

    def tampilkan(self): #fungsi untuk menampilkan semua data di list
        curr = self.head #untuk memulai list dari kepala
        while curr: #selama node masih ada
            print(curr.data, end=" <-> ") #untuk menampilkan data dengan tanda panah dua arah
            curr = curr.next #untuk lanjut ke node berikutnya
        print("None") #untuk menampilkan list terakhir

# Contoh penggunaan
dll = DoubleLinkedList()
dll.tambah_di_akhir(10)
dll.tambah_di_akhir(20)
dll.tambah_di_akhir(30)

print("Sebelum penghapusan:")
dll.tampilkan()

dll.hapus_node_awal()

print("Setelah penghapusan:")
dll.tampilkan()
