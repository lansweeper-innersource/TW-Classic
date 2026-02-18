<!-- # How to scan an Apple Mac computer -->
Lansweeper supports scanning of macOS. Scanned macOS data includes disks, network interfaces, memory, model, OS, processor, serial number, software, uptime and more.





## Scan an Apple Mac computer

1. Make sure you meet [the Mac scanning requirements](/classic/docs/apple-mac-scanning-requirements).
2. Submit your computer's IP range for scanning by selecting **Add Scanning Target** in the **Scanning > Scanning Targets** section of the console. If you have multiple scanning servers, there will be a separate configuration tab for each server. When submitting your range, you will be asked to specify a scanning schedule.

   

     

   Make sure you do **not** check the **No SSH** option when submitting your IP range for scanning. If **No SSH** is checked, the SSH protocol will not be scanned for machines in the IP range and data returned for your Mac computer will be limited.
3. Submit your SSH username and password as a credential in the **Scanning > Scanning Credentials** section of the web console. You can use the same username and password for all Linux, Unix and Mac computers by editing the Global SSH credential or submit a non-global credential with the **Add new Credential** button.

   

   
4. If the credential you set up is not a global credential, map the credential to your computer's IP range by clicking the **+ Credential** button next to the range on the same page.

   
5. Wait for your scanning schedules to trigger or initiate an immediate scan by clicking the **Scan now** button next to the range under **Scanning > Scanning Targets**.

   
6. Monitor the progress of your scan request under **Scanning > Scanning Queue**.

   
