---
title: "Checklist for database-attach upgrade (SharePoint 2013) - SharePoint Server"
description: "Use this checklist as you upgrade from SharePoint 2010 Products to SharePoint 2013."
ms.topic: checklist
---
Note

Checklist for database-attach upgrade (SharePoint 2013)

# Checklist for database-attach upgrade (SharePoint 2013)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

This checklist helps you confirm that you follow all the steps that you must follow as you prepare for upgrade, perform the upgrade, and perform post-upgrade steps. This checklist applies only to upgrade of the content and service application databases. It does not apply to upgrade of My Sites or other site collections. For more information, see Upgrade a site collection to SharePoint 2013.

Some steps include notes about how long that step might take. These rough estimates only give you a relative idea of the duration of the step. To discover how much time each step will take for your environment, we recommend that you perform trial upgrades in a test environment. For more information, see Use a trial upgrade to SharePoint 2013 to find potential issues.

Important

The steps in this article apply to both SharePoint Foundation 2013 and SharePoint 2013, except for the steps about how to upgrade the service applications, which apply mostly to SharePoint 2013 (the Business Data Connectivity service application applies to both).

Prepare for upgrade

## Prepare for upgrade

Follow these steps in order before you start an upgrade to SharePoint 2013:

Pre-upgrade steps

### Pre-upgrade steps

| Step | Notes |
| --- | --- |
| **Create an inventory of server-side customizations in the environment** 
 Create an inventory of the server-side customizations in your environment (solutions, features, Web Parts, event handlers, master pages, page layouts, CSS files, and so on). Record all customizations needed for your environment in the upgrade worksheet. 
 Detailed steps: Identify and install customizations in the "Use a trial upgrade to find potential issues" article. | Complete this step for the whole environment. Check each web server to make sure that you don't miss any customizations. Keep the inventory up to date as you prepare for the upgrade. |
| **Clean up your environment** 
 Before you begin to upgrade, make sure that your environment is functioning in a healthy state and that you clean up any content that you do not have to upgrade. Clean up any orphaned sites or data, address any large lists and large ACLs, remove extraneous document versions, and remove any unused templates, features and Web Parts. 
 Detailed steps: Clean up an environment before an upgrade to SharePoint 2013. | Complete this step one time for the whole environment. 
 This process might take days or weeks to finish. |
| **Test the upgrade process** 
 Try out upgrade in a test environment to find any issues and determine how long your actual upgrade might take. 
 Detailed steps: Use a trial upgrade to SharePoint 2013 to find potential issues | Perform this step multiple times, until you are prepared to perform the actual upgrade. |

Complete the database attach upgrade

## Complete the database attach upgrade

Follow these steps in order while you upgrade the content and service application databases for your environment.

Prepare the new environment

### Prepare the new environment

| Step | Notes |
| --- | --- |
| **Install and configure SharePoint 2013 and any language packs** 
 Install the prerequisite software, and then install and configure SharePoint 2013. | Complete these steps on each server in your farm. 
 This step might take one hour or more, depending on the number of servers are in your environment. |
| **Configure service applications** 
 Enable and configure the services that you need in your new environment. 
 Do not configure the following service applications - you will configure them while you upgrade their databases later in the process: 
 Business Data Connectivity service 
 Managed Metadata service 
 PerformancePoint services 
 Search 
 Secure Store service 
 User Profile service | Complete this step one time for the whole environment. |
| **Configure general farm settings** 
 Reapply any general farm settings that you must have from your previous farm — such as blocked file types, e-mail setting, and quota settings — and add users or groups to the Farm Administrators group. Configure new settings such as usage and health data collection, diagnostic logging, and mobile accounts. | Complete this step one time for the whole environment. |

Important

If you had disabled the Workflow Auto Cleanup timer job in your SharePoint 2013 environment, make sure that you disable this timer job in your new environment also. If this timer job is enabled in the new environment and disabled in the previous version environment, you might lose workflow associations when you upgrade. For more information about this timer job, see Disable preservation of workflow history (SharePoint Server 2010).

Detailed steps for this phase: Create the SharePoint 2013 farm for a database attach upgrade.

Back up and restore databases

### Back up and restore databases

| Step | Notes |
| --- | --- |
| **Record the passphrase for the Secure Store service application** 
 The Secure Store service application uses a passphrase to encrypt information. You must record this passphrase so that you can use it in the new environment. | Complete this step one time for each Secure Store service application in the environment. |
| **Set the previous version databases to be read-only** 
 If you want your original environment to remain available to users in a read-only state, set the databases to read-only before you back them up. | Complete this step for each content database in your environment. 
 Depending on your organization, you might need a database administrator to complete this step. |
| **Back up databases** 
 Back up all the content databases and the following service application databases before you begin the database attach upgrade process: 
 Business Data Connectivity 
 Managed Metadata 
 PerformancePoint 
 Search Administration 
 Secure Store 
 User Profile: Profile, Social, and Sync databases | Complete this step for each content database and supported service application database in your environment. 
 This step can take an hour, several hours, or longer, depending on your dataset and your environment. 
 Depending on your organization, you might need a database administrator to complete this step. |
| **Export the encryption key for the User Profile service application** 
 The User Profile service application requires an encryption key that is stored separately from the database and is needed if you want to upgrade the User Profile Sync database. | Complete this step one time for each User Profile service application in the environment. |
| **Restore a backup copy of the databases** 
 Restore the databases from the backup. | Complete this step for each content database and supported service application database in your environment. 
 This step can take an hour or longer, depending on your dataset and your environment. 
 Depending on your organization, you might need a database administrator to complete this step. |
| **Set the restored databases to be read-write** 
 Before you can attach and upgrade the databases that you copied to the new environment, you must set them to read-write. | Complete this step for each content database and supported service application database in your environment. 
 Depending on your organization, you might need a database administrator to complete this step. |

Detailed steps for this phase: Copy databases to the new farm for upgrade to SharePoint 2013

Upgrade service application databases

### Upgrade service application databases

| Step | Notes |
| --- | --- |
| **Start the service application instances** 
 Start the following service instances from Central Administration: 
 Business Data Connectivity service 
 Managed Metadata service 
 PerformancePoint services 
 Secure Store service 
 User Profile service 
 Start the instance of the Search service application by using PowerShell. | Complete this step one time for the whole environment. |
| **Upgrade the Secure Store service application** 
 Use PowerShell to create the new service application and upgrade the database, create a proxy and add it to the default proxy group, and then restore the passphrase from the previous environment. | Complete this step one time for each Secure Store service application in the previous environment. |
| **Upgrade the Business Data Connectivity service application** 
 Use PowerShell to create the new service application and upgrade the database. You do not have to create a proxy for the Business Data Connectivity service application. 

**NOTE** 
The Business Data Connectivity service application is available in both SharePoint Foundation 2013 and SharePoint 2013. | Complete this step one time for each Business Data Connectivity service application in the previous environment. |
| **Upgrade the Managed Metadata service application** 
 Use PowerShell to create the new service application and upgrade the database, and then create a proxy and add it to the default proxy group. You must upgrade the Managed Metadata service application before you can upgrade the User Profile service application. | Complete this step one time for each Managed Metadata service application in the previous environment. |
| **Upgrade the User Profile service application** 
 Use PowerShell to create the new service application and upgrade the database, and then create a proxy and add it to the default proxy group. After you have created the User Profile service application, you must import the Microsoft Identity Integration Server Key (MIIS) encryption key. Finally, you can start the User Profile Synchronization service. | Complete this step one time for each User Profile service application in the previous environment. |
| **Upgrade the PerformancePoint Services service application** 
 Use PowerShell to create the new service application and upgrade the database, and then create a proxy and add it to the default proxy group. | Complete this step one time for each PerformancePoint Services service application in the previous environment. |
| **Upgrade the Search service application** 
 Use PowerShell to create the new service application and upgrade the database, and then create a proxy and add it to the default proxy group. 
 > [!NOTE]> This step applies to only SharePoint 2013. Although SharePoint Foundation 2013 includes search functionality, it is not the same Search service application that is in SharePoint 2013 and it cannot be upgraded. | Complete this step one time for each Search service application in the previous environment. |
| **Verify that all of the new proxies are in the default proxy group** 
 Use the **Get-SPServiceApplicationProxyGroup** cmdlet to verify that all of the service application proxies are in the default proxy group. | Complete this step one time for the whole environment. |

Detailed steps for this phase: Upgrade service applications to SharePoint 2013.

Create web applications

### Create web applications

| Step | Notes |
| --- | --- |
| **Create and configure web applications** 
 Create a web application for each web application that existed in the old environment. If the desire is to use Windows Claims Authentication, create the new Web Applications in Windows Claims mode instead of Classic mode. | Complete this step one time for the whole environment. |
| **Reapply server-side customizations** 
 Manually transfer all server-side customizations to your new farm. Refer to the inventory that you created in the upgrade worksheet to make sure that you install all components that your sites depend on to work correctly. When you install solutions, make sure that you add it to the appropriate path (/14 or /15). If you want a solution to be available to both paths, install it two times, and the second time use the **CompatibilityLevel** parameter when you install it, and it will be installed to the /15 path. | Make sure that you reapply customizations to all web servers in the farm. |
| **Verify custom components** 
 Use the **Test-SPContentDatabase** Microsoft PowerShell cmdlet to verify that you have all the custom components that you need for that database. | Complete this step for each content database in your environment.  
 Running the cmdlet takes only a few minutes, but addressing issues might take longer. |

Detailed steps for this phase: Upgrade content databases from SharePoint 2010 to SharePoint 2013.

Attach and upgrade content databases

### Attach and upgrade content databases

| Step | Notes |
| --- | --- |
| **Attach a content database to a web application** 
 Attach the content database that contains the root site collection first. For My Sites, attach the content database that contains the My Site host before attaching databases that contain the My Sites. 
 You must perform this action from the command line. Use the **Mount-SPContentDatabase** Microsoft PowerShell cmdlet. | Complete this step for one content database in your environment. 
 This step might take several minutes or several hours, depending on your dataset and hardware on the web servers, database servers, and storage subsystem. |
| **Verify upgrade for the first database** 
 Verify that upgrade succeeded for the first database, and review the site to see whether there are any issues. 
 Detailed steps: Verify database upgrades in SharePoint 2013. | Complete this step for the content database that you just attached. |
| ****Attach remaining databases**** 
 Attach and upgrade the remaining content databases in your environment. You must complete this action from the command line. | Complete this step for each of the remaining content databases in your environment. 
 This step might take several minutes or several hours, depending on your dataset, whether you are upgrading multiple databases in parallel, and the hardware on the web servers, database servers, and storage subsystem. |
| **Monitor upgrade progress** 
 Use the Upgrade Status page in the SharePoint Central Administration website to monitor progress as your databases are upgraded. 
 Detailed steps: Verify database upgrades in SharePoint 2013. | Complete this step for each content database that you upgrade. 
 This step might take several minutes, an hour, several hours, or days, depending on your content. |
| **Verify upgrade for the remaining database** 
 Verify that upgrade succeeded for the remaining databases. 
 Detailed steps: Verify database upgrades in SharePoint 2013. | Complete this step for each of the remaining content databases in your environment. 
 This step might take several minutes, an hour, several hours, or days, depending on your content. |

Detailed steps for this phase: Upgrade content databases from SharePoint 2010 to SharePoint 2013.

Complete post-upgrade steps

## Complete post-upgrade steps

Follow these steps in order after you perform a database-attach upgrade.

Post upgrade steps for database attach upgrade

### Post upgrade steps for database attach upgrade

| Step | Notes |
| --- | --- |
| **Verify that site collections are working as expecting in 2010 mode** 
 Review the site collections and make sure that they work in 2010 mode before you begin to upgrade any site collections. You can use a similar review list as the one provided for upgraded sites in Review site collections upgraded to SharePoint 2013 
 > [!NOTE]> If the SharePoint 2013 Web Application was created in Windows Claims mode, complete the next step prior to testing site collections. | Complete this step one time for your whole environment. |
| **Migrate user accounts to claims authentication, if it is necessary** 
 By default, new web applications in SharePoint 2013 use claims authentication. If you were using classic authentication in the previous environment, you must migrate the users to claims authentication. For more information, see Migrate from classic-mode to claims-based authentication in SharePoint 2013. | Complete this step one time for every web application that has changed authentication methods. |
| **Update links that are used in any upgraded InfoPath form templates** 
 For a database-attach upgrade, you exported and imported all InfoPath form templates in your environment when you created the new environment. After upgrade, you can now update the links that are used in those upgraded form templates to point to the correct URLs by using a Microsoft PowerShell cmdlet. 
 For more information, see Configure InfoPath Forms Services (SharePoint Server 2010). | Complete this step one time for your whole environment. |
| **Configure your Search topology** 
 The architecture for the Search service has changed for SharePoint 2013. Plan and configure your Search topology to suit your environment and the new architecture. For more information, see Scale search for Internet sites in SharePoint Server and Manage the search topology in SharePoint Server. | Complete this step one time for your whole environment. |
| **Start a full crawl** 
 After all content is upgraded and all settings are configured, you can start a full search crawl of your content. For more information, see Start, pause, resume, or stop a crawl in SharePoint Server. | Complete this step one time for your whole environment. 
 A full crawl can take several hours or days to complete, depending on how much content is in your environment. |
| **Back up your farm** 
 Back up your farm so that you have a current backup of your upgraded environment before you start to upgrade site collections. For more information, see Back up farms in SharePoint Server. | Complete this step one time for your whole environment. |

See also

## See also

Other Resources

### Other Resources

Create the SharePoint 2013 farm for a database attach upgrade

Copy databases to the new farm for upgrade to SharePoint 2013

Upgrade service applications to SharePoint 2013

Upgrade content databases from SharePoint 2010 to SharePoint 2013

Overview of the upgrade process from SharePoint 2010 to SharePoint 2013

Upgrade a site collection to SharePoint 2013

Test and troubleshoot an upgrade to SharePoint 2013

Additional resources

## Additional resources

- Last updated on 
		2023-01-26
