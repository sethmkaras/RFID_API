#!/bin/bash
createTunnel(){
/usr/bin/ssh -N -R 
if [[ $? -eq 0 ]]; then
	echo Tunnel to jumpbox created
else
	echo Error
if
}
/bin/pidof ssh
if [[ $? -ne 0 ]]; then
  echo Creating new tunnel connection
  createTunnel
fi
