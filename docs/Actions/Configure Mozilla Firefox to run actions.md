<!-- # Configure Mozilla Firefox to run actions -->
You can configure Mozilla Firefox to run actions. For more information, check out [Custom Actions.](https://www.lansweeper.com/feature/custom-actions/)

From Firefox version 57 onward, Mozilla Firefox only supports WebExtensions. Make sure you are running the latest version of Firefox and the latest version of the [Lansweeper](https://www.lansweeper.com/) extension, which is a WebExtension. Older Lansweeper plugins or extensions will be removed by Firefox when updating to Firefox version 57 or higher.

1. Download and run [this executable](https://cdn.lansweeper.com/content/firefox/LansweeperFirefoxExtension_v2.exe) and select **Next**. The executable adds the Lansweeper extension for Firefox to the `Program Files\Mozilla Firefox\browser\extensions` or `Program Files (x86)\Mozilla Firefox\browser\extensions` directory on your computer. ![configuring-mozilla-firefox-to-run-actions-2.jpg](/docs/.document360/assets/article_003/image_002.jpg)
2. Enter "about:addons" in the Firefox address bar and select **Enter**.![configuring-mozilla-firefox-to-run-actions-3.jpg](/docs/.document360/assets/article_003/image_003.jpg)
3. Select the **Extensions** menu.
4. Click the cogwheel icon and select **Install Add-on From File...**![Configuring-Mozilla-Firefox-to-run-actions-6.jpg](/docs/.document360/assets/article_003/image_004.jpg)
5. Browse to `Program Files\Mozilla Firefox\browser\extensions` or `Program Files (x86)\Mozilla Firefox\browser\extensions`.
6. Select "addon@lansweeper.com.xpi" and click **Open**.![Configuring-Mozilla-Firefox-to-run-actions-7.jpg](/docs/.document360/assets/article_003/image_005.jpg)
7. When prompted, select **Enable** for the Lansweeper Shell Execute extension.![configuring-mozilla-firefox-to-run-actions-5.jpg](/docs/.document360/assets/article_003/image_006.jpg)
8. Restart Firefox. To ensure that Firefox is fully stopped before restarting, you can open Windows Task Manager (Ctrl+Shift+Esc), right-click the firefox.exe process(es) under **Processes** and select **End Process**.
