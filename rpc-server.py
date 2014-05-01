from bmkg import *
from SimpleXMLRPCServer import SimpleXMLRPCServer

# Menbuat server yang akan berjalan pada localhost port 8888
server = SimpleXMLRPCServer(("localhost", 8888))
print "server running pada port 8888"

# Registrasi fungsi dari bmkg.py pada server RPC
server.register_introspection_functions()
server.register_multicall_functions()
server.register_function(aviation_observation, "aviation_observation")
server.register_function(cuaca_indo_1, "cuaca_indo_1")
server.register_function(gempaterkini, "gempaterkini")
server.register_function(Klimat_Potensi_Banjir, "Klimat_Potensi_Banjir")
server.register_function(Maritim_Tinggi_Gelombang_12jam, "Maritim_Tinggi_Gelombang_12jam")

# Jalankan server selamanya
server.serve_forever()
