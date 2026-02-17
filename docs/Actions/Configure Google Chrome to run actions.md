<!-- # Configure Google Chrome to run actions -->
To learn how to protect your browser from potentially dangerous installations, see [Managing Chrome Extensions](https://www.lansweeper.com/pro-tips/managing-chrome-extensions/).

To run asset and user actions in Google Chrome, you first need to install Lansweeper's Chrome extension.

In the past, Lansweeper used an NPAPI plugin to run actions in Chrome. As recent Chrome releases no longer support NPAPI plugins, a new Lansweeper extension was released.

If Chrome is warning you that your plugin is unsupported, reinstall the new Lansweeper extension.

## Install the extension components

1. Download and run [the Lansweeper Extension executable](https://www.lansweeper.com/files/LansweeperExtension_6.0.exe).
2. Select **Next**. The executable adds a Lansweeper folder with the extension components to `Program Files (x86)\Google\Chrome\Application` on your computer. It also attempts to add the extension, which communicates with the extension components, to your browser configuration.
3. Restart Chrome. To ensure that Chrome is fully stopped before restarting, open Windows Task Manager (Ctrl+Shift+Esc), search for the chrome.exe process(es) under **Processes** and select **End Task**.
4. Make sure the extension is enabled. Enter "chrome://extensions/" in Chrome's address bar, select Enter and enable the extension, if it's not already enabled.
   If the extension does not appear in the extension list, install it from the Chrome Web Store.

## Installing the extension from the Chrome Web Store

Make sure you've installed the extension components first, as the extension won't work without the extension components.

1. Follow [this link](https://chrome.google.com/webstore/detail/lansweeper-shell-execute/nnpeignlpkmbhjegcbfacbgcnhhjlghp) to find the Lansweeper extension in the Chrome Web Store.
2. Select **Add To Chrome**.
3. Select **Add extension** in the resulting pop-up.
4. Make sure the extension is enabled. Enter "chrome://extensions/" in Chrome's address bar, select Enter and enable the extension, if it's not already enabled.
