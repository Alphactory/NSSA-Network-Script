import os
from pythonping import ping
import netifaces

# clear terminal
os.system('cls' if os.name == 'nt' else 'clear')
print("\n")

# get default gateway
gateways = netifaces.gateways()
default_gateway = gateways['default'][netifaces.AF_INET][0]
print(f'default gateway: {default_gateway}')

#ping default gateway
print("pinging default gateway")
ping(default_gateway, verbose=True, count=1)

#ping remote address
print("pinging remote address")
ping("8.8.8.8", verbose=True, count=1)

#ping remote address with dns
print("pinging remote address with dns")
ping("google.com", verbose=True, count=1)

print("test complete.")