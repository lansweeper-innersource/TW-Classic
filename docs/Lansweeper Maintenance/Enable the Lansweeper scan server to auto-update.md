<!-- # Enable the Lansweeper scan server to auto-update -->

Auto-updates ensure Lansweeper stays updated with the latest features, security patches, and performance improvements without manual intervention. By enabling automatic updates, you can reduce maintenance efforts, minimize downtime, and keep your system running smoothly.

Auto-update is enabled by default.

## Requirement & considerations

- Lansweeper **12.3.2.2** or later is required.
- If the auto-update fails, the Update Service will trigger a rollback.
- Auto-update supports environments with multiple scan servers.
- Ensure scan server jobs, such as scanning and deployments, are not running during scheduled auto-updates, as they will be interrupted.

## Network connectivity requirements

To allow Lansweeper to download and install updates automatically, ensure your network or proxy allows outbound traffic to the following URLs over HTTPS (port 443). These connections are required for retrieving update packages, version information, and related files.

If your environment uses a strict firewall, proxy, or operates in a restricted or air‑gapped network, whitelist the following URLs:

- [https://cdn.lansweeper.com](https://cdn.lansweeper.com )
- <https://discovery-gateway.lansweeper.com/versions>
- <https://download.lansweeper.com>

If your organization uses regional routing or inspection, ensure that TLS 1.2 or higher is supported for these connections. Without outbound access to these domains, the auto‑update feature cannot complete successfully.

## Enable auto-update

1. In your Lansweeper On-premises console, go to **Configuration > Auto-update**.
2. Select **Automatically install updates**.  
   ![auto-update.png](/docs/.document360/assets/article_101/image_002.jpg)

## Manage auto-updates

When it is available, a new version will appear under the **Availability** section. The system checks for new versions every hour.

![adab4590-6b63-4d67-8c35-4ca479f945cb.png](/docs/.document360/assets/article_101/image_003.jpg)

### Install updates manually

If you'd prefer to install updates before the scheduled maintenance time, select **Install updates**.

### Schedule auto-updates

You can choose the days and times for your updates. Auto-updates interrupt scan server jobs, so schedule them accordingly.

1. In your Lansweeper On-premises console, go to **Configuration > Auto-update > Change period**.
2. Select which days of the week you want the update to occur.
3. Select which time of day you want the update to occur.
4. Select **Save maintenance settings**.

### **Update history**

The **History** section contains the history of previous auto-updates, where you can review past updates, including version details and statuses.

![2b723303-26aa-425f-af93-9abab5dc55c8.png](/docs/.document360/assets/article_101/image_004.jpg)

## **Database permission requirement**

The **LansweeperUser** account used to connect to the **LansweeperDB** instance must have the `dbcreator` role assigned.

If this role is not configured, a notification will appear:

> "The LansweeperUser account used to connect to the LansweeperDB instance doesn't have the 'dbcreator' role. In the unlikely event that a rollback is needed during the auto-update process, the service will not be able to roll back the database automatically unless the 'dbcreator' role is granted to the LansweeperDBUser."

To resolve this issue, execute the following command:

```
use master 
GO 
EXEC sp_addsrvrolemember [lansweeperuser], [dbcreator]; 
GO 
GRANT VIEW SERVER STATE TO [lansweeperuser] 
GO 
use lansweeperdb 
GO
```
