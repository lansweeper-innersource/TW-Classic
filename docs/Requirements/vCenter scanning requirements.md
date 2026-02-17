<!-- # vCenter scanning requirements -->
You can scan your VMware virtual environments using vCenter credentials. Scanning with vCenter gives a more complete overview of your virtual environment compared to the old VMware scanning method using the Managed Object Browser (MOB). Scanned vCenter data includes datacenters, datastores, clusters, ESXi hosts, VMware guests and more.

In order to scan your vCenter server, the requirements listed below must be met and you must set up a user with (at a minimum) read-only access to the vCenter server.

To make sure a vCenter server meets the requirements for scanning, do the following:

1. Make sure that the machine is a vCenter Server Appliance (vCSA) and that TCP ports 135, 139 and 445 are closed on the vCenter server.

   Scanning a vCenter Server environment installed as software on a Windows computer is not supported. If Lansweeper determines a machine to be a Windows computer, if it finds TCP port 135 to be open, vCenter scanning is skipped.
2. Make sure TCP port 443 (HTTPS) is open on the vCenter server, as Lansweeper uses this port to determine whether the machine is a vCenter server.
3. Log into your vCenter server's vSphere Client.

   ![vCenter-scanning-requirements-1.jpg](/docs/.document360/assets/article_172/image_002.jpg)
4. Select **Administration** from the dropdown menu.

   ![vCenter-scanning-requirements-2.jpg](/docs/.document360/assets/article_172/image_003.jpg)
5. Navigate to **Users and Groups**, select your preferred domain and select **Add User**.

   ![vCenter-scanning-requirements-3.jpg](/docs/.document360/assets/article_172/image_004.jpg)
6. Enter your preferred credentials and click **OK**.

   ![vCenter-scanning-requirements-4.jpg](/docs/.document360/assets/article_172/image_005.jpg)
7. Navigate to **Global Permissions** and select the **"+"** button.

   ![vCenter-scanning-requirements-5.jpg](/docs/.document360/assets/article_172/image_006.jpg)
8. In the resulting pop-up, select the domain you created the user in earlier, enter the user, select **Read-only** and select **OK**.

   ![vCenter-scanning-requirements-6.jpg](/docs/.document360/assets/article_172/image_007.jpg)
9. Your account should now be ready for use. You can test it by opening a web browser, browsing to the IP address of your vCenter server and submitting the username and password you created, which should grant you access to vCenter.   
   You can then start scanning the vCenter server by following the instructions in [this knowledge base article](/docs/scan-a-vcenter-server).
