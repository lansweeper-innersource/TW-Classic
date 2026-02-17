<!-- # Configure SSL in IIS Express -->
Recent [Lansweeper](https://www.lansweeper.com/) releases automatically set up SSL for you if you install the console under IIS Express, the default web server. If you update your Lansweeper installation from an older release, SSL is automatically set up as well. You can customize your SSL setup however, by choosing a custom HTTPS port, setting up a custom certificate and/or forcing HTTPS.

To customize your SSL setup if your console is running under IIS Express (the default web server), do the following:

1. Stop the **IIS Express service** in Windows Services.  
   ![procedure-stopping-the-web-server-service.jpg](/docs/.document360/assets/article_034/image_002.jpg)
2. If you would like to change the HTTPS port chosen during your initial Lansweeper installation, open the iisexpress.config file found at `Program Files (x86)\Lansweeper\IISexpress\iisexpress.config` with Notepad or another text editor, perform a search for "bindingInformation" and replace your current HTTP and HTTPS ports with custom (free) ports of your choice.  
   ![changing-the-web-console-ports-under-iis-express-1.jpg](/docs/.document360/assets/article_034/image_003.jpg)
3. If you would like to replace the built-in SSL certificate with your own one:
   1. Open the Windows Certificate Manager (certmgr.msc) and browse to your own certificate.
   2. Double-click on your certificate and open the **Details**tab.
   3. Mark the "Thumbprint" attribute and copy its value.  
      ![Thumbprint.png](/docs/.document360/assets/article_034/image_004.jpg)
   4. Open the IISExpressSvc.exe file found at `Program Files (x86)\Lansweeper\IISexpress\IISExpressSvc.exe.config` with Notepad or another text editor, search for "UseCustomSSLCertificate" and set it to 1.
   5. Paste the thumbprint of your certificate into the value of "CertificateThumbPrint" and save the file.  
      ![IISExpressSvc.jpg](/docs/.document360/assets/article_034/image_005.jpg)  

      Client browsers need to trust your certificate or have it locally installed in order to open the web page on an HTTPS connection
4. Add the SSL certificate to the certificate stores.  
   Before the certificate can be used it needs to be added to the certificate stores on your Lansweeper web server.
   1. Open the Start menu on your Lansweeper server, select **Run** and run "mmc" as administrator. The  
      Microsoft Management Console will open.
   2. In the File menu, select **Add/Remove Snap-in**. Select **Certificates** and select **Add**.
   3. Select **Computer Account** in the resulting pop-up and select **Local Computer**. Select **Finish** and then **OK**.  
      ![ErikT_2-1673352167072.jpg](/docs/.document360/assets/article_034/image_006.jpg)
   4. In the File menu, select **Add/Remove Snap-in** again.
   5. Select **My User Account**.  
      ![ErikT_3-1673352245545.jpg](/docs/.document360/assets/article_034/image_007.jpg)
   6. Select **Finish** and then **Ok**.
   7. Browse to Console Root\Certificates... Ensure your certificate is present in all of the following stores:
      - Current User > ... > Personal
      - Current User > ... > Trusted Root Certification Authorities
      - Local Computer > ... > Personal
      - Local Computer > ... > Trusted Root Certification Authorities
   8. If your certificate is missing from any of these, add it:

      1. In the console tree, click the logical store where you want to import the certificate.
      2. Right-click the **Certificates** folder and select **All Tasks\Import**.
      3. Select your .pfx certificate file, submit your password and continue until the import is completed.
5. Restart the **IIS Express service** in Windows Services.  
   ![procedure-starting-the-web-server-service.jpg](/docs/.document360/assets/article_034/image_008.jpg)
6. Optionally, you can have Lansweeper redirect HTTP traffic to HTTPS by ticking **Force Https** in the **Configuration > Website Access**section of the web console. You may need to restart the IIS Express service again to make the change take effect.  
   ![changing-the-web-console-ports-under-iis-express-2.jpg](/docs/.document360/assets/article_034/image_009.jpg)  

   Old Lansweeper releases may ask you to submit the HTTPS port in the web console as well. Make sure the HTTPS port submitted in the web console matches the HTTPS port submitted in your iisexpress.config file earlier.

   Make sure HTTPS access is working properly prior to ticking **Force Https**. If the HTTPS port is incorrectly configured, you will lock yourself out of the web console. You can test HTTPS access by browsing to: `https://<IP or name of the machine hosting your console>:<HTTPS port number>/`  
   Should you lock yourself out, run the following executable on the machine hosting the Lansweeper service and select **Reset**:  
   `Https: Program Files (x86)\Lansweeper\Service\ResetWebUserRoles.exe`
