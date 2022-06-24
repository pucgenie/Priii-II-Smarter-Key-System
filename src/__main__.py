#!/bin/python3
# thanks to https://raspberrypi.stackexchange.com/a/116162/27200 Sejpalsinh Jadeja

# import os
# https://bluedot.readthedocs.io/en/latest/btcommapi.html#bluetoothserver
from bluedot.btcomm import BluetoothServer
# import bluetooth
from systemd import journal
from systemd.daemon import notify, Notification

def beginShell():
	pass

def endShell():
	"""
	"TODO: Set timer (wifioff) if something was switched on by us?
	"""
	pass

# os.system('sudo bluetoothctl discoverable on && sudo bluetoothctl agent NoInputNoOutput')
# import time
# time.sleep(2)


class BlConCommands:
	def stamode(self, timeout=None, *args,):
		"""
		Connect to known WiFis automatically. Starts sshd.
		@param timeout After <time in minutes> elapses, do wifioff. Default: infinite.
		"""
		
		pass

	def apmode(self, apname, apkey, timeout=15, *args,):
		"""
		Start an Access Point to enable clients to connect to the WiFi and use ssh for advanced system access. Starts sshd.
		@param apname ESSID of Access Point to announce.
		@param apkey Password of Access Point.
		@param timeout After time in minutes elapses, do wifioff. Default: 15 minutes.
		"""
		pass

	def wifioff(self, *args,):
		"""
		Stops sshd, disconnects WiFi by using rfkill.
		"""
		pass

	def reboot(self, *args,):
		"""
		Whatever the reason, reboot now.
		"""
		pass

	def skson(self, *args,):
		"""
		Turn on Smart Key System power (but don't change key power state)
		"""
		pass

	def sksoff(self, *args,):
		"""
		Turn off Smart Key System power (but don't change key power state)
		"""
		pass

	def keyon(self, *args,):
		"""
		Turn on key power.
		"""
		pass

	def keyoff(self, *args,):
		"""
		Turn off key power.
		"""
		pass

	def unlock(self, *args,):
		"""
		Turn on key power if necessary, actuate unlock button. (Turn off key power if powered on automatically.)
		"""
		pass

	def lock(self, *args,):
		"""
		Turn on key power if necessary, turn off SKS if necessary, actuate lock button. (Turn on SKS again if powered off automatically, turn off ke>
		"""
		pass

	def active(self, *args,):
		"""
		Turn on SKS power, turn on key power.
		"""
		pass

	def pieps(self, *args,):
		"""
		Use not-so-loud high horn to play a sound. Optional.
		"""
		pass

	def staconnect(self, *args,):
		"""
		Add new known WiFi. Optional.
		"""
		pass

	def staremove(self, *args,):
		"""
		Remove known WiFi by ESSID. Optional.
		"""
		pass

	def osexec(self, *args,):
		"""
		Execute something, quick'n'dirty. Or start bash.
		"""
		pass


bconcHandler = BlConCommands()

import shlex


def data_received(data):
	"""
	Input is trusted, secured by Bluetooth pairing.
	"""
	concmd = shlex.split(data.decode(encoding='UTF-8'))
	conresult = getattr(bconcHandler, concmd[0])(lambda bytesToSend: s.send(bytesToSend), *concmd[1:],)
	if not conresult:
		s.send(f"Not implemented: {data.decode(encoding='UTF-8')}".encode(encoding='UTF-8'))


s = BluetoothServer(
	data_received_callback=data_received,
	encoding=None,
	auto_start=True, power_up_device=True,
	when_client_connects=beginShell, when_client_disconnects=endShell,
)

print(s)

# prevent Python from exiting because the main thread reached end of code. Bluetooth Server runs in the background.
input()
