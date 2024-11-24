#!/usr/bin/python
# -*- coding: utf-8 -*-
# RAED & mfaraj57 &	 (c) 2018
# Code RAED & mfaraj57

from .compat import compat_Request, compat_urlopen, PY3
from Components.About import about
from Tools.Directories import fileExists, copyfile, resolveFilename, SCOPE_PLUGINS
import datetime
import json
import os
import re
import sys
import traceback

logfile = "/tmp/backupflash.log"
backupflash_script = "/tmp/backupflash.sh"


if not fileExists('/usr/lib64'):
	LIBPATH = '/usr/lib'
else:
	LIBPATH = '/usr/lib64'


def logdata(label='', data=None, logfile='logfile.log'):
	"""
	Logs a label and associated data to a specified log file.

	Args:
		label (str): The label for the log entry.
		data (any): The data to log.
		logfile (str): The path to the log file. Defaults to 'logfile.log'.
	"""
	try:
		with open(logfile, 'a') as log_file:
			log_file.write(str(label) + ' : ' + str(data) + "\n")
	except Exception as e:
		print("Failed to write to log file:", e)


def dellog():
	if os.path.exists(logfile):
		os.remove(logfile)


def copylog(device_path):
	try:
		# Costruzione dei percorsi nella destinazione
		logfile2 = os.path.join(device_path, "backupflash.log")
		backupflash_script2 = os.path.join(device_path, "backupflash.sh")

		# Controllo esistenza del file sorgente e destinazione
		if os.path.exists(logfile2):
			os.remove(logfile2)

		if os.path.exists(logfile) and os.path.isfile(logfile):
			copyfile(logfile, logfile2)

		if os.path.exists(backupflash_script) and os.path.isfile(backupflash_script):
			copyfile(backupflash_script, backupflash_script2)

	except Exception as e:
		print("Error: -", e)


def getimage_version():
	try:
		image_version = about.getEnigmaVersionString()
		return image_version.strip()
	except:
		return None


def getversioninfo():
	currversion = '1.0'
	version_file = resolveFilename(SCOPE_PLUGINS, 'Extensions/backupflashe/tools/version')
	if os.path.exists(version_file):
		try:
			fp = open(version_file, 'r').readlines()
			for line in fp:
				if 'version' in line:
					currversion = line.split('=')[1].strip()
		except:
			pass
	return currversion


def getboxtype():
	"""
	Determines the type of box based on the content of '/proc/stb/info/model'.
	Falls back to a default value or hostname if necessary.

	Returns:
		str: The box type.
	"""
	default_boxtype = "dm7080hd"
	model_file = '/proc/stb/info/model'

	try:
		# Attempt to read the model from the file
		if os.path.exists(model_file):
			with open(model_file, 'r') as f:
				boxtype = f.read().strip().replace('\\l', '')
		else:
			# Fallback to default if the file does not exist
			boxtype = default_boxtype
	except Exception as e:
		# Handle unexpected errors during file access
		print(f"Error reading model file: {e}")
		boxtype = default_boxtype

	# Map specific model names to their respective box types
	model_map = {
		"dm525": "dm520",
		"one": "dreamone",
		"two": "dreamtwo"
	}
	boxtype = model_map.get(boxtype, boxtype)

	# Fallback to hostname if boxtype is empty
	if not boxtype.strip():
		boxtype = getHostName()

	return boxtype


def getHostName():
	try:
		boxtype = open("/etc/hostname").read()
		return boxtype.strip()
	except:
		return ""


def get_images(url, regx):
	images = []
	logdata("images_url", url)
	try:
		req = compat_Request(url, headers={'User-Agent': 'Mozilla/5.0'})  # add [headers={'User-Agent': 'Mozilla/5.0'}] to fix HTTP Error 403: Forbidden
		response = compat_urlopen(req, timeout=5)
		data = response.read()
		response.close()
		match = re.findall(regx, data, re.M | re.I)
		for item1, item2 in match:
			images.append((item1, item2))
		return images
	except:
		trace_error()
		return []


def get_images2(url, regx):
	images = []
	logdata("images_url", url)
	try:
		req = compat_Request(url, headers={'User-Agent': 'Mozilla/5.0'})  # add [headers={'User-Agent': 'Mozilla/5.0'}] to fix HTTP Error 403: Forbidden
		response = compat_urlopen(req, timeout=5)
		if PY3:
			data = response.read().decode('utf-8')
		else:
			data = response.read()
		response.close()
		match = re.findall(str(regx), data, re.M | re.I)
		for item1, item2 in match:
			images.append((item1, item2))
		return images
	except:
		trace_error()
		return []


def get_images_mediafire(url):
	"""
	Extracts image download links from a MediaFire folder URL.

	Args:
		url (str): The MediaFire folder URL.

	Returns:
		list: A list of tuples containing the file name and the download URL.
	"""
	def fetch_url_content(url):
		"""Fetch content from a given URL with error handling."""
		try:
			req = compat_Request(url, headers={'User-Agent': 'Mozilla/5.0'})
			with compat_urlopen(req, timeout=10) as response:
				return response.read().decode('utf-8')
		except Exception:
			trace_error()
			return None

	# Log the provided URL
	logdata("images_url", url)

	# Fetch the initial JSON data from the URL
	raw_data = fetch_url_content(url)
	if not raw_data:
		return []

	try:
		# Parse the JSON data
		jdata = json.loads(raw_data)
		files = jdata['response']['folder_content']['files']
	except (KeyError, json.JSONDecodeError):
		trace_error()
		return []

	# Extract image download links
	images = []
	for file_item in files:
		try:
			download_url = file_item['links']['normal_download']
			file_content = fetch_url_content(download_url)
			if not file_content:
				continue

			# Extract href links matching the pattern
			hrefs = re.findall(r'href="(.*?)"', file_content, re.M | re.I)
			for href in hrefs:
				if "download" in href:
					file_name = os.path.basename(href)
					images.append((file_name, href))
					break
		except KeyError:
			trace_error()
			continue

	print(images)
	return images


def trace_error(logfile="error.log"):
	"""
	Logs the traceback of the current exception to stdout and optionally to a log file.

	Args:
		logfile (str): Path to the log file. If the file does not exist, no logging occurs.
	"""
	try:
		# Print the traceback to stdout
		traceback.print_exc(file=sys.stdout)

		# Check if the logfile exists and append the traceback
		if os.path.exists(logfile):
			with open(logfile, 'a') as log_file:
				traceback.print_exc(file=log_file)
	except Exception as e:
		# Handle unexpected errors in logging
		print(f"Failed to log error: {e}")


def getimage_name():
	# Definizione dei percorsi
	paths = [
		('Backup-GP3', '%s/enigma2/python/Plugins/Bp/geminimain'),
		('Backup-GP4', '%s/enigma2/python/Plugins/GP4/geminilocale/plugin.pyo'),
		('Backup-BlackHole', '%s/enigma2/python/Blackhole'),
		('Backup-OpenBH', '%s/enigma2/python/Screens/BpBlue.pyo'),
		('Backup-MediaSat', '%s/enigma2/python/MediaSat'),
		('Backup-TSimage', '%s/enigma2/python/Plugins/TSimage'),
		('Backup-VTI', '%s/enigma2/python/Plugins/SystemPlugins/VTIPanel'),
		('Backup-DreamElite', '%s/enigma2/python/DE'),
		('Backup-Demonisat', '%s/enigma2/python/Plugins/SystemPlugins/DemonisatManager'),
		('Backup-OpenDroid', '%s/enigma2/python/OPENDROID'),
		('Backup-EGAMI', '%s/enigma2/python/EGAMI'),
		('Backup-Satdreamgr', '%s/enigma2/python/Plugins/Satdreamgr'),
		('Backup-newnigma2', '%s/enigma2/python/Plugins/newnigma2')
	]
	name = None

	# Verifica dei percorsi
	for backup_name, path in paths:
		if os.path.exists(path % LIBPATH):
			name = backup_name
			break

	# Lettura di /etc/image-version
	if name is None and os.path.exists("/etc/image-version"):
		try:
			with open("/etc/image-version") as f:
				for line in f:
					if line.startswith("creator="):
						name = "Backup-" + line.replace("creator=", "").strip().split(" ")[0]
						break
		except IOError:
			pass

	# Lettura di /etc/issue.net
	if name is None and os.path.exists("/etc/issue.net"):
		try:
			with open("/etc/issue.net") as f:
				content = f.read().lower()
				if "power-sat" in content:
					name = "Backup-PowerSat"
				elif "ooozooon" in content:
					name = "Backup-OoZooN"
				elif "peter" in content:
					name = "Backup-PeterPan"
				elif "italysat" in content:
					name = "Backup-ItalySat"
				elif "openatv" in content:
					name = "Backup-openATV"
				elif "rudream" in content:
					name = "Backup-ruDREAM"
				elif "openeight" in content:
					name = "Backup-OpenEight"
				elif "openplus" in content:
					name = "Backup-OpenPlus"
				elif "openpli" in content:
					name = "Backup-OpenPLI"
				elif "opendreambox" in content:
					name = "Backup-Opendreambox"
		except IOError:
			pass

	# Valore di default
	if name is None:
		name = "Backup-dreambox"

	# Aggiunta della data
	now = datetime.datetime.now()
	name += "-" + now.strftime('%Y-%m-%d')

	return name


def getmDevices():
	backup_paths = [
		'/media/usb', '/media/usb1', '/media/hdd', '/media/hdd2',
		'/media/sdcard', '/media/sd', '/universe', '/media/ba', '/data'
	]
	mdevices = []

	if os.path.exists('/proc/mounts'):
		with open('/proc/mounts', 'r') as f:
			mounts = f.readlines()

		for path in backup_paths:
			if any(line.find(path) != -1 for line in mounts):
				backup_dir = path + "/backup"
				os.makedirs(backup_dir, exist_ok=True)
				mdevices.append((backup_dir, backup_dir))

	return mdevices
