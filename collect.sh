#!/bin/bash
i=1
while(($i<=500))
do
    cat /proc/vmstat |egrep -w 'nr_dirty' >> nr_dirty
    cat /proc/vmstat |egrep -w 'nr_dirtied' >> nr_dirtied
    cat /proc/vmstat |egrep -w 'nr_written' >> nr_written
    cat /proc/vmstat |egrep -w 'nr_dirty_threshold' >> nr_dirty_threshold
    cat /proc/vmstat |egrep -w 'nr_dirty_background_threshold' >> nr_dirty_background_threshold
    sleep 0.05

    let "i++"
done
