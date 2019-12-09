#!/bin/bash

rm -rf file
rm -rf a.out
rm -rf nr_dirty
rm -rf nr_dirtied
rm -rf nr_written
rm -rf nr_dirty_background_threshold
rm -rf nr_dirty_threshold
touch file

(./collect.sh & (sleep 1.5 && cc write.c && ./a.out)) 

sleep 35
./edit_coll_info.sh &&
./plt.py & ./plt2.py

