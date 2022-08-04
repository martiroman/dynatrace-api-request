# -*- coding: utf-8 -*-
#import DynaApi
import json
import requests

with open('/etc/dynatrace-integrations/config.json', 'r') as file: config = json.load(file)

def licencias():

    r = requests.get(config["DYNATRACE"]["API_URL"] + '/api/v2/metrics?metricSelector=builtin%3Abilling.%2A&Api-Token=' + config["DYNATRACE"]["API_TOKEN"]) #, json=json.loads(host.toJson()))

    return r.text.encode('utf-8')


def application(environ, start_response):
    status = '200 OK'
    peticion = environ['REQUEST_URI']

    #if peticion.startswith('/licencias'):
    output = licencias()

    response_headers = [('Content-type', 'application/json')]

    start_response(status, response_headers)

    return [output]

