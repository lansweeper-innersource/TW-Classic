<!-- # Change the web console ports under IIS Express -->
The Lansweeper installer lets you choose a custom HTTP and HTTPS port to install the web console under.

If you don't choose custom ports, the installer will automatically install the web console under the first available ports. You can always change the ports afterwards, if required.

To change the web console ports if your console is running under IIS Express (the default web server):

1. Stop **IIS Express service** in Windows Services.
2. Open the iisexpress.config file found at **`Program Files (x86)\Lansweeper\IISexpress\iisexpress.config`**with Notepad or another text editor.
3. Search for "bindingInformation" and replace your current HTTP and HTTPS ports with custom (free) ports of your choice.  
   
4. Restart **IIS Express service** in Windows Services.
5. If Windows Firewall or another type of firewall is enabled on the server hosting the web console, make sure to update your firewall configuration to allow traffic over your newly configured ports.
6. Test web console access under your newly configured ports by browsing to the URLs below.  

   ```
   http://<IP address or name of the machine hosting your web console>:<HTTP port number>/   
   https://<IP address or name of the machine hosting your web console>:<HTTPS port number>/
   ```
7. Optionally, have Lansweeper redirect HTTP traffic to HTTPS by ticking **Force https when configured** in the **Configuration > Website Settings**section of the web console. You may need to restart **IIS Express service** again to make the change take effect.  
   

     

   Older Lansweeper releases may ask you to submit the HTTPS port in the web console as well. Make sure the HTTPS port submitted in the web console matches the HTTPS port submitted in your IIS Express configuration file earlier.

   Should your HTTPS port fail or become blocked at some point, you can once again disable redirects to HTTPS. To do so, run the following executable on the machine hosting the Lansweeper service and select **Reset**:  
   `https: Program Files (x86)\Lansweeper\Tools\ResetWebUserRoles.exe`
