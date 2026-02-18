<!-- # Configure scopes, permissions, and roles -->
This page is for Lansweeper Sites. For Lansweeper On-prem, see [Web console user roles and permissions](/classic/docs/web-console-user-roles-and-permissions).

Lansweeper Sites allows you to granularly control which users have access and control over various features and assets in your site.

There are three components that allow you to manage access to your site:

- Scopes: Scopes, also called asset scopes, control which assets users can view in their inventory.
- Permissions: Permissions control the features that a user has access to in your site and the actions they can take.
- Roles: Roles are made up of scopes and permissions that you have assigned to that role.

Check out our YouTube video on [Access Management](https://www.youtube.com/watch?v=lZjfHT8sbqk) for more information.

On this page:

- Configure scopes
- Configure permissions and roles
- Create a new role
- Create and link an asset scope to a role
- Add a role to a user
- Priority

## Configure scopes

Scopes, or asset scopes, allow you to control which assets users can view in their Lansweeper Site Inventory. If no scopes are configured, users can see every asset within their inventory. By adding scopes, you restrict the assets users are able to view.

To configure scopes:

1. In your Lansweeper Site, go to **Configuration > Account management > Asset scopes > Add new asset scope**.
2. Enter a **Name** for your asset scope that represents your desired scope. Optionally, enter a description.
3. Under **Conditions**, select the option **Asset type**, **Asset domain**, **IP location**, or **Location**from the dropdown.
4. Select the expression **Equal to** or **Not equal** **to** from the dropdown.
5. Enter a value.
6. Optionally, select the plus symbol to add another condition. By default, **And** is applied. Select **And** to change the option to **Or**.
7. Select **Save and exit**.

Once your scope is created, you need to add it to a role in order to apply the scope to your desired users.

To view a list of your scopes, go to **Configuration > Account management > Asset scopes**.

## Configure permissions and roles

Roles are made up of permissions and scopes. Permissions control the features that a user has access to and the actions they can take. They are configured within a role. Roles are then added to an account or account group. If no roles and permissions are configured, users will not have access to any element of your Lansweeper Site. By adding permissions and roles to users, you grant users more access to your site.

By default, Lansweeper Sites includes the following roles:

- Administrator: All permissions are granted, except for those that are only granted to [site owners](/classic/docs/adding-owners-to-a-cloud-site), such as managing site settings and deleting a site.
- Analyze data: Permissions allow the user to view all the data available from a Lansweeper Site, create reports, and create dashboards without configuring asset information or details.
- Application admin: Permissions allow the user to access API and applications for your Lansweeper Site.
- Manage assets: Permissions allow the user to manage and configure assets, but not configure the site itself.
- View data: Permissions allow users to view data in Lansweeper Sites, with no configuration options.

All of the default roles can be edited as needed. You can view your roles by going to **Configuration > Account management > Roles & permissions**.

### Create a new role

1. Go to **Configuration > Account management > Roles and permissions**, and select **Add new role**.
2. Name your role and select **Create role**.
3. From the list of options, select which permissions you want to grant for the role.
4. Select the **Save role**icon.

### Create and link an asset scope to a role

When you create a new asset scope or edit an asset scope, you can link roles to the scope.

1. Go to **Configuration > Account management > Asset scopes**, and select **Add new asset scope**.
2. Name your asset scope and create a condition if required.  

   You can use conditions to include installations in your asset scopes.
3. In the **Available roles**section, select the roles you want to link the asset scope to.
4. Under **Asset scopes**, select the asset scope that you previously configured from the list.
5. Select **Save and exit**, or select the **Save scope**icon.

### Add a role to a user

For scopes and permissions to apply to a user, you must assign that user with an appropriate role.

When you invite a new user, you can add the role to the user when you [invite them to your site](/classic/docs/add-users-to-a-cloud-site).

You can also add a role to an existing user or account group.

1. Go to **Configuration > Account management > All accounts** or **Account groups**.
2. Select the account group or account of your choice.
3. Navigate to the **Available roles** section and select the role from the list.
4. Select **Save and exit**.

## Priority

If multiple roles are applied to a user, the **permissions** from each role are combined. This means that the user has access to all the features that the permissions defined in the roles grant access to.

Similarly, if multiple scopes are applied to the same role or user, the **scopes** from each are combined. This means that the user has access to all assets that the scopes defined in the roles grant access to.

For example, if a user has the following roles applied:

Role 1:

- Permission: Can only view assets
- Scope: Access to Windows assets only

Role 2:

- Permissions: Can view assets and edit assets
- Scope: Access to Linux assets only

In this case, the user will be able to view and edit the assets that are available to them, and they'll have access to both Windows and Linux assets.
