<!-- # How to scan users -->
An inventory of your Active Directory users is available on Lansweeper Sites. If you want to [view your user inventory](/docs/view-your-user-inventory), consider [linking with Lansweeper Sites](/docs/link-lansweeper-on-prem-with-lansweeper-sites), if you haven't already.

When Lansweeper scans a Windows computer, it automatically retrieves the user accounts configured on the computer, as well as the configured user groups and their members. This information can be found in the **Config > User Info** section of individual computer webpages, under **Users, Groups** and **Users In Groups**. These tabs are not populated for domain controllers. Local users and groups configured on domain controllers are no longer scanned, as such scans could cause performance issues.

In addition to scanning locally configured users and groups, Lansweeper also detects the currently logged on (local or domain) user during every computer scan and adds it to the **Config > User Info > Last Logon** section of the computer webpage. The logon time values reflect when Lansweeper scanned the computer and detected the users.

![how-to-scan-users-1.jpg](/docs/.document360/assets/article_195/image_001.jpg)

As previously mentioned, users configured on computers and users that log into computers are automatically detected. However, it is possible to scan additional domain users directly from Active Directory as well. Lansweeper allows you to pull user accounts directly from Active Directory OUs specified by you and to do so on a schedule.   
To scan an Active Directory user OU, follow these steps:

1. If you want users that are disabled in AD to be included in the scan you'll be performing, make sure the below option is ticked in the **Configuration > Server Options** section of the web console. If this option is not ticked, users marked as disabled are skipped during scanning. This option is available from Lansweeper 7.2 onward.

   ![setting-scan-users-disabled-in-active-directory.jpg](/docs/.document360/assets/article_195/image_002.jpg)
2. Submit a domain username and password with (at least) read-only access to Active Directory as a credential in the **Scanning > Scanning Credentials** section of the console.   

   ![menu-scanning-scanning-credentials.jpg](/docs/.document360/assets/article_195/image_003.jpg)

     
   You can use the same credential for all Windows computers and users by configuring the Global Windows credential or submit a non-global credential with the **Add new Credential** button. Submit a down-level logon name like NetBIOS domain name\username or a user principal name (UPN) like username@yourdomain.local

   ![how-to-scan-users-2.jpg](/docs/.document360/assets/article_195/image_004.jpg)
3. If the credential you set up is not a global credential, map the credential to your domain by selecting the **Map Credential** button on the same page. In the resulting pop-up, submit your NetBIOS domain name and select the credential you created earlier. In the example below, the credential was mapped to the "lansweeper" domain.

   ![how-to-scan-users-3.jpg](/docs/.document360/assets/article_195/image_005.jpg)
4. Submit your user OU for scanning by selecting the **Add Scanning Target** button in the **Scanning > Scanning Targets** section of the web console and selecting the **Active Directory User/Group Path** scanning type. If you have multiple scanning servers, there will be a separate configuration tab for each server. Lansweeper will scan the users in the OU you've submitted and any sub-OUs contained within.

   ![menu-scanning-scanning-targets.jpg](/docs/.document360/assets/article_195/image_006.jpg)

   ![how-to-scan-users-4.jpg](/docs/.document360/assets/article_195/image_007.jpg)
5. Wait for your scanning schedules to trigger or click **Scan now** next to the scanning target to initiate an immediate scan.   
   Keep in mind that user OU scans will not show up in your scanning queue. You can determine when a user OU was last scanned by looking at the **Last Scan** value next to the scanning target.

   ![how-to-scan-users-5.jpg](/docs/.document360/assets/article_195/image_008.jpg)
6. List scanned domain users with the built-in Active Directory Users OU or Active Directory User Departments widget or by running a built-in or custom report based on the tblADusers database table.

   ![how-to-scan-users-6.jpg](/docs/.document360/assets/article_195/image_009.jpg)

   ![how-to-scan-users-7.jpg](/docs/.document360/assets/article_195/image_010.jpg)  
     
   You can also perform a search for a specific username or user display name in the web console search bar to view the Active Directory details of that specific user. Scanned domain user data includes user picture, first name, last name, display name, title, department, office, email, telephone, fax, password settings and a variety of other Active Directory user attributes.

   ![how-to-scan-users-8.jpg](/docs/.document360/assets/article_195/image_011.jpg)
