<!-- # The relay could not be contacted -->
[Lansweeper](https://www.lansweeper.com/) includes a scanning agent called LsAgent. LsAgent is a cross-platform, lightweight program that you can install on Windows, Linux and Mac computers and that automatically collects an inventory from the computer it's installed on.

LsAgent sends scanned data back to your Lansweeper installation, either directly or through our relay server in the cloud. Data is securely sent to the relay server over HTTPS, stored in an encrypted format and deleted once a scanning server has retrieved it. Thanks to the relay server connectivity, LsAgent can even scan computers outside of your network and over the Internet. An introduction to LsAgent can be found in [this knowledge base article](/classic/docs/introduction-to-lsagent-for-windows-linux-and-mac).

In order for LsAgent to send scanned data back to your Lansweeper installation through the cloud relay server, relay access must first be enabled in the **Scanning > Relay Configuration** section of the Lansweeper web console.   
If setting up access to the cloud relay server fails, the page may return an error similar to:

An unexpected error occurred while contacting the relay.

Other errors you could run into include:

- ERROR could not sync asset scans from Relay System.ServiceModel.EndpointNotFoundException: There was no endpoint listening that could accept the message. This is often caused by an incorrect address or SOAP action. See InnerException, if present, for more details. ---> System.Net.WebException: The remote name could not be resolved.
- ERROR could not sync asset scans from Relay System.ServiceModel.EndpointNotFoundException: There was no endpoint listening that could accept the message. This is often caused by an incorrect address or SOAP action. See InnerException, if present, for more details. ---> System.Net.WebException: The remote server returned an error: (407) Proxy Authentication Required.
- INFO Error while refreshing config An error occurred while making the HTTP request. This could be due to the fact that the server certificate is not configured properly with HTTP.SYS in the HTTPS case. This could also be caused by a mismatch of the security binding between the client and the server.

There are several possible causes for these errors, the most basic one being that your Lansweeper server does not have internet access.



## Resolve the relay server connection failure

1. Make sure your Lansweeper server has internet access.
2. If your Lansweeper server accesses the internet through a proxy server, make sure you've submitted your proxy settings in the following section of the web console: **Configuration > Server Options**.
3. Make sure outbound traffic on your Lansweeper server is not blocked by a firewall, anti-virus program or other software. Your scanning server must be able to make an outbound connection to port 443 of lsagentrelay.lansweeper.com.
4. Make sure TLS 1.2 is enabled on your Lansweeper server, as the relay server requires communication through this protocol.
5. Make sure you've only used your Lansweeper license key in a single Lansweeper installation to request relay access. Using the same key for relay access in a second installation is not allowed and will result in you being asked to take over relay access from your first installation.
6. Try enabling relay access again under **Scanning > Relay Configuration**.
7. If the issue persists, look for relay related errors in the **Errorlog.txt** file, which can be found at `Program Files (x86)\Lansweeper\Service\Errorlog.txt` on your Lansweeper server. The sample errors below are caused by an internet access issue, proxy server and TLS misconfiguration, respectively.
