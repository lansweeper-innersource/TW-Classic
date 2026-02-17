<!-- # Web console user roles and permissions -->
This page is for Lansweeper Classic. For Lansweeper Sites (in the cloud), see [Configure scopes, permissions, and roles](/docs/configure-scopes-permissions-and-roles).

By default, everyone in your network can access all of Lansweeper's features and menus simply by browsing to the web console URL and selecting **Built-in Admin**. However, you can restrict access to the console and configure what users can see or do once they've been granted access.

To do this, you can assign a built-in or custom user role (a set of permissions) to user groups or individual user accounts. A user's role determines what the user can see or do within the console.

There are built-in roles, which you can modify with the pencil shaped edit buttons, but you can create your own as well. Roles are configured in the **User Roles** section of the **Configuration > User Access & Roles**menu.  


This article simply lists the built-in roles, the permissions that can be included in a role and the rights these permissions provide. For a complete guide on how to restrict web console access, please review [this knowledge base article](/docs/restrict-access-to-the-web-console).

User permissions are cached. If you make changes to a user's permissions, have that user log out of Lansweeper and back in to see the changes take effect. A logout can be achieved by restarting the web browser.

## Built-in user roles

The user roles below are included in Lansweeper by default, but you can modify them and create your own as well. To see a complete list of permissions included in each role, select the pencil shaped edit button next to a role.



- **Administrator**: gives users full access to the asset management portion of Lansweeper.
- **Administrator + Agent**: gives users full access to the asset management portion of Lansweeper and nearly full access to help desk tickets in their own teams, except for the ability to edit other agents' notes, delete tickets or delete ticket attachments.
- **Agent 1st line**: allows agents to perform a limited number of operations on help desk tickets in their own teams.
- **Agent 2nd line**: allows agents to perform a limited number of operations on help desk tickets in their own teams, less limited than the 1st line role.
- **Asset manager**: gives users nearly full access to the asset management portion of Lansweeper, except for the ability to view help desk reports and access items in the Configuration menu.
- **Asset manager + Agent**: gives users nearly full access to the asset management portion of Lansweeper and nearly full access to help desk tickets in their own teams, except for the ability to edit other agents' notes, delete tickets or delete ticket attachments.
- **View assets**: gives users read-only access to assets.
- **View assets + Agent 1st line**: gives users read-only access to assets and allows them to perform a limited number of operations on help desk tickets in their own teams.
- **View assets + Agent 2nd line**: gives users read-only access to assets and allows them to perform a limited number of operations on help desk tickets in their own teams.

## Asset management permissions

When configuring a new role or using the pencil shaped edit button next to an existing role, the first set of permissions in the pop-up relates mostly to the asset management portion of Lansweeper.

Below is a list of available asset management and other general permissions.

- **Access Asset Management**: gives users read-only access to all assets in the Lansweeper database. This includes both scanned and manually added assets.
- **Access Scanning Targets**: allows users to view and modify submitted network segments and other settings under **Scanning > Scanning Targets**.  
  
- **Access Scanning Credentials**: allows users to [modify and map scanning credentials](/docs/create-and-map-scanning-credentials) under **Scanning > Scanning Credentials**.  
  
- **Access Data Selection**: allows users to access the **Data Selection** section of the **Scanning** menu. These menus allow you to configure [file scanning](/docs/windows-custom-file-scanning), [registry scanning](/docs/scan-registry-values-with-custom-registry-scanning), [item intervals](/docs/manage-scanned-item-intervals), [custom OID scanning](/docs/scan-extra-snmp-data-with-custom-oid-scanning) and [performance scanning](/docs/how-to-scan-performance-information-of-windows-and-linux-computers). Item intervals control how often specific data is scanned for Windows computers and whether a change history of this data is kept.  
  
- **Edit Asset Data**: allows users to make manual changes to asset data. Changes can be made for instance by selecting **Edit asset** on individual asset pages or by clicking the **Assets** link at the top of the web console and using one of the edit buttons on the left.
- **View And Use Basic Actions**: allows users to view and run Basic asset and user actions. Which actions are considered Basic actions can be configured in the web console under **Configuration > Asset Pages** and **Configuration > User Pages**.  
  
- **View And Use Advanced Actions**: allows users to view and run Advanced asset and user actions. Which actions are considered Advanced actions can be configured in the web console under **Configuration > Asset Pages** and **Configuration > User Pages**..
- **Wake On Lan**: allows users to perform a Wake-on-LAN (WOL) of one or more assets at once. Keep in mind that a WOL of a computer only works if WOL capabilities are enabled in the computer's network card settings and BIOS.  
  
- **Rescan Assets**: allows users to rescan assets with the **Rescan** and **Rescan Asset** buttons found throughout the web console, e.g. on individual asset pages and in asset overviews.  
  
- **Add Asset Comments**: allows users to [add comments to assets](/docs/add-comments-to-assets) by selecting **Add comment** in the **Comments** tab of individual asset pages.  
  
- **Add Asset Docs**: allows users to [add documents to assets](/docs/add-documents-to-assets) by selecting **Add document** in the **Docs** tab of individual asset pages.  
  
- **View License Keys**: allows users to view scanned license keys of Windows computers, e.g. on individual computer webpages, in reports and under **Software > Scanned License Keys**.  
  
- **Edit License Key Settings**: allows users to change license key scanning settings for Windows computers under **Software > License Key Settings**.  
  
- **View License Compliance**: allows users to view license compliance reports in the **Software** menu of the web console.  
  
- **Edit License Compliance**: allows users to configure the license compliance modules in the **Software** menu of the web console.  
  
- **Edit Reports**: allows users to create and modify reports in the **Reports** menu of the web console.
- **View Reports Containing Helpdesk Tables**: allows users to see the results of reports in the **Reports** menu that contain helpdesk database tables. Helpdesk tables start with "htbl...", e.g. "htblticket". Keep in mind that this permission allows users to see all tickets that meet the report criteria, even tickets that they would otherwise not be authorized to view in ticket filters.
- **Share Dashboard Tabs**: allows users to [share dashboard tabs with other users](/docs/share-dashboard-tabs-with-other-users) and to change the contents of shared dashboard tabs.  
  
- **Access Deployment**: allows users to create, modify and delete deployment packages in the **Deployment** menu, to schedule deployments and to run deployment packages with the **Deploy Package** buttons found throughout the web console.  
  
- **Access Configuration**: allows users to access the items in the **Configuration** menu of the web console, the **Software > Authorization** menu and the **Software > Anti-Virus Settings** menu. Keep in mind that users with this permission can change their own user role to add additional permissions.
- **View Database Tables**: allows users to access the **Configuration > Database Tables** menu, which lists information on the Lansweeper database like table names and sizes.  
  
- **LsAgent Configuration**: allows users to access the **LsAgent** section of the **Scanning** menu. These menus allow you to configure [LsAgent](/docs/introduction-to-lsagent-for-windows-linux-and-mac) settings like groups, schedules, relay access etc. The permission also allows users to access the **LsAgent Assets** section of the **Assets** menu.
- **Access Uptime Information**: allows users to view scanned uptime events of Windows computers, both in the **Uptime** tab of individual computer webpages and in reports.
- **Access BitLocker Recovery Keys**: allows users to view BitLocker recovery keys scanned from Active Directory for Windows computers. These keys can be viewed in the **Config > Windows > BitLocker encryption > Recovery keys** tab of individual computer webpages and in reports.

## Helpdesk permissions (agents only)

When configuring a new role or using the pencil shaped edit button next to an existing role, the second set of permissions in the pop-up relates to the helpdesk portion of Lansweeper.

Below is a list of available help desk permissions. Unless stated otherwise, the actions referenced can be performed through the **Actions** menu in individual tickets and ticket overviews, or through the **Edit** button in individual tickets.

Keep in mind that an agent license is required to perform agent related tasks. Granting someone agent permissions has no effect if that user is not assigned an agent license by ticking the Active checkbox next to his account under Configuration\User Access & Roles.

Many of the permissions below control what operations an agent can perform on a ticket. Which tickets an agent can actually see in ticket filters largely depends on the teams the agent is in. More specifically, an agent can see the following tickets in ticket filters:   

- Tickets assigned to a team they're a member of.
- Tickets with a ticket type that's linked to a team they're a member of.
- Tickets assigned to them.
- Tickets they're subscribed to.
- Tickets they've created.
- Tickets they're a CC user of.

- **Assign To Self**: allows agents to assign tickets to themselves, e.g. with the **Pick up** button in individual tickets and ticket filters.
- **Edit User Notes**: allows agents to use the pencil shaped edit button in the upper right corner of user notes to modify their contents.
- **Edit Other Agent's Notes**: allows agents to use the pencil shaped edit button in the upper right corner of other agents' notes to modify their contents. Keep in mind that you don't need this permission to edit your own notes as an agent. An agent can already edit his own notes by default.
- **Create Internal Notes**: allows agents to add internal notes to tickets. Internal notes are only visible to other agents, not to regular users.
- **Create Public Notes**: allows agents to add public replies to tickets. Public replies are visible to both agents and users.
- **Alter Knowledgebase Articles**: allows agents to create, modify and delete knowledge base articles in the **Knowledgebase** menu.
- **Access Calendar**: allows agents to view calendar events in the **Calendar** menu. Agents can view events they themselves have created and events they've specifically been granted access to by other agents. Agents that are team leaders can also view events created by their team members.
- **Alter Calendar Events**: allows agents to create, modify and delete calendar events they have access to in the **Calendar** menu. Agents have access to events they themselves have created and events they've specifically been granted access to by other agents. Agents that are team leaders also have access to events created by their team members.
- **Edit Templates**: allows agents to create, modify and delete ticket templates. The template configuration menu can be accessed by hitting the **Templates** button in the upper right corner of the note editor when writing a note in any ticket.
- **Perform Ticket Actions**: allows agents to see and use the **Actions** menu in individual tickets and ticket overviews, as well as the **Edit** button in individual tickets. If agents are not granted additional sub-permissions, they will only be able to link assets to tickets, generate ticket print previews and fill in ticket custom fields through these menus.
- **Alter State**: allows agents to change the state of unassigned tickets and tickets assigned to them.
- **Alter Other Agent's Ticket State**: allows agents to change the state of all tickets they have access to, even tickets that are assigned to other agents.
- **Alter Priority**: allows agents to change the ticket priority of tickets.
- **Alter Type**: allows agents to change the ticket type of tickets.
- **Alter Teams**: allows agents to change the assigned team of tickets. Keep in mind that agents that are team leaders can change the assigned team of tickets even without being granted the Alter Teams permission.
- **Alter SLA**: allows agents to change the applied SLA (service-level agreement) of tickets. Keep in mind that agents that are team leaders can change the applied SLA of tickets even without being granted the Alter SLA permission.
- **Merge Tickets**: allows agents to combine two tickets into one. The ticket chosen as parent will chronologically be listed as the oldest once the tickets are combined.
- **Alter User**: allows agents to see and use the **Actions > Users** menu options. These allow agents to change the user of a ticket, i.e. the user who supposedly submitted the ticket. They also allows agents to edit user details like username and to add or remove CC users.
- **Assign Tickets To Other Agents / Unassign Other Agents**: allows agents to assign tickets to other agents, reassign them and unassign them.
- **Alter Follow Up**: allows agents to add follow-ups to tickets and to edit or remove follow-ups of existing tickets. Ticket filters can be used to list tickets with a follow-up that's due.
- **Alter Subscribers**: allows agents to add other agents as subscribers to tickets, as well as to remove subscribed agents through a ticket's Subscribed tab.
- **Duplicate Ticket**: allows agents to quickly create a new ticket based on an existing one, with the same ticket properties (user, type, state, priority...) and initial note as the original ticket.
- **Ignore Tickets**: allows agents to mark tickets as ignored. Ignored tickets are not deleted from your database, but excluded from most ticket overviews, text searches and help desk widgets. Ignored tickets can still be viewed by searching for their specific ticket ID or creating a ticket filter with the Ignored Tickets option checked.
- **Set Personal**: allows agents to set tickets to personal. If a ticket is set to personal, the agent's name is displayed in any public agent replies sent via email to the user of the ticket. Personal tickets can be identified in the web console by the speech bubble icons accompanying their notes.
- **Delete Tickets**: allows agents to [delete tickets from the database](/docs/delete-tickets-from-the-helpdesk). Keep in mind that deleted tickets can only be recovered through [a database restore](/docs/restore-your-installation-from-a-backup).
- **Edit Ticket Description / Subject**: allows agents to use the pencil shaped edit button in the upper right corner of a ticket's initial note to modify this note and the ticket subject.
- **Delete Attachments**: allows agents to remove attachments from tickets with the delete buttons next to each attachment.

## Helpdesk agent access permission

- **Allow full access to all tickets regardless of team or type**: allows agents to see all tickets in the database, regardless of which teams these tickets are assigned to. To perform actions on these tickets, the agents do still require the appropriate help desk permissions listed earlier on in this article.
