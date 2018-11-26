# pyshodan
Little python script to quickly query using the Shodan API

## Description
A simple Python script to quickly query Shodan using the IP-address, domain name, or search for a specific banner.

## Usage
The script accepts either of the three parameters:
* --ip to look up information based on the IP-address
* --domain to look up information based on the domain name
* --banner to look up IP-addresses and hostnames that contain a specific banner
### Example
Look up the ports and services (if available) of the given IP-address
```sh
pyshodan.py --ip 8.8.8.8
```
Look up the IP, ISP, Country, ports and services for a specific domain
```sh
pyshodan.py --domain google.com
```
Look for a specific banner":
```sh
pyshodan.py --banner X-Forwarded-For
```
