<!-- # Import assets from a CSV file -->
In Lansweeper Classic, there is a built-in option for importing new assets from a .csv file. This allows you to quickly and easily populate your Lansweeper database and web console with devices that can or cannot be scanned. Submit asset names, descriptions, locations, manufacturers, models, SKUs, order numbers, serial numbers, purchase dates, warranty dates and more.

The import feature can currently only be used to import new assets, not update existing ones.

1. Browse to the **Assets > Import Assets**section of the web console.![menu-assets-import-assets.jpg](/docs/.document360/assets/article_133/image_001.jpg)
2. Download the template linked on the page.![importing-assets-1.jpg](/docs/.document360/assets/article_133/image_002.jpg)
3. Open your template, add assets to it and save it as a .csv file. Each line represents one asset.![importing-assets-2.jpg](/docs/.document360/assets/article_133/image_003.jpg)
   - Use the same [date format configured in your web console](/docs/set-the-date-format).
   - Some fields, like the Assettype field, include a dropdown with possible values.
   - Lines with only an OScode, Assettype and State are ignored during import.
   - For Windows computers you need to submit, at a minimum, an asset name, asset domain, asset type and state.
   - For non-Windows machines you need to submit, at a minimum, an asset name, asset type and state.
   - If you're importing assets that will be scanned later, keep in mind [how Lansweeper uniquely identifies assets](/docs/how-lansweeper-uniquely-identifies-assets). If your import file does not include the information Lansweeper uses for its internal asset IDs, new assets will be generated upon scanning. For Windows computers specifically, you need to submit the machines' actual computer names and domain names in your import file. Alternatively, enable rename detection and submit the machines' MAC addresses, models and serial numbers. For non-Windows assets, you need to submit the assets' MAC addresses or IP addresses.
4. Select **Browse** in the web console to launch Windows Explorer, select your .csv file and select **Open**.
5. Select **Validate Import** to look for any mistakes in your file. You may be prompted to add an asset name to one of your assets, submit a domain name for Windows computers etc. Any error messages will mention the row number of the asset that has an error. If any errors are generated, correct your file and re-submit it in the web console.![importing-assets-3.jpg](/docs/.document360/assets/article_133/image_004.jpg)
6. When you've resolved any errors, select **Import Assets**.![importing-assets-4.jpg](/docs/.document360/assets/article_133/image_005.jpg)
