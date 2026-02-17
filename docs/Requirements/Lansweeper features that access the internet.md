<!-- # Lansweeper features that access the internet -->

Lansweeper has several optional features that require internet access to function properly.

This information can help you correctly configure your firewalls and proxy servers for proper Lansweeper functioning. Most of the below features are disabled by default. This article is divided into multiple categories:

- [Scanning](#heading1)
- [Mailing](#heading2)
- [Auto-update](#heading6)
- [Lansweeper Sites](#heading3)
- [Dashboard widgets](#heading4)
- [Miscellaneous other features](#heading5)

## Scanning

### AirWatch scanning

Lansweeper can [scan mobile devices that are enrolled in VMware AirWatch](/docs/scan-mobile-devices-through-vmware-workspace-one-uem-powered-by-airwatch). For AirWatch scanning, your scan server must be able to access the URL below and its sub-URLs.

- https://<AirWatch server URL submitted by you>/API

### AWS scanning

Lansweeper can [scan VPCs and instances (virtual machines) hosted on the AWS cloud platform](/docs/scan-an-aws-cloud-environment). For AWS scanning, your scan server must be able to access URLs ending in amazonaws.com and their sub-URLs.

- https://\*.amazonaws.com

### Azure scanning

Lansweeper can [scan resource groups and virtual machines hosted on the Microsoft Azure cloud computing platform](/docs/scan-an-azure-cloud-environment). For Azure scanning, your scan server must be able to access the URLs below and their sub-URLs.

- https://management.azure.com/
- https://management.core.windows.net/

### Azure AD scanning

Lansweeper can [scan Azure Active Directory (AAD) users and groups](/docs/scan-microsoft-entra-id-azure-ad-users-and-groups). For AAD scanning, your scan server must be able to access the URLs below and their sub-URLs.

- https://login.microsoftonline.com/
- https://graph.microsoft.com/

### Chrome OS scanning

Lansweeper can [scan Chrome OS devices](/docs/how-to-scan-chrome-os-machines) like Chromebooks. For Chrome OS scanning, your scan server must be able to access the URLs below and their sub-URLs.

- https://accounts.google.com/
- https://www.googleapis.com/
- https://admin.googleapis.com/
- https://oauth2.googleapis.com/

### Intune scanning

Lansweeper can [scan mobile devices enrolled in Microsoft Intune](/docs/scan-mobile-devices-through-microsoft-intune). For Intune scanning, your scan server must be able to access the URLs below and their sub-URLs.

- https://login.microsoftonline.com/
- https://graph.microsoft.com/

### Microsoft 365 scanning

Lansweeper can [scan Microsoft 365 environments](/docs/scan-microsoft-365-targets). For M365 scanning, your scan server must be able to access the URLs below and their sub-URLs.

- https://login.microsoftonline.com/
- https://graph.microsoft.com/

### Warranty scanning

Lansweeper can [scan warranty data from several manufacturers](/docs/set-up-automated-warranty-checks). For warranty scanning, your scan server must be able to access the URLs below and their sub-URLs.

- https://api.dell.com/support/assetinfo
- https://apigtwb2c.us.dell.com/
- https://support.ts.fujitsu.com/
- https://www-947.ibm.com/support/entry/
- https://csp.lenovo.com/
- https://pcsupport.lenovo.com/
- https://support.dynabook.com/support/
- <https://warranty.api.hp.com/>

### Extended display scanning

[Extended display scanning](/docs/extended-display-scanning) retrieves additional data for monitors attached to Windows computers. In order for extended display scanning to automatically retrieve the most up-to-date monitor data, your scan server must be able to access the URL below and its sub-URLs.

- https://discovery-gateway.lansweeper.com/

### Credential-free Device Recognition (CDR)

[Credential-free Device Recognition (CDR)](/docs/credential-free-device-recognition-cdr) enriches asset data by sending device fingerprints to a Lansweeper API. For CDR to work, your scan server must be able to access the URLs below and their sub-URLs.

- https://authentication.lansweeper.com/
- https://recognition.lansweeper.com/

### LsAgent relay

The LsAgent relay server allows you to [scan assets over the internet that have the LsAgent scanning agent installed](/docs/introduction-to-lsagent-for-windows-linux-and-mac). To link with the relay, your scan server must be able to access the URL below and its sub-URLs.

- https://lsagentrelay.lansweeper.com/

## Mailing

### Help desk mailing

Lansweeper includes [a help desk system](/docs/introduction-to-the-help-desk) where you can create and respond to tickets via email.

- The incoming mail server(s) of your help desk email account(s) are fully configurable by you. Which email servers are accessed depends on your submitted configuration.
- The outgoing mail server(s) of your help desk email account(s) are fully configurable by you. Which email servers are accessed depends on your submitted configuration.

### Email alerts

Lansweeper includes [an alert system](/docs/send-report-and-event-log-alerts) whereby you can have specific reports or event log entries sent to you via email.

- The outgoing mail server(s) used for email alerts are fully configurable by you. Which email servers are accessed depends on your submitted configuration.

## Auto-update

Auto‑updates ensure Lansweeper stays updated with the latest features, security patches, and performance improvements without manual intervention, reducing maintenance efforts, minimizing downtime, and keeping your system running smoothly.  
To enable auto‑updates, your scan server must be able to access the URLs below and their sub‑URLs:

- <https://discovery-gateway.lansweeper.com/versions>
- <https://download.lansweeper.com/>

## Lansweeper Sites

[Lansweeper Sites](/docs/introduction-to-lansweeper-sites) offers a new way for you to use and access Lansweeper, by using a centralized interface. To link with Sites, your Lansweeper installation must be able to access the URLs below and their sub-URLs.

- [edge.eu.lansweeper.com](https://edge.eu.lansweeper.com/ "https://edge.eu.lansweeper.com/")
- [edge.us.lansweeper.com](https://edge.us.lansweeper.com/ "https://edge.us.lansweeper.com/")
- [https://id.eu.lansweeper.com](https://id.eu.lansweeper.com/ "https://id.eu.lansweeper.com/")
- [https://id.us.lansweeper.com](https://id.us.lansweeper.com/ "https://id.us.lansweeper.com/")
- [https://app.lansweeper.com](https://app.lansweeper.com/ "https://app.lansweeper.com/")
- [https://eu.lansweeper.com](https://eu.lansweeper.com/ "https://eu.lansweeper.com/")
- [https://us.lansweeper.com](https://us.lansweeper.com/ "https://us.lansweeper.com/")
- [discovery-gateway.lansweeper.com](https://discovery-gateway.lansweeper.com/ "https://discovery-gateway.lansweeper.com/")
- [discovery-gateway.eu.lansweeper.com](https://discovery-gateway.eu.lansweeper.com/ "https://discovery-gateway.eu.lansweeper.com/")

## Dashboard widgets

### Lansweeper news widget

The dashboard of the local Lansweeper web console includes a Lansweeper news widget. For the widget to work, your web server must be able to access the URL below.

- https://www.lansweeper.com/blog-rss.aspx

### iFrame widget

The dashboard of the local Lansweeper web console includes an iFrame widget.

- Which websites are loaded in the iFrame widget and accessed by your web server depends on how you configured the widget.

### RSS reader widget

The dashboard of the local Lansweeper web console includes an RSS reader widget.

- Which feeds are loaded in the RSS reader widget and accessed by your web server depends on how you configured the widget.

## Miscellaneous other features

### Banner notifications

The local Lansweeper web console displays [banner notifications](/docs/lansweeper-metrics-and-notification-system) by default. To retrieve banner notifications, your web server must be able to access the URL below and its sub-URLs.

- https://lsservicecommunicatorprd.azurewebsites.net/

### Metrics

Your Lansweeper installation has [metrics](/docs/lansweeper-metrics-and-notification-system) enabled by default. The scan server sending metrics must be able to access the URL below and its sub-URLs.

- https://lsservicecommunicatorprd.azurewebsites.net/

### MIB Library

Your Lansweeper installation lets you access [the MIB Library](/docs/introduction-to-the-mib-importer-and-mib-library#heading11 "MIB Library"), where you can import MIB files for SNMP scanning. To search the MIB Library, your web server must be able to access the URL below and its sub-URLs.

- https://mibapiprd.lansweeper.com/
