<!-- # View assets -->
Go to Lansweeper Site's **Inventory**to view the assets in your network.

Want to learn more about all the assets Lansweeper can scan in your network? Check out [What We Discover](https://www.lansweeper.com/assets/).

In **All assets**, you can view all of your assets from every installation that is linked to your site, or browse a variety of pre-configured views based on specific search criteria.

There are a variety of configuration options available to view your assets in a structure that best suits your unique environment. You can:

- Create a custom view
- Sort by multiple columns
- Create an advanced filter view
- Manage a custom view
- Export view
- View assets with issues
- View assets with vulnerabilities

The Customize and Advanced filter views can be combined to create customized views adapted to your specific needs.

## Create a custom view

Organize your asset inventory to best suit your unique environment by creating custom views. Custom views allow you to create a personalized view of your data by displaying the information you require in the format your desire.

To create a custom view:

1. In **Inventory**, select **Customize view.**
2. Under **Fixed columns**, toggle the fixed columns that you want to display **On** or **Off**. Select and hold the column to reorder it.
3. Under **Scrollable columns**, hover over a column and select **X** to remove it, or select and hold the column to reorder it.
4. Under **Available columns**, use the search to find the column you want to add, then click to add it to your custom view.
5. Select **Apply**.
6. If you're happy with the view, select **Unsaved View > Save view and Configurations**. If you'd like to revert to the previous view, select **Restore the default value**.
7. Enter a name for your view. You can also add a description.
8. Select **Save**.

Your view is added to **Inventory > Custom views**.

You can add [normalized data](/classic/docs/software-data-normalization "Normalize your data") or scanned data to your custom views. The normalized fields contain a NORMALIZED tag. Although you can create custom views with scanned data, we recommend using the normalized version for proper organization and aggregation.

## Sort by multiple columns

1. Go to **Inventory** and select any view you want to display.
2. Select a second column you want to sort scanned assets by. Assets are sorted by **Name**by default.
3. Optionally, select more columns to sort your list of assets by. You can sort assets by up to 4 different columns at the same time.   

   Your list of scanned assets will be sorted by the selected columns, prioritizing those selected first.
4. Select **Unsaved View > Save view and Configurations**.
5. Enter a name for your view. You can also add a description.
6. Select **Save**.  

   You can remove a sorted column by selecting **X** .

## Create an advanced filter view

Discover specific data within your inventory by creating advanced filters. Advanced filters allow you to easily find assets based on the fields, operations, and values you require.

To create an advanced filter view:

1. In **Inventory**, select **Advanced filter view**.
2. Enter a field name or select the arrow to view a list of the pre-configured and [custom fields](/classic/docs/edit-assets#customfield "Create a custom field") available.
3. Select an operation.
4. Enter a value. Either:
   - Choose from the list of predefined values.
   - Create new values by selecting **Change**. Enter your value then select **Add filter value** if you wish to add additional values, and select **Apply values** once you're done.
5. Select **+** to add additional filters.
6. Select **Apply**.
7. If you're happy with the view, select **Unsaved View> Save view and Configurations**. If you'd like to revert to the previous view, select **Restore the default value**.
8. Enter a name for your view. You can also add a description.
9. Select **Save**.

Your view is added to **Inventory > Custom view**.

## Manage a custom view

Once a custom view is created, you can edit, rename, share, or delete the view as needed.

To manage a custom view:

1. In **Inventory**, select **Custom views**.
2. Select the view you wish to edit.
3. Select **Custom view**. From there, you can edit, rename, share, or delete the view.

All saved views are private by default. If you want to share your views with other users, you can use the **Share view** option to grant users access to your view.

## Export view

Share your custom views by exporting the view in the format that best suits your environment.

To export a view:

1. In **Inventory**, go to **Export view**.
2. Select the export type:
   - **Standard export**: Download the first 10,000 results automatically. Your file will start downloading once you select **Export**.
   - **Full export**: Download all of the results. You'll receive an email with the attached file once you select **Export**.
3. Select **CSV file** or **XSLX file** for the file type.
4. Select **Export**.

## View assets with issues

To maintain the health of your asset inventory, it's important to address issues that may arise. Lansweeper offers a variety of ways to easily view your assets with scan issues or duplicate conflicts. 

## Scan issues

You can view a list of your assets with scanning issues through the Inventory module's advanced filter. For more information about seeing assets with scan issues, see [View scan issues](/classic/docs/view-scan-issues "View scan issues").

To view your assets with scan issues in the Inventory:

1. Go to **Inventory > Advanced filter view**.
2. Select **Scan issues** from the list of fields.
3. Select an operation and value for you to filter.
4. Select **+** to add additional filters.
5. Select **Apply**.
6. If you're happy with the view, select **Unsaved View > Save view and Configurations**. If you'd like to revert to the previous view, select **Restore the default value**.
7. Enter a name for your view. You can also add a description.
8. Select **Save**.

Your view is added to **Inventory > Custom view**.

## Duplicate assets

Duplicate assets can be generated in your inventory for a variety of reasons. For more information, see [Resolve asset duplicate conflicts](/classic/docs/asset-deduplication-in-cloud "Resolve asset duplicate conflicts").

To view duplicate assets, go to **Inventory > Duplicate conflicts**.

You can also create an advanced filter to view specific assets with duplicate conflicts.

To view assets with duplicate conflicts:

1. Go to **Inventory > Advanced filter view**.
2. Select **Duplicates** from the list of fields.
3. Select an operation and value for you to filter.
4. Select **+** to add additional filters.
5. Select **Apply**.
6. If you're happy with the view, select **Unsaved View> Save view and Configurations**. If you'd like to revert to the previous view, select **Restore the default value**.
7. Enter a name for your view. You can also add a description.
8. Select **Save**.

Your view is added to **Inventory > Custom view**.

## View assets with vulnerabilities

Assets that are affected by vulnerabilities are represented in the **Vulnerabilities** column by the vulnerability icon: .

Hover over the icon to see what severity of vulnerabilities are affecting the asset. Select **Check vulnerabilities** to be redirected to the asset's risk insights page.

For more information about vulnerabilities, check out the articles in [Cyber Security and Risk Insights](https://community.lansweeper.com/t5/cyber-security-and-risk-insights/tkb-p/risk-insights).

### Filter assets with vulnerabilities

To view all your assets that are affected by vulnerabilities:

1. Go to **Inventory > Advanced filter view**.
2. In the dropdown, search for **Vulnerabilities**.
3. Select the **Exists** operator.
4. Select **Apply**.

You can also filter assets based on the severity of the vulnerability affecting them.

1. Go to **Inventory > Advanced filter view**.
2. In the dropdown, search for **Vulnerability severity**.
3. Select the **Equal to** operator.
4. In the value dropdown, select **Critical**, **High**, **Medium**, or **Low**, depending on your preference.
5. Select **Apply**.
