<!-- # How to scan a VMware server -->
VMware servers can be scanned directly with a read-only credential to the server or [indirectly through their vCenter server](/docs/scan-a-vcenter-server). This article explains how to scan the servers directly.

Scanned VMware ESX(i) data includes disks, installed guest machines, network interfaces, manufacturer, model, memory, processor, uptime and more. If the server's guest machines are scanned as separate assets and have the VMware Tools installed, the Lansweeper webpage of the VMware server also links to the Lansweeper webpages of the guest assets.

![how-to-scan-a-vmware-server-1.jpg](/docs/.document360/assets/article_190/image_001.jpg)

## Scanning a VMware server

To scan a VMware server directly, follow these steps:

1. Make sure you meet [the VMware server scanning requirements](/docs/vmware-server-scanning-requirements).
2. Submit your server's IP range for scanning by clicking the **Add Scanning Target** button in the **Scanning > Scanning Targets** section of the console. If you have multiple scanning servers, there will be a separate configuration tab for each server. When submitting your range, you will be asked to specify a scanning schedule.

   ![menu-scanning-scanning-targets.jpg](/docs/.document360/assets/article_190/image_002.jpg)

   ![procedure-submitting-ip-range-for-scanning.jpg](/docs/.document360/assets/article_190/image_003.jpg)
3. Submit your VMware username and password as a credential in the **Scanning > Scanning Credentials** section of the web console. You can use the same username and password for all VMware servers by editing the Global ESXi credential or submit a non-global credential with the **Add new Credential** button.

   ![menu-scanning-scanning-credentials.jpg](/docs/.document360/assets/article_190/image_004.jpg)

   ![how-to-scan-a-vmware-server-2.jpg](/docs/.document360/assets/article_190/image_005.jpg)
4. If the credential you set up is not a global credential, map the credential to your server's IP range by clicking **+ Credential** next to the range on the same page.

   ![how-to-scan-a-vmware-server-3.jpg](/docs/.document360/assets/article_190/image_006.jpg)
5. Wait for your scanning schedules to trigger or initiate an immediate scan by clicking **Scan now** next to the range under **Scanning > Scanning Targets**.

   ![procedure-scan-now-under-scanning-targets.jpg](/docs/.document360/assets/article_190/image_007.jpg)
6. Monitor the progress of your scan request under **Scanning > Scanning Queue**.

   ![menu-scanning-scanning-queue.jpg](/docs/.document360/assets/article_190/image_008.jpg)
