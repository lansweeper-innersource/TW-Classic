<!-- # Lansweeper installation and management types -->
Setting up Lansweeper involves choosing from three [installation types](#installationtype): Cloud-first, On-premise, and Hybrid. The installation type determines how you can set up and access your Lansweeper data.

After choosing an installation type, you’ll also have to choose a [management type](#managementtype): either On-premise management, or Cloud management. The management type dictates how and where your Lansweeper license is managed. Although you can [change your management type](#changemanagement) if needed, it is by no means an easy process.

## Installation types

There are three ways to set up your Lansweeper installation:

1. **A Cloud-first installation**: the inventory and scanning configuration is managed from [a Cloud-based site](http://app.lansweeper.com/). This is also known as a [Cloud-first site](/docs/install-lansweeper-sites).
2. **A local on-premise installation**: the inventory and scanning configuration is managed from a locally installed web console. This is known as an [On-premise installation](/docs/install-lansweeper-on-prem).
3. **A** **local on-premise installation linked to a cloud site**: the inventory and scanning configuration is managed from both a locally installed web console and a cloud site. This is also known as a [Hybrid installation](#hybrid).

Note that you can’t mix different installation types in the same cloud site.

- In a Cloud-first scenario, all linked installation types need to be Cloud-first installations, and you won’t be able to link any Hybrid installations.
- In a Hybrid scenario, all linked installation types need to be Hybrid installations, and you won’t be able to link any Cloud-first installations.

### Cloud-first installation

In a Cloud-first scenario, your Lansweeper license is managed and granted from Lansweeper Sites.  
While the Cloud-first installer is identical to the On-prem/Hybrid installer, the management type you choose will vary.

To set up a Cloud-first installation, see [Install Lansweeper Sites](/docs/install-lansweeper-sites).

A Cloud-first installation differs from a Cloud-first trial installation, as the trial installer is uniquely linked to a specific cloud site. If you want to try the Cloud-First trial instead, see [Install the Lansweeper Cloud-first trial](/docs/install-the-lansweeper-trial).

### On-premise installation

In a local on-premise scenario, you are sent a Lansweeper license key which needs to be entered in the local web console when installing Lansweeper On-prem or renewing your subscription.  
While the On-prem installer is identical to the Cloud-first/Hybrid installer, the management type you choose will vary.

To set up a Lansweeper On-prem installation, see [Install Lansweeper On-prem](/docs/install-lansweeper-on-prem).

### Hybrid installation

In a hybrid scenario, you are sent a Lansweeper license key which needs to be entered in the local web console when installing Lansweeper On-prem or renewing your subscription.  
While the Hybrid installer is identical to the Cloud-first/On-prem installer, the management type you choose will vary.

To set up a Hybrid installation, you must [install Lansweeper On-prem](/docs/install-lansweeper-on-prem) first. Afterwards, [link your on-premise installation to a Lansweeper cloud site](/docs/link-lansweeper-on-prem-with-lansweeper-sites).

## Management types

The management type of your installation dictates how and where your Lansweeper license is managed.   
There are two ways your license can be managed:

- Via a license key: after purchasing a Lansweeper license, you will be sent a license key via email.
- Via a subscription: after purchasing a Lansweeper license, your subscription will automatically be added to your cloud site. Any linked installations will be validated as well.

### On-premise management

If you were sent a license key, your management type will be **On-premise management**. Both **On-premise** and **Hybrid** installations have the On-premise management type.

During the installation process, you will have to enter your license key in the [First Run Wizard](/docs/install-lansweeper-on-prem#FRW).

### Cloud management

If you weren’t sent a license key, and your subscription is managed from the cloud, your management type will be **Cloud management**. Only **Cloud-first** installations have the Cloud management type.

During the installation process, you will have to link your scan server to your cloud site, but you won’t have to enter a license key, since your subscription is managed from the cloud.

If you aren’t sure if your license is managed from the cloud, go to your cloud site and navigate to **Configuration > License status**. If you can’t see the **License status** menu, your license is managed from On-prem instead.

### Change your management type

After using Lansweeper for a while, you might want to change your Lansweeper management type. Carefully consider whether you want to change your management type, as it's a difficult process.

#### Cloud to On-premise management

Depending on your needs, you may find that the Cloud management type is still suitable. If you are interested in the On-prem web console, for example, you could enable the console by following the steps in [Enable the Lansweeper Classic web console](/docs/enable-the-lansweeper-on-premises-web-console).

If you do want to change to On-premise management:

1. Contact our Lansweeper Sales team via [our sales form](https://www.lansweeper.com/contact/contact-sales/), and inform us of your decision. You will be sent an on-premise license key via mail.
2. Unlink the installation(s) you want to locally manage from your cloud site.
3. Enter your new Lansweeper license key in your on-premise installation.
4. Optionally, you can link your On-prem installation to a cloud site again. For more information on linking your On-prem installation, see [Link Lansweeper On-prem with Lansweeper Sites](/docs/link-lansweeper-on-prem-with-lansweeper-sites).

If you want to link your Lansweeper On-premises installation to your previous Lansweeper Site, you will need to unlink all installations from the Site and remove all data.   
For more information on unlinking your installations, see [Remove an installation from your site](/docs/remove-an-installation-from-your-cloud-site).

#### On-premise to Cloud management

Moving from On-premise to Cloud management involves losing all of your collected data and configurations, as you must reinstall Lansweeper completely.

If you do want to change to Cloud management:

1. Contact our Lansweeper Sales team via [our sales form](https://www.lansweeper.com/contact/contact-sales/), and inform us of your decision.
2. Unlink all installations linked to your cloud site, and remove all data. For more information on unlinking your installations, see [Remove an installation from your site](/docs/remove-an-installation-from-your-cloud-site).
3. Uninstall all on-premise installations.
4. Reinstall Lansweeper in Cloud-first mode. For more information on installation Lansweeper Cloud-first, see [Install Lansweeper Sites](/docs/install-lansweeper-sites).
5. Your newly created cloud site will be connected to your existing license, becoming a subscription managed from the cloud.
