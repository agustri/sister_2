sister_2
========

List file project
==================
1. `bmkg.py` : Berisi fungsi2 dasar untuk mendownload dan parsing xml dari data.bmkg.go.id
2. `pyro-client.py` : client Pyro4
3. `pyro-server.py` : server Pyro4 yang meregistrasikan fungsi2 dari bmkg.py
4. `rpc-client.py` : client RPC standar dari Python
5. `rpc-server.py` : server RPC standar dari Python yang meregistrasikan fungsi2 dari bmkg.py
6. `xml/*` : berisi file xml dari data.bmkg.go.id

Instalasi Package Pyro4
=======================
Dokumentasi lengkap instalasi package Pyro4 : http://pythonhosted.org//Pyro4/install.html
	- Download file *.tar.gz dari https://pypi.python.org/pypi/Pyro4
	- Ekstrak file tersebut
	- Eksekusi file `setup.py` dari file yang di Ekstrak

Perhatian
=========
Agar `bmkg.py` mengambil data langsung dari data.bmkg.go.id pastikan
`remote_xml="yes"` pada file bmkg.py

Dokumentasi
===========
1. RPC : https://docs.python.org/2/library/xmlrpclib.html
2. Pyro4 : http://pythonhosted.org//Pyro4/servercode.html
3. Cara parsing XML : https://docs.python.org/2/library/xml.etree.elementtree.html