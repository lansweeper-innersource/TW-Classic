<!-- # OT components and architecture -->

For more information about Lansweeper OT, see [Lansweeper for OT Asset Management](https://www.lansweeper.com/use-cases/ot-asset-management/).

Lansweeper OT enables organizations to scan, detect, and identify a wide range of OT devices from popular manufacturers. It’s made up of four components:

- The hub
- The sensor
- The update service
- Lansweeper Sites environment



## The hub

The hub comprises a SQLite database and a user interface that allows you to manage your OT environment. From the user interface, you can:

- View your data
- Manage sensors
- Add scanning targets
- Trigger scans
- Create scanning schedules
- Update protocols

The hub receives data from your sensors and writes that data to the underlying SQLite database. It is also responsible for syncing your scanned OT data with Lansweeper.



## The sensor

The sensor scans your OT devices and sends the data to the hub.

You have full control over your scan targets, schedule, and protocol configuration to ensure information is recorded without interfering with your production environment.

## The update service

The update service provides the hub and sensors with regular updates to keep your OT installation up to date. It is installed automatically on any machine with the hub or sensor installed.

By default, the update service is scheduled to check for software updates every week, but you can configure this schedule in **Settings >****Maintenance**.



## Lansweeper Sites environment

For a complete overview of your IT and OT inventory and access to the full range of Lansweeper’s capabilities, we recommend linking your OT installation with a Lansweeper Site. You can view your OT devices in the **Dashboard** module, or in **Inventory** **> Asset types > OT**.

In your **Inventory**, you can also view the details of your OT devices by selecting the asset.  


Sensors and scans must be implemented and managed through the hub.
