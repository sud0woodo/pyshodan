'''
Author: sud0woodo
Little python script to quickly look up information on an IP address, domain or banner.

NOTE: You will need a valid Shodan API key to perform the queries.
'''
import shodan
import argparse

API_KEY = "[INSERT API KEY]"
api = shodan.Shodan(API_KEY)

def ip_lookup(ip_address):
    try:
        ip = api.host(ip_address)
        print("IP: {}".format(ip['ip_str']))
        print("Country: {}".format(ip['country_name']))

        for data in ip['data']:
            print("Port: {}".format(data['port']))
            print("\tProtocol: {}".format(data['transport']))
            print("\tBanner: {}".format(data['product']))
    except shodan.APIError as e:
        print("API Error: {}".format(e))

def domain_lookup(domain_address):
    try:
        domain = api.search(domain_address)
        for data in domain['matches']:
            print("IP: {}".format(data['ip_str']))
            print("Domain: {}".format(u''.join(data['domains'])))
            print("Hostnames: {}".format(u''.join(data['hostnames'])))
            print("ISP: {}".format(data['isp']))
            print("Country: {}".format(data['location']['country_name']))
            print("Port: {}".format(data['port']))
            print("\tProtocol: {}".format(data['transport']))
            print("\tService: {}".format(data['product']))
            print("\tVersion: {}".format(data['version']))
    except shodan.APIError as e:
        print("API Error: {}".format(e))

def banner_search(query):
    try:
        query = api.search(query)
        print("Results found: {}".format(query['total']))
        for data in query['matches']:
            print("IP: {}".format(data['ip_str']))
            print("Port: {}".format(data['port']))
            print("Data: {}\n".format(u''.join(data['data']).encode('utf-8')))
    except shodan.APIError as e:
        print("API Error: {}".format(e))

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', help='IP address to lookup', dest='ip', required=False)
    parser.add_argument('--domain', help='Get information on domain', dest='domain', required=False)
    parser.add_argument('--banner', help='Search for specific banner', dest='banner', required=False)

    args = parser.parse_args()

    if bool(args.ip):
        ip_lookup(args.ip)
    elif bool(args.domain):
        domain_lookup(args.domain)
    elif bool(args.banner):
        banner_search(args.banner)
    else:
        print("Please provide a valid parameter, use -h to show help.")
