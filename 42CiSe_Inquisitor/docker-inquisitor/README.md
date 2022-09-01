# Start containers:
First of all we need to install Docker, docker-compose and then run
> docker-compose up -d
> sh start.sh (gets into attacker container).

# To start running commands just write:
> docker exec -it attacker bash

# To look at the ips contained in the network:
> docker network ls
> docker network inspect docker-inquisitor_default

# Ftp server user and password:
- User: ftp
- Password: ftp

# To see traffic use 'tcpdump':
> tcpdump -n (listens but donesn't solve ips).
> tcpdump -D (interfaces list).
> tcpdump -ni eth0 arp (only shows arp packages).

# To see arp table use 'arp' command from net-tools package:
> arp -n (see arp table without solving ips).

# To increase table contents write 'ping'.

# To send arp packages use 'arping' command from arping package.
(This won't increase arp table).
