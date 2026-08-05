---
title: "Core infrastructure documentation — pages 2601-2640"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p2601-2640
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p2601-2640
family: sccm
documentKind: "doc"
abstract: "4. On the General page, enter a name for the new software family and, optionally, a description. ７ Note The validation state for all new custom software labels is always set to User Defined. 5. On the Summary page, review the settings, and then click Next. 6. On the Completion p"
---

# Core infrastructure documentation — pages 2601-2640

<!-- p.2601 -->

   4. On the General page, enter a name for the new software family and, optionally, a
     description.

       ７ Note

       The validation state for all new custom software labels is always set to User
       Defined.

   5. On the Summary page, review the settings, and then click Next.

   6. On the Completion page, click Close to exit the wizard.

Hardware requirements
Hardware requirements information can help you verify that computers meet the
hardware requirements for software titles before they are targeted for software
deployments. Many hardware requirements are predefined in the Asset Intelligence
catalog, and you can create new user-defined hardware requirement information to
meet custom requirements. The validation state for all predefined hardware
requirements is always Validated, while user-defined hardware requirements
information added to the Asset Intelligence catalog is User Defined.

  ） Important

  The hardware requirements displayed in the Configuration Manager console are
  retrieved from the Asset Intelligence catalog on the local computer and are not
  based on inventoried software title information from System Center 2012
  Configuration Manager clients. Hardware requirements information is not updated
  as part of the synchronization process with System Center Online. You can create
  user-defined hardware requirements for inventoried software that does not have
  associated hardware requirements.

Use the following procedure to create a user-defined hardware requirement.

To create a user-defined hardware requirements

   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, click Asset Intelligence, and then click
     Hardware Requirements.

<!-- p.2602 -->

   3. On the Home tab, in the Create group, click Create Hardware Requirements.

   4. On the General page, enter the following information:

      a. Software title: Specifies the software title for which the hardware requirements
        are associated. The software title cannot already exist in the Asset Intelligence
        catalog.

     b. Validation state: Lists the validation state as User Defined for the hardware
        requirements. You cannot modify this setting.

      c. Minimum CPU (MHz): Specifies the minimum processor speed, in megahertz
        (MHz), required by the software title.

     d. Minimum RAM (KB): Specifies the minimum RAM, in kilobytes (KB), required by
        the software title.

      e. Minimum Disk Space (KB): Specifies the minimum free disk space, in KB,
        required by the software title.

      f. Minimum Disk Size (KB): Specifies the minimum hard disk size, in KB, required
        by the software title.

        Click Next.

   5. On the Summary page, review the settings, and then click Next.

   6. On the Completion page, click Close to exit the wizard.

Modify categorization information for inventoried
software
Predefined software in the Asset Intelligence catalog is configured with specific
categorization information, such as product name, vendor, software category, and
software family. When the predefined categorization information does not meet your
requirements, you can modify the information in the properties for the software title.
When you modify categorization information for predefined software, the validation
state for the software changes from Validated to User Defined.

  ） Important

  The categorization information can only be modified at the top-level site.

<!-- p.2603 -->

Use the following procedure to modify categorization information for inventoried
software.

To modify the categorizations for software titles

   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, click Asset Intelligence, and then click
     Inventoried Software.

   3. Select a software title or select multiple software titles for which you want to
     modify categorizations.

   4. On the Home tab, in the Properties group, click Properties.

   5. On the General tab, you can modify the following categorization information:

            Product Name: Specifies the name of the inventoried software title.

            Vendor: Specifies the name of the vendor that developed the inventoried
            software title.

            Category: Specifies the software category that is currently assigned to the
            inventoried software title.

            Family: Specifies the software family that is currently assigned to the
            inventoried software title.

   6. Click OK to save the changes.

     Use the following procedure to revert software to the original categorization
     information.

Revert categorization information to original settings for
software
Configuration Manager stores categorization information obtained from System Center
Online in the database. The information cannot be deleted. After the information has
been modified, you can revert the categorization information back to the System Center
Online categorization. Inventoried software that is not in the Asset Intelligence catalog
can also be reverted back to the original settings.

Use the following procedure to revert categorization information to the original settings.

<!-- p.2604 -->

To revert categorization information to original settings

   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, click Asset Intelligence, and then click
     Inventoried Software.

   3. Select a software title or select multiple software titles that you want to revert to
     the original settings. Only software that has a User Defined state can be reverted.

         Tip

        Click the State column to sort by the validation state. Sorting lets you see all
        software by validation state and quickly select multiple items to revert to the
        original settings.

   4. On the Home tab, in the Product group, click Revert.

   5. Click Yes to revert the software to the original categorization information.

   6. When you revert categorization information for software that is in the Asset
     Intelligence catalog, the validation state changes from User Defined to Validated.
     When you revert software that is not in the catalog, the validation state changes
     from User Defined to Uncategorized.

Request a catalog update for uncategorized
software titles
Uncategorized software title information can be submitted to System Center Online for
research and categorization. After an uncategorized software title is submitted, and
there are at least 4 categorization requests from customers for the same software title,
researchers identify, categorize, and then make the software title categorization
information available to all customers that are using the System Center Online service.
Microsoft gives the highest priority to software titles that have the most requests for
categorization. Custom software and line-of-business applications are unlikely to receive
a category, and as a best practice, you should not send these software titles to Microsoft
for categorization.

When software title information is submitted to System Center Online for categorization,
the following conditions apply:

<!-- p.2605 -->

     Only basic software title information is transmitted to System Center Online, and
     software title information to be categorized can be reviewed before submission.

     Software license information is never transmitted.

     Any software title that is uploaded becomes publicly available as part of the
     System Center Online catalog and can be downloaded by other customers.

     The source of the software title is not stored in the System Center Online catalog.
     However, application titles containing confidential or proprietary information
     should not be submitted for categorization by System Center Online.

  ７ Note

  For more information about Asset Intelligence privacy information, see Security
  and privacy for Asset Intelligence.

Use the following procedure to request Asset Intelligence catalog software title
categorization from System Center Online.

To request a catalog update for uncategorized software titles
   1. In the Configuration Manager console, click Assets and Compliance.

   2. In the Assets and Compliance workspace, click Asset Intelligence, and then click
     Inventoried Software.

   3. Select a product name or select multiple product names, to be submitted to
     System Center Online for categorization. Only uncategorized inventoried software
     titles can be submitted to System Center Online for categorization. If an
     inventoried software title has been categorized by an administrator resulting in a
     user-defined state, you must right-click the inventoried software title, and then
     click Revert to revert the software title to the Uncategorized state before it can be
     submitted to System Center Online for categorization.

       ７ Note

       Configuration Manager can process up to 2000 software titles for
       categorization at a time. If you select more than 2000 software titles, only the
       first 2000 software titles will be processed. You must select the remaining
       software titles for categorization in batches of less than 2000.

<!-- p.2606 -->

         Tip

        Click the State column to sort by the validation state. This lets you see all
        uncategorized product names and quickly select multiple items to submit for
        categorization.

   4. On Home tab, in the Product group, click Request Catalog Update.

   5. Review the System Center Online categorization submission privacy message. Click
     Details to view the information that will be sent to System Center Online.

   6. Select I have read and understood this message, and then click OK to allow the
     selected software titles to be submitted for categorization.

   7. Verify that the state of the inventoried software product names submitted to
     System Center Online for categorization has changed from Uncategorized to
     Pending.

        ７ Note

        Software that is submitted to System Center Online for categorization has a
        validation state of Pending on a central administration site is still displayed
        with a validation state of Uncategorized on child primary sites.

Resolve software details conflicts
After newly updated software categorization details have been received from System
Center Online that conflict with existing software details information, you can choose
how to resolve the conflict. Software that has a current conflict has a validation state of
Updatable. After a software details conflict has been resolved, the software
categorization information is retained in the Asset Intelligence catalog according to the
setting that you specify. A software details conflict does not occur for the same software
categorization value again unless the System Center Online value changes after the
conflict has been resolved.

Use the following procedure to resolve a software details conflict.

To resolve a software details conflict

   1. In the Configuration Manager console, click Assets and Compliance.

<!-- p.2607 -->

   2. In the Assets and Compliance workspace, click Asset Intelligence, and then click
     Inventoried Software.

   3. Review the State column for software titles in the Updatable state.

   4. Select the software title for which you have to resolve a conflict, and then on the
     Home tab, in the Product group, and click Resolve Conflict.

   5. Review the following information:

           Local value: Specifies the existing software categorization information in the
           Asset Intelligence catalog that conflicts with newer System Center Online
           software categorization details.

           Downloaded value: Specifies the new System Center Online software
           categorization information for conflicting Asset Intelligence catalog software
           categorization information.

   6. Select one of the following settings to resolve the software details conflict:

           Do not change the locally edited catalog information value: Resolves the
           software details conflict by retaining the existing Asset Intelligence catalog
           software categorization information. When you select this setting, the
           software title state changes from Updatable to User Defined.

           Overwrite the locally edited catalog information value with the
           downloaded System Center Online value: Resolves the software details
           conflict by overwriting the existing Asset Intelligence catalog software
           categorization information with new information obtained from System
           Center Online. When you select this setting, the software title state changes
           from Updatable to Validated.

           Click OK to save the conflict resolution.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2608 -->

Security and privacy for Asset
Intelligence in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article contains security guidance and privacy information for Asset Intelligence in
Configuration Manager.

Security guidance

Secure license files
When you import a Microsoft Volume Licensing file or a General License Statement file,
secure the file and communication channel. Configure NTFS permissions to make sure
that only authorized users can access the license files. Use Server Message Block (SMB)
signing to keep the integrity of the data when it's transferred to the site server during
the import process.

Limit permissions for users who import license files
Use the principle of least permissions to import the license files. Use role-based
administration to grant the Manage Asset Intelligence permission to the administrative
user who imports license files. The built-in role of Asset Manager includes this
permission.

Privacy information
Asset Intelligence extends the inventory capabilities of Configuration Manager to
provide a higher level of asset visibility. Asset Intelligence information collection isn't
automatically enabled. You can modify the type of information collected by enabling
hardware inventory reporting classes. For more information, see Configure Asset
Intelligence.

Configuration Manager stores Asset Intelligence information in the site database the
same as inventory information. When clients connect to management points by using
HTTPS, the data is always encrypted during transfer to the management point. When
clients connect by using HTTP, configure the inventory data transfer to be signed and

<!-- p.2609 -->

encrypted. Inventory data isn't stored in an encrypted format in the database.
Information is kept in the database until the site maintenance task Delete Aged
Inventory History deletes it every 90 days by default. You can configure the deletion
interval.

Asset Intelligence doesn't send information about users, computers, or license usage to
Microsoft. You can choose to send System Center Online requests for categorization. For
these requests, you tag one or more uncategorized software titles and send them to
Microsoft for research and categorization. After you upload a software title, Microsoft
researchers identify and categorize the software. They then make that information
available to all customers who use the online service.

When you submit information to System Center Online, understand the following
privacy implications:

      Upload applies only to generic software title information that you choose to send
      to Microsoft. For example, software name and publisher. Inventory information
      isn't sent to Microsoft.

      Upload never occurs automatically, and the system isn't designed for this task to
      be automated. Manually select and approve the upload of each software title.

      Before the upload process starts, the Configuration Manager console shows you
      exactly what data it will upload.

      License information isn't sent to Microsoft. Configuration Manager stores the
      license information in a separate area of the site database, and it can't be sent to
      Microsoft.

      Any software title that you upload becomes public. The knowledge of that
      software and its categorization become part of the online Asset Intelligence
      catalog. Other customers can then download the catalog updates.

      The source of the software title isn't recorded in the Asset Intelligence catalog, and
      it isn't made available to other customers. Still verify that you don't include any
      application titles that contain any private information.

      You can't recall uploaded data.

Feedback
Was this page helpful?    Yes     No

<!-- p.2610 -->

Provide product feedback

<!-- p.2611 -->

Example validation state transitions for
Asset Intelligence
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Asset Intelligence validation states in Configuration Manager aren't static and can
change from administrative actions that you take to affect the data that are stored in the
Asset Intelligence catalog. This topic provides examples for possible validation state
transitions.

Uncategorized catalog item is categorized by
the administrative user
                                                                                  ﾉ   Expand table

 State transition       State transition description

 Uncategorized          An inventoried software title that hasn't been previously categorized by
                        System Center Online or that the administrative user has entered into the
                        Asset Intelligence catalog.

 Uncategorized to       The uncategorized item is categorized by the administrative user.
 UserDefined

Categorized catalog item is recategorized by
the administrative user
                                                                                  ﾉ   Expand table

 State transition      State transition description

 Validated             Catalog item has been defined by System Center Online researchers and is
                       present in the Asset Intelligence catalog.

 Validated to User     The validated catalog item is re-categorized by the administrative user.
 Defined

  ７ Note

<!-- p.2612 -->

 Because categorization information obtained from System Center Online is stored
 in the database and cannot be deleted, the administrative user can revert back to
 the System Center Online categorization later.

User-defined catalog item is recategorized by
System Center Online
                                                                               ﾉ   Expand table

State transition   State transition description

Uncategorized      An inventoried software title is entered into the Asset Intelligence catalog
                   that hasn't been previously categorized by System Center Online or the
                   administrative user.

User Defined       The uncategorized item is categorized by the administrative user.

User Defined to    A user-defined catalog item has been categorized differently by System
Updateable         Center Online during subsequent manual bulk updates of the Asset
                   Intelligence catalog.

                   The administrative user can use the Software Details Conflict Resolution
                   dialog box to decide whether to use the new categorization information or
                   the previous user-defined value.

Updateable to      The administrative user uses the Software Details Conflict Resolution
Validated          dialog box to use the new categorization information received from System
                   Center Online during the previous catalog update.

or

Updateable to      The administrative user uses the Software Details Conflict Resolution
User Defined       dialog box to use the previous user-defined value.

 ７ Note

 Because categorization information obtained from System Center Online is stored
 in the database and cannot be deleted, the administrative user can revert back to
 the System Center Online categorization later.

Uncategorized catalog item is submitted to
System Center Online for categorization

<!-- p.2613 -->

                                                                                ﾉ   Expand table

State transition   State transition description

Uncategorized      An inventoried software title is entered into the Asset Intelligence database
                   that hasn't been previously categorized by System Center Online or the
                   administrative user.

Uncategorized      The uncategorized item is submitted to System Center Online for
to Pending         categorization by the administrative user.

Pending to         The item is categorized by System Center Online. The administrative user
Validated          imports the item into the Asset Intelligence catalog by using a bulk catalog
                   update or Asset Intelligence catalog synchronization. Both are available by
                   using the Asset Intelligence synchronization point site system role.

User-defined catalog item is submitted to
System Center Online for categorization
                                                                                ﾉ   Expand table

State transition   State transition description

Uncategorized      An inventoried software title is entered into the Asset Intelligence database
                   that hasn't been previously categorized by an administrative user or System
                   Center Online.

User Defined       You categorized the uncategorized item.

User Defined to    You submit the user-defined item to System Center Online for categorization.
Pending

Pending to         A user-defined catalog item has been categorized differently by System
Updateable         Center Online during subsequent catalog synchronization. You can use the
                   Resolve Conflict action to decide whether to use the new categorization
                   information or the previous user-defined value. For more information about
                   resolving conflicts, see Resolve software details conflicts.

Updateable to      You use the Resolve Conflict action and select the new categorization
Validated          information received from System Center Online during the previous catalog
                   update. For more information about resolving conflicts, see Resolve software
                   details conflicts.

or

Updateable to      You use the Resolve Conflict action and select to use the previous user-
User Defined       defined value. For more information about resolving conflicts, see Resolve
                   software details conflicts.

<!-- p.2614 -->

  ７ Note

  Because categorization information obtained from System Center Online is stored
  in the database and cannot be deleted, you can revert back to the System Center
  Online categorization later.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2615 -->

Example Asset Intelligence general license import file
in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The example information in this topic can be used to create a sample general software license file to import software licenses into the Asset
Intelligence catalog by using the Import Software License Wizard. You can copy and paste the following table into a new Microsoft Excel
spreadsheet and save it with a .csv file name extension to be used as an example general software license import file for testing purposes.
When creating the license import file, all header fields are required while only Name, Publisher, Version, and EffectiveQuantity data values
are required in the spreadsheet. For more information about importing software licenses to the Asset Intelligence catalog, see Configuring
Asset Intelligence.

                                                                                                                             ﾉ   Expand table

 Name       Publisher    Version   Language   EffectiveQuantity   PONumber   ResellerName    DateOfPurchase   SupportPurchased   SupportExpirationDate

 Software   Software     1.01      English    1                   Purchase   Reseller name   10/10/2010       0                  10/10/2012
 Title 1    publisher                                             number

 Software   Software     1.02      English    1                   Purchase   Reseller name   10/10/2010       0                  10/10/2012
 title 2    publisher                                             number

 Software   Software     1.03      English    1                   Purchase   Reseller name   10/10/2010       0                  10/10/2012
 title 3    publisher                                             number

 Software   Software     1.04      English    1                   Purchase   Reseller name   10/10/2010       0                  10/10/2012
 title 4    publisher                                             number

 Software   Software     1.05      English    1                   Purchase   Reseller name   10/10/2010       0                  10/10/2012
 title 5    publisher                                             number

 Software   Software     1.06      English    1                   Purchase   Reseller name   10/10/2010       0                  10/10/2012
 title 6    publisher                                             number

 Software   Software     1.07      English    1                   Purchase   Reseller name   10/10/2010       0                  10/10/2012
 title 7    publisher                                             number

 Software   Software     1.08      English    1                   Purchase   Reseller name   10/10/2010       0                  10/10/2012
 title 8    publisher                                             number

 Software   Software     1.09      English    1                   Purchase   Reseller name   10/10/2010       0                  10/10/2012
 title 9    publisher                                             number

 Software   Software     1.10      English    1                   Purchase   Reseller name   10/10/2010       0                  10/10/2012
 title 10   publisher                                             number

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.2616 -->

Manage Microsoft Lifecycle Policy with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the Configuration Manager product lifecycle dashboard to view the Microsoft
Lifecycle Policy. The dashboard shows the state of the Microsoft Lifecycle Policy for
Microsoft products installed on devices managed with Configuration Manager. It also
provides you with information about Microsoft products in your environment,
supportability state, and support end dates. Use the dashboard to understand the
availability of support for each product. This information helps you plan for when to
update the Microsoft products you use before their current end of support is reached.

For more information, see the Microsoft Lifecycle Policy.

Prerequisites
To see data in the product lifecycle dashboard, the following components are required:

      Install Internet Explorer 9 or later on the computer that runs the Configuration
      Manager console.

      To get updates for the data on this dashboard, the service connection point must
      be online. If the service connection point is in offline mode, synchronize it
      regularly. For more information, see About the service connection point.

      In version 2111 and earlier: Configure and synchronize the asset intelligence
      synchronization point. The dashboard uses the asset intelligence catalog as
      metadata for product titles. Configuration Manager compares this metadata
      against inventory data in your hierarchy. For more information, see Configure asset
      intelligence in Configuration Manager.

        ７ Note

        Starting in version 2203, the product lifecycle dashboard isn't dependent on
        the asset intelligence synchronization point.

      Enable asset intelligence hardware inventory classes. The lifecycle dashboard
      depends on these classes. The dashboard won't display data until clients scan for

<!-- p.2617 -->

     and return hardware inventory.

Use the product lifecycle dashboard
To access the lifecycle dashboard in the Configuration Manager console, go to the
Assets and Compliance workspace, expand Asset Intelligence, and select the Product
Lifecycle node.

Based on inventory data the site collects from managed devices, the dashboard displays
information about all current products. However, the information displayed for
operating systems and SQL Server is limited to the following versions:

     Windows Server 2008 and later
     Windows XP and later
     SQL Server 2008 and later

  ７ Note

  The data in the dashboard is based on the site the Configuration Manager console
  connects to. If the console connects to your top-tier site, you see data for the entire
  hierarchy. When connected to a child primary site, only data from that site displays.

Product lifecycle dashboard

<!-- p.2618 -->

                                                                                       

Change the view by selecting one of the following options from the Product category
list:

        All: View all products together
        Windows Client: View Windows client OS versions
        Windows Server: View Windows server OS versions
        Database: View SQL Server versions
        Configuration Manager: View Configuration Manager versions
        Microsoft Office: View information for installed versions of Office 2003 through
        Office 2016

The dashboard has the following tiles:

        Top 5 products past end-of-support: This tile is a consolidated data view of
        products found in your environment past their end-of-support. The graph shows
        installed software that's expired when compared against the support lifecycle for
        operating systems and SQL Server products.

        Top 5 products nearing end-of-support: This tile is a consolidated data view of
        products found in your environment that are nearing end-of-support in next 18
        months. The graph shows installed software that's within 18 months of end-of-
        support when compared against the support lifecycle for operating systems and
        SQL Server products.

<!-- p.2619 -->

     Starting in version 2103, use the time slider to control the timeframe for this tile.
     The default is 18 months, but you can adjust it from 1 to 36 months.

     Lifecycle data for installed products: This tile gives you a general idea of when a
     product transitions from supported to the expired state. The chart provides a
     breakdown of the number of clients where the product is installed, the support
     availability state, and a link to learn more about the next steps to take. The
     following information is included in the chart:
        Support time remaining
        Number in environment
        Mainstream support end date
        Extended support end date
        Next steps

Starting in version 2103, the dashboard also has a subnode, All Product Lifecycle Data.
You can sort and filter the product lifecycle information, which gives you multiple ways
to view it. When you select a product, you can View devices for that product. From the
list of devices, you can create a direct membership collection. Use this action to deploy
the latest software versions to these collections so that the devices are kept current.

  ） Important

  The information shown in this dashboard is provided for your convenience and
  only for use internally within your company. You should not solely rely on this
  information to confirm compliance. Be sure to verify the accuracy of the
  information provided to you, along with availability of support information by
  visiting the Microsoft Lifecycle Policy.

<!-- p.2620 -->

Reporting
Other reports are available as well. In the Configuration Manager console, go to the
Monitoring workspace, expand Reporting, and expand Reports. The following reports
are added under the category Asset Intelligence:

     Lifecycle 01A - Computers with a specific software product: View a list of
     computers on which a specified product is detected.

     Lifecycle 02A - List of machines with expired products in the organization: View
     computers that have expired products on them. You can filter this report by
     product name.

     Lifecycle 03A - List of expired products found in the organization: View details
     for products in your environment that have expired lifecycle dates.

     Lifecycle 04A - General Product Lifecycle overview: View a list of product
     lifecycles. Filter the list by product name and days to expiration.

     Lifecycle 05A - Product lifecycle dashboard: This report includes similar
     information as the in-console dashboard. Select a category to view the count of
     products in your environment, and the days of support remaining.

For more information, see List of reports.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2621 -->

Asset intelligence deprecation
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Starting in November 2021, the asset intelligence feature of Configuration Manager is
deprecated. This article provides more detail about the specific functional areas of asset
intelligence that are deprecated or still supported.

Deprecated functionality
The following functional areas are deprecated and may be removed in a future version.
Support for these areas will end November 2022.

      The asset intelligence catalog, which includes the following functionality:

         Cloud updates to the predefined software title information such as product
         name and vendor

         Cloud updates to the predefined software categories and software families and
         the associated SQL views and reports

         Cloud updates to the predefined hardware requirements for software titles and
         the associated SQL views and reports

      The asset intelligence synchronization point, which includes the following
      functionality:

         Catalog synchronization

         The ability to request catalog updates for uncategorized software

      The Microsoft Volume License import and reconciliation including the associated
      SQL views and reports

Supported functionality
The following functional areas aren't currently included in the deprecation and will
remain supported:

      The inventoried software titles, which includes the following functionality:

         Asset intelligence hardware inventory reporting WMI classes

<!-- p.2622 -->

        The associated SQL views:

           Asset intelligence hardware inventory views

           Asset intelligence status view

        The associated reports

     The product lifecycle dashboard and its associated reports

     The General License Statement import and reconciliation and the associated SQL
     views and reports

     The ability to view the asset intelligence inventory in the console from the
     Inventoried Software node

     The existing static, predefined software title information provided with setup for
     new and existing sites:
        Product name
        Vendor
        Product category
        Product family
        Hardware requirement

     The ability to customize the inventoried software title information such as the
     product name and vendor

     The ability to add custom software categories, families, and labels to inventoried
     software titles

     The ability for an administrator to add custom hardware requirements to
     inventoried software titles

References
Asset intelligence reports

Asset intelligence client WMI classes

Asset intelligence views

Feedback

<!-- p.2623 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2624 -->

Introduction to remote control in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use remote control to remotely administer, provide assistance, or view any client
computer in the hierarchy. You can use remote control to troubleshoot hardware and
software configuration problems on client computers and to provide support.
Configuration Manager supports the remote control of all workgroup computers and
domain-joined computers that run supported operating systems for the Configuration
Manager client. For more information, see Supported operating systems for clients and
devices for Configuration Manager

Configuration Manager also lets you configure client settings to run Windows Remote
Desktop and Remote Assistance from the Configuration Manager console.

  ７ Note

  You cannot establish a Remote Assistance session from the Configuration Manager
  console to a client computer that is in a workgroup.

You can start a remote control session in the Configuration Manager console from
Assets and Compliance > Devices, from any device collection, from the Windows
Command Prompt window, or from the Windows Start menu.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2625 -->

Prerequisites for remote control in
Configuration Manager
Article • 02/22/2023

Applies to: Configuration Manager (current branch)

Remote control in Configuration Manager has external dependencies and dependencies
in the product.

Dependencies external to Configuration
Manager
To help improve performance, install the most up-to-date video driver on client devices.

You can't use Configuration Manager remote control to remotely administer client
computers that run versions of the Configuration Manager client earlier than current
branch.

  ７ Note

  No Windows services are required as an external dependency for remote control.

Supported operating systems for the remote control
viewer
The remote control viewer is supported on all operating systems that are supported for
the Configuration Manager console. For information, see Supported configurations for
Configuration Manager consoles.

The following OS versions don't support the remote control viewer, but they do support
the remote control client:

      Windows Embedded
      Windows Embedded for Point of Service (POS)
      Windows Fundamentals for Legacy PCs

Configuration Manager dependencies

<!-- p.2626 -->

Enable remote control
By default, remote control isn't enabled when you install Configuration Manager. For
more information about how to enable and configure remote control, see Configure
remote control.

Reporting
Before you can run reports for remote control, install the reporting services point site
system role. For more information, see Introduction to reporting.

Security permissions
     To access collection resources and to start a remote control session from the
     Configuration Manager console, your account needs the Read, Read Resource, and
     Remote Control permissions for the Collection object.

     The Remote Tools Operator security role includes the permissions that are
     required to manage remote control in Configuration Manager.

     Permitted viewers must be given permission to use remote control by adding these
     users to the Permitted viewers of Remote Control and Remote Assistance list in
     the Remote Tools client settings.

For more information, see Configure role-based administration.

Remote clients
Remote tools aren't supported for clients that are connected remotely. For example, you
can't remote control a client that communicates with the site through a cloud
management gateway (CMG). For more information about the network ports required
for remote tools, see Ports used in Configuration Manager.

   Tip

  For tenant-attached devices, remote tools are available in the Microsoft Intune
  admin center. For more information, see Support for remote tools.

Next steps
Configure remote control

<!-- p.2627 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2628 -->

Configuring remote control in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This procedure describes configuring the default client settings for remote control.
These settings apply to all computers in your hierarchy. If you want these settings to
apply to only some computers, assign a custom device client setting to a collection that
contains those computers. For more information a see How to configure client settings.

To use Remote Assistance or Remote Desktop, it must be installed and configured on
the computer that runs the Configuration Manager console. For more information about
how to install and configure Remote Assistance or Remote Desktop, see your Windows
documentation.

To enable remote control and configure client settings

   1. In the Configuration Manager console, choose Administration > Client Settings >
      Default Client Settings.

   2. On the Home tab, in the Properties group, choose Properties.

   3. In the Default dialog box, choose Remote Tools.

   4. Configure the remote control, Remote Assistance and Remote Desktop client
      settings. For a list of remote tools client settings that you can configure, see
      Remote Tools.

      You can change the company name that appears in the ConfigMgr Remote
      Control dialog box by configuring a value for Organization name displayed in
      Software Center in the Computer Agent client settings.

      Client computers are configured with these settings the next time they download
      client policy. To initiate policy retrieval for a single client, see How to manage
      clients.

Enable keyboard translation

By default, Configuration Manager transmits the key position from the viewer's location
to the sharer's location. This can present a problem for keyboard configurations that

<!-- p.2629 -->

differ from viewer to sharer. For example, a viewer with an English keyboard would type
an "A", but the sharer's French keyboard would provide a "Q". You now have the option
of configuring remote control so that the character itself is transmitted from the viewer's
keyboard to the sharer, and what the viewer intends to type arrives at the sharer.

To turn on keyboard translation, in Configuration Manager Remote Control, choose
Action,and choose Enable keyboard translation to transmit key position.

  ７ Note

  Special keys, such as ~!#@$%, will not be translated correctly.

Keyboard shortcuts for the remote control
viewer
                                                                                ﾉ   Expand table

 Keyboard shortcut                     Description

 Alt+Page Up                           Switches between running programs from left to right.

 Alt+Page Down                         Switches between running programs from right to left.

 Alt+Insert                            Cycles through running programs in the order that they
                                       were opened.

 Alt+Home                              Displays the Start menu.

 Ctrl+Alt+End                          Displays the Windows Security dialog box (Ctrl+Alt+Del).

 Alt+Delete                            Displays the Windows menu.

 Ctrl+Alt+Minus Sign (on the           Copies the active window of the local computer to the
 numeric keypad)                       remote computer Clipboard.

 Ctrl+Alt+Plus Sign (on the numeric    Copies the entire local computer's window area to the
 keypad)                               remote computer Clipboard.

Feedback
Was this page helpful?    Yes         No

<!-- p.2630 -->

Provide product feedback

<!-- p.2631 -->

How to remotely administer a Windows
client computer by using Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager allows you to connect to client computers using Configuration
Manager Remote Control. Before you begin to use remote control, ensure that you
review the information in the following articles:

      Prerequisites for remote control

      Configuring remote control

Here are three ways to start the remote control viewer:

      In the Configuration Manager console.

      In a Windows command prompt.

      From the Windows Start menu, on a computer that runs the Configuration
      Manager console, in the Microsoft Endpoint Manager program group.

        ７ Note

        The above Start menu path is for versions from November 2019 (version 1910)
        or later. In earlier versions, the folder name is Microsoft System Center.

To remotely administer a client computer from
the Configuration Manager console
   1. In the Configuration Manager console, choose Assets and Compliance > Devices
      or Device Collections.

   2. Select the computer that you want to remotely administer and then, in the Home
      tab, in the Device group, choose Start > Remote Control.

        ） Important

<!-- p.2632 -->

    If the client setting Prompt user for Remote Control permission is set to True,
    the connection does not initiate until the user at the remote computer agrees
    to the remote control prompt. For more information, see Configuring remote
    control.

3. After the Configuration Manager Remote Control window opens, you can
  remotely administer the client computer. Use the following options to configure
  the connection.

    ７ Note

    If the computer that you connect to has multiple monitors, the display from
    all the monitors is shown in the remote control window.

       File
          Connect - Connect to another computer. This option is unavailable when a
          remote control session is active.
          Disconnect - Disconnects the active remote control session but doesn't
          close the Configuration Manager Remote Control window.
          Exit - Disconnects the active remote control session and closes the
          Configuration Manager Remote Control window.

         ７ Note

         When you disconnect a remote control session, the contents of the
         Windows Clipboard on the computer that you are viewing is deleted.

       View
          Color depth - Choose either 16 bits or 32 bits per pixel.
          Full Screen - Maximizes the Configuration Manager Remote Control
          window. To exit full screen mode, press Ctrl+Alt+Break.
          Optimize for low bandwidth connection - Choose this option if the
          connection is low bandwidth.
          Display:
               All Screens - If the computer that you connect to has multiple monitors,
               the display from all the monitors is shown in the remote control
               window.
               First Screen - The first screen is at the top and far left as shown in
               Windows display settings. You can't select a specific screen. When you

<!-- p.2633 -->

               switch the configuration of the viewer, reconnect the remote session.
               The viewer saves your preference for future connections.
               Scale to Fit - Scales the display of the remote computer to fit the size of
               the Configuration Manager Remote Control window.
               Status Bar - Toggles the display of the Configuration Manager Remote
               Control window status bar.

           ７ Note

           The viewer saves your preference for future connections.

        Action
           Send Ctrl+Alt+Del Key - Sends a Ctrl+Alt+Del key combination to the
           remote computer.
           Enable Clipboard Sharing - Lets you copy and paste items to and from the
           remote computer. If you change this value, you must restart the remote
           control session for the change to take effect.
               If you don't want clipboard sharing to be enabled in the Configuration
               Manager console, on the computer running the console, set the value
               of the registry key
               HKEY_CURRENT_USER\Software\Microsoft\ConfigMgr10\Remote
               Control\Clipboard Sharing to 0.
           Enable Keyboard Translation - Translates the keyboard layout of the
           computer running the console to the connected device's layout.
           Lock Remote Keyboard and Mouse - Locks the remote keyboard and
           mouse to prevent the user from operating the remote computer.

        Help
           About Remote Control - Displays the current version of the viewer.

 4. Users at the remote computer can view more information about the remote
   control session when they click the Configuration Manager Remote Control icon.
   The icon is in the Windows notification area or the icon on the remote control
   session bar.

To start the remote control viewer from the
Windows command line
   At the Windows command prompt, type <Configuration Manager Installation
   Folder>\AdminConsole\Bin\i386\CmRcViewer.exe

<!-- p.2634 -->

CmRcViewer.exe supports the following command-line options:

      Address - Specifies the NetBIOS name, the fully qualified domain name (FQDN), or

     the IP address of the client computer that you want to connect to.
      Site Server Name - Specifies the name of the Configuration Manager site server to

     which you want to send status messages that are related to the remote control
     session.
      /? - Displays the command-line options for the remote control viewer.

Example: CmRcViewer.exe <Address> <\\Site Server Name>

  ７ Note

  The remote control viewer is supported on all operating systems that are supported
  for the Configuration Manager console. For more information, see Supported
  configurations for Configuration Manager consoles and Prerequisites for remote
  control.

Next steps
Audit remote control usage

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2635 -->

How to audit remote control usage in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can use Configuration Manager reports to view audit information for remote
control.

For more information about how to configure reporting in Configuration Manager, see
Introduction to reporting.

The following two reports are available with the category Status Messages - Audit:

      Remote Control - All computers remote controlled by a specific user - Displays a
      summary of remote control activity that a specific user initiated.

      Remote Control - All remote control information - Displays a summary of status
      messages about remote control of client computers.

To run the report Remote Control - All computers remote
controlled by a specific user
   1. In the Configuration Manager console, click Monitoring.

   2. In the Monitoring workspace, expand Reporting, and then click Reports.

   3. In the Reports node, click the Category column to sort the reports so that you can
      more easily find the reports in the category Status Messages - Audit.

   4. Select the report Remote Control - All computers remote controlled by a specific
      user, and then, on the Home tab, in the Report Group, click Run.

   5. In the User Name list of the Remote Control - All computers remote controlled
      by a specific user, specify the user that you want to report audit information for,
      and then click View Report.

   6. When you have finished viewing the data in the report, close the report window.

To run the report Remote Control - All remote control
information

<!-- p.2636 -->

   1. In the Configuration Manager console, click Monitoring.

   2. In the Monitoring workspace, expand Reporting, and then click Reports.

   3. In the Reports node, click the Category column to sort the reports so that you can
     more easily find the reports in the category Status Messages - Audit.

   4. Select the report Remote Control - All remote control information, and then, on
     the Home tab, in the Report Group, click Run to open the Remote Control - All
     remote control information window.

   5. When you have finished viewing data in the report, close the report window.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2637 -->

Security and privacy for remote control
in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This topic contains security and privacy information for remote control in Configuration
Manager.

Security best practices for remote control
Use the following security best practices when you manage client computers by using
remote control.

                                                                                ﾉ   Expand table

 Security best practice          More information

 When you connect to a remote    When Configuration Manager detects that the remote control
 computer, do not continue if    session is authenticated by using NTLM instead of Kerberos,
 NTLM instead of Kerberos        you see a prompt that warns you that the identity of the remote
 authentication is used.         computer cannot be verified. Do not continue with the remote
                                 control session. NTLM authentication is a weaker authentication
                                 protocol than Kerberos and is vulnerable to replay and
                                 impersonation.

 Do not enable Clipboard         The Clipboard supports objects such as executable files and text
 sharing in the remote control   and could be used by the user on the host computer during the
 viewer.                         remote control session to run a program on the originating
                                 computer.

 Do not enter passwords for      Software that observes keyboard input could capture the
 privileged accounts when        password. Or, if the program that is being run on the client
 remotely administering a        computer is not the program that the remote control user
 computer.                       assumes, the program might be capturing the password. When
                                 accounts and passwords are required, the end user should enter
                                 them.

 Lock the keyboard and mouse     If Configuration Manager detects that the remote control
 during a remote control         connection is terminated, Configuration Manager automatically
 session.                        locks the keyboard and mouse so that a user cannot take
                                 control of the open remote control session. However, this
                                 detection might not occur immediately and does not occur if
                                 the remote control service is terminated.

<!-- p.2638 -->

Security best practice            More information

                                  Select the action Lock Remote Keyboard and Mouse in the
                                  ConfigMgr Remote Control window.

Do not let users configure        Do not enable the client setting Users can change policy or
remote control settings in        notification settings in Software Center to help prevent users
Software Center.                  from being spied on. If one user changes it, it can allow a
                                  different user on the same machine to be viewed remotely.

                                  This setting is for the computer, not for the logged-on user.

Enable the Domain Windows         Enable the client setting Enable remote control on clients
Firewall profile.                 Firewall exception profiles and then select the Domain
                                  Windows Firewall for intranet computers.

If you log off during a remote    If you do not log off in this scenario, the session remains open.
control session and log on as a
different user, ensure that you
log off before you disconnect
the remote control session.

Do not give users local           When you give users local administrator rights, they might be
administrator rights.             able to take over your remote control session or compromise
                                  your credentials.

Use either Group Policy or        You can use Configuration Manager and Group Policy to make
Configuration Manager to          configuration changes to the Remote Assistance settings. When
configure Remote Assistance       Group Policy is refreshed on the client, by default, it optimizes
settings, but not both.           the process by changing only the policies that have changed on
                                  the server. Configuration Manager changes the settings in the
                                  local security policy, which might not be overwritten unless the
                                  Group Policy update is forced.

                                  Setting policy in both places might lead to inconsistent results.
                                  Choose one of these methods to configure your Remote
                                  Assistance settings.

Enable the client setting         Although there are ways around this client setting that prompts
Prompt user for Remote            a user to confirm a remote control session, enable this setting
Control permission.               to reduce the chance of users being spied upon while working
                                  on confidential tasks.

                                  In addition, educate users to verify the account name that is
                                  displayed during the remote control session and disconnect the
                                  session if they suspect that the account is unauthorized.

Limit the Permitted Viewers       Local administrator rights are not required for a user to be able
list.                             to use remote control.

<!-- p.2639 -->

Security issues for remote control
Managing client computers by using remote control has the following security issues:

     Do not consider remote control audit messages to be reliable.

     If you start a remote control session and then log on by using alternative
     credentials, the original account sends the audit messages, not the account that
     used the alternative credentials.

     Audit messages are not sent if you copy the binary files for remote control rather
     than install the Configuration Manager console, and then run remote control at the
     command prompt.

Privacy information for remote control
Remote control lets you view active sessions on Configuration Manager client
computers and potentially view any information stored on those computers. By default,
remote control is not enabled.

Although you can configure remote control to provide prominent notice and get
consent from a user before a remote control session begins, it can also monitor users
without their permission or awareness. You can configure View Only access level so that
nothing can be changed on the remote control, or Full Control. The account of the
connecting administrator is displayed in the remote control session, to help users
identify who is connecting to their computer.

By default, Configuration Manager grants the local Administrators group Remote
Control permissions.

Before you configure remote control, consider your privacy requirements.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.2640 -->

Introduction to power management in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Power Management in Configuration Manager addresses the need that many
organizations have to monitor and reduce the power consumption of their computers.
The feature takes advantage of the power management features built into Windows to
apply relevant and consistent settings to computers in the organization. You can apply
different power settings to computers during business hours and nonbusiness hours.
For example, you might want to apply a more restrictive power plan to computers
during nonbusiness hours. In cases where computers must always remain turned on, you
can prevent power management settings from being applied.

Power management in Configuration Manager includes several reports to help you
analyze power consumption and computer power settings in your organization. You can
also use the reports to help you troubleshoot problems with power management.

For a detailed workflow about how to configure and use power management, see
Administrator checklist for power management.

  ） Important

  Configuration Manager power management is not supported on virtual machines.
  You cannot apply power plans to virtual machines, nor can you or report power
  data from them.

The power management workflow
Use the following three phases to plan and implement power management in
Configuration Manager.

Monitoring and planning phase
Power Management uses Configuration Manager hardware inventory to collect data
about computer usage and power settings for computers in the site. There are a number
of reports that you can use to analyze this data and determine the optimal power
management settings for computers. For example, during the monitoring and planning
