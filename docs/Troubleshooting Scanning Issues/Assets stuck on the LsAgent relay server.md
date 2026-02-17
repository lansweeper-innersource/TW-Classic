<!-- # Assets stuck on the LsAgent relay server -->
Lansweeper provides the [LsAgent](/docs/introduction-to-lsagent-for-windows-linux-and-mac) to scan your data. While configuring the LsAgent to contact the relay, the following errors may occur:

- The relay could not be contacted.
- An unexpected error occurred while contacting the relay.

![the-relay-could-not-be-contacted-1.jpg](/docs/.document360/assets/article_250/image_002.jpg)

To resolve the relay server connection failure, do the following:

1. Make sure your Lansweeper server has Internet access.
2. If your Lansweeper server accesses the Internet through a proxy server, make sure you've submitted your proxy settings in **Configuration > Server Options**.
3. Make sure outbound traffic on your Lansweeper server is not blocked by a firewall, anti-virus program, or other software. Your scanning server must be able to make an outbound connection to port 443 of lsagentrelay.lansweeper.com.
4. Make sure TLS 1.2 is enabled on your Lansweeper server, as the relay server requires communication through this protocol.
5. Make sure you've only used your Lansweeper license key in a single Lansweeper installation to request relay access. Using the same key for relay access in a second installation is not allowed and will result in you being asked to take over relay access from your first installation.
6. Try enabling relay access again in **Scanning > Relay Configuration**
7. If the issue persists, look for relay-related errors in the log file below, which can be found on your Lansweeper server. The sample errors below are caused by an internet access issue, proxy server and TLS misconfiguration, respectively.  
    `Program Files (x86)\Lansweeper\Service\Errorlog.txt`

   ERROR could not sync asset scans from Relay System.ServiceModel.EndpointNotFoundException: There was no endpoint listening that could accept the message. This is often caused by an incorrect address or SOAP action. See InnerException, if present, for more details. ---> System.Net.WebException: The remote name could not be resolved.

   ERROR could not sync asset scans from Relay System.ServiceModel.EndpointNotFoundException: There was no endpoint listening that could accept the message. This is often caused by an incorrect address or SOAP action. See InnerException, if present, for more details. ---> System.Net.WebException: The remote server returned an error: (407) Proxy Authentication Required.

   INFO Error while refreshing config An error occurred while making the HTTP request. This could be due to the fact that the server certificate is not configured properly with HTTP.SYS in the HTTPS case. This could also be caused by a mismatch of the security binding between the client and the server.

2.11.0.0

2.11.0.0

2.11.0.0

2.11.0.0
