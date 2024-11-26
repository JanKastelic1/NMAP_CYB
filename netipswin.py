import ipaddress
import os
import subprocess

# Input and output file names
home_dir = os.path.expanduser("~")
input_file = os.path.join(home_dir, "Documents", "ipconfig_output.txt")
output_file = os.path.join(home_dir, "Documents", "network_ips.txt")

# Run ipconfig and save output to a file
with open(input_file, "w") as f:
    subprocess.run(["ipconfig"], stdout=f, text=True)

# Open the output file for writing
with open(output_file, "w") as outfile:
    # Read the ipconfig output file line by line
    with open(input_file, "r") as infile:
        lines = infile.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            if "IPv4 Address" in line:  # Match IPv4 Address line
                ip = line.split(":")[1].strip()
                # Find the corresponding subnet mask
                netmask_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
                if "Subnet Mask" in netmask_line:
                    netmask = netmask_line.split(":")[1].strip()
                    # Convert IP and netmask to network address with CIDR notation
                    network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
                    # Write the network address in CIDR notation to the output file
                    outfile.write(f"{network}\n")

print(f"Network IPs saved to {output_file}")
