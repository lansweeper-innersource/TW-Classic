<!-- # Configure Cloud Discovery -->

Lansweeper’s Cloud Discovery identifies and catalogs all assets within your cloud infrastructure, including virtual machines, storage buckets, databases, and more.

To learn more about Cloud Discovery, see [Introduction to Cloud Discovery](/classic/docs/introduction-to-cloud-discovery).

## Configure Cloud Discovery

You can configure the discovery settings for Cloud from within your Lansweeper Site, allowing you to determine what to scan and when the scans should take place.

For more information about the discovery menu, see [Discovery configuration](/classic/docs/overview-of-discovery-components-and-configuration).

Before scanning your cloud provider, you’ll first need to set up your infrastructure to allow the Cloud sensor to access your environment. Depending on your cloud provider, these steps may differ, but setting up authentication to your cloud environment is crucial.  
For more information on preparing your cloud environment, see [Set up Cloud sensor access](/classic/docs/set-up-cloud-discovery-access).

### Create a new Cloud Discovery action

Cloud Discovery uses the Cloud discovery action to scan for assets in your cloud infrastructure. Currently, you can select either Microsoft Azure, Microsoft Intune, Microsoft Entra ID and Microsoft 365, Amazon Web Services (AWS), or Google Cloud Platform (GCP) as your cloud provider.

#### Microsoft Azure

1. In your Lansweeper Site, go to **Scanning > Discovery actions**.
2. Select **Add new action**.
3. In the pop-up, select the **Cloud** action type and choose **Add action**.
4. Enter a name and description for your action.
5. In **Cloud sources**, select **Cloud provider -** **Microsoft Azure**.
6. Enter your **Tenant ID**, **Application ID** and **Key Vault URI**.
7. Select **List subscriptions**.
8. Select the subscriptions you want to add to the discovery action.
9. Select a workload to scan. By default, all workloads will be selected.
10. Optionally, specify the **Resource Groups** or **Tags** to include in or exclude from the Discovery action.
11. Select **Create new trigger**.
12. In the pop-up, select a scheduling mode, choose when to run the action and enter a name for the trigger.
13. Select **Save trigger**.
14. Select **Save and exit**.

#### Microsoft Intune

1. In your Lansweeper Site, go to **Scanning > Discovery actions**.
2. Select **Add new action**.
3. In the pop-up, select the **Cloud** action type and choose **Add action**.
4. Enter a name and description for your action.
5. In **Cloud sources**, select **Endpoint Management - Microsoft Intune**.
6. Enter your **Tenant ID**, **Application ID**, and **Key Vault URI**.
7. Select **Validate connection**.
8. Optionally, specify the **Device categories** to include in or exclude from the Discovery action.
9. Select **Create new trigger**.
10. In the pop-up, select a scheduling mode, choose when to run the action, and enter a name for the trigger.
11. Select **Save trigger**.
12. Select **Save and exit**.

#### Microsoft Entra ID and Microsoft 365

1. In your Lansweeper Site, go to **Scanning > Discovery actions**.
2. Select **Add new action**.
3. In the pop-up, select the **Cloud** action type and choose **Add action**.
4. Enter a name and description for your action.
5. In **Cloud sources**, select **Identity and Access - Microsoft 365**.
6. Enter your **Tenant ID**, **Application ID**, and **Key Vault URI**.
7. Select **Validate connection**.
8. Optionally, specify the **Resource Groups** or **Tags** to include or exclude in the Discovery action.
9. Select **Create new trigger**.
10. In the pop-up, select a scheduling mode, choose when to run the action, and enter a name for the trigger.
11. Select **Save trigger**.
12. Select **Save and exit**.

#### Amazon Web Services (AWS)

1. In your Lansweeper Site, go to **Scanning > Discovery actions**.
2. Select **Add new action**.
3. In the pop-up, select the **Cloud** action type and choose **Add action**.
4. Enter a name and description for your action.
5. In Cloud sources, select **Cloud provider -****Amazon Web Services (AWS)**.
6. Enter your **Role ARN**.
7. Select either **Standalone account** or **Organization Unit ID or Root ID**.
8. If you selected the latter, enter your Organization Unit ID or your Root ID.
9. Select **List accounts**.
10. Select the accounts you want to add to the discovery action.
11. Select a workload to scan. By default, all workloads will be selected.
12. Select a region to scan. By default, all regions except for China and GovCloud will be selected.
13. Optionally, specify the **Tags** to include in or exclude from the Discovery action.
14. Select **Create new trigger**.
15. In the pop-up, select a scheduling mode, choose when to run the action and enter a name for the trigger.
16. Select **Save trigger**.
17. Select **Save and exit**.

#### Google Cloud Platform (GCP)

1. In your Lansweeper Site, go to **Scanning > Discovery actions**.
2. Select **Add new action**.
3. In the pop-up, select the **Cloud** action type and choose **Add action**.
4. Enter a name and description for your action.
5. In **Cloud sources**, select **Cloud provider -****Google Cloud Platform (GCP)**.
6. Enter your **Workload Identity Pool ID**, **Workload Identity Provider**, **Project Number** and **Service Account Email**.
7. Select **List projects**.
8. Select the projects you want to add to the discovery action.
9. Select a workload to scan. By default, all workloads will be selected.
10. Optionally, specify the **Labels** to include in or exclude from the Discovery action.
11. Select **Create new trigger**.
12. In the pop-up, select a scheduling mode, choose when to run the action and enter a name for the trigger.
13. Select **Save trigger**.
14. Select **Save and exit**.

### Manage Cloud Discovery actions

1. In your Lansweeper Site, go to **Scanning > Discovery actions**.
2. Select the discovery action you want to edit.
3. In the **Cloud action detail** view, manage the cloud provider, authentication information, filters, or triggers.
4. Select **Save and exit**.
