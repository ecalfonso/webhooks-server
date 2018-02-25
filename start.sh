#!/bin/bash

sudo webhook\
	-verbose\
	-hooks hooks.json\
	-ip 192.168.29.2\
	-port 5000\
	-hotreload
