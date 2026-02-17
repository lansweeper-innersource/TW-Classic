<!-- # View your user inventory -->
Lansweeper Sites allows you to view your company’s users by creating an inventory of Active Directory users. The user inventory enables you to easily see a list of your users, discover details about your users, and create and view relations between your users and other assets.

At this time, only Active Directory users are available in the user inventory.

On this page:

- View users
  - Create a custom view
  - Create an advanced filter view
  - Export your view
- Find users
- Learn more about your users
  - Learn about which users are connected to your assets
- Create user relations
- Restrict user inventory access

## View users

To view your entire inventory of users, go to **Users > All users**.

You can also create customized views that allow you to see the users you want, and filter out any users that don’t match the criteria you’ve established. Once you’ve created your custom views, you can export those views and share them.

### Create a custom view

Organize your user inventory to best suit your unique environment by creating custom views. Custom views allow you to add or remove columns containing specific fields and order those columns in the way that makes the most sense for you.

You can combine custom views and advanced filters to further refine your list of users.

1. Go to **Users > All users**.
2. Select **Customize view**.
3. To add columns to the table, select the plus symbol under **Available columns**. To remove columns, select the x symbol under **Scrollable columns**.
4. Select **Apply**.
5. If you’re happy with your view, select **Unsaved view > Save view and configuration**.
6. Enter a view name and a description. Select **Save**.

To view your custom view, go to **Users > Custom views** and select the name of the view.

### Create an advanced filter view

Advanced filters allow you to filter your list of users so that only the ones that meet the criteria you want are displayed.

You can combine advanced filters and custom views to further refine your list of users.

1. Go to **Users > All users**.
2. Select **Advanced filter view**.
3. Enter a field name or select the arrow to view a list of the pre-configured fields available.
4. Select an operation.
5. Enter a value.
6. Select **+** to add additional filters.
7. By default, the And operator is applied. If you want to change the operator to Or, select **And**.
8. Select **Apply**.
9. If you're happy with the view, select **Unsaved View> Save view and Configurations**.
10. Enter a view name and a description. Select **Save**.

To view your custom view, go to **Users > Custom views** and select the name of the view.

### Export your view

Share your custom views by exporting the view in the format that best suits your environment.

1. Go to **Users**.
2. If you want to export the list of all users, select **All users**. Otherwise, select **Custom views** then select the view you want to export.
3. Select **Export view**.
4. Select the export type:
   - **Standard export**: Download the first 10,000 results automatically. Your file will start downloading once you select **Export**.
   - **Full export**: Download all of the results. You'll receive an email with the attached file once you select **Export**.
5. Select **CSV file** or **XSLX file** for the file type.
6. Select **Export**.

## Find users

If you want to find specific users, you can search for those users using either the local user inventory search or global search.

- Local search: Go to **Users** and enter your search into the search bar. This only searches your user inventory.
- Global search: Go to the global search icon at the bottom-left of the screen and enter your search. This searches across all of your users, assets, and reports.

## Learn more about your users

To learn more about a specific user, select the display name of that user. You’ll be redirected to the user **Summary** page.

From here, you can find extra available information about the user such as their address, phone number, organization details, active directory group details, and more.

If the user has relationships configured between it and another asset, they’ll be displayed under **Relations**. You can also create user relations from here.

If applicable, an Exchange tab is available if the user is connected to a related account.

Currently, the user inventory is intended to give you better visibility of your users, so users are read-only. However, users are still manageable through [Lansweeper On-Premises](/docs/how-to-scan-users).

### Learn about which users are connected to your assets

Users connected to assets are also displayed on asset summary pages. To access an asset summary page, go to **Inventory** and select the asset you want to learn more about. If you’ve created a user relation, the relation is displayed under **Relations**.

Additionally, if an asset has been used by an Active Directory user, their username is displayed in the **Last user** field, as well as their user type. Select the username to be redirected to the user’s summary page.

To view a list of assets where the Last user field displays a user, go to **Inventory > Advanced Filter view**. Select **Last user** for the field name dropdown and **Exists** for the operation, then **Apply**.

## Create user relations

User relations allow you to see how specific users are related to assets in various ways. The user summary page shows existing relationships and allows you to create new user relations.

1. Go to **Users**.
2. Locate the user you want to edit from the list. You can search or use a custom view to help narrow your search.
3. Select the user’s display name.
4. Select **Add relation**.  
   
5. Enter the name of an asset or search for it in the dropdown.
6. Add the relation type from the dropdown.
7. Optionally, add a start and end date, and comments.
8. Select **Add new relationship**.

You can view the relation on the user summary page. Select the name of the asset to be redirected to the asset summary page. The relation is also added to the asset summary page.

## Restrict user inventory access

If multiple people have access to your Lansweeper Site, you might want to restrict certain people’s access to the user inventory to limit the exposure of potentially sensitive or personally identifiable data. User access can be granted or restricted by editing the permissions for specific roles.

1. Go to **Configuration > Account management > Roles and permissions**.
2. Select the role you want to configure.
3. Select the **Users** tab. Depending on the role and your preference, select or deselect the following options. Selecting the option allows access to that field.
   - View users
   - Export Users
   - Full Export
4. Select **Save role**.

Ensure each role has the correct permissions you desire, and that those roles are assigned to accounts accordingly.

For more information about how roles and permissions are configured, see [Configure scopes, permissions, and roles](/docs/configure-scopes-permissions-and-roles).
