from godaddypy import Client, Account
import sys
import urllib.request

# get external IP
print ("Getting external IP address...")
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

# domain and hostname to change: host.domain where host has no dot in it. Domain is the registered domain. So you can't nest subdomains.
hostname, domain = sys.argv[1].partition(".")[::2]

print(f"Updating {hostname} at {domain} to {external_ip}")

# godaddy api credentials
credentials = {}
with open("godaddy_credentials.ini") as f:
    for line in f:
        name, var = line.partition("=")[::2]
        credentials[name.strip()] = str(var).strip()

# Authenticate and get a client
my_acct = Account(api_key=credentials["dns_godaddy_key"], api_secret=credentials["dns_godaddy_secret"])
client = Client(my_acct)

# Check if the record exists to create it or update it
records = client.get_records(domain, 'A', hostname)

create = True
update = True

for r in records:
    create = False # it exists
    if r["data"] == external_ip:
        update = False # it is updated
        break

if create:
    print(f"The record needs to be created.")
    client.add_record(domain, {'name': hostname, 'ttl': 600, 'data': external_ip, 'type': 'A'})
elif update:
    print(f"The record exists but needs to be updated.")
    client.update_record_ip(external_ip, domain, hostname, 'A')
else:
    print(f"The record exists. Nothing to do.")

records = client.get_records(domain, 'A', hostname)
print(f"Final result: {records}")
