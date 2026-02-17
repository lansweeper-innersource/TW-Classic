<!-- # Set up Cloud Discovery access -->
Starting **June 2025**we’re transitioning to FusionAuth as our new authentication provider. Auth0 will be supported until **July 2025**, but we recommend switching as soon as possible. For more information, see [Migrate from Auth0 to FusionAuth authenticator for Cloud Actions](/docs/migrate-from-auth0-to-fusionauth-authenticator-for-cloud-actions).  
Lansweeper Sites hosted in the United States **only** support FusionAuth.

![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_307/image_001.jpg) **This page explains how to set up your Microsoft Azure (including Microsoft Cloud resources), Amazon Web Services (AWS) and Google Cloud Platform (GCP) environments for Lansweeper's Cloud Discovery.**

---

Before scanning your cloud provider, you’ll first need to set up your infrastructure to allow Cloud Discovery to access your environment. Depending on your cloud provider, these steps may differ, but setting up authentication to your cloud environment is crucial. 

On this page, we'll go over the steps needed to set up your [Microsoft Azure, Microsoft Intune, or Microsoft 365](#azure), [Amazon Web Services (AWS)](#aws), and [Google Cloud Platform (GCP)](#gcp) environments.

## Set up Microsoft Azure, Microsoft Intune, and Microsoft 365

Integrating Microsoft Azure, Microsoft Intune, or Microsoft 365 with FusionAuth for Workload Identity Federation involves several steps, ensuring a secure and seamless authentication process without traditional credentials. This setup allows our scanning application to authenticate with Azure services using tokens from FusionAuth, leveraging federated identities.

Intune assets retrieved via Cloud Discovery will not be reconciled yet with assets scanned by your Lansweeper On-prem installation. If the same asset is scanned by both sources, your inventory will display duplicates.

### Register a new application

You’ll first need to register a new application in the Azure portal. You can find detailed instructions in [Quickstart: Register an app in the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app ).

After registering the app, copy the **Application (client) ID** and the **Directory (tenant) ID** and save them for later.

### Add Microsoft Graph API permissions

Next, you’ll need to grant the correct permissions to the newly created app registration. You can find detailed instructions on adding permissions in [Quickstart: Configure an app to access a web API](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis#add-permissions-to-access-microsoft-graph ).

From the list of permissions, add the following permissions based on the data you want to retrieve. Ensure you grant admin consent for each permission added.   
For Microsoft Azure, make sure that the App Registration itself has Reader access to the subscriptions you want to scan.

| **Data** | **Permission Type** | **Permission name** |
| --- | --- | --- |
| Microsoft 365/Entra ID (Organization and Users) | Application | Organization.Read.All Directory.Read.All |
| Microsoft Intune | Application | DeviceManagementManagedDevices.Read.All |

### Configure Federated credentials

Federated credentials are what enable workload identity federation for software workloads. You can find detailed information about Federated credentials in [Create a trust relationship between an app and an external identity provider](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-create-trust?pivots=identity-wif-apps-methods-azp ).

To configure Federated credentials for Lansweeper Discovery:

1. In **Federated credential scenario**, select **Other issuer**.
2. In the **Issuer** field, enter `https://login.auth.lansweeper.com/6d02a192-efc6-a58a-e413-8abc60f3b067` (no trailing space or “/” character).
3. For the **Type**, select **Explicit subject identifier**.
4. In the **Value** field, enter `866d6f4d-c8fa-4342-9f6a-377932892ee0`
5. Enter a **Name** and **Description** for your credential.
6. In the **Audience** field, enter `866d6f4d-c8fa-4342-9f6a-377932892ee0`

### Assign permissions to access Azure resources

To allow your app registration to read resources under a specific subscription, you must assign the necessary role to your new application. Repeat this process for every subscription you wish to scan. You can find detailed instructions on assigning roles in [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal ).

The **Reader** role should be an appropriate role for Lansweeper Discovery.

##### Custom role creation to fully scan some resource types

Some Azure resources require more permissions than the Reader role to be fully scanned by Lansweeper. You can add these permissions to your app registration by creating a Custom Role in Azure.

To create and assign a custom role:

1. Create an Azure custom role. See [Azure custom roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles) for detailed steps.
2. Add the required permissions to the role. The permissions you add depend on the type of Azure resource you want to scan. For example:
   - For **App and Web Services**: Microsoft.Web/sites/config/list/action
   - For **AKS clusters**: Microsoft.ContainerService/managedClusters/listClusterUserCredential/action  
     If a cloud asset is missing permissions, the issue appears in the asset’s **Scan issues** tab.
3. Assign the role to the app registration you created for scanning. Choose the appropriate scope based on what you want to cover:
   - **Management Group**
   - **Subscription**
   - **Resource Group**

When properly configured, the additional scanned properties appear in the asset’s **Cloud Properties** section.

### Create an Azure key vault

The final step in setting up Azure for Lansweeper Discovery is creating an Azure key vault. You can find detailed instructions on creating a key vault in [Quickstart - Create an Azure Key Vault with the Azure portal](https://learn.microsoft.com/en-us/azure/key-vault/general/quick-create-portal ).

After creating a default key vault, you need to configure the permissions:

1. Select **Vault access policy** instead of **Azure role-based access control**.
2. Create an access policy with all secret permissions for your account.
3. Add a secret named LansweeperSiteID to your key vault, entering your Lansweeper Site ID in the **Secret Value** field.  

   To find your Site ID, go to **Configuration > Site settings** in your Lansweeper Site.
4. Grant the **Get** access policy on secrets to your app registration.

After configuring the Azure key vault, copy the **Vault URI** and save it for later.

For additional security, you may want to restrict access to the key vault. Depending where your Lansweeper Site is hosted, restrict access to the following IPs:

- EU: 54.247.163.109, 54.247.185.164, 34.243.192.131
- US: 3.143.85.134, 3.142.89.208, 3.133.69.44

### Create a Microsoft Cloud Discovery action

You can now [create a Cloud Discovery action](/docs/configure-cloud-discovery#azure ) to schedule your cloud asset scanning.

## Set up Amazon Web Services (AWS)

Integrating AWS with FusionAuth for Workload Identity Federation involves several steps, ensuring a secure and seamless authentication process without traditional credentials. This setup allows our scanning application to authenticate with AWS services using tokens from FusionAuth , leveraging federated identities.

### Create an OIDC provider

You’ll first need to create an OpenID Connect (OIDC) provider. You can find detailed instructions in [Create an OpenID Connect (OIDC) identity provider in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html ).

To configure the OIDC provider for Lansweeper Discovery:

1. In the **Provider URL** field, enter `https://login.auth.lansweeper.com/6d02a192-efc6-a58a-e413-8abc60f3b067` (no trailing space or “/” character).
2. In the **Audience** field, enter `866d6f4d-c8fa-4342-9f6a-377932892ee0`

### AWS scanning mechanism

In order to scan multiple AWS accounts, you'll need to configure different account types.   
We can define two account types:

- Main account: defines one Role to list the other accounts, and another Role to read your cloud resources within this account
- Target accounts: defines one Role to read your cloud resources within each account

### Main account: create the accounts listing policy

You’ll first need to create and configure a custom policy. You can find detailed instructions on IAM policies in [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html ).

This policy will allow your Lansweeper Site to list the AWS accounts, as well as assume the Target roles to read the resources in the AWS accounts.

1. In the **Policy editor**, add the following JSON:  

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "organizations:List*",
                   "organizations:Describe*",
                   "sts:GetCallerIdentity",
                   "iam:GetRole",
                   "sts:TagSession",
                   "sts:AssumeRole"
               ],
               "Resource": "*",
               "Condition": {
                   "StringEquals": {
                       "aws:PrincipalTag/siteId": [
                           "<your site ID>"
                       ]
                   }
               }
           }
       ]
   }
   ```

   To find your Site ID, go to **Configuration > Site settings**in your Lansweeper Site.
2. To use the same role to scan the AWS accounts in different Lansweeper Sites, include the Sites in an array similar to:  

   ```
   "StringEquals": {
            "aws:PrincipalTag/siteId": ["site ID #1", "site ID #2"]
           }
   ```

### Main account: create a new role and trust entity

Next, you'll need to create a role and trust entity. You can find detailed instructions in [Creating a role using custom trust policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html ).

This role will allow your Lansweeper Site to assume the permissions listed in the above policy, through the FusionAuth authentication mechanism.

To configure this role for Lansweeper Discovery:

1. Select **Web identity** as the type of trusted entity.
2. In the **Identity provider** field, enter `https://login.auth.lansweeper.com/6d02a192-efc6-a58a-e413-8abc60f3b067`
3. In the **Audience** field, enter `866d6f4d-c8fa-4342-9f6a-377932892ee0`
4. Make sure to select the custom policy you created earlier.
5. Enter a role name, e.g. **LSMainAccountRole**.
6. Create the role, then edit the role.
7. In **Trust relationships**, select **Edit trust policy**.
8. Add a new action named `sts:TagSession`  

   Do not skip adding the **sts:TagSession** action.
9. Save the policy.

You should end up with the following JSON:

```
{
           "Version": "2012-10-17",
           "Statement": [
               {
                   "Effect": "Allow",
                   "Principal": {
                       "Federated": "arn:aws:iam::<account number>:oidc-provider/login.auth.lansweeper.com/6d02a192-efc6-a58a-e413-8abc60f3b067"
                   },
                   "Action": [
                       "sts:AssumeRoleWithWebIdentity",
                       "sts:TagSession"
                   ],
                   "Condition": {
                       "StringEquals": {
                           "login.auth.lansweeper.com/6d02a192-efc6-a58a-e413-8abc60f3b067:aud": "866d6f4d-c8fa-4342-9f6a-377932892ee0"
                       }
                   }
               }
           ]
        }
```

After updating the role, copy the **Role ARN** and save it for later.

### Main and Target accounts: create the Reading policy

You’ll need to create and configure a custom Reading policy. You can find detailed instructions on IAM policies in [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html ).

This policy needs to be created **in all accounts** whose resources will be listed by your Lansweeper Site.

We recommend you use the same name, e.g. LSReadResourcesPolicy, for this Reading policy in all of your accounts to facilitate policy management.

In the **Policy editor**, add the following JSON:

```
{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "<see full list of permissions at the end>"
                ],
                "Resource": "*"
            }
        ]
    }
```

### Main and Target accounts: create a new role and trust entity

Finally, you'll need to create another role and trust entity. You can find detailed instructions in [Creating a role using custom trust policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html ).

This role will allow your Lansweeper Site to read your cloud resources, and needs to be created **in each account** you want to scan.

1. Select **Custom trust policy** as the type of trusted entity.
2. Add a Principal, and select **IAM Roles** as Principal type.
3. Update the ARN with `arn:aws:sts::<main account number>:assumed-role/LSMainAccountRole/web-identity`  

   `main account number` should be replaced with the ID of the AWS account you created the Main role for.  
   `LSMainAccountRole` should be replaced with the name of the Main role, e.g. LSMainAccountRole.
4. In the Action section, add `sts:TagSession`
5. Select **Next**.
6. In the **Permissions policies** page, search for and select the previously created Reading policy.
7. Enter a name for this role, e.g. **LSReading****Role**.  

   You need to use the same name for this role in all of your accounts.

The role trust relationship should look like:

```
{
           "Version": "2012-10-17",
           "Statement": [
               {
                   "Effect": "Allow",
                   "Principal": {
                       "AWS": [
                         "arn:aws:sts::<main account number>:assumed-role/LSMainAccountRole/web-identity"
                       ]
                   },
                   "Action": [
                       "sts:AssumeRole",
                       "sts:TagSession"
                   ]
               }
           ]
        }
```

### Create an AWS Cloud Discovery action

You can now [create a Cloud Discovery action](/docs/configure-cloud-discovery#aws ) to schedule your cloud asset scanning.

To create an AWS discovery action, you will need:

- The ARN of the Main account role, e.g. `arn:aws:iam::<main account number>:role/LSMainAccountRole`
- The name of the reading role, e.g. `LSReadingRole`

### List of AWS permissions

See below for the full list of actions performed by our scanning application.

```
"organizations:ListAccounts",
        "organizations:ListAccountsForParent",
        "organizations:DescribeOrganization",
        "sts:GetCallerIdentity",
        "iam:GetRole",
        "resource-groups:Get*",
        "resource-groups:List*",
        "resource-groups:Search*",
        "ssm:Describe*",
        "ssm:Get*",
        "ssm:List*",
        "codepipeline:Get*",
        "codepipeline:List*",
        "elasticbeanstalk:Describe*",
        "elasticbeanstalk:List*",
        "appfabric:Get*",
        "appfabric:List*",
        "dms:Describe*",
        "dms:List*",
        "ds:Describe*",
        "ds:Get*",
        "ds:List*",
        "route53-recovery-readiness:Get*",
        "route53-recovery-readiness:List*",
        "iam:Get*",
        "iam:List*",
        "autoscaling:Describe*",
        "autoscaling:Get*",
        "securityhub:Describe*",
        "securityhub:Get*",
        "securityhub:List*",
        "network-firewall:Describe*",
        "network-firewall:List*",
        "sqs:Get*",
        "sqs:List*",
        "launchwizard:Describe*",
        "launchwizard:Get*",
        "launchwizard:List*",
        "compute-optimizer:Describe*",
        "compute-optimizer:Get*",
        "dlm:Get*",
        "savingsplans:Describe*",
        "savingsplans:List*",
        "sagemaker-groundtruth-synthetic:Get*",
        "sagemaker-groundtruth-synthetic:List*",
        "emr-serverless:Get*",
        "emr-serverless:List*",
        "route53domains:Get*",
        "route53domains:List*",
        "ses:Describe*",
        "ses:Get*",
        "ses:List*",
        "codeartifact:Describe*",
        "codeartifact:Get*",
        "codeartifact:List*",
        "networkmanager:Describe*",
        "networkmanager:Get*",
        "networkmanager:List*",
        "athena:Get*",
        "athena:List*",
        "iot:Describe*",
        "iot:Get*",
        "iot:List*",
        "appsync:Get*",
        "appsync:List*",
        "ce:Describe*",
        "ce:Get*",
        "ce:List*",
        "cloudtrail:Describe*",
        "cloudtrail:Get*",
        "cloudtrail:List*",
        "kinesis:Describe*",
        "kinesis:Get*",
        "kinesis:List*",
        "iotwireless:Get*",
        "iotwireless:List*",
        "sdb:Get*",
        "sdb:List*",
        "application-autoscaling:Describe*",
        "application-autoscaling:List*",
        "glacier:Describe*",
        "glacier:Get*",
        "glacier:List*",
        "lambda:Get*",
        "lambda:List*",
        "s3:Describe*",
        "s3:Get*",
        "s3:List*",
        "trustedadvisor:Describe*",
        "apprunner:Describe*",
        "apprunner:List*",
        "iotevents:Describe*",
        "iotevents:List*",
        "sagemaker:Describe*",
        "sagemaker:Get*",
        "sagemaker:List*",
        "sagemaker:Search*",
        "clouddirectory:Get*",
        "clouddirectory:List*",
        "iotroborunner:Get*",
        "iotroborunner:List*",
        "account:Get*",
        "account:List*",
        "rds:Describe*",
        "rds:List*",
        "serverlessrepo:Get*",
        "serverlessrepo:List*",
        "serverlessrepo:Search*",
        "lakeformation:Describe*",
        "lakeformation:Get*",
        "lakeformation:List*",
        "lakeformation:Search*",
        "appstream:Describe*",
        "appstream:List*",
        "glue:Get*",
        "glue:List*",
        "glue:Search*",
        "elastic-inference:Describe*",
        "elastic-inference:List*",
        "logs:Describe*",
        "logs:Get*",
        "logs:List*",
        "iotanalytics:Describe*",
        "iotanalytics:Get*",
        "iotanalytics:List*",
        "ecr:Describe*",
        "ecr:Get*",
        "ecr:List*",
        "kafka:Describe*",
        "kafka:Get*",
        "kafka:List*",
        "scheduler:Get*",
        "scheduler:List*",
        "codedeploy:Get*",
        "codedeploy:List*",
        "servicediscovery:Get*",
        "servicediscovery:List*",
        "kms:Describe*",
        "kms:Get*",
        "kms:List*",
        "ecr-public:Describe*",
        "ecr-public:Get*",
        "ecr-public:List*",
        "workspaces-web:Get*",
        "workspaces-web:List*",
        "elasticfilesystem:Describe*",
        "elasticfilesystem:List*",
        "route53-recovery-control-config:Describe*",
        "route53-recovery-control-config:Get*",
        "route53-recovery-control-config:List*",
        "batch:Describe*",
        "batch:List*",
        "events:Describe*",
        "events:List*",
        "waf-regional:Get*",
        "waf-regional:List*",
        "workspaces:Describe*",
        "redshift:Describe*",
        "redshift:Get*",
        "organizations:Describe*",
        "organizations:List*",
        "emr-containers:Describe*",
        "emr-containers:List*",
        "kafkaconnect:Describe*",
        "kafkaconnect:List*",
        "datapipeline:Describe*",
        "datapipeline:Get*",
        "datapipeline:List*",
        "dynamodb:Describe*",
        "dynamodb:Get*",
        "dynamodb:List*",
        "sts:Get*",
        "lightsail:Get*",
        "s3-object-lambda:Get*",
        "s3-object-lambda:List*",
        "cloudfront-keyvaluestore:Describe*",
        "cloudfront-keyvaluestore:Get*",
        "cloudfront-keyvaluestore:List*",
        "firehose:Describe*",
        "firehose:List*",
        "codebuild:Describe*",
        "codebuild:List*",
        "notifications:Get*",
        "notifications:List*",
        "cloudfront:Describe*",
        "cloudfront:Get*",
        "cloudfront:List*",
        "cloudformation:Describe*",
        "cloudformation:Get*",
        "cloudformation:List*",
        "autoscaling-plans:Describe*",
        "autoscaling-plans:Get*",
        "backup:Describe*",
        "backup:Get*",
        "backup:List*",
        "kinesisvideo:Describe*",
        "kinesisvideo:Get*",
        "kinesisvideo:List*",
        "eks:Describe*",
        "eks:List*",
        "pipes:Describe*",
        "pipes:List*",
        "ec2messages:Get*",
        "mq:Describe*",
        "mq:List*",
        "identitystore-auth:List*",
        "tag:Describe*",
        "tag:Get*",
        "config:Describe*",
        "config:Get*",
        "config:List*",
        "es:Describe*",
        "es:Get*",
        "lookoutvision:List*",
        "sns:Get*",
        "sns:List*",
        "cloudsearch:Describe*",
        "cloudsearch:List*",
        "secretsmanager:Describe*",
        "secretsmanager:List*",
        "notifications-contacts:Get*",
        "notifications-contacts:List*",
        "elasticloadbalancing:Describe*",
        "cloudwatch:Describe*",
        "cloudwatch:Get*",
        "cloudwatch:List*",
        "elasticmapreduce:Describe*",
        "elasticmapreduce:Get*",
        "elasticmapreduce:List*",
        "waf:Get*",
        "waf:List*",
        "elasticache:Describe*",
        "elasticache:List*",
        "route53-recovery-cluster:Get*",
        "route53-recovery-cluster:List*",
        "swf:Describe*",
        "swf:Get*",
        "swf:List*",
        "ec2:Describe*",
        "ec2:Get*",
        "ec2:List*",
        "ec2:Search*",
        "transfer:Describe*",
        "transfer:List*",
        "iot1click:Describe*",
        "iot1click:Get*",
        "iot1click:List*",
        "wafv2:Describe*",
        "wafv2:Get*",
        "wafv2:List*",
        "ecs:Describe*",
        "ecs:List*",
        "kinesisanalytics:Describe*",
        "kinesisanalytics:Get*",
        "kinesisanalytics:List*",
        "route53:Get*",
        "route53:List*",
        "route53resolver:Get*",
        "route53resolver:List*"
```

## Set up Google Cloud Platform (GCP)

Integrating GCP with FusionAuth for Workload Identity Federation involves several steps, ensuring a secure and seamless authentication process without traditional credentials. This setup allows our scanning application to authenticate with GCP services using tokens from FusionAuth, leveraging federated identities.

### Create a Workload Identity Pool

You’ll first need to create a Workload Identity Pool. You can find detailed instructions on creating Workload Identity Pools in [Manage workload identity pools and providers](https://cloud.google.com/iam/docs/manage-workload-identity-pools-providers ).

To configure the Workload Identity Pool for Lansweeper Discovery:

1. Select the **OpenID Connect (OIDC)** provider.
2. In the **Issuer URL** field, enter `https://login.auth.lansweeper.com/6d02a192-efc6-a58a-e413-8abc60f3b067`
3. In the **Allowed audiences** field, enter `866d6f4d-c8fa-4342-9f6a-377932892ee0`
4. For attributes, map **google.subject** to **assertion.sub**.
5. Add a second attribute mapping, and map **attribute.site\_id** to **assertion.site\_id**

   To find your Site ID, go to **Configuration > Site settings**in your Lansweeper Site.
6. Finally, add the following attribute condition: `attribute.site_id == '<your site ID>'`  

   To allow several Lansweeper Sites to scan your GCP assets with the same credentials, include the OR-operator “||” to your attribute condition, e.g. `attribute.side_id == '<site ID #1>' || attribute.site_id == '<site ID #2>'`

After creating the Workload Identity Pool, copy the **pool ID** and save it for later.

### Create a service account

Next, you’ll need to create a service account that grants permissions to the application. You can find detailed instructions in [Create service accounts](https://cloud.google.com/iam/docs/service-accounts-create ).

The **Viewer** role should be an appropriate role for Lansweeper Discovery. After creating the service account, copy the **account email address** and save it for later.

### Configure roles

Your service account needs access to your organization and folders. You can find detailed instructions on granting the appropriate roles in [Manage access to projects, folders, and organizations](https://cloud.google.com/iam/docs/granting-changing-revoking-access ).

The service account will need the **Folder Viewer** and **Organization Viewer** roles.

### Configure access to Workload Identity Pool

The Workload Identity Pool needs to be configured to allow impersonation of the service account by the federated identity. You can find detailed instructions in [Manage workload identity pools and providers](https://cloud.google.com/iam/docs/manage-workload-identity-pools-providers ).

In the **Attribute name** field, select **subject** and enter `866d6f4d-c8fa-4342-9f6a-377932892ee0`

### Multiple GCP projects

If you want to scan multiple GCP projects, you will have to grant the **Viewer** role to the service account you created for every project you want to scan. You can find detailed instructions on granting the appropriate roles in [Manage access to projects, folders, and organizations](https://cloud.google.com/iam/docs/granting-changing-revoking-access ).

### Create a GCP Cloud Discovery action

You can now [create a Cloud Discovery action](/docs/configure-cloud-discovery#gcp ) to schedule your cloud asset scanning.
