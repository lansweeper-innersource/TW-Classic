<!-- # Troubleshoot: Selected Cloud management instead of On-premises management during installation -->

If you accidentally select Cloud management instead of On-prem management during the initial Lansweeper setup, you will not be able to access the On-premises console or enter your license key to begin scanning. To resolve the error, follow the steps below.

To resolve this error, you must delete your current site, create a new one, and link it to your installation. Cloud-first sites can not be converted into hybrid sites. For more information about license and installation types, check out [Lansweeper installation and management types](/docs/lansweeper-installation-and-management-types).

1. [Enable the on-premises console.](/docs/enable-the-lansweeper-on-premises-web-console)
2. In the on-prem console, select **Cloud link overview > Unlink from cloud site > Confirm**.
3. Go to **Configuration > Your Lansweeper license > Add license**.
4. Enter your license key and select **Ok**.
5. Navigate to your Lansweeper Site.
6. Go to **Configuration > Site settings > Delete this site**. Enter the name of the site, then select **Delete this site**.
7. [Link your on-prem console to a new Lansweeper Site.](/docs/link-lansweeper-on-prem-with-lansweeper-sites)

