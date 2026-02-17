<!-- # Set up and run Lansweeper IT Agent Discovery Portable -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_345/image_001.jpg) **Learn to set up and run Lansweeper IT Agent Discovery Portable on Windows for on-demand network scanning and asset discovery, without installation or credentials.**

Lansweeper IT Agent Discovery Portable runs on Windows without requiring installation. It allows on-demand local scanning without credentials, making it a convenient solution for targeted network discovery.

IT Agent Discovery can also be installed on Linux and Unix machines and run as a background service. For more information, see [Install IT Agent Discovery](/docs/install-it-agent-discovery).  

## Prerequisites

Before proceeding, ensure you have a [Network Discovery installation](/docs/install-network-discovery#Windows) in your environment.

1. Ensure the [connection requirements](/docs/install-it-agent-discovery#connection) are met and your [Windows operating system](/docs/install-it-agent-discovery#OSWindows) is supported.
2. Open a browser and navigate to [https://app.lansweeper.com](https://app.lansweeper.com/).
3. Navigate to the Lansweeper Site to which you want to link the IT Agent Discovery.
4. In your Lansweeper Site, go to **Scanning > Discovery systems > Download installers/packages**.
5. Under **IT Agent Discovery**, select **Download IT Agent Portable Windows** and **Download IT Agent Portable configuration**.
6. Navigate to your Network Discovery Hub. Go to **Settings > Data Transfer > IT Agent Portable code(s)** and select **Enable file import**.
7. Enter the name of the import folder. For a Hub on Windows, the default is `C:\Program Files\Lansweeper Network Discovery\hub\import` (or `./import`). For a Hub on Linux and macOS, the default is `./import`.
8. Select **Generate key** and copy the key, or enter a custom key.
9. Select **Save File Import Settings** **>** **OK**.

## Run IT Agent Discovery Portable and save to file for importing

For optimal performance, run IT Agent Portable from a folder with elevated privileges.

### Single execution on 1 machine

To execute Lansweeper IT Agent Discovery Portable on a single machine:

1. Open an elevated PowerShell command prompt.
2. Run the following command to extract the contents of the ZIP file:

   ```
   tar -xf C:\Users\%USERNAME%\Downloads\Lansweeper.IT.Agent.Portable.zip C:\Temp\Lansweeper-IT-Agent-Portable
   ```
3. Run the following command to initiate the scan. Replace `fileimportkey` with your copied key:

   ```
   C:\Temp\Lansweeper-IT-Agent-Portable\Lansweeper-IT-agent-portable-windows-x64.exe scan --file C:\Temp\Lansweeper-IT-Agent-Portable\discoveryresult-%COMPUTERNAME%.data --key fileimportkey
   ```

### Logon script in Active Directory

To run the Lansweeper IT Agent on all Windows domain members through a logon script:

1. Copy the `Lansweeper.IT.Agent.Portable.zip` file you downloaded to the `NETLOGON` share on your domain controller (default location: `C:\WINDOWS\SYSVOL\domain\scripts`).
2. Open an elevated PowerShell command prompt.
3. Run the following command to extract the contents of the ZIP file. Replace `DomainController01.domain.local` with the name of your domain controller:

   ```
   Expand-Archive -Force \\DomainController01.domain.local\NETLOGON\Lansweeper.IT.Agent.Portable.zipC:\Temp\Lansweeper-IT-Agent-Portable
   ```
4. Run the following command to initiate the scan. Replace `fileimportkey` with your copied key:  

   ```
   C:\Temp\Lansweeper-IT-Agent-Portable\Lansweeper-IT-agent-portable-windows-x64.exe scan --file C:\Temp\Lansweeper-IT-Agent-Portable\discoveryresult-%COMPUTERNAME%.data --key fileimportkey
   ```

## Post-Execution

1. After a successful execution, copy the following file:  

   ```
   C:\Temp\Lansweeper-IT-Agent-Portable\discoveryresult-%COMPUTERNAME%.data
   ```
2. On the computer where you have Network Discovery Hub installed, navigate to the import folder:

   ```
   C:\Program Files\Lansweeper Network Discovery\hub\Import
   ```
3. Paste the copied discovery result file to trigger the Hub to sync the discovery result.
4. Once synced, go to your Lansweeper Site, navigate to **Inventory**, and validate that the asset details page is updated.

## Run IT Agent Discovery Portable and Send Directly to Network Discovery Hub

For optimal performance, run IT Agent Portable from a folder with elevated privileges.

### Single Execution on 1 Machine - Method 1

To execute Lansweeper IT Agent Discovery Portable on a single machine and store the results directly into a Network Discovery Hub:

1. Ensure the asset has access to the Network Discovery Hub (port <https://mynetworkdiscoveryhub.domain.local:59525> by default).
2. Open an elevated PowerShell command prompt.
3. Run the following command to extract the contents of the ZIP file:  

   ```
   Expand-Archive -Force C:\Users\%USERNAME%\Downloads\Lansweeper.IT.Agent.Portable.zip C:\Temp\Lansweeper-IT-Agent-Portable
   ```
4. Run the following command to initiate the scan. Fill in the correct Hub URI and replace `fileimportkey` with your copied key:

   ```
   C:\Temp\Lansweeper-IT-Agent-Portable\Lansweeper-IT-agent-portablewindows-x64.exe scan -h https://mynetworkdiscoveryhub.domain.local:59525 --key fileimportkey
   ```

### Single Execution on 1 Machine - Method 2

To execute Lansweeper IT Agent Discovery Portable on a single machine and store the results directly into a Network Discovery Hub:

1. Ensure the asset has access to the Network Discovery Hub (port <https://mynetworkdiscoveryhub.domain.local:59525> by default).
2. Open an elevated PowerShell command prompt.
3. Run the following command to extract the contents of the ZIP file:  

   ```
   Expand-Archive -Force C:\Users\%USERNAME%\Downloads\Lansweeper.IT.Agent.Portable.zip C:\Temp\Lansweeper-IT-Agent-Portable
   ```
4. Update the IT Agent Portable configuration file (scanoptions.json) you downloaded to:  

   ```
   { "ScanOptions": { "Key": "The IT Agent Portable code generated in your Network Discovery hub", "File": "optional: The path of the file where you want to save the output to, example discoveryresult.data", "HubUri": "optional: The URI to connect to your Network Discovery hub, example: https://mynetworkdiscoveryhub.domain.local:59525" } }
   ```

   Run the following command to initiate the scan:

   ```
   C:\Temp\Lansweeper-IT-Agent-Portable\Lansweeper-IT-agent-portable-windows-x64.exe scan
   ```
