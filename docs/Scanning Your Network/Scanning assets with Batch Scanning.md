<!-- # Scanning assets with Batch Scanning -->

Batch Scanning is an agentless, on-demand scanning method that allows you to quickly scan any IP addresses, IP ranges or DNS names of client machines submitted by you. It is suitable for scanning Linux, Unix, Mac and Windows computers, VMware servers and other network devices. Some examples of network devices are: cameras, firewalls, mail servers, music systems, NAS devices, printers, routers, switches, UPS devices, VOIP phones and web servers.

Windows computers submitted for Batch Scanning can belong to a domain or a workgroup. You can submit an unlimited number of IP addresses, IP ranges and DNS names in the **Batch Scanning** tab of the **Scanning > Scanning Targets**page in the web console. Make sure to separate multiple entries using line breaks, commas or semicolons. If you have multiple scanning servers, there will be separate configuration tabs on the **Scanning Targets** page, one for each server.





As agentless scanning of Linux, Unix, Mac and Windows computers, VMware servers and SNMP enabled network devices requires credentials, make sure to submit and map your scanning credentials as well, by following the instructions in [this knowledge base article](/docs/create-and-map-scanning-credentials). Batch Scanning uses global and mapped credentials just like other scanning methods.

Assets submitted for Batch Scanning are moved to the top of the scanning queue, if they are not already in the queue. Their scans are given priority, so you can see the scan results more quickly.

## Batch Scanning settings

- **Upload file**: use this button to submit your IP addresses, IP ranges and DNS names of client machines through an import file, instead of having to manually submit them. Accepted file formats are .csv and .txt.
- **Scan now**: use this button to start your scan after you've submitted the items to be scanned in the input box below. You will see a message indicating that your assets were added to the scanning queue.
- **Clear text**: use this button to clear any items you've submitted in the input box, in case you made some mistakes and want to start over.
- **Ping targets**: if checked, Lansweeper will ping the assets you've submitted and only scan those that respond to the ping request. If unchecked, Lansweeper will try to scan all assets you've submitted, regardless of whether they can be pinged.

  Unchecking **Ping targets** will slow down scanning, so it is generally recommended that you only uncheck this if you have assets that don't respond to ping requests.
