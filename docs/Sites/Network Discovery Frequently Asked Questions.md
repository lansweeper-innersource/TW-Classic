<!-- # Network Discovery: Frequently Asked Questions -->

Lansweeper's Network Discovery enables you to discover all IT and OT assets within your network. If you'd like to learn more about Network Discovery, head on over to [Install Network Discovery](/docs/install-network-discovery).

## Frequently asked questions (FAQ)

- Can I install "(full) Network Discovery" on a machine that already has "OT Network Discovery"?
- During the installer I get the message: “There has been an error. Could not start Lansweeper IT Netw...
- What are the installer return codes and possible error messages?
- Why am I not seeing all asset data (yet)?
- How do I solve duplicate issues?
- Can I unlink the Network Discovery from my Lansweeper Site?
- Can I reset or change the password from my Network Discovery Hub?
- I’m not seeing an asset for IT Agent/Network Discovery in my inventory. Why is it not appearing?
- How can I deal with the license limit when using Lansweeper Discovery in Configuration > License sta...
- I’m currently using Lansweeper On-premises with Lansweeper Site. Can I use Lansweeper Discovery in t...
- How do I avoid duplicates when using Lansweeper Discovery together with Lansweeper On-Premises in my...
- My discovery results aren’t showing up in my Lansweeper Site, how can I troubleshoot this?
- If I want to move from Lansweeper On Prem to Lansweeper Discovery but have thousands of manually cre...
- How many Network Discovery IT/OT sensors should I deploy? Does Network Discovery have load balancing...
- Can I install Lansweeper Network Discovery on Linux box?
- If I have two hubs installed and the credentials are saved to the first hub, are they only used for ...
- Why is my Network Discovery installed on Linux only reporting back recognition data but no detailed ...
- What is the packet size of the message Lansweeper sends to the assets for discovery, and what can be...
- Do the Network Discovery hub and/or sensor update automatically on Linux?
- Why does the installation of Network Discovery fail with “Unable to initialize installer” on Windows...
- How are the credentials handled in rest and in transit when using Network Discovery?
- How can I backup Network Discovery?

### Can I install "(full) Network Discovery" on a machine that already has "OT Network Discovery"?

Yes, these can be ran on the same machine.

### During the installer I get the message: “There has been an error. Could not start Lansweeper IT Network Discovery Hub Service. The application will exit now.” How can I solve it?

We've observed that this process may run slower on certain machines. The slowdown could be due to factors such as a slow hard disk, low memory, or limited CPU resources. We are currently investigating the root cause of this issue.

To resolve this message during the installation:

1. Press **Windows + R** to open **Run**.
2. Enter **regedit** to open the **Registry Editor**.
3. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control` or copy-paste the location in the navigation bar.
4. In the **Control registry** folder, move to the right side and create a new DWORD (32-bit) Value called “ServicesPipeTimeout”.
5. In the **Edit Value** window, change the **Base** to **Decimal**.
6. In the **Value Data** field, enter a value of “600000”.
7. Select **OK**.
8. Exit the Registry Editor and restart your system.Failing to restart will prevent the changes from being applied.
9. After restarting, run the Network Discovery installer.

### What are the installer return codes and possible error messages?

When the installer terminates with an exit code during the pre-installation phase, no actions have been executed with no files or changes left behind.

In the event the installer terminates during the installation, a rollback will occur and no files or changes will be left behind.

The ranges are the following:

- **0** (zero) will be returned when the installer finished as expected, without issues.
- **20-39** range: issues regarding OS, installer or current installation (pre-installation)
- **40-59** range: issues regarding user input (pre-installation)
- **60-79** range: issues during installation (removing the installation)
- **80-99** range: warnings during installation (keeping the installation)

| Exit Code | Description | Position |
| --- | --- | --- |
| 0 | The installer finished with success. |  |
| 20-39 | Issues regarding OS, installer, or current installation. | Pre-installation |
| 20 | Another installation is already in progress. Please finish that installation before starting a new one. |  |
| 21 | This installer is being run on an unsupported operating system. Please update your OS if possible. |  |
| 22 | The existing installation is newer than the version you want to install. Installer will be closed. |  |
| 40-59 | Issues regarding user input. | Pre-installation |
| 40 | You must accept the terms of use before continuing with the installation. Please use the accepteula parameter for this. |  |
| 41 | A valid linking code to your Lansweeper Site is required to continue. Please use the cloudtoken parameter for this. |  |
| 42 | A valid proxy configuration is required to continue with the installation. Please use both the proxyserver and proxyport parameters (or none). |  |
| 43 | A valid proxy port is required to continue with the installation. Please use the proxyport parameter correctly. |  |
| 44 | No module was selected to be installed. Installer will be closed. |  |
| 60-79 | Issues during the installation (installation will be rolled back). | Installation |
| 60 | PowerShell script execution is not enabled on your computer. Ensure your computer is configured to allow PowerShell script execution. |  |
| 61 | A link to your Lansweeper Site could not be made. (IT Agent only) |  |
| 62 | A required component service could not be started. |  |
| 80-99 | Warnings during installation (installation will be kept). | Installation |
| 80 | The installation succeeded but a link to your Lansweeper Site could not be made. (Network Discovery only) |  |

When using the MacOS PKG, the installer command only returns 0 (success) or 1 (general error). To get the specific exit code similar to the list above, this extra log file is available at `/tmp/Lansweeper-Network-Discovery_exitcode.log`.   
This file only contains the specific exit code as an integer value.

### Why am I not seeing all asset data (yet)?

We’re remapping all data to a universal data model. As we’re doing this in phases, you’ll only see certain data sections available on the asset page.

Currently, these sections are available:

- HW
- Operating System
- Software
- Monitor

This list is continuously being extended.

### How do I solve duplicate issues?

1. In your Lansweeper Site, go to **Scanning > Discovery systems**.
2. Select **Agent-less**.
3. Select the Network Discovery installation.
4. Select **Delete**.
5. Select **Yes**.

### Can I disable the auto-update behavior?

Auto update is enabled by default in an 8 hour time window varying between 08:00 am and 06:00 pm. Though not recommended, you can still disable the auto-update behavior after installation by running the following command on the machine running Network Discovery:

```
sc config "Lansweeper Network Discovery Update service" start= disabled sc stop "Lansweeper Network Discovery Update service"
```

You can also disable auto-updates for specific groups in your Lansweeper Site by following these steps:

1. In your Lansweeper Site, navigate to **Scanning > Discovery groups**.
2. Select the Discovery group.
3. Enable the **Pause auto-update** toggle.

This will prevent the group's Discovery Systems from applying updates automatically, although currently, updates will still be downloaded.

To block downloads entirely in the meantime, you can block outgoing connections by executing the following steps:

1. Run the command below to verify the download IPs:

   ```
   nslookup download.lansweeper.com
   ```

   This should return:
   - 18.239.208.15
   - 18.239.208.60
   - 18.239.208.83
   - 18.239.208.108
2. Block the IP addresses by executing the following firewall rules:

   ```
   netsh advfirewall firewall add rule name="Block auto-update Lansweeper" dir=out action=block remoteip=18.239.208.15 enable=yes
   netsh advfirewall firewall add rule name="Block auto-update Lansweeper" dir=out action=block remoteip=18.239.208.60 enable=yes
   netsh advfirewall firewall add rule name="Block auto-update Lansweeper" dir=out action=block remoteip=18.239.208.108 enable=yes
   netsh advfirewall firewall add rule name="Block auto-update Lansweeper" dir=out action=block remoteip=18.239.208.83 enable=yes
   ```

This will still allow access to discovery-gateway.lansweeper.com, which is needed for data synchronization.

Please note that your Lansweeper Site requires a minimum version of Network Discovery to maintain synchronization. To that end, we recommend to re-enabling the auto-update feature when possible.

### Can I unlink the Network Discovery from my Lansweeper Site?

Yes, you can:

1. In your Lansweeper Site, go to **Scanning > Discovery systems**.
2. Select **Agent-less**.
3. Select the Network Discovery installation.
4. Select **Delete**.
5. Select **Yes**.

After unlinking, Network Discovery will continue to scan, and will keep trying to send its data to your Lansweeper Site. To avoid this from happening, we recommend you uninstall Network Discovery on the machine it was installed on. We’re looking to automate this process so you don’t have to manually uninstall Network Discovery installations you no longer want to track.

### Can I reset the password from my Network Discovery Hub?

Yes, you can:

1. Navigate to the hub installation directory (default path:   
   `C:\Program Files\Lansweeper Network Discovery\hub`).
2. Right-click AuthenticationTool.exe and select **Run as administrator**.
3. Choose to either enable or disable authentication:
   - **Enable Authentication:** This option will prompt you to set a new password for the hub, which will be required the next time you access it.
   - **Disable Authentication:** This option removes the password requirement. Only disable authentication to reset your password. If you disable authentication, we strongly recommend re-enabling it as soon as possible to maintain the security of your hub.

### I’m not seeing an asset for IT Agent/Network Discovery in my inventory. Why is it not appearing?

Some ports may not be open, or specific access might be missing between your sensor and the asset.

To verify if a port is not open, or if access is missing:

1. Open the Lansweeper Network Discovery hub UI (hosted at [https://localhost:59525](https://localhost:59525/ "https://localhost:59525") by default).
2. Go to **Discover now**.
3. Enter the IP address/FQDN/machine name of the asset.
4. Optionally, enter any credentials.
5. Start the discovery.

The result will appear in Discovery results where you can for instance compare the open ports to [this list](/docs/ports-scanned-or-used-by-lansweeper "/docs/ports-scanned-or-used-by-lansweeper"), to see if any required ports are missing.

### How can I deal with the license limit when using Lansweeper Discovery in Configuration > License status?

If you are using Lansweeper IT Agent Discovery, Network Discovery, or Cloud Discovery in your Lansweeper Site, you may encounter warning messages when you approach or exceed your license limit.

While assets discovered through these Discovery systems are counted toward your licensed asset total, exceeding the limit will not immediately restrict access to insights—this will only happen once our Lansweeper Site subscription process is finalized.

### I’m currently using Lansweeper On-premises with Lansweeper Site. Can I use Lansweeper Discovery in the same Lansweeper Site?

Yes, you can but be aware duplicates are still likely to occur.

Please refer to the next section for guidance on managing duplicates when using both Lansweeper On-premises and Lansweeper Discovery within the same site.

### How do I avoid duplicates when using Lansweeper Discovery together with Lansweeper On-Premises in my Lansweeper Site?

In this hybrid scenario where you use Lansweeper IT Agent Discovery, Network Discovery, or Cloud Discovery together with Lansweeper On-premises in a single Lansweeper Site, we recommend either of the following options:

#### Option 1

1. Use Lansweeper Discovery on parts of your network not yet scanned by Lansweeper On-premises.
2. Set up discovery exclusions: go to **Scanning > Discovery actions**, and add exclusions to your**Agentless actions** to ensure specific assets aren’t discovered by Lansweeper Network Discovery.
3. Resolve duplicates manually by going to **Inventory > Duplicate conflicts**.

#### Option 2

If the above is not an option:

1. Remove Network Discovery from your Lansweeper Site:
   1. Go to **Scanning > Discovery systems > All systems**.
   2. Select the relevant Network Discovery system.
   3. Select **Delete system**.
2. Create a new site and link it to your Network Discovery:
   1. Create a new site using [this link](https://app.lansweeper.com/create-site?path= "https://app.lansweeper.com/create-site?path="), or by selecting **Change site > Create new site**.
   2. In your new site, select **Access empty site**.
   3. Go to **Scanning > Discovery systems**, and select**Link discovery system**.
   4. In the pop-up, select **Create new code**.
   5. Select an expiration period, select **Apply** and **Copy code**.
   6. Open the Lansweeper Network Discovery hub UI (hosted at [https://localhost:59525](https://localhost:59525/ "https://localhost:59525") by default) and select **Lansweeper Site Link Overview**.
   7. Select **Unlink from Lansweeper Site**.
   8. Finally, select **Linking options**, and use your newly created code to link the Hub to your new Lansweeper Site.

### How do I convert from Lansweeper On-Premises to Lansweeper Network Discovery (and vice versa)?

Both Lansweeper On-Premises and Lansweeper Network Discovery can work alongside one another; you don’t convert one into the other, as you can install and uninstall both independently.

- Remove a Lansweeper On-premises installation from your Lansweeper Site: check out [Remove an installation from your site](/docs/remove-an-installation-from-your-cloud-site#:~:text=In%20your%20cloud%20site%2C%20go,data%20or%20Remove%20all%20data. "/docs/remove-an-installation-from-your-cloud-site#:~:text=In%20your%20cloud%20site%2C%20go,data%20or%20Remove%20all%20data.").
- Remove a Lansweeper Network Discovery system from your Lansweeper Site: check out [Install Network Discovery](/docs/install-network-discovery#remove).
- Link a Lansweeper On-premises installation to your Lansweeper Site: check out [Link Lansweeper On-prem with Lansweeper Sites](/docs/link-lansweeper-on-prem-with-lansweeper-sites "/docs/link-lansweeper-on-prem-with-lansweeper-sites").
- Link a Lansweeper Network Discovery system to your Lansweeper Site: check out [Install Network Discovery](/docs/install-network-discovery#linkdiscovery).

### How do I prevent Lansweeper Network Discovery from automatically adding assets to the inventory?

Lansweeper Network Discovery automatically attempts to discover as many assets as possible. It does this using Network Visibility, a passive detection method that captures IP and MAC addresses from broadcasted network packets across all network interfaces of linked sensors. Additionally, it performs active discovery actions within the IP range and Active Directory domain where these sensors are located.

To view assets detected by Network Visibility, navigate to **Reports > All assets detected by Network Visibility** (example: Lansweeper report).

If needed, you can refine or disable discovery actions by going to **Scanning > Discovery actions**, where you can add filters or remove actions entirely.

For full control, you can also entirely disable passive detection. To do this, go to **Scanning > Discovery groups** and select a discovery group. In there, disable **Network Visibility**.   
This will stop sensors from inspecting network packets, and restrict asset discovery to the targets defined in **Scanning > Discovery actions**.

### My discovery results aren’t showing up in my Lansweeper Site, how can I troubleshoot this?

- Check if Lansweeper Site's status is OK by checking Lansweeper Status (Data pipeline > "Modernized Discovery")
- Check if these APIs are working:
  - [Config API](https://discovery-gateway.lansweeper.com/config-api/ready) (Send configuration from Lansweeper Site to Lansweeper Discovery)
  - [Syncer API](https://discovery-gateway.lansweeper.com/syncer-api/ready) (Receive data in Lansweeper Site from Lansweeper Discovery)
  - [Notification API](https://discovery-gateway.lansweeper.com/notification-api/ready) (Add/update notifications in Lansweeper Site about Lansweeper Discovery)
  - [Recognition API](https://discovery-gateway.lansweeper.com/recognition-api/ready) (Recognize assets in Lansweeper Site from received data from Lansweeper Discovery)
- Ensure either the IT Agent or Network Discovery service is running by opening `services.msc` on Windows or Activity Monitor app on macOS or `sudo ps -aux | less` on Linux
- Check the logs for errors using [paths and logs](/docs/install-it-agent-discovery#pathsandlogs) or [network discovery paths and logs](/docs/install-network-discovery#pathsandlogs)

### If I want to move from Lansweeper On Prem to Lansweeper Discovery but have thousands of manually created assets in their database, how can we ensure those stay visible inside of LS Site after the Lansweeper database is no longer sync'd?

As the data is already in LS Site, it stays there. Just make sure to unlink LS Classic or that the cleanup rules are no longer removing assets automatically after x time. As long as the sync server remains connected, the cleanup rules remain active. Network discovery acts as a new installation in LS Site. Each hub is considered an installation. Don't think of it as a one-off replacement; think of it as a secondary installation.

This means the assets from an LS Classic/On-Prem install already syncing to Cloud will remain in Cloud even if you add a Network Discovery Hub in your LS Site. If you then unlink/uninstall LS Classic/On-Prem and choose to keep the data in LS Site, those manually created/updated assets will have been synced to LS Site earlier and will remain there. Adding a network discovery will only add new/update existing assets.

### How many Network Discovery IT/OT sensors should I deploy? Does Network Discovery have load balancing where traffic can move between sensors easily without overloading one vs. another?

There's no load balancing in a discovery action yet. So right now, if you assign lots of targets in an action to multiple sensors, they will all be contacted by the first listed sensor in the action. Once we’ve added load balancing capabilities (foreseen in 2025), you will be able to indicate which sensor takes which part of the entire target list.

Depending on the type of asset, access, and provided credentials, it takes several minutes to scan an asset with network discovery.

- <5000 assets + weekly data update: 1 sensor or more
- <5000 assets + daily data update: 2 sensors or more
- >=5000 assets + weekly data update: 2 sensors or more
- >=5000 assets + daily data update: 4 sensors or more
- >=10,000 assets + weekly data update: 2 sensors or more
- >=10,000 assets + daily data update: 4 sensors or more

### Can I install Lansweeper Network Discovery on Linux box?

Yes, as long as the Linux operating system (and version) is mentioned in the supported operating system list, found in [Install Network Discovery](/docs/install-network-discovery#OS).

### If I have two hubs installed and the credentials are saved to the first hub, are they only used for actions where the first hub is mapped to? Or can the second hub also use those same credentials? Or do I need to save credentials to the Hub on the network where they'll be used?

Yes, only by the specific Hub, but you can easily "sync" credentials from one hub to another by going to Lansweeper Site > Scanning > Discovery credentials. There, you can easily add extra hubs that need to send the specific credential to their sensors. By adding extra hubs, the original hub will send the credential to the other hub, over LS Site, with full encryption both in transit and at rest.

### Why is my Network Discovery installed on Linux only reporting back recognition data but no detailed asset data for Windows assets?

Currently, Network Discovery on Linux can’t get the details yet from a Windows device due to access restrictions. If you do enable Windows Remote Management between the Windows asset and the Linux sensor, you might already get more information. See [How to configure WINRM for HTTPS - Windows Client | Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management) on how to enable it on your Windows asset.

### What is the packet size of the message Lansweeper sends to the assets for discovery, and what can be the maximum response message size?

Lansweeper sends discovery messages with a maximum packet size of **8191 bytes** for any non-PowerShell-based request, and **32766 bytes** for PowerShell-based requests.

The maximum response message size is up to **4 MB** for Windows Server during an initial scan. However, typical response sizes are much smaller, especially during rescans, as not every item on a Windows system is rescanned.

### Do the Network Discovery hub and/or sensor update automatically on Linux?

Yes, they update automatically using your Linux package manager, such as **apt** or **yum**. For more information on automating updates and upgrades, you can refer to resources such as [apt - Automate Updates and Upgrade](https://askubuntu.com/questions/1331557/automate-updates-and-upgrade).

### Why does the installation of Network Discovery fail with “Unable to initialize installer” on Windows?

This error occurs when the environment variable **TMP** or **TEMP** refers to a path that doesn’t exist. To resolve the issue, update the environment variable to point to a valid directory:

1. Press **Windows + R** to open the Run dialog.
2. Type `sysdm.cpl` and press **Enter** to open **System Properties**.
3. In the **Advanced** tab, select **Environment Variables**.
4. Locate the **TMP** or **TEMP** variables under **User variables** or **System variables**.
5. Select the variable and select **Edit**.
6. Update the **Variable value** to point to a valid folder path, such as `C:\Windows\Temp`.
7. Select **OK** to save changes.
8. Finally, retry the installation.

### How are the credentials handled in rest and in transit when using Network Discovery?

#### Credential storage

Credentials are securely stored in the Discovery Hub database using two layers of encryption:

1. The database itself is fully encrypted, and can only be used by the current installation.
2. Credentials are encrypted separately using advanced security measures. The encryption key is stored independently, and is only accessible by the machine itself, ensuring enhanced protection.

#### Credential usage

When a credential is used for scanning a target on a sensor, the encryption process differs from how credentials are stored in the Discovery Hub:

- When a sensor is started, it will generate a Public/Private key pair, which is only kept in memory.
- After a successfully authenticating with the Hub, the sensor shares its Public key with the Hub.
- When a sensor needs a credential for scanning a target:
  1. The Hub retrieves the encrypted credential and decrypts it.
  2. The credential is immediately re-encrypted using the sensor's Public key.

This process ensures that only the designated sensor has the capability to decrypt and utilize the credential as needed.

#### Credentials received from Lansweeper Sites

A similar encryption process is applied when credentials are received from Lansweeper Sites:

- The Hub generates a Public/Private key pair, and shares the Public key with Lansweeper Sites.
- When a user enters a new credential in Lansweeper Sites, it is encrypted before being sent to the Hub.
- Upon receiving the encrypted credential, the Hub decrypts and securely stores it locally.

#### Flow diagram



### How can I backup Network Discovery?

Backing up the install folder of your hub (default: C:\Program Files\Lansweeper Network Discovery) would suffice. You don't need to backup your sensor as it's better to reinstall it while connecting it to your hub to restore it.  
There's no on prem inventory to back up for Network Discovery. The hub stores discovery results and tries to sync them to LS Site. If you don't have a backup, the worst thing that can happen is that your assets haven't been refreshed for x time. All your assets remain in your Lansweeper Site which is automatically backed up by Lansweeper.  
(Re)installing network discovery (on the same/other device), assigning the new sensors in the discovery actions, and sharing the credentials to its hub, will continue to update your assets.
