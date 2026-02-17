<!-- # Hardware data normalization -->

In IT, OT, and IoT asset management, consistent and accurate data is essential for effective monitoring and reporting. Lansweeper Sites’s normalization feature addresses any potential inconsistencies—such as variations in manufacturer names—by standardizing hardware data across the platform. This ensures consistent information, regardless of the source, enhancing the value of your asset inventory.

Using machine learning, Lansweeper Sites normalizes the manufacturer and model fields. For instance, where an asset may have its manufacturer listed as "VMware" or the older "VMware Inc", Lansweeper Sites will normalize all of these manufacturer names to "VMware".

## Data consolidation flow

The normalization and consolidation process in Lansweeper Sites follows a specific flow to determine which information is displayed:

1. **Locked fields**: If the manufacturer or model fields are locked, the locked value will be prioritized and displayed throughout Lansweeper Sites. Locked fields will not be updated or normalized.

- To lock a field, select **Edit asset** in the asset detail view, and toggle the field lock.
- If you are editing assets through our API, fields will be locked by default. To unlock a field, go to your Lansweeper Site, select **Edit asset** in the asset detail view, and toggle the field lock.

2. **No locked value**: If no field is locked, the normalized value will be displayed throughout Lansweeper Sites.
3. **No normalized value**: If no normalized value is available, Lansweeper Sites will display the value directly as it was scanned from the asset.
4. **No scanned value**: If no value is found from the scanner, the value manually set in the unlocked field within the asset detail view will be displayed throughout Lansweeper Sites.

If you are using custom data for the manufacturer or model fields, make sure to lock the relevant fields.
