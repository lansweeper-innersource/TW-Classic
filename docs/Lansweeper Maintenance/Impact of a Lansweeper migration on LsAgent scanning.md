<!-- # Impact of a Lansweeper migration on LsAgent scanning -->
LsAgent is a cross-platform, lightweight scanning agent that you can install on Windows, Linux and Mac computers. It automatically collects an inventory from the computer it's installed on and sends the data back to your Lansweeper installation, either directly or through our relay server in the cloud. Data is securely sent to the relay server over HTTPS (TLS 1.2), stored in an encrypted format and deleted once a scanning server has retrieved it. More information on LsAgent can be found in [this knowledge base article](/classic/docs/introduction-to-lsagent-for-windows-linux-and-mac).

If you are scanning client machines using LsAgent and migrate your Lansweeper installation, there are some things to keep in mind to ensure your clients continue to successfully scan.

This article explains the impact of migrating the Lansweeper server that receives LsAgent scans, both for installations that connect to our LsAgent relay server and installations that receive LsAgent scans directly from client machines.

## Migration impact when using the relay server

When you first enabled the use of the relay server in the **Scanning > Relay Configuration** menu of your Lansweeper Classic installation, a relay authentication key was generated. This key is one of the properties used to uniquely identify your Lansweeper installation on the relay server. You submitted this key in the LsAgent installer on your client machines as well.

In addition to your relay authentication key, your Lansweeper license key and a unique identifier (GUID) generated during the setup of your Lansweeper installation are also used to uniquely identify your installation on our relay server.

Using these properties, the relay server can match LsAgent scans it receives from client machines to the correct Lansweeper installation.

### Ensure continuous data transfer via the relay for LsAgent clients after migration

- Make sure to keep your original Lansweeper license key applied to your installation after the migration.  In most cases, if you migrate your installation and Lansweeper database correctly, your license key will be automatically migrated as well.
- Ensure that your migrated installation effectively takes over LsAgent scan retrieval.
  1. Go to the **Scanning > Relay Configuration** menu of the migrated installation
  2. Select **Override Relay Access**.  
     

By following these steps, you can guarantee that your LsAgent clients continue sending data over the relay seamlessly after migrating your Lansweeper installation.

## Migration impact when not using the relay server

If your LsAgent clients are sending data directly to your Lansweeper installation, without going to the relay server first, there are still some things to keep in mind when migrating the installation.

When you installed LsAgent on your client machines, you submitted either the name or IP address of your Lansweeper scan server in the LsAgent installer. This is the server the clients are sending their data to. When you migrate your installation, that server name or IP address may change.

### Ensure continuous data transfer for LsAgent clients after migration

1. Leave your original Lansweeper installation running while you migrate to your new server.
2. Make sure your new server's firewall allows inbound connections over whichever port you configured as your listen port in the **Configuration > Server Options** section of the Lansweeper Classic web console.
3. Check the Server value listed in the LsAgent.ini file of one of your LsAgent installations, found at `Program Files (x86)\LansweeperAgent\LsAgent.ini`. This value will either be the name or IP address of your old server.
4. Choose one of the following options:
   - **Match server name or IP**  
     Give your new server the same name or IP address as is listed in your LsAgent.ini files, and update your DNS server to reflect this. That way no changes are required to your LsAgent installations themselves.
   - **Using the same external LansweeperDB**  
     If your old and new scan servers use the same external LansweeperDB:
     1. Go to the **Scanning > LsAgent Scanning** section of the Lansweeper Classic web console.
     2. Selectin **Link Scanserver** in the **Configuration** tab to link your new server to each LsAgent group in.
     3. Wait for this configuration change to sync down to your LsAgent clients, which may take up to 24 hours. The clients will start sending scanned data to the new server.
   - **Using the built-in LansweeperDB**If you are using the built-in LansweeperDB, choose one of the following:
     - Modify the new server IP and FQDN to match those of the old server.
     - Replace the Server value in the LsAgent.ini file with the new server values, and delete the lsagentconfiguration.xml file in all the assets scanned via LsAgent.

By following these steps, you can guarantee that your LsAgent clients continue sending data seamlessly after migrating your Lansweeper installation.

LsAgent clients that are down or disabled during the migration period won't receive the new server configuration. Their configuration will need to be updated manually by replacing the Server value in their LsAgent.ini file and purging their lsagentconfiguration.xml file. Alternatively, these agents can be uninstalled and then reinstalled with the correct Server value.
