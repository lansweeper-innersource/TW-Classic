<!-- # Lansweeper installer not launching -->
If you've downloaded the latest Lansweeper installer and the installer isn't launching when executed, the file may be blocked or incomplete. This article explains how to resolve this issue.

As of version 10.4 the options /classic needs to be used to install Lansweeper Classic. Running the LansweeperSetup.exe without that option, will attempt to link immediately to [Lansweeper Cloud](/docs/introduction-to-lansweeper-sites "Lansweeper Cloud") during the install steps.

Try the following solutions one by one and verify whether the Lansweeper installer still isn't launching afterward:

- Re-download **LansweeperSetup.exe** from [our download page](https://www.lansweeper.com/install-lansweeper/) and make sure the file size listed in the installer properties matches the one listed on our download page.
- Right-click **LansweeperSetup.exe**, select **Properties**, then the **General** tab and choose **Unblock**, if available. Windows itself sometimes blocks files originating from the internet, requiring you to unblock them.

  ![menu-lansweepersetup-properties.jpg](/docs/.document360/assets/article_289/image_001.jpg)

  ![lansweeper-installer-not-launching-1.jpg](/docs/.document360/assets/article_289/image_002.jpg)
- Temporarily disable anti-virus software installed on your machine or whitelist **LansweeperSetup.exe** within the anti-virus software. Anti-virus software sometimes incorrectly identifies executables as threats and blocks them.  

  If it turns out your anti-virus software was blocking the Lansweeper installer, please let the Lansweeper support team know at [support@lansweeper.com](mailto:support@lansweeper.com?subject=False%20positive%20when%20launching%20LansweeperSetup.exe) so we can report the false positive to the vendor.
