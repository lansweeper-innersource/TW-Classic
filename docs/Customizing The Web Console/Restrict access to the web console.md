<!-- # Restrict access to the web console -->
When you install Lansweeper Classic and access the web console for the first time, you are presented with a First Run Wizard, which allows you to set up scanning and configure some basic options. Any subsequent times you access the console, you are presented with a login screen.

By default, everyone in your network can access all of Lansweeper's features and menus simply by browsing to the web console URL and selecting **Built-in Admin**. However, you can restrict access to the console and configure what users can see or do once they've been granted access.

You can assign a built-in or custom user role, a set of permissions, to user groups or individual user accounts. A user's role determines what the user can see or do within the console.

Should you accidentally lock yourself out of certain parts of the web console or the web console entirely, follow the instructions in [this knowledge base article](/docs/locked-out-of-the-web-console) to regain access.

  To restrict access to the web console:

1. Browse to the **Configuration > Website Settings**section of the web console.  
   
2. Select **Edit** in the **Website access** section of the page.
3. In the resulting pop-up, submit one or more Active Directory user groups. The pop-up will automatically try to compile a list of groups in your domain to choose from, but you can also manually submit a group with the format NetBIOS domain name\group name. Access to the Lansweeper web console will be restricted to the users in the groups you've specified. These users will also have the basic ability to access the help desk portion of Lansweeper to submit their own tickets.  

   These users will not be able to respond to tickets or see any other portion of Lansweeper without being granted additional permissions further down this article. If you do not want to restrict who can submit their own help desk tickets, do not submit any groups under Website Access.

   
4. Browse to the **Configuration > User Access & Roles**section of the web console.  
   
5. Select **Add Role** in the **User Roles** section of the page to create your own user role, i.e. set of permissions. You can assign this role to user groups or individual user accounts afterwards.   
   Instead of creating your own role, you can also make use of the built-in roles, which are listed below. [This article](/docs/web-console-user-roles-and-permissions) explains what each of the available permissions in a role gives the user access to.
   - Administrator : full access to asset management
   - Administrator + Agent : full access to asset management and nearly full access to help desk tickets in own teams, except for the ability to edit other agents' notes, delete tickets or delete ticket attachments
   - Agent 1st line: limited access to help desk tickets in own teams
   - Agent 2nd line: limited access to help desk tickets in own teams, less limited than the 1st line role
   - Asset manager: nearly full access to asset management, except for the ability to view help desk reports or run database scripts
   - Asset manager + Agent: nearly full access to asset management and nearly full access to help desk tickets in own teams, except for the ability to edit other agents' notes, delete tickets or delete ticket attachments
   - View assets: read-only access to assets
   - View assets + agent 1st line: read-only access to assets and limited access to help desk tickets in own teams
   - View assets + agent 2nd line: read-only access to assets and limited access to help desk tickets in own teams  
     
6. If necessary, select **Add Local User** or **Add AD User** in the **Users** section of the page to add a Windows user account to the page, so you can give the user a role. By default, the page lists all users that have logged into the web console, but you can manually add additional users as well.   

   Keep in mind that the AD pop-up only lists Active Directory users that have been scanned by Lansweeper. Take a look at [how you can scan AD users.](/docs/how-to-scan-users)
7. Assign a built-in or the custom user role you created earlier to one or more user accounts in the **Users** section of the page.  
   Alternatively, assign the role to one or more Active Directory user groups in the **User Roles** section of the page. The group pop-up will automatically try to compile a list of groups in your domain to choose from, but you can also manually submit a group with the format NetBIOS domain name\group name. It is recommended that you give at least one user or group full access to Lansweeper by assigning the Administrator + Agent role or a custom role that includes all permissions.  
   
8. If the user needs to be able to respond to help desk tickets, select **Make Agent** next to the user in the **Users** section of the page. You will be asked to add the user to one or more agent teams and, optionally, make the user team leader of those teams. Users can only be made agents if they have an associated Windows account, i.e. if there is an account listed in the Username column.  
     

   An agent can see the following tickets in ticket filters:   
   - Tickets assigned to a team they're a member of.
   - Tickets with a ticket type that's linked to a team they're a member of.
   - Tickets assigned to them.
   - Tickets they're subscribed to.
   - Tickets they've created.
   - Tickets they're a CC user of.

   A team leader can do some extra things with tickets, without being given specific permissions for this. A team leader can:   
   - Change the SLAs of tickets assigned to their team.
   - Change the team of tickets assigned to their team.
   - See and edit calendar events created by members of their team.
9. Log out of the web console and then back in with your Windows user account by restarting your web browser. Verify that you have access to all Lansweeper features and menus that you need access to.  
   
10. Uncheck **Allow built-in admin** in the **Configuration > Website Settings** section of the web console to disable the Built-in Admin button in the login screen. Users will now only be able to log into the web console with their Windows user account and will only have access to the Lansweeper features and menus included in their user role.  
    
11. You've now restricted access to the web console. Optionally, disable the login screen and have your browser automatically log you in with your current Windows user account.   
    To do this, you first need to enable authentication in your web server settings. We have configuration instructions for [IIS Express](/docs/enable-authentication-in-iis-express) and [IIS](/docs/enable-authentication-in-iis). If you're unsure which web server is hosting your console, have a look at the **WebServer** section of the **Configuration > Website Settings** section of the console.   
    Once you've enabled authentication in your web server settings, your browser will either prompt you for credentials or automatically log you in with your current Windows user account. This depends on your browser configuration. We have instructions for [enabling or disabling login prompts](/docs/manage-web-browser-login-prompts) in specific browsers.
