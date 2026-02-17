<!-- # Overview of scanning targets and methods -->
[Lansweeper](https://www.lansweeper.com/) offers a variety of [methods to scan your network](https://www.lansweeper.com/resources/lansweeper-scanning-guide/), most of which can be configured in the **Scanning > Scanning Targets** section of the Lansweeper On-prem web console. You can use one or more of these scanning methods, depending on your personal needs and preferences.

The overview below lists the various available scanning methods and some basic properties of each. This can help you make an informed decision on which method(s) to use. You can click through to a specific scanning method to see its respective knowledge base article, where the method is explained in more detail.

| Scanning method | Scans Windows computers | Scans Linux, Unix, Mac computers | Scans devices (printers, switches...) and ESX(i) | Scanning schedule | Scans new assets not yet in database | Agentless |
| --- | --- | --- | --- | --- | --- | --- |
| [Active Directory Computer Path](/docs/scanning-with-an-active-directory-computer-path-scanning-target) | ✔ | ✔ | ✔ | Fixed | ✔ | ✔ |
| [Active Directory Domain](/docs/scan-an-active-directory-domain-scanning-target) | ✔ | ✔ | ✔ | Dynamic | ✔ | ✔ |
| [Active Directory Path (Eventlog only)](/docs/scanning-with-an-eventlog-only-scanning-target) | event log data only | ✘ | ✘ | Interval | ✔ | ✔ |
| [Active Directory User/Group Path](/docs/scanning-with-an-active-directory-usergroup-path-scanning-target) | AD users and groups only | ✘ | ✘ | Fixed | AD users and groups only | ✔ |
| [AirWatch](/docs/scan-mobile-devices-through-vmware-workspace-one-uem-powered-by-airwatch) | ✘ | ✘ | ✔  mobile devices: Android, iOS, Chrome OS, Windows Phone | Fixed or interval | ✔ | ✔ |
| [Asset Group](/docs/scanning-with-an-asset-group-asset-type-or-report-scanning-target) | ✔ | ✔ | ✔ | Fixed or interval | ✘ | ✔ |
| [Asset Radar](/docs/introduction-to-asset-radar) | ✔ | ✔ | ✔ | Continuous | ✔ | ✔ |
| [Asset Type](/docs/scanning-with-an-asset-group-asset-type-or-report-scanning-target) | ✔ | ✔ | ✔ | Fixed or interval | ✘ | ✔ |
| [AWS Region](/docs/scan-an-aws-cloud-environment) | ✔  Cloud hosted | ✔  Cloud hosted | ✘ | Fixed or interval | ✔ | ✔ |
| [Azure](/docs/scan-an-azure-cloud-environment) | ✔  Cloud hosted | ✔  Cloud hosted | ✘ | Fixed or interval | ✔ | ✔ |
| [Credential-free Device Recognition](/docs/credential-free-device-recognition-cdr) | ✔  (can update information) | ✔  (can update information) | ✘  (can update information) | Fixed or interval | ✔ | ✔ |
| [Chrome OS](/docs/how-to-scan-chrome-os-machines) | ✘ | ✘ | ✔  Chrome OS devices | Fixed or interval | ✔ | ✔ |
| [Intune](/docs/scan-mobile-devices-through-microsoft-intune) | ✘ | ✘ | ✔  mobile devices: Android, iOS, Windows Phone | Fixed or interval | ✔ | ✔ |
| [Intune V2](/docs/scan-mobile-devices-through-microsoft-intune) | ✘ | ✘ | ✔  mobile devices: Android, iOS, Windows Phone | Fixed or interval | ✔ | ✔ |
| [IP Range](/docs/scanning-with-an-ip-range-scanning-target) | ✔ | ✔ | ✔ | Fixed or interval | ✔ | ✔ |
| [Report](/docs/scanning-with-an-asset-group-asset-type-or-report-scanning-target) | ✔ | ✔ | ✔ | Fixed or interval | ✘ | ✔ |
| [SCCM](/docs/integrate-lansweeper-with-sccm) | ✔ | ✔ | ✔  (but no assets created) | Fixed or interval | ✔ | ✔ |
| [Windows Computer](/docs/scan-a-windows-computer-scanning-target) | ✔ | ✘ | ✘ | Fixed | ✔ | ✔ |
| [Windows Computer (Eventlog only)](/docs/scanning-with-an-eventlog-only-scanning-target) | event log data only | ✘ | ✘ | Interval | ✔ | ✔ |
| [Workgroup](/docs/scanning-with-a-workgroup-scanning-target) (deprecated) | ✔ | ✘ | ✘ | Dynamic | ✔ | ✔ |
| [Batch Scanning](/docs/scanning-assets-with-batch-scanning) | ✔ | ✔ | ✔ | ✘ | ✔ | ✔ |
| Rescan buttons | ✔ | ✔ | ✔ | ✘ | ✘ | ✔ |
| [LsAgent](/docs/introduction-to-lsagent-for-windows-linux-and-mac) | ✔ | ✔ | ✘ | custom | ✔ | ✘ |
| [LsPush](/docs/introduction-to-the-lspush-scanning-agent-for-windows) | ✔ | ✘ | ✘ | custom | ✔ | ✘ |