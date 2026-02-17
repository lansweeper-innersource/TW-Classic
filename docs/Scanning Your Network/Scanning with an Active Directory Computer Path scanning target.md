<!-- # Scanning with an Active Directory Computer Path scanning target -->
Active Directory Computer Path is an agentless, scheduled scanning target that scans any Windows computers in the Active Directory computer container or OU specified by you. You can submit an unlimited number of Active Directory Computer Path targets for scanning and specify a separate scanning schedule for each.

To submit a target like this for scanning, click the **Add Scanning Target** button in the **Scanning > Scanning Targets**section of the web console and choose the Active Directory Computer Path scanning type in the resulting pop-up. If you have multiple scanning servers, there will be multiple configuration tabs on the **Scanning Targets** page, one for each server.





As agentless scanning of Windows computers requires credentials, make sure to submit and map your Windows scanning credentials as well, by following the instructions in [this knowledge base article](/docs/create-and-map-scanning-credentials).

## Active Directory Computer Path settings

Below is an overview of available Active Directory Computer Path options and settings. Each scanning target can be configured differently.



- **Adsi Path**: the computer container or organizational unit should be entered.

  Active Directory Computer Path imports any computer objects whose operatingSystem attribute includes the words "Windows" or "Hyper-V". It does this for the CN/OU you've submitted and any sub-OUs contained within. Objects whose operatingSystem attribute does not include the words "Windows" or "Hyper-V" are considered non-Windows and passed off to the same scanning procedure used by the IP Range scanning targets. These non-Windows assets are scanned as if they were submitted for scanning as part of an IP Range target.

  If you want computers that are disabled in AD to be included in your scan, make sure this option is ticked in the **Configuration > Server Options** section of the web console. More information can be found in [this knowledge base article](/docs/how-to-scan-disabled-active-directory-users-and-computers).
- **Domain (Netbios)**: the NetBIOS name of the domain your computer CN/OU belongs to should be entered.
- **Description**: a custom description of the scanning target can be entered.
- **Schedule**: determines when (on which days of the week and at what time) the scanning target will be scanned.
- **Enable**: toggle this option to enable or disable scanning of the scanning target.
