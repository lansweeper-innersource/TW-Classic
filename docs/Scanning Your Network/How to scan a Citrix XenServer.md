<!-- # How to scan a Citrix XenServer -->
Citrix scanning is a feature introduced in Lansweeper 7.0. You will need to [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/ "updating your installation") if you are running a lower Lansweeper version.

Lansweeper supports scanning of Citrix XenServers. Scanned Citrix XenServer data includes installed XenServer guests, disks, physical interfaces, storage, crash dumps, CPUs, pool information and more. If the Citrix XenServer hosts are scanned, they will also link to the Lansweeper webpages of the XenServer guest assets.



## Scanning a Citrix XenServer

To scan a Citrix XenServer, follow these steps:

1. Make sure you meet [the Citrix scanning requirements](https://www.lansweeper.com/knowledgebase/citrix-scanning-requirements).
2. Submit your server's IP range for scanning by clicking the **Add Scanning Target** button in the **Scanning > Scanning Targets** section of the console. If you have multiple scanning servers, there will be a separate configuration tab for each server. When submitting your range, you will be asked to specify a scanning schedule.

   

   
3. Submit your Citrix username and password as a credential in the **Scanning > Scanning Credentials** section of the web console. You can use the same username and password for all Citrix XenServers by editing the Global Citrix credential or submit a non-global credential with the **Add new Credential** button.

   

   
4. If the credential you set up is not a global credential, map the credential to your server's IP range by clicking the **+ Credential** button next to the range on the same page.

   
5. Wait for your scanning schedules to trigger or initiate an immediate scan by clicking **Scan now**next to the range under **Scanning > Scanning Targets**.

   
6. Monitor the progress of your scan request under **Scanning > Scanning Queue**.

   
