<!-- # Scan Windows computer certificates -->
From version 9.5 onward, Lansweeper is capable of scanning certificates that are in the Local Computer store of Windows computers. Specifically, for each Local Computer certificate Lansweeper retrieves the certificate store, certificate name, thumbprint, serial, issued to, issued by, start date, expiration date, intended purposes, used template and more.

This article explains how to set up Windows certificate scanning and how to view certificate data in Lansweeper.

![scanned-windows-computer-certificates.png](/docs/.document360/assets/article_237/image_002.jpg)

## Configure client machines for certificate scanning

To scan certificates of a Windows computer, the computer must meet [the general Windows scanning requirements](/docs/windows-domain-scanning-requirements). In addition, the machine must either have the Remote Registry service or PowerShell enabled. Only one of the two is necessary: Lansweeper first tries to retrieve certificates using the Remote Registry service, but if that fails, it tries PowerShell as a fall-back.

### 1. Remote Registry service

Lansweeper first tries to retrieve certificates using the Remote Registry service. If you want Lansweeper to use this method for certificate retrieval, make sure the Remote Registry service is enabled and running in Windows Services on your client machines. If the service is enabled but stopped, Lansweeper will attempt to start it.

### 2. PowerShell

If Lansweeper cannot retrieve certificates using the Remote Registry service, it tries PowerShell next. In order for the PowerShell commands to run successfully on your client machines, each client machine must meet these requirements:

- The Windows Remote Management service (WinRM) must be running.
- Remote receiving of PowerShell commands must be enabled.
- A certificate must be set up for the PowerShell connection.
- A WSMan listener must be set up to receive the PowerShell commands over HTTPS.
- A firewall rule must be added to allow traffic over TCP port 5986.

The below sample PowerShell commands can be run on your client machines to properly configure them as specified above. Save the commands in a .ps1 file and execute this PowerShell script as an administrator on the client machines.   
For added security, you can replace the "\*" in the script with the IP address of your Lansweeper scan server. Even more restrictive certificate setups can be created as well, which is best discussed with your network or certificate admin.

```
## Starts the WinRM service
Start-Service -Name "WinRM"
## Enables remote PowerShell
Enable-PSRemoting -Force
## Sets up a certificate and WSMan listener
$Cert = New-SelfSignedCertificate -CertstoreLocation Cert:\LocalMachine\My -DnsName "LsCertificateScanning"
New-Item -Path WSMan:\LocalHost\Listener -Transport HTTPS -Address * -CertificateThumbPrint $Cert.Thumbprint ?Force
## Optional step, for added security, which removes every HTTP listener from WSMan
# Get-ChildItem WSMan:\Localhost\listener | Where -Property Keys -eq "Transport=HTTP" | Remove-Item -Recurse
## Allows traffic over port 5986 in Windows Firewall
New-NetFirewallRule -DisplayName "Windows Remote Management (HTTPS-In)" -Name "Windows Remote Management (HTTPS-In)" -Profile Any -LocalPort 5986 -Protocol TCP
```

## Enable certificate scanning

Certificate scanning is enabled by default in new and updated Lansweeper installations. However, it's good to double-check that certificate scanning is in fact enabled before attempting to scan or view certificate data.

1. Browse to the **Scanning > Scanned Item Interval** menu of the web console.  
   ![menu-scanning-scanned-item-interval.png](/docs/.document360/assets/article_237/image_003.jpg)
2. Make sure the **Enable** checkbox of the CERTIFICATES item is ticked. The default [refresh interval](/docs/manage-scanned-item-intervals) of the item is 6 days.

## Add certificate permission to relevant roles

Access to scanned certificate data is controlled by a specific permission. Only users whose user role includes this permission can view certificate data on individual Windows asset pages and in reports. By default, the built-in admin, the Administrator and the Administrator + Agent role have the certificate permission. If you have a different or custom role, however, you will need to manually add the certificate permission to it.

1. Browse to the **Configuration > User Access & Roles** menu of the web console.
2. In the **User Roles** section of the page, click the edit button next to your user role.
3. In the resulting pop-up, make sure the **Access Certificate Information** permission is checked. Note that you may need to log out of Lansweeper and back in to see the user role change take effect.  
   ![access-certificate-information-permission.png](/docs/.document360/assets/article_237/image_004.jpg)

## Scan certificate data

Once you've completed the previous steps, fully rescan your client machines to immediately retrieve the certificate data. For instance, click the **Assets** menu at the top of the web console, filter the **Type** column for Windows computers, tick the upper checkbox to select all assets and then select **Rescan asset(s)**. Note that you must use an agentless scanning method or LsAgent to scan your client machines, as the older LsPush agent does not scan certificates.  
![rescan-windows-computers.png](/docs/.document360/assets/article_237/image_005.jpg)

If you rescan your computers with one of the **Rescan** buttons found throughout the web console, the certificate data will immediately be retrieved as part of the rescan. If you use another scanning method like an IP range target, the certificate data being refreshed will depend on how you configured the CERTIFICATES item interval. With a default CERTIFICATES item interval of 6 days for instance, an IP range scan will only refresh certificate data every 6 days at most.

## View certificate data

Windows certificate data can be viewed in the **Config > Windows > Certificates** tab of individual Windows asset pages. You can also use built-in or custom reports to view certificate data. Perform a search for "certificate" in the **Reports** menu of the web console to find built-in certificate reports. There are built-in reports for expiring, expired and self-signed certificates for instance.

If you want to build a custom report, an easy way to do so is by editing a built-in report and choosing **Save As** from the report builder. This creates a copy of the report that you can customize further.
