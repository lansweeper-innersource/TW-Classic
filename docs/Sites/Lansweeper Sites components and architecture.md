<!-- # Lansweeper Sites components and architecture -->

A local [Lansweeper](https://www.lansweeper.com/) installation can be [linked with a Site](/docs/link-lansweeper-on-prem-with-lansweeper-sites). Linking a local installation causes the installation's current data and any subsequent data changes to be sent to Lansweeper Sites. The Sites interface offers [a number of advantages](/docs/introduction-to-lansweeper-sites) over the local one: centralized access to multiple Lansweeper installations, more granular permissions over assets, a new report builder, a fully integrated API, and more.

## Lansweeper Sites installation components

To link a Lansweeper installation with a Site, you must first set up a full Lansweeper installation in your own network. You must install a Lansweeper database, web console and at least one scan server in your own network. Optionally, you can add secondary scan servers as well, though only one scan server will be responsible for syncing all of your installation's data with your Site.

### Local components

- **Database**: Your local database stores scanned and custom data, reports and settings. It can be hosted in SQL LocalDB or Microsoft SQL Server.
- **Scan server**: A scan server is a machine that has the Lansweeper Server service installed. This service is the beating heart of your Lansweeper installation. It scans data, runs deployments, performs database cleanups and sends emails. A scan server is in constant communication with the database to send data and retrieve settings. A Lansweeper installation has at least one scan server, but it can also have multiple.
- **Web console**: Your local web console displays data and settings stored in your database. It also allows you to make changes to them. The web console can be hosted in IIS Express or IIS. The console communicates with the database to retrieve data and send setting changes. Linking a Lansweeper installation with a Site starts from the **Configuration > Link With Cloud Site** menu of the local web console.

### Interaction with Lansweeper Sites

- **Sync server**: When you link a local Lansweeper installation with Sites, one scan server becomes the so-called "sync server". A sync server is a regular scan server, but one that is responsible for syncing all of the installation's data with Lansweeper Sites. If your installation only has one scan server, that server is automatically made the sync server. If your installation has multiple scan servers, you are asked to pick one as your sync server when you link with a Site. It doesn't matter which server you choose as long as that server meets [the requirements for linking with Lansweeper Sites](/docs/cloud-linking-requirements).
- **A Site**: A Site is a collection of one or more linked Lansweeper installations, which you give a specific name. You can create as many sites as you want in Lansweeper Sites. When you link a Lansweeper On-prem installation with Sites, you are asked to pick a site to link with. A Lansweeper On-prem installation can only be actively linked with 1 site at a time, but multiple installations can be linked with the same Site. The interface lets you select the site you want to view, by clicking the site icon in the upper left corner of the interface.

## Lansweeper Sites setup examples

### Basic network with a single subnet

If you have a simple network with a single subnet, consider setting up your Sites connection as shown in the diagram below.

- **Possible use case**: a single, small home or company network



### Larger network with multiple subnets

If you have a large network with multiple subnets, consider setting up your Lansweeper Sites connection as shown in the diagram below.

- **Possible use case**: a medium to large company network where locally all asset data is managed by a single team
- ****Advantages****:
  - Having one scan server per subnet, though not strictly required for scanning, improves asset detection and recognition.
  - Having one central, local database simplifies database backup, cleanup and other operations.
  - Only one scan server must be linked with a Site, so only one scan server must meet the Lansweeper Sites requirements.
  - Each scanned asset is only sent to Sites once, optimizing traffic and reducing the risk of duplicates.
  - In Lansweeper Sites, asset access can be managed using [scopes](/docs/configure-scopes-permissions-and-roles).
- ****Disadvantages:****
  - This setup only works if all scan servers can communicate with the local, central database.
  - In the local Lansweeper web console, any user with asset access can see all assets.



### Multiple isolated networks with one or more subnets, same company

If your company has multiple local, isolated networks that can't communicate with each other, consider setting up your Lansweeper Sites connections as shown in the diagram below.

- **Possible use case**: a large company network where locally asset data is managed by multiple teams
- ****Advantages****:
  - The local company networks don't need to be able to communicate with each other.
  - Each Lansweeper installation can locally only access its own data.
  - In Lansweeper Sites, asset access across the various installations can be managed using [scopes](/docs/configure-scopes-permissions-and-roles).
- ****Disadvantages****:
  - Each local Lansweeper installation must be linked with your Site, so each installation must meet the Lansweeper Sites requirements.
  - If multiple local installations do scan the same assets, these assets may be sent to Sites multiple times, generating unnecessary traffic and increasing the risk of [duplicates](/docs/asset-deduplication-in-cloud).



### Multiple isolated networks with one or more subnets, multiple companies

If you are managing data of multiple unrelated companies, consider setting up your Sites connections as shown in the diagram below.

- **Possible use case**: a Managed Service Provider (MSP) that manages data from multiple companies
- ****Advantages****:
  - Data from different companies can be completely separated using Sites. Each Site can represent one company.
  - Within each company site, asset access can be managed further using [scopes](/docs/configure-scopes-permissions-and-roles).
- ****Disadvantages****:
  - Reports cannot be run across multiple sites at once unless you have access to the multi-site management portal for MSPs.


