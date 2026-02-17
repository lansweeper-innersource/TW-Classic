<!-- # Scan a vCenter server -->

You can scan your VMware virtual environments using vCenter credentials. Scanned vCenter data includes version, build, OS, manufacturer, network interfaces, datacenters, ESXi servers, datastores, VMware guests and more. If VMware guests are scanned as separate assets as well, Lansweeper will automatically link them to the correct ESXi server and vCenter server.

## Scanning a vCenter server

To retrieve data from a vCenter server, follow these steps:

1. Make sure you meet [the vCenter scanning requirements](/docs/vcenter-scanning-requirements).
2. Submit your vCenter server's IP range for scanning by clicking **Add Scanning Target** in the **Scanning > Scanning Targets** section of the web console. If you have multiple scanning servers, there will be a separate configuration tab for each server. When submitting your range, you will be asked to specify a scanning schedule.  
   ![menu-scanning-scanning-targets.jpg](/docs/.document360/assets/article_215/image_002.jpg)

   ![how-to-scan-a-windows-computer-5.jpg](/docs/.document360/assets/article_215/image_003.jpg)
3. Submit your vCenter username and password as a credential in the **Scanning > Scanning Credentials** section of the web console. You can use the same username and password for all vCenter servers by editing the Global vCenter credential or submit a non-global credential with the **Add new Credential** button.  
   ![menu-scanning-scanning-credentials.jpg](/docs/.document360/assets/article_215/image_004.jpg)

   ![How-to-scan-vCenter-1.jpg](/docs/.document360/assets/article_215/image_005.jpg)
4. If the credential you set up is not a global credential, map the credential to your vCenter server's IP address or IP range by clicking the **Map Credential** button on the same page.  
   ![How-to-scan-vCenter-2.jpg](/docs/.document360/assets/article_215/image_006.jpg)
5. Wait for your scanning schedules to trigger or initiate an immediate scan by clicking **Scan now** next to the scan target under **Scanning > Scanning Targets**.
6. Monitor the progress of your scan request under **Scanning > Scanning Queue**.  
   ![menu-scanning-scanning-queue.jpg](/docs/.document360/assets/article_215/image_007.jpg)
