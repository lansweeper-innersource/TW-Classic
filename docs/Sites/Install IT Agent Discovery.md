<!-- # Install IT Agent Discovery -->

Lansweeper's IT Agent Discovery is a lightweight, cross-platform scanning agent that can run on Windows, Linux, and Mac computers. IT Agent Discovery automatically collects an inventory from the computer it's installed on, securely sends scanned data to your Lansweeper Site over HTTPS, and can scan computers outside your network and over the internet.

On this page:

- Benefits of IT Agent Discovery
- Is IT Agent Discovery or LsAgent right for me?
- Requirements   
  - Connection requirements
  - Supported operating systems
- Installation paths and logs
- Install IT Agent Discovery on Windows
  - Install IT Agent Discovery on Windows interactively
  - Install IT Agent Discovery on Windows silently
  - Uninstall IT Agent Discovery on Windows
- Install IT Agent Discovery on Linux
  - Install IT Agent Discovery on Linux silently
  - Uninstall IT Agent Discovery on Linux
- Install IT Agent Discovery on macOS
  - Install IT Agent Discovery on macOS interactively
  - Install IT Agent Discovery on macOS silently
  - Uninstall IT Agent Discovery on macOS
- Next steps
- Frequently asked questions (FAQ)

## Benefits of IT Agent Discovery

IT Agent Discovery offers a range of advantages compared to other scanning agents, including:

- **Direct Discovery Results**: IT Agent is able to transmit discovery results directly to your Lansweeper Site, eliminating the need for a Lansweeper On-premises scan server.
- **Cross-Platform Auto-Updates**: IT Agent can automatically update Windows, Linux, and macOS machines, expanding beyond the Windows-only auto-update capability of LsAgent.
- **Expanded Device Data**: IT Agent gathers comprehensive data on devices, including additional information like user details on macOS. This enriched dataset is mapped within your Lansweeper Site, providing enhanced visibility of your network.
- **Silent Installation Across Platforms**: IT Agent supports silent deployment on Windows, Linux, and macOS. This empowers administrators to implement the agent seamlessly, minimizing disruptions to end-users. In contrast, LsAgent restricts silent installs to Windows.
- **Reduced Vulnerability Risk**: IT Agent for Windows, built on .NET 8.0, mitigates vulnerability risks in comparison to LsAgent for Windows.

## Is IT Agent Discovery or LsAgent right for me?

While IT Agent Discovery offers many advantages, it may not be the optimal choice for every environment. To determine the right scanning agent for your needs, consider the following questions:

- Do you primarily use Lansweeper Sites to view and manage your assets rather than Lansweeper On-premises?
- Does the computer you want to scan have internet access?
- Does the Windows computer you want to scan run on Windows 7 SP1 or Server 2012 or later?

If you've answered **YES** to all of these questions, then IT Agent Discovery is right for you.   
If you've answered **NO** to any of these questions, then [install LsAgent](/classic/docs/introduction-to-lsagent-for-windows-linux-and-mac "Introduction to LsAgent for Windows, Linux and Mac") instead.

## Requirements

Before installing IT Agent Discovery, make sure the requirements below are met.

- Connection requirements
- Supported operating systems
  - Windows
  - Linux
  - MacOS

### Connection requirements

The computer running IT Agent Discovery must allow the following outbound connections using TLS 1.2 or higher:

| **URL** | **Description** |
| --- | --- |
| [https://app.lansweeper.com](https://app.lansweeper.com/api/scanner-connect) (port 443) | Connects to your Lansweeper Site. |
| EU: [https://discovery-gateway.eu.lansweeper.com/](https://discovery-gateway.lansweeper.com/) (port 443) US: [https://discovery-gateway.us.lansweeper.com/](https://discovery-gateway.lansweeper.com/) (port 443) | Authenticates, logs in, syncs data, and gets auto updates from your Lansweeper Site. |
| [https://download.lansweeper.com/](https://download.lansweeper.com/ "https://download.lansweeper.com") (port 443) | Downloads updates automatically when a new version is released. |
| <https://app.lansweeper.com/api/scanner-connect> (port 443) | Required to provide connection data to Lansweeper Site for multi-region (EU/US). |

If the computer running IT Agent Discovery requires a proxy server, you can provide the details using a silent installation method.

### Supported operating systems

The IT Agent Discovery can be installed on the following operating systems.

#### Windows

- Windows 7 SP1 (with extended security updates installed) and 8.1 (x64)
- Windows 10 1607 or higher (x64)
- Windows 11 22000 or higher (x64)
- Windows Server 2012 or higher (x64)

#### Linux

##### .deb packages:

- Debian 12 up to penultimate version (x64)
- Ubuntu 22.04 up to penultimate version (x64)

##### .rpm packages:

- Alpine Linux 3.19 up to penultimate version (x64)
- Azure Linux 3.0 up to penultimate version (x64)
- CentOS Stream Linux 9 up to penultimate version (x64)
- Fedora 40 up to penultimate version (x64)
- openSUSE Leap 16 up to penultimate version (x64)
- Oracle Linux 7 up to penultimate version (x64)
- Red Hat Enterprise Linux 8 up to penultimate version (x64)
- SUSE Enterprise Linux (SLES) 15.6 up to penultimate version (x64)

#### MacOS

- macOS 10.15 up to penultimate version (x64) (requires [Rosetta](https://support.apple.com/en-us/102527) to be installed until dedicated ARM builds are made available)

### System requirements

|  |  |  |
| --- | --- | --- |
| **Specifications** | **Minimum** | **Recommended** |
| CPU | x64, single-core 1 GHz | x64, dual-core 2 GHz |
| RAM | 2 GB RAM | 8 GB RAM |
| Free disk space | 500 MB | 1 GB |
| Network speed | 100 Mbps | 1000 Mbps |

## Installation paths and logs

By default, IT Agent Discovery will be installed in the following locations:

- Windows: `C:\Program Files\Lansweeper IT Agent Discovery`
- Linux: `/opt/lansweeper-it-agent`
- macOS: `/Application Support/Lansweeper IT Agent Discovery`

By default, logs can be found in the following locations:

- `sensors\logs\Lansweeper.IT.Sensor.log`
- `hub\logs\Lansweeper.Discovery.Hub.log`
- Windows Installer:
  - `C:\Program Files\Lansweeper IT Agent Discovery\install\logs\Lansweeper_IT_Agent_Discovery_installer.log`
  - `C:\Users\%USERNAME%\AppData\Local\Temp\installbuilder_installer_00000.log (if the installation was not successful)`
  - `C:\Users\%USERNAME%\AppData\Local\Temp\Lansweeper.IT.Hub.log`
  - `C:\Users\%USERNAME%\AppData\Local\Temp\Lansweeper_IT_Agent_Discovery_uninstaller.log`
- MacOS: `/tmp/Lansweeper_IT_Agent*.log`

When contacting Lansweeper for troubleshooting, we offered a built-in log collector tool, so we have more info during the analysis of the issue.

Gather the logs on Windows using `C:\Program Files\Lansweeper IT Agent Discovery\tools\gatherlogs\gatherlogs.ps1` (using an elevated PowerShell prompt). This will return a .zip file, which you can share with our Support department.

The default path to check the status of your IT Agent is either [https://localhost:59530/status/hub](https://localhost:59525/status/hub "https://localhost:59525/status/hub") or [https://localhost:59530/status](https://localhost:59525/status "https://localhost:59525/status") (as soon as IT Agent is a single file).

## Install IT Agent Discovery on Windows

You can also run IT Agent Discovery on Windows computers as a foreground application, included as a logon script. For more information, see [Set up and run IT Agent Portable](/classic/docs/set-up-and-run-lansweeper-it-agent-discovery-portable).

You can use three methods to install the IT Agent Discovery on a Windows computer.

If the computer running IT Agent Discovery requires a proxy server, use a silent install method.

- Install the IT Agent Discovery on Windows interactively
- Install the IT Agent Discovery on Windows silently

### Install IT Agent Discovery on Windows interactively

1. Ensure the connection requirements are met and your Windows operating system is supported.
2. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/).
3. Choose the Lansweeper Site to which you want to link the IT Agent Discovery.
4. Go to **Discovery (or Scanning) > Discovery systems**, then go to**Download installers/packages > Download IT Agent****installer**.
5. Run the downloaded installer.
6. Select **Yes** to allow the app to make changes to your device.
7. Select **I accept the agreement**.
8. Choose the installation directory and select **Next**.
9. While keeping the installer open, open a browser and navigate to your Lansweeper Site.
10. Select **Link Discovery system**. In the pop-up, select **Create new code**.
11. Choose an expiration date, select **Apply** and select **Copy code**.
12. Paste the Lansweeper linking code in the installer, then select **Next**.
13. Select **Next** to begin the installation.

Once the installation is complete, you can view your IT Agent Discovery in your Lansweeper Site by going to **Discovery (or Scanning)****> Discovery systems > All systems**. You can view the asset details discovered with your IT Agent Discovery in **Inventory > All assets**.

### Install IT Agent Discovery on Windows silently

#### Method 1 - using a config file

1. Ensure the connection requirements are met, and your Windows operating system is supported.
2. In your Lansweeper Site, go to **Discovery (or Scanning)****> Discovery systems**, then go to **Download installers/packages**. Select**Download IT Agent installer** and **Download IT Agent silent installation configuration**.
3. Select **Link Discovery system**. In the pop-up, select **Create new code**.
4. Choose an expiration date, select **Apply** and select **Copy code**.
5. On your Windows computer, open the downloaded **lansweeperitagentinstallation.cfg**file.
6. In the file, replace `cloudtokenvalue` with your copied linking code. If the computer requires a proxy server, remove the `#` for `proxyserver=myproxyserver.domain.local` and `proxyport=8080`.   

   ```
   mode=unattended   
   accepteula=1   
   path=C:\Program Files\Lansweeper IT Agent Discovery   
   cloudtoken=cloudtokenvalue   
   #proxyserver=myproxyserver.domain.local   
   #proxyport=8080
   ```
7. In an elevated command prompt, enter the following command, replacing `X.X.X` in `Lansweeper-IT-agent-discovery-X.X.X` with the version number of your installer:  

   The version numbers for your installer can be found in your Lansweeper Site. Go to **Discovery (or Scanning)****> Discovery systems > Download installers/packages > IT Agent installer > Version**and locate your installer.

   ```
   Lansweeper-IT-agent-discovery-X.X.X-windows-x64-installer.exe --optionfile lansweeperitagentinstallation.cfg
   ```

Once the installation is complete, you can view your IT Agent Discovery in your Lansweeper Site by going to **Discovery (or Scanning)****> Discovery systems > All systems**. You can view the asset details discovered with your IT Agent Discovery in **Inventory > All assets**.

#### Method 2 - without using a config file

1. Ensure the connection requirements are met, and your Windows operating system is supported.
2. In your Lansweeper Site, go to **Discovery (or Scanning)****> Discovery systems**, then go to**Download installers/packages >****Download IT Agent installer**.
3. Select **Link Discovery system**. In the pop-up, select **Create new code**.
4. Choose an expiration date, select **Apply** and select **Copy code**.
5. Enter the following command in an elevated command prompt, replacing `cloudtokenvalue`  with the copied linking code. If the computer requires a proxy server, add parameters `--proxyserver proxyserveraddress` and `--proxyport 8080`. Replace `X.X.X` in `Lansweeper-IT-agent-discovery-X.X.X` with the version number of your installer  

   The version numbers for your installer can be found in your Lansweeper Site. Go to **Discovery (or Scanning)****> Discovery systems****> Download installers/packages > IT Agent installer > Version**and locate your installer.

   ```
   Lansweeper-IT-agent-discovery-X.X.X-windows-x64-installer.exe --mode unattended --accepteula 1 --path "C:\Program Files\Lansweeper IT Agent Discovery" --cloudtoken cloudtokenvalue
   ```

#### Method 3 - using .msi

1. Ensure the connection requirements are met, and your Windows operating system is supported.
2. In your Lansweeper Site, go to **Discovery (or Scanning)****> Discovery systems**, then go to**Download installers/packages >****Download IT Agent installer**.
3. Select **Link Discovery system**. In the pop-up, select **Create new code**.
4. Choose an expiration date, select **Apply** and select **Copy code**.
5. Enter the following command in an elevated command prompt, replacing `cloudtokenvalue`  with the copied linking code. If the computer requires a proxy server, add parameters `--proxyserver proxyserveraddress` and `--proxyport 8080`. Replace `X.X.X` in `Lansweeper-IT-agent-discovery-X.X.X` with the version number of your installer  

   The version numbers for your installer can be found in your Lansweeper Site. Go to **Discovery (or Scanning)****> Discovery systems****> Download installers/packages > IT Agent installer > Version**and locate your installer.

   ```
   msiexec /i "C:\Path\To\Lansweeper-IT-agent-discovery-X.X.X-windows-x64-installer.msi" /quiet ARGUMENTS="--mode unattended --accepteula 1 --path ""C:\Program Files\Lansweeper IT Agent Discovery"" --cloudtoken cloudtokenvalue"
   ```

Once the installation is complete, you can view your IT Agent Discovery in your Lansweeper Site by going to **Discovery (or Scanning)****> Discovery systems > All systems**. You can view the asset details discovered with your IT Agent Discovery in **Inventory > All assets**.

#### Method 4 - using a deployment script

1. Ensure the connection requirements are met, and your Windows operating system is supported.
2. In your Lansweeper Site, go to **Discovery (or Scanning)****> Discovery systems**, then go to**Link Discovery system**. In the pop-up, select **Create new code**.
3. Choose an expiration date, select **Apply** and select **Copy code**.
4. Run the following .ps1 deployment script, replacing `cloudtokenvalue`  with the copied linking code:

   ```
   # ==============================================
   # Lansweeper IT Agent Discovery Silent Installer
   # ==============================================
   # --- 1. Set Cloud Token Variable ---
   $CloudToken = "cloudtokenvalue" # Replace with your linking code
   # --- 2. Define Download URLs ---
   $InstallerUrl = "https://download.lansweeper.com/stable/windows/it-agent-discovery/latest"
   $ConfigUrl    = "https://download.lansweeper.com/stable/windows/lansweeper-it-agent-installation-config-stable/latest"
   # --- 3. Define Local File Paths ---
   $TempFolder   = "$env:TEMP\LansweeperInstaller"
   $InstallerExe = "$TempFolder\Lansweeper-IT-Agent-Discovery-Installer.exe"
   $ConfigFile   = "$TempFolder\install_config.cfg"
   # --- 4. Prepare Temp Folder ---
   if (Test-Path $TempFolder) {
       Remove-Item -Recurse -Force $TempFolder
   }
   New-Item -ItemType Directory -Path $TempFolder | Out-Null
   # --- 5. Download Installer and Config ---
   Write-Host "Downloading Lansweeper IT Agent Discovery installer..."
   Invoke-WebRequest -Uri $InstallerUrl -OutFile $InstallerExe
   Write-Host "Downloading Lansweeper config file..."
   Invoke-WebRequest -Uri $ConfigUrl -OutFile $ConfigFile
   # --- 6. Insert Cloud Token into Config ---
   Write-Host "Updating config file with cloud token..."
   (Get-Content $ConfigFile) -replace "cloudtokenvalue", $CloudToken | Set-Content $ConfigFile -Encoding UTF8
   # --- 7. Run Silent Install with Config ---
   Write-Host "Running silent installation..."
   Start-Process -FilePath $InstallerExe -ArgumentList "--mode unattended --optionfile `"$ConfigFile`"" -Wait -NoNewWindow
   # --- 8. Cleanup Installer ---
   if (Test-Path $InstallerExe) {
       Remove-Item $InstallerExe -Force
       Write-Host "Installer removed."
   }
   Write-Host "Lansweeper IT Agent Discovery installation completed."
   ```

Once the installation is complete, you can view your IT Agent Discovery in your Lansweeper Site by going to **Discovery (or Scanning)****> Discovery systems > All systems**. You can view the asset details discovered with your IT Agent Discovery in **Inventory > All assets**.

### Uninstall IT Agent Discovery on Windows

To uninstall the IT Agent Discovery on Windows, either:

- Open the **Start** menu, then go to **Control Panel > Add or remove programs** and locate **Lansweeper IT Agent Discovery**. Select **Uninstall**.
- Open a command prompt and enter: `"C:\Program Files\Lansweeper IT Agent Discovery\uninstall.exe" --mode unattended`
- Open a command prompt and enter: `msiexec /x "C:\Path\To\Lansweeper-IT-agent-discovery-X.X.X-windows-x64-installer.msi"`

## Install IT Agent Discovery on Linux

Only silent installs are currently supported for the IT Agent Discovery on Linux.

### Install IT Agent Discovery on Linux silently

#### Method 1 - without using config file

1. Ensure the [connection requirements](/classic/docs/install-it-agent-discovery#connection) are met, and your Linux operating system is supported.
2. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/).
3. Choose the Lansweeper Site to which you want to link the IT Agent Discovery.
4. Go to **Discovery (or Scanning)****> Discovery systems**, then go to **Download installers/packages** and navigate to the **IT Agent Discovery**section.
5. Locate the Linux OS and select **Download IT Agent repository package** for deb or rpm, depending on your Linux distribution.
6. Select **Link Discovery system**. In the pop-up, select **Create new code**.
7. Choose an expiration date, select **Apply** and select **Copy code**.
8. Depending on your Linux distribution, follow the instructions below, replacing `cloudtokenvalue` with the copied linking code:
   - Debian and Ubuntu:
     1. Install the repository package. Copy it to your machine.  

        These packages are required to update Lansweeper repositories: **ca-certificates** and **openssl**.
     2. In a terminal, enter `sudo dpkg -i ./lansweeper-repository.deb`.
     3. Enter `sudo apt update` to make the system aware of the repository.
     4. Enter `sudo env LINKING_CODE=cloudtokenvalue apt install lansweeper-it-agent`.  
        If you're using a proxy server, add the `PROXY_SERVER` and `PROXY_PORT` parameters:  

        ```
        sudo env LINKING_CODE=cloudtokenvalue PROXY_SERVER=<your_proxy_server> PROXY_PORT=<your_proxy_port> apt install lansweeper-it-agent
        ```

        `PROXY_SERVER` should be set to the IP address or FQDN of your proxy server, and `PROXY_PORT` to the port number it uses.
     5. Once there is an update, update the package by entering `sudo apt update && apt upgrade lansweeper-it-agent`.
   - Red Hat, CentOS, and SUSE:
     1. Install the repository package. Copy it to your machine.
     2. In a terminal, enter `sudo yum install ./lansweeper-repository-1-0-x86_64.rpm`.
     3. Enter `sudo yum update` to make the system aware of the repository.
     4. Enter `sudo env LINKING_CODE=cloudtokenvalue yum install lansweeper-it-agent.x86_64`.   
        If you're using a proxy server, add the `PROXY_SERVER` and `PROXY_PORT` parameters:  

        ```
        sudo env LINKING_CODE=cloudtokenvalue PROXY_SERVER=<your_proxy_server> PROXY_PORT=<your_proxy_port> yum install lansweeper-it-agent.x86_64
        ```

        `PROXY_SERVER` should be set to the IP address or FQDN of your proxy server, and `PROXY_PORT` to the port number it uses.
     5. Once there is an update, update the package by entering `sudo yum update && yum upgrade lansweeper-it-agent.x86_64`.

Once the installation is complete, you can view your IT Agent Discovery in your Lansweeper Site by going to **Discovery (or Scanning)****> Discovery systems > All systems**. You can view the asset details discovered with your IT Agent Discovery in **Inventory > All assets**.

#### Method 2 - using a deployment script and config file

1. Ensure the connection requirements are met and your macOS operating system is supported.
2. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/).
3. Choose the Lansweeper Site to which you want to link the IT Agent Discovery.
4. Go to **Discovery (or Scanning)****> Discovery systems**and select **Link Discovery system**. In the pop-up, select **Create new code**.
5. Choose an expiration date, select **Apply** and select **Copy code**.
6. Run the following .sh deployment script, replacing `cloudtokenvalue` with the copied linking code. Next, make it executable by running `chmod +x “filename“`.

   ```
   #!/bin/bash
   set -e

   # ----------------------------
   # Lansweeper IT Agent Installer Script
   # ----------------------------

   # Set your cloud token here
   cloudtoken="cloudtokenvalue"

   # Check system architecture
   ARCH=$(uname -m)
   if [[ "$ARCH" != "x86_64" && "$ARCH" != "amd64" ]]; then
       echo "   Lansweeper IT Agent Discovery is only available for amd64 (x86_64)."
       echo "   You are running: $ARCH"
       echo "   Please use an x86_64 VM or Docker container with --platform linux/amd64."
       exit 1
   fi

   # Check curl/wget
   if ! command -v curl &>/dev/null && ! command -v wget &>/dev/null; then
       echo "   Neither curl nor wget found. Please install one of them."
       echo "   Example (Debian/Ubuntu): sudo apt install curl -y"
       echo "   Example (RHEL/Fedora):   sudo yum install curl -y"
       exit 1
   fi

   # Detect distro family
   if [ -f /etc/debian_version ]; then
       PKGTYPE="deb"
       INSTALLER_URL="https://download.lansweeper.com/deb-repository/stable/latest"
       INSTALLER_PATH="/tmp/lansweeper-it-agent.deb"
       INSTALL_CMD="sudo dpkg -i $INSTALLER_PATH || sudo apt-get install -f -y"
   elif [ -f /etc/redhat-release ] || [ -f /etc/centos-release ] || [ -f /etc/fedora-release ]; then
       PKGTYPE="rpm"
       INSTALLER_URL="https://download.lansweeper.com/rpm-repository/stable/latest"
       INSTALLER_PATH="/tmp/lansweeper-it-agent.rpm"
       INSTALL_CMD="sudo rpm -i $INSTALLER_PATH || sudo yum install -f -y"
   else
       echo " Unsupported Linux distribution."
       exit 1
   fi

   echo " Downloading Lansweeper IT Agent Discovery installer for $PKGTYPE..."

   # Download installer
   if command -v curl &>/dev/null; then
       curl -L -o "$INSTALLER_PATH" "$INSTALLER_URL"
   else
       wget -O "$INSTALLER_PATH" "$INSTALLER_URL"
   fi

   echo " Installing Lansweeper IT Agent Discovery with cloud token..."

   # Create config file with cloudtoken
   CONFIG_PATH="/etc/lansweeper-it-agent/itagent.conf"
   sudo mkdir -p /etc/lansweeper-it-agent
   cat <<EOF | sudo tee "$CONFIG_PATH" >/dev/null
   {
     "cloudtoken": "$cloudtoken"
   }
   EOF

   # Silent install
   eval "$INSTALL_CMD"

   # Remove installer
   rm -f "$INSTALLER_PATH"

   echo "   Installation completed."
   echo "   Cloud token has been set in: $CONFIG_PATH"
   echo "   If your token changes, re-run this script to update it."
   ```

Once the installation is complete, you can view your IT Agent Discovery in your Lansweeper Site by going to **Discovery (or Scanning)****> Discovery systems > All systems**. You can view the asset details discovered with your IT Agent Discovery in **Inventory > All assets**.

### Uninstall IT Agent Discovery on Linux

To uninstall IT Agent Discovery Linux, open your terminal and run the following commands, depending on your environment.

Debian and Ubuntu: `sudo dpkg -r lansweeper-it-agent`

Red Hat, CentOS, and SUSE: `sudo rpm -e lansweeper-it-agent`

## Install IT Agent Discovery on macOS

There are multiple you can use to install the IT Agent Discovery on a macOS computer.

If the computer running IT Agent Discovery requires a proxy server, use a silent install method.
### Install IT Agent Discovery on macOS interactively

1. Ensure the connection requirements are met, and your macOS operating system is supported.
2. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/ "https://app.lansweeper.com/").
3. Choose the Lansweeper Site to which you want to link the IT Agent Discovery.
4. Go to **Discovery (or Scanning)****> Discovery systems**, then go to**Download installers/packages** and navigate to the **IT Agent Discovery**section.
5. Locate the macOS with DMG format. Select **Download IT Agent disk image** to download the installer.
6. Run the IT Agent Discovery installer on your macOS machine. In the resulting pop-up, double-click **the name of the installer**, then **Next**.  
   If the software is blocked, click the Apple icon in the upper-left corner of your screen. Select **System Preferences** **> Security & Privacy** **> Open Anyways**.
7. Select **I accept the agreement > Next**.
8. Select the installation directory. By default, the directory is **/Library/Application Support/Lansweeper IT Agent Discovery**. Select **Next**.
9. While keeping the installer open, open a browser and navigate to your Lansweeper Site.
10. Go to **Discovery (or Scanning)****> Discovery systems**and select **Link Discovery system**. In the pop-up, select **Create new code**.
11. Choose an expiration date, select **Apply** and select **Copy code**.
12. Paste the Lansweeper linking code in the installer, then select **Next**.

Once the installation is complete, you can view your IT Agent Discovery in your Lansweeper Site by going to **Discovery (or Scanning)****> Discovery systems > All systems**. You can view the asset details discovered with your IT Agent Discovery in **Inventory > All assets**.

### Install IT Agent Discovery on macOS silently

#### Method 1 - DMG Deployment

1. Ensure the connection requirements are met and your macOS operating system is supported.
2. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/).
3. Choose the Lansweeper Site to which you want to link the IT Agent Discovery.
4. Go to **Discovery (or Scanning)****> Discovery systems**, then go to **Download installers/packages** and navigate to the **IT Agent Discovery**section.
5. Select **Download IT Agent disk image**to download and store the .dmg file on your machine.
6. Go to **Discovery (or Scanning)****> Discovery systems**and select **Link Discovery system**. In the pop-up, select **Create new code**.
7. Choose an expiration date, select **Apply** and select **Copy code**.
8. In an elevated command prompt, enter `hdiutil attach Lansweeper-IT-agent-discovery-0.9.0-16-osx-installer.dmg` to mount the dmg file.
9. Enter `cd "/Volumes/Lansweeper IT Agent Discovery"` to navigate to the volume.
10. Enter the following command, replacing `cloudtokenvalue` with the copied linking code and replacing X.X.X in `Lansweeper-IT-agent-discovery-X.X.X-X-osx-installer.dmg` with the version number of your installer. If the computer requires a proxy server, add parameters `--proxyserver proxyserveraddress` and `--proxyport 8080`.  
      

    ```
    sudo Lansweeper-IT-agent-discovery-X.X.X-X-osx-installer.app/Contents/MacOS/installbuilder.sh --mode unattended --accepteula 1 --path "/Library/Application Support/Lansweeper IT Agent Discovery" --cloudtoken cloudtokenvalue
    ```

Once the installation is complete, you can view your IT Agent Discovery in your Lansweeper Site by going to **Discovery (or Scanning)****> Discovery systems > All systems**. You can view the asset details discovered with your IT Agent Discovery in **Inventory > All assets**.

#### Method 2 - PKG deployment

1. Ensure the [connection requirements](/classic/docs/install-it-agent-discovery#connection) are met, and your macOS operating system is supported.
2. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/).
3. Choose the Lansweeper Site to which you want to link the IT Agent Discovery.
4. Go to **Discovery (or Scanning)****> Discovery systems**, then go to **Download installers/packages** and navigate to the **IT Agent Discovery**section.
5. Select **Download IT Agent package** and **IT Agent Discovery macOS package silent installation configuration**to download both files.
6. Go to **Discovery (or Scanning)****> Discovery systems**and select **Link Discovery system**. In the pop-up, select **Create new code**.
7. Choose an expiration date, select **Apply** and select **Copy code**.
8. In the downloaded **IT Agent package silent installation configuration** file, replace `cloudtokenvalue` with your copied linking code and modify the content to suit your needs. If the computer requires a proxy server, remove the `#` for `proxyserver=myproxyserver.domain.local` and `proxyport=8080`.  
     

   ```
   #!/bin/sh
   PreinstallConfig="/tmp/LansweeperITAgent-Preinstall.cfg" # Don't change this path!
   [ -f $PreinstallConfig ] && chmod 744 $PreinstallConfig
   cat > $PreinstallConfig << EOF
   mode=unattended
   accepteula=1
   path=/Library/Application Support/Lansweeper IT Agent Discovery
   cloudtoken=cloudtokenvalue
   #proxyserver=myproxyserver.domain.local 
   #proxyport=8080
   EOF
   chmod 744 $PreinstallConfig
   ```
9. Enter the following command: `sudo ./tmp/LansweeperPreinstallScript.sh`
10. Enter the following command, replacing X.X.X in `LansweeperITDiscovery-X.X.X` with the version number of your installer: `sudo installer -pkg Lansweeper-IT-agent-discovery-X.X.X-osx-installer.pkg -target /`  
    Note: The version numbers for your installer can be found in your Lansweeper Site. Go to **Discovery (or Scanning)****> Discovery systems > Download installers/packages**.

Once the installation is complete, you can view your IT Agent Discovery in your Lansweeper Site by going to **Discovery (or Scanning)****> Discovery systems > All systems**. You can view the asset details discovered with your IT Agent Discovery in **Inventory > All assets**.

#### Method 3 - PKG deployment using a script

1. Ensure the connection requirements are met and your macOS operating system is supported.
2. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/).
3. Choose the Lansweeper Site to which you want to link the IT Agent Discovery.
4. Go to **Discovery (or Scanning)****> Discovery systems**and select **Link Discovery system**. In the pop-up, select **Create new code**.
5. Choose an expiration date, select **Apply** and select **Copy code**
6. Run the following .sh deployment script, replacing `cloudtokenvalue` with the copied linking code. Next, make it executable by running `chmod +x “filename“`.

   ```
   #!/bin/bash
   # ==============================================
   # Lansweeper IT Agent Discovery Silent Installer (macOS)
   # ==============================================
   # --- 1. Set Cloud Token Variable ---
   CLOUDTOKEN="cloudtokenvalue"   # Replace with your linking code
   # --- 2. Define Download URLs ---
   INSTALLER_URL="https://download.lansweeper.com/stable/MAC/it-agent-discovery-pkg/latest"
   CONFIG_URL="https://download.lansweeper.com/stable/MAC/pkg-scripts/it-agent-discovery-stable/latest"
   # --- 3. Define Local File Paths ---
   WORKDIR="/tmp/lansweeper-install"
   INSTALLER_PKG="$WORKDIR/lansweeper-it-agent-discovery.pkg"
   CONFIG_SCRIPT="$WORKDIR/it-agent-config.sh"
   # --- 4. Prepare Work Directory ---
   rm -rf "$WORKDIR"
   mkdir -p "$WORKDIR"
   # --- 5. Download Installer and Config ---
   echo "Downloading Lansweeper IT Agent Discovery installer..."
   curl -L "$INSTALLER_URL" -o "$INSTALLER_PKG"
   echo "Downloading Lansweeper config script..."
   curl -L "$CONFIG_URL" -o "$CONFIG_SCRIPT"
   # --- 6. Insert Cloud Token into Config ---
   echo "Updating config script with cloud token..."
   sed -i.bak "s/cloudtokenvalue/$CLOUDTOKEN/g" "$CONFIG_SCRIPT"
   rm -f "$CONFIG_SCRIPT.bak"
   # --- 7. Run Silent Install ---
   echo "Running silent installation..."
   sudo installer -pkg "$INSTALLER_PKG" -target /
   # --- 8. Apply Config Script (if required by Lansweeper docs) ---
   echo "Applying configuration..."
   sudo bash "$CONFIG_SCRIPT"
   # --- 9. Cleanup ---
   rm -f "$INSTALLER_PKG"
   echo "Installer removed."
   echo " Lansweeper IT Agent Discovery installation completed."
   ```

Once the installation is complete, you can view your IT Agent Discovery in your Lansweeper Site by going to **Discovery (or Scanning)****> Discovery systems > All systems**. You can view the asset details discovered with your IT Agent Discovery in **Inventory > All assets**.

### Uninstall IT Agent Discovery on macOS

To uninstall IT Agent Discovery on macOS, you can either:

- Go to **/Library/Application Support/Lansweeper IT Agent Discovery** and execute **uninstall.app**.
- Open a command prompt and enter:

  ```
  sudo "/Library/Application Support/Lansweeper IT Agent Discovery/uninstall.app/Contents/MacOS/installbuilder.sh" --mode unattended
  ```

## Next steps

Now that you've finished installing IT Agent Discovery, learn how to [configure IT Agent Discovery](/classic/docs/configure-it-agent-discovery).

## Frequently asked questions (FAQ)

For a list of answers to frequently asked questions, check out [IT Agent Discovery: Frequently Asked Questions](/classic/docs/it-agent-discovery-frequently-asked-questions).
