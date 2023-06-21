#!/usr/bin/bash 
# 
# This script will install ISO file on available USB stick.  Syntax:
# 	./booter.sh SOURCE
# 
shopt -s lastpipe
src=$1

result=`lsblk -do PATH,SUBSYSTEMS,SIZE | grep usb`
# result=`ls -l | grep -v "^total "`
lnct=`echo "$result" | wc -l`

if [ $lnct -lt 1 ]; then
  echo "no USB device"
  exit 1
fi

if [ $lnct -eq 1 ]; then
  line=$result
fi

if [ $lnct -gt 1 ]; then
  echo "There are more than one USB thumb drives:"
  echo
  echo "$result" | cat -n
  echo "Please, select the number from the above menu: "
  read resp
  if [ $resp -ge 1 ] && [ $resp -le $lnct ]; then
    index=1
    echo "$result" | while read -r line; do
      if [ $index -gt $resp ]; then
	echo "out of range"
	exit 1
      fi
      if [ $index -eq $resp ]; then
        break
      fi
      let "index = $index + 1"
    done
  fi
fi
echo $line
usbdev=`echo $line | awk '{ print $1 }'`
echo $usbdev
