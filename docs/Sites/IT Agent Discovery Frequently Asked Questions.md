<!-- # IT Agent Discovery: Frequently Asked Questions -->

Lansweeper's IT Agent Discovery is a lightweight, cross-platform scanning agent that can run on Windows, Linux, and Mac computers. If you'd like to know more about IT Agent Discovery, head on over to [Install IT Agent Discovery](/docs/install-it-agent-discovery).

## Frequently asked questions (FAQ)

- [Can I use a single command to deploy IT Agent to multiple computers over an extended period of time?](#q1)
- [When should I use IT Agent over LsAgent?](#q2)
- [During the installer I get the message: “There has been an error. Could not start Lansweeper IT Agen...](#q3)
- [What are the installer return codes and possible error messages?](#q4)
- [Why is the size of the IT Agent installer rather big?](#q5)
- [What is the scan frequency of the IT Agent?](#q6)
- [Can I force the IT Agent to perform an immediate ad hoc rescan of the asset(s)?](#q7)
- [How many IT Agent installations can I link to my Lansweeper Site?](#q8)
- [Can I use another service account to run the IT Agent services(s) instead of Local System?](#q9)
- [Why am I not seeing all asset data (yet)?](#q10)
- [How do I solve duplicate issues?](#q11)
- [Can I disable the auto-update behavior?](#q12)
- [Can I unlink the IT Agent installation from my Lansweeper Site?](#q13)
- [If I uninstall IT Agent on the asset, could you also unlink the installation in your Lansweeper Site...](#q14)
- [Do scan exclusions apply to IT Agent?](#q15)
- [I’m not seeing an asset for IT Agent/Network Discovery in my inventory. Why is it not appearing?](#q16)
- [How can I deal with the license limit when using Lansweeper Discovery in Configuration > License sta...](#q17)
- [I’m currently using Lansweeper On-premises with Lansweeper Site. Can I use Lansweeper Discovery in t...](#q18)
- [How do I avoid duplicates when using Lansweeper Discovery together with Lansweeper On-Premises in my...](#q19)
- [Why do I receive the “Unable to locate package lansweeper-it-agent“ message when installing IT Agent...](#q20)
- [My IT Agent install keeps failing due to a previous corrupt install. How can I completely remove any...](#q21)
- [Will .NET be required for IT Agent for Linux Devices?](#q22)
- [IT Agent install keeps failing and I’m seeing this message in the log file: Ensure TLS1.2 is enabled...](#q23)
- [My discovery results aren’t showing up in my Lansweeper Site, how can I troubleshoot this?](#q24)
- [Does IT Agent Discovery update automatically on Linux?](#q25)
- [Why does the installation of IT Agent fail with “Unable to initialize installer” on Windows?](#q26)
- [Do we need to replace the linking code of the already-existing IT Agent, or is it only required to h...](#q27)

### Can I use a single command to deploy IT Agent to multiple computers over an extended period of time?

Yes, we've extended the linking code duration, so you can choose how long a single linking code should remain valid (1 day, 1 month, 3 months).To create a new linking code:

1. In your site, go to **Scanning > Discovery systems**, and select **Link discovery system**.
2. Select **Create new** **code**, select an expiration period and select **Apply**.
3. Select **Copy code**, and paste it into the installer.

### When should I use IT Agent over LsAgent?

- IT Agent can send discovery results directly to your Lansweeper Site, eliminating the need for an on-premises Lansweeper scanning server.
- Like LsAgent, IT Agent can auto-update on Windows. Additionally, IT Agent can auto-update on Linux and macOS platforms as well.
- IT Agent gathers additional data from devices, such as user information on macOS. This data is mapped to your Lansweeper Site, providing enhanced visibility.
- IT Agent supports silent installation on Windows, similar to LsAgent, but is also compatible with Linux and macOS systems.
- IT Agent for Windows is built on .NET 6.0, offering a reduced vulnerability risk compared to LsAgent for Windows, which uses .NET FW 4.8.
- IT Agent can be instructed to scan its assets on demand using the Lansweeper Cloud API. Unlike LsAgent, where a scan must be force-started manually, IT Agent provides a streamlined process for immediate asset scanning.

### During the installer I get the message: “There has been an error. Could not start Lansweeper IT Agent Discovery Hub Service. The application will exit now.” How can I solve it?

We've observed that this process may run slower on certain machines. The slowdown could be due to factors such as a slow hard disk, low memory, or limited CPU resources. We are currently investigating the root cause of this issue.To resolve this message during the installation:

1. Press **Windows + R** to open **Run**.
2. Enter **regedit** to open the **Registry Editor**.
3. Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control` or copy-paste the location in the navigation bar.
4. In the **Control registry** folder, move to the right side and create a new DWORD (32-bit) Value called “ServicesPipeTimeout”.
5. In the **Edit Value** window, change the **Base** to **Decimal**.
6. In the **Value Data** field, enter a value of “600000”.
7. Select **OK**.
8. Exit the Registry Editor and restart your system.Failing to restart will prevent the changes from being applied.
9. After restarting, run the IT Agent installer.

### What are the installer return codes and possible error messages?

When the installer terminates with an exit code during the pre-installation phase, no actions have been executed with no files or changes left behind.In the event the installer terminates during the installation, a rollback will occur and no files or changes will be left behind.The ranges are the following:

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

When using the MacOS PKG, the installer command only returns 0 (success) or 1 (general error). To get the specific exit code similar to the list above, this extra log file is available at `/tmp/Lansweeper-IT-Agent-Discovery_exitcode.log`.   
This file only contains the specific exit code as an integer value.

### Why is the size of the IT Agent installer rather big?

Currently, the IT Agent installer has all the core next-generation discovery components, resulting in a bigger installer.To cater to mass deployments over metered connections, we're looking into decreasing the size by stripping redundant parts and keeping only those required for local computer scanning.

### What is the scan frequency of the IT Agent?

IT Agent performs a daily scan of the computer it’s installed on. You can change this frequency of 24 hours in your Lansweeper Site. For detailed instructions, see [Configure IT Agent Discovery](/docs/configure-it-agent-discovery).

### Can I force the IT Agent to perform an immediate ad hoc rescan of the asset(s)?

IT Agent performs a rescan every 24 hours by default. You can also force a scan using the API. For more information on using the API, see [Perform actions | Documentation](https://developer.lansweeper.com/docs/data-api/guides/actions#request-the-scan).

### How many IT Agent installations can I link to my Lansweeper Site?

As many as you like, there's no limit.

### Can I use another service account to run the IT Agent services(s) instead of Local System?

Yes, you can:

1. Go to Windows > Services.
2. Double click the Lansweeper **IT Agent Discovery Hub** or **Sensor** or **Update** service.
3. Go to the **Log On** tab.
4. Select **This account** and enter the new service account.This account needs to be a local administrator on the machine running IT Agent, in order to retrieve all asset details. You can also use a least privileged account instead, but it won't be able to get all asset details as mentioned in the link.

### Why am I not seeing all asset data (yet)?

We’re remapping all data to a universal data model. As we’re doing this in phases, you’ll only see certain data sections available on the asset page.Currently, these sections are available:

- HW
- Operating System
- Software
- Monitor

This list is continuously being extended.

### How do I solve duplicate issues?

1. In your Lansweeper Site, go to **Scanning > Discovery systems**.
2. Select **IT Agent-based**.
3. Select the IT Agent installation.
4. Select **Delete**.
5. Select **Yes**.

### Can I disable the auto-update behavior?

Auto update is enabled by default in an 8 hour time window varying between 08:00 am and 06:00 pm. Though not recommended, you can still disable the auto-update behavior after installation by running the following command on the machine running IT Agent:

```
sc config "Lansweeper IT Agent Discovery Update service" start= disabled sc stop "Lansweeper IT Agent Discovery Update service"
```

You can also disable auto-updates for specific groups in your Lansweeper Site by following these steps:

1. In your Lansweeper Site, navigate to **Scanning > Discovery groups**.
2. Select the Discovery group.
3. Enable the **Pause auto-update** toggle.

This will prevent the group's Discovery Systems from applying updates automatically, although currently, updates will still be downloaded.To block downloads entirely in the meantime, you can block outgoing connections by executing the following steps:

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

This will still allow access to discovery-gateway.lansweeper.com, which is needed for data synchronization.Please note that your Lansweeper Site requires a minimum version of IT Agent to maintain synchronization. To that end, we recommend to re-enabling the auto-update feature when possible.

### Can I unlink the IT Agent installation from my Lansweeper Site?

Yes, you can:

1. In your Lansweeper Site, go to **Scanning > Discovery systems**.
2. Select **IT Agent-based**.
3. Select the IT Agent installation.
4. Select **Delete**.
5. Select **Yes**.

After unlinking, IT Agent will continue to scan, and will keep trying to send its data to your Lansweeper Site. To avoid this from happening, we recommend you uninstall the IT Agent on the machine it was installed on. We’re looking to automate this process so you don’t have to manually uninstall IT Agents you no longer want to track.When doing an auto uninstall of the IT Agent on Linux, it won't delete the new user and group added as its required to correctly remove the other data. You can still cleanup this user and group manually.

### If I uninstall IT Agent on the asset, could you also unlink the installation in your Lansweeper Site?

We like to promote centralized management from within your Lansweeper Site. When you decide to unlink the IT Agent installation, we plan on auto-uninstalling IT Agent to keep a clean system.If you still do a manual uninstall on the machine itself, we could go for a global option in your Lansweeper Site that auto-archives installations of type IT Agent and/or IT and keeps/deletes data.Currently, unlinking from your Lansweeper Site means the asset data is also removed but we plan on offering you the option to choose whether or not to keep the data when unlinking the IT Agent from your Lansweeper Site.

### Do scan exclusions apply to IT Agent?

No, scan exclusions only apply to scan servers (and indirectly LsAgent installations) from Lansweeper On-prem installations.

IT Agent by default gathers information about the asset it's installed on, including data on Hyper-V virtual guests and external monitors.

Ensure your IT Agents are not part of the **Default Group** found in **Scanning > Discovery groups**. Instead, assign them to another group, such as **Default Group IT Agent**.

Currently, if you don’t want an IT Agent to report specific assets, and it's already in **Default Group IT Agent**, you need to remove the IT Agent.

To remove an IT Agent:

1. Go to **Scanning > Discovery systems > IT Agent-based**.
2. Select the IT Agent you want to remove.
3. In the **IT Agent Sensor Detail** view, select **Delete source**.

For Network Discovery, IP address or range exclusions can be set up within each agentless discovery action.

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
2. Set up discovery exclusions: go to **Scanning > Discovery actions**, and add exclusions to your**IT Agent-based actions** to ensure specific assets aren’t discovered by Lansweeper IT Agent Discovery.
3. Resolve duplicates manually by going to **Inventory > Duplicate conflicts**.

#### Option 2

If the above is not an option:

1. Remove IT Agent Discovery from your Lansweeper Site:
   1. In your Lansweeper Site, go to **Scanning > Discovery systems**.
   2. Select **IT Agent-based**.
   3. Select the IT Agent installation.
   4. Select **Delete**.
   5. Select **Yes**.
2. Create a new site and link it to your IT Agent Discovery:
   1. Create a new site using [this link](https://app.lansweeper.com/create-site?path= "https://app.lansweeper.com/create-site?path="), or by selecting **Change site > Create new site**.
   2. In your new site, select **Access empty site**.
   3. Go to **Scanning > Discovery systems**, then go to**Download installers/packages > Download IT Agent****installer**.
   4. Run the downloaded installer.
   5. Select **Yes**to allow the app to make changes to your device.
   6. Select **I accept the agreement**.
   7. Choose the installation directory and select **Next**.
   8. While keeping the installer open, open a browser and navigate to your Lansweeper Site.
   9. Select**Link discovery system**. In the pop-up, select **Create new code**.
   10. Choose an expiration date, select **Apply** and select **Copy code**.
   11. Paste the Lansweeper linking code in the installer, then select **Next**.
   12. Select **Next**to begin the installation.

### Why do I receive the “Unable to locate package lansweeper-it-agent“ message when installing IT Agent on Linux?

Ensure you have outgoing access to [https://discovery-gateway.lansweeper.com/](https://discovery-gateway.lansweeper.com/ "https://discovery-gateway.lansweeper.com/") and [https://download.lansweeper.com](https://download.lansweeper.com/ "https://download.lansweeper.com") on the machine you want to install IT Agent on.

### My IT Agent install keeps failing due to a previous corrupt install. How can I completely remove any IT Agent reference from my computer and install IT Agent again?

Download the latest IT Agent installer for Windows from "[https://app.lansweeper.com > Scanning > Discovery systems > Downloads/packages](https://app.lansweeper.com)" and save the following code as a **ITAgentCleanup.bat**.

```
        @echo off

        :: BatchGotAdmin
        :-------------------------------------
        REM  --> Check for permissions
        >nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

        REM --> If error flag set, we do not have admin.
        if '%errorlevel%' NEQ '0' (
            echo Requesting administrative privileges...
            goto UACPrompt
        ) else ( goto gotAdmin )

        :UACPrompt
            echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
            set params = %*:"=""
            echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

            "%temp%\getadmin.vbs"
            del "%temp%\getadmin.vbs"
            exit /B

        :gotAdmin
            pushd "%CD%"
            CD /D "%~dp0"
        :--------------------------------------
        :: Uninstall Lansweeper IT Agent
        "C:\Program Files\Lansweeper IT Agent Discovery\uninstall.exe" --mode unattended

        :: Sleep for x seconds to continue
        TIMEOUT /T 300

        :: Ensure lingering services are stopped and removed
        sc stop "Lansweeper IT Agent Discovery Hub Service"
        sc delete "Lansweeper IT Agent Discovery Hub Service"
        sc stop "Lansweeper IT Agent Discovery Sensor Service"
        sc delete "Lansweeper IT Agent Discovery Sensor Service"
        sc stop "Lansweeper IT Agent Discovery Update Service"
        sc delete "Lansweeper IT Agent Discovery Update Service"

        :: Sleep for x seconds to continue
        TIMEOUT /T 60

        :: Delete default install directory
        del /S "C:\Program Files\Lansweeper IT Agent Discovery\*"

        :: Cleanup first reg location
        for /f "delims="  %%a in ('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Lansweeper" ^| find "Lansweeper IT Agent Discovery"') do (set "regs=%%a")
        echo %regs%
        reg delete "%regs%" /f

        :: Cleanup second reg location
        for /f "delims="  %%a in ('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall" ^| find "Lansweeper IT Agent Discovery"') do (set "regs=%%a")
        echo %regs%
        reg delete "%regs%" /f

        :: Reinstall Lansweeper IT Agent
        :: Todo: in the following line, correct the path to the actual location of the installer and also the cloudtokenvalue from your LS Site in https://app.lansweeper.com > Scanning > Discovery systems > Link discovery system. After doing so, uncomment the last line (removing the ::) and run this file
        :: C:\Temp\Lansweeper-IT-agent-discovery-0.23.2-windows-x64-installer.exe --mode unattended --accepteula 1 --path "C:\Program Files\Lansweeper IT Agent Discovery" --cloudtoken cloudtokenvalue
```

Edit the last line in a text editor and run it on your computer.

### Will .NET be required for IT Agent for Linux Devices?

.NET8 is a dependency for IT Agent on Linux, Windows and macOS. The [installer flow](/docs/install-it-agent-discovery#LinuxSilent) handles the dependency automatically as a self-contained package.

### The IT Agent Discovery installation keeps failing and I’m seeing this message in the log file: Ensure TLS1.2 is enabled, Internet access is available, you entered a linking code which is (still) valid, and run the installer again.

Ensure the computer on which you’re running the installer is allowed to use curl to make outbound connections to these URLs. Install IT Agent Discovery - Lansweeper Community. Ensure `C:\Program Files\Lansweeper IT Agent Discovery\resources\curl.exe` is allowed by Microsoft Defender and isn’t blocked by Attack Surface Reduction configuration.

### My discovery results aren’t showing up in my Lansweeper Site, how can I troubleshoot this?

- Check if Lansweeper Site's status is OK by checking Lansweeper Status (Data pipeline > "Modernized Discovery")
- Check if these APIs are working:
  - [Config API](https://discovery-gateway.lansweeper.com/config-api/ready) (Send configuration from Lansweeper Site to Lansweeper Discovery)
  - [Syncer API](https://discovery-gateway.lansweeper.com/syncer-api/ready) (Receive data in Lansweeper Site from Lansweeper Discovery)
  - [Notification API](https://discovery-gateway.lansweeper.com/notification-api/ready) (Add/update notifications in Lansweeper Site about Lansweeper Discovery)
  - [Recognition API](https://discovery-gateway.lansweeper.com/recognition-api/ready) (Recognize assets in Lansweeper Site from received data from Lansweeper Discovery)
- Ensure either the IT Agent or Network Discovery service is running by opening services.msc on Windows or Activity Monitor app on macOS or `sudo ps -aux | less` on Linux
- Check the logs for errors using [paths and logs](/docs/install-it-agent-discovery#pathsandlogs) or [network discovery paths and logs](/docs/install-network-discovery#pathsandlogs)

### Does IT Agent Discovery update automatically on Linux?

Yes, it updates automatically using your Linux package manager, such as **apt** or **yum**. For more information on automating updates and upgrades, you can refer to resources such as [apt - Automate Updates and Upgrade](https://askubuntu.com/questions/1331557/automate-updates-and-upgrade).

### Why does the installation of IT Agent fail with “Unable to initialize installer” on Windows?

This error occurs when the environment variable **TMP** or **TEMP** refers to a path that doesn’t exist. To resolve the issue, update the environment variable to point to a valid directory:

1. Press **Windows + R** to open the Run dialog.
2. Type `sysdm.cpl` and press **Enter** to open **System Properties**.
3. In the **Advanced** tab, select **Environment Variables**.
4. Locate the **TMP** or **TEMP** variables under **User variables** or **System variables**.
5. Select the variable and select **Edit**.
6. Update the **Variable value** to point to a valid folder path, such as `C:\Windows\Temp`.
7. Select **OK** to save changes.
8. Finally, retry the installation.

### Do we need to replace the linking code of the already-existing IT Agent, or is it only required to have a valid linking code during the installation?

The IT Agent Discovery linking code is only needed during installation to associate the agent with the correct Lansweeper Site. Once the code expires, the IT Agent Discovery service will continue sending scanned data to the site, so there's no need to replace the code.
