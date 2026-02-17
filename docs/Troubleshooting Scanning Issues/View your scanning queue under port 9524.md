<!-- # View your scanning queue under port 9524 -->
In most circumstances, you should view your [scanning queue](/docs/view-and-clear-your-scanning-queue) by opening the web console, then navigating to **Scanning > Scanning Queue**. The scanning queue is the most user-friendly way to view and manage scans: it's easily accessible, refreshes automatically, and allows you to clear scan requests.

However, if you need to troubleshoot scanning issues, you can also access the queue under a port. Access to this queue is disabled by default and is only intended to be used in very specific circumstances.

Accessing the scanning queue under a port poses a security risk. Do not allow unrestricted access to the page. Only enable access to the queue under a port if you have a very specific need for it or if you're troubleshooting scanning issues. We recommend viewing the scanning queue under **Scanning > Scanning Queue** in the web console.

Lansweeper's default port is port 9524. This is the port your scanning server will use to listen for data sent by the LsAgent and LsPush scanning agents, and is also the port you'll access to view the scanning queue.

You can update the listen port if needed, but it is not generally required. To update the port, go to **Configuration > Server options > Service options > Listen port**.

## View the scanning queue under a port

1. Go to your **Windows Services** and right-click the **Lansweeper server** service. Select **Stop**.  
   ![sophie_0-1681228317236.jpeg](/docs/.document360/assets/article_274/image_002.jpg)
2. Open the **File explorer** and navigate to `Program Files (x86)\Lansweeper\Tools`.
3. Double-click **ConfigEditor.exe**.
4. In the the **Service** tab, select **Add** in the **appSettings** section.  

   Make sure you're in the **Service** tab, not the **Website** tab for these steps.
5. In the **Key** field, enter **ShowQueueStatus**. In the **Value** field, enter **1**.
6. Select **Add**, then **Save**.  
   ![sophie_1-1681228339335.jpeg](/docs/.document360/assets/article_274/image_003.jpg)
7. Go to your **Windows Services** and right-click the **Lansweeper server** service. Select **Restart**.
8. In your web browser, navigate to the following URL:  
   `https://<IP address or name of the machine hosting your scanning service>:<listen port number>`  
   For example, if your scanning service is hosted on computer LAN-001 and the listen port is the default 9524, the URL would be <https://lan-001:9524>.  

   If you are using Windows Vista, Windows Server 2008, or an older operating system, use HTTP instead of HTTPS.
