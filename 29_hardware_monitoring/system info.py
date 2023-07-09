#!/usr/bin/python3

"""
	Scanning your system about CPU, memory usage
	and other hardware informations.

	By default, some packages, like psutil, GPUtil aren't installed on your system,
	which needs to be installed by pip.
"""

import platform as p
import os, re, subprocess as s
import psutil, GPUtil

tab = '\t'
quote = "'"

def analyzeCPU() -> str:
	"""
		Analyzing the CPU depending on the
		operating system and if it was able
		to scan the data.
	"""
	if p.system() == "Windows":
		return p.processor()
	#end if

	#	usually in use for macOS
	if p.system() == "Darwin":
		os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'

		command ="sysctl -n machdep.cpu.brand_string"
		return s.check_output(command).strip()
	#end if

	if p.system() == "Linux":
		command = "cat /proc/cpuinfo"

		allInformations = s.check_output(command, shell=True).decode().strip()
		for line in allInformations.split("\n"):
			if "model name" in line:
				return re.sub( ".*model name.*:", "", line,1)
			#end if
		#end for

	return "unable to detect your system CPU..."
#end function

def usageCPU() -> str:
	"""
		returning current CPU usages
		depending on how many processes you're
		running at the moment, your machine, etc.
	"""
	load1, load2, load3 = psutil.getloadavg()
	return f"{(load1 / os.cpu_count()) * 100:.5}%{tab}{(load2 / os.cpu_count()) * 100:.5}%{tab}{(load3 / os.cpu_count()) * 100:.5}%"
#end function

def humanReadableSize(bytes: int) -> str:
	"""
		transforming bytes into a better format
	"""
	readable = ''

	#	it's primitive, but works :P

	if bytes < 1024:
		readable = f'{bytes:.5} B'
	elif bytes >= 1024 and bytes < (1024*1024):
		readable = f'{bytes/1024:.5} KB'
	elif bytes >= (1024*1024) and bytes < (1024*1024*1024):
		readable = f'{bytes/(1024*1024):.5} MB'
	elif bytes >= (1024*1024*1024) and bytes < (1024*1024*1024*1024):
		readable = f'{bytes/(1024*1024*1024):.5} GB'
	else:
		readable = f'{bytes/(1024*1024*1024/1024):.5} TB'
	#end if

	return readable
#end function

def getCPUTemperature() -> float:
	"""
		Receiving the CPU temperature.

		ATTENTION: It may be, that the used key doesn't exist,
		so run the command psutil.sensors_temperatures() instead
		to reveal your requested information.
	"""
	return psutil.sensors_temperatures()['k10temp'][0].current
#end function

def getGPUInformations() -> str:
	"""
		Do the same thing for your GPU.

		Make sure, that the GPUtil package
		has been installed on your system.
	"""

	everything = list()

	#	the available GPU RAM must be multiplicated with 1024,
	#	otherwise a wrongly information returns

	for gpu in GPUtil.getGPUs():
		everything.append(f"""
{tab}{tab}name: {gpu.name}
{tab}{tab}driver: {gpu.driver}
{tab}{tab}temperature: {gpu.temperature} °C ({(gpu.temperature * 9/5) + 32} °F)
{tab}{tab}total RAM: {humanReadableSize(gpu.memoryTotal * 1024)}
{tab}{tab}used: {humanReadableSize(gpu.memoryUsed * 1024)}
{tab}{tab}free: {humanReadableSize(gpu.memoryFree * 1024)}
""")
	#end for

	return ''.join(everything)
#end function

def displayHardware():
	"""
		Hardware monitoring with python 3.
	"""

	#	receiving RAM informations
	ram = psutil.virtual_memory()

	allInformations = f"""
	You're running this script on a {quote}{p.system()}{quote} machine, with:

	machine type: {quote}{p.machine()}{quote}
	computer name: {quote}{p.node()}{quote}
	full OS name: {quote}{p.platform()}{quote}
	system release name: {quote}{p.release()}{quote}

	short summary:
	{p.uname()}

	hardware monitoring:
	CPU: {analyzeCPU()}
	# of cores: {os.cpu_count()}
	current CPU usages: {usageCPU()}
	current temperature: {getCPUTemperature()} °C

	RAM:
		total: {humanReadableSize(ram[0])}
		available: {humanReadableSize(ram[1])}
		currently in use: {ram[2]}%
		used: {humanReadableSize(ram[3])}
		free: {humanReadableSize(ram[4])}
		active: {humanReadableSize(ram[5])}
		inactive: {humanReadableSize(ram[6])}
		buffers: {humanReadableSize(ram[7])}
		cached: {humanReadableSize(ram[8])}
		shared: {humanReadableSize(ram[9])}
		slab: {humanReadableSize(ram[10])}

	GPU:{getGPUInformations()}
	"""

	print(allInformations)
#end function

if __name__ == '__main__':
	displayHardware()
#end entry point