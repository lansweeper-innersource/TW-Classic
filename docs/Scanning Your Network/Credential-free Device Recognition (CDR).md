<!-- # Credential-free Device Recognition (CDR) -->
Credential-free Device Recognition is a feature introduced in Lansweeper 8.2. You will need to [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/ "updating your installation") if you are running a lower Lansweeper version.

## What is Device Recognition?

[Credential-free Device Recognition or CDR](https://www.lansweeper.com/feature/credential-free-device-recognition/) is a feature that aims to do very much with very little. Building upon existing functionality such as the Asset Radar and [IP scanning](https://www.lansweeper.com/feature/ip-scanner/), Lansweeper applies machine learning techniques and big data to enrich assets.

CDR allows Lansweeper to more accurately determine the asset type of certain devices, adding additional information that could previously not be retrieved without credentials, such as the manufacturer, model and operating system. This means that assets that were previously generically identified can now be enriched.

This article details how this feature works, how to enable it and what the pitfalls are.

## How Credential-free Device Recognition works

Using a combination of data gathered from IP scanning and, most importantly, Asset Radar, Lansweeper generates fingerprints. Fingerprints consist of at least a MAC address and may be further enriched with data gathered from various protocols, such as DHCP, HTTP, ARP, etc.   
These fingerprints are generated, encrypted, and stored in the Lansweeper database. They are then sent to the Lansweeper-owned recognition API.   
Based on the received fingerprint, the recognition API returns more information about the device, which is then also stored in the Lansweeper database. Finally, during the next scan of the device, this information is applied to the asset, i.e. its asset type is updated, extra fields are filled in.

To make optimal use of both Asset Radar and CDR, it is recommended to have [a scanning server](/docs/set-up-an-installation-with-multiple-scanning-servers) in each subnet or VLAN that contains relevant devices. CDR will have the greatest impact on devices for which you don't have credentials (yet), IoT devices and unmanaged devices.

## How to enable Credential-free Device Recognition

Credential-free Device Recognition (CDR) can only be enabled on a single scanning server. If you've updated from an older version of Lansweeper to 8.2 or newer, the first scanning server you updated will automatically be set as your CDR server. When you install Lansweeper for the first time, the first scanning server you install will be selected as your CDR server.

CDR is enabled by default in most cases. To toggle the feature, browse to **Configuration > Server Options**. In the **Credential-free Device Recognition** section, select **Enable Credential-free Device Recognition on this server**.



A check then verifies whether this scanning server meets the below requirements:

- The Lansweeper Server service is operational.
- The scanning server can reach the endpoint URLs, which you can find listed at the bottom of this article.
- Whether your license allows the usage of this feature.



Select **Ok** to enable CDR once the requirements checks are passed.



## Disable Credential-free Device Recognition

1. Navigate to your Lansweeper On-premises console.
2. Go to **Configuration > Server Options**.
3. In the **Credential-free Device Recognition** section, select **Disable Credential-free Device Recognition on this server**.

## Troubleshooting

### Make sure the Lansweeper Server service is running

The scanning server you have selected as your recognition server must be operational. Open **services.msc** on the relevant Lansweeper server and check that the Lansweeper Server service is running. If it is not, you can refer to [this article](https://www.lansweeper.com/knowledgebase/scanserver-unavailable-or-not-listed-in-web-console).

### Make sure your Lansweeper server can connect to the internet

Credential-free Device Recognition requires your scanning server to be able to access the internet either directly or via a proxy. You may receive the error below in your web console. This may be caused by one of the following:

- The scanning server you've enabled CDR on has no internet access.
- The scanning server you've enabled CDR on requires proxy configuration.
- Your firewall is blocking access to the URLs used by CDR.



#### Internet Access

Connect to your Lansweeper server directly and test using a browser whether you can connect to the internet, e.g. [www.google.com](http://www.google.com). If this fails, investigate and resolve your server's connection issue.

#### Proxy server

If your Lansweeper server connects to the internet via a proxy, add your proxy details under **Configuration > Server Options**. Make sure these details are correct and that your proxy server is currently available. Do not fill in this configuration section if you do not use a proxy server.

****

#### Firewall

Your firewall or proxy may block certain outbound connections, in which case you'll need to whitelist the endpoints used by CDR. Make sure your Lansweeper service can connect to the URLs below. This may mean for example allowing outbound traffic targeting port 443 on recognition.lansweeper.com. The specifics will differ based on the firewall or proxy system in use.

- The recognition endpoint: https://recognition.lansweeper.com/3/devrecog
- The license authentication endpoint: https://authentication.lansweeper.com
