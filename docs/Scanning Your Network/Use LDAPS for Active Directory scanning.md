<!-- # Use LDAPS for Active Directory scanning -->
Lansweeper supports using the LDAPS protocol for scanning and otherwise connecting to on-premises Active Directory domains. LDAPS communication is encrypted and therefore more secure than plain LDAP.

In Lansweeper Classic, you can choose per domain and per scan server which protocol you want to use for on-premises Active Directory connections, LDAP or LDAPS. You can also choose your preferred port. The LDAP(S) configuration you submit for a domain is used when connecting to that domain in the context of:

- Performing an [Active Directory Domain](/docs/scan-an-active-directory-domain-scanning-target) scan
- Performing an [Active Directory Computer Path](/docs/scanning-with-an-active-directory-computer-path-scanning-target) scan
- Performing an [Active Directory User/Group Path](/docs/scanning-with-an-active-directory-usergroup-path-scanning-target) scan
- Performing an [Active Directory Path (Eventlog Only)](/docs/scanning-with-an-eventlog-only-scanning-target) scan
- Refreshing Active Directory details of individual computers and users in the Lansweeper database
- Running domain-related [cleanup options](/docs/perform-automated-database-cleanups) found in the **Configuration > Server Options** menu
- Checking for Exchange servers in the domain, when performing [Exchange scanning](/docs/scan-exchange-server-mailboxes)

To configure LDAP(S) for an on-premises domain:

1. Browse to the **Scanning > Scanning Targets** menu of the web console. If you have multiple scan servers, there will be a tab for each server.   
   By default, in the LDAP(S) section of the page, only an All Domains configuration will be present. This configuration is used for LDAP(S) connections to any domains that don't have a domain-specific configuration. You can edit this configuration if you want.  
   
2. Select **Add Domain LDAP(S) Config** to add a configuration for a specific domain.
3. In the resulting pop-up, you can choose whether to use LDAP or LDAPS for connections to the domain, as well as the ports.   
   Ports 389 and 636 are the default LDAP and LDAPS ports, respectively. For an LDAPS connection to your domain to be successful, make sure that LDAPS is properly configured in the domain itself and that the necessary certificates are present in the correct certificate stores of your Lansweeper scan server.  
    For connections to your domain in the context of scanning and other operations, Lansweeper will try ports and protocols in this order until one is successful:

- The LDAPS port of your domain-specific configuration, if you added a domain-specific configuration and if you ticked LDAPS for the configuration
- The LDAP port of your domain-specific configuration, if LDAP is ticked
- The LDAPS port of the All Domains configuration, if LDAPS is ticked
- The LDAP port of the All Domains configuration, if LDAP is ticked
- As a final fallback, LDAP over port 389
