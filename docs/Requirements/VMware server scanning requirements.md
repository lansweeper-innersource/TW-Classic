<!-- # VMware server scanning requirements -->
VMware servers can be scanned directly with a read-only credential to the server or [indirectly through their vCenter server](/docs/scan-a-vcenter-server). To scan a VMware ESX(i) server directly, certain requirements must be met. Specifically, you must set up a user with read-only access to the server. In order for Lansweeper to link your VMware guest assets to their hosts, you must also ensure that the VMware Tools are installed on the guest machines.

This article explains how to set up a user with read-only access to your VMware server, so you can submit it as a scanning credential in Lansweeper. There are instructions for both the [VMware web client](#heading1) and [locally installed vSphere client](#heading2).

## Configuring a VMware server with web client

To set up an account with read-only access to your VMware server by using the server's web client, do the following:

1. Log into your VMware server's web interface.

   ![vmware-server-scanning-requirements-7.jpg](/docs/.document360/assets/article_173/image_001.jpg)
2. Under the **Host** menu, select **Manage**.

   ![vmware-server-scanning-requirements-8.jpg](/docs/.document360/assets/article_173/image_002.jpg)
3. Select the **Security & users** tab and go the **Users** menu within this tab.
4. Select **Add user** and submit a name, description and password for your user and select **Add**. Be aware that your username is case-sensitive.

   ![vmware-server-scanning-requirements-9.jpg](/docs/.document360/assets/article_173/image_003.jpg)

   ![vmware-server-scanning-requirements-10.jpg](/docs/.document360/assets/article_173/image_004.jpg)
5. Right-click the **Host menu** and select **Permissions**.

   ![vmware-server-scanning-requirements-11.jpg](/docs/.document360/assets/article_173/image_005.jpg)
6. Click the **Add user** button, select the user you created earlier and the **Read-only** role**.** Select **Add User** and then **Close** afterwards.

   ![vmware-server-scanning-requirements-12.jpg](/docs/.document360/assets/article_173/image_006.jpg)

   ![vmware-server-scanning-requirements-13.jpg](/docs/.document360/assets/article_173/image_007.jpg)
7. Your account should now be ready for use and you now meet the VMware scanning requirements. You can start scanning the VMware server by following the instructions in [this knowledge base article](/docs/how-to-scan-a-vmware-server).
8. In order for Lansweeper to link your VMware guest assets to their hosts, also ensure that the VMware Tools are installed on the guest machines.

## Configuring a VMware server with local vSphere client

To set up an account with read-only access to your VMware server by using a locally installed vSphere client, do the following:

1. Log into your VMware server's vSphere client.

   ![vmware-server-scanning-requirements-1.jpg](/docs/.document360/assets/article_173/image_008.jpg)
2. Select your VMware server on the left, right-click within the **Local Users & Groups** menu and select **Add...**

   ![vmware-server-scanning-requirements-2.jpg](/docs/.document360/assets/article_173/image_009.jpg)
3. Submit your preferred username in the upper two input boxes of the resulting pop-up, your preferred password in the lower two input boxes and select **OK**. Be aware that your username is case-sensitive.

   ![vmware-server-scanning-requirements-3.jpg](/docs/.document360/assets/article_173/image_010.jpg)
4. Right-click within the **Permissions** menu and select **Add Permission...**

   ![vmware-server-scanning-requirements-4.jpg](/docs/.document360/assets/article_173/image_011.jpg)
5. In the resulting pop-up, select the read-only role and select **Add...**

   ![vmware-server-scanning-requirements-5.jpg](/docs/.document360/assets/article_173/image_012.jpg)
6. Select the user you created earlier, click **Add** and then **OK** twice.

   ![vmware-server-scanning-requirements-6.jpg](/docs/.document360/assets/article_173/image_013.jpg)
7. Your account should now be ready for use and you now meet the VMware scanning requirements. You can start scanning the VMware server by following the instructions in [this knowledge base article](/docs/how-to-scan-a-vmware-server).
8. In order for Lansweeper to link your VMware guest assets to their hosts, also ensure that the VMware Tools are installed on the guest machines.
