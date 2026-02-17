<!-- # Check for Lansweeper updates -->

It is recommended that you [update your Lansweeper installation](/docs/update-lansweeper-on-premises) on a regular basis, to ensure that you have the latest available patches installed and access to any new features that have been released. Updates are free to anyone with an active Lansweeper license.

If you aren't sure whether a new Lansweeper update has been published, you can always take a look for yourself.

An overview of changes made in Lansweeper updates can be found in [our changelog](https://www.lansweeper.com/changelog.aspx).

## Check for a Lansweeper update

1. Browse to the **Configuration > Your Lansweeper License**section of the web console.
2. Select **Check for Updates now**. You could also tick **Automatically check for updates once a week** to perform periodic update checks. When periodic update checks are enabled and an update is available, you are notified through a pop-up when logging into the web console.
3. Review the page on the Lansweeper website that you're redirected to. This page indicates whether your installation is up-to-date. If your installation is not up-to-date, update it by following [these instructions](/docs/update-lansweeper-on-premises).  

   If you are scanning your Windows computers with the LsPush scanning agent in a logon script, group policy or scheduled task, you need to manually copy the up-to-date LsPush executable to any folder referenced by your script, policy or task. This is why the update check page states that your LsPush version must be manually checked. When you update your Lansweeper installation, the latest version of the LsPush executable is automatically added to the `Program Files (x86)\Lansweeper\Client` folder on your Lansweeper server.
