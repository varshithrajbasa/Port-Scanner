# Port-Scanner
Fastest Port Scanner
version 1.1.2

### Usage:
```
git clone https://github.com/varshithrajbasa/Port-Scanner.git
cd Port-Scanner
chmod +x portscanner.py
./portscanner.py --help
```

### Example:
```
./portscanner.py --help

  ____________________
< Port Scanner v.1.1.2 >
  --------------------
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||


        Usage:
        ./portscanner.py [options] value [optional] value

        options:
            -i      ip address
            -h      hostname
            -l      list of ip addresses or hostnames

        optional:
            -p      range of ports Ex: -p 80 8888 (default range 1 to 65535)
```

### Usage with ip:
```
./portscanner.py -i 127.0.0.1
```

### Usage with hostname:
```
./portscanner.py -i localhost
```

### Usage with list file:
Add ip addresses or hostnames to list.txt or create your own file 
```
./portscanner.py -l file.txt
```

### Usage with port:
```
./portscanner.py -i 127.0.0.1 -p 80 8080
```

### Video:

![Port-Scanner](https://varshithrajbasa.github.io/files/Port-Scanner/Port-Scanner.gif "Fastest Port Scanner")