#!/bin/bash
vim -e nr_dirty <<-!
    :%s/^.\{8\}/   /
    :let i=1
    :g/^/ s//\=i . ' '/|let i=i+1
    :wq
!

vim -e nr_dirtied <<-!
    :%s/^.\{10\}/   /
    :let i=1
    :g/^/ s//\=i . ' '/|let i=i+1
    :wq
!

vim -e nr_written <<-!
    :%s/^.\{10\}/   /
    :let i=1
    :g/^/ s//\=i . ' '/|let i=i+1
    :wq
!

vim -e nr_dirty_threshold <<-!
    :%s/^.\{18\}/   /
    :let i=1
    :g/^/ s//\=i . ' '/|let i=i+1
    :wq
!

vim -e nr_dirty_background_threshold <<-!
    :%s/^.\{29\}/   /
    :let i=1
    :g/^/ s//\=i . ' '/|let i=i+1
    :wq
!