#!/bin/bash
for i in `ls changes`; do
  echo ==============================
  echo $i
  echo diff changes/$i reservations/$i
  echo ==============================
  diff changes/$i reservations/$i
 done > diff.out
