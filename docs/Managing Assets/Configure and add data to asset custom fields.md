<!-- # Configure and add data to asset custom fields -->
Lansweeper scans Linux, Unix, Mac and Windows computers, VMware servers and other network devices like printers and switches. Though a wealth of data is scanned and available for viewing, you may at times want to manually add more information to your assets.

Your Lansweeper installation includes 20 so-called asset custom fields that are reserved for manual data submission. You can change the display names of these fields to your liking and specify their type. Available types include combo box, currency, date, hyperlink, numeric and more.

Asset custom fields are configured globally, meaning that all assets have the same custom fields. Each asset can of course have its own value for each of these fields. You can fill in the available custom fields for each of your assets by going to the individual asset pages or by using one of the mass editing options. Once a field is filled in for a specific asset, it is displayed in the asset's **Summary** tab. Empty fields are not displayed.  


1. Browse to the **Configuration > Asset Pages**section of the web console.
2. In the **Asset Custom fields** section of the page, place your cursor in the Display Name column and submit a display name for the field you want to use. Don't forget to press **Enter** while your cursor is still present in the line to save the change. The display name you've chosen will be used in the **Summary** tab of assets and certain asset overviews.
3. Optionally, place your cursor in the Info column and submit an informational description for the field. Press **Enter** while your cursor is still present in the line to save the change. The description you've chosen will be displayed as a tooltip next to the field in the **Summary** tab of assets.
4. Select the field type from the Type dropdown and, for combo boxes and radio button lists, submit the possible field values in the Values column. Values must be separated using commas. Available field types are: combo box, currency, date, hyperlink, numeric, radiobutton list, textarea , textbox, time and yes/no checkbox.
5. Make sure the user role of whoever will be filling in asset custom fields includes the **Edit Asset Data** permission. Users that don't have this permission cannot edit custom field data. A complete guide on configuring web console access can be found in [this knowledge base article](/docs/restrict-access-to-the-web-console).
6. Fill in the custom fields of your assets. There are several ways to do this. You can either:
   - Browse to a specific asset's detailed page and select **Edit asset** under **Asset options**.  
     
   - Go to the **Assets** section, tick the checkboxes in front of the assets and select**Mass Edit Assets**under **Asset Actions**. This allows you to set the same custom field value for multiple assets at once.  
     
   - Go to the **Assets**section and select **Mass Edit Assets button** under **Options**. This allows you to place your cursor in the custom field column of the desired asset in the asset list and edit the field value.
7. If you ever want to build your own asset custom field report, create a query based on the tblAssetCustom database table. A sample report that lists your assets and their custom field values can be found [here in our report center](https://www.lansweeper.com/report/). When building an asset custom field report, it is important to keep in mind that:
   - Asset custom fields retain their original Custom1-Custom20 names within the Lansweeper database, regardless of what you set their display names to in the web console. To assign your preferred display names within a report, use aliases. Do not rename the fields within the database itself, as this will break your installation.
   - Asset custom fields retain their original field type (i.e. text) within the Lansweeper database, regardless of what you set their display type to in the web console. If you want to process custom field data in certain ways, to perform calculations for instance, convert the field values within your report.
