#!/usr/bin/env python3

# Script to output whitelisted IP addresses based on whitelisted domain names
doh_ipv4_blocklist = 'https://raw.githubusercontent.com/dibdot/DoH-IP-blocklists/refs/heads/master/doh-ipv4.txt'
doh_ipv6_blocklist = 'https://raw.githubusercontent.com/dibdot/DoH-IP-blocklists/refs/heads/master/doh-ipv6.txt'

whitelist_domains = [
  "mask-api.icloud.com",
  "mask-h2.icloud.com",
  "mask.icloud.com"
]

##

# processing function
import urllib.request
import operator

def processFile(inUrl, outFileName):
  with urllib.request.urlopen(inUrl) as inF:
      with open(outFileName, 'w') as outF:
        for line in inF:
          line = line.decode('utf-8')

          for domain in whitelist_domains:
            if operator.contains(line, domain):
                outF.write(line)
                break

# process ipv4
processFile(doh_ipv4_blocklist, 'whitelist-ip-doh-ipv4.txt')

# process ipv6
processFile(doh_ipv6_blocklist, 'whitelist-ip-doh-ipv6.txt')
