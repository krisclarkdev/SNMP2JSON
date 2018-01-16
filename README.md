# SNMP2JSON
Python script that reads an SNMP table and outputs it to JSON

## Installation

```
git clone https://github.com/krisclarkdev/SNMP2JSON.git
cd SNMP2JSON
pip install argparse
pip install easysnmp
```

## Usage

Output to console

```
python ./snmp2json.py -c public -n 192.168.1.1 -p 161 -t ifEntry
```

Outout to file

```
python ./snmp2json.py -c public -n 192.168.1.1 -p 161 -t ifEntry -f ~/snmp.json
```

## Options

```
usage: snmp2json.py [-h] [-c COMMUNITY] [-n HOSTNAME] [-p PORT] [-t TABLE]

Reads an SNMP table into a JSON String

optional arguments:
  -h, --help            show this help message and exit
  -c COMMUNITY, --community COMMUNITY
                        SNMP Community String
  -n HOSTNAME, --hostname HOSTNAME
                        SNMP Hostname
  -p PORT, --port PORT  SNMP Port
  -t TABLE, --table TABLE
                        SNMP Port
```
