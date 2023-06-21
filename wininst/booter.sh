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
usbdev=`echo $line | awk '{ print $1 }'`

export http_proxy=http://proxy-dmz.intel.com:912
export https_proxy=http://proxy-dmz.intel.com:912
export no_proxy=localhost,intel.com,10.0.0.0/8,10.64.0.0/10,100.64.0.0/12,100.80.0.0/16,10.244.0.0/16,10.96.0.0/12,10.45.128.26,10.45.128.27,10.45.128.28,10.45.128.10,10.45.128.41,10.45.128.42,10.45.128.43,10.45.128.44,10.45.128.45,10.45.128.46
echo $src | grep -q http
if [ $? -eq 0 ]; then
  cd /tmp
  retv=$?
  if [ $retv -ne 0 ]; then
    echo "cd /tmp failed"
    exit $retv
  fi
  wget $src
  retv=$?
  if [ $retv -ne 0 ]; then
    echo "wget failed"
    exit $retv
  fi
else
  mount `dirname $src` /mnt
  retv=$?
  if [ $retv -ne 0 ]; then
    echo "mount failed"
    exit $retv
  fi
  cd /mnt
  retv=$?
  if [ $retv -ne 0 ]; then
    echo "cd /mnt failed"
    exit $retv
  fi
fi

dd if=`basename $src` of=$usbdev
retv=$?
if [ $retv -ne 0 ]; then
  echo "dd command failed"
  exit $retv
fi


