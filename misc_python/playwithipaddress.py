import ipaddress

# https://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xhtml

linkScopedUnicast = ipaddress.IPv6Network("fe80::/10")
print(linkScopedUnicast)
print(linkScopedUnicast[1])
print(linkScopedUnicast[-1])

