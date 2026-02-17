<!-- # File and image upload errors and SLA calculation issues -->
The Lansweeper web console can either be installed under the IIS Express or the IIS web server. From Lansweeper version 6.0.100 onward, permissions on Lansweeper folders are made more restrictive for security reasons. If you did not manually make changes to your web server settings prior to updating, the change in folder permissions should have no impact on Lansweeper functionality.

If your web console is hosted under IIS, it uses a Lansweeper application pool by default and this pool is given access to the necessary Lansweeper folders after the 6.0.100 update. If your web console is hosted under IIS and you set up a custom application pool for it however, you'll need to manually grant this custom app pool permissions to the necessary Lansweeper folders.

This article explains how to find out which app pool your Lansweeper console is using. It also explains which folders this app pool needs permissions to and how to apply them. If you are unsure which web server you are using, you can verify this in the following section of the web console: **Configuration > Website Settings**.  
If your custom app pool doesn't have the correct folder permissions, file and image uploads and SLA calculation of tickets received via email can fail. This can result in console errors similar to the ones below. This article aims to resolve these errors.

Access to the path 'C:\Program Files (x86)\Lansweeper\website\helpdesk\files\<file name>' is denied.  
A generic error occurred in GDI+.

If your web console is hosted under IIS and uses a custom application pool, follow these steps to resolve the issues mentioned above:

1. On the machine hosting your web console, open the **Start** menu and select **Run.**
2. In the input box, type "inetmgr" and select **OK**. IIS Manager will open.

   ![procedure-opening-inetmgr.jpg](/docs/.document360/assets/article_286/image_001.jpg)
3. Expand the name of your computer, then the **Sites** section and select the **Lansweeper** website.

   ![file-and-image-upload-errors-and-sla-calculation-issues-1.jpg](/docs/.document360/assets/article_286/image_002.jpg)
4. On the right, select **Advanced Settings...** and take note of the **Application Pool** field in the resulting pop-up. This is the application pool currently being used by your Lansweeper web console. In the sample screenshot below, the web console is using app pool "Custom Lansweeper".

   ![file-and-image-upload-errors-and-sla-calculation-issues-2.jpg](/docs/.document360/assets/article_286/image_003.jpg)
5. In Windows File Explorer, right-click each of the folders listed below and select **Properties**.

   `Program Files (x86)\Lansweeper\Key`

   `Program Files (x86)\Lansweeper\SQLData`

   `Program Files (x86)\Lansweeper\Website`
6. Select the **Security** tab, select **Edit...** and then **Add...** in the resulting pop-up.
7. Enter the name of your IIS app pool in the format seen below. In the sample screenshot below, the app pool is Custom Lansweeper. After entering the name, select **Check Names** and then **OK**.

   `IIS AppPool\<your app pool name>`

   ![file-and-image-upload-errors-and-sla-calculation-issues-3.jpg](/docs/.document360/assets/article_286/image_004.jpg)
8. Tick the **Full control** checkbox and select **OK**.

   ![file-and-image-upload-errors-and-sla-calculation-issues-4.jpg](/docs/.document360/assets/article_286/image_005.jpg)
9. Make sure to change the security settings of each of the 3 folders listed in step 5 of this article.
10. Refresh any web console pages which previously gave errors.
