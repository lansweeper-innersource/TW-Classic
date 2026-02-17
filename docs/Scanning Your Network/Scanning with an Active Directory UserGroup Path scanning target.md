<!-- # Scanning with an Active Directory User/Group Path scanning target -->
Active Directory User/Group Path is an agentless, scheduled scanning target suitable for scanning Active Directory users and Active Directory user and computer groups. It only scans AD users and AD groups, not computer objects.

Active Directory User/Group Path scanning targets allow you to scan an unlimited number of OUs in an unlimited number of domains for users and groups and to specify a separate scanning schedule for each OU.

To submit a target like this for scanning, select **Add Scanning Target** in the **Scanning > Scanning Targets** section of the web console and choose the Active Directory User/Group Path scanning type in the resulting pop-up. If you have multiple scanning servers, there will be multiple configuration tabs on the **Scanning** **Targets** page, one for each server.





Active Directory User/Group Path requires a credential with read-only access to Active Directory. You can either use a credential with the necessary privileges as your global Windows credential or map the credential to the domain you are trying to scan. More info on submitting and mapping scanning credentials can be found in [this knowledge base article](/docs/create-and-map-scanning-credentials).

## Active Directory User/Group Path settings

Below is an overview of available Active Directory User/Group Path options and settings. Each scanning target can be configured differently.



- Adsi Path: organizational unit (OU).  

  Active Directory User/Group Path scans the users in the OU you've submitted and any sub-OUs contained within. It also scans the user and computer groups within the OU.

  If you want users that are disabled in AD to be included in your scan, make sure this option is ticked in the Configuration\Server Options section of the web console: [Scan users that are disabled in Active Directory](/docs/how-to-scan-disabled-active-directory-users-and-computers). This option is available from Lansweeper 7.2 onward. If this checkbox is not ticked, disabled users are skipped during scanning.
- Domain (Netbios): NetBIOS name of the domain your OU belongs to.
- Description: custom description you can assign to the scanning target.
- Schedule: determines when (on which days of the week and at what time) the scanning target will be scanned.
- Enable: check/uncheck this box to enable/disable scanning of the scanning target.
