#!/usr/bin/python3

import socket  # this import is for the socket library
			   # https://www.geeksforgeeks.org/socket-in-computer-network/

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "137.74.187.100"  # ipv4 address of hackthissite.org for testing
port = 80


def port_scanner(port):
	if s.connect_ex((host, port)):
		print("The port is possibly closed")
	else:
		print("The port is possibly open")


port_scanner(port)
