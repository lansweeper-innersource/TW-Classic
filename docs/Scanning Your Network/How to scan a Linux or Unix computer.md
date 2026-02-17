<!-- # How to scan a Linux or Unix computer -->
Lansweeper supports scanning of Linux and Unix operating systems. Scanned Linux data includes disks, network interfaces, manufacturer, model, memory, OS, processor, serial number, software, uptime, users, user logons and more.





To scan a Linux or Unix computer without a scanning agent:

1. Make sure you meet [the Linux/Unix scanning requirements](/docs/linux-and-unix-agentless-scanning-requirements).
2. Submit your computer's IP range for scanning by selecting **Add Scanning Target** in the **Scanning > Scanning Targets** section of the console. If you have multiple scanning servers, there will be a separate configuration tab for each server. When submitting your range, you will be asked to specify a scanning schedule.  
   

     
     

   Make sure you **do not** check the **No SSH** option when submitting your IP range for scanning. If **No SSH** is checked, the SSH protocol will not be scanned for machines in the IP range and data returned for your Linux computer will be limited. If your client computer uses a custom SSH port, make sure to submit the correct port number in the pop-up as well.
3. Submit your SSH username/password combination or SSH certificate/key as a credential in the **Scanning > Scanning Credentials** section of the web console. You can use the same username/password combination for all Linux, Unix and Mac computers by editing the Global SSH credential.   
   Alternatively, submit a non-global username/password combination or certificate/key with the **Add new Credential** button. Choose SSH as your credential type.  
   
4. If the credential you set up is not a global credential, map the credential to your computer's IP range by clicking the **+ Credential** button next to the range on the same page.  
   
5. Wait for your scanning schedules to trigger or initiate an immediate scan by clicking the **Scan now** button next to the range under **Scanning > Scanning Targets**.  
   
6. Monitor the progress of your scan request under **Scanning > Scanning Queue**.  
   
