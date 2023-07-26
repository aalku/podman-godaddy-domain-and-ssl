from godaddypy import Client, Account
import sys
import urllib.request

# get external IP
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

# domain and hostname to change: host.domain where host has no dot in it. Domain is the registered domain. So you can't nest subdomains.
hostname, domain = sys.argv[1].partition(".")[::2]

print(domain)
print(hostname)
print(external_ip)

# godaddy api credentials
credentials = {}
with open("godaddy_credentials.ini") as f:
    for line in f:
        name, var = line.partition("=")[::2]
        credentials[name.strip()] = str(var).strip()

# print(credentials)

# Authenticate and get a client
my_acct = Account(api_key=credentials["dns_godaddy_key"], api_secret=credentials["dns_godaddy_secret"])
client = Client(my_acct)

# Try to updatr and existing record
res = client.update_record_ip(external_ip, domain, hostname, 'A')

# Check if the record existed or else create it
records = client.get_records(domain, 'A', hostname)
if (len(records) == 0):
    client.add_record(domain, {'name': hostname, 'ttl': 600, 'data': external_ip, 'type': 'A'})
    records = client.get_records(domain, 'A', hostname)

print(records)
