<!-- # Online status indicator -->
If you access an asset's Lansweeper webpage, you'll notice an online status indicator right below the asset name and next to the IP address. Ping statuses are also added when you've clicked **Ping Assets** in asset overviews.

These online status indicators are based on a ping request performed from the server hosting your Lansweeper web console to the client asset. If the asset is a Windows computer, the NetBIOS name (e.g. REDBERRY) is pinged; if the asset is not a Windows computer, the IP address is pinged.

The ping requests are performed on demand when you open the asset's Lansweeper webpage or select the **Ping Assets** button in overviews. This data isn't stored in the Lansweeper database.

The online status icon has 4 possible colors or values:

-  Gray: indicates that the online status indicator is still loading and that the ping request hasn't been completed yet.
-  Green: indicates that a ping response was received from the client machine and that the machine is online.
-  Red: indicates that a ping response was not received from the client machine or that the machine is offline.
-  Orange: indicates that the client machine is offline, but that a ping response was received from vPro features configured on the machine. vPro is a technology offered by Intel that allows for remote access to offline machines.

Lansweeper compares the TTL value set in the client machine's registry with the TTL value of the ping response to determine whether vPro is enabled.

## More information on pings

Pings are performed from the server hosting the Lansweeper Classic web console, not from the server hosting the scanning service. It is possible for a client machine to be successfully scanned but have a red status indicator, i.e. if your scanning service and web console are on different machines and the client machine is not pingable from the web server.

Pings are performed to the client machine's NetBIOS name (in case of a Windows computer) or IP address (in case of a non-Windows asset). If the client machine is a Windows computer and its name cannot be resolved from the Lansweeper Classic web server, this will result in a ping failure and red status indicator. For Windows computers, DNS resolution must be successful from the web server to get accurate status indicator results.
