def validate_ip(ip_address):
    octets = ip_address.split('.')
    
    if len(octets) != 4:
        return False
    
    for octet in octets:
        if not octet.isdigit() or not (0 <= int(octet) <= 255):
            return False
    
    return True

valid_ips = ["192.168.0.1", "127.0.0.1"]
invalid_ips = ["256.100.50.0", "192.168.0", "192.168.0.256", "abc.def.ghi.jkl"]

for ip in valid_ips:
    print(f"{ip} is valid: {validate_ip(ip)}")

for ip in invalid_ips:
    print(f"{ip} is valid: {validate_ip(ip)}")
