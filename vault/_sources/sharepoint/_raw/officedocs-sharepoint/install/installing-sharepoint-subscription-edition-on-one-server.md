---
title: "Installing SharePoint Server Subscription Edition on one server - SharePoint Server"
description: "Learn how to install SharePoint Server Subscription Edition on one server."
ms.topic: article
---
Note

Installing SharePoint Server Subscription Edition on one server

# Installing SharePoint Server Subscription Edition on one server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

You can install and configure SharePoint Server Subscription Edition on a single server if you are hosting only a few sites for a limited number of users or if you want to create a trial or development environment. This configuration is also useful if you want to configure a farm to meet your needs first, and then add servers to the farm at a later stage.

Note

In previous versions of SharePoint, a single server installation automatically installed SQL Server Express. In SharePoint Server Subscription Edition, a single server installation contains only SharePoint. SQL Server can be installed on the same server or on a separate server; both scenarios are supported. For better performance we recommend installing SQL Server on a separate server.

Overview

## Overview

After you have completed setup and the SharePoint Products Configuration Wizard, you will have installed binaries, configured security permissions, configured registry settings, configured the configuration database, configured the content database, and installed the SharePoint Central Administration website. Next, you can choose to run the Farm Configuration Wizard to configure the farm, select the services that you want to use in the farm, and create the first site collection, or you can manually perform the farm configuration at your own pace.

Before you install SharePoint Server Subscription Edition on a single server

## Before you install SharePoint Server Subscription Edition on a single server

Before you begin to install and configure SharePoint Server Subscription Edition, do the following:

Ensure that you perform a clean installation of SharePoint Server Subscription Edition.

Ensure that you are prepared to set up the required accounts by using appropriate permissions. For detailed information, see Initial deployment administrative and service accounts in SharePoint Server.

Ensure the Max degree of parallelism is set to 1. For additional information about max degree of parallelism see, Configure the max degree of parallelism Server Configuration Option.

Important

As a security best practice, we recommend that you install SharePoint Server Subscription Edition by using least-privilege administration.

Tip

If you decide to install prerequisites manually, you can still run the Microsoft SharePoint Products Preparation Tool to verify which prerequisites are required on each server.

Install SharePoint Server Subscription Edition on a single server

## Install SharePoint Server Subscription Edition on a single server

To install and configure SharePoint Server Subscription Edition on a single server, you will follow these steps:

Run the **Microsoft SharePoint Products and Technologies Preparation Tool,** which installs all prerequisites to use SharePoint Server.

Run Setup, which installs binaries, configures security permissions, and edits registry settings for SharePoint Server Subscription Edition.

Run SharePoint Products Configuration Wizard, which installs and configures the configuration database, installs and configures the content database, and installs the SharePoint Central Administration website.

Configure browser settings.

Run the Farm Configuration Wizard, which configures the farm, creates the first site collection, and selects the services that you want to use in the farm.

Perform post-installation steps.

Important

To complete the following procedures, the account that you use must be a member of the Administrators group on the computer on which you are installing SharePoint Server. For information about user accounts, see Initial deployment administrative and service accounts in SharePoint Server.

Run the Microsoft SharePoint Products Preparation Tool

### Run the Microsoft SharePoint Products Preparation Tool

Because the prerequisite installer downloads components from the Microsoft Download Center, you must have Internet access on the computer on which you are running the installer. Use the following procedure to install software prerequisites for SharePoint Server Subscription Edition.

**To run the Microsoft SharePoint Products Preparation Tool**

Verify that the user account that is performing this procedure is the farm administrator user account. For information about the farm administrator user account, see Initial deployment administrative and service accounts in SharePoint Server.

In the SharePoint Server installation disc image software, mount the ISO file, and click the splash.hta file. The SharePoint Server splash screen is displayed.

Click **Install software prerequisites**.

On the **Welcome to the SharePoint Products Preparation Tool** page, click **Next**.

On the **License Terms for software products** page, review the terms, select the **I accept the terms of the License Agreement(s)** check box, and then click **Next**.

On the **Your system needs to restart to continue** page, click **Finish** to restart the computer.

Repeat steps 2-4.

On the **Installation Complete** page, click **Finish**.

Run Setup

### Run Setup

The following procedure installs binaries, configures security permissions, and edits registry settings for SharePoint Server. At the end of Setup, you can choose to start the SharePoint Products Configuration Wizard, which is described later in this section.

**To run Setup**

Verify that the user account that is performing this procedure is the farm administrator user account. For information about the farm administrator user account, see Initial deployment administrative and service accounts in SharePoint Server.

On the **SharePoint Server Start** page, click **Install SharePoint Server**.

On the **Enter Your Product Key** page, enter your product key, and then click **Continue**.

On the **Read the Microsoft Software License Terms** page, review the terms, select the **I accept the terms of this agreement** check box, and then click **Continue**.

Optional: To install SharePoint Server at a custom location, or to store search index files at a custom location, click the **File Location** tab, and then either type the custom location or click **Browse** to find the custom location.

Note

If you intend to use this computer as a search server, we recommend that you store the search index files on a separate storage volume or partition. Any other search data that needs to be stored is stored in the same location as the search index files. You can only set this location at installation time.

Click **Install Now**.

When Setup finishes, a dialog prompts you to complete the configuration of your server. Ensure that the **Run the SharePoint Products Configuration Wizard now** check box is selected.

Click **Close** to start the configuration wizard.

Note

If Setup fails, check log files in the Temp folder of the user account you used to run Setup. Ensure that you are logged in using the same user account and then type %temp% in the location bar in Windows Explorer. If the path in Windows Explorer resolves to a location that ends in a "1" or "2", you have to navigate up one level to view the log files. The log file name is SharePoint Server Setup (<  *time stamp*>).

Run the SharePoint Products Configuration Wizard

### Run the SharePoint Products Configuration Wizard

Use the following procedure to install and configure the configuration database and the content database, and to install the SharePoint Central Administration website.

**To run the SharePoint Products Configuration Wizard**

Verify that the user account that is performing this procedure is the farm administrator user account. For information about the farm administrator user account, see Initial deployment administrative and service accounts in SharePoint Server.

If you have closed the SharePoint Products Configuration Wizard, you can access it by clicking **Start**, point to **All Apps**, click **Microsoft SharePoint Products**, and then click **SharePoint Products Configuration Wizard**. If the **User Account Control** dialog appears, click **Continue**.

On the **Welcome to SharePoint Products** page, click **Next**.

In the dialog that notifies you that some services might have to be restarted during configuration, click **Yes**.

On the **Connect to a server farm** page, click **Create a new server farm**, and then click **Next**.

On the **Specify Configuration Database Settings** page, do the following:

In the **Database server** box, type the name of the computer that is running SQL Server.

In the **Database name** box, type a name for your configuration database or use the default database name. The default name is SharePoint_Config.

In the **Username** box, type the user name of the farm administrator service account. Ensure that you type the user name in the format DOMAIN\username.

Important

The farm administrator service account is used to access your configuration database. It also acts as the application pool identity account for the SharePoint Central Administration application pool, and it is the account under which the Microsoft SharePoint Foundation Timer service runs. The SharePoint Products Configuration Wizard adds this account to the SQL Server Login accounts, the SQL Server **dbcreator** server role, and the SQL Server **securityadmin** server role. The user account that you specify as the farm administrator service account has to be a domain user account. However, it does not have to be a member of any specific security group on your SharePoint servers or your database servers. We recommend that you follow the principle of least-privilege and specify a user account that is not a member of the Administrators group on your SharePoint servers or your database servers.

In the **Password** box, type the user password.

Click **Next**.

On the **Specify Farm Security Settings** page, type a passphrase, and then click **Next**.

Although a passphrase resembles a password, it is usually longer to improve security. It is used to encrypt credentials of accounts that are registered in SharePoint Server. For example, the SharePoint Server server farm administrator service account that you provide when you run the SharePoint Products Configuration Wizard. Ensure that you remember the passphrase, because you must use it every time that you add a server to the farm. Ensure that the passphrase meets the following criteria:

- Contains at least eight characters

- Contains at least three of the following four character groups:

- English uppercase characters (from A through Z)

- English lowercase characters (from a through z)

- Numerals (from 0 through 9)

- Nonalphabetic characters (such as !, $, #, %)

On the **Specify Server Role** page, choose the appropriate role, click **Next**.

Note

For a single server farm, we recommend choosing the **Single Server Farm** role, although you can select a **Custom** role if you want to individually manage the services instances that run on the server. You can change the role of a server later if you change your mind or want to expand your farm by adding additional servers.

On the **Configure SharePoint Central Administration Web Application** page, do the following:

- Either select the **Specify port number** check box and type the port number that you want the SharePoint Central Administration web application to use, or leave the **Specify port number** check box cleared if you want to use the default port number.

- Click either **NTLM** or **Negotiate (Kerberos)**.

Click **Next**.

On the **Completing the SharePoint Products Configuration Wizard** page, review your configuration settings to verify that they are correct, and then click **Next**.

On the **Configuration Successful** page, click **Finish**. When the wizard closes, setup opens the web browser and connects to Central Administration.

If the SharePoint Products Configuration Wizard fails, check the PSCDiagnostics log files, which are located on the drive on which SharePoint Server Subscription Edition are installed, in the`%COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\LOGS` folder.

If you are prompted for your user name and password, you might have to add the SharePoint Central Administration website to the list of trusted sites and configure user authentication settings in Internet Explorer. You might also want to disable the Internet Explorer Enhanced Security settings. If you see a proxy server error message, you might have to configure proxy server settings so that local addresses bypass the proxy server. Instructions for configuring proxy server settings are provided in the following section. For more information about how to configure browser and proxy settings, see Configure browser settings.

Configure browser settings

### Configure browser settings

After you run the SharePoint Products Configuration Wizard, you should confirm that SharePoint Server works correctly by configuring additional settings in Internet Explorer.

If you are not using Internet Explorer, you might have to configure additional settings for your browser. For information about supported browsers, see Plan browser support in SharePoint Servers 2016 and 2019.

To confirm that you have configured browser settings correctly, log on to the server by using an account that has local administrative credentials. Next, connect to the SharePoint Central Administration web site. If you are prompted for your user name and password when you connect, perform the following procedures:

- Add the SharePoint Central Administration website to the list of trusted sites

- Disable Internet Explorer Enhanced Security settings

If you receive a proxy server error message, perform the following procedure:

- Configure proxy server settings to bypass the proxy server for local addresses

**To add the SharePoint Central Administration website to the list of trusted sites**

Verify that the user account that completes this procedure has the following credentials:

- The user account is a member of the Administrators group on the computer on which you are performing the procedure.

In Internet Explorer, on the **Tools** menu, click **Internet Options**.

On the **Security** tab, in the **Select a zone to view or change security settings** area, click **Trusted Sites**, and then click **Sites**.

Clear the **Require server verification (https:) for all sites in this zone** check box.

In the **Add this web site to the zone** box, type the URL to your site, and then click **Add**.

Click **Close** to close the **Trusted Sites** dialog.

Click **OK** to close the **Internet Options** dialog.

**To disable Internet Explorer Enhanced Security settings**

Verify that the user account that completes this procedure has the following credentials:

- The user account is a member of the Administrators group on the computer on which you are performing the procedure.

Click **Start**, point to **All Apps**, point to **Administrative Tools**, and then click **Server Manager**.

In **Server Manager**, select the root of **Server Manager**.

In the **Security Information** section, click **Configure IE ESC**.

The **Internet Explorer Enhanced Security Configuration** dialog appears.

In the **Administrators** section, click **Off** to disable the Internet Explorer Enhanced Security settings, and then click **OK**.

**To configure proxy server settings to bypass the proxy server for local addresses**

Verify that the user account that completes this procedure has the following credentials:

- The user account is a member of the Administrators group on the computer on which you are performing the procedure.

In Internet Explorer, on the **Tools** menu, click **Internet Options**.

On the **Connections** tab, in the **Local Area Network (LAN) settings** area, click **LAN Settings**.

In the **Automatic configuration** area, clear the **Automatically detect settings** check box.

In the **Proxy Server** area, click the **Use a proxy server for your LAN** check box.

Type the address of the proxy server in the **Address** box.

Type the port number of the proxy server in the **Port** box.

Select the **Bypass proxy server for local addresses** check box.

Click **OK** to close the **Local Area Network (LAN) Settings** dialog.

Click **OK** to close the **Internet Options** dialog.

Run the Farm Configuration Wizard

### Run the Farm Configuration Wizard

You have now completed setup and the initial configuration of SharePoint Server. You have created the SharePoint Central Administration web site. You can now configure your farm and sites, and you can select services by using the Farm Configuration Wizard.

**To run the Farm Configuration Wizard**

Verify that the user account that is performing this procedure is the farm administrator user account. For information about the farm administrator user account, see Initial deployment administrative and service accounts in SharePoint Server.

On the SharePoint Central Administration home page, on the **Quick Launch**, click **Configuration Wizards**, and then click **Launch the Farm Configuration Wizard**.

On the **Help Make SharePoint Better** page, click one of the following options, and then click **OK**:

- **Yes, I am willing to participate (Recommended.)**

- **No, I don't want to participate.**

On the **Configure your SharePoint farm** page, next to **Yes, walk me through the configuration of my farm using this wizard**, click **Start the Wizard**.

On the **Service Applications and Services** page, in the **Service Account** section, click the service account option that you want to use to configure your services.

Important

For security reasons, we recommend that you use a different account from the farm administrator account to configure services in the farm.
If you decide to use an existing managed account — that is, an account of which SharePoint Server Subscription Edition is aware — make sure that you click that option before you continue.

In the **Services** section, review the services that you want to use in the farm, and then click **Next**.

On the **Create Site Collection** page, do the following:

In the **Title and Description** section, in the **Title** box, type the name of your new site.

Optional: In the **Description** box, type a description of what the site contains.

In the **Web Site Address** section, select a URL path for the site.

In the **Template Selection** section, in the **Select a template** list, select the template that you want to use for the top-level site in the site collection.

Note

To view a template or a description of a template, click any template in the **Select a template** list.

Click **OK**.

On the **Configure your SharePoint farm** page, review the summary of the farm configuration, and then click **Finish**.

Post-installation steps

## Post-installation steps

After you install and configure SharePoint Server, your browser window opens to the Central Administration web site of your new SharePoint site. Although you can start adding content to the site or customizing the site, we recommend that you first perform the following administrative tasks.

**Configure usage and health data collection** You can configure usage and health data collection in your server farm. The system writes usage and health data to the logging folder and to the logging database.

**Configure diagnostic logging** You can configure diagnostic logging that might be required after initial installation or upgrade. The default settings are sufficient for most situations. Depending upon the business needs and life-cycle of the farm, you might want to change these settings.

**Configure incoming e-mail** You can configure incoming e-mail so that SharePoint sites accept and archive incoming e-mail. You can also configure incoming e-mail so that SharePoint sites can archive e-mail discussions as they occur, save e-mailed documents, and show e-mailed meetings on site calendars. In addition, you can configure the SharePoint Directory Management Service to provide support for e-mail distribution list creation and administration.

**Configure outgoing email** You can configure outgoing email so that your Simple Mail Transfer Protocol (SMTP) server sends email alerts to site users and notifications to site administrators. You can configure both the "From" email address and the "Reply" email address that appear in outgoing alerts.

**Configure Search settings** You can configure Search settings to crawl the content in SharePoint Server.

**Configure Central Administration Access URL**

**Using Alternative URL to Access Central Administration**: You can specify an alternative URL to access Central Administration by using Alternate Access Mapping (AAM). This can be done via the optional `-Url <String>` parameter in the PowerShell cmdlets `New-SPCentralAdministration` and `Set-SPCentralAdministration` and PSConfig.exe command line utility `PSConfig.exe -cmd adminvs`.

**Using host name binding for Central Administration**: You can configure the SharePoint Central Administration website to use host header bindings, that will allow it to share the same Transmission Control Protocol (TCP) port number as other websites. This would typically be used to let the SharePoint Central Administration site and your content website to be hosted on the same TCP port, such as port 443 for Secure Sockets Layer (SSL).

To configure the SharePoint Central Administration website, specify the host header binding with the `-HostHeader` parameter of the `New-SPCentralAdministration` and `Set-SPCentralAdministration` cmdlets, or with the `-hostheader` parameter of the `psconfig.exe -cmd adminvs` command.

Additional resources

## Additional resources

- Last updated on 
		2025-08-11
