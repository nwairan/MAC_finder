# MAC Finder Script Documentation

The `MAC_finder.py` script is a Python script designed to search for a specific MAC address in the MAC address table of Cisco devices. It uses the `netmiko` library to establish SSH connections to network devices and retrieve the MAC address information. This documentation provides information on how to use the script and its functionality.

## Prerequisites

Before using the script, ensure that the following prerequisites are met:

1. Python: The script is written in Python, so you need to have Python installed on your system. You can download Python from the official Python website: [Python Downloads](https://www.python.org/downloads/).

2. Required Python Libraries: Install the necessary Python libraries using `pip`:

   ```bash
   pip install netmiko netaddr
   ```

3. Cisco Devices: You should have access to Cisco devices (e.g., Cisco routers or switches) that you want to search for MAC addresses on.

## Usage

To use the `MAC_finder.py` script, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where the script is located.

3. Run the script using the following command format:

   ```bash
   python MAC_finder.py <ip_list_file> <mac_address> <username> <password>
   ```

   - `<ip_list_file>`: Path to a text file containing a list of IP addresses of Cisco devices, with one IP address per line.

   - `<mac_address>`: The MAC address you want to search for. Enter it without any delimiters (e.g., `9C57AD3EC082`).

   - `<username>`: The SSH username for logging into the Cisco devices.

   - `<password>`: The SSH password for logging into the Cisco devices.

4. The script will iterate through the list of IP addresses, establish SSH connections to each device, and search for the specified MAC address in the MAC address table.

5. The script will print the results, including the hostname of the device and the output of the search.

6. Error messages, if any, will be logged in a file named `log.log` in the same directory as the script.

## Example

Here's an example of how to run the script:

```bash
python MAC_finder.py ip_list.txt 9C57AD3EC082 myusername mypassword
```

Make sure to replace `ip_list.txt` with the path to your IP list file and replace `myusername` and `mypassword` with the actual SSH credentials for your Cisco devices.

## Logging

The script logs any errors encountered during execution in a file named `log.log` located in the same directory as the script. You can review this log file for troubleshooting purposes.

## Note

- Ensure that the MAC address you provide as an argument is in the correct format. The script will convert it to Cisco-style MAC address format.

- The script uses the `netmiko` library for SSH connections, so make sure that the necessary network connectivity and SSH access are set up on your Cisco devices.

- Always handle sensitive credentials securely and avoid hardcoding them in your script for security reasons.

## Conclusion

The `MAC_finder.py` script provides a convenient way to search for a specific MAC address in the MAC address table of Cisco devices. By following the usage instructions and providing the required parameters, you can efficiently retrieve information about the presence of a MAC address on your network devices.
