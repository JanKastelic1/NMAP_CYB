import ipaddress

# Input and output file names
input_file = "Documents/inet_mask_output.txt"
output_file = "Documents/network_ips.txt"

# Open the output file for writing
with open(output_file, "w") as outfile:
    # Read the input file line by line
    with open(input_file, "r") as infile:
        for line in infile:
            # Only process lines that contain "inet" and "netmask" for IPv4 addresses
            if "inet " in line and "netmask" in line:
                # Split the line to extract IP and netmask
                parts = line.split()
                ip = parts[1]       # IP address is the second item
                netmask = parts[3]  # Netmask is the fourth item
                
                # Convert IP and netmask to network address with CIDR notation
                network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
                
                # Write the network address in CIDR notation to the output file
                outfile.write(f"{network}\n")

print(f"Network IPs saved to {output_file}")
