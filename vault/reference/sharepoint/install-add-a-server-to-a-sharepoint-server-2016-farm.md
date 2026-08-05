---
title: "Add a server to a SharePoint Server 2016 or SharePoint Server 2019 farm - SharePoint Server"
type: reference
domain: sharepoint
slug: install-add-a-server-to-a-sharepoint-server-2016-farm
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/install/add-a-server-to-a-sharepoint-server-2016-farm
family: install
documentKind: "how-to"
abstract: "Learn how to add a server to an existing SharePoint Server farm."
---

# Add a server to a SharePoint Server 2016 or SharePoint Server 2019 farm - SharePoint Server

Note

Add a server to a SharePoint Servers 2016 or 2019 farm

# Add a server to a SharePoint Servers 2016 or 2019 farm

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Before you add a server to a SharePoint farm

## Before you add a server to a SharePoint farm

Determine server role

### Determine server role

To add a new server to the farm, you must know its intended role to plan for additional or specialized configurations and assess the potential effect of adding the server to a production environment.

In SharePoint Server 2016, the concept of server roles has changed from previous versions. Server role types are now defined by MinRole which allow for better deployment and health of the server in the farm. For additional information about the MinRole feature and a description for each server role type, see Overview of MinRole Server Roles in SharePoint Servers 2016 and 2019.

Additional tasks

### Additional tasks

Before you start to install prerequisite software, you have to complete the following:

Verify that the new server meets the hardware and software requirements described in Hardware and software requirements for SharePoint Server 2016.

Verify that the new server meets the hardware and software requirements described in Hardware and software requirements for SharePoint Server 2019.

Verify that you have the minimum level of permissions that are required to install and configure SharePoint Servers 2016 or 2019 on a new server. You must be a member of the Farm Administrators SharePoint group and the Administrators group on the local server to complete the procedures in this article. For more information, see Initial deployment administrative and service accounts in SharePoint Server.

Verify that you know the name of the database server on the farm to which you are connecting, and the name of the configuration database if you are adding the server by using Microsoft PowerShell commands.

If you intend to use PowerShell commands to add the server, verify that you meet the following minimum memberships is installed.

**Securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Add-SPShellAdmin.

- Document the location of the SharePoint Server binary and log files on the existing farm servers. We recommend that the location of these files on the new server map to the locations used on the other servers in the farm.

Important

If you change the location of the trace log to a non-system drive, change the location on all the servers in the farm. Existing or new servers cannot log data if the location does not exist. In addition, you will be unable to add new servers unless the path that you specify exists on the new server. You cannot use a network share for logging purposes.

Install prerequisite software

## Install prerequisite software

Before you can install SharePoint Server and add a server to the farm, you must check for and install all the prerequisite software on the new server. You do this by using the Microsoft SharePoint Products Preparation Tool, which requires an Internet connection to download and configure SharePoint Server prerequisites. If you do not have an Internet connection for the farm servers, you can still use the tool to determine the software that is required. You will have to obtain installable images for the required software.

For download locations, see Links to applicable software in "Hardware and software requirements (SharePoint Server 2016)."

For download locations, see Links to applicable software in "Hardware and software requirements (SharePoint Server 2019)."

Tip

After you obtain a copy of the required software, we recommend that you create an installation point that you can use to store the images. You can use this installation point to install future software updates.

For detailed instructions about how to install the prerequisites, see Prepare the farm servers in the article, Install SharePoint Servers 2016 or 2019 across multiple servers.

Tip

If you decide to install prerequisites manually, you can still run the Microsoft SharePoint Products Preparation Tool to verify which prerequisites are required on each server.

Install the SharePoint software

## Install the SharePoint software

After you install the prerequisites, follow these steps to install SharePoint Servers 2016 or 2019 on the new server. For detailed instructions about how to install SharePoint Server, see Install SharePoint Server on one server.

**To install SharePoint Server**

Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see Initial deployment administrative and service accounts in SharePoint Server.

From the product media or a file share that contains the SharePoint Server Products installation files, run Setup.exe.

On the **Enter Your Product Key** page, enter your product key, and then click **Continue**.

Review and accept the Microsoft License Terms.

Accept the default file location where SharePoint Server will be installed or change the installation path in order to suit your requirements.

Tip

As a best practice, we recommend that you install SharePoint Server on a drive that does not contain the operating system.

Click **Install Now**.

When Setup finishes, a dialog prompts you to run the **SharePoint Products Configuration Wizard**. You can start the wizard immediately or from the Windows command prompt later.

Add the new SharePoint server to the farm

## Add the new SharePoint server to the farm

You add the new server to the farm by using one of the following procedures:

To add a server by using the SharePoint Products Configuration Wizard

To add a new SharePoint Server 2016 or SharePoint Server 2019 server to the farm by using the PSConfig.exe command-line tool

To add a server by using Microsoft PowerShell

**To add a new SharePoint Server 2016 or SharePoint Server 2019 server to the farm by using the SharePoint Products Configuration Wizard**

Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see Initial deployment administrative and service accounts in SharePoint Server.

Start the **SharePoint Products Configuration Wizard**.

On the **Welcome to SharePoint Products** page, click **Next**.

On the **Connect to a server farm** page, click **Connect to an existing server farm.**

Click **Next**.

On the **Specify Configuration Database settings** page, type the name of the instance of SQL Server in the **Database server** box, and then click **Retrieve Database Names**.

Select the name of the configuration database in the **Database name** list, and then click **Next**.

On the **Specify Farm Security Settings** page, type the name of the farm passphrase in the **Passphrase** box, and then click **Next**.

On the **Specify Server Role** page, choose the appropriate role, and then click **Next**.

Note

The concept of server roles has changed staring with SharePoint Server 2016. You can't add a server to a farm if the farm currently contains a server assigned to the "Single Server Farm" role. > For additional information about MinRole, see Overview of MinRole Server Roles in SharePoint Servers 2016 and 2019.

On the **Completing the SharePoint Products Configuration Wizard** page, click **Next**.

On the server that hosts Central Administration, click **Manage servers in this farm** to verify that the new server is part of the farm.

Note

You can also verify a successful server addition or troubleshoot a failed addition by examining the log files. These files are located on the drive on which SharePoint Server is installed, in the %COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\LOGS folder.

On the **Servers in Farm** page, click the name of the new server. Use the list of available services on the **Services on Server** page to start the services that you want to run on the new server.

Note

This step should only apply if the Custom role is used.

**To add a new SharePoint Server server to the farm by using the PSConfig.exe command-line tool**

To create a farm by using the PSConfig.exe command-line tool, use the following syntax:

```
psconfig.exe -cmd configdb -connect -server <SqlServerName> -database <ConfigDbName> -user <DOMAIN\FarmServiceAccount> -password <FarmServiceAccountPassword> -passphrase <FarmPassphrase> -admincontentdatabase <AdminContentDbName> -localserverrole <ServerRole> -cmd helpcollections -installall -cmd secureresources -cmd services -install -cmd installfeatures -cmd adminvs -provision -port <PortNumber> -windowsauthprovider onlyusentlm -cmd applicationcontent -install
```

Where <ServerRole> can be any of the following values: WebFrontEnd, Application, DistributedCache, Search, or Custom.

Note

The SingleServerFarm cannot be used unless the SharePoint farm has zero servers in it.

Note

If SharePoint Server 2016 Feature Pack 2 has been applied, additional <ServerRole> options are available: ApplicationWithSearch, WebFrontEndWithDistributedCache. These options are also available in SharePoint Server 2019.

Note

The  `PSConfig.exe -cmd Services -Provision` syntax is deprecated, but not removed yet. Do not use the **Provision** parameter when you create or join a farm. Using this parameter will lead to failures.

**To add a new SharePoint Server 2016 or SharePoint Server 2019 server to the farm by using PowerShell**

Verify that you have the following memberships:

**securityadmin** fixed server role on the SQL Server instance.

**db_owner** fixed database role on all databases that are to be updated.

Administrators group on the server on which you are running the PowerShell cmdlets.

An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.

Note

If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps

Start the SharePoint Management Shell.

At the PowerShell command prompt, type the following command to connect the server to a configuration database:

```
Connect-SPConfigurationDatabase -DatabaseServer <SqlServerName> -DatabaseName <ConfigDbName> -Passphrase <FarmPassphrase>  -LocalServerRole <ServerRole>
```

Where:

*<$DatabaseServer>* is the name of the server that hosts the configuration database

*<DatabaseName>* is the name of the configuration database

*<$Passphrase>* is the passphrase for the farm

*<ServerRole>* is the server role type

Where <ServerRole> can be any of the following values: WebFrontEnd, Application, DistributedCache, Search, or Custom.

Note

If SharePoint Server 2016 Feature Pack 2 has been applied, additional <ServerRole> options are available: ApplicationWithSearch, WebFrontEndWithDistributedCache. These options are also available in SharePoint Server 2019.

Note

The concept of server roles has changed starting with SharePoint Server 2016. You can't add a server to a farm if the farm currently contains a server assigned to the "Single Server Farm" role. > For additional information about MinRole, see Overview of MinRole Server Roles in SharePoint Servers 2016 and 2019.

At the PowerShell command prompt, type the following command to install the Help File Collections:

```
Install-SPHelpCollection -All
```

At the PowerShell command prompt, type the following command to install the Security Resource for SharePoint Server:

```
Initialize-SPResourceSecurity
```

At the PowerShell command prompt, type the following command to install the basic services:

```
Install-SPService
```

At the PowerShell command prompt, type the following command to install all the features:

```
Install-SPFeature -AllExistingFeatures
```

At the PowerShell command prompt, type the following command to set the port number of the SharePoint Central Administration website:

```
New-SPCentralAdministration -Port <PortNumber> -WindowsAuthProvider NTLM
```

Note

If the SharePoint Central Administration website is already provisioned on an existing server in the farm, you can skip this step.

At the PowerShell command prompt, type the following command to install application content:

```
    Install-SPApplicationContent
```

At the PowerShell command prompt, type the following command to start the Timer service:

```
Start-Service SPTimerV4
```

At the PowerShell command prompt, type the following command to get a list of servers in the farm.

```
Get-SPServer
```

Note

You can also verify a successful server addition or troubleshoot a failed addition by examining the log files. These files are located on the drive on which SharePoint Servers 2016 or 2019 is installed, in the %COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\LOGS folder.

Additional resources

## Additional resources

- Last updated on 
		2023-01-25
