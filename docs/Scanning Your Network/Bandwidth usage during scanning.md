<!-- # Bandwidth usage during scanning -->
Effective network management requires a balance between thorough data collection and efficient bandwidth usage. Although Lansweeper uses as much bandwidth as it can get by default, this guide delves into Lansweeper's bandwidth utilization across different scanning methods, providing practical insights and best practices to optimize your network scans.

On this page:

- SSH and SNMP scans
- Agent-based vs agentless scanning
- Maximum number of subnets per scan server
- Best practices for reducing bandwidth usage

## SSH and SNMP scans

In network management and monitoring, scanning tools such as SSH (Secure Shell) and SNMP (Simple Network Management Protocol) are commonly used to gather information about devices.

### SSH scans

SSH is widely used for accessing and managing network devices such as NAS (Network Attached Storage), routers, and switches. The payload size for SSH scans can vary significantly depending on the type of device being scanned and the amount of data gathered.

- **General payload size**: Between 5 KB and 500 KB.
- **Linux devices**: The payload can be up to 2 MB.
- **macOS devices**: The payload can be up to 1 MB.

### SNMP scans

SNMP is another protocol used for network management, commonly applied to routers, switches, printers, and scanners. Like SSH, the payload size for SNMP scans can vary based on the device and the amount of data collected.

- **General payload size**: Between 5 KB and 500 KB.
- **Custom OID scanning**: The payload size can increase as more specific data is gathered.

---

## Agent-based vs agentless scanning

Agent-based scanning is where you will install a small piece of software onto a Windows, Mac, or Linux computer to scan that specific device. Agentless scanning, on the other hand, does not involve installing any software on the target device. Instead, the scan server directly communicates with the device to gather data.

### Agent-based scanning

The agent collects data and compresses it before sending it to the scan server or a relay, reducing the overall bandwidth usage.

- **Compression**: gzip compression is used to reduce the size of scan results.
- **Bandwidth consumption**: Only consumes bandwidth when sending the compressed scan results to a scan server or the LsAgent relay.

### Agentless scanning

The agentless scanning method generally consumes more bandwidth as the data is not compressed and the connection remains open for the duration of the scan.

- **No compression**: Data found on the asset is not compressed, resulting in larger data transfers.
- **Extended bandwidth usage**: The communication between the scan server and assets is kept open while the scan is in progress, contacting multiple ports.

---

## Maximum number of subnets per scan server

A single scan server can handle a substantial number of simultaneous scans, though there is no strict maximum number of subnets defined. The practical limits depend on the server's configuration and the scanning schedule.

- **Simultaneous scans**: Up to 100 simultaneous scans can be handled by one scan server. This can be configured on your scan server via **Configuration > Scan server > Computer/IP threads**.
- **Subnets**: There is no defined maximum number of subnets. In theory, a scan server could scan the entire internet, though this would be time-consuming.

To efficiently distribute the scanning load, it's important to optimize your scanning schedule. For instance, you might configure your scan servers to target critical infrastructure during low-usage periods (e.g., weekends or early mornings), while scanning less critical workstations during regular business hours.

---

## Best practices for reducing bandwidth usage

- Reduce the number of scanning threads  
  The number of concurrent scans is determined by the **Computer Threads** and **IP Threads** values configured in the **Service Options** section of the **Configuration > Server Options**page in the web console.  

  Computer or IP thread changes won't take effect until you restart the **Lansweeper Server** service on your Lansweeper server.
- Scan your Windows, Linux and Mac computers with [LsAgent](/docs/introduction-to-lsagent-for-windows-linux-and-mac) instead  
  LsAgent scans locally, doesn't need to set up client connections and therefore generates a small amount of traffic for one full Windows computer scan. Windows computers can also be scanned locally with [LsPush](/docs/introduction-to-the-lspush-scanning-agent-for-windows) instead.
- Set up a Lansweeper installation with multiple scanning servers  
  A multi-scanning server setup allows for more efficient load balancing, as the scanning load and network traffic are divided among multiple machines.
- Disable scanning of any Windows data you're not interested in  
  This can be toggled in the **Scanning > Scanned Item Interval** section of the web console. The intervals can be increased as well, so data is scanned less frequently.
- Disable scanning of any Windows computer license keys, files and registry keys you're not interested in  
  This can be toggled in the **Software > License Key Settings** and **Scanning > File & Registry Scanning**sections of the web console.
- Use QoS on your WAN connections to throttle network traffic  
  This is recommended for Lansweeper as well as other applications.
