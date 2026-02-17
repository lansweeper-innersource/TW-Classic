<!-- # Mark software and add-ons as authorized -->
Software on Windows computers can be marked as authorized (approved), unauthorized (denied) or unrated (neutral).

By default, any new software detected in your network is marked as neutral. When you've configured software authorization, you can use one of the built-in Lansweeper reports to keep track of unauthorized software installations in your network.

Internet Explorer add-ons (ActiveX controls, browser bars, Browser Helper Objects and extensions) can also be marked as authorized. A default list of authorized add-ons is included in your Lansweeper installation but can be customized to suit your needs. Unauthorized add-ons can once again be listed by running built-in reports.

## Set the authorization status of Windows software

1. Browse to the **Software > Authorization**section of the web console.  
   ![menu-software-authorization.jpg](/docs/.document360/assets/article_144/image_001.jpg)
2. Click one or more times on a bullet in the Approved column in the **Software Authorization** section of the page to mark a software package as approved, denied or neutral. A green bullet means that the software is authorized (approved), a red bullet that the software is unauthorized (denied) and a gray bullet that the software is unrated (neutral).  
   ![marking-software-and-add-ons-as-authorized-1.jpg](/docs/.document360/assets/article_144/image_002.jpg)
   - You can search through one or more columns to easily find specific software packages. In the example above, we filtered the Publisher column to only list software packages published by Adobe.
   - You can use the **Approve All Results/Deny All Results/Unrate All Results** buttons to change the authorization status of multiple software packages at once. If you filter the Name, Publisher or Approved column, only the software included in your search results will be affected by the buttons.
   - Software authorization statuses remain saved in the database even if you were to delete all computers with the specified software from your Lansweeper installation. That way, the authorization data is still available if a new computer appears in the network that has the software installed.
3. You can use the built-in reports below, found in the **Reports** tab of the web console, to list authorized, unauthorized and unrated software installations detected in your network.  
   - Software: Approved software
   - Software: Unauthorized software
   - Software: Unrated software
4. When you browse to a Windows computer's Lansweeper webpage and open the **Software** tab, authorization bullets are also displayed next to the names of the software packages.  
   ![marking-software-and-add-ons-as-authorized-2.jpg](/docs/.document360/assets/article_144/image_003.jpg)

## Set the authorization status of ActiveX controls, browser bars, BHOs and extensions

1. Browse to the **Software > Authorization**section of the web console.  
   ![menu-software-authorization.jpg](/docs/.document360/assets/article_144/image_004.jpg)
2. Select **Add allowed Active-X** in the **Allowed Active-X Controls** section of the page and enter the control ID you want to authorize into the first field of the pop-up window.   
   Optionally, you can comment on what kind of control it is in the Remark field. Select **Ok** afterward.  
   ![marking-software-and-add-ons-as-authorized-3.jpg](/docs/.document360/assets/article_144/image_005.jpg)
3. You can use the built-in reports below, found in the **Reports** tab of the web console, to list unauthorized add-ons detected in your network. An online search for the control ID will provide more information on the add-on.
   - IE: unauthorized ActiveX control
   - IE: unauthorized IE Bars
   - IE: unauthorized IE BHOs
   - IE: unauthorized IE Extensions
4. Authorized and unauthorized add-ons are also listed in the **Config > Internet Explorer** section of a Windows computer's Lansweeper webpage.  
   ![marking-software-and-add-ons-as-authorized-4.jpg](/docs/.document360/assets/article_144/image_006.jpg)
