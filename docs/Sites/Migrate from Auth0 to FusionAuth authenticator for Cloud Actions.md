<!-- # Migrate from Auth0 to FusionAuth authenticator for Cloud Actions -->

To continue using Cloud Actions, you must update your credentials to use FusionAuth instead of Auth0 as the authentication provider.

As of June 2025, Lansweeper supports FusionAuth for all Cloud Action integrations, including Amazon AWS, Google GCP, Microsoft Azure, Microsoft 365 (Entra ID), and Intune.

While Auth0 will remain supported until the end of September 2025, we strongly recommend updating as soon as possible to avoid any disruptions. 

## Prerequisites

- Your [Cloud Actions](/classic/docs/configure-cloud-discovery) were previously configured using Auth0 credentials.
- You have access to the Azure Portal, AWS Console, and/or GCP Console.

## Microsoft Azure

1. In the **Azure Portal**, open the **App Registration** used for Azure, M365/Entra ID, or Intune Cloud Actions.
2. Go to **Manage** > **Certificates & secrets**, then select the **Federated credentials** tab.
3. Select **+ Add credential** and enter:
   - **Federated credential scenario**: Other issuer
   - **Issuer**: `https://login.auth.lansweeper.com/6d02a192-efc6-a58a-e413-8abc60f3b067`
   - **Type**: Explicit subject identifier
   - **Value**: `866d6f4d-c8fa-4342-9f6a-377932892ee0`
4. Under **Credential details**, enter:
   - **Name**: Any value, e.g., `FusionAuth`
   - **Audience**: `866d6f4d-c8fa-4342-9f6a-377932892ee0`
5. Select **Add** to save the credential.
6. Remove the previous Auth0 federated credential.

## Amazon AWS

1. In the **AWS Console**, go to **IAM** > **Identity providers**.
2. Select **Add provider** and enter:
   - **Provider type**: OpenID Connect (OIDC)
   - **Provider URL**: `https://login.auth.lansweeper.com/6d02a192-efc6-a58a-e413-8abc60f3b067`
   - **Audience**: `866d6f4d-c8fa-4342-9f6a-377932892ee0`
3. Click **Add provider**.

## Google GCP

1. In the **GCP Console**, go to **IAM** > **Workload Identity Federation**.
2. Open the identity pool used by your GCP Cloud Actions. This corresponds to the **Workload Identity Pool ID** field in your GCP Cloud Actions.
3. Under **Connected service accounts**:
   - Select the tab, then delete the current service account linked to Auth0:   
     `google.subject="D9vGk9gXUNtrwWdifIe0BWC865gu8oHd@clients"`
4. Click **+ Grant access**:
   - Select **Grant access using service account impersonation**.
   - Select the service account used in Cloud Actions.
   - In **Select principals**, choose:
     - **Attribute name**: `subject`
     - **Attribute value**: `866d6f4d-c8fa-4342-9f6a-377932892ee0`
   - Dismiss the **Configure your application** pop-up.
   - Wait for the service account to appear in the list again.
5. Locate the **Providers** tab.
6. Edit the provider used by your Cloud Actions.
   - In the following fields, enter:
     - **Name**: (Optional — if changed, you’ll need to update the **Workload Identity Pool ID** in Cloud Actions)
     - **Issuer (URL)**: `https://login.auth.lansweeper.com/6d02a192-efc6-a58a-e413-8abc60f3b067`
     - **Audience 1**: `866d6f4d-c8fa-4342-9f6a-377932892ee0`

Your Cloud Actions will now use FusionAuth to authenticate instead of Auth0.

No changes are required to Tenant ID, Application ID, Key Vault URI, Role ARNs, or Cloud Action parameters, provided IDs remain unchanged.
