CC= gcc
CFLAGS=
LIB=

all:main

myfile:
	$(CC) $(CFLAGS) -c myfile.c

main:myfile
	$(CC) $(CFLAGS) myfile.o main.c -o main

run:
	.\main.exe