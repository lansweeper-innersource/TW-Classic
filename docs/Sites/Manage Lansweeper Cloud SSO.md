<!-- # Manage Lansweeper Cloud SSO -->
Using Single Sign-On (SSO) to log in to Lansweeper is recommended, as it has a number of benefits; it simplifies management tasks, eliminates the need for each user to have multiple login/password combinations and allows you to enforce your own security policies, among other things. If you want to set up your SSO connection, see [Set up Lansweeper Cloud SSO](/classic/docs/set-up-lansweeper-sso).

However, there are occasions when you may need to disable or delete a verified and enabled domain from your SSO configuration, or delete the SSO connection altogether.

## Disable or delete a domain

Before you can delete an SSO connection, you need to disable or delete all its enabled domains.

After disabling or deleting a domain, anyone within the affected domain will lose SSO access to Lansweeper, and will need to log in using Lansweeper credentials. If accounts do not have credentials yet, they will receive an email explaining how to create Lansweeper credentials.

Lansweeper credentials consist of an email address and a password, created within the Lansweeper environment.   
SSO credentials are provided by your identity provider, and work across multiple applications.

### Disable a domain

1. Go to **Settings > Single Sign-On**.
2. Select **Disable domain** for the domain you want to disable.  
   
3. In the pop-up, select **Disable domain**.

The domain has been disabled for the SSO connection.

### Delete a domain

If the domain is not disabled yet, follow the steps on disabling a domain.

1. Go to **Settings > Single Sign-On**.
2. Select **Delete domain** for the domain you want to disable.  
   
3. In the pop-up, select **Delete**.

The domain has been deleted for the SSO connection.

## Delete an SSO connection

You will lose all information of the SSO connection and its added domains if you delete an SSO connection.

Before you can delete an SSO connection, you need to disable or delete all its enabled domains.   
To delete an SSO connection:

1. Go to **Settings > Single Sign-On**.
2. Select **Delete connection** for the SSO connection you want to delete.  
   
3. In the pop-up, select **Delete**.

The SSO connection has been deleted.
