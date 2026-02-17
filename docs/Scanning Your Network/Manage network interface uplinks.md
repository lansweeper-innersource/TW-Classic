<!-- # Manage network interface uplinks -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_208/image_001.jpg) **This page explains how you can customize your uplink settings, rescan switches and how automated device scanning linked to uplinks works.**

When Lansweeper scans a router or switch using SNMP, it also tries to detect the assets connected to the device's network interfaces. Specifically, Lansweeper pulls a list of connected MAC addresses from SNMP OIDs on the router or switch.   
It also tries to match these connected MAC addresses with network devices already present in the Lansweeper database. If there is a match, the switch port not only shows the MAC address of the connected device but also a link to the device's Lansweeper webpage.

By default, if Lansweeper discovers more than 4 devices connected to a switch port, the port will be deemed to be an uplink. An uplink is a port on a router or switch that is designed to connect to another router, switch or internet access device.

In most cases, the label "uplink" will be correct for switch ports with more than 4 connected devices. However, there may be situations where you want to raise this setting. If you have a server connected to a port for instance, and that server is hosting lots of virtual machines, you may need to raise the uplink setting in order to see all connected devices on the port.

## Customize uplink setting

To customize when a switch port is deemed to be an uplink:

1. Go to the **Configuration > Server Options** menu of the web console.
2. In the **Switch scanning section**, change the amount of connected devices. The default value is 4 connected devices.  

   We recommend only raising the uplink setting as much as is required; submitting large values may impact performance.

## Rescan switches

Once you've changed the uplink setting, you must also rescan your switches. There are various ways to do this.

1. Go to the **Assets** section of the web console.
2. Filter the asset list for switches.
3. Select the switches and then select **Rescan asset(s)**.   
   Alternatively, if your switch's IP range is submitted for scanning under the **Scanning > Scanning Targets** menu, you could also rescan the range from that menu.

Once your switches have been rescanned, any additional connected devices that were detected on a port will be listed on the switch page, if the device count for the port does not exceed your uplink setting. If the device count for the port still exceeds what you've configured as your uplink setting, the port will still be considered an uplink.

![switch-uplink.png](/docs/.document360/assets/article_208/image_002.jpg)
