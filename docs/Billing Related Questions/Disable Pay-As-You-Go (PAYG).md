<!-- # Disable Pay-As-You-Go (PAYG) -->

If you're running a Lansweeper Classic on‑premises installation, it may still contain an active license key. As long as this key is present, your on‑prem environment continues sending telemetry, which results in ongoing PAYG billing.

To stop billing, you must either remove or replace the on‑prem license key, or fully stop the Lansweeper services.

There are two ways to disable your Lansweeper Classic installation.

### Disable the Lansweeper service

You can disable the Lansweeper services to prevent telemetry from being generated:

1. Open **Windows Services**.
2. Locate the **Lansweeper Server** service.
3. Right-click the service, and select **Properties**.
4. Set the **Startup type** to **Disabled**.
5. Stop the service if it's still running.
6. Save the changes.

### Turn off the machine

If the server hosts no other critical applications, you can shut it down entirely to stop all Lansweeper activity.
