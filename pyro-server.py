from bmkg import *
import Pyro4

class BMKG(object):
	def moh(self):
		return "YOOOO"
	def aviation_observation(self):
		return aviation_observation()
	def cuaca_indo_1(self):
		return cuaca_indo_1()
	def gempaterkini(self):
		return gempaterkini()
	def Klimat_Potensi_Banjir(self):
		return Klimat_Potensi_Banjir()
	def Maritim_Tinggi_Gelombang_12jam(self):
		return Maritim_Tinggi_Gelombang_12jam()

Pyro4.Daemon.serveSimple(
	{
		BMKG() : "BMKG"
	},
	host="localhost", port=9999, ns=False, verbose=True)
