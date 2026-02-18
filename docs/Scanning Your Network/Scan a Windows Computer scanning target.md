<!-- # Scan a Windows Computer scanning target -->
Windows Computer is an agentless, scheduled scanning target that scans any individual Windows domain or workgroup computer specified by you. You can submit an unlimited number of Windows Computer targets for scanning and specify a separate scanning schedule for each.

To submit a target like this for scanning, select **Add Scanning Target** in the **Scanning > Scanning Targets** section of the web console and choose the Windows Computer scanning type in the resulting pop-up. If you have multiple scanning servers, there will be multiple configuration tabs on the Scanning Targets page, one for each server.





As agentless scanning of Windows computers requires credentials, make sure to submit and map your Windows scanning credentials as well, by following the instructions in [this knowledge base article](/classic/docs/create-and-map-scanning-credentials).

## Windows Computer settings

Below is an overview of available Windows Computer options and settings. Each scanning target can be configured differently.



- Target: NetBIOS name of the domain or workgroup computer you want to scan.
- Domain/Workgroup (Netbios): NetBIOS name of the domain or name of the workgroup your computer belongs to.
- Description: custom description you can assign to the scanning target.
- Schedule: determines when (on which days of the week and at what time) the scanning target will be scanned.
- Enable: check/uncheck this box to enable/disable scanning of the scanning target.
