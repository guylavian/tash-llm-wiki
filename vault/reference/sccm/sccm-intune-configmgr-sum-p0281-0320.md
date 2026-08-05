---
title: "Software update management documentation — pages 281-320"
type: reference
domain: sccm
slug: sccm-intune-configmgr-sum-p0281-0320
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-sum-p0281-0320
family: sccm
documentKind: "doc"
abstract: "Assign an update to a category Once you've authored your update, you can assign it to a category by selecting the update then clicking the Categorize button. You can also right-click the update and select Categorize. About detectoids Once authoring mode is enabled, you can creat"
---

# Software update management documentation — pages 281-320

<!-- p.281 -->

Assign an update to a category
Once you've authored your update, you can assign it to a category by selecting the
update then clicking the Categorize button. You can also right-click the update and
select Categorize.

About detectoids
Once authoring mode is enabled, you can create detectoids for updates. Detectoids are
useful when you have multiple updates that use the same rule (or a set of rules) to
determine applicability. In those instances, you would create a detectoid and assign it as
a prerequisite for an update. You can assign multiple detectoids to an authored update.

Create a detectoid
   1. Open the Updates Workspace.

<!-- p.282 -->

   2. In the ribbon, click the Detectoid button.
   3. Follow the prompts in the wizard to create your detectoid.

Release history
     2019 RTW version 6.0.394.0     . Released November, 6, 2019
     Update rollup version 6.0.283.0 from KB4462765       . Released September 7, 2018.
     2017 RTW version 6.0.276.0     . Released March 26, 2018.

Next steps
To get started, first install, and then configure options for Updates Publisher.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.283 -->

Install Updates Publisher
Article • 10/04/2022

Applies to: System Center Updates Publisher

The information in these articles can help you download, install, and set up Updates
Publisher for use with your Configuration Manager environment.

Prerequisites and limitations
System Center Updates Publisher can only be used with Configuration Manager. It isn't
intended for use with stand-alone WSUS hierarchies.

The following sections detail requirements to install and use Updates Publisher, and
limitations or known issues for its use.

Operating systems
Install and run Updates Publisher on a 64-bit editions of the following operating
systems. There are no minimum cumulative update or service pack requirements.

      Windows Server 2016 (Standard, Datacenter)
      Windows Server 2012 R2 (Standard, Datacenter)
      Windows 11
      Windows 10 (Pro, Education, Pro Education, Enterprise)
      Windows 8.1 (Professional, Enterprise)

Prerequisites
The following are required on the computer that runs Updates Publisher.

      64-bit operating system: The computer where you install Updates Publisher must
      run a 64-bit operating system.
      WSUS 6.2 or later:
         On Windows Server, install the default Administration Console to meet this
         requirement.
         For Windows 8.1 or later operating systems, install the Remote Server
         Administration Tools (RSAT) for Windows operating systems     . This installs the
         necessary support to use Updates Publisher (API and PowerShell cmdlets, and
         User Interface Management Console).
      Permissions:

<!-- p.284 -->

         Installation: Local admin
         Most operations: local user
         Publishing, or operations that involve WSUS: Member of WSUS Administrators
         group on the WSUS Server.

Supported languages
Updates Publisher is available only in English but can manage updates for other
languages. The language support depends on the task, such as publishing, creating, or
editing updates.

When exporting or publishing updates, Updates Publisher displays the title and
description of the software update based on the locale of the computer where Updates
Publisher is installed.

For example, you create a software update that has an English and Spanish title.

     If you create the update on a computer whose locale is English, by default, you
     would see the title and description in English.
     If you then export or publish that update to a computer whose locale is Spanish,
     on that computer you would see the title and description in Spanish.

Publishing
When you publish software updates, you can specify the language of the software
update binary file. You can also specify that the binary is language neutral. The following
languages are supported:

     Arabic
     Chinese (Hong Kong S.A.R.)
     Chinese (Traditional)
     Chinese (Simplified)
     Czech
     Danish
     Dutch
     English
     Finnish
     French
     German
     Greek
     Hebrew
     Hungarian

<!-- p.285 -->

     Italian
     Japanese
     Korean
     Norwegian
     Polish
     Portuguese
     Portuguese (Brazil)
     Russian
     Spanish
     Swedish
     Turkish

Software update titles and descriptions
The following languages are supported for software update titles and descriptions.

     Chinese (Traditional)
     Chinese (Simplified)
     English
     French
     German
     Italian
     Japanese
     Korean
     Portuguese (Brazil)
     Russian
     Spanish

Install Updates Publisher
Get the UpdatesPubliser.msi for installing System Center Updates Publisher from
https://aka.ms/SCUPDownload        .

To install Updates Publisher, run UpdatesPublisher.msi on a computer that meets the
prerequisites. The installer creates the following folder to contain the files necessary to
run Updates Publisher: %PROGRAMFILES%\Microsoft\UpdatesPublisher*.

Because this folder contains all the files necessary to use Updates Publisher, you can
copy the folder and its contents to a new location or computer and then use Updates
Publisher from that location. However, the new location or computer must meet the
prerequisites to run Updates Publisher.

<!-- p.286 -->

After installation completes, run UpdatesPublisher.exe from the UpdatesPublisher folder
to start Updates Publisher.

Next steps
After you install Updates Publisher, we recommend you configuring the options for
Updates Publisher. You must configure some options before you can use some features
of Updates Publisher.

However, if you want to use the defaults and don't plan to deploy updates to an update
server or to managed devices, you can jump right to managing software update
catalogs, or create software updates and create update catalogs of your own.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.287 -->

Configure options for Updates Publisher
Article • 10/04/2022

Applies to: System Center Updates Publisher

Review and configure the options and related settings that affect the operation of
Updates Publisher.

To access the Updates Publisher options, in upper left corner of the console, click on the
Updates Publisher Properties tab, and then choose Options.

Options are divided into the following:

      Update Server
      ConfigMgr Server
      Proxy Settings
      Trusted Publishers
      Advanced
      Updates
      Logging

Update Server
You must configure Updates Publisher to work with update server like Windows Server
Update Services (WSUS) before you can publish updates. This includes specifying the
server, methods to connect to that server when it's remote from the console, and a
certificate to use to digitally sign updates you publish.

      Configure an update server. When you configure an update server, select the top-
      level WSUS server (update server) in your Configuration Manager hierarchy so that
      all child sites have access to the updates that you publish.

<!-- p.288 -->

If your update server is remote from your Updates Publisher server, specify the
fully qualified domain name (FQDN) of the server, and if you'll connect by SSL.
When you connect by SSL, the default port changes from 8530 to 8531. Ensure the
port you set matches what is in use by your update server.

   Tip

  If you do not configure an update server, you can still use Updates Publisher
  to author software updates.

Configure the signing certificate. You must configure and successfully connect to
an update server before you can configure the signing certificate.

Updates Publisher uses the signing certificate to sign the software updates that are
published to the update server. Publishing fails if the digital certificate isn't
available in the certificate store of the update server or the computer that runs
Updates Publisher.

For more information about adding the certificate to the certificate store, see
Certificates and security for Updates Publisher.

If a digital certificate isn't automatically detected for the update server, choose one
of the following:

   Browse: Browse is only available when the update server is installed on the
   server where you run the console. After you select a certificate, you must choose
   Create to add that certificate to the WSUS certificate store on the update server.
   You must enter the .pfx file password for certificates that you select by this
   method.

   Create: Use this option to create a new certificate. This also adds the certificate
   to the WSUS certificate store on the update server.

If you create your own signing certificate, configure the following:

   Enable the Allow private key to be exported option.

   Set Key Usage to digital signature.

   Set Minimum key size to a value equal to or greater than 2048 bit.

Use the Remove option to remove a certificate from the WSUS certificate store.
This option is available when the update server is local to the Updates Publisher
console you use, or when you used SSL to connect to a remote update server.

<!-- p.289 -->

ConfigMgr Server
Use these options when you use Configuration Manager with Updates Publisher.

     Specify the Configuration Manager server: After you enable support for
     Configuration Manager, specify the location of the top-tier site server from your
     Configuration Manager hierarchy. If that server is remote from the Updates
     Publisher install, specify the FQDN of the site server. Choose Test Connection to
     ensure you can connect to the site server.

     Configure thresholds: Thresholds are used when you publish updates with a
     publication type of Automatic. The threshold values help determine when the full
     content for an update is published instead of only the metadata. To learn more
     publication types, see Assign updates to a publication

     You can one or both of the following thresholds:

        Requested client count threshold: This defines how many clients must request
        an update before Updates Publisher can automatically publish the full set of
        content for that update. Until the specified number of clients request the
        update, only the updates metadata is published.

        Package source size threshold (MB): This prevents automatic publishing of
        updates that exceed the size you specify. If the updates size exceeds this value,
        only the metadata is published. Updates that are smaller than the specified size
        can have their full content published.

Proxy Settings
Updates Publisher uses the proxy settings when you import software catalogs from the
Internet or publish updates to the Internet.

     Specify the FQDN or IP address of a proxy server. IPv4 and IPv6 are supported.

     If the proxy server authenticates users for Internet access, you must specify the
     Windows name. A universal principle name (UPN) isn't supported.

Trusted Publishers
When you import an update catalog, the source of that catalog (based on its certificate),
is added as a trusted publisher. Similarly, when you publish an update, the source of the
updates certificate is added as a trusted publisher.

<!-- p.290 -->

You can view certificate details for each publisher and remove a publisher from the list
of trusted publishers.

Content from publishers that aren't trusted can potentially harm client computers when
the client scans for updates. You should accept content only from publishers that you
trust.

Advanced
Advanced options include the following:

         Repository location: View and modify the location of the Database file,
         scupdb.sdf. This file is the repository for Updates Publisher.

         Timestamp: When enabled, a timestamp is added to updates you sign that
         identifies when it was signed. An update that was signed while a certificate was
         valid can be used after that signing certificate expires. By default, software updates
         can't be deployed after their signing certificate expires.

         Check for updates to subscribed catalogs: Each time Updates Publisher starts, it
         can automatically check for updates to catalogs that you have subscribed to. When
         a catalog update is found, details are provided as Recent Alerts in the Overview
         window of the Updates Workspace.

         Certificate revocation: Choose this option to enable certificate revocation checks.

         Local source publishing: Updates Publisher can use a local copy of an update
         you're publishing before downloading that update from the Internet. The location
         must be a folder on the computer that runs Updates Publisher. By default, this
         location is My Documents\LocalSourcePublishing. Use this when you have
         previously downloaded one or more updates, or have made modifications to an
         update you want to deploy.

         Software Updates Cleanup Wizard: Start the updates cleanup wizard. The wizard
         expires updates that are on the update server but not in the Updates Publisher
         repository. See Expire unreferenced updates for more details.

Updates
Updates Publisher can automatically check for new updates each time it opens. You can
also opt into receiving preview builds of Updates Publisher.

<!-- p.291 -->

To manually check for updates, in the Updates Publisher console click on
to open the Updates Publisher Properties, and then choose Check for update.

After Updates Publisher finds a new update, it displays the Update Available window
and you can then choose to install it. If you choose to not install the update, it's offered
the next time you open the console.

Logging
Updates Publisher logs basic information about Updates Publisher to
%WINDIR%\Temp\UpdatesPublisher.log.

Use notepad or CMTrace to view the log. CMTrace is the Configuration Manager log file
tool and can be found in the \SMSSetup\Tools folder of the Configuration Manager
source media.

You can change the size of the log and its level of detail.

When you enable database logging, information about the queries that are run against
the Updates Publisher database are included. Use of database logging can lead to
reduced performance of the Updates Publisher computer.

To view the log file, in the console click on         to open the Updates Publisher
Properties, and then choose View log file.

Expire unreferenced software updates
You can run the Software Update Cleanup Wizard to expire updates that are on your
update server but not in the Updates Publisher repository. This notifies Configuration
Manager which then removes those updates from any future deployments.

The act of expiring an update can't be reversed. Only perform this task when you're sure
that the software updates you select are no longer required by your organization.

To remove expired software updates

   1. In the Updates Publisher console, click on              to open the Updates Publisher
     Properties, and then choose Options.

   2. Choose Advanced, and then under Software Update Clean Wizard, choose Start.

   3. Select the software updates you want to expire, and then choose Next.

<!-- p.292 -->

   4. After reviewing your selections, chose Next to accept the selections and expire
     those updates.

   5. After the wizard finishes, choose Close to complete the wizard.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.293 -->

Manage software update catalogs in
Updates Publisher
Article • 10/04/2022

Applies to: System Center Updates Publisher

Use the Catalogs Workspace to manage software update catalogs. This includes adding
new catalogs, managing existing catalog subscriptions, and importing information about
the updates from a catalog to the Updates Publisher repository.

Software update catalogs contain information about related updates that are created by
organizations other than Microsoft. Other organizations include your own organization
and third-party software vendors that have registered their catalogs with Microsoft.
Registered catalogs from software vendors are called partner catalogs. Catalogs that you
create, and that are not registered with Microsoft, are called user catalogs.

Add software update catalogs
You must add an update catalog to Updates Publisher before you can manage the
updates that it contains. When you add a catalog, Updates Publisher:

       Creates a subscription to that catalog, so it can check for updates to that catalog.
       Adds the catalog to a list in the My Software Update Catalogs window of the
       Catalogs Workspace.

Information about each subscribed catalog is available in the console. Information
includes the download URL or location, the name of the company or organization who
created the catalog, and when it was last imported or modified.

Updates Publisher can automatically check your subscriptions for changes each time it
starts. This is configured as an Advanced option. When configured, Updates Publisher
references the download URL or location information for the subscription and alerts you
when there are changes to the catalog that were made since the last time you imported
it to the repository.

To manually check for a catalog update, select the catalog from the My Software
Update Catalogs list and then choose Refresh from the ribbon.

In addition to adding catalogs, and viewing information about subscribed catalogs, you
can:

<!-- p.294 -->

     Edit information for user catalogs.
     Delete (remove) a catalog from Updates Publisher.
     Import updates from a catalog into the Updates Publisher repository. When you
     import updates, you import all updates contained in that catalog. You can then
     view the updates in the Updates workspace where you can then select and publish
     updates to your update server.

  ７ Note

  Deleting a catalog from Updates Publisher results in the updates in that catalog
  being removed from your repository. This does not affect the updates you have
  published to your update server. To remove updates from your update server that
  are no longer in your repository, see Expire unreferenced software updates.

Manage update catalogs
You can view the list catalogs you have imported in the My Software Update Catalogs
window of the Catalogs Workspace. From this workspace you can:

     Add a partner catalog: Use one of the following to find new partner catalogs:

       In the console, go to Updates Workspace > Overview. In the Getting Started
       window, choose Add Partner Software Updates Catalogs.

       In the console, go to Catalogs Workspace > My Catalogs. Then, from the
       ribbon, choose Add Catalogs.

     Add a user catalog: In the console, go to Catalogs Workspace > My Catalogs.
     Then, from the ribbon, choose Add Catalogs. In addition to the location of the .cab
     file, you must specify a Publisher, Name, and Description to identify the catalog.

     Check for updates to catalogs: Select one or more catalogs and then choose
     Refresh from the ribbon.

     Edit a user catalog: Select a user catalog and then choose Edit from the ribbon.
     You can then modify the user defined properties.

     Delete catalogs: Select one or more catalogs and then choose Remove from the
     ribbon. This removes the catalog, your subscription, and the updates from those
     catalogs from your Updates Publisher repository.

     Add updates from a catalog to your repository: Choose Import from the ribbon
     to start the Import Catalog wizard. For more infomration, see Import updates

<!-- p.295 -->

Import updates
When you import a catalog, Updates Manager adds the updates from that catalog to
the Updates Publisher repository. After updates are imported, you can publish them to
your update server to make them available to managed devices.

To import updates
   1. To start the Import Catalog wizard, choose Import from the Ribbon in one of the
     following workspaces:

          Catalogs Workspace

          Updates Workspace

   2. On the Import Type page, select one or more catalogs you've added to Updates
     Publisher, or specify a path to a catalog you have not yet added as a subscription.
     Chose Next to view the summary screen, and when ready, choose Next to start the
     import.

   3. On the Security Warning – Catalog Validation window, review the catalog
     certificate, and when ready, chose Accept to import the updates.

       Ｕ Caution

       Accept updates only from publishers that you trust. Software updates from
       publishers who are not trusted can potentially harm client computers when
       scanning for updates.

       If you no longer trust a publisher, remove that publisher from the trusted
       publishers list. To find more information about accepting catalogs, click Tell
       Me More in the Security Warning – Catalog Validation dialog box.

     If you choose to always accept catalogs from a publisher, that publisher is added
     to the trusted publishers list. You can review and edit this list as an Updates
     Publisher option.

   4. Import skips import of an update when the update is already in the repository and
     one of the following is true:

          The update is unchanged from the last time it was imported.

<!-- p.296 -->

           The update has been edited and has a new digital hash. Editing an update
           prevents a new update from overwriting the original as doing so would
           overwrite changes you might have deployed.

   5. On the Confirmation page review the import results.

   6. Click Close to complete the wizard. You can now view the updates for this catalog
     in the Updates Workspace.

Next steps
After you import updates, common actions include:

     Manage updates to bundle, assign, and deploy them your update server.
     Create applicability rules to help determine when updates deploy to your update
     server.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.297 -->

Manage software updates in Updates
Publisher
Article • 10/04/2022

Applies to: System Center Updates Publisher

In System Center Updates Publisher, you use the Updates Workspace to manage
software updates and bundles that you have imported to the repository.

Management tasks include duplicating, editing, and expiring or reactivating updates and
bundles, and assigning updates and bundles to publications. You can also export
custom catalogs for use with other Updates Publisher installations.

To get updates that you can manage:

      Add an update catalog to your installation of Updates Publisher
      Import the updates from that catalog to your repository.

You can also create your own updates.

Create a duplicate of an update
You can create duplicates, or copies, of updates that are in your repository. Then you
can modify the copy instead of modifying the original update. You cannot create copies
of update bundles.

To create a copy, select an update in the Updates Workspace, and then choose
Duplicate. The copy of the update appears in the same location in the Updates
Workspace with Copy of added to its name.

A new copy you create has a status of Unexpired, but otherwise retains the settings of
the original.

Edit updates and bundles
You can select updates and bundles that are in your repository to modify them.

In the Updates Workspace select an update or bundle, and then select Edit from the
Home tab to open the edit wizard. Updates and bundles each have separate but closely
related wizards that present the same options as the Create Update or Create Bundle
wizards.

<!-- p.298 -->

When editing, you can change any available detail about the update or bundle so that it
can be used in your environment. For example, you can edit the applicability or
precedence rules, or change the language. You can also change the product and vendor
to move the update or bundle to a custom folder to group updates for your own use.

Assign updates and bundles to a publication
You can select updates and bundles in the Updates Workspace and then choose Assign
from the Home tab of the ribbon to add them to a publication. This starts the Assign
Software Updates wizard.

     See Publish updates and bundles for information on how to select and publish
     updates and bundles as a single task.
     See Manage publications for information on how to manage groups of updates
     and bundles as a single object. After you assign updates to a publication, you can
     manage that publication, which in turn includes all its assigned updates.

When you assign updates to a publication:

     You can include expired and non-expired updates and bundles in the same
     publication.

     Specify the publication type:

        Full Content – This publishes the full content of the update to your WSUS
        Server. This includes metadata and the update binaries.

        Metadata only – This publishes only the metadata; update binaries are not
        published. You might choose this option when you want to gather compliance
        data.

        Automatic – This mode is only available when you have connected Updates
        Publisher to Configuration Manager (See the ConfigMgr Server option.)

     With this type, Updates Publisher queries Configuration Manager to determine if
     the updates or bundles should be published with full content or only metadata.
     Full content for an update is published only when that update meets the
     Requested client count threshold and Package source size threshold, which are
     specified on the ConfigMgr Server page of Updates Publisher options.

     Select a publication:

        Use Assign software update to existing publications when you have already
        created a publication that you want to use. This option is not available until at

<!-- p.299 -->

          least one publication exists.

          Use Assign software update to a new publication when you do not have a
          suitable publication. This will create a new publication with the name that you
          specify.

After you assign updates to a publication, you can use the Publication Workspace to
publish or export the publication as a group.

Publish updates and bundles from the Updates
Workspace
When you publish updates and bundles, Updates Publisher adds information about
those updates and bundles (metadata) and possibly the binaries for the updates (full
content), to an update server for deployment to devices.

Before you have the option to publish, you must configure the Update Server option for
Updates Publisher. To open this configuration option, go to Updates Workspace >
Overview and select Configure WSUS and Signing Certificate. You can also go to the
Update Server page in the Updates Publisher options.

There are two ways to publish updates and bundles:

     Directly from the Updates Workspace. (See the following procedure, To publish
     updates and bundles.)
     As a publication from the Publications Workspace.

  ７ Note

  Updates Publisher can only publish updates that are 375 megabytes (MB) or less in
  size.

To publish updates and bundles
   1. Go to Updates Workspace and select one or more updates and bundles that you
     want to publish. Then choose Publish from Home tab of the ribbon.

   2. On the Select page of the Publish wizard, select how you want to publish the
     updates. The options are the same as for assigning updates: Full Content,
     Metadata only, or Automatic.

     You can also choose to sign all updates with a new publishing certificate.

<!-- p.300 -->

   3. Complete the wizard.

If publishing fails, you are presented with a link to the UpdatesPublisher.log file that can
provide more information.

Export updates
You can export updates and bundles from your Updates Publisher repository to create a
custom update catalog. Then, you can add and then import that catalog to another
instance of Updates Publisher. (You can also export updates as a publication.)

To export directly, go to Updates Workspace > All Software Updates and select one or
more updates and bundles. You cannot export a vendor or product folder, but you can
select a folder and then select the updates in that folder for export.

With one or more updates selected, choose Export from the Home tab of the ribbon,
and then provide a path and filename for the catalog export.

You will have the option to export (include) dependent software updates.

Delete updates and bundles
You can delete updates and bundles of updates to remove them from the Updates
Publisher repository.

Go to Updates Workspace > All Software Updates and select one or more individual
updates. Then choose Delete from the Home tab of the ribbon.

     If your selection contains only updates or bundles that have not been published or
     that are expired, you are asked to confirm deletion before they are removed.

     If your selection includes an update or bundle that has been published and is not
     yet expired, you are given a warning. You should expire those updates and then
     publish that change before you delete them from the repository.

If you delete an update or bundle from a vendor and then import that catalog again,
that update is restored to your repository.

Manage vendor and product folders
To view a list of vendors, and products for each vendor for which you have imported or
created updates, go to Updates Workspace > Overview > All Software Updates.

<!-- p.301 -->

Folders for vendors and products are automatically created by Updates Publisher when
you use a wizard to import or create a software update or bundle. You can also create
these folders manually.

     To create a vendor folder, in the navigation pane of the Updates Workspace, right-
     click on All Software Updates, and then choose Create Vendor.

     To create a product folder under a vendor folder, right-click on the vendor folder
     and choose Create Product.

In addition to creating folders, you can rename or delete any vendor or product folder in
your repository. To do so, right-click on the folder and choose the option you want,
Rename or Delete. Deleting a folder removes all the updates and bundles in that folder
and its product folders from the Updates Publisher repository.

You can move updates between vendor and product folders, including to folders you
create. To move an update or bundle to a new folder, you must select and then Edit the
update or bundle. Then, on the Information page of the Edit Update wizard you can
reassign the vendor and product. When the Edit Update wizard completes, the change
applies and the update moves to the new folder.

View the XML of an update or bundle
You can select a single update or bundle in the Updates Workspace and then choose
View XML to display the XML structure of that update. There are no options to edit the
XML structure directly.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.302 -->

Manage publications in Updates
Publisher
Article • 10/04/2022

Applies to: System Center Updates Publisher

You can use publications to manage groups of updates and bundles as a single object.
This includes publishing the updates to a management server and exporting the
publication as group for use with another install of Updates Publisher.

Create publications
Publications are created two ways:

      When you manage updates and bundles in the Updates Workspace, you can
      assign them to a new publication that is created at that time.

      In the Publications Workspace, you can use the Create button on the Publication
      tab of the ribbon. This method lets you create a publication for future use. Later,
      when you assign updates, you can use this publication.

Rename a publication
To rename a publication, select the publication from within the Publications Workspace,
and then on the Publication tab of the ribbon, choose Edit.

Change the publication type of updates in a
publication
From the Publication Workspace, you can modify the publication type of updates and
bundles that are assigned to a publication.

   1. Select the publication that contains the updates you want to modify, and then
      select one or more update or bundles from the All <publication name> member
      updates list.

   2. Next, on the Home tab, choose one of the following options. The options that are
      available depend on the publication type of the updates you have selected.

            Automatic

<!-- p.303 -->

           Full Content
           Metadata only

After making a change, you might need to refresh the publication view to see the new
values.

For information about the different publication types, see Assign updates and bundles
to a publication.

   Tip

  When you set the publication type of a bundle, all the software updates in that
  bundle are published with the publication type of that bundle.

Remove updates from a publication
To remove updates or bundles from a publication, in the Publications Workspace select
the publication you want to modify, and then select the updates and bundles you want
to remove. Next, on the Home tab of the ribbon, choose Remove.

After updates are removed from a publication, they remain available in the Updates
Publisher repository.

Publish publications
When you publish updates and bundles, Updates Publisher adds information about
those updates and bundles (metadata) and possibly the binaries for the updates (full
content), to an update server for deployment to devices.

Before you have the option to publish, you must configure the Update Server option for
Updates Publisher. To open this configuration option, go to Updates Workspace >
Overview and select Configure WSUS and Signing Certificate. You can also go to the
Update Server page in the Updates Publisher options.

  ７ Note

  Updates Publisher can only publish updates that are 375 megabytes (MB) or less in
  size.

To publish a publication

<!-- p.304 -->

   1. Go to the Publications Workspace, and then select a publication that contains the
        group of updates and bundles that you want to publish or export. Then choose
        Publish from Home tab of the ribbon.

   2. On the Select page of the Publish wizard you can choose to sign all updates with a
        new publishing certificate, but you cannot change the publication type.

   3. Complete the wizard.

        If publishing fails, you are presented with a link to the UpdatesPublisher.log file
        that can provide more information.

Export a publication
You can export a publication from your Updates Publisher repository. Doing so exports
the updates and bundles that are assigned to that publication and creates an update
catalog. You can then add and then import that catalog to another instance of Updates
Publisher. You can also export updates that are not part of a publication.

To export a publication, go to the Publications Workspace and select the publication
that contains updates that you want to export. You can only select one publication at a
time.

With the publication selected, choose Export from the Home tab of the ribbon, and
then provide a path and filename for the catalog export.

You also have the option to export (include) dependent software updates as part of the
export.

Delete a publication
To delete a publication, select the publication the Publications Workspace, and then
choose Delete from the Publication tab of the ribbon.

After the publication is removed from Updates Publisher, the updates that were in the
publication remain available in the Updates Publisher repository.

Expire or reactivate updates and bundles
You can use the Updates Workspace to select and then expire or reactivate updates and
bundles. You can expire and reactivate updates and bundles as many times as you
choose.

<!-- p.305 -->

     To expire updates or bundles, in the Updates Workspace select one or more
     updates or bundles that are not expired, and then choose Expire from the Home
     tab. Until you publish the update or bundle as expired to Configuration Manager,
     you can reactivate it.

     Before you can remove (delete) a custom update or bundle from Configuration
     Manager, you must expire it and then publish that expired status to Configuration
     Manager. After updates or bundles are expired in Configuration Manager, you can
     no longer deploy or reactivate the update or bundle.

     To reactivate updates or bundles, in the Updates Workspace select one or more
     updates that are expired, and then choose Reactivate from the Home tab of the
     ribbon. If the expired update was previously published as expired to Configuration
     Manager, you cannot reactivate it.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.306 -->

Create software updates and update
bundles with Updates Publisher
Article • 10/04/2022

Applies to: System Center Updates Publisher

With Updates Publisher you can use the Create Update wizard to create your own
updates and the Create Bundle wizard to create bundles of updates.

Because these two wizards have a similar workflow, the procedure to create an update
bundle refers to the procedure for creating updates, with only the relevant differences
detailed.

Use the Create Update wizard
   1. In the console go to Updates Workspace, and then in the Getting Started pane,
      choose Update from the Home tab of the ribbon. This opens the Create Update
      wizard.

   2. On the Package page, use the following information to help you configure the
      update:

            Choose Browse to locate the software update package you'll use as a
            package source. Valid sources include .MSI, .MSP, or .EXE files. Updates
            Publisher requires access to the file to create a file hash. The hash and file
            name are then used in the update metadata for the update that you're
            creating.

            Specify the source location of the content for this update. Normally this is the
            location where the update binary will be downloaded from during publishing
            to a WSUS server. If the Use a local source to publish software update
            content option is selected, then the path isn't required.

            Later, when the update is published to a WSUS server, Updates Publisher
            downloads the binaries for the update from the indicated source location. If
            no path is provided then Update Publisher will search the local source
            publishing path for the update binary.

            Specify the Binary language of the software update.

<!-- p.307 -->

       Specify Success return codes, and Success pending reboot codes for the
       update. Separate multiple return codes by using a comma. You can use return
       codes to determine when update install was successful, and when reboots
       were required.

          Windows installer files and patches (.MSI and .MSP files) automatically set
          these values, and they can't be modified.

          For .EXE updates, the default codes defined by the .EXE file are used if no
          return codes are specified.

       Specify any command-line arguments that are required to install the software
       update.

          Windows installer files and patches (.MSI and .MSP files) automatically set
          these values. For these file types the arguments must be specified as
          [name]=[value]. In addition, all options that start with a / (like /qn) aren't
          supported for .MSI or .MSP software updates.

          For .EXE updates, all arguments are valid.

    ７ Note

    You can use Updates Publisher to create only packages that are smaller than 2
    GB. Import options are disabled if the software update package is too large.

3. On the Information page, specify details about the update that are included when
  the update is published or exported. Details include localized properties like the
  updates name (title) and description. Then, you specify more general details such
  as the classification, vendor, product, and where to learn more about the update.

  Localized properties:

       Language: Select a language and then specify a title and description. You can
       then select additional languages, one at time, with each language supporting
       its own title and description.

       Title: Enter the name of the update. This name displays in the Updates
       Workspace of the Updates Publisher console.

       Description: A friendly description of the update. You might include what the
       update installs, and why or when it should be used.

<!-- p.308 -->

Classification: The following are common descriptions for the different
classifications.

      Update: An update to an application or file that is currently installed.

      Critical: A broadly released update for a specific problem that addresses a
      critical bug that isn't related to security.

      Feature Pack: New product features that are distributed outside of a product
      release and are typically included in the next full product release.

      Security: A broadly released update for a product-specific issue that is related
      to security.

      Update Rollup: A cumulative set of hotfixes that are packaged together for
      easy deployment. These hotfixes can include security updates, critical
      updates, updates, and so on. An update rollup generally addresses a specific
      area, such as security or a product feature.

      Service Pack: A cumulative set of hotfixes that are applied to an application.
      These hotfixes can include security updates, critical updates, software
      updates, and so on.

      Tool: Specifies a tool or feature that helps complete one or more tasks.

      Driver: An update for driver software.

Vendor: Specify a vendor for the update. You can use the dropdown list to use
values from updates that are in the repository. When you specify a vendor, the
wizard creates a folder with that vendor name under All Software Updates in the
Updates Workspace if that folder doesn't already exist. The following are Windows
Server Update Services (WSUS) reserved names that can't be entered for updates
you create:

      Microsoft Corporation
      Microsoft
      Update
      Software Update
      Tools
      Tool
      Critical
      Critical Updates
      Security
      Security Updates

<!-- p.309 -->

       Feature Pack
       Update Rollup
       Service Pack
       Driver
       Driver Update
       Bundle
       Bundle Update

  Product: Specify the type of product that the update is for. You can use the
  dropdown list to use values from updates that are in the repository. The same list
  of WSUS reserved names that can't be used for Vendor, can't be used for Product.

  More info URL: Specify the URL where you can find more information about this
  update. You must use lowercase letters for https or http when you enter this URL.

4. On the Optional Info page, you can configure details that provide additional
  information about the update.

       Bulletin ID: Bulletin IDs are usually, but not always, provided by update
       vendors.

       Article ID: If a software update article is available, the Article ID can be useful
       to individuals seeking additional information about the update.

       CVE IDs: List one or more Common Vulnerabilities and Exposures (CVE)
       identifiers that provide security information about the update or update
       bundle. When listing more than one, use a semicolon to separate the CVEs as
       in this example: CVE1;CVE2.

       Support URL: List the URL that contains support information for this update,
       if available. You must use lowercase letters for https or http when you enter
       this URL.

       Severity: Set the severity level for this update.

       Impact: The following options can be used to specify impact:
          Normal – Use this to indicate the update requires typical installation
          procedures.
          Minor – Use this to indicate the update requires minimal installation
          procedures.
          Requires exclusive handling – Use this to indicate the update must be
          installed by itself, exclusive from any other updates.

<!-- p.310 -->

       Restart Behavior: Use this to provide information about the updates restart
       behavior. This setting doesn't affect the actual behavior of the update install.
          Never reboots: The computer never performs a system restart after
          installing the software update.
          Always requires reboot: The computer always performs a system restart
          after installing the software update.
          Can request reboot: After installing the software update, the computer
          requests a system restart only if a restart is necessary. The user has the
          option to postpone the restart. This is the default value.

5. On the Prerequisite page, specify the prerequisites that must be installed on a
  computer before this update can install. Prerequisites can be detectoids or other
  updates. Detectoids are high-level rules like one that requires the computers CPU
  to be a 64-bit processor. Detectoids can also specify specific updates that must be
  installed before this update can install.

       For better performance, use detectoids instead of creating installable and
       installed rules that perform the same check or action.

  Use the search option for Available software updates and detectoids to help you
  find specific updates or detectoids. For example, search on CPU to find the
  detectoids that let you limit installation based on specific CPU architecture.

  You can select one or more items at a time to add as a prerequisite. When adding
  prerequisites, the selected detectoids are added as one or more groups. To qualify
  for installation, a computer must meet the requirement of at least one member of
  each group that you configure:

       When you click Add Prerequisite, all items you have selected are added to
       separate, individual, groups. To qualify for this update, a computer must meet
       the prerequisite in this group and pass requirements for any additional
       groups that are configured.

       When you click Add Group, all items you have selected are added to a single
       group. To qualify for this update, a computer must meet at least one of the
       prerequisites in this group and pass requirements for any additional groups
       that are configured.

6. On the Supersedence page, specify the updates that are replaced (superseded) by
  this update. When this update is published, Configuration Manager will mark each
  update that is superseded as Expired. Clients will then install this update instead of
  the superseded updates.

<!-- p.311 -->

7. On the Applicability page use the Rule Editor to define a set of rules that
  determine whether a device needs this update. (This page is similar to the Installed
  page, that follows it.)

  To add a new rule, click on         . This opens the Applicability Rule page where you
  can configure rules.

  Types of rules you can create include:

        File – Use this rule to require that a device have a file with properties that
        meet one or more criteria you specify before this update can be applied.

        Registry – Use this type to specify registry details that must be present
        before a device qualifies to install this update.

        System – This rule uses system details to determine applicability. You can
        choose between defining a Windows version, a Windows language, processor
        architecture, or specify a WMI query to identify the devices operating system.

        Windows Installer – Use this rule type to determine applicability based on an
        installed .MSI or Windows Installer patch (.MSP). You can also determine if
        specific components or features are installed as part of the requirement.

             ） Important

             On managed devices, the Windows Update Agent cannot detect
             Windows Install packages that are installed per-user. When you use this
             rule type, configure additional applicability rules, like file versions or
             registry key values, so that the Windows Installer package can be
             properly detected regardless of a per-user or per-system basis.

        Saved rule – This option lets you find and use rules you created in the Rules
        Workspace.

        After you create a rule, you can use the other icons to modify the rule, and if
        there are multiple rules, to define relationships between those rules.

  When you're done creating and adding rules, click OK in the Create Rule Set
  dialog box to save that set. You can then create a New rule and add that to the set
  as well.

  When you have multiple rules or rule sets to add to an update, you can use the
  logical operators in the Rule Editor to determine conditions between the rules, and

<!-- p.312 -->

     in which order they process.

   8. On the Installed page, use the Rule Editor to define a set of rules that determine
     whether a device has already installed the update you're configuring. (This page is
     similar to the Applicability page, that proceeds this page.)

     This page of the wizard supports configuring rules with the same options and
     criteria as the Applicability page.

     When the wizard completes, the new update is added to a node in the Updates
     Workspace that is identified by the Vendor and Product name you used for that
     update.

Use the Create Bundle wizard
Because this wizard uses the same workflow as the Create Update wizard, use that
workflow, but note the following difference for bundles:

   1. To start the wizard, in the console go to Updates Workspace, and then select
     Bundle from the Home tab of the ribbon.

   2. Unlike the Create Update wizard, there's no Package page when creating a bundle.

   3. On the Information page, specify details about the update bundle that are
     included when the update is published, or exported.

   4. On the Optional Info page, you can configure details that provide additional
     information about the update bundle. The available options are the same as for
     creating an update. However, options for Impact and Restart Behavior aren't
     available as they don't apply to bundles.

   5. On the Prerequisite page, specify the prerequisites that must be installed on a
     computer before this bundle can install. These rules are the same as seen for
     individual updates.

   6. On the Supersedence page, specify the updates that are replaced (superseded) by
     this update bundle. These rules are the same as seen for individual updates.

   7. On the Members page, you select updates to add to the update bundle. Only
     updates you have created or imported to Updates Publisher are available.

When the wizard completes, the new update bundle is added to a node in the Updates
Workspace that is identified by the Vendor name you used for the update bundle.

<!-- p.313 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.314 -->

Manage Applicability rules in Updates
Publisher
Article • 10/04/2022

Applies to: System Center Updates Publisher

With Updates Publisher, applicability rules define requirements that must be met before
a device can install an update. The rules are also used to determine if the computer has
an update installed. An applicability rule that is complex with multiple parts is referred
to as a rule set.

Update bundles do not use applicability rules.

Overview of applicability rules
You manage applicability rules from the Rules Workspace. When you create a rule, you
are specifying one or more conditions. When multiple conditions are specified, you can
configure relationships between the conditions so they are evaluated sequentially or
combined into logical And or Or statements.

For example, the following is a rule set that contains three rules. The first rule verifies
that the MyFile file exists, and the second and third rules verify that the language of the
Windows operating system is either English or Japanese.

  Example

  And
    File '\[PROGRAM\_FILES\] \\Microsoft\\MyFile' exists
    Or
      Windows Language is English
      Windows Language is Japanese

All updates require at least one applicability rule. Updates you import already have
applicability rules applied, and when you create your own updates, you must add one or
more rules to them. You can modify and expand on the rules for any update in Updates
Publisher.

To view rules you have created, in the Rules Workspace, select a rule from the My saved
rules list. The individual conditions and logical operations for that rule display in the
Applicability Rules pane of the console. Rules for updates that you import can only be
viewed and modified when you edit that update.

<!-- p.315 -->

You can create rules in two locations in Updates Publisher:

     In the Rules Workspace, you create and save rule sets that you can then use later.
     When editing or creating an update you can select Saved rule as the Rule type,
     and then select from a list of your pre-created rule sets.

     You can also create new rules at the time that you create or edit an update. Rules
     you create in this way are not saved for future use.

Create applicability rule
The following information is similar to how you create rules from within the Create
Update wizard. But unlike the wizard, you have the option to save your rule sets for
future use.

   1. In the Rules Workspace, choose Create to open the Create Rule wizard.

   2. Specify a name for the rule, and then click         . This opens the Applicability Rule
     page where you can configure rules.

   3. For Rule type, select one of the following. The options you must configure vary for
     each type:

              File – Use this rule to require that a device have a file with properties that
              meet one or more criteria you specify before this update can be applied.

              Registry – Use this type to specify registry details that must be present
              before a device qualifies to install this update.

              System – This rule uses system details to determine applicability. You can
              choose between defining a Windows version, a Windows language, processor
              architecture, or specify a WMI query to identify the devices operating system.

              Windows Installer – Use this rule type to determine applicability based on an
              installed .MSI or Windows Installer patch (.MSP). You can also determine if
              specific components or features are installed as part of the requirement.

                ） Important

                On managed deices, the Windows Update Agent cannot detect
                Windows Install packages that are installed per-user. When you use this
                rule type, configure additional applicability rules, like file versions or

<!-- p.316 -->

              registry key values, so that the Windows Installer package can be
              properly detected regardless of a per-user or per-system basis.

           Saved rule – This option lets you find and use rules that you previously
           configured and saved.

   4. Continue to add and configure additional rules as desired.

   5. Use the logical operation buttons to order and group different rules to create
     more complex prerequisite checks.

   6. When the rule set is complete, click OK to save it. The rule set now appears in the
     My saved rules list.

Edit applicability rule sets
To edit an applicability rule, in the Rules Workspace select any rule that is saved in the
My saved rules list, and then choose Edit from the ribbon. This opens the Edit Rule
wizard.

The Edit Rule wizard displays the current rules for the rule set. You edit rules in the same
way as you use the Create Rule wizard to create new rules. You can use this wizard to
rename the rule set, delete rules, re-order rules and relationships, or add new rules.

After you make changes, choose OK to save the changes and close the wizard.

For more details about using the rule wizard, see Step 7, the applicability page, of the
Create Update wizard.

Delete applicability rules
To delete a saved applicability rule, in the Rules Workspace select the rule or rule set
from the My saved rules list, and then choose Delete from the ribbon. This removes the
saved rule or rule set from Updates Publisher.

To delete a rule from a specific update, you must edit the update.

Feedback
Was this page helpful?    Yes     No

<!-- p.317 -->

Provide product feedback

<!-- p.318 -->

Manage certificates and security for
Updates Publisher
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The following procedures can help you to configure the certificate store on the update
server, configure a self-signing certificate on the client computer, and to configure the
Group Policy to allow the Windows Update Agent on computers to scan for published
updates.

Configure the certificate store on the update
server
Updates Publisher uses a digital certificate to sign the updates in the catalogs it
publishes. Before a catalog can be published to the update server, that certificate must
be in the certificate store on the update server, and in the certificate store of the
Updates Publisher computer if that computer is remote from the update server.

The following procedure is one of several possible methods to add the certificate to the
certificate store on the update server.

To configure the certificate store
   1. On a computer that can access both the Updates Publisher computer and the
      update server, Click Start, click Run, type MMC in the text box, and then click OK
      to open the Microsoft Management Console (MMC).

   2. Click File, click Add/Remove Snap-in, click Add, click Certificates, click Add, select
      Computer account, and then click Next.

   3. Select Another computer, type the name of the update server or click Browse to
      find the update server computer, click Finish, click Close, and then click OK.

   4. Expand Certificates (update server name), expand WSUS, and then click
      Certificates.

   5. In the results pane, right-click the desired certificate, click All Tasks, and then click
      Export.

<!-- p.319 -->

   6. In the Certificate Export Wizard, use the default settings to create an export file
      with the name and location specified in the wizard. This file must be available to
      the update server before proceeding to the next step.

   7. Right-click Trusted Publishers, click All Tasks, and then click Import. Complete the
      Certificate Import Wizard using the exported file from step 6.

   8. If a self-signed certificate is used, such as WSUS Publishers Self-signed, right-click
      Trusted Root Certification Authorities, click All Tasks, and then click Import.
      Complete the Certificate Import Wizard using the exported file from step 6.

   9. Right-click Certificates (update server name), click Connect to another computer,
      enter the computer name for the Updates Publisher computer, and click OK.

  10. If Updates Publisher is remote from the update server, repeat steps 7 through 9 to
      import the certificate to the certificate store on the Updates Publisher computer.

Configure a self-signing certificate on client
computers
On client computers, the Windows Update Agent (WUA) will scan for the updates from
the catalog. This process will fail to install updates when the agent cannot locate that
digital certificate in the Trusted Publishers store on the local computer. If a self-signed
certificate was used to publishing the updates catalog, such as WSUS Publishers Self-
signed, the certificate must also be in the Trusted Root Certification Authorities
certificate store on the local computer so that the agent can verify the validity of the
certificate.

You can use one of several methods for configuring certificates on client computers, like
using Group Policy and the Certificate Import Wizard or by using the Certutil tool and
software distribution.

The following is provided as one example of how to configure the signing certificate on
client computers.

To configure a self-signing certificate on client computers
   1. On a computer with access to the update server, click Start, click Run, type MMC in
      the text box, and then click OK to open the Microsoft Management Console
      (MMC).

<!-- p.320 -->

   2. Click File, click Add/Remove Snap-in, click Add, click Certificates, click Add, select
     Computer account, and then click Next.

   3. Select Another computer, type the name of the update server or click Browse to
     find the update server computer, click Finish, click Close, and then click OK.

   4. Expand Certificates (update server name), expand WSUS, and then click
     Certificates.

   5. Right-click the certificate in the results pane, click All Tasks, and then click Export.
     Complete the Certificate Export Wizard using the default settings to create an
     export certificate file with the name and location specified in the wizard.

   6. Use one of the following methods to add the certificate used to sign the updates
     catalog to each client computer that will use WUA to scan for the updates in the
     catalog. Add the certificate on the client computer as follows:

           For self-signed certificates: Add the certificate to the Trusted Root
           Certification Authorities and Trusted Publishers certificate stores.

           For certification authority (CA) issued certificates: Add the certificate to the
           Trusted Publishers certificate store.

        ７ Note

        The WUA also checks whether the Allow signed content from intranet
        Microsoft update service location Group Policy setting is enabled on the
        local computer. This policy setting must be enabled for WUA to scan for the
        updates that were created and published with Updates Publisher. For more
        information about enabling this Group Policy setting, see How to Configure
        the Group Policy on Client Computers.

Configuring Group Policy to allow WUA on
computers to scan for published updates
Before the Windows Update Agent (WUA) on computers will scan for updates that were
created and published with Updates Publisher, a policy setting must be enabled to allow
signed content from an intranet Microsoft update service location. When the policy
setting is enabled, WUA will accept updates received through an intranet location if the
updates are signed in the Trusted Publishers certificate store on the local computer.
