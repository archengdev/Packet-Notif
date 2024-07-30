# get private RC4 keys
from private import KEY_INCOMING, KEY_OUTGOING

from scapy.all import *
import socket
from arc4 import ARC4

import threading

import chime

 


chime.info()

conf.sniff_promisc = 0 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('8.8.8.8', 80))
CLIENT_IP = sock.getsockname()[0]
sock.close()
packet_buffer = b''
PACKET_ID_REF = {74:'HELLO'}
arc4_server = ARC4(KEY_INCOMING)
predicted_seq_server = -1
ooo_storage = {}
history = {}
decryption_history = b''
 
def parse_stream(packet):
	global predicted_seq_server
	global ooo_storage
	global packet_buffer 
	global arc4_server
	global history
	global decryption_history
	if packet.haslayer(Raw):
		packet_data = packet[Raw].load
		if packet[IP].src == CLIENT_IP:
			if PACKET_ID_REF.get(packet_data[4]) == 'HELLO':
				hello_reset(packet)
				return
		else:
			if predicted_seq_server != -1:
				if packet[TCP].seq == predicted_seq_server:
					history[predicted_seq_server] = [packet_buffer,decryption_history]
					predicted_seq_server += len(packet_data) 
					identify_packets(packet_data)
 
				elif packet[TCP].seq < predicted_seq_server:
					predicted_seq_server = packet[TCP].seq + len(packet_data)
					packet_buffer = history[packet[TCP].seq][0]
					arc4_server = ARC4(KEY_INCOMING)
					server_decrypt_arc4(history[packet[TCP].seq][1])
					decryption_history = history[packet[TCP].seq][1]
					identify_packets(packet_data)
 
				else:
					ooo_storage[packet[TCP].seq] = packet[Raw].load
					history[predicted_seq_server] = [packet_buffer,decryption_history]
					while predicted_seq_server in ooo_storage:
							target_load = ooo_storage[predicted_seq_server]
							del ooo_storage[predicted_seq_server]
							predicted_seq_server += len(target_load)
							identify_packets(target_load)
 
 
def identify_packets(data=b''): 
	global packet_buffer
	packet_buffer += data
	if len(packet_buffer) >= 5:
		packet_size = int.from_bytes(packet_buffer[0:4],'big')
		if len(packet_buffer) >= packet_size:
			packet = packet_buffer[:packet_size]
			decrypt_packet(packet)
			packet_buffer = packet_buffer[packet_size:]
			identify_packets()
 
def decrypt_packet(packet_data):
	global decryption_history
	decrypted = server_decrypt_arc4(packet_data[5:])
		# decrypted = packet_data[0:5]+server_decrypt_arc4(packet_data[5:])
	decryption_history += packet_data[5:]
	packet_id = packet_data[4]
	# if packet_id not in (92, 8, 10, 42, 11, 44, 120, 6, 45, 117, 12): print(packet_id)
	# either 101 or 114
	handler = HANDLERS.get(packet_id)
	if handler:
		# print(packet_id)
		handler(decrypted)
 
def hello_reset(packet):
	global packet_buffer
	global arc4_server
	global predicted_seq_server
	global ooo_storage
	global decryption_history
	global history
 
	packet_buffer = b''
	arc4_server = ARC4(KEY_INCOMING)
	predicted_seq_server = packet[TCP].ack
	ooo_storage = {}
	decryption_history = b''
	history = {}
 
 
def server_decrypt_arc4(ciphertext):
	return arc4_server.decrypt(ciphertext)
 
def handle_chat(decrypted):
	print(str(decrypted)) 
    # pass

 
def handle_notification(decrypted):
	print(type(decrypted))
	string = str(decrypted)
	print(string)
	print(decrypted.decode('utf_8'))
	# print(string)
	if string[21:22] == 'd':
		print(string)
		chime.info()
		# tab_in()
		
    
HANDLERS = {67:handle_notification}
 
def main():
	sniff(filter = 'tcp port 2050', iface = 'WiFi',prn = parse_stream)
 
x = threading.Thread(target=main)
x.start()



"""
misc notes:

hello: 92
new dungeon: 101/114??????????
move: 42
chat: 44
quests: 6
random:12/18/139

random stuff: 8/10
more randomstuff: 11/67/ 120/45/117
"""

# moonline: b'\x08\n\x008{"k":"s.dungeon_opened_by","t":{"player":"Bobbybeast",}}\x00\x00O\xdf'

# shaitain: b'\x08\n\x006{"k":"s.dungeon_opened_by","t":{"player":"BIGHURTS",}}\x00\x00m\x99'

#ot: b'\x08\n\x006{"k":"s.dungeon_opened_by","t":{"player":"Coolfood",}}\x00\x00\x070'
#ot: b'\x08\n\x008{"k":"s.dungeon_opened_by","t":{"player":"Sleepersun",}}\x00\x00\x070'

#mv: b'\x08\n\x006{"k":"s.dungeon_opened_by","t":{"player":"Huntrexx",}}\x00\x00O\xdf'

#fungal: b'\x08\n\x004{"k":"s.dungeon_opened_by","t":{"player":"Alrino",}}\x00\x00\xb2o'
#fungal: b'\x08\n\x008{"k":"s.dungeon_opened_by","t":{"player":"Bobbybeast",}}\x00\x00\xb2o'

#lod: b'\x08\n\x006{"k":"s.dungeon_opened_by","t":{"player":"Drwasabl",}}\x00\x00\xb2\x17'

#mt: b'\x08\n\x007{"k":"s.dungeon_opened_by","t":{"player":"DarkPutin",}}\x00\x00\x017'

#cnidarian: b'\x08\n\x004{"k":"s.dungeon_opened_by","t":{"player":"HowCat",}}\x00\x00\t\xfa'

#sewer: b'\x08\n\x008{"k":"s.dungeon_opened_by","t":{"player":"DabossofXX",}}\x00\x00\x02>'
#sewer: b'\x08\n\x001{"k":"s.dungeon_opened_by","t":{"player":"ame",}}\x00\x00\x02>'

#udl: b'\x08\n\x001{"k":"s.dungeon_opened_by","t":{"player":"ame",}}\x00\x00\x07\x1a'

#parasite: b'\x08\n\x005{"k":"s.dungeon_opened_by","t":{"player":"MINROKS",}}\x00\x00\x07\x98'
#parasite: b'\x08\n\x005{"k":"s.dungeon_opened_by","t":{"player":"MINROKS",}}\x00\x00\x07\x98'
#parasite: b'\x08\n\x005{"k":"s.dungeon_opened_by","t":{"player":"MINROKS",}}\x00\x00\x07\x98'

#lab: b'\x08\n\x008{"k":"s.dungeon_opened_by","t":{"player":"Usalixxxxx",}}\x00\x00\x08\x90'
#lab: b'\x08\n\x004{"k":"s.dungeon_opened_by","t":{"player":"Xethyl",}}\x00\x00\x08\x90'

#nest: b'\x08\n\x00={"k":"s.dungeon_opened_by","t":{"player":"TheOneEyes,9a0c",}}\x00\x00\x10\xa3

#lost halls: b'\x08\n\x006{"k":"s.dungeon_opened_by","t":{"player":"BIGHURTS",}}\x00\x00m\x99'