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
                    [-v VERSION] [-f FILENAME]

Reads an SNMP table into a JSON String

optional arguments:
  -h, --help            show this help message and exit
  -c COMMUNITY, --community COMMUNITY
                        SNMP Community String (Default: public)
  -n HOSTNAME, --hostname HOSTNAME
                        SNMP Hostname (Default: 192.168.1.1)
  -p PORT, --port PORT  SNMP Port (Default: 161)
  -t TABLE, --table TABLE
                        SNMP Port (Default: ifEntry)
  -v VERSION, --version VERSION
                        SNMP Version (Default: 2)
  -f FILENAME, --file FILENAME
                        Save the results to a file (Default: print to screen)
```

## Example output

```
{
	"ifEntry": [{
		"oid_index": "1",
		"oid": "ifIndex",
		"value": "1",
		"snmp_type": "INTEGER"
	}, {
		"oid_index": "2",
		"oid": "ifIndex",
		"value": "2",
		"snmp_type": "INTEGER"
	}, {
		"oid_index": "3",
		"oid": "ifIndex",
		"value": "3",
		"snmp_type": "INTEGER"
	}, 
				{
		"oid_index": "4",
		"oid": "ifIndex",
		"value": "4",
		"snmp_type": "INTEGER"
	}, {
		"oid_index": "5",
		"oid": "ifIndex",
		"value": "5",
		"snmp_type": "INTEGER"
	}]
}
```
