<!-- # Configure Network Discovery -->

Lansweeper's Network Discovery enables you to discover all IT and OT assets within your network. By utilizing the necessary discovery credentials, Network Discovery gathers all asset details both on the local machine and on remote IT assets.

To learn more about installing Network Discovery, see [Install Network Discovery](/docs/install-network-discovery).

You can configure the discovery settings for Network Discovery from within your Lansweeper Site, allowing you to determine what to scan and when the scans should take place.

For more information about the discovery menu, see [Discovery configuration](/docs/overview-of-discovery-components-and-configuration).

### Create a new Network Discovery action

Before creating a new Discovery action, make sure your sensors have access to the necessary ports on the targeted assets. For more information, check out [Ports scanned or used by Lansweeper](/docs/ports-scanned-or-used-by-lansweeper).

1. In your Lansweeper Site, go to **Discovery (or Scanning) > Discovery actions**.
2. Select **Add new action**.
3. In the pop-up, select the **Agent-less** action type and choose **Add action**.
4. Enter a name and description for your action.
5. Select **Target**.
6. In the pop-up, enter a target you want to discover.   

   A target can be an IP address, an IP range, an FQDN, a machine name, an AD domain, or an SCCM server.
7. Select **Save target**.
8. Select **Manage sensors**.
9. In the pop-up, select the sensors that should be used for the discovery.   

   An IT sensor collects details from IT devices, such as workstations, servers, routers, and switches.   
   An OT sensor returns data from OT devices, including programmable logic controllers (PLCs), remote terminal units (RTUs), and industrial control systems (ICS). Find out more information over at [Operational Technology Security and Asset Management Solution](https://www.lansweeper.com/blog/ot/operational-technology-security/).
10. Select **Close**.
11. Optionally, select **Credentials**.  

    Add credentials to a Network Discovery action to gather even more asset details.
12. In the pop-up, select a credential to use for the discovery.
13. Select **Close**.
14. Select **Create new trigger**.
15. In the pop-up, select a time and date for the trigger, and enter a name.
16. Select **Save trigger**.
17. Select **Save and exit**.

### Manage Network Discovery actions

1. In your Lansweeper Site, go to **Discovery (or Scanning)****> Discovery actions**.
2. Select the discovery action you want to edit.
3. In the **Agent-less action detail** view, manage your targets, exclusions, sensors, triggers, or credentials.
4. Select **Save and exit**.

### Create Discovery credentials

Configure credentials for your discovery. Add credentials so the sensors can pick up more details when discovering your assets.

1. In your Lansweeper Site, go to **Discovery (or Scanning)****> Discovery Credentials > Add new credential.**
2. Enter a display name that identifies the credential.
3. Choose the vault(s) which should have access to the credential.
   - A vault is on-premise on the hub and stores the encrypted credentials at rest.
   - The vault only shares relevant credentials encrypted in transit with its linked sensors when the discovery action runs.
4. Choose the types which are valid for this credential. One credential can be reused for multiple purposes, such as a Domain account for Windows and SSH.
5. Fill in the corresponding credentials parameters.
6. Select **Save and exit**.

When adding an SSH credential for remote discovery of Unix/Linux based devices, make sure to optimize the `sudoers` file on the target device.

To optimize the `sudoers` file on the target device:

1. On the Unix/Linux based device, open the `sudoers` file by entering the `sudo visudo` command.   
   Enter your password if prompted.
2. Use the arrow keys to navigate to the bottom of the file.
3. Select **i** to enter insert mode, and select **Enter** to insert a new line.   
   Do not remove existing lines from the file. Instead, add **#** to the start of a line to ignore that line. This ensures no information is accidentally deleted.
4. Add the following line to the file, replacing `lansweeperdiscoveryuser` with the SSH user you configured in your Lansweeper Site for remote discovery:  

   ```
   lansweeperdiscoveryuser ALL=(root) NOPASSWD: /usr/sbin/dmidecode, /usr/sbin/lspci, /usr/sbin/lshw, /usr/bin/lshw, /usr/sbin/hwinfo, /usr/sbin/lvs, /usr/sbin/pvs, /usr/sbin/vgs, /usr/sbin/smbios, /sbin/smbios
   ```
5. Select **Esc** to exit insert mode.
6. Type **:wq** and select **Enter** to save your changes and exit `visudo`.

## Create or edit Discovery groups

Discovery groups help manage the operational settings of your discovery systems, like the Network Discovery hubs and sensors, and your IT Agents.

You can manage, for instance, the frequency of updates, auto-update behaviour, and network visibility.

For more information, see [Discovery groups](/docs/overview-of-discovery-components-and-configuration#groups).

### Configure Network Visibility for Network Discovery

Network visibility allows your sensors to detect assets passively using sensor network interfaces. Enabling visibility will put your interfaces in a promiscuous mode so all broadcasted messages are parsed to identify source and destination MAC and IP addresses.

We recommend leaving this option enabled so you also get details on unknown assets.

1. In your Lansweeper Site, go to **Discovery (or Scanning)****> Discovery Groups**.
2. Select **Default Group**. This discovery group manages your Network Discovery hubs and sensors by default.
3. To enable or disable the network visibility, select the **Network visibility** toggle.
4. Select **Save and exit**.

### Configure Auto Update for Network Discovery or IT Agent

1. In your Lansweeper Site, go to **Discovery (or Scanning)****> Discovery Groups**.
2. Select **Default Group**. This discovery group manages your Network Discovery hubs and sensors by default.
3. To pause or resume the auto-updates, select the **Pause auto-update** toggle.
4. To choose a schedule for the auto-updates, select the days and the specific time for the updates.
5. Select **Save and exit**.
