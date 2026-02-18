<!-- # How to scan disabled Active Directory users and computers -->
Disabled AD user and computer scanning is a feature introduced in Lansweeper 7.2. You will need to [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/ "updating your installation") if you are running a lower Lansweeper version.

From version 7.2 onward, each Lansweeper scanning server can be configured to scan Active Directory users and computers that have been disabled in AD. In prior Lansweeper versions, AD objects were ignored during scanning if they were disabled.

This article explains how to enable scanning of disabled AD users and computers and how to view the results.

### Step 1: enable scanning of disabled Active Directory users and/or computers

Go to **Scanning > Scanning Targets > On-Premises Active Directory Scanning Options**. In the **Scanning Scope** section, enable one or both of the options below, depending on whether you want to scan just disabled computer objects, just disabled user objects or both. Keep in mind that enabling the options below will no longer allow you to enable cleanup options for removing disabled users or computers, and vice versa. The "scan disabled" and "remove disabled" options cannot be combined because they logically contradict each other.   


If the AD options above are greyed out, scroll down and make sure the "remove computers disabled..." and "remove users disabled..." options are unchecked.

### Step 2: scan disabled Active Directory users and/or computers

Go to **Scanning > Scanning Targets** and add the below scanning targets. Afterward, click **Scan Now** next to these targets to scan them.  


These targets connect directly to Active Directory to retrieve the user and computer objects.

- For computers, the scan type will be an Active Directory Computer Path. More information on this target type and how to set it up can be found in [this article](/classic/docs/scanning-with-an-active-directory-computer-path-scanning-target).
- For users, the scan type will be an Active Directory User Path. More information on this target type and how to set it up can be found in [this article](/classic/docs/scanning-with-an-active-directory-usergroup-path-scanning-target).

### Step 3: view the scanning results

Go to the **Reports** menu and search for "enabled/disabled". There are two reports that list AD computers and users and whether they're enabled or disabled.  

Individual computer and user webpages also show the object's Active Directory status. 

Disabled Active Directory computers are very likely to have a scanning error. Their Active Directory status will prevent them from being logged onto the network and will therefore prevent them from being scanned directly.
