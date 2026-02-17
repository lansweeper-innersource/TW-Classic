<!-- # Create and map scanning credentials -->

This page is for Lansweeper Classic. For Lansweeper Sites using Network Discovery, see [Create discovery credentials](/docs/create-discovery-credentials).

[Lansweeper](https://www.lansweeper.com/) uses scanning credentials, which are login/password combinations and certificates/keys, to remotely access and scan network assets. The following assets require a scanning credential in order to be scanned remotely: Linux, Unix, Mac and Windows computers, VMware and vCenter servers, Citrix XenServers, network devices (printers, switches) that have SNMP enabled, AWS and Azure cloud assets, and Office 365 accounts. Windows computer credentials are also used when deploying packages on computers.

Your Lansweeper On-premises installation allows you to submit an unlimited number of scanning credentials. Scanning credentials are managed in the following section of the web console: **Scanning > Scanning Credentials**.

![menu-scanning-scanning-credentials.jpg](/docs/.document360/assets/article_180/image_002.jpg)

Scanning credentials must be created and then mapped, so Lansweeper knows when to use them. If you map a Windows credential to a domain for instance, Lansweeper will try to use that credential for any Windows computer within that domain.

Linux, Mac and Windows computers can be scanned locally as well, with a scanning agent. Linux and Mac can be scanned with [LsAgent](/docs/introduction-to-lsagent-for-windows-linux-and-mac), while Windows can be scanned with [LsAgent](/docs/introduction-to-lsagent-for-windows-linux-and-mac) or the older [LsPush](/docs/introduction-to-the-lspush-scanning-agent-for-windows) scanning agent. If you scan your computers exclusively with an agent and don't use the deployment module, you do not need to submit computer scanning credentials.

[Creating scanning credentials](#heading1)

- [Airwatch](#heading3)
- [AWS](#heading4)
- [Azure](#h376818429901675258920305)
- [Chrome OS](#h227416601111675258927828)
- [Citrix](#h6354044191311675258934068)
- [Intune](#h4472063731501675258939670)
- [Office 365](#h4823011611681675258947552)
- [Microsoft Cloud Service to scan Office 365](#h2354863021851675258953778)
- [Microsoft Cloud Service to scan Intune](#h6858765112011675258961128)
- [SCCM](#h4970773422161675258967008)
- [SNMP (v1/v2)](#h9047364642301675258972401)
- [SNMP (v3)](#h6216594972431675258977178)
- [SSH](#h3525972072551675258983321)
- [SSH certificate](#h3734877722661675258990018)
- [vCenter](#h8377408762761675258995935)
- [VMware](#h8700711722851675259003240)
- [Windows](#h7160035012931675259008716)

[Mapping scanning credentials](#heading2)

- [AWS region](#h3771657283061675259023453)
- [Azure subscription ID](#h8376401773121675259031210)
- [IP address](#h9811232513171675259037465)
- [IP range](#h4359842623211675259041972)
- [Individual Windows computer](#h6351306093241675259047888)
- [Domain or workgroup](#h6779615743261675259052965)

## Creating scanning credentials

To create a credential, select **Add new Credential** in the **Scanning > Scanning Credentials** section of the web console. There are various types of credentials:

### AirWatch credentials (added in Lansweeper 7.2)

![creating-and-mapping-scanning-credentials-21.jpg](/docs/.document360/assets/article_180/image_003.jpg)

- Used for scanning: Android, iOS (iPhone and iPad), Chrome OS and Windows Phone mobile devices enrolled in VMware AirWatch. When you submit an AirWatch credential, an AirWatch scanning target is automatically created as well.
- Must have: read-only access to the REST API in VMware Workspace ONE. Info on how to set this up can be found in [this knowledge base article](/docs/vmware-workspace-one-uem-powered-by-airwatch-scanning-requirements).
- Name: custom name you can assign to the credential.
- Username: your username in VMware Workspace ONE.
- Password: your user account's password.
- Server URL: your VMware Workspace ONE server URL.
- API key: API key with read access to the REST API in VMware Workspace ONE.

### AWS credentials (added in Lansweeper 7.1)

![creating-and-mapping-scanning-credentials-1.jpg](/docs/.document360/assets/article_180/image_004.jpg)

- Used for scanning: AWS VPCs and instances.
- Must have: list-only programmatic access to your EC2-VPC environments. Info on how to set this up can be found in [this knowledge base article](/docs/aws-scanning-requirements).
- Name: custom name you can assign to the credential.
- Access key: access key ID of the user with list access to EC2.
- Secret key: secret access key of the user with list access to EC2.

### Azure credentials (added in Lansweeper 7.1)

![creating-and-mapping-scanning-credentials-2.jpg](/docs/.document360/assets/article_180/image_005.jpg)

- Used for scanning: Azure resource groups and virtual machines.
- Must have: read-only access to your Azure subscription. You must register an application in Azure Active Directory of the type Web App / API, generate a key for it and assign it the Reader role for your subscription. Info on how to set this up can be found in [this knowledge base article](/docs/azure-scanning-requirements).
- Name: custom name you can assign to the credential.
- Directory ID: your Azure Active Directory (tenant) ID.
- Application ID: ID of the application with read access to your subscription.
- Application password: password/key of the application with read access to your subscription.

### Chrome OS credentials (added in Lansweeper 7.2)

![creating-and-mapping-scanning-credentials-22.jpg](/docs/.document360/assets/article_180/image_006.jpg)

- Used for scanning: Chrome OS (e.g. Chromebook) machines. When you submit a Chrome OS credential, a Chrome OS scanning target is automatically created as well.
- Must have: read-only access to the Google Admin SDK API. Info on how to set this up can be found in [this knowledge base article](/docs/chrome-os-scanning-requirements).
- Name: custom name you can assign to the credential.
- Username: email address of your Google account.
- JSON key: JSON key with read access to the Google Admin SDK API.

### Citrix credentials (added in Lansweeper 7.0)

![creating-and-mapping-scanning-credentials-3.jpg](/docs/.document360/assets/article_180/image_007.jpg)

- Used for scanning: Citrix XenServers.
- Must have: access to XenAPI and be able to run the following command groups on your XenServers: delegating, drivers, locate, networking, processes, services, software, storage. Full root access is not required. Info on how to configure Citrix credentials can be found in [this knowledge base article](/docs/citrix-scanning-requirements).
- Name: custom name you can assign to the credential.
- Login: your Citrix login.
- Password: your Citrix login's password.

### Intune credentials (added in Lansweeper 7.1)

![creating-and-mapping-scanning-credentials-4.jpg](/docs/.document360/assets/article_180/image_008.jpg)

- Used for scanning: Android, iOS (iPhone and iPad) and Windows Phone mobile devices enrolled in Microsoft Intune. When you submit an Intune credential, an Intune scanning target is automatically created as well.
- Must have: access to your Intune environment. You must register an application in Azure Active Directory of the type Native and grant it the DeviceManagementManagedDevices.Read.All permission under Microsoft Graph. Your user account must also have access to Intune.
- Name: custom name you can assign to the credential.
- Username: user with the ability to view devices in your Intune environment
- Password: user's password.
- Application ID: ID of the application with the DeviceManagementManagedDevices.Read.All permission.

### Office 365 credentials (added in Lansweeper 7.1)

![creating-and-mapping-scanning-credentials-5.jpg](/docs/.document360/assets/article_180/image_009.jpg)

- Used for scanning: Office 365 accounts. When you submit an Office 365 credential, an Office 365 scanning target is automatically created as well.
- Must have: administrative permissions to Office 365 to be able to inventory all contacts, mailboxes and ActiveSync devices. A global administrator is guaranteed to have sufficient rights.
- Name: custom name you can assign to the credential
- Login: user (email address) with administrative permissions to your Office 365 environment
- Password: user's password

## Microsoft Cloud Service credential to scan your Office 365 data (added in Lansweeper 8.3)

![creating-and-mapping-scanning-credentials-24.jpg](/docs/.document360/assets/article_180/image_010.jpg)

- Used for scanning: Office 365 accounts with a Microsoft Graph application.
- Must have: administrative permissions to Office 365 to be able to inventory all contacts, mailboxes and ActiveSync devices. A global administrator is guaranteed to have sufficient rights.
- Name: custom name you can assign to the credential
- Application ID (obtained when creating the [Microsoft Graph app](https://www.lansweeper.com/knowledgebase/creating-microsoft-cloud-services-application) in Azure)
- Directory ID (obtained when creating the [Microsoft Graph app](https://www.lansweeper.com/knowledgebase/creating-microsoft-cloud-services-application) in Azure)
- Authentication type: either a client secret or a certificate thumbprint
- Create target for: When you check **Create target for: Office 365 v2**, an Office 365 v2 scanning target is automatically created as well.

## Microsoft Cloud Service credential to scan your Intune data (added in Lansweeper 8.3)

![creating-and-mapping-scanning-credentials-24.jpg](/docs/.document360/assets/article_180/image_011.jpg)

- Used for scanning: Mobile devices enlisted in Intune with a Microsoft Graph application.
- Must have: access to your Intune environment. You must register an application in Azure Active Directory of the type Native and grant it the DeviceManagementManagedDevices.Read.All permission under Microsoft Graph. Your user account must also have access to Intune. Info on how to set this up can be found in [this knowledge base article](/docs/scan-mobile-devices-through-microsoft-intune).
- Name: custom name you can assign to the credential
- Application ID (obtained when creating the [Microsoft Graph app](https://www.lansweeper.com/knowledgebase/creating-microsoft-cloud-services-application) in Azure)
- Directory ID  (obtained when creating the [Microsoft Graph app](https://www.lansweeper.com/knowledgebase/creating-microsoft-cloud-services-application) in Azure)
- Authentication type: either a client secret or a certificate thumbprint
- Create target for: When you check **Create target for: Intune v2**, an Intune v2 scanning target is automatically created as well.

### SCCM credentials (added in Lansweeper 7.2)

![creating-and-mapping-scanning-credentials-23.jpg](/docs/.document360/assets/article_180/image_012.jpg)

- Used for scanning: assets from your SCCM server's database. When you submit an SCCM credential, an SCCM scanning target is automatically created as well.
- Must have: local administrative permissions on the SCCM server and, at a minimum, the Read-Only Analyst security role within SCCM's Administrative Users.
- Name: custom name you can assign to the credential.
- Username: a down-level logon name like NetBIOS domain name\username (domain credentials) or a user principal name (UPN) like username@yourdomain.local (domain credentials) or .\username (local credentials) or username@outlook.com (Microsoft accounts).
- Password: your user account's password.
- SCCM server: name, IPv4 address or IPv6 address of an SMS Provider server in your SCCM environment.

### SNMP(v1/v2) credentials

![creating-and-mapping-scanning-credentials-6.jpg](/docs/.document360/assets/article_180/image_013.jpg)

- Used for scanning: network devices that have SNMPv1 or SNMPv2 enabled.
- Must have: read-only SNMP access to your devices.
- Name: custom name you can assign to the credential.
- Community: the (case-sensitive!) SNMP community string used by your devices. Many network devices use public and private as their default SNMP community strings, public being for read-only access and private for read/write access. Your devices could be using custom strings, however.
- Use SNMP(v1)/Use SNMP(v2): optionally, uncheck one of these boxes to have Lansweeper only try SNMPv1 or SNMPv2. Unchecking one of these boxes is generally only recommended if your devices have trouble processing SNMPv1 or SNMPv2 requests.

### SNMP(v3) credentials

![Scanning credentials SNMPv3.png](/docs/.document360/assets/article_180/image_014.jpg)

- Used for scanning: network devices that have SNMPv3 enabled.
- Must have: read-only SNMP access to your devices.
- Name: custom name you can assign to the credential.
- Login: your SNMP login.
- Password: your SNMP login's password.
- Encryption key: encryption key required if authentication type is set to MD5 or SHA1.
- Authentication type: None, MD5 or SHA1.
- Privacy type: None, DES, AES 128, AES 192, AES 256 or Triple DES.
- Context: optionally, context name of the SNMPv3 credential.

### SSH credentials

![creating-and-mapping-scanning-credentials-8.jpg](/docs/.document360/assets/article_180/image_015.jpg)

- Used for scanning: Linux, Unix and Mac computers.
- Must have: access to the uname (Linux/Unix) or system\_profiler (Mac) command. More info on Linux/Unix scanning requirements can be found in [this knowledge base article](/docs/linux-and-unix-agentless-scanning-requirements) and more info on Mac scanning requirements can be found in [this knowledge base article](/docs/apple-mac-scanning-requirements).
- Name: custom name you can assign to the credential.
- Login: your SSH login.
- Password: your SSH login's password.

### SSH certificate credentials

![creating-and-mapping-scanning-credentials-9.jpg](/docs/.document360/assets/article_180/image_016.jpg)

- Used for scanning: Linux and Unix computers.
- Must have: access to the uname command. More info on Linux/Unix scanning requirements can be found in [this knowledge base article](/docs/linux-and-unix-agentless-scanning-requirements).
- Name: custom name you can assign to the credential.
- Login: your login.
- Passphrase: your passphrase, if there is one.
- Private SSH key: your SSH key. Sample inputs can be seen in the info pop-up when hovering over the question mark icon.
- Sudo Password: your sudo password.

### vCenter credentials (added in Lansweeper 7.0)

![creating-and-mapping-scanning-credentials-10.jpg](/docs/.document360/assets/article_180/image_017.jpg)

- Used for scanning: vCenter servers.
- Must have: read-only access to your vCenter servers. Info on how to set this up can be found in [this knowledge base article](/docs/vcenter-scanning-requirements).
- Name: custom name you can assign to the credential.
- Login: your vCenter login.
- Password: your vCenter login's password.

### VMware credentials

![creating-and-mapping-scanning-credentials-11.jpg](/docs/.document360/assets/article_180/image_018.jpg)

- Used for scanning: VMware servers.
- Must have: read-only access to your ESXi servers.
- Name: custom name you can assign to the credential.
- Login: your VMware login.
- Password: your VMware login's password.

### Windows credentials

![creating-and-mapping-scanning-credentials-12.jpg](/docs/.document360/assets/article_180/image_019.jpg)

![creating-and-mapping-scanning-credentials-13.jpg](/docs/.document360/assets/article_180/image_020.jpg)

- Used for scanning: Windows computers and users.
- Must have: administrative permissions on your computers and, for scanning domain computers and users, read-only access to Active Directory. A domain admin can be used to scan a domain, but has more permissions than required. More info on Windows domain scanning requirements can be found in [this knowledge base article](/docs/windows-domain-scanning-requirements) and more info on Windows workgroup scanning requirements can be found in [this knowledge base article](/docs/windows-workgroup-scanning-requirements).
- Name: custom name you can assign to the credential.
- Login: a down-level logon name like NetBIOS domain name\username (domain credentials) or a user principal name (UPN) like username@yourdomain.local (domain credentials) or .\username (local credentials) or username@outlook.com (Microsoft accounts).
- Password: your user account's password.

## Mapping scanning credentials

To map a credential, click the **Map Credential** button in the **Scanning > Scanning Credentials** section of the web console. You can select multiple credentials at once.   
Credentials are tried in the order you see them. In the example below, Lansweeper will first try the Window domain credential and then the local credential. You can change the order in which credentials are tried by grabbing (left-click and hold) a credential in the **Credentials** column and dragging it to a new position.

![creating-and-mapping-scanning-credentials-14.jpg](/docs/.document360/assets/article_180/image_021.jpg)

The only credentials that don't need to be mapped are global credentials. Global credentials are tried for any asset of the specified type, if all other credentials of the same type have failed. Your global Windows credential is tried for any Windows computer for instance, if all other credentials mapped to the computer have failed.

Lansweeper also remembers which credential it last successfully scanned an asset with. When the asset is rescanned, the last successful credential is tried first. If that fails, any mapped credentials are tried. If those fail as well, your global credentials are tried.

### An AWS region

![creating-and-mapping-scanning-credentials-15.jpg](/docs/.document360/assets/article_180/image_022.jpg)

Select an AWS region from the dropdown. Additional regions can be submitted by selecting the **Add Scanning Target** button in the **Scanning > Scanning Targets** section of the web console and selecting AWS Region from the Scanning Type dropdown.

### An Azure subscription ID

![creating-and-mapping-scanning-credentials-16.jpg](/docs/.document360/assets/article_180/image_023.jpg)

Select an Azure subscription ID from the dropdown. Additional subscription IDs can be submitted by selecting the **Add Scanning Target** button in the **Scanning > Scanning Targets** section of the web console and selecting Azure from the Scanning Type dropdown.

### An IP address

![creating-and-mapping-scanning-credentials-17.jpg](/docs/.document360/assets/article_180/image_024.jpg)

### An IP range

![creating-and-mapping-scanning-credentials-18.jpg](/docs/.document360/assets/article_180/image_025.jpg)

Select a range from the dropdown. Additional ranges can be submitted by selecting the **Add Scanning Target** button in the **Scanning > Scanning Targets** section of the web console and selecting IP Range from the Scanning Type dropdown.

### An individual Windows computer

![creating-and-mapping-scanning-credentials-19.jpg](/docs/.document360/assets/article_180/image_026.jpg)

Domain\Computername: `NetBIOS domain name\NetBIOS computer name` or `workgroup name\NetBIOS computer name`.

### A domain or workgroup

![creating-and-mapping-scanning-credentials-20.jpg](/docs/.document360/assets/article_180/image_027.jpg)

Domain or Workgroup: NetBIOS name of the domain or name of the workgroup
