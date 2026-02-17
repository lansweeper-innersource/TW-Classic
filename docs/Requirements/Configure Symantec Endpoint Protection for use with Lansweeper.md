<!-- # Configure Symantec Endpoint Protection for use with Lansweeper -->
To pull data from the Linux, Unix, Mac and Windows computers, VMware servers and other devices in your network, Lansweeper queries a number of ports on the devices. A list of scanned ports can be found in [this knowledge base article](https://www.lansweeper.com/kb/20/used-TCP-ports.html). It is important to allow traffic from your Lansweeper server to these ports, to ensure a successful network scan.

Since the release of Lansweeper 6.0, Symantec Endpoint Protection in particular is prone to wrongly identifying Lansweeper traffic as port attacks on your devices. This may result in traffic being blocked and errors similar to the one below in your Symantec installation. Lansweeper 6.0 scans the same network device ports as previous Lansweeper releases, but does so more quickly to speed up scanning. Symantec identifies this sped up traffic as port attacks in some cases.

An easy way to prevent errors like the one below and to allow for a successful network scan is to whitelist all traffic coming from your Lansweeper server. More restrictive rules may work as well.

The client will block traffic from IP address <IP of Lansweeper server> for the next 600 seconds (from <date and time> to <date and time>)

## Whitelisting all Lansweeper traffic

To whitelist all traffic from the Lansweeper server in Symantec Endpoint Protection, do the following:

1. Open Symantec Endpoint Protection Manager.
2. Select the **Policies** tab.
3. Select the **Firewall** tab.  
   
4. Select the existing policy applied to your client machines on the right and choose **Edit the policy**. Alternatively, create a new policy to apply to your clients.

   
5. In the policy pop-up, select the **Rules** tab.
6. Select the **Add Rule...** button.

   
7. Give your rule a name, e.g. "Lansweeper". Select **Next** to continue.

   
8. Tick **Allow connections**. Select **Next** to continue.

   
9. Tick **All Applications**. Select **Next** to continue.

   
10. Tick **Any computer or site**. Select **Next** to continue.

    
11. Tick **All types of communication (all protocols and ports, local and remote)**. Select **Next** to continue.

    
12. Optionally, you can choose to have a log entry generated when a connection is made by the Lansweeper server. Select **Finish** to create the rule.

    
13. Once the rule has been created, double-click in the **Host** column and submit your Lansweeper server's IP address, to only apply the rule to traffic coming from your Lansweeper server.   
    In the example below, the IP address of the Lansweeper server is 192.168.1.50. Select **OK** several times to close all pop-ups and submit your changes.

    

    

    
