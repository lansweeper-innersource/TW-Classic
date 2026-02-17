<!-- # Comparing Lansweeper Sites and Lansweeper On-premises -->
Before you start discovering your IT inventory it’s important to understand what our different solutions have to offer. We have listed the most important features you can expect in our two distinct platforms.

Lansweeper Sites allows you to manage your IT inventory completely from the cloud.

If you would like to try Lansweeper Sites, go to <https://app.lansweeper.com/try>. After registering your account you can download and install the Lansweeper application. It only takes a few minutes to start exploring your scanned data in Lansweeper Sites.

Some key features Lansweeper Sites offers are:

- Installation federation
- Access to your assets from anywhere
- Advanced permission and scope system
- Risk Insights
- OT discovery
- API Access

If you would like to try Lansweeper On-premises instead, go to <https://www.lansweeper.com/product/on-prem/>.

## Discovery and inventory

|  | | **Inventory in Lansweeper Sites** | | **Inventory in Lansweeper On-premises** |
| --- | --- | --- | --- | --- |
| **Feature** | **Item** | **Lansweeper Discovery** | **Lansweeper On-prem scanning** | **Classic Lansweeper On-prem scanning** |
| Discovery/scanning targets and data | Active Directory | ✔ (Merged into one AD domain target for Network Discovery) | ✔ (Computer Path, Domain, User/Group Path) | ✔ (Computer Path, Domain, User/Group Path) |
| AirWatch (VMware Workspace One UEM) | Planned (Cloud Discovery) | ✔ | ✔ |
| Asset Group | Planned (Inventory action) | ✘ | ✔ |
| Asset Type | Planned (Inventory action) | ✘ | ✔ |
| Amazon Web Services (AWS) | ✔ (using Cloud Discovery) | ✘ | ✔ (Compute only) |
| Azure | ✔ (using Cloud Discovery, China region planned) | ✘ | ✔ (Compute only, China region supported) |
| Azure Active Directory/Microsoft Entra ID | Planned (Cloud Discovery) | ✘ | ✔ |
| Chrome OS | Planned  (Cloud Discovery) | ✔ | ✔ |
| Citrix | ✔ | ✘ | ✔ |
| Google Cloud Platform (GCP) | ✔ (using Cloud Discovery) | ✘ | ✘ |
| Hyper-V | ✔ (using Network Discovery) | ✔ (using IP range, AD targets, or Windows computer) | ✔ |
| Intune | ✔**ᶜ** (using Cloud Discovery) | ✔ | ✔ (Mobile devices only) |
| IP range (start to finish address) | ✔ | ✔ | ✔ |
| IP address, IP range using CIDR, hostname, FQDN | ✔ | ✔ | ✘ |
| IPv4/6 range exclusions | ✔ | ✔ | ✔ |
| Microsoft 365 | ✔ (using Cloud Discovery) | ✘ | ✔ |
| Monitor or display discovery | Planned (IT Agent and Network Discovery) | ✔ | ✔ |
| Report | Planned (Inventory action) | ✘ | ✔ |
| SCCM | ✔ | ✔ | ✔ |
| Schedules | ✔ | ✔ | ✔ (Set per target) |
| User data | ✔ (User data from Windows, Linux, and macOS related with AD, Azure AD, Intune, and M365) | ✔ | ✔ (User data from Windows and Linux  related with AD, Azure AD, and M365) |
| User logon data | Planned (Network Discovery and IT Agent) | ✔ | ✔ |
| VMware ESXi and vCenter | ✔ | ✔ | ✔ |
| Windows computer | ✔**ª** | ✔ | ✔ |
| Custom scanning with commands/scripts | Planned (Network Discovery) | ✘ | ✘ |
| Custom eventlog scanning | Planned (Network Discovery) | ✘ | ✔ |
| Custom file/directory scanning in Linux | Planned (Network Discovery) | ✘ | ✔ |
| Custom file scanning in Windows | Planned (Network Discovery) | ✘ | ✔ |
| Custom performance counters | Planned (Network Discovery) | ✘ | ✔ |
| Discovery/scanning and inventory options | Agent-based Discovery | ✔ (IT Agent to Network Discover Hub or Lansweeper Sites) | ✔ (IT Agent to Lansweeper Sites) | ✔ (LsAgent) |
| Agent-based on demand Discovery (without installation on asset) | ✔ (IT Agent Portable) | ✔ (LsPush) | ✔ (LsPush) |
| Auto update | ✔ (all components) | ✔ (On-prem scanning and LsAgent Windows only) | ✔ (On-prem scanning and LsAgent Windows only) |
| Custom SNMP scanning with OIDs and MIB files | Planned  (Network Discovery) | ✘ | ✔ |
| Custom registry key scanning in Windows | Planned  (Network Discovery) | ✘ | ✔ |
| Database discovery | Planned for various databases  (Network Discovery) | ✔  (SQL Server only) | ✔  (SQL Server only) |
| Deployments | ✘ (integrations can be used instead) | ✘ (integrations can be used instead) | ✔ |
| Discovery progress | ✔ (currently only available in Network Discovery Hub) | ✔ | ✔ |
| Firewall rule scanning | Planned (Network Discovery) | ✘ | ✔ |
| Framework | .NET 8 (in IT Agent and Network Discovery) | .NET Framework 4.8 (.NET 8 for LsAgent) | .NET Framework 4.8 (.NET 8 for LsAgent) |
| HP warranty data | Planned | Planned | ✔ |
| Import and export discovery actions/credentials | Planned (Network Discovery) | ✘ | ✘ |
| Link with external credential vaults | Planned (Network Discovery) | ✘ | ✘ |
| LsAgent Relay configuration | *N/A* | ✘ | ✔ |
| Manual asset adding | *✔* | *✔* | *✔* |
| Manual asset rescanning | *✔* | *✔* | *✔* |
| Open TCP ports and extra fingerprint data | Planned (Network Discovery) | ✘ | ✘ |
| Operating system support | ✔**\*** | ✔**ᵇ** | ✔**ᵇ** |
| OT assets | ✔ | ✔ (in combination with Network Discovery) | ✔ (in combination with Network Discovery) |
| Passive detection (Asset radar/network visibility) | ✔ (using Network Discovery) | ✔ (Asset Radar) | ✔ (Asset Radar) |
| Scan/Discovery issues | ✔ | ✔ | ✔ |
| Scanning/Discovery exclusions | Planned (Network Discovery) | ✔ | ✔ |
| Discovery/scanning credentials | AirWatch (VMware Workspace One UEM) | Planned  (Cloud Discovery) | ✔**ᵉ** | ✔ |
| Amazon Web Services (AWS) | ✔ (using Cloud Discovery) | ✘**ᵉ** | ✔ |
| Azure | ✔ (using Cloud Discovery) | ✘**ᵉ** | ✔ |
| Chrome OS | Planned (Cloud Discovery) | ✘**ᵉ** | ✔ |
| Citrix | ✔ | ✔**ᵉ** | ✔ |
| GCP | ✔ (using Cloud Discovery) | ✘**ᵉ** | ✔ |
| Integration with legacy AD LAPS | Planned (Network Discovery) | ✘ | ✔ |
| Integration with Windows LAPS | Planned (Network Discovery) | ✘ | ✘ |
| Integration with external credential vaults | Planned (Network Discovery) | ✘ | ✘ |
| Microsoft Cloud Service (Azure, Azure AD, Entra ID, Intune, M365) | ✔ (using Cloud Discovery) | ✔**ᵉ** | ✔ |
| SCCM | ✔ | ✘**ᵉ** | ✔ |
| SSH | ✔ | ✔**ᵈ** | ✔ |
| VMware ESXi | ✔ | ✔**ᵉ** | ✔ |
| Windows | ✔ª | ✔**ᵈ** | ✔ |
| SNMP | ✔ | ✔**ᵈ** | ✔ |

  

**ª** Local tracking using IT Agent: Windows, Linux and macOS.   
Remote discovery (Windows, Linux and macOS): On Linux, Windows discovery is limited to Credential-free Device Recognition (CDR). Full data discovery (software, user info, ...) is planned but not yet available and will require remote WinRM on Windows assets.   
Active Directory discovery is not supported on Linux sensors due to connectivity incompatibilities with domain controllers.

**ᵇ** Local tracking using LsAgent: Windows, Linux and macOS  
Remote scanning: Windows only

**ᶜ** Currently in beta; you might see duplicates if you're also using Lansweeper On-prem scanning in your site. No duplicates if you're only using Network, IT Agent, or Cloud Discovery.

**ᵈ** Unique assets in combination with Lansweeper Discovery: planned by Q3 2025.   
Already available via beta; sign up for [the Network Discovery beta](https://www.lansweeper.com/product/beta/).

**ᵉ**Unique assets in combination with Lansweeper Discovery: planned by Q4 2025, beta not available yet.

## Marketplace

### Integrations

| **Feature** | **Item** | **Lansweeper Sites** | **Lansweeper On-prem** |
| --- | --- | --- | --- |
| ITAM | AdminRemix | ✔ | ✘ |
| Asset Panda | ✔ | ✘ |
| CyberStockroom | ✔ | ✘ |
| Oomnitza Data connector | ✔ | ✘ |
| Reftab | ✔ | ✘ |
| Setyl | ✔ | ✘ |
| Timly Asset Tracking Maintenance | ✔ | ✘ |
| Analytics | Microsoft Power BI | ✔ | ✘ |
| Splunk | ✔ | ✔ |
| Monitoring | PRTG | ✔ | ✘ |
| Senhub | ✔ | ✘ |
| Subscription and SAM | AssetLabs Streamline | ✔ | ✘ |
| Licenseware | ✔ | ✔ |
| CMDB | 4me | ✔ | ✘ |
| Efecte | ✔ | ✘ |
| HaloITSM | ✔ | ✘ |
| HaloPSA | ✔ | ✘ |
| Jira Service Management Assets | ✔ | ✘ |
| Servicely.ai | ✔ | ✔ |
| ServiceNow - CI Sync | ✔ | ✔ |
| ServiceNow Service Graph | ✔ | ✘ |
| TOPdesk ITSM | ✔ | ✘ |
| Vivantio CSM | ✔ | ✘ |
| Vivantio ITSM | ✔ | ✘ |
| Security | Armis Data Connector | ✔ | ✘ |
| Automox | ✔ | ✘ |
| Axonius data connector | ✔ | ✔ |
| Cortex XSOAR | ✔ | ✘ |
| DeepSurface RiskAnalyzer | ✔ | ✘ |
| Device Total | ✔ | ✘ |
| Devolutions Remote Desktop Manager | ✔ | ✘ |
| FortifyData Cybersecurity Assessment | ✔ | ✘ |
| IBM Q-Radar | ✔ | ✘ |
| Microsoft Sentinel | ✔ | ✘ |
| Noetic Cyber™ | ✔ | ✘ |
| OverSOC | ✔ | ✘ |
| Splunk Enterprise Security | ✔ | ✘ |
| Splunk SOAR | ✔ | ✘ |
| ThreatAware | ✔ | ✘ |
| Service desk | Fresh Service | ✔ | ✘ |
| InvGate Service Desk | ✔ | ✘ |
| Jira Service Management | ✔ | ✘ |
| ManageEngine ServiceDesk Plus | ✔ | ✘ |
| Mint Service Desk | ✔ | ✘ |
| Services | Help Desk Migration | ✔ | ✘ |

  

### Services

| **Feature** | **Item** | **Lansweeper Sites** | **Lansweeper On-prem** |
| --- | --- | --- | --- |
| Implementation | Health Check by Cheops | ✔ | ✔ |
| Health Check by ITHealth | ✔ | ✔ |
| ITAM Solutions, by SHI | ✔ | ✘ |
| Lansweeper Concierge by ITHealth | ✔ | ✔ |
| Onboarding Services by Cheops | ✔ | ✔ |
| Professional Services, by ITHealth | ✔ | ✔ |
| Professional Services, by Multipoint | ✔ | ✘ |
| Valiantys Governance | ✔ | ✘ |

## Analyze

### Filtering and sorting

| **Feature** | **Item** | **Lansweeper Sites** | **Lansweeper On-prem** |
| --- | --- | --- | --- |
| Built-in Views | Software overview | ✔ | ✔ |
| Inventory overview | ✔ | ✔ |
| License keys | ✘ | ✔ |
| Microsoft 365 | ✔ | ✔ |
| Risk Insights | ✔ | ✘ |
| Users overview | ✔ | ✘ |
| Custom Views | Inventory | ✔ | ✘ |
| Scan issues | ✔ | ✘ |
| Risk insights | ✔ | ✘ |
| Software | ✔ | ✘ |
| Users | ✔ | ✘ |
| Filter Views | Inventory | ✔ (Advanced) | ✔ (Basic) |
| Scan issues | ✔ (Advanced) | ✔ (Basic) |
| Risk insights | ✔ | ✘ |
| Software | ✔ (Advanced) | ✔ (Basic) |
| Users | ✔ (Advanced) | ✔ (Basic) |
| Share Views | Share Custom views | ✔ | ✘ |

### Inventory

| **Feature** | **Item** | **Lansweeper Sites** | **Lansweeper On-prem** |
| --- | --- | --- | --- |
| Cleanup | Delete assets or change asset states | ✔ (Planned for Network Discovery) | ✔ |

### Report

| **Feature** | **Item** | **Lansweeper Sites** | **Lansweeper On-prem** |
| --- | --- | --- | --- |
| Export Reports | CSV | ✔ | ✔ |
| Excel | ✔ | ✔ |
| HTML File | ✘ | ✘ |
| JSON | ✘ | ✘ |
| PDF | ✘ | ✘ |
| Word | ✘ | ✘ |
| XML | ✘ | ✔ |
| Report Library | Built-in reports | ✔ | ✔ |
| Run Report | Manual | ✔ | ✔ |
| Schedule | ✔ | ✔ |
| Email scheduled report | ✘ | ✔ |

  

### Diagrams

| **Feature** | **Item** | **Lansweeper Sites** | **Lansweeper On-prem** |
| --- | --- | --- | --- |
| Diagram Viewer | Asset scopes | ✔ | ✘ |
| Cloud assets | Planned | ✘ |
| Export diagrams | ✔ | ✘ |
| Filters by asset metadata | ✔ | ✘ |
| Information on the asset | ✔ | ✘ |
| Integrated search | ✔ | ✘ |
| Issues on the asset | ✔ | ✘ |
| IT assets | ✔ | ✘ |
| Location maps | Partial | ✔ |
| Network topologies | ✔ | ✘ |
| Network Discovery assets (including OT) | Planned | ✘ |
| Running status on the asset (for virtual assets) | ✔ | ✘ |
| Virtual environments | ✔ | ✘ |

For location maps: the location asset type is provided in Lansweeper to illustrate related assets and relations.

### Helpdesk

| **Feature** | **Item** | **Lansweeper Sites** | **Lansweeper On-prem** |
| --- | --- | --- | --- |
| Helpdesk |  | Using integrations | ✔ |

  

## Configure

### Access Management

| **Feature** | **Item** | **Lansweeper Sites** | **Lansweeper On-prem** |
| --- | --- | --- | --- |
| Asset Scopes |  | ✔ | ✘ |
| Authentication | MFA | ✔ | ✘ |
| SSO | ✔ | ✘ |
