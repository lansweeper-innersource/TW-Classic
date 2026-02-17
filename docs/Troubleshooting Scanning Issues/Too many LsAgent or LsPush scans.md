<!-- # Too many LsAgent or LsPush scans -->
When you install LsAgent or set up LsPush, you can configure the agent to send data to one of your scan servers. A scan server configured by you can also retrieve relay data. While scan servers can handle many LsAgent and LsPush data, it's possible to overload a server with too much agent data.

If your server has less than 1 GB or less than 10% of available memory, the Lansweeper web console might display a warning notification.

To resolve this issue, you can:

- Direct agent scans to a different or new server
- Reduce the frequency or scope of your agent scans

## Direct agent scans to a different scan server

### LsPush

If you've integrated LsPush with a logon script, change the scan target in the logon script. Follow the instructions in [How to use the LsPush scanning agent in a group policy](/docs/scan-windows-computers-with-lspush-in-a-group-policy), but update the scan server you set in Step 4.

### LsAgent

If you're sending LsAgent scans directly to scan servers:

1. In the Lansweeper web console, go to **Scanning >LsAgent scanning**.
2. Select a group of LsAgent assets, then **Configuration**. Next, either:
   - Link additional scan servers by selecting **Link Scanserver**. For more information about adding scan servers, see [Setting up an installation with multiple scanning servers - Installation - Lansweeper Community](/docs/set-up-an-installation-with-multiple-scanning-servers).
   - Reorder the servers in the list. The LsAgent initially attempts to send scan data directly to the servers in the order you specify.

If no server can be reached directly and cloud relay access has been set up for LsAgent, LsAgent will try to send data to the relay.



### LsAgent cloud relay

Only one scan server can be configured to retrieve data from LsAgent's cloud relay server. You can configure which scan server in the **Scanning** **>** **Relay Configuration** section of the Lansweeper web console.

If the scan server retrieving data from the relay is overloaded, consider diverting more LsAgent scans directly to scan servers.

## Reduce the frequency or scope of your agent scans

### LsPush

If you've integrated LsPush with a logon script, change the scan target in the logon script. Follow the instructions in [How to use the LsPush scanning agent in a group policy](/docs/scan-windows-computers-with-lspush-in-a-group-policy), but reduce the number of machines the LsPush policy is applied to or change the scan trigger in your LsPush script.

### LsAgent

If you're sending LsAgent scans directly to scan servers:

1. In the Lansweeper web console, go to **Scanning >LsAgent scanning**.
2. Select a group of LsAgent assets, then **Configuration**.
3. Adjust the **Scan schedule** so that scans are run less frequently.



*If you can't find what you're looking for, create a post in our [Community Forum](https://community.lansweeper.com/t5/forum/bd-p/Lansweeper_General_Forum "Lansweeper community").*
