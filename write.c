#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main(){
    int fd = open("./file", O_RDWR | O_APPEND);
    if(fd < 0){
        printf("open error\n");
        return fd;
    }

    printf("fd = %d\n",fd);
    
    int i = 0;
    for(; i < (1 << 20); i++){
        write(fd, "11111", 300);
    }

    return fd;
}
