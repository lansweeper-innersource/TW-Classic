<!-- # Scan an Active Directory Domain scanning target -->
[Lansweeper](https://www.lansweeper.com/) offers the Active Directory Domain scanning target. This is an agentless, fully automated scanning target suitable for scanning Windows computers that are part of an Active Directory domain.

Active Directory Domain can be configured to scan an entire domain or only a select number of sites or OUs. It contacts your domain controllers every X minutes to retrieve a list of newly logged on computers and scans those computers if they haven't been scanned by an Active Directory Domain target in the last X number of hours or days. If a computer was scanned by an Active Directory Domain target at one point, but then does not report to a domain controller again, the Active Directory Domain target will also rescan that computer after X hours or days. Active Directory Domain scanning targets allow you to scan an unlimited number of domains.

To submit a domain (entirely or in part) for scanning with an Active Directory Domain target, select **Add Scanning Target** in the **Scanning > Scanning Targets** section of the web console and choose the Active Directory Domain scanning type in the resulting pop-up. You'll need to enter your domain's DNS and NetBIOS names into the pop-up window. If you have multiple scanning servers, there will be separate configuration tabs on the **Scanning Targets** page, one for each server.





As agentless scanning of Windows computers requires credentials, make sure to submit and map your Windows scanning credentials as well, by following the instructions in [this knowledge base article](/classic/docs/create-and-map-scanning-credentials).

## Active Directory Domain settings

Below is an overview of available Active Directory Domain buttons, options and settings. What is scanned by the target can be configured in the **Add Scanning Target** pop-up itself, while the schedule that is used can be configured further down the **Scanning > Scanning Targets** page. The same schedule applies to all Active Directory Domain targets.





- Domain DNS name: your domain's DNS name. If you're not sure what your domain's DNS name is, you can verify this by following the instructions in [this knowledge base article](/classic/docs/finding-your-domains-dns-and-netbios-names).
- Domain (Netbios): your domain's NetBIOS name. If you're not sure what your domain's NetBIOS name is, you can verify this by following the instructions in [this knowledge base article](/classic/docs/finding-your-domains-dns-and-netbios-names).  

  You must submit your domain's DNS and NetBIOS names, even if you don't plan on scanning your entire domain.

  If the Active Directory Domain target sees a non-Windows asset report to a domain controller, that asset is passed off to the same scanning procedure used by the IP Range scanning targets and is scanned as well. An asset is considered a Windows computer if its operatingSystem attribute in Active Directory includes the words "Windows" or "Hyper-V". Objects whose operatingSystem attribute does not include the words "Windows" or "Hyper-V" are considered non-Windows.
- Description: custom description you can assign to the scanning target
- Add OU Filter: use this button to limit scanning to certain computer containers or OUs.  

  If you add OU filters, the Active Directory Domain target will only scan the specified OUs and any sub-OUs contained within.
- Add Site Filter: if you add a site filter, the Active Directory Domain target will only contact domain controllers in the specified Active Directory site for a list of newly logged on computers.  

  Whenever possible, it is recommended that you use OU filters instead of site filters. Unless you are absolutely certain which domain controllers belong to which site and which computers are managed by those domain controllers, do not use site filters.

  If you add both site and OU filters, the site filters are applied first and then the OU filters. The scanning target will only contact domain controllers in the specified site(s) for a list of newly logged on computers and, of those newly logged on computers, only computers that belong to the OUs submitted by you will be scanned.
- Enable: check/uncheck this box to enable/disable scanning of the scanning target.
- Check Interval: determines how often (every X minutes) the scanning target contacts your domain controllers to retrieve a list of newly logged on computers.
- Min. Time Between Scan (per Asset): determines how long (X hours or days) the scanning target will wait before rescanning a machine previously scanned by the target.   
  In the example above, the target will scan a computer that reports to a domain controller, if that computer hasn't been scanned by the target in the last 20 hours.
- Max. Time Between Scan (per Asset): determines how long (X hours or days) the scanning target will wait before rescanning a machine that was previously scanned by the target, but that has not reported to a domain controller again.   
  In the example above, the target will rescan a computer previously scanned by the target after 3 days, even if that computer has not reported to a domain controller again.
