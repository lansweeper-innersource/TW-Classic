<!-- # Credential and database security in Lansweeper -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_075/image_001.jpg) **This page explains the security measures built into Lansweeper to protect user data and credentials.**

This page is for Lansweeper On-prem. For Lansweeper Sites, see [Credential and Network Discovery Hub security](/docs/credential-and-network-discovery-hub-security).

The security and confidentiality of credentials and scanned data are of critical importance in developing the Lansweeper software. Passwords of credentials submitted in Lansweeper are always encrypted prior to being added to your Lansweeper database. The Lansweeper database is also password protected when hosted under Microsoft SQL LocalDB or Microsoft SQL Server. Databases hosted in the deprecated SQL Compact database server can only be accessed locally on the server and don't have a password.

This article highlights some of the measures built into Lansweeper to protect your data and credentials and to eliminate security risks. Topics discussed are:

- [Security of submitted scanning and other credentials](#heading1)
- [Security of the database and its connection string](#heading2)
- [Restrictions on running database scripts](#heading3)
- [Security of the web console](#heading4)
- [Permissions on installation folders](#heading5)

## Security of submitted scanning and other credentials

Certain tasks performed by Lansweeper require you to submit credentials. To remotely scan and deploy on Windows computers for instance, username/password combinations with administrative rights on the computers must be provided. Remote scans of other types of assets also require credentials, with varying degrees of access rights documented in [this knowledge base article](/docs/create-and-map-scanning-credentials). Lastly, credentials are also required to access servers used for help desk and alert mailing.

The passwords of submitted credentials are always encrypted prior to being added to your database, the same database that also stores scanned and other data. Once submitted, the passwords are no longer visible in plain text in the web console or database itself.

The screenshot below shows the encryption key generated for one specific Lansweeper installation. Lansweeper installations automatically use a unique key file for credential encryption. The encryption key can be found in `Program Files (x86)\Lansweeper\Key\Encryption.txt`.

![Credential Security 1.png](/docs/.document360/assets/article_075/image_002.jpg)

## Security of the database and its connection string

The Lansweeper software consists of [3 components](/docs/lansweeper-classic-components-and-architecture): database, scanning service and web console. If the database is hosted in the deprecated Microsoft SQL Compact database server, it can only be accessed by processes running locally on the server and has no password. If the database is hosted in SQL LocalDB or SQL Server, it does have a password.

SQL Server databases can also be accessed remotely from other servers in your network, if the necessary firewall and SQL Server configuration is performed and if the correct database password is provided. The database password is automatically randomized under SQL LocalDB and SQL Server to prevent unauthorized access.   
You can also specify your own password by following the instructions in [this knowledge base article](/docs/change-the-lansweeper-database-password).

The two configuration files below, found on the scanning server and web server respectively, tell the scanning service and web console which Lansweeper database to access.

`Program Files (x86)\Lansweeper\Service\Lansweeperservice.dll.config`

`Program Files (x86)\Lansweeper\Website\web.config`  

Starting from Lansweeper 11.1, Lansweeperservice.exe.config has been changed to Lansweeperservice.dll.config.

The database connection strings in these files are obfuscated, making it impossible for someone with access to these files to see where your database is hosted or what its password is.   
Connection string modifications must be made using the ConfigEditor tool documented in [this knowledge base article](/docs/how-to-use-the-configeditor-tool).

![advanced-credential-and-database-security-in-lansweeper-6-2.jpg](/docs/.document360/assets/article_075/image_003.jpg)

## Restrictions on running database scripts

For added security, executing database scripts from the web console has been made impossible. Scripts can now only be run from external tools like the **DatabaseMaintenance.exe** tool found at `Program Files (x86)\Lansweeper\Tools\DatabaseMaintenance.exe` on the Lansweeper server.

Tools like SQL Server Management Studio and SQL Compact Toolbox can also be used to run scripts, but connections to SQL LocalDB and SQL Server databases do of course require users to know and submit the database password.

![menu-databasemaintenance.jpg](/docs/.document360/assets/article_075/image_004.jpg)

## Security of the web console

To ensure that whoever will be managing your Lansweeper installation can access the configuration, the web console is by default accessible to anyone in your network that knows the correct URL. Web console access can easily be restricted to certain users or groups by following the instructions in [this knowledge base article](/docs/restrict-access-to-the-web-console).

Restricting access takes just a few minutes and allows you to specify not only who can log in, but also which specific tasks they can perform within the console. Applied web console permissions remain intact after subsequent Lansweeper updates.

![Security and credentials 1.png](/docs/.document360/assets/article_075/image_005.jpg)   
The **Built-in admin** button gives full rights to the console but can be removed. Who can log in with the available login boxes and what they can access can be restricted.

## Permissions on installation folders

When you install Lansweeper, most files used by the database, scanning service and web console are copied to `Program Files (x86)\Lansweeper` on your Lansweeper server. The default permissions on the subfolders located in the Lansweeper installation folder have been made more restrictive where possible, so only necessary users and processes have access.
