<!-- # Create asset types -->
When scanning a device, Lansweeper uses a complex internal procedure to determine the device's asset type. Examples of asset types are Linux, Apple Mac, Windows, Printer, Router, and Switch.

Many asset types are built-in, but you can create your own as well by following the instructions below. Once you've added an asset type, you can assign it to assets, either [manually](/classic/docs/change-an-assets-asset-type#heading1 "Changing an asset type") or [automatically](/classic/docs/change-an-assets-asset-type#heading2 "Changing an asset type").

1. Browse to the **Configuration >****Asset Mapping** section of the web console.
2. Select **Add Asset Type** in the **Asset Types** section of the page.
3. Enter an asset type name into the Name field of the pop-up window.
4. Optionally, you can link your own icons to the relation type by placing them in the `Program Files (x86)\Lansweeper\Website\images` folder, found on the computer hosting your Lansweeper web console. Icons should be in the .jpeg, .jpg or .png format and must be stored in two resolutions: 10x10 pixels and 16x16 pixels.  
   
5. Select **Ok**. The asset type is now included in any asset type dropdowns within the web console.
6. You can also edit existing asset types by placing your cursor in the Name or Icon columns, changing, and pressing Enter while your cursor is still in the line. Gray items are locked and cannot be edited to prevent unexpected scanning behavior.
