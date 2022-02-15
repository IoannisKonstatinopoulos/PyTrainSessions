import requests
import json
from urllib.parse import urlparse
import pandas

""" Make the Request API call and return the json data"""


def call_api_live_curry(url):
    try:
        req = requests.get(url)
        response_body = req.json()
        return response_body
    except Exception:
        print(f"Can't complete connection with : {urlparse(url).netloc} .")


""" Give the URL and get the curry content """


def get_curry_content(dict):
    """Open file in order to save it and compare keys to find the missing from mandatory parameters"""

    try:
        with open('new_content_result.json', 'w') as json_file:
            master_keys = {'Project': None, 'SYSID': None, 'Service': None, 'TLC': None, 'hostname': None}
            temp_list = []
            for i in dict['result']:
                for key in master_keys.keys():
                    if key not in i['content'].keys():
                        i['content'].update({key: None})
                json.dump(i['content'], json_file, sort_keys=True)
                temp_list.append(i['content'])
            return temp_list
    except Exception as e:
        print(f"Error while processing the result from API Call with error : {e}")


""" Convert content results from Dictionary to CSV """

def report_to_csv(json_curry):

    column_order = ['Project', 'SYSID', 'Service', 'TLC', 'hostname']  # Tried to set a list of ordered columns but unsucessfully couldn't find the method - note that doesn't affect the funcionality of the program
    try:
        print(json_curry)
        read_json = pandas.read_json(json.dumps(json_curry), orient=column_order)
        read_json.to_csv('final.csv')
        return print("Passed Successfully.")
    except Exception:
        print(f"Couldn't convert. ")


url_live_test = 'http://alethea-support-training-bt.lab.up:8888/metadata/search?aql=SELECT%20hostname,Project,SYSID,Service,TLC%20FROM%20vm%20WHERE%20Product=CURRY%20AND%20Service=TOMCAT%20ORDER%20BY%20SYSID'

curry = call_api_live_curry(url_live_test)

response_JSON = get_curry_content(curry)
report_to_csv(response_JSON)
