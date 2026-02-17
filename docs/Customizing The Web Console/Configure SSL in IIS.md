<!-- # Configure SSL in IIS -->
To secure the traffic to your Lansweeper web console, it is recommended to enable SSL and use an SSL certificate from a trusted Certificate Authority. If you installed Lansweeper on IIS Server, the web console will be installed under HTTP by default.

You can customize your SSL setup by choosing a custom HTTPS port and setting up a custom certificate.

If your Lansweeper installation is not running under HTTPS, a notification will be shown.

## Prerequisites

Install your own certificate on the server hosting the Lansweeper web service. For detailed instructions on installing SSL certificates, see [Install an IIS certificate](#installcert).   
Make sure your certificate is available under **Server Certificates** in IIS:

1. Open the IIS Manager home page.
2. Select **Server Certificates**.
3. Verify whether your certificate is listed.  
   ![How-to-configure-SSL-in-IIS-1.png](/docs/.document360/assets/article_033/image_002.jpg)

The default certificate included with Lansweeper is for example purposes only and should not be used in production environments.

## Install an SSL certificate

The following steps describe how to install an SSL certificate in IIS 8, IIS 8.5, and IIS 10:

1. In IIS, go to **Start > Administrative Tools > Internet Information Services (IIS) Manager**.
2. In **Connections**, select your server’s hostname.
3. Double-click **Server Certificates**.
4. In Actions, select **Complete Certificate Request…**
5. On the **Specify Certificate Authority Response** page, select the **...**browse button to locate your certificate.
6. Enter a descriptive name for easy future reference and choose an appropriate certificate store.
7. Select **OK**.
8. In **Internet Information Services (IIS) Manager**, unfold your server’s name.
9. Expand **Sites** and select the site where you want to install the SSL certificate.
10. In **Actions**, select **Bindings…**
11. In the **Site Bindings** window, select https and then select **Edit**.
12. In the **Edit Site Binding** window, select your SSL certificate.
13. Select **OK**.

## Add a certificate binding

1. In IIS, select **Lansweeper Web Site**. ![How-to-configure-SSL-in-IIS-3.png](/docs/.document360/assets/article_033/image_003.jpg)
2. Select **Bindings** on the right.  
   ![How-to-configure-SSL-in-IIS-4.png](/docs/.document360/assets/article_033/image_004.jpg)
3. In the dialogue that opens, select **Add** and select **https** for the type.  
   ![How-to-configure-SSL-in-IIS-5.png](/docs/.document360/assets/article_033/image_005.jpg)
4. Enter the port you want to use for this binding on the right.
5. Select the SSL certificate to be used.
6. Select **OK** to save the binding.  
   ![How-to-configure-SSL-in-IIS-26.png](/docs/.document360/assets/article_033/image_006.jpg)
7. Your binding is saved. You can close the **Site Bindings** dialogue, and your Lansweeper web console should be available now via HTTPS.
