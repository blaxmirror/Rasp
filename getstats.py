#!/usr/bin/env python3

import os
import platform

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return int(res.replace("temp=","").replace("'C\n",""))

def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return(line.split()[1:4])

def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))

def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return(line.split()[1:5])

def getstats():
    stats = {"CPU_temp":0, "CPU_usage":0, "RAM_total":0, "RAM_used":0, "RAM_free":0, "DISK_total":0, "DISK_used":0, "DISK_perc":0}
    if (platform.system()=="Linux"):
        stats["CPU_temp"] = getCPUtemperature()
        stats["CPU_usage"] = getCPUuse()

        RAM_stats = getRAMinfo()
        # MB
        stats["RAM_total"] = round(int(RAM_stats[0])/1000, 1)
        stats["RAM_used"] = round(int(RAM_stats[1])/1000, 1)
        stats["RAM_free"] = round(int(RAM_stats[2])/1000, 1)

        DISK_stats = getDiskSpace()
        # B
        stats["DISK_total"] = DISK_stats[0]
        stats["DISK_used"] = DISK_stats[1]
        stats["DISK_perc"] = DISK_stats[3]
    return stats
