<!-- # Add managers to an SSO connection -->
The person who [set up SSO](/docs/set-up-lansweeper-sso) for one or more domains in Cloud is by default the owner of that SSO connection. An SSO connection has at least one owner. Optionally, you can add more Cloud SSO managers. Having multiple managers is ideal for redundancy and security purposes, so you are not dependent on a single person to manage the SSO configuration.

An SSO connection can have up to 10 managers and there are two possible manager roles:

- **Admin:** An admin can edit the settings of the SSO connection, e.g. can add domains to the connection.
- **Owner:** An owner can edit the settings of the SSO connection, e.g. can add domains to the connection. In addition, an owner can manage other owners and admins. An owner can add or remove other owners and admins and can change a user's manager role.

Every SSO connection must have at least one owner. If you are the only owner of a connection, you cannot leave it. As an owner, you cannot change your own manager role either; only another owner can change your role.

To add managers:

1. Go to the **Settings** module.
2. Choose the **Single Sign-On** menu and select **Add new managers** next to the relevant SSO connection.  
   
3. In the resulting pop-up, submit the email address(es) of the user(s) you want to invite as manager(s), and select the users' desired role, **Admin**or **Owner**.
4. Once you've confirmed, the selected users will receive an email about their new manager role. Users you wish to invite as manager or owner must have already created their own user account in Cloud.

To remove a previously added manager or to change their role, hover over the manager's user icon within the SSO connection and click one of the available buttons.  

