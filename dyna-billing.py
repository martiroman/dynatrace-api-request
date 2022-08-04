#!/usr/bin/env python
"""

"""
import json
import requests

with open('/etc/dynatrace-integrations/config.json', 'r') as file: config = json.load(file)

#####MAIN###############################################################################################################
def main():
    
    r = requests.get(config["DYNATRACE"]["API_URL"] + '/api/v2/metrics?metricSelector=builtin%3Abilling.%2A&Api-Token=' + config["DYNATRACE"]["API_TOKEN"]) #, json=json.loads(host.toJson()))
    
    print(r.text)

if __name__ == '__main__':
    main()