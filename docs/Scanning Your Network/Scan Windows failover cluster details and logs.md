<!-- # Scan Windows failover cluster details and logs -->

From version 7.2 onward, Lansweeper is capable of scanning details and logs of Windows failover clusters. Specifically, Lansweeper can retrieve the name and IP of the cluster, the cluster nodes and cluster logs. If the cluster is used for failover of Hyper-V virtual machines, Lansweeper can also retrieve the guest machines and Hyper-V logs. A detected virtual machine is automatically turned into an asset, if one does not already exist.

This base article explains how to set up failover cluster scanning and how to view failover cluster data in Lansweeper.  


### Step 1: configure client machines for failover cluster scanning

Failover cluster data is partly retrieved through WMI (Windows Management Instrumentation) on the cluster nodes and partly through PowerShell commands run on the nodes.   
In order for the PowerShell commands to run successfully on the nodes, each node must meet these requirements:

- The Windows Remote Management service (WinRM) must be running.
- Remote receiving of PowerShell commands must be enabled.
- A certificate must be set up for the PowerShell connection.
- A WSMan listener must be set up to receive the PowerShell commands over HTTPS.
- A firewall rule must be added to allow traffic over TCP port 5986.

The below sample PowerShell commands can be run on your cluster nodes to properly configure them as specified above. Save the commands in a .ps1 file and execute this PowerShell script as an administrator on the cluster nodes. For added security, you can replace the "\*" in the script with the IP address of your Lansweeper scanning server. Even more restrictive certificate setups can be created as well, which is best discussed with your network or certificate admin.

```
## Starts the WinRM service
Start-Service -Name "WinRM"
## Enables remote PowerShell
Enable-PSRemoting -Force
## Sets up a certificate and WSMan listener
$Cert = New-SelfSignedCertificate -CertstoreLocation Cert:\LocalMachine\My -DnsName "LsClusterScanning"
New-Item -Path WSMan:\LocalHost\Listener -Transport HTTPS -Address * -CertificateThumbPrint $Cert.Thumbprint ?Force
## Optional step, for added security, which removes every HTTP listener from WSMan
# Get-ChildItem WSMan:\Localhost\listener | Where -Property Keys -eq "Transport=HTTP" | Remove-Item -Recurse
## Allows traffic over port 5986 in Windows Firewall
New-NetFirewallRule -DisplayName "Windows Remote Management (HTTPS-In)" -Name "Windows Remote Management (HTTPS-In)" -Profile Any -LocalPort 5986 -Protocol TCP
```

### Step 2: enable Windows failover cluster scanning

Failover cluster scanning is enabled in Lansweeper by default. To double-check that both cluster and Hyper-V scanning are enabled though, browse to the **Scanning > Scanned Item Interval** section of the web console.   


The items seen below should be enabled to scan failover cluster and Hyper-V information.  
 

### Step 3: configure failover cluster cleanup

To keep your database as small as possible, Lansweeper deletes old failover cluster and Hyper-V logs on a scheduled basis. To customize the cleanup schedule, browse to the **Configuration > Server Options** section of the web console and adjust the items seen below. We recommend keeping these settings as low as possible.  
 

### Step 4: scan failover cluster data

Once you've configured your client machines as specified in step 1 of this article, you can [scan them like any other Windows computer](/docs/how-to-scan-a-windows-computer). The failover cluster and Hyper-V information is automatically retrieved.

### Step 5: view failover cluster data

Windows cluster data can be viewed on the asset pages of your cluster nodes, in the **Windows cluster** tab. This tab contains the cluster name, IP address, nodes and logs. The logs can be filtered to list everything related to that cluster or only entries related to that specific client machine.  


If the cluster is used for failover of Hyper-V virtual machines, the virtual machines can be found in the client machine's **Summary** tab and the Hyper-V logs in the **Hyper-V log** tab. There are also built-in reports in the **Reports** menu of the web console, both for cluster information and Hyper-V guest machines. Perform a search for "cluster" or "Hyper-V" within the reports.  
  
