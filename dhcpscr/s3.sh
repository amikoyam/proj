#!/bin/bash
for i in *.conf; do
if [ -f $i.old ]; then
echo ====================
echo diff $i $i.old
echo ====================
diff $i $i.old
fi
done > diff.out
