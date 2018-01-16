import argparse
import json
from easysnmp import Session

_author_ = 'krisclarkdev'
_project_ = 'SNMP2JSON'

class SNMP2JSON:
    parser = argparse.ArgumentParser(description='Reads an SNMP table into a JSON String')

    def __init__(self):
        SNMP2JSON.parser.add_argument('-c', '--community',
                                        action='store', dest='community',
                                        help='SNMP Community String (Default: public)', default='public')

        SNMP2JSON.parser.add_argument('-n', '--hostname',
                                          action='store', dest='hostname',
                                          help='SNMP Hostname (Default: 192.168.1.1)', default='192.168.1.1')

        SNMP2JSON.parser.add_argument('-p', '--port',
                                          action='store', dest='port',
                                          help='SNMP Port (Default: 161)', default='161')

        SNMP2JSON.parser.add_argument('-t', '--table',
                                          action='store', dest='table',
                                          help='SNMP Port (Default: ifEntry)', default='ifEntry')

        SNMP2JSON.parser.add_argument('-v', '--version',
                                          action='store', dest='version',
                                          help='SNMP Version (Default: 2)', default=2)

        SNMP2JSON.parser.add_argument('-f', '--file',
                                          action='store', dest='filename',
                                          help='Save the results to a file (Default: print to screen)', default=None)

        SNMP2JSON.args = SNMP2JSON.parser.parse_args()

    def fetchTable(self):
        session = Session(hostname=SNMP2JSON.args.hostname + ':' + SNMP2JSON.args.port, community=SNMP2JSON.args.community, version=SNMP2JSON.args.version)
        system_items = session.walk(SNMP2JSON.args.table)

        data = []
        for item in system_items:
            oid = item.oid
            oid_index = item.oid_index
            snmp_type = item.snmp_type
            value = item.value

            test = {
                'oid': oid,
                'oid_index': oid_index,
                'snmp_type': snmp_type,
                'value': value
            }

            data.append(test)

        allData = {
            '' + SNMP2JSON.args.table: data
        }

        if(SNMP2JSON.args.filename == None):
            print json.dumps(allData, indent=4, sort_keys=True)
        else:
            with open(SNMP2JSON.args.filename, 'wt') as f:
                f.write(json.dumps(allData, indent=4, sort_keys=True))
            print 'JSON Flushed to ' + SNMP2JSON.args.filename

SNMP2JSON().fetchTable()
