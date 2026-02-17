<!-- # Manage custom asset data from your Lansweeper Site -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_319/image_001.jpg) **Learn how to manage custom asset data in Lansweeper Sites, including asset states, types, relation types, groups, and custom fields, for seamless integration and transition from Lansweeper On-premises.**

This functionality is available only in Lansweeper On-Premises version 11.3.0.5 and newer. If you're using an older version, please [update to the latest release](/docs/update-lansweeper-on-premises).

Asset states, types, relation types, groups, and custom fields originally created in your Lansweeper On-premises console can be managed in your site, facilitating a smooth transition of your daily operations from Lansweeper On-premises to Lansweeper Sites.

The benefits of enabling this feature are:

- **Migrate operations to Lansweeper Sites:** By managing custom asset data created in Lansweeper On-premises from your site, you can more easily transition your day-to-day operations to Lansweeper Sites without losing any custom data that you’ve already configured.
- **Custom asset data in views and reports:** Use custom asset data in your custom views and reports.
- **Custom asset data in integrations:** Include custom asset data in your integrations for enhanced data management.
- **Multiple Lansweeper On-premises installations:** If you have multiple Lansweeper On-premises installations, your custom asset data is federated, providing a consolidated view in your site.

Before enabling this feature, it’s essential to understand the implications. Please make sure to carefully review the [requirements and considerations](#requirements).

On this page:

- [What Is Custom Asset Data?](#what)
- [Requirements & Considerations](#requirements)
- [Manage Custom Fields](#customfields)
  - [Enable the Management of Custom Fields](#enable-customfields)
  - [View, Edit, Delete, or Add Custom Fields](#edit-customfields)
  - [Edit the Values of Custom Fields](#values-customfields)
- [Manage Asset States, Types, Relation Types, and Groups](#customassetdata)
  - [Enable the Management of Asset States, Types, Relation Types, and Groups](#enable-customassetdata)
  - [View, Edit, Delete, or Add Asset States, Types, Relation Types, and Groups](#edit-customassetdata)
  - [Edit Asset Data Values](#values-customassetdata)

## What Is Custom Asset Data?

**Custom asset data** includes all manually defined information about your assets, such as:

- [Custom fields](/docs/configure-and-add-data-to-asset-custom-fields)
- [Asset states](/docs/create-use-and-change-asset-states)
- [Asset types](/docs/create-asset-types)
- [Relation types](/docs/create-asset-relation-types)
- [Groups](/docs/grouping-assets#heading2)   

  Only static groups are available in Lansweeper Sites. Dynamic groups are available in Lansweeper On-premises.

## Requirements & Considerations

- **Irreversible enablement:** Once enabled, this feature cannot be disabled.
- **Review fields before enabling:** Ensure your custom asset data fields’ names and details are accurate before enabling. Updates to field names must be made manually in both your site and on-prem installation to stay aligned.
- **One-way flow:** Updates made in the Lansweeper On-premises console will sync to the Lansweeper Site but not vice versa.
- **Permission required:** Only site owners can enable this feature.

## Manage Custom Fields

Due to the customization options in custom fields, enabling custom fields is done separately from asset states, types, relation types, and groups.

#### Custom fields federation rules

These rules apply to all installations connected to a site.

- **Same Name and Type**: Fields with the same name and type will be combined. Radio button lists, combo boxes, and Yes/No values will become a dropdown with all values added as options.
- **Same Name, different Type**: Fields with the same name but different types will create separate fields.
- **Slot ID**: The Slot ID is not included in your site.
- **Case and character sensitivity**: Fields are case-insensitive (e.g., "po" and "PO" are the same) but character-sensitive (e.g., "P.O." and "PO" are different).

### Enable the Management of Custom Fields

1. Review your custom fields in every Lansweeper On-premises installation connected to your site.  

   Remember, fields are only updated once upon initial enablement. Any updates you make to your field name or type afterwards will not be reflected in your site, and you’ll have to update both manually.
2. In your Lansweeper Site, go to **Configuration > Site Settings**.
3. Go to **Manage all custom asset data in your site**.
4. Select **Custom Fields > Enable**.
5. Confirm whether you’re ready to enable this feature. Remember, once enabled, it can not be disabled.
6. Select **Enable**.

Once complete, a confirmation message appears.

Depending on its complexity, updating custom asset data will take a few minutes. During this time, your inventory might temporarily display inconsistencies. These will automatically resolve once the update is complete.

### View, Edit, Delete, or Add Custom Fields

In your Lansweeper Site, go to **Inventory > Manage Custom Fields**.

### Edit the Values of Custom Fields

If you’re planning to manage your inventory from your Lansweeper Site or if you need the values between your site and on-prem installation to be different, you can select the option to **Lock against edits from on-prem**. If you do NOT lock against on-prem edits, any changes you make to the value of that field in on-prem will overwrite values added in your site.

Any changes you make to your custom fields in your Lansweeper Site will NOT be reflected in your Lansweeper On-premises console.

To update custom field values:

1. In your **Inventory**, find the asset you want to edit from the list and select the asset.
2. Select **Edit asset**.
3. Navigate to the section of the field you want to edit.
4. Edit the custom fields as needed. If you’re editing custom fields, optionally **lock against edits from on-prem**.
5. Select **Save and Exit**.

## Manage Asset States, Types, Relation Types, and Groups

Asset states, types, relation types, and groups are enabled as one and cannot be individually enabled.

### Enable the Management of Asset States, Types, Relation Types, and Groups

1. Review your custom data in all Lansweeper On-premises installations connected to your site.  

   Remember, fields are only updated once upon initial enablement. Any updates you make to your field name or type afterwards will not be reflected in your site, and you’ll have to update both manually.
2. In your Lansweeper Site, go to **Configuration > Site Settings**.
3. Go to **Manage all custom asset data in your** site.
4. Select **Asset States, Types, Relation Types, Groups > Enable**.
5. Confirm whether you’re ready to enable this feature. Remember, once enabled, it can not be disabled.
6. Select **Enable**.

Once complete, a confirmation message appears.

Depending on its complexity, updating custom asset data will take a few minutes. During this time, your inventory might temporarily display inconsistencies. These will automatically resolve once the update is complete.

### View, Edit, Delete, or Add Asset States, Types, Relation Types, and Groups

- To manage **asset states**, go to **Inventory > Asset States > Manage Asset States**.
- To manage **asset types**, go to **Inventory > Asset Types > Manage Asset Types**.
- To manage **relation types**, go to **Configuration > Asset Management > Relations > Manage Relations**.
- To manage **groups**, go to **Inventory > Asset Groups > Manage Asset Groups**.

### Edit the values of asset states, types, relation types, and groups

Any changes you make to your custom fields in your Lansweeper Site will NOT be reflected in your Lansweeper On-premises console.

1. In **Inventory**, find and select the asset to edit.
2. Select **Edit Asset**.
3. Navigate to the section of the field you want to edit.
4. Enter an updated value for that field.
5. Select **Save and Exit**.
