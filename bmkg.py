import urllib2
import xml.etree.ElementTree as ET

remote_xml="yes"

xml_source = {
	1 : "http://data.bmkg.go.id/aviation_observation.xml",
	2 : "http://data.bmkg.go.id/cuaca_indo_1.xml",
	3 : "http://data.bmkg.go.id/gempaterkini.xml",
	4 : "http://data.bmkg.go.id/Klimat_Potensi_Banjir.xml",
	5 : "http://data.bmkg.go.id/Maritim_Tinggi_Gelombang_12jam.xml"
}

# download data dari url
def readurl(url):
	url = urllib2.urlopen(url)
	data = url.read()
	url.close()
	return data

# menggabungkan string name dan value menjadi 'name<spasi>: value'
def addvalue(name, value):
	return "{0:23}: {1}\n".format(str(name), str(value))

# konversi node dari xml menjadi 'node.tag<spasi>: node.text'
def addnode(node):
	return "{0:23}: {1}\n".format(str(node.tag), str(node.text))

# ============= Download kemudian parsing file xml ==================
def aviation_observation():
	tree = ET.parse("xml/aviation_observation.xml") 
	root = tree.getroot()
	if remote_xml=="yes" :
		xml1 = readurl(xml_source[1])
		root = ET.fromstring(xml1)

	# print root.tag
	output = addnode(root[0])
	output += "[data pertama : aviation_observation]\n"
	for i in root[1]:
		output += addnode(i)
	return str(output)

def cuaca_indo_1 ():
	tree = ET.parse("xml/cuaca_indo_1.xml") 
	root = tree.getroot()
	if remote_xml=="yes" :
		xml1 = readurl(xml_source[2])
		root = ET.fromstring(xml1)
	
	output = addvalue("tanggal mulai", root[0][0].text)
	output += addvalue("tanggal selesai", root[0][1].text)
	output += "[data pertama : cuaca_indo_1]\n"
	for i in root[1][0]:
		output += addnode(i)
	return output

def gempaterkini():
	tree = ET.parse("xml/gempaterkini.xml") 
	root = tree.getroot()
	if remote_xml=="yes" :
		xml1 = readurl(xml_source[3])
		root = ET.fromstring(xml1)

	output = "[data pertama : gempaterkini]\n"
	for i in root[0]:
		if i.tag=="point" :
			output += addnode(i[0])
		else:
			output += addnode(i)
	return output

def Klimat_Potensi_Banjir():
	tree = ET.parse("xml/Klimat_Potensi_Banjir.xml") 
	root = tree.getroot()
	if remote_xml=="yes" :
		xml1 = readurl(xml_source[4])
		root = ET.fromstring(xml1)

	output = addvalue("tanggal publikasi", root[0].text)
	output += addvalue("jumlah data", root[1].text)
	output += "[data pertama : Klimat_Potensi_Banjir]\n"
	for i in root[2][0]:
		if i.tag=="dataWilayah" :
			for wil in i:
				output += addvalue(wil[0].tag, wil[0].text)
		else:
			output += addnode(i)
	return output

def Maritim_Tinggi_Gelombang_12jam():
	tree = ET.parse("xml/Maritim_Tinggi_Gelombang_12jam.xml") 
	root = tree.getroot()
	if remote_xml=="yes" :
		xml1 = readurl(xml_source[5])
		root = ET.fromstring(xml1)

	output = addvalue("tanggal publikasi", root[0].text)
	output += "[data pertama : Maritim_Tinggi_Gelombang_12jam]\n"
	for i in root[1]:
		if i.tag=="Gelombang" :
			output += addnode(i[0][0])
			for wil in i[0][1]:
				output += addvalue(wil.tag, wil.text)
		elif i.tag=="WilayahHujan" :
			output += addvalue("WilayahHujan", i[0].text)
		else:
			output += addnode(i)
	return output
# ===================================================================