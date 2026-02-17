<!-- # Cloud Discovery: Frequently Asked Questions -->

[Lansweeper’s Cloud Discovery](/docs/introduction-to-cloud-discovery) identifies and catalogs all assets within your cloud infrastructure, includingvirtual machines, storage buckets, databases, and more.

## Frequently asked questions (FAQ)

- I configured my AWS, Azure or GCP discovery action and assets are not ending up in my Lansweeper Sit...

### I configured my AWS, Azure or GCP discovery action and assets are not ending up in my Lansweeper Site: Inventory > Cloud assets.

- Ensure you set up the right access from Lansweeper Site to your public cloud environment. See [Microsoft Azure](/docs/set-up-cloud-discovery-access#azure), [Amazon Web Services (AWS)](/docs/set-up-cloud-discovery-access#aws), and [Google Cloud Platform (GCP)](/docs/set-up-cloud-discovery-access#gcp).
- If you encounter the following error while creating the discovery action:  
  *"The application does not have the required permission to access the key vault. Ensure the application has ‘GET secret’ and ‘LIST secret’ permissions."*It indicates that the app registration does not have access to the secrets of the key vault. While it can access the key vault itself, it cannot read the secrets.   
  To resolve this issue, you need to add an Access Policy to the key vault and grant the application the required permissions.
  - In the **Access policies** section of the key vault, you need to define the access of your Application (App registration) to the secrets (Get and List access). You must also add your own user account access on the secrets. This will allow you to edit the secrets.

    
  - When receiving this message while configuring AWS: “Missing role permissions or the Site ID is missing from the policy configuration”, ensure you set your **Lansweeper Site ID** (in [https://app.lansweeper.com](https://app.lansweeper.com/) > Configuration > Site settings) in the permissions of the policy aws:PrincipalTage/siteID with a value similar as “3805ffa8-c8ca-4276-cb34-331ab64b3784“ **(not your AWS account number).**
  - This is also described in this Medium article: [Accessing Azure Key Vault Secrets with Azure Functions](https://medium.com/@dssc2022yt/accessing-azure-key-vault-secrets-with-azure-functions-2e651980f292).

- If you can’t find the audience field for Azure federated credentials:  
  In the German version of Azure, this appears to be the *Benutzergruppe* field. For your convenience, we have included a screenshot of the English version below so you can follow the steps in the KB article.  

  
- Ensure there are no hidden trailing space characters in the secret value of the key vault.
- Ensure the Lansweeper Site ID saved in the secret is indeed the ID of the Lansweeper Site you are creating the Cloud Discovery action in (see **Configuration > Site settings > Site ID**).
- When you create the Cloud Discovery action, set a trigger to occur 5 minutes in the future (for testing purposes) and wait 10-15 minutes before checking the inventory.
