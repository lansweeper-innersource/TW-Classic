<!-- # Overview of scanning targets and methods -->
[Lansweeper](https://www.lansweeper.com/) offers a variety of [methods to scan your network](https://www.lansweeper.com/resources/lansweeper-scanning-guide/), most of which can be configured in the **Scanning > Scanning Targets** section of the Lansweeper On-prem web console. You can use one or more of these scanning methods, depending on your personal needs and preferences.

The overview below lists the various available scanning methods and some basic properties of each. This can help you make an informed decision on which method(s) to use. You can click through to a specific scanning method to see its respective knowledge base article, where the method is explained in more detail.

| Scanning method | Scans Windows computers | Scans Linux, Unix, Mac computers | Scans devices (printers, switches...) and ESX(i) | Scanning schedule | Scans new assets not yet in database | Agentless |
| --- | --- | --- | --- | --- | --- | --- |
| [Active Directory Computer Path](/classic/docs/scanning-with-an-active-directory-computer-path-scanning-target) | ✔ | ✔ | ✔ | Fixed | ✔ | ✔ |
| [Active Directory Domain](/classic/docs/scan-an-active-directory-domain-scanning-target) | ✔ | ✔ | ✔ | Dynamic | ✔ | ✔ |
| [Active Directory Path (Eventlog only)](/classic/docs/scanning-with-an-eventlog-only-scanning-target) | event log data only | ✘ | ✘ | Interval | ✔ | ✔ |
| [Active Directory User/Group Path](/classic/docs/scanning-with-an-active-directory-usergroup-path-scanning-target) | AD users and groups only | ✘ | ✘ | Fixed | AD users and groups only | ✔ |
| [AirWatch](/classic/docs/scan-mobile-devices-through-vmware-workspace-one-uem-powered-by-airwatch) | ✘ | ✘ | ✔  mobile devices: Android, iOS, Chrome OS, Windows Phone | Fixed or interval | ✔ | ✔ |
| [Asset Group](/classic/docs/scanning-with-an-asset-group-asset-type-or-report-scanning-target) | ✔ | ✔ | ✔ | Fixed or interval | ✘ | ✔ |
| [Asset Radar](/classic/docs/introduction-to-asset-radar) | ✔ | ✔ | ✔ | Continuous | ✔ | ✔ |
| [Asset Type](/classic/docs/scanning-with-an-asset-group-asset-type-or-report-scanning-target) | ✔ | ✔ | ✔ | Fixed or interval | ✘ | ✔ |
| [AWS Region](/classic/docs/scan-an-aws-cloud-environment) | ✔  Cloud hosted | ✔  Cloud hosted | ✘ | Fixed or interval | ✔ | ✔ |
| [Azure](/classic/docs/scan-an-azure-cloud-environment) | ✔  Cloud hosted | ✔  Cloud hosted | ✘ | Fixed or interval | ✔ | ✔ |
| [Credential-free Device Recognition](/classic/docs/credential-free-device-recognition-cdr) | ✔  (can update information) | ✔  (can update information) | ✘  (can update information) | Fixed or interval | ✔ | ✔ |
| [Chrome OS](/classic/docs/how-to-scan-chrome-os-machines) | ✘ | ✘ | ✔  Chrome OS devices | Fixed or interval | ✔ | ✔ |
| [Intune](/classic/docs/scan-mobile-devices-through-microsoft-intune) | ✘ | ✘ | ✔  mobile devices: Android, iOS, Windows Phone | Fixed or interval | ✔ | ✔ |
| [Intune V2](/classic/docs/scan-mobile-devices-through-microsoft-intune) | ✘ | ✘ | ✔  mobile devices: Android, iOS, Windows Phone | Fixed or interval | ✔ | ✔ |
| [IP Range](/classic/docs/scanning-with-an-ip-range-scanning-target) | ✔ | ✔ | ✔ | Fixed or interval | ✔ | ✔ |
| [Report](/classic/docs/scanning-with-an-asset-group-asset-type-or-report-scanning-target) | ✔ | ✔ | ✔ | Fixed or interval | ✘ | ✔ |
| [SCCM](/classic/docs/integrate-lansweeper-with-sccm) | ✔ | ✔ | ✔  (but no assets created) | Fixed or interval | ✔ | ✔ |
| [Windows Computer](/classic/docs/scan-a-windows-computer-scanning-target) | ✔ | ✘ | ✘ | Fixed | ✔ | ✔ |
| [Windows Computer (Eventlog only)](/classic/docs/scanning-with-an-eventlog-only-scanning-target) | event log data only | ✘ | ✘ | Interval | ✔ | ✔ |
| [Workgroup](/classic/docs/scanning-with-a-workgroup-scanning-target) (deprecated) | ✔ | ✘ | ✘ | Dynamic | ✔ | ✔ |
| [Batch Scanning](/classic/docs/scanning-assets-with-batch-scanning) | ✔ | ✔ | ✔ | ✘ | ✔ | ✔ |
| Rescan buttons | ✔ | ✔ | ✔ | ✘ | ✘ | ✔ |
| [LsAgent](/classic/docs/introduction-to-lsagent-for-windows-linux-and-mac) | ✔ | ✔ | ✘ | custom | ✔ | ✘ |
| [LsPush](/classic/docs/introduction-to-the-lspush-scanning-agent-for-windows) | ✔ | ✘ | ✘ | custom | ✔ | ✘ |