<!-- # Install Network Discovery -->

Lansweeper's Network Discovery enables you to discover all IT and OT assets within your network. By utilizing the necessary discovery credentials, Network Discovery gathers all asset details both on the local machine and on remote IT assets.

On this page:

- Requirements   
  - Connection requirements
  - Supported operating systems
  - System requirements
- Installation paths and logs
- Install Network Discovery on Windows
  - Install Network Discovery on Windows interactively
  - Install Network Discovery on Windows silently
  - Uninstall Network Discovery on Windows
- Install Network Discovery on Linux
  - Uninstall Network Discovery on Linux
- Install Network Discovery on macOS
  - Install Lansweeper Network Discovery on macOS interactively
  - Install Network Discovery on macOS silently
  - Uninstall Network Discovery on macOS
- Start Network Discovery
- Change the default certificate
- Set a proxy for Network Discovery
- Link Network Discovery to Lansweeper site
- Remove Network Discovery from Lansweeper site
- Frequently asked questions (FAQ)

## Requirements

### Connection requirements

The computer running the hub component of Network Discovery must allow the following outbound connections using TLS 1.2 or higher, when you've linked the hub with your Lansweeper site:

| **URL** | **Description** |
| --- | --- |
| [https://app.lansweeper.com](https://app.lansweeper.com/api/scanner-connect) (port 443) | Connects to your Lansweeper site. |
| EU: [https://discovery-gateway.eu.lansweeper.com](https://discovery-gateway.eu.lansweeper.com/ "https://discovery-gateway.eu.lansweeper.com")(port 443) US: [https://discovery-gateway.us.lansweeper.com/](https://discovery-gateway.lansweeper.com/) (port 443) Older versions: <https://discovery-gateway.lansweeper.com/> (port 443) | Authenticates, logs in, syncs data, and gets auto updates from your Lansweeper site. |
| [https://download.lansweeper.com/](https://download.lansweeper.com/ "https://download.lansweeper.com") (port 443) | Downloads updates automatically when a new version is released. |
| <https://app.lansweeper.com/api/scanner-connect> (port 443) | Required to provide connection data to your Lansweeper site for multi-region (EU/US). |

If the computer running Network Discovery requires a proxy server, you can provide the details using this procedure.

If you're seeing "An issue occurred during linking: Cloud installation could not be created. You can try again by clicking the button link with Lansweeper site Or go to your local Hub", ensure these connection requirements are met.

### Supported operating systems

Network Discovery can be installed on the following operating systems.

#### Windows

- Windows 10 21H2 or higher (x64)
- Windows 11 22000 or higher (x64)
- Windows Server (Core) 2012 or higher (x64)

#### Linux

##### .deb packages:

- Debian 12 up to penultimate version (x64)
- Ubuntu 22.04 up to penultimate version (x64)

##### .rpm packages:

- CentOS Stream 9 up to penultimate version (x64)
- Fedora 40 up to penultimate version (x64)
- openSUSE Leap 15.6 up to penultimate version (x64)
- Red Hat Enterprise Linux 8 up to penultimate version (x64)
- SUSE Enterprise Linux (SLES) 15.6 up to penultimate version (x64)

#### MacOS

- macOS 13 up to penultimate version (x64) (requires [Rosetta](https://support.apple.com/en-us/102527) to be installed until dedicated ARM builds are made available)

### System requirements

#### Hub system requirements

| Specifications | Minimum for 2 sensors | Recommended for up to 5 sensors | Recommended for up to 10 sensors | Recommended for up to 100 sensors |
| --- | --- | --- | --- | --- |
| CPU | x64, single-core 1 GHz | x64, quad-core 2 GHz | x64, octa-core 2 GHz | x64, octa-core 4 GHz |
| RAM | 2 GB RAM | 16 GB RAM | 32 GB RAM | 256 GB RAM |
| Free disk space on SSD | 1 GB | 10 GB | 50 GB | 500 GB |
| Internal network speed | 100 Mbps | 1000 Mbps | 1000 Mbps | 1000 Mbps |
| External network speed (to your site) | 20 Mbps | 100 Mbps | 300 Mbps | 300 Mbps |

#### Sensor system requirements

| Specifications | Minimum | Recommended |
| --- | --- | --- |
| CPU | x64, single-core 1 GHz | x64, dual-core 2 GHz |
| RAM | 1 GB RAM | 4 GB RAM |
| Free disk space | 500 MB | 1 GB |
| Network speed | 100 Mbps | 1000 Mbps |

## Installation paths and logs

By default, Network Discovery will be installed in the following locations:

- Windows: `C:\Program Files\Lansweeper Network Discovery`
- Linux:
  - `/opt/lansweeper-hub`
  - `/opt/lansweeper-it-sensor`
  - `/opt/lansweeper-ot-sensor`
- macOS: `/Application Support/Lansweeper Network Discovery`

By default, logs can be found in the following locations:

- `tools\gatherlogs\gatherlogs.ps1`
- `sensors\IT\logs\Lansweeper.IT.Sensor.log`
- `sensors\OT\logs\Lansweeper.IT.Sensor.log`
- `hub\logs\Lansweeper.Discovery.Hub.log`
- `update\logs\Lansweeper.Discovery.Update.log`
- Windows Installer:
  - `C:\Program Files\Lansweeper Network Discovery\install\logs\Lansweeper_Network_Discovery_installer.log`
  - `C:\Users\%USERNAME%\AppData\Local\Temp\installbuilder_installer_00000.log (if the installation was not successful)`
  - `C:\Users\%USERNAME%\AppData\Local\Temp\Lansweeper_Network_Discovery_uninstaller.log`
  - `C:\Users\%USERNAME%\AppData\Local\Temp\Lansweeper.IT.Hub.log`
- MacOS: `/tmp/Lansweeper_Network_Discovery*.log`

When reaching out to Lansweeper for troubleshooting, we offered a built-in log collector tool, so we have more info during the analysis of the issue.

Gather the logs on Windows using `C:\Program Files\Lansweeper Network Discovery\tools\gatherlogs\gatherlogs.ps1`(using an elevated PowerShell prompt). This will return a .zip file, which you share with our support department.

- Check the status of the sensors connected to the hub: <https://localhost:59525/status/sensors>
- Check the status of the sync between Network Discovery hub and Lansweeper site: <https://localhost:59525/status/sync>
- Check the status of the import functionality for IT Agent Portable: <https://localhost:59525/status/import>

## Install Network Discovery on Windows

#### Install Network Discovery on Windows interactively

1. Ensure your Windows operating system is supported.
2. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/).
3. If you have multiple Lansweeper sites, select the site to which you want to link Network Discovery.
4. Go to **Discovery (or Scanning) > Discovery systems > Download installers/packages** and navigate to the**Network Discovery**section.
5. Locate the Windows OS and select **Download Network Discovery installer** and **Download Network Discovery silent installation configuration**.
6. Optionally, select **Link Discovery system**. In the pop-up, select **Create new code**, choose an expiration date, select **Apply** and select **Copy code**.
7. Run the installer.
8. Select **I accept the agreement > Next**.
9. Choose which directory to install Network Discovery, then **Next**.
10. Select **Install Hub** and **Install IT Sensor**. 
    - Specify another hostname for the machine hosting the hub if you’re only installing the IT Sensor.
    - Specify another TCP port if you want to override the default port for Hub to Sensor communication.
11. Select **Next**.
12. If you copied a linking code earlier, you can paste it here.
13. Select **Next**.
14. Select **Open Hub after finishing the installer > Finish**.

Now that Network Discovery is installed, check out the Hub and start Network Discovery.

### Install Network Discovery on Windows silently

#### Method 1

1. Ensure your Windows operating system is supported.
2. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/).
3. If you have multiple Lansweeper sites, select the site to which you want to link Network Discovery.
4. Go to **Discovery (or Scanning)****> Discovery systems > Download installers/packages** and navigate to the**Network Discovery**section.
5. Locate the Windows OS and select **Download Network Discovery installer** and **Download Network Discovery silent installation configuration**.
6. Select **Link Discovery system**. In the pop-up, select **Create new code**.
7. Choose an expiration date, select **Apply** and select **Copy code**.
8. On your Windows computer, open the downloaded **lansweepernetworkdiscoveryinstallation.cfg**file.
9. In the file, replace `cloudtokenvalue` with your copied linking code. If the computer requires a proxy server, remove the `#` for `proxyserver=myproxyserver.domain.local` and `proxyport=8080`.   

   ```
   mode=unattended  
   accepteula=1  
   path=C:\Program Files\Lansweeper Network Discovery  
   components=hub,itsensor,otsensor  
   hubinstance=localhost  
   hubport=59525  
   installnpcapdriver=1  
   dcomautoconfig=1  
   #cloudtoken=cloudtokenvalue  
   #proxyserver=myproxyserver.domain.local   
   #proxyport=8080  
   #hubcode=MyHubCode generated in hub UI > Settings > Data transfer > Hub code (only required for distributed deployment of sensors across multiple systems, connecting to a remote hub)
   ```
10. In an elevated command prompt, enter the following command, replacing `X.X.X` in `Lansweeper-network-discovery-X.X.X` with the version number of your installer:  

    ```
    Lansweeper-network-discovery-X.X.X-windows-x64-installer.exe --optionfile lansweepernetworkdiscoveryinstallation.cfg
    ```

    The version numbers for your installer can be found in your Lansweeper site. Go to **Scanning > Download installers/packages > Network Discovery installer > Version** and locate your installer.

Now that Network Discovery is installed, check out the Hub and start Network Discovery.

#### Method 2

1. Ensure your Windows operating system is supported.
2. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/).
3. If you have multiple Lansweeper sites, select the site to which you want to link Network Discovery.
4. Go to **Discovery (or Scanning)****> Discovery systems> Download installers/packages** and navigate to the**Network Discovery**section.
5. Locate the Windows OS and select **Download Network Discovery installer**.
6. Select **Link Discovery system**. In the pop-up, select **Create new code**.
7. Choose an expiration date, select **Apply** and select **Copy code**.
8. Enter the following command in an elevated command prompt, replacing `cloudtokenvalue` with the copied linking code.   
   If the computer requires a proxy server, add parameters `--proxyserver proxyserveraddress` and `--proxyport 8080`. Replace `X.X.X` in `Lansweeper-network-discovery-X.X.X` with the version number of your installer.  

   ```
   Lansweeper-network-discovery-X.X.X-windows-x64-installer.exe --mode unattended --accepteula 1 --path "C:\Program Files\Lansweeper Network Discovery Discovery" --cloudtoken cloudtokenvalue
   ```

   The version numbers for your installer can be found in your Lansweeper site. Go to **Scanning > Download installers/packages > Network Discovery installer > Version** and locate your installer.

Now that Network Discovery is installed, check out the Hub and start Network Discovery.

## Uninstall Network Discovery on Windows

To uninstall the Network Discovery on Windows, either:

- On your Windows computer, open the **Start** menu, then go to **Control Panel > Add or remove programs** and locate **Lansweeper Network Discovery**. Select **Uninstall**.
- Open a command prompt and enter:

  ```
  "C:\Program Files\Lansweeper Network Discovery\uninstall.exe" --mode unattended 
  ```

## Install Network Discovery on Linux

On Linux, remote Windows discovery is limited to Credential-free Device Recognition (CDR). Full data discovery (software, user info, ...) for remote Windows discovery is planned but not yet available and will require remote WinRM on those Windows assets.   
Active Directory discovery is not supported on Linux sensors due to connectivity incompatibilities with domain controllers.

Only silent installs are currently supported for Network Discovery on Linux.

1. Ensure your Linux operating system is supported.
2. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/).
3. If you have multiple Lansweeper sites, select the site to which you want to link Network Discovery.
4. Go to **Discovery (or Scanning)****> Discovery systems > Download installers/packages** and navigate to the**Network Discovery**section.
5. Locate the Linux OS and select **Download Lansweeper repository package** for deb or rpm, depending on your Linux distribution.
6. Select **Link Discovery system**. In the pop-up, select **Create new code**.
7. Choose an expiration date, select **Apply** and select **Copy code**.
8. Depending on your Linux distribution, follow the instructions below, replacing `cloudtokenvalue`  with the copied linking code.

#### Debian and Ubuntu

1. Install the repository package. Copy it to your machine.  

   These packages are required to update Lansweeper repositories: **ca-certificates**and **openssl**.
2. In a terminal, enter `sudo dpkg -i ./lansweeper-repository.deb`.
3. Enter `sudo apt update` to make the system aware of the repository.
4. To install the Network Discovery hub, enter `sudo env LINKING_CODE=cloudtokenvalue apt install lansweeper-network-discovery-hub`
   - Optional: To install the IT sensor for your IT assets, enter `sudo env HUB_CODE=MyHubCodeGeneratedinHubUI-Settings-DataTransfer-HubCode apt install lansweeper-network-discovery-it-sensor`.
   - Option: To install the OT sensor for your OT assets, enter `sudo env HUB_CODE=MyHubCodeGeneratedinHubUI-Settings-DataTransfer-HubCode apt install lansweeper-network-discovery-ot-sensor`
5. After the install is done, set the hub location:
   1. Go to the install directory of the Linux sensor and open `appsettings.json`.
   2. Change "HubUrl": "<https://localhost:59525/IT/Sensor>" to "HubUrl": "[https://MyRemoteHub01:59525/IT/Sensor](https://myremotehub01:59525/IT/Sensor)"
   3. Enter: `sudo systemctl restart lansweeper-network-discovery-it-sensor`
   4. Enter: `sudo systemctl restart lansweeper-network-discovery-ot-sensor`

Once there is an update, update the packages by entering

```
sudo apt update && apt upgrade lansweeper-network-discovery-hub sudo apt update && apt upgrade lansweeper-network-discovery-it-sensor sudo apt update && apt upgrade lansweeper-network-discovery-ot-sensor
```

#### Red Hat, CentOS, and SUSE

1. Install the repository package. Copy it to your machine.
2. In a terminal, enter `sudo yum install ./lansweeper-repository-1-0-x86_64.rpm`.
3. Enter `sudo yum update` to make the system aware of the repository.
4. Enter `sudo env LINKING_CODE=cloudtokenvalue`.
5. Enter `sudo yum install lansweeper-network-discovery-hub`.
   - For the IT sensor, enter `sudo yum install lansweeper-network-discovery-it-sensor`.
   - For the OT sensor, enter `sudo yum install lansweeper-network-discovery-ot-sensor`.
6. Once there is an update, update the packages by entering

   ```
   sudo yum update && yum upgrade lansweeper-network-discovery-hub
   sudo yum update && yum upgrade lansweeper-network-discovery-it-sensor
   sudo yum update && yum upgrade lansweeper-network-discovery-ot-sensor
   ```

Now that Network Discovery is installed, check out the Hub and start Network Discovery.

### Optional: Link your Linux sensor to a remote Windows/Linux/macOS Network Discovery hub

1. Go to the install directory of the Linux sensor and open `appsettings.json`.
2. For an IT sensor, change `"HubUrl": "https://localhost:59525/IT/Sensor"` to `"HubUrl": "https://MyRemoteHubIPaddress:59525/IT/Sensor"`.
3. For an OT sensor, change `"HubUrl": "https://localhost:59525/OT/Sensor"` to `"HubUrl": "https://MyRemoteHubIPaddress:59525/OT/Sensor"`.
4. Add a file called `hubcode.txt` (with `chmod 744`, encoding UTF-8) in your install directory. Paste the hub code retrieved from [https://MyRemoteHubIPaddress:59525](http:// )**> settings > data transfer > Hub** in the `hubcode.txt` file.
5. Once the file is saved, restart the sensor service using either of the following commands:
   - `sudo systemctl restart lansweeper-network-discovery-it-sensor`
   - `sudo systemctl restart lansweeper-network-discovery-ot-sensor`  
       
     This will make the sensor retrieve the certificate from the hub (located in `C:\Program Files\Lansweeper Network Discovery\hub\ssl\Lansweeper_Discovery_Internal_Communication.cer`) and install it as a trusted certificate on the sensor. Next, the sensor will use the hub code to authenticate itself within the hub, making it a trusted new sensor.

Your sensor will appear as a newly added sensor in the list at `https://MyRemoteHubIPaddress:59525/Sensors`.

### Uninstall Network Discovery on Linux

To uninstall Network Discovery Linux, open your terminal and run the following commands, depending on your environment.

- Debian and Ubuntu:

  1. `sudo dpkg -r lansweeper-network-discovery-ot-sensor`
  2. `sudo dpkg -r lansweeper-network-discovery-it-sensor`
  3. `sudo dpkg -r lansweeper-network-discovery-hub`
- Red Hat, CentOS, and SUSE:

  1. `sudo rpm -e lansweeper-network-discovery-it-sensor`
  2. `sudo rpm -e lansweeper-network-discovery-ot-sensor`
  3. `sudo rpm -e lansweeper-network-discovery-hub`

## Install Network Discovery on macOS

On macOS, remote Windows discovery is limited to Credential-free Device Recognition (CDR). Full data discovery (software, user info, ...) for remote Windows discovery is not supported on macOS.  
Active Directory discovery is not supported on macOS sensors due to connectivity incompatibilities with domain controllers.

There are multiple you can use to install the Network Discovery on a macOS computer.

If the computer running Network Discovery requires a proxy server, use a silent install method.

#### Install Lansweeper Network Discovery on macOS interactively

1. Ensure your macOS operating system is supported.
2. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/).
3. If you have multiple Lansweeper sites, select the site to which you want to link Network Discovery.
4. Go to **Discovery (or Scanning)****> Discovery systems > Download installers/packages** and navigate to the**Network Discovery**section.
5. Locate the macOS with DMG format. Select **Download Network disk image** to download the installer.
6. Select **Link Discovery system**. In the pop-up, select **Create new code**.
7. Choose an expiration date, select **Apply** and select **Copy code**.
8. Run the Network Discovery installer on your macOS machine. In the resulting pop-up, double-click the **name of the installer**, then **Next**.  

   If the software is blocked, select the Apple icon in the upper-left corner of your screen. Select **System Preferences > Security & Privacy > Open Anyways**.
9. Select **I accept the agreement > Next**.
10. Select the installation directory. By default, the directory is **/Library/Application Support/Lansweeper Network Discovery**. Select **Next**.
11. Paste the Lansweeper linking code in the installer, then select **Next**.  

    On macOS 15 and higher, you will need to manually trust the certificate. You can do so by opening a browser and navigating to [https://localhost:59525](https://localhost:59525/ "https://localhost:59525"), and selecting **View certificate**.

Now that Network Discovery is installed, check out the Hub and start Network Discovery.

### Install Network Discovery on macOS silently

#### Method 1 - PKG deployment

1. Ensure your macOS operating system is supported.
2. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/).
3. If you have multiple Lansweeper sites, select the site to which you want to link Network Discovery.
4. Go to **Discovery (or Scanning)****> Discovery systems > Download installers/packages** and navigate to the**Network Discovery**section.
5. Select **Download Network Discovery package** and **Network Discovery macOS package silent installation configuration** to download both files.
6. Select **Link Discovery system**. In the pop-up, select **Create new code**.
7. Choose an expiration date, select **Apply** and select **Copy code**.
8. In the downloaded **Network Discovery package silent installation configuration** file, replace `cloudtokenvalue` with your copied linking code and modify the content to suit your needs. If the computer requires a proxy server, remove the `#` for `proxyserver=myproxyserver.domain.local` and `proxyport=8080`.   

   ```
   #!/bin/sh  
   PreinstallConfig="/tmp/LansweeperNetworkDiscovery-Preinstall.cfg" # Don't change this path!  
   [ -f $PreinstallConfig ] && chmod 744 $PreinstallConfig  
   cat > $PreinstallConfig << EOF  
   mode=unattended  
   accepteula=1  
   path=/Library/Application Support/Lansweeper Network Discovery  
   cloudtoken=cloudtokenvalue  
   #proxyserver=myproxyserver.domain.local   
   #proxyport=8080  
   EOF  
   chmod 744 $PreinstallConfig
   ```
9. Enter the following command: `sudo ./tmp/LansweeperPreinstallScript.sh`
10. Enter the following command, replacing `cloudtokenvalue` with the copied linking code, and replacing `X.X.X` in `Lansweeper-network-discovery-X.X.X-X-osx-installer.dmg` with the version number of your installer.   
    If the computer requires a proxy server, add parameters `--proxyserver proxyserveraddress` and `--proxyport 8080`.  

    ```
    sudo Lansweeper-network-discovery-X.X.X-X-osx-installer.app/Contents/MacOS/installbuilder.sh --mode unattended --accepteula 1 --path /Library/Application Support/Lansweeper Network Discovery/ --cloudtoken cloudtokenvalue
    ```
11. The version numbers for your installer can be found in your Lansweeper site. Go to **Scanning > Discovery systems > Download installers/packages**.

    On macOS 15 and higher, you will need to manually trust the certificate. You can do so by opening a browser and navigating to [https://localhost:59525](https://localhost:59525/ "https://localhost:59525"), and selecting **View certificate**.

Now that Network Discovery is installed, check out the Hub and start Network Discovery.

### Method 2 - DMG deployment

1. Ensure your macOS operating system is supported.
2. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/).
3. If you have multiple Lansweeper sites, select the site to which you want to link Network Discovery.
4. Go to **Discovery (or Scanning)****> Discovery systems > Download installers/packages** and navigate to the**Network Discovery**section.
5. Locate the macOS with DMG format. Select **Download Network disk image** to download the installer.
6. Select **Link Discovery system**. In the pop-up, select **Create new code**.
7. Choose an expiration date, select **Apply** and select **Copy code**.
8. In an elevated command prompt, enter `hdiutil attach Lansweeper-network-discovery-0.9.0-16-osx-installer.dmg`  to mount the dmg file.
9. Enter `cd "/Volumes/Lansweeper Network Discovery"` to navigate to the volume.
10. Enter the following command, replacing `cloudtokenvalue` with the copied linking code, and replacing `X.X.X` in `Lansweeper-network-discovery-X.X.X-X-osx-installer.dmg` with the version number of your installer.   
    If the computer requires a proxy server, add parameters `--proxyserver proxyserveraddress` and `--proxyport 8080`.  

    ```
    sudo Lansweeper-network-discovery-X.X.X-X-osx-installer.app/Contents/MacOS/installbuilder.sh --mode unattended --accepteula 1 --path /Library/Application Support/Lansweeper Network Discovery/ --cloudtoken cloudtokenvalue
    ```

    On macOS 15 and higher, you will need to manually trust the certificate. You can do so by opening a browser and navigating to [https://localhost:59525](https://localhost:59525/ "https://localhost:59525"), and selecting **View certificate**.

Now that Network Discovery is installed, check out the Hub and start Network Discovery.

### Uninstall Network Discovery on macOS

To uninstall Network Discovery on macOS, you can either:

- Go to **/Library/Application Support/Lansweeper Network Discovery** and execute **uninstall.app**.
- Open a command prompt and enter:  

  ```
  sudo "/Library/Application Support/Lansweeper Network Discovery/uninstall.app/Contents/MacOS/installbuilder.sh" --mode unattended
  ```

## Start Network Discovery

Now that Network Discovery is installed, you can check out the Hub and start Network Discovery.

1. On the machine where you installed the Hub for Network Discovery, open a browser and navigate to [https://localhost:59525](https://localhost:59525/ "https://localhost:59525").
2. Go to **Sensors** to ensure the sensor is present.
3. Go to **Discover now**.
4. Enter an IP address to scan.
5. Optionally, enter credentials and choose advanced options to personalize discovery.
6. Select **Discover**.
7. Go to **Discovery queue** to validate the scan has worked as expected.
8. To see the details of a discovered asset, go to **Discovery results** and select a result.

## Change the default certificate

1. Generate your own .pfx file and password. For more information on creating a .pfx file, see [How to create a .pfx file](https://www.ssl.com/how-to/combine-a-private-key-with-p7b-certificate-how-to-create-a-pfx-file/).
2. In your installation folder, open **appsettings.json**.
3. Search for "Certificate".
4. Change the "Path" and the "Password" values to the values of the .pfx file you've generated earlier.
5. Save the appsettings.json file.
6. Restart the **Lansweeper Network Discovery Hub** service.

## Set a proxy for Network Discovery

### Trial installation

If you need a proxy for your trial installation, follow the [interactive Windows installation](/classic/docs/install-network-discovery#WInteractive), but instead of double-clicking the installer, open a command prompt and run:

```
Lansweeper-network-discovery-x.y.z-windows-x64-installer.exe --advanced=1
```

This will launch the Hub UI before it attempts to connect to your Lansweeper site, allowing you to configure the Hub's proxy settings first.

### Standard installation

1. On the machine where you installed the Hub for Network Discovery, open a browser and navigate to [https://localhost:59525](https://localhost:59525/ "https://localhost:59525").
2. Go to **Settings** and open **Proxy**.
3. Enter the **username**, **password**, and the **address** and **port**.
4. Enable the **Use a proxy server**toggle.
5. Select **Save proxy settings**.
6. Now you can continue to link Network Discovery to your Lansweeper Site in the next section.

## Link Network Discovery to Lansweeper site

You can optionally send all results from Network Discovery to your Lansweeper site to add or update your inventory.

1. Open a browser and navigate to <https://app.lansweeper.com/redirect-to/scanning/systems?skipEmpty=true&getLinkingCode=true>, login, optionally select the site to link with and select **Copy code**.
2. Open the Lansweeper Network Discovery hub UI (hosted at [https://localhost:59525](https://localhost:59525/ "https://localhost:59525") by default) and select **Linking options**.
3. Select **Cloud-based inventory for all assets**.
4. Enter your newly created code, and select **Link with Lansweeper site**.

## Remove Network Discovery from Lansweeper site

If required, you can remove Network Discovery, all its sensors, and all data it has brought in from your Lansweeper site:

1. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/ "https://app.lansweeper.com/").
2. If you have multiple Lansweeper sites, select the site you want to remove Network Discovery from.
3. Go to **Discovery (or Scanning)****> Discovery systems > All systems**.
4. Select the relevant Network Discovery system.
5. Finally, select **Delete system**.

Removing a Network Discovery system from your Lansweeper site will remove all linked sensors and all asset data it has ever brought in.

## Next steps

Now that you've installed Network Discovery, learn how to [Configure Network Discovery](/classic/docs/configure-network-discovery).

## Frequently asked questions (FAQ)

For a list of answers to frequently asked questions, check out [Network Discovery: Frequently Asked Questions](/classic/docs/network-discovery-frequently-asked-questions).
