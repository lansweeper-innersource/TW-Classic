<!-- # Track user and system activity with Audit trail -->

Audit trail is a **foundational security feature** in Lansweeper Sites, designed to fill a key visibility gap in user activity monitoring. It enhances audit readiness by providing clear records of who did what and when, directly within your Lansweeper Site.  
  
Lansweeper’s audit trails capture user actions across four key areas: configuration changes (e.g. discovery settings or site setup), inventory edits (e.g. manual asset updates), view exports or API access, and user logins. These events help ensure accountability and support internal or regulatory audits.  
  
Audit trail data is stored securely for up to **12 months** and includes user-identifiable actions, and can be exported for further analysis. Because the data may include personally identifiable information (PII), it's intended for compliance and internal audit use, not for routine support cases.

## Export audit trail data

You can export audit data for reporting, review, or long‑term archival directly from within your Lansweeper Site.  
To export a timeline of user and system activity in your Lansweeper Site:

1. In your Lansweeper Site, go to **Configuration** > **Audit trail**.
2. Select **Export audit trail**.
3. In the popup, select the file type.
4. Select **Export**.

## Export audit trail data via the Data API

For automated workflows, integrations, or advanced analytics, audit trail data can also be retrieved using the Lansweeper Data API.

The Data API includes a dedicated **AuditTrail** data type, allowing you to filter records by date or event type, retrieve detailed user information, and manage large datasets through built‑in pagination.

For technical details and schema definitions, check out [the Types specification](https://developer.lansweeper.com/docs/data-api/reference/types#audittrail).

## Audit trail events

Currently, audit trails are grouped into four main categories:

- Site access
- Accounts configuration
- Inventory configuration
- Discovery configuration
- Data extraction

**All plans** **have access** to Site access, Accounts configuration, and Custom views. Inventory configuration is **only available** on Pro and higher plans. For more information on plans, check out [the pricing page](https://www.lansweeper.com/pricing/).

### Site access

Tracks when users access your Lansweeper Site.

| **Endpoint** | **Description** |
| --- | --- |
| siteAccess | Tracks when a user accesses the site |

### Accounts configuration

Tracks changes to user roles, groups, scopes, and related permissions.

| **Endpoint** | **Description** |
| --- | --- |
| addRole | Creates a new user role |
| updateRole | Edits and updates an existing user role |
| deleteRole | Deletes a single role |
| deleteRoles | Deletes multiple roles in bulk |
| createScope | Creates a new permission scope |
| updateScope | Edits and updates an existing scope |
| deleteScope | Deletes a single scope |
| deleteScopes | Deletes multiple scopes in bulk |
| scopesBulkUpdate | Edits and updates multiple scopes in bulk |
| updateProfile | Edits and updates a user profile |
| deleteProfile | Deletes a single user profile |
| deleteProfiles | Deletes multiple profiles in bulk |
| leaveSite | Tracks when a Lansweeper user leaves the site |
| toggleBlockedAccount | Blocks or unblocks an account’s access to the site |
| createGroup | Creates a new account group |
| updateGroup | Edits and updates an account group |
| deleteGroups | Deletes multiple account groups in bulk |
| deleteGroup | Deletes a single account group |

### Inventory configuration

Tracks updates to asset groups and inventory-related settings.

| **Endpoint** | **Description** |
| --- | --- |
| createAssetGroup | Creates a new asset group |
| updateAssetGroup | Edits and updates an asset group |
| deleteAssetGroup | Deletes a single asset group |
| createManyAssetGroups | Creates multiple asset groups in bulk |
| updateManyAssetGroups | Edits and updates multiple asset groups in bulk |
| deleteManyAssetGroups | Deletes multiple asset groups |
| mergeAssetGroups | Merges two asset groups |
| createAssetRelations | Creates an asset relation between assets or between an asset and a user |
| updateAssetCleanUpRules | Edits and updates asset cleanup rules |
| createAssetStates | Creates new asset states |
| updateAssetStates | Edits and updates asset states |
| deleteAssetStates | Deletes asset states |
| updateIpLocations | Edits and updates IP locations |
| deleteIpLocations | Deletes IP locations |
| createIpLocations | Creates new IP locations |
| deleteAsset | Deletes a single asset |
| deleteAssets (UI) | Deletes multiple assets in bulk |
| deleteAssets (API) | Deletes multiple assets in bulk using the API |
| resolveDedupConflict | Resolves asset duplicates, only keeping a single record in the inventory |
| createAssetV2 | Creates a new asset |
| updateAssetV2 | Updates an asset |
| createAssetRelationTypes | Creates new asset relation types |
| updateAssetRelationTypes | Edits and updates asset relation types |
| deleteAssetRelationTypes | Delete asset relation types |
| launchAssetOperation | Executes a bulk operation on assets |
| bulkEditAssets | Edits multiple assets in bulk (deprecated) |
| bulkDeleteAssets | Deletes multiple assets in bulk (deprecated) |
| securedBulkEditAssets | Securely edits multiple assets in bulk |
| securedBulkDeleteAssets | Securely deletes multiple assets in bulk |
| securedBulkDeleteUsers | Securely deletes multiple users in bulk |
| launchUserOperation | Executes a bulk operation on users |
| manageAssetTypes | Creates, edits or deletes asset types |
| createAssetTypes | Creates multiple asset types in bulk |
| updateAssetTypes | Edits and updates multiple asset types in bulk |
| deleteAssetTypes | Deletes multiple asset types in bulk |
| assetsResync | Forces resynchronization of one or more assets |
| createAzureCloudScanningTarget | Creates an Azure cloud scanning target |
| updateAzureCloudScanningTarget | Edits and updates an Azure cloud scanning target |
| deleteAzureCloudScanningTarget | Deletes a single Azure cloud scanning target |
| createAdUserPathScanningTarget | Creates an AD user path scanning target |
| updateAdUserPathScanningTarget | Edits and updates an AD user path scanning target |
| deleteAdUserPathScanningTarget | Deletes a single AD user path scanning target |
| createAwsRegionScanningTarget | Creates an AWS region scanning target |
| updateAwsRegionScanningTarget | Edits and updates an AWS region scanning target |
| deleteAwsRegionScanningTarget | Deletes a single AWS region scanning target |
| createIntuneV2ScanningTarget | Creates an Intune scanning target |
| updateIntuneV2ScanningTarget | Edits and updates an Intune scanning target |
| deleteIntuneV2ScanningTarget | Deletes a single Intune scanning target |

### Discovery configuration

Tracks updates to discovery settings.

| Endpoint | Description |
| --- | --- |
| updateScanningTargetByScanningTargetId | Edits and updates a scanning target by ID |
| updateAllScanningTargets | Edits and updates all available scanning targets |
| triggerScanNowByScanningTargetId | Triggers a scan for a scanning target by ID |
| triggerScanNowByFilter | Triggers a scan using a filter |
| createWindowsComputerScanningTarget | Creates a Windows computer scanning target |
| updateWindowsComputerScanningTarget | Edits and updates a Windows computer scanning target |
| deleteWindowsComputerScanningTarget | Deletes a single Windows computer scanning target |
| createAdComputerPathScanningTarget | Creates an AD computer path scanning target |
| updateAdComputerPathScanningTarget | Edits and updates an AD computer path scanning target |
| deleteAdComputerPathScanningTarget | Deletes a single AD computer path scanning target |
| createIntuneScanningTarget | Creates an Intune scanning target |
| updateIntuneScanningTarget | Edits and updates an Intune scanning target |
| deleteIntuneScanningTarget | Deletes a single Intune scanning target |
| createChromeOsScanningTarget | Creates a Chrome OS scanning target |
| updateChromeOsScanningTarget | Edits and updates a Chrome OS scanning target |
| deleteChromeOsScanningTarget | Deletes a single Chrome OS scanning target |
| createSccmScanningTarget | Creates an SCCM scanning target |
| updateSccmScanningTarget | Edits and updates an SCCM scanning target |
| deleteSccmScanningTarget | Deletes a single SCCM scanning target |
| createAdDomainScanningTarget | Creates an AD domain scanning target |
| updateAdDomainScanningTarget | Edits and updates an AD domain scanning target |
| deleteAdDomainScanningTarget | Deletes a single AD domain scanning target |
| createIpRangeScanningTarget | Creates an IP range scanning target |
| updateIpRangeScanningTarget | Edits and updates an IP range scanning target |
| deleteIpRangeScanningTarget | Deletes a single IP range scanning target |
| createAirWatchScanningTarget | Creates an AirWatch scanning target |
| updateAirWatchScanningTarget | Edits and updates an AirWatch scanning target |
| deleteAirWatchScanningTarget | Deletes a single AirWatch scanning target |
| createAdUserPathScanningTarget | Creates an AD user path scanning target |
| updateAdUserPathScanningTarget | Edits and updates an AD user path scanning target |
| deleteAdUserPathScanningTarget | Deletes a single AD user path scanning target |
| createConfigGroup | Creates a config group |
| updateConfigGroup | Edits and updates a config group |
| deleteConfigGroup | Deletes a config group |
| createCredential | Creates a credential |
| updateCredential | Edits and updates a credential |
| deleteCredential | Deletes a credential |
| shareHubCredential | Shares a Hub credential |
| createAction | Creates an action |
| updateAction | Edits and updates an action |
| deleteAction | Deletes an action |
| scanNowAction | Triggers a scan action |
| createActionItAgent | Create an IT agent action |
| updateActionItAgent | Edits and updates an IT agent action |
| createExclusion | Creates a discovery exclusion |
| updateExclusion | Edits and updates a discovery exclusion |
| deleteExclusion | Deletes a discovery exclusion |

### Data extraction

Tracks when users export views.

| Endpoint | Description |
| --- | --- |
| exportView | Exports all data from a selected view, including filters and query |
| exportFilteredAssets | Exports filtered assets |
