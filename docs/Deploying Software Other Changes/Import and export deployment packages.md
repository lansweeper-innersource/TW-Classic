<!-- # Import and export deployment packages -->
Lansweeper includes [a deployment module](https://www.lansweeper.com/kb-category/deploying-software-and-other-changes/) that allows you to remotely make changes to the Windows computers in your network. You can create your own deployment packages, but you can also import packages from and export them to .xml files.

This allows you to use packages that others have created. It also allows you to share your creations with other Lansweeper users and with the Lansweeper support team, e.g. should you be having trouble running certain packages you've created.

## Import or export a deployment package

1. Browse to the **Deployment > Deployment packages**section of the web console.
2. To export a package, select the package and select **Export**, above the package name and description.
3. To import a package, select **Import**, select the **Browse...** button in the resulting pop-up, select your .xml file and click **OK**.  

   Make sure you also download and place any files referenced by your deployment package in your package share folder. By default, this is the `Program Files (x86)\Lansweeper\PackageShare` folder on your Lansweeper server, which is automatically shared as DefaultPackageShare$. If you configured a different package share, you can see its name listed in the **Deployment > Security Options** section of the console.
