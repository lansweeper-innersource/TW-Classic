<!-- # Credential and Network Discovery Hub security -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_349/image_001.jpg) **This page explains the security measures built into Lansweeper to protect user data and credentials.**

This page is for Lansweeper Sites. For Lansweeper On-prem, see [Credential and database security](/docs/credential-and-database-security-in-lansweeper).

The security and confidentiality of credentials and discovered data are of critical importance in developing the Lansweeper software. Passwords of credentials submitted in Lansweeper are always encrypted both in transit and at rest.

This article highlights some of the measures built into Lansweeper to protect your data and credentials, and to eliminate security risks.

- [Security of submitted discovery and other credentials](#credentials)
- [Security of the Network Discovery Hub UI](#hub)
- [Permissions on installation folders](#installation)

## Security of submitted discovery and other credentials

Certain tasks performed by Lansweeper require you to submit credentials. To remotely discover Windows computers for instance, username/password combinations with administrative rights on the computers must be provided. Remote discovery of other types of assets also require credentials, with varying degrees of access rights. For more information on discovery credentials, check out [Configure Network Discovery](/docs/configure-network-discovery#credential).

The passwords of submitted credentials are always encrypted prior to being saved to the vault in your Network Discovery Hub. Once submitted, the passwords are no longer visible in plain text your Lansweeper Site or Network Discovery Hub.   
In a Lansweeper Site with multiple Network Discovery Hubs, you can share a credential between the vaults of multiple Hubs, while still keeping the shared credentials encrypted both in transit and at rest.

## Security of the Network Discovery Hub UI

To ensure that whoever will be managing your Lansweeper Network Discovery installation can troubleshoot possible issues, the Hub requests a custom password to be set during its first session. This password can be reset by following the steps detailed over at [Network Discovery: Frequently Asked Questions](/docs/network-discovery-frequently-asked-questions#q7).

## Permissions on installation folders

When you install Lansweeper Network Discovery, all files are copied to default locations. For more information on the default locations, check out [Install Network Discovery](/docs/install-network-discovery#pathsandlogs). The default permissions on the subfolders located in the installation folder have been made more restrictive where possible, so only necessary users and processes have access.
