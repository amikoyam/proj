#!/bin/bash
for i in `ls reservations`; do
  echo ==============================
  echo $i
  echo diff reservations/$i /etc/dhcp/reservations/$i
  echo ==============================
  diff reservations/$i /etc/dhcp/reservations/$i
 done > diff2.out
