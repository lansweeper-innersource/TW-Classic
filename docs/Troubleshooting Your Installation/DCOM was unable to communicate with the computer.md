<!-- # DCOM was unable to communicate with the computer -->
After installing Lansweeper and scanning your network, you may start seeing entries with an Event ID like the one below in your Lansweeper server's Event Viewer. While your Event Viewer classifies these entries as errors, they are just informational messages and can generally be ignored.

![dcom-was-unable-to-communicate-with-the-computer-1.jpg](/docs/.document360/assets/article_282/image_002.jpg)

When Lansweeper scans a Windows computer, it uses DCOM to establish the initial connection to the client machine. If the client machine is offline or firewalled, DCOM automatically logs an error in your server's Event Viewer. This error indicates that Lansweeper was unable to scan the client machine, but does not point to an underlying issue with your server or Lansweeper installation.

Regardless, there are steps you can take to stop seeing these events. Lansweeper automatically [excludes them from scanning](/docs/excluding-events-from-scanning) so they don't show up in your Lansweeper web console, but you can also prevent them from being added to your Event Viewer altogether.

## Prevent DCOM from logging events in Event Viewer

1. On the machine hosting the **Lansweeper Server** service, run **regedit.exe**, the Registry Editor.
2. Go to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole` and Modify the **ActivationFailureLoggingLevel**.  
   ![dcom-was-unable-to-communicate-with-the-computer-3.jpg](/docs/.document360/assets/article_282/image_003.jpg)
3. Set the **ActivationFailureLoggingLevel** value to "2".  
   ![dcom-was-unable-to-communicate-with-the-computer-4.jpg](/docs/.document360/assets/article_282/image_004.jpg)
4. If the **ActivationFailureLoggingLevel** value does not exist, manually create it.  
   ![dcom-was-unable-to-communicate-with-the-computer-2.jpg](/docs/.document360/assets/article_282/image_005.jpg)  

   Keep in mind that setting this value to "2" will prevent DCOM from logging any failures.
5. Reboot the machine hosting the **Lansweeper Server** service.
