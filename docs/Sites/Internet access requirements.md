<!-- # Internet access requirements -->
This article is for Lansweeper Sites. For Lansweeper On-premises, go to [Lansweeper features that access the internet](/docs/lansweeper-features-that-access-the-internet "/docs/lansweeper-features-that-access-the-internet").

![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_374/image_001.jpg) **This page provides an overview of the features in Lansweeper Sites that require internet access.**

Lansweeper Sites requires access to the internet to function properly.

All of the URLs for the Lansweeper Sites sync server are required. However, the scanning URLs are only required if you use that particular scanning method.

| **Category** | **Item** | **URLs** |
| --- | --- | --- |
| Lansweeper Sites | [Sync server](/docs/cloud-requirement-sync-server-internet-access) | For a full list of URLs based on your region, see [Cloud requirement: sync server internet access](/docs/cloud-requirement-sync-server-internet-access). |
| Scanning | [AirWatch](/docs/scan-vmware-workspace-one-uem-powered-by-airwatch-targets) | https://<AirWatch server URL submitted by you>/API |
| [AWS](/docs/scan-an-aws-region "Scan an AWS region") | https://\*.amazonaws.com |
| Azure | https://management.azure.com/  https://management.core.windows.net/ |
| Azure AD | https://login.microsoftonline.com/  https://graph.microsoft.com/ |
| [Chrome OS](/docs/scan-chrome-os-targets) | https://accounts.google.com/  https://www.googleapis.com/  https://admin.googleapis.com/  https://oauth2.googleapis.com/ |
| [Intune V2](/docs/scan-intune-v2-targets) | https://login.microsoftonline.com/  https://graph.microsoft.com/ |
| Microsoft 365 | https://login.microsoftonline.com/  https://graph.microsoft.com/ |
| [Warranty](/docs/enable-warranty-tracking) | https://api.dell.com/support/assetinfo  https://apigtwb2c.us.dell.com/  https://support.ts.fujitsu.com/  https://support.hp.com/  https://support.hpe.com/  https://css.api.hp.com/  https://www-947.ibm.com/support/entry/  https://csp.lenovo.com/  https://pcsupport.lenovo.com/  https://support.dynabook.com/support/ |
