<!-- # Automatically redirected to login screen -->
The Lansweeper software consists of 3 components: a database, a scanning service and a web console. The web console, scanning service and other files are added to the folder specified in the Lansweeper installer during the initial installation.

To ensure that the scanning service and web console run successfully, it is important that no changes are made to the files in the Lansweeper installation folder. Modifications, migrations or deletions of files can cause issues with your Lansweeper installation. Users may be taken back to the Lansweeper login screen for instance or may encounter errors similar to the one below in dashboard widgets and other web console locations.  
![automatically-redirected-to-login-screen-1.jpg](/docs/.document360/assets/article_279/image_001.jpg)

Anti-virus software can make changes to the Lansweeper installation files and cause issues like this. Even though the files are clean, anti-virus software can make changes to their metadata in the process of scanning them, causing the Lansweeper web console to restart and log everyone out.

To prevent session errors and automatic redirects to the login screen:

1. Double-check that you are running the latest Lansweeper release by following [these instructions](/docs/check-for-lansweeper-updates). It is recommended that you update your Lansweeper installation on a regular basis, to ensure that you have the latest available patches installed, as well as access to any new features that have been released.
2. Either disable any anti-virus software on the server hosting your Lansweeper installation, or reconfigure your anti-virus software not to scan the Lansweeper installation folder.   
   Specific instructions for disabling or reconfiguring your anti-virus software should be available in the anti-virus software's documentation. Alternatively, the vendor of the anti-virus software should be able to provide information on this. The default Lansweeper installation folder, which should be excluded from anti-virus scans, is `C:\Program Files (x86)\Lansweeper`.
