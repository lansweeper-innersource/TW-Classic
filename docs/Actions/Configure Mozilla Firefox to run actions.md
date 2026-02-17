<!-- # Configure Mozilla Firefox to run actions -->
You can configure Mozilla Firefox to run actions. For more information, check out [Custom Actions.](https://www.lansweeper.com/feature/custom-actions/)

From Firefox version 57 onward, Mozilla Firefox only supports WebExtensions. Make sure you are running the latest version of Firefox and the latest version of the [Lansweeper](https://www.lansweeper.com/) extension, which is a WebExtension. Older Lansweeper plugins or extensions will be removed by Firefox when updating to Firefox version 57 or higher.

1. Download and run [this executable](https://cdn.lansweeper.com/content/firefox/LansweeperFirefoxExtension_v2.exe) and select **Next**. The executable adds the Lansweeper extension for Firefox to the `Program Files\Mozilla Firefox\browser\extensions` or `Program Files (x86)\Mozilla Firefox\browser\extensions` directory on your computer. 
2. Enter "about:addons" in the Firefox address bar and select **Enter**.
3. Select the **Extensions** menu.
4. Click the cogwheel icon and select **Install Add-on From File...**
5. Browse to `Program Files\Mozilla Firefox\browser\extensions` or `Program Files (x86)\Mozilla Firefox\browser\extensions`.
6. Select "addon@lansweeper.com.xpi" and click **Open**.
7. When prompted, select **Enable** for the Lansweeper Shell Execute extension.
8. Restart Firefox. To ensure that Firefox is fully stopped before restarting, you can open Windows Task Manager (Ctrl+Shift+Esc), right-click the firefox.exe process(es) under **Processes** and select **End Process**.
