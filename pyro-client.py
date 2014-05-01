import Pyro4

# Client akan melakukan koneksi ke server localhost:9999 dan memanggil object BMKG
uri = "PYRO:BMKG@localhost:9999"
bmkg = Pyro4.Proxy(uri)

notice =  """
Pilih nomor data yang akan di-ambil dari server:
1. aviation_observation
2. cuaca_indo_1
3. gempaterkini
4. Klimat_Potensi_Banjir
5. Maritim_Tinggi_Gelombang_12jam

Pilihan: """

# Cara memanggil fungsi dari server : <Remote object>.<method pada remote object>()
def aviation_observation():
	print bmkg.aviation_observation()

def cuaca_indo_1 ():
	print bmkg.cuaca_indo_1()

def gempaterkini():
	print bmkg.gempaterkini()

def Klimat_Potensi_Banjir():
	print bmkg.Klimat_Potensi_Banjir()

def Maritim_Tinggi_Gelombang_12jam():
	print bmkg.Maritim_Tinggi_Gelombang_12jam()

# fungsi di atas dimasukkan ke dictionary
case = {
	"1" : aviation_observation,
	"2" : cuaca_indo_1,
	"3" : gempaterkini,
	"4" : Klimat_Potensi_Banjir,
	"5" : Maritim_Tinggi_Gelombang_12jam	
}

while True:
	print notice
	inp = raw_input()
	# panggil method sesuai key input dari dictionary case
	case[inp]()
