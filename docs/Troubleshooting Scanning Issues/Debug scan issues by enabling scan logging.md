<!-- # Debug scan issues by enabling scan logging -->
Scan logging can be enabled to help debug scan issues. By enabling scan logging, a history of Lansweeper Server scan attempts is created.

Enabling scan logging can significantly increase the size of your database. Only enable this feature when it's necessary for debugging purposes.

To enable scan logging:

1. Go to **Configuration > Server options**.
2. Under **Scan Logging,**select **Enable scan logging.**
3. Select **Delete scan logs after 60 days.**

   Scan logging can significantly increase your database's size, so enter the fewest days possible and delete the data on a regular basis.
4. Open **Windows Services** on your system and find **Lansweeper Server**. Right-click then select **Restart**.
5. Once the new scan attempts have been completed, [create a report](/docs/add-a-report-to-your-lansweeper-installation "Create a new report") based on the tblScanHistory database table. For example, the SQL query might resemble the following:

   ```
   Select Top 1000000 tsysAssetTypes.AssetTypeIcon10 As icon,  
     tblAssets.AssetID,  
     tblAssets.AssetName,  
     tblAssets.Domain,  
     tsysAssetTypes.AssetTypename As AssetType,  
     tblAssets.Username,  
     tblAssets.Userdomain,  
     tblAssets.IPAddress,  
     tblScanHistory.ScanTime,  
     tblScanHistory.ScanServer,  
     tsysScanningMethods.ScanningMethod,  
     tblScanHistory.Description As ScanDescription  
   From tblScanHistory  
     Inner Join tsysScanningMethods On tsysScanningMethods.ScanningMethodId =  
       tblScanHistory.ScanningMethodId  
     Inner Join tblAssets On tblAssets.AssetID = tblScanHistory.AssetId  
     Inner Join tsysAssetTypes On tsysAssetTypes.AssetType = tblAssets.Assettype  
   Order By tblScanHistory.ScanTime Desc
   ```

Scan logging is enabled. Use the report to help debug any scanning issues you might encounter.
