<!-- # Introduction to the LsPush scanning agent for Windows -->
[Lansweeper](https://www.lansweeper.com/) includes [several scanning methods](https://www.lansweeper.com/resources/lansweeper-scanning-guide/) to scan the assets in your network. You can scan the Linux, Unix, Mac and Windows computers, VMware servers and other devices in your network without installing any Lansweeper software on the machines you're scanning.

However, for Windows computers, you can choose to perform your scans with a scanning agent. Lansweeper's scanning agent is called LsPush.

## What is LsPush

LsPush is a small executable that scans the computer locally when ran on a Windows computer. The scan results can be sent directly to your Lansweeper server for automatic processing, or stored in a file which can be imported into your Lansweeper installation later on.

LsPush is a true scanning agent, as the executable itself scans the computer and does not require your Lansweeper installation to perform the scan.

LsPush is not a program that is permanently installed on your computers. It is a lightweight executable that must simply be run on the Windows computer whenever you want to scan the machine. Running the executable can be fully automated by integrating the scanning agent into logon scripts, group policies or scheduled tasks.

## Where to find LsPush

The executable can be found in the folder at `Program Files (x86)\Lansweeper\Client` on your Lansweeper scanning server, i.e. the server hosting your Lansweeper Server service. It does not need to be downloaded separately.  


When updating your Lansweeper installation, the latest version of the LsPush executable is automatically added to the Client folder on your Lansweeper server. Make sure to use the latest LsPush executable to scan your machines, as scanning with old agents can cause incomplete data to be returned. If you have just updated Lansweeper and are scanning with LsPush in a logon script, group policy or scheduled task, copy the up-to-date LsPush to any folder referenced by your script, policy or task.

## Why use LsPush for scanning

LsPush largely scans the same data as agentless scanning methods. However, it has several advantages over agentless scanning because it scans locally:

- It does not require you to submit scanning credentials.
- It does not require administrative privileges to be able to scan.
- It does not require you to reconfigure your Windows computers' firewalls for scanning.
- It is immune to almost all scanning errors, including access denied and firewall errors.
- It can scan computers of your remote employees, after which the results can be imported back into Lansweeper.
- It can scan computers running a Windows Home edition.
- It generates very little network traffic, only around 40 kB for one scanned computer.
- It can be integrated into logon scripts, group policies, scheduled tasks, custom scripts etc.

## How to scan with LsPush

There are many ways to run LsPush on your machines. Basically any process that can run the LsPush executable, preferably with a parameter, can trigger LsPush scans of your machines. LsPush scans can be fully automated for instance by integrating the scanning agent into logon scripts, group policies or scheduled tasks.   
Below are some methods to perform LsPush scans.

- **Using a group policy**: this allows you to scan domain computers as soon as users log into them.  

  [This knowledge base article](/classic/docs/scan-windows-computers-with-lspush-in-a-group-policy) contains a complete guide on how to scan with LsPush in a group policy.
- **Using a scheduled task**: this allows you to scan workgroup computers as soon as users log into them.  

  [This knowledge base article](/classic/docs/scan-windows-computers-with-the-lspush-scanning-agent-in-a-scheduled-task) contains a complete guide on how to scan with LsPush in a scheduled task.
- **From a USB drive**: this can be used to scan stock computers.  

  [This knowledge base article](/classic/docs/scan-windows-computers-from-a-usb-drive-with-lspush) contains a complete guide on how to scan from a USB drive with LsPush.
- **By manually launching the executable**: this can be used to scan remote or stock computers.  

  [This knowledge base article](/classic/docs/scan-individual-windows-computers-with-the-lspush-scanning-agent) contains a complete guide on how to run manual LsPush scans on computers.

## How data scanned by LsPush reaches your Lansweeper installation

How the scanned data reaches your Lansweeper installation depends on how you are running LsPush and which parameters you are using:

- **Direct server connection:**  
  If the machines you're scanning are in the same network as your Lansweeper installation or have a connection to the installation through for instance a VPN, scanned data can automatically be sent back to Lansweeper. For this, the name of your Lansweeper scanning server must be included in your command. By default, your Lansweeper server listens for agent data on port 9524, but a custom port can also be configured by submitting it in the **Configuration > Server Options**section of the web console, and restarting the Lansweeper Server service.

  

    

  From Lansweeper version 6.0.100 onward, scanning servers running Windows 7, Windows Server 2008 R2 or a more recent operating system use HTTPS instead of HTTP to handle incoming requests by the LsPush scanning agent. As a result, only the most recent version of LsPush will still be able to connect to 6.0.100 scanning servers. Make sure to implement the new executable in any logon scripts, group policies or other scheduled jobs you're using to run the scanning agent. Use of older LsPush versions will result in socket errors similar to the one below. Connection to server failed Socket Error # 10054 Connection reset by peer.
- **Manual import**If the machines you're scanning do not have a connection to your Lansweeper installation, scanned data can be saved in text files. These files must be placed in the import folder found at `Program Files (x86)\Lansweeper\Service\import` on your Lansweeper scanning server, where they are automatically processed. When the files have disappeared from the import folder, the import process has completed and the machines can be found in the web console.

    

  It is critical that no changes are made to the extension or contents of the files prior to placing them in the import folder. File changes can cause import failures.

  The scan files are compressed and hence not human-readable in their raw form. The Lansweeper scanning service decompresses and reads the data when the files are imported.

## What parameters LsPush accepts

The executable recognizes and accepts several parameters:

- When LsPush is initiated without parameters, by simply double-clicking the executable, the computer is scanned, an on-screen progress bar is shown and the scan results are attached as a text file to a draft email. This is so you can easily send the results to whoever is managing your Lansweeper installation, where the results can be imported.
- **<IP address or name of your Lansweeper scanning server>**   
  When included in your command, the computer is silently scanned and the scanned data is sent directly to your Lansweeper scanning server for import. By default, your Lansweeper server listens for LsPush data on port 9524.  

  ```
  Examples:   
  lspush.exe LAN-001   
  lspush.exe 192.168.1.50
  ```
- **<port>**   
  Optional parameter to accompany the scanning server parameter. When included in your command, the computer is silently scanned and the scanned data is sent to the port on your Lansweeper scanning server specified by you. Including this parameter is not required if your Lansweeper server listens for LsPush data on the default port 9524. If you do decide to use a custom port, the custom port must also be submitted in the **Configuration > Server Options**section of the web console and the Lansweeper Server service must be restarted.  

  ```
  Examples:   
  lspush.exe LAN-001 9500   
  lspush.exe 192.168.1.50 9500
  ```
- **/showresult**   
  Optional parameter to accompany the scanning server parameter, mostly used for testing and troubleshooting purposes. When included in your LsPush command, the computer is silently scanned, the scanned data is sent to your Lansweeper scanning server and you receive visual feedback as to whether the connection to the Lansweeper server succeeded. The success or failure pop-up is generated when the computer scan has completed, so it may take a short while to appear.  

  ```
  Examples:   
  lspush.exe LAN-001 /showresult   
  lspush.exe 192.168.1.50 /showresult   
  lspush.exe LAN-001 9500 /showresult   
  lspush.exe 192.168.1.50 9500 /showresult
  ```
- **/file**   
  When included in your LsPush command, the computer is scanned, an on-screen progress bar is shown and the scanned data is stored in a text file in the `%localappdata%\Temp\lspush` folder on the computer. The file can then be placed in the import folder of your Lansweeper scanning server for processing.  

  ```
  Example:   
  lspush.exe /file
  ```
- **/folder**   
  When included in your LsPush command, the computer is silently scanned and the scanned data is stored in a text file in the folder specified by you. The file can then be placed in the import folder of your Lansweeper scanning server for processing.  

  ```
  Examples:   
  lspush.exe /folder "c:\users\lan\downloads"   
  lspush.exe /folder "\\LAN-001\sharedfolder"
  ```
