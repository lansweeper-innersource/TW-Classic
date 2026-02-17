<!-- # Where are Lansweeper data, reports, and settings stored? -->
The Lansweeper software includes both an [IT asset management](https://www.lansweeper.com/it-asset-management/) system and helpdesk. Most of the data scanned by Lansweeper and manually submitted in the web console is stored in the Lansweeper database. Your database is hosted in either the Microsoft SQL LocalDB, Microsoft SQL Server or the deprecated Microsoft SQL Compact database server.

However, some things are stored outside of the database. Below is an overview of where scanned and user submitted data is stored. This information is relevant when backing up and restoring your Lansweeper installation.

The procedure for backing up your Lansweeper installation can be found in [this knowledge base article](/docs/back-up-your-installation), while the procedure for restoring a backup can be found in [this article](/docs/restore-your-installation-from-a-backup).

## Stored in the Lansweeper database

- Scanned and manually submitted asset data
- Indexes used by the asset search bar
- Deployment package steps and settings, though files referenced by packages are stored outside of the database
- Ticket note text, knowledge base article text, calendar events and other helpdesk data. Helpdesk images and attached files are stored outside of the database, as explained further in this article.
- Built-in and custom reports
- Scanning, helpdesk and other settings. Scanning credentials are encrypted using an encryption file, making it impossible for anyone to decrypt them unless the Lansweeper server itself is already compromised. More information on credential security can be found in [this knowledge base article](/docs/credential-and-database-security-in-lansweeper).

## Asset management data stored in Lansweeper website folders

- Custom icons you may have added to asset or user actions  
  `Program Files (x86)\Lansweeper\Website\actions`
- Custom images you may have added to assets or location maps  
  `Program Files (x86)\Lansweeper\Website\assetpictures`
- Documents you may have added to assets or the license compliance modules  
  `Program Files (x86)\Lansweeper\Website\DOCS`
- Custom icons you may have added to asset types or asset relation types  
  `Program Files (x86)\Lansweeper\Website\images`
- Custom images you may have added to users  
  `Program Files (x86)\Lansweeper\Website\userpictures`
- Custom widgets you may have added to dashboards  
  `Program Files (x86)\Lansweeper\Website\WidgetsCustom`

## Helpdesk data stored in Lansweeper website folders

- Indexes used for knowledge base article and ticket search  
  `Program Files (x86)\Lansweeper\Website\App_Data`
- Custom login pop-up message you may have configured for the web console under **Configuration > Website Settings**`Program Files (x86)\Lansweeper\Website\customdata`
- Files and images attached to or embedded in tickets and knowledge base articles.  
  `Program Files (x86)\Lansweeper\Website\helpdesk\files`
- Custom icons you may have added to ticket types.  
  `Program Files (x86)\Lansweeper\Website\helpdesk\icons`
- Custom logo you may have added to the helpdesk under **Configuration > Look & Feel**`Program Files (x86)\Lansweeper\Website\helpdesk\logo`
- Custom translations you may have added to the helpdesk  
  `Program Files (x86)\Lansweeper\Website\lang`
- Custom widgets you may have added to dashboards  
  `Program Files (x86)\Lansweeper\Website\WidgetsCustom`

## Stored in other Lansweeper folders

- Custom scripts, executables and other files you may have added to asset or user actions  
  `Program Files (x86)\Lansweeper\Actions`
- The key used to encrypt and decrypt your scanning and other credentials, which is unique to each Lansweeper installation  
  `Program Files (x86)\Lansweeper\Key`
- Custom scripts, executables and other files you may have referenced in deployment packages.  
  `Program Files (x86)\Lansweeper\PackageShare`
- Report results you may have automatically had exported to files through Lansweeper's report alert feature.  
  `Program Files (x86)\Lansweeper\Service\export`
