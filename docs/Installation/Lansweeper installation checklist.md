<!-- # Lansweeper installation checklist -->
The below checklist can be used to prepare a Lansweeper installation, from a simple Easy install to a distributed setup with multiple scan servers. Being prepared ensures a smooth installation process, as well as efficient scanning of your network after installation. This checklist includes the following sections:

1. [Pre-install recommendations](#heading1)
2. [Installing Lansweeper](#heading2)
3. [Post-install recommendations](#heading3)

## 1. Pre-install recommendations

| Description | | More information |
| --- | --- | --- |
| 1.1 | Find the right Lansweeper setup for you:  - Which database server - Which web server - Distributed or not - How many scan servers - How many installations | [Which Lansweeper setup is right for you?](/docs/which-lansweeper-setup-is-right-for-you) |
| 1.2 | Review Lansweeper installation requirements | [Lansweeper installation requirements](/docs/lansweeper-installation-requirements) |
| 1.3 | Select or set up machine(s) to install Lansweeper on |  |
| 1.4 | If selecting Microsoft SQL Server as your database server, either:  - Download and install SQL Server, making sure to keep Lansweeper requirements in mind. Know the password of at least one sysadmin account in the SQL instance, as you'll require this for the Lansweeper installation process. - Configure your existing SQL Server instance, if you have one, according to Lansweeper requirements. Know the password of at least one sysadmin account in the SQL instance, as you'll require this for the Lansweeper installation process. | [Configuring a SQL Server instance to host the Lansweeper database](/docs/configuring-a-sql-server-instance-to-host-the-lansweeper-database) |
| 1.5 | If selecting IIS as your web server and IIS is not already installed on your machine, install it | [Install IIS (Internet Information Services)](/docs/install-iis-internet-information-services) |
| 1.6 | If performing a distributed Lansweeper installation, make sure required firewall ports are open between machines, so scan server(s) and web console can communicate with the database | [Ports scanned or used by Lansweeper](/docs/ports-scanned-or-used-by-lansweeper) |
| 1.7 | If intending to access the Lansweeper web console from machines other than the web server, make sure the website ports you intend to use are open between machines |  |
| 1.8 | If intending to use Lansweeper features that require internet access, make sure your Lansweeper server can access the internet | [Lansweeper features that access the internet](/docs/lansweeper-features-that-access-the-internet) |
| 1.9 | If intending to scan computers or other assets without a scanning agent, make sure:  - Firewalls are properly configured to allow for this - You create a user account with the required permissions for scanning | [Ports scanned or used by Lansweeper](/docs/ports-scanned-or-used-by-lansweeper)  [Overview of scanning targets and methods](/docs/overview-of-scanning-targets-and-methods)  [Creating and mapping scanning credentials](/docs/create-and-map-scanning-credentials) |
| 1.10 | Make sure your DNS servers are up-to-date, so your Lansweeper scan servers properly resolve client machine names |  |

## Installing Lansweeper

### 2a. Installing Lansweeper Cloud

| Description | | More information |
| --- | --- | --- |
| 2.1 | Start your free trial and download Lansweeper Cloud | [Start your free trial](https://app.lansweeper.com/try/) |
| 2.2 | Download the latest Lansweeper Cloud installer | [Download Lansweeper Cloud](https://www.lansweeper.com/download/) |
| 2.3 | Install the Lansweeper Cloud-first trial | [Install the Lansweeper Cloud-first trial](/docs/install-the-lansweeper-trial "Install Lansweeper in trial mode") |

### 2b. Installing Lansweeper Classic

| Description | | More information |
| --- | --- | --- |
| 2.1 | Grab your Lansweeper Classic license key, either:  - A trial key, if you haven't purchased a license yet - The license key you purchased |  |
| 2.2 | Download the latest Lansweeper Classic installer | [Download Lansweeper Classic](https://www.lansweeper.com/download/) |
| 2.3 | If intending to scan Windows, Linux or Mac computers with the LsAgent scanning agent, download the LsAgent installer(s) | [Download LsAgent](https://www.lansweeper.com/download/lsagent/) |
| 2.4 | Install Lansweeper according to your needs and specifications | [Perform an Easy Install](/docs/install-lansweeper-on-prem#heading1 "Performing an Easy Install")  [Perform an Advanced Install](/docs/install-lansweeper-on-prem#heading2 "Advanced Lansweeper installation") |
| 2.5 | Complete the First Run Wizard presented in the web console, which sets up an initial scanning configuration | [Configure the First Run Wizard](/docs/install-lansweeper-on-prem#FRW) |

## 3. Post-install recommendations

Once you've completed your Lansweeper installation, you may want to configure some other important settings and processes. Below, the essential ones are mentioned.

| Description | | More information |
| --- | --- | --- |
| 3.1 | Configure the web console date format and first day of the week | [Set the date format](/docs/set-the-date-format) |
| 3.2 | Add additional scanning targets and credentials to scan your network, if necessary | [Overview of scanning targets and methods](/docs/overview-of-scanning-targets-and-methods)  [Creating and mapping scanning credentials](/docs/create-and-map-scanning-credentials) |
| 3.3 | Install LsAgent on your client machines, if intending to scan with LsAgent | [Install LsAgent on a Windows computer](/docs/install-lsagent-on-a-windows-computer)  [Install LsAgent on a Linux computer](/docs/install-lsagent-on-a-linux-computer)  [Install LsAgent on a Mac computer](/docs/install-lsagent-on-a-mac-computer)  [Silently installing LsAgent on Windows, Linux or Mac](/docs/silently-installing-lsagent-on-a-windows-linux-or-mac-computer) |
| 3.4 | For security reasons, set up a custom SSL certificate in the web console | [Configure SSL in IIS Express](/docs/configure-ssl-in-iis-express)  [Configure SSL in IIS](/docs/configure-ssl-in-iis) |
| 3.5 | Give more users access to the web console, if desired | [Restrict access to the web console](/docs/restrict-access-to-the-web-console) |
| 3.6 | For security reasons, disable the built-in admin account for logging into the web console | [Manage the built-in admin account](/docs/managing-the-built-in-admin-account) |
| 3.7 | Configure automated cleanups of the Lansweeper database | [Perform automated database cleanups](/docs/perform-automated-database-cleanups) |
| 3.8 | Familiarize yourself with the Lansweeper backup procedure, so you can get a backup schedule in place | [Back up your installation](/docs/back-up-your-installation) |
| 3.9 | Familiarize yourself with the Lansweeper update procedure, so you can get an update schedule in place | [Update Lansweeper Classic](/docs/update-lansweeper-on-premises)  [Update your Lansweeper scan server](/docs/update-your-lansweeper-sites-scan-server) |
| 3.10 | Link your Lansweeper installation with Cloud | [Getting started with Lansweeper Cloud](https://www.lansweeper.com/resources/getting-started-with-cloud/) |
