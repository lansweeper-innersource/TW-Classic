<!-- # Extended display scanning -->
Extended display scanning is a feature introduced in Lansweeper 9.4. You will need to [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/ "updating your installation") if you are running a lower Lansweeper version.

Extended display scanning retrieves additional data for monitors attached to Windows computers: size in inches, max resolution, aspect ratio, response time, refresh rate, number and type of ports, power usage and more. A wide variety of common monitor models are supported for extended display scanning.

![extended-display-data.png](/docs/.document360/assets/article_184/image_001.jpg)

Extended display scanning is enabled by default in the First Run Wizard of new Lansweeper installations. The feature can also be manually toggled in the **Configuration > General** menu of the Lansweeper web console.

Extended display scanning makes use of a monitor catalog to match known monitor properties to your scanned monitor assets. The catalog is hard coded into the Lansweeper software, but Lansweeper also automatically retrieves an up-to-date copy of the catalog online if available. This requires your Lansweeper server to have access to the following API URL and its sub-URLs: https://discovery-gateway.lansweeper.com/

![menu-configuration-general.png](/docs/.document360/assets/article_184/image_002.jpg)

If you manually enable the feature, don't forget to fully rescan your Windows computers afterward, using the Rescan functionality or a scanning agent. The extended display data will be added to the asset pages of your computers' connected monitor assets when the computers' monitor data is rescanned.

It can also be viewed in the built-in "Monitor: information" report, in built-in charts in the **Chart Report** dashboard widget and in custom reports based on the `tblExtendedDisplayUni` database table. If extended display data was detected for a monitor asset, that monitor asset counts toward your Lansweeper installation's licensed asset limit. If no extended display data could be found or if the extended display scanning feature is not enabled, the monitor asset does not count toward your licensed asset limit. Be aware that if you disable extended display scanning after previously having it enabled, your previously detected extended display data is deleted. If you re-enable the feature, you will need to fully rescan your Windows computers for the extended display data to reappear.
