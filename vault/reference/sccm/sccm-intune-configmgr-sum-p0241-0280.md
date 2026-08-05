---
title: "Software update management documentation — pages 241-280"
type: reference
domain: sccm
slug: sccm-intune-configmgr-sum-p0241-0280
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-sum-p0241-0280
family: sccm
documentKind: "doc"
abstract: "Surface Windows Windows Windows Windows Windows Windows Windows model 10 1709 10 1803 10 1809 10 1903 10 1909 10 2004 10 20H2 Surface N/A Yes Yes Yes Yes Yes Yes Laptop 2 Surface N/A N/A N/A Yes Yes Yes Yes Laptop 3 Surface N/A Yes, with Yes, with Yes, with Yes, with Yes, with Y"
---

# Software update management documentation — pages 241-280

<!-- p.241 -->

Surface   Windows   Windows     Windows     Windows     Windows     Windows     Windows
model     10 1709   10 1803     10 1809     10 1903     10 1909     10 2004     10 20H2

Surface   N/A       Yes         Yes         Yes         Yes         Yes         Yes
Laptop
2

Surface   N/A       N/A         N/A         Yes         Yes         Yes         Yes
Laptop
3

Surface   N/A       Yes, with   Yes, with   Yes, with   Yes, with   Yes, with   Yes, with
Go                  the         the         the         the         the         the
                    product     product     product     product     product     product
                    "Windows    "Windows    "Windows    "Windows    "Windows    "Windows
                    10 S        10 S        10 S        10 S        10 S        10 S
                    version     version     version     version     version     version
                    1803 and    1809 and    1903 and    1903 and    1903 and    1903 and
                    later       later       later       later       later       later
                    Servicing   Upgrade     Upgrade     Upgrade     Upgrade     Upgrade
                    drivers"    &           &           &           &           &
                    selected    Servicing   Servicing   Servicing   Servicing   Servicing
                                drivers"    drivers"    drivers"    drivers"    drivers"
                                selected    selected    selected    selected    selected

Surface   N/A       N/A         Yes         Yes         Yes, with   Yes, with   Yes, with
Go 2                                                    the         the         the
                                                        product     product     product
                                                        "Windows    "Windows    "Windows
                                                        10 S        10 S        10 S
                                                        version     version     version
                                                        1903 and    1903 and    1903 and
                                                        later       later       later
                                                        Upgrade     Upgrade     Upgrade
                                                        &           &           &
                                                        Servicing   Servicing   Servicing
                                                        drivers"    drivers"    drivers"
                                                        selected    selected    selected

Surface   N/A       N/A         N/A         N/A         N/A         Yes         Yes
Laptop
Go

Surface   Yes       Yes         Yes         Yes         Yes         Yes         Yes
Studio

Surface   N/A       Yes         Yes         Yes         Yes         Yes         Yes
Studio
2

<!-- p.242 -->

Verify the configuration
To verify the software update point is configured correctly, use the WsyncMgr.log and
the WCM.log.

   1. Open WsyncMgr.log and check for the following log entry:

       text

       Surface Drivers can be supported in this hierarchy since all software
       update points are on Windows Server 2016, WCM SCF property Sync Catalog
       Drivers is set.
       …
       Sync Catalog Drivers SCF value is set to : 1

   2. If either of the following entries are logged in WsyncMgr.log, double check that
     you selected the Include Microsoft Surface drivers and firmware updates option
     in the properties of your software update point:

              Sync Surface Drivers option is not set
              Sync Catalog Drivers SCF value is set to : 0

   3. Open WCM.log and look for items resembling the following entries:

       text

       <Categories>
       <Category Id="Product:05eebf61-148b-43cf-80da-1c99ab0b8699"><!
       [CDATA[Windows 10 and later drivers]]></Category>
       <Category Id="Product:06da2f0c-7937-4e28-b46c-a37317eade73"><!
       [CDATA[Windows 10 Creators Update and Later Upgrade & Servicing
       Drivers]]></Category>
       <Category Id="Product:c1006636-eab4-4b0b-b1b0-d50282c0377e"><!
       [CDATA[Windows 10 S and Later Servicing Drivers]]></Category>
       … …
       </Categories>

     This entry is an XML element that lists every product group and classification that's
     currently synchronized by your software update point server. If you can't find the
     products that you've selected, double-check the products for the software update
     point are saved.

   4. You can also wait until the next synchronization finishes. Then, check whether the
     Surface driver and firmware updates are listed in Software Updates in the
     Configuration Manager console. For example, the console might display the

<!-- p.243 -->

     following information:

Frequently asked questions (FAQ)

After I follow the steps in this article, my Surface drivers
are still not synchronized. Why?
If you synchronize from an upstream Windows Server Update Services (WSUS) server,
instead of Microsoft Update, make sure that the upstream WSUS server is configured to
support and synchronize Surface driver updates. All downstream servers are limited to
updates that are present in the upstream WSUS server database.

There are more than 68,000 updates that are classified as drivers in WSUS. To prevent
non-Surface related drivers from synchronizing to Configuration Manager, Microsoft
filters driver synchronization against an allow list. After the new allow list is published
and incorporated into Configuration Manager, the new drivers are added to the console
following the next synchronization. Microsoft aims to get the Surface drivers added to
the allow list on the second Tuesday each month to make them available for
synchronization to Configuration Manager.

If your Configuration Manager environment is offline, a new allow list is imported every
time you import servicing updates to Configuration Manager. You will also have to
import a new WSUS catalog that contains the drivers before the updates are displayed
in the Configuration Manager console. Because a stand-alone WSUS environment
contains more drivers than a Configuration Manager SUP, we recommend that you
establish a Configuration Manager environment that has online capabilities, and that
you configure it to synchronize Surface drivers. This provides a smaller WSUS export
that closely resembles the offline environment.

<!-- p.244 -->

If your Configuration Manager environment is online and able to detect new updates,
you will receive updates to the list automatically. If you don’t see the expected drivers,
please review the WCM.log and WsyncMgr.log for any synchronization failures.

My Configuration Manager environment is offline, can I
manually import Surface drivers into WSUS?
No. Even if the update is imported into WSUS, the update won't be imported into the
Configuration Manager console for deployment if it isn't listed in the allow list. You must
use the Service Connection Tool to import servicing updates to Configuration Manager
to update the allow list.

What alternative methods do I have to deploy Surface
driver and firmware updates?
For information about how to deploy Surface driver and firmware updates through
alternative channels, see Manage Surface driver and firmware updates. If you want to
download the .msi or .exe file, and then deploy through traditional software deployment
channels, see Keeping Surface Firmware Updated with Configuration Manager.

My Surface drivers are expired or no longer visible after
removing my CAS. What should I do?
If you recently removed a central administration site from your hierarchy, you may
notice that the option to Include Microsoft Surface drivers and firmware updates is no
longer enabled. You may also see that the driver updates are expired in your
Configuration Manager console. When you remove a CAS, you'll need to re-enable
synchronization of Surface drivers and reconfigure this feature. For more information
about post-setup tasks for CAS removal, see Removing the central administration site
(CAS).

Next steps
For more information about Surface drivers, see the following articles:

     Considerations for Surface and Configuration Manager
     Surface Update History
     Download the latest firmware and drivers for Surface devices

<!-- p.245 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.246 -->

Integrate with Windows Update client
policies
Article • 03/31/2025

Applies to: Configuration Manager (current branch)

   Tip

  This feature was formerly known as Windows Update for Business.

Windows Update client policies allows you to keep Windows 10 or later devices in your
organization always up-to-date with the latest security defenses and Windows features
when these devices connect directly to the Windows Update (WU) service. Configuration
Manager can differentiate between Windows computers that use Windows Update
client policies and WSUS for getting software updates.

  ２ Warning

  If you are using co-management for your devices and you have moved the
  Windows Update policies to Intune, then your devices will get their Windows
  Update client policies from Intune.

        If the Configuration Manager client is still installed on the co-managed device
        then settings for Cumulative Updates and Feature Updates are managed by
        Intune. However, third-party patching, if enabled in Client Settings, is still
        managed by Configuration Manager.

Some Configuration Manager features are no longer available when Configuration
Manager clients are configured to receive updates from WU, which includes Windows
Update client policies or Windows Insiders:

      Windows Update compliance reporting:

         Configuration Manager will be unaware of the updates that are published to
         WU. The Configuration Manager clients configured to received updates from
         WU will display unknown for these updates in the Configuration Manager
         console.

<!-- p.247 -->

        Troubleshooting overall compliance status is difficult because unknown status
        was only for the clients that hadn't reported scan status back from WSUS. Now
        it also includes Configuration Manager clients that receive updates from WU.

        Definition Updates compliance is part of overall update compliance reporting
        and won't work as expected either.

     Overall Endpoint Protection reporting for Defender based on update compliance
     status won't return accurate results because of the missing scan data.

     Configuration Manager won't be able to deploy or report compliance on Microsoft
     app updates for clients configured to use Windows Update client policies to
     receive updates. This includes updates for Microsoft 365 Apps, Internet Explorer,
     Edge, and Visual Studio.

     Configuration Manager can still deploy 3rd party updates that are published to
     WSUS and managed through Configuration Manager to clients that use Windows
     Update client policies to receive updates. If you don't want any 3rd party updates
     to be installed on clients connecting to Windows Update client policies, then
     disable the client setting named Enable software updates on clients.

     Configuration Manager full client deployment that uses the software updates
     infrastructure won't work for clients that use Windows Update client policies to
     receive updates.

Identify clients that use Windows Update client
policies for Windows updates
Use the following procedure to identify clients that use Windows Update client policies
to get Windows updates and upgrades. Then configure these clients to stop using
WSUS to get updates, and deploy a client agent setting to disable the software updates
workflow for these clients.

Prerequisites for Windows Update client policies
     Clients that run Windows 10 Desktop Pro or Windows 10 Enterprise Edition version
     1511 or later

     Windows Update client policies is deployed and clients use Windows Update client
     policies to get Windows updates and upgrades.

<!-- p.248 -->

To identify clients that use Windows Update client
policies
   1. Ensure the Windows Update Agent isn't scanning against WSUS, if it was
     previously enabled. The following registry key can be used to indicate whether the
     computer is scanning against WSUS or Windows Update. If the registry key doesn't
     exist, it's not scanning against WSUS.
     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU\UseWUS
     erver

   2. There's a new attribute, UseWUServer, under the Windows Update node in
     Configuration Manager Resource Explorer.

   3. Create a collection based on the UseWUServer attribute for all the computers that
     use Windows Update client policies for updates and upgrades. You can create a
     collection based on a query similar to the one below:

       wql

       Select sr.* from SMS_R_System as sr join SMS_G_System_WINDOWSUPDATE as
       su on sr.ResourceID=su.ResourceID where su.UseWUServer is null

   4. Create a client agent setting to disable the software update workflow. Deploy the
     setting to the collection of computers that are connected directly to Windows
     Update client policies.

   5. The computers that are managed via Windows Update client policies will display
     Unknown in the compliance status and won't be counted as part of the overall
     compliance percentage.

Configure deferral policies with Windows
Update client policies
You can configure deferral policies for Windows 10 or later Feature Updates or Quality
Updates for Windows devices managed directly by Windows Update client policies. You
can manage the deferral policies in the new Windows Update for Business Policies
node under Software Library > Windows Servicing.

  ７ Note

<!-- p.249 -->

 You can set deferral policies for Windows Insider. For more information about the
 Windows Insider program, see Getting started with Windows Insider program for
 Business.

Prerequisites for deferral policies
    Windows 10 version 1703 or later
    Windows 10 or later devices managed by Windows Update client policies must
    have Internet connectivity

To create a deferral policy with Windows Update client policies

  1. In Software Library > Windows Servicing > Windows Update for Business
    Policies
  2. On the Home tab, in the Create group, select Create Windows Update for
    Business Policy to open the Create Windows Update for Business Policy Wizard.
  3. On the General page, provide a name and description for the policy.
  4. On the Deferral Policies page, configure whether to defer or pause Feature
    Updates. Feature Updates are generally new features for Windows. After you
    configure the Branch readiness level setting, you can then define if, and for how
    long, you would like to defer receiving Feature Updates following their availability
    from Microsoft.

         Branch readiness level: Set the branch for which the device will receive
         Windows updates. Choose either Semi-Annual Channel (Targeted), Semi-
         Annual Channel, or a Windows Insider build.

               ７ Note

               Deploy policies for Semi-Annual Channel to Windows 10, version 1903
               or later. Deploy policies for Semi-Annual Channel (Targeted) to
               Windows 10, version 1809 or earlier.

               If you deploy a policy for Semi-Annual Channel (Targeted) to Windows
               10, version 1903 or later, the deployment fails with the error
               0x8004100c.

         Deferral period (days): Specify the number of days for which Feature
         Updates will be deferred. You can defer receiving these Feature Updates for
         up to 365 days from their release.

<!-- p.250 -->

         Pause Features Updates starting: Select whether to pause devices from
         receiving Feature Updates for up to 35 days from the time you pause the
         updates. After the maximum days have passed, pause functionality will
         automatically expire and the device will scan Windows Updates for applicable
         updates. Following this scan, you can pause the updates again. You can
         unpause Feature Updates by clearing the checkbox.
  5. Choose whether to defer or pause Quality Updates. Quality Updates are generally
    fixes and improvements to existing Windows functionality and are typically
    published the second Tuesday of every month, though can be released at any time
    by Microsoft. You can define if, and for how long, you would like to defer receiving
    Quality Updates following their availability.

         Deferral period (days): Specify the number of days for which Quality Updates
         will be deferred. You can defer receiving these Quality Updates for up to 30
         days from their release.
         Pause Quality Updates starting: Select whether to pause devices from
         receiving Quality Updates for up to 35 days from the time you pause the
         updates. After the maximum days have passed, pause functionality will
         automatically expire and the device will scan Windows Updates for applicable
         updates. Following this scan, you can pause the updates again. You can
         unpause Quality Updates by clearing the checkbox.

  6. Select Install updates from other Microsoft Products to enable the group policy
    setting that make deferral settings applicable to Microsoft Update, as well as
    Windows Updates.
  7. Select Include drivers with Windows Update to automatically update drivers from
    Windows Updates. If you clear this setting, driver updates aren't downloaded from
    Windows Updates.
  8. Complete the wizard to create the new deferral policy.

To deploy a deferral policy with Windows Update client policies

  1. In Software Library > Windows Servicing > Windows Update for Business
    Policies
  2. On the Home tab, in the Deployment group, select Deploy Windows Update for
    Business Policy.
  3. Configure the following settings:

         Configuration policy to deploy: Select the Windows Update client policy that
         you would like to deploy.
         Collection: Click Browse to select the collection where you want to deploy
         the policy.

<!-- p.251 -->

           Allow remediation outside the maintenance window: If a maintenance
           window has been configured for the collection to which you're deploying the
           policy, enable this option to let policy settings remediate the value outside of
           the maintenance window. For more information about maintenance windows,
           see How to use maintenance windows.
           Schedule: Specify the compliance evaluation schedule by which the deployed
           policy is evaluated on client computers. The schedule can be either a simple
           or a custom schedule.
   4. Complete the wizard to deploy the policy.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.252 -->

Enable third-party updates
Article • 10/08/2024

Applies to: Configuration Manager (current branch)

The Third-Party Software Update Catalogs node in the Configuration Manager console
allows you to subscribe to third-party catalogs, publish their updates to your software
update point (SUP), and then deploy them to clients.

Prerequisites
      Sufficient disk space on the top-level software update point's WSUSContent
      directory to store the source binary content for third-party software updates.
         The amount of required storage varies based on the vendor, types of updates,
         and specific updates that you publish for deployment.
         If you need to move the WSUSContent directory to another drive with more free
         space, see the How to change the location where WSUS stores updates locally
         blog post.
      The third-party software update synchronization service requires internet access.
         For the partner catalogs list, download.microsoft.com over HTTPS port 443 is
         needed.
         Internet access to any third-party catalogs and update content files. Additional
         ports other than 443 may be needed.
         Third-party updates use the same proxy settings as the SUP.

Additional requirements when the SUP is
remote from the top-level site server
   1. SSL should be enabled on the SUP when it's remote. This requires a server
      authentication certificate generated from an internal certificate authority or via a
      public provider.

            Configure SSL on WSUS
               When you configure SSL on WSUS, note some of the web services and the
               virtual directories are always HTTP and not HTTPS.
               Configuration Manager downloads third-party content for software update
               packages from your WSUS content directory over HTTP.
            Configure SSL on the SUP

<!-- p.253 -->

   2. When setting the third-party updates WSUS signing certificate configuration to
     Configuration Manager manages the certificate in the Software Update Point
     Component Properties, the following configurations are required to allow the
     creation of the self-signed WSUS signing certificate:

           Remote registry should be enabled on the SUP server.
           The WSUS server connection account should have remote registry
           permissions on the SUP/WSUS server.

   3. Create the following registry key on the Configuration Manager site server:

           HKLM\Software\Microsoft\Update Services\Server\Setup , create a new

           DWORD named EnableSelfSignedCertificates with a value of 1 .

   4. To enable installing the self-signed WSUS signing certificate to the Trusted
     Publishers and Trusted Root stores on the remote SUP server:

           The WSUS server connection account should have remote administration
           permissions on the SUP server.

           If this item isn't possible, export the certificate from the local computer's
           WSUS store into the Trusted Publisher and Trusted Root stores.

  ７ Note

  The WSUS server connection account can be identified by viewing the Proxy and
  Account Settings tab on the Site System role properties of the SUP. If an account is
  not specified, the site server's computer account is used.

Enable third-party updates on the SUP
If you enable this option, you can subscribe to third-party update catalogs in the
Configuration Manager console. You can then publish those updates to WSUS and
deploy them to clients. The following steps should be run once per hierarchy to enable
and set up the feature for use. The steps may need to be rerun if you ever replace the
top-level SUP's WSUS server.

   1. In the Configuration Manager console, go to the Administration workspace.
     Expand Site Configuration, and select the Sites node.

   2. Select the top-level site in the hierarchy. In the ribbon, select Configure Site
     Components, and select Software Update Point.

<!-- p.254 -->

   3. Switch to the Third-Party Updates tab. Select the option Enable third-party
     software updates.

Configure the WSUS signing certificate
You'll need to decide if you want Configuration Manager to automatically manage the
third-party WSUS signing certificate using a self-signed certificate, or if you need to
manually configure the certificate.

Automatically manage the WSUS signing certificate
If you don't have a requirement to use PKI certificates, you can choose to automatically
manage the signing certificates for third-party updates. The WSUS certificate
management is done as part of the sync cycle and gets logged in the wsyncmgr.log .

<!-- p.255 -->

   1. In the Configuration Manager console, go to the Administration workspace.
      Expand Site Configuration, and select the Sites node.
   2. Select the top-level site in the hierarchy. In the ribbon, select Configure Site
      Components, and select Software Update Point.
   3. Switch to the Third-Party Updates tab. Select the option Configuration Manager
      manages the certificate.
   4. A new certificate of type Third-party WSUS Signing is created in the Certificates
      node under Security in the Administration workspace.

Manually manage the WSUS signing certificate
If you need to manually configure the certificate, such as needing to use a PKI certificate,
you'll need to use either System Center Updates Publisher or another tool to do so.

   1. Configure the signing certificate using System Center Updates Publisher.
   2. In the Configuration Manager console, go to the Administration workspace.
      Expand Site Configuration, and select the Sites node.
   3. Select the top-level site in the hierarchy. In the ribbon, select Configure Site
      Components, and select Software Update Point.
   4. Switch to the Third-Party Updates tab. Select the option for Manually manage the
      certificate.

Enable third-party updates on the clients
Enable third-party updates on the clients in the client settings. The setting sets the
Windows Update agent policy for Allow signed updates for an intranet Microsoft update
service location. This client setting also installs the WSUS signing certificate to the
Trusted Publisher store on the client. The certificate management logging is seen in
updatesdeployment.log on the clients. Run these steps for each custom client setting
you want to use for third-party updates. For more information, see the About client
settings article.

   1. In the Configuration Manager console, go to the Administration workspace and
      select the Client Settings node.
   2. Select an existing custom client setting or create a new one.
   3. Select the Software Updates tab on the left-hand side. If you don't have this tab,
      make sure that the Software Updates box is enabled.
   4. Set Enable third-party software updates to Yes.

Add a custom catalog

<!-- p.256 -->

Partner catalogs are software vendor catalogs that have their information already
registered with Microsoft. With partner catalogs, you can subscribe to them without
having to specify any additional information. Catalogs that you add are called custom
catalogs. You can add a custom catalog from a third-party update vendor to
Configuration Manager. Custom catalogs must use https and the updates must be
digitally signed.

   1. Go to the Software Updates Library workspace, expand Software updates, and
     select the Third-Party Software Update Catalogs node.

   2. select Add Custom Catalog in the ribbon.

   3. On the General page, specify the following items:

           Download URL: A valid HTTPS address of the custom catalog.
           Publisher: The name of the organization that publishes the catalog.
           Name: The name of the catalog to display in the Configuration Manager
           Console.
           Description: A description of the catalog.

<!-- p.257 -->

           Support URL (optional): A valid HTTPS address of a website to get help with
           the catalog.
           Support Contact (optional): Contact information to get help with the catalog.

   4. Select Next to review the catalog summary and to continue with completing the
     Third-party Software Updates Custom Catalog Wizard.

Subscribe to a third-party catalog and sync
updates
When you subscribe to a third-party catalog in the Configuration Manager console, the
metadata for every update in the catalog are synced into the WSUS servers for your
SUPs. The sync of the metadata allows the clients to determine if any of the updates are
applicable. Perform the following steps for each third-party catalog to which you want
to subscribe:

   1. In the Configuration Manager console, go to the Software Library workspace.
     Expand Software Updates and select the Third-Party Software Update Catalogs
     node.
   2. Select the catalog to subscribe and then select Subscribe to Catalog in the ribbon.

   3. Review and approve the catalog certificate on the Review and approve page of the
     wizard.

        ７ Note

        When you subscribe to a third-party software update catalog, the certificate
        that you review and approve in the wizard is added to the site. This certificate
        is of type Third-party Software Updates Catalog. You can manage it from the
        Certificates node under Security in the Administration workspace.

   4. If the third-party catalog is v3, you'll be offered pages to Select Categories and
     Stage Content. For more information about configuring these options, see the
     Third-party v3 catalog options section.
   5. Choose your options on the Schedule page:

<!-- p.258 -->

           Simple schedule: Choose the hour, day, or month interval. The default is a
           simple schedule that synchronizes every 7 days.
           Custom schedule: Set a complex schedule.
   6. Review your settings on the Summary page and complete the wizard.
   7. After the catalog is downloaded, the product metadata needs to be synchronized
     from the WSUS database into the Configuration Manager database. Manually start
     the software updates synchronization to synchronize the product information.
   8. Once the product information is synchronized, Configure the SUP to synchronize
     the desired product into Configuration Manager.
   9. Manually start the software updates synchronization to synchronize the new
     product's updates into Configuration Manager.
 10. When the synchronization completes, you can see the third-party updates in the
     All Updates node. These updates are published as metadata-only updates until
     you choose to publish them.

           The icon with the blue arrow represents a metadata-only software update.

Publish and deploy third-party software
updates
Once the third-party updates are in the All Updates node, you can choose which
updates should be published for deployment. When you publish an update, the binary
files are downloaded from the vendor and placed into the WSUSContent directory on the
top-level SUP.

   1. In the Configuration Manager console, go to the Software Library workspace.
     Expand Software Updates and select the All Software Updates node.

   2. Select Add Criteria to filter the list of updates. For example, add Vendor for HP. to
     view all updates from HP.

   3. Select the updates that are required by your organization. Select Publish Third-
     Party Software Update Content.

           This action downloads the update binaries from the vendor then stores them
           in the WSUSContent directory on the top-level software update point.

   4. Manually start the software updates synchronization to change the state of the
     published updates from metadata-only to deployable updates with content.

<!-- p.259 -->

       ７ Note

       When you publish third-party software update content, any certificates used
       to sign the content are added to the site. These certificates are of type Third-
       party Software Updates Content. You can manage them from the Certificates
       node under Security in the Administration workspace.

   5. Review the progress in the SMS_ISVUPDATES_SYNCAGENT.log . The log is located on
     the top-level software update point in the site system Logs folder.

   6. Deploy the updates using the Deploy software updates process.

   7. On the Download Locations page of the Deploy Software Updates Wizard, select
     the default option to Download software updates from the internet. In this
     scenario, the content is already published to the software update point, which is
     used to download the content for the deployment package.

   8. Clients will need to run a scan and evaluate updates before you can see
     compliance results. You can manually trigger this cycle from the Configuration
     Manager control panel on a client by running the Software Updates Scan Cycle
     action.

Third-party v3 catalog options
V3 catalogs allow for categorized updates. When using catalogs that include
categorized updates, you can configure synchronization to include only specific
categories of updates to avoid synchronizing the entire catalog. With categorized
catalogs, when you're confident you'll deploy a category, you can configure it to
automatically download and publish to WSUS.

  ） Important

  This option is only available for v3 third-party update catalogs, which support
  categories for updates. These options are disabled for catalogs that aren't
  published in the v3 format.

   1. In the Configuration Manager console, go to the Software Library workspace.
     Expand Software Updates and select the Third-Party Software Update Catalogs
     node.

   2. Select the catalog to subscribe and select Subscribe to Catalog in the ribbon.

<!-- p.260 -->

3. Choose your options on the Select Categories page:

       Synchronize all update categories (default)
          Synchronizes all updates in the third-party update catalog into
          Configuration Manager.

       Select categories for synchronization
          Choose which categories and child categories to synchronize into
          Configuration Manager.

4. Choose if you want to Stage update content for the catalog. When you stage the
  content, all updates in the selected categories are automatically downloaded to
  your top-level software update point meaning you don't need to ensure they're
  already downloaded before deploying. You should only automatically stage
  content for updates you are likely to deploy to avoid excessive bandwidth and
  storage requirements.

       Do not stage content, synchronize for scanning only (recommended)
          Don't download any content for updates in the third-party catalog
       Stage the content for selected categories automatically

<!-- p.261 -->

             Choose the update categories that will automatically download content.
             The content for updates in selected categories will be downloaded to the
             top-level software update point's WSUS content directory.

   5. Set your Schedule for catalog synchronization, then complete the wizard.

Edit an existing subscription
You can edit an existing subscription by selecting Properties from the ribbon or the
right-click menu.

  ） Important

  Some options are only available for v3 third-party update catalogs, which support
  categories for updates. These options are disabled for catalogs that aren't
  published in the v3 format.

   1. In the Third-Party Software Update Catalogs node, right-click on the catalog and
     select Properties or select Properties from the ribbon.

<!-- p.262 -->

2. You can view the following information from the General tab, but not edit the
  information:

    ７ Note

    If you need to change any of the information here, you have to add a new
    custom catalog.
    Provided the download URL is unchanged, the existing catalog must be
    removed before one with the same download URL can be added.

       Download URL: The HTTPS address of the custom catalog.
       Publisher: The name of the organization that publishes the catalog.
       Name: The name of the catalog to display in the Configuration Manager
       Console.
       Description: A description of the catalog.
       Support URL: A valid HTTPS address of a website to get help with the
       catalog.
       Support Contact: Contact information to get help with the catalog.

3. Choose your options on the Select Categories tab.

       Synchronize all update categories (default)
          Synchronizes all updates in the third-party update catalog into
          Configuration Manager.
       Select categories for synchronization
          Choose which categories and child categories to synchronize into
          Configuration Manager.

4. Choose your options for the Stage update content tab.

       Do not stage content, synchronize for scanning only (recommended)
          Don't download any content for updates in the third-party catalog
       Stage the content for selected categories automatically
          Choose the update categories that will automatically download content.
          The content for updates in selected categories will be downloaded to the
          top-level software update point's WSUS content directory.

5. Select how often to synchronize the catalog on the Schedule tab.

       Simple schedule: Choose the hour, day, or month interval.
       Custom schedule: Set a complex schedule.

<!-- p.263 -->

Unsubscribe from catalog and delete custom
catalogs
In the Third-Party Software Update Catalogs node, right-click on the catalog and select
Unsubscribe to stop synchronizing the catalog.
You can also use the Unsubscribe option from the ribbon. When you unsubscribe from a
catalog, the approval for catalog signing and update content certificates are removed.
Existing updates aren't removed, but you may not be able to deploy them. With custom
catalogs, you also have the option of deleting it after you've unsubscribed. Select Delete
Custom Catalog from either the ribbon or the right-click menu for the catalog. Deleting
the custom catalog removes it from view in the Third-Party Software Update Catalogs
node.

Monitoring progress of third-party software
updates
Synchronization of third-party software updates is handled by the
SMS_ISVUPDATES_SYNCAGENT component on the top-level default software update
point. You can view status messages from this component, or see more detailed status
in the SMS_ISVUPDATES_SYNCAGENT.log . This log is on the top-level software update point
in the site system Logs folder. By default this path is C:\Program Files\Microsoft
Configuration Manager\Logs. For more information on monitoring the general software
update management process, see Monitor software updates.

List additional third-party updates catalogs
To help you find custom catalogs that you can import for third-party software updates,
there's a documentation page with links to catalog providers. Starting in Configuration
Manager 2107, you can also choose More Catalogs from the ribbon in the Third-party
software update catalogs node. Right-clicking on Third-Party Software Update
Catalogs node displays a More Catalogs menu item. Selecting More Catalogs opens a
link to a documentation page containing a list of additional third-party software update
catalog providers.

<!-- p.264 -->

Known issues
  The machine where the console is running is used to download the updates from
  WSUS and add it to the updates package. The WSUS signing certificate must be
  trusted on the console machine. If it isn't, you may see issues with the signature
  check during the download of third-party updates.
  The third-party software update synchronization service can't publish content to
  metadata-only updates that were added to WSUS by another application, tool, or
  script, such as SCUP. The Publish third-party software update content action fails
  on these updates. If you need to deploy third-party updates that this feature
  doesn't yet support, use your existing process in full for deploying those updates.
  Configuration Manager has a new version for the catalog cab file format. The new
  version includes the certificates for the vendor's binary files. These certificates are
  added to the Certificates node under Security in the Administration workspace
  once you approve and trust the catalog.
     You can still use the older catalog cab file version as long as the download URL
     is https and the updates are signed. The content will fail to publish because the
     certificates for the binaries aren't in the cab file and already approved. You can
     work around this issue by finding the certificate in the Certificates node,
     unblocking it, then publish the update again. If you're publishing multiple
     updates signed with different certificates, you'll need to unblock each certificate
     that is used.
     For more information, see status messages 11523 and 11524 in the below status
     message table.
  When the third-party software update synchronization service on the top-level
  software update point requires a proxy server for internet access, digital signature
  checks may fail. To mitigate this issue, configure the WinHTTP proxy settings on
  the site system. For more information, see Netsh commands for WinHTTP.

<!-- p.265 -->

   When using a CMG for content storage, the content for third-party updates won't
   download to clients if the Download delta content when available client setting is
   enabled.
   If the catalog provider has changed the catalog's signing certificate since you last
   approved it or subscribed, the catalog sync will fail until the certification is
   approved in the Certificates node. For more information, see MessageID 11508 in
   status messages table.

Status messages
                                                                                ﾉ     Expand table

MessageID   Severity   Description                          Possible cause     Possible solution

11508       Error      Failure when checking signature      The signing        Make sure to
                       for catalog <catalog name> to        certification on   review and
                       WSUS. Make sure the catalog is       the catalog        approve the
                       subscribed and the catalog           may have           certificate in the
                       certificate <certificate> is not     changed since      Certificates node
                       blocked. See                         it was             to allow the
                       SMS_ISVUPDATES_SYNCAGENT.log         originally         catalog to
                       for further details.                 subscribed or      synchronize.
                                                            last approved.

11516       Error      Failed to publish content for        Configuration      Publish the update
                       update "Update ID" because the       Manager            in an alternate
                       content is unsigned. Only            doesn't allow      way.
                       content with valid signatures can    unsigned
                       be published.                        updates to be      See if a signed
                                                            published.         update is available
                                                                               from the vendor.

11523       Warning    Catalog "X" does not include         This message       Contact the
                       content signing certificates,        can occur          catalog provider
                       attempts to publish update           when you           to obtain an
                       content for updates from this        import a           updated catalog
                       catalog may be unsuccessful          catalog that is    that includes the
                       until content signing certificates   using an older     content signing
                       are added and approved.              version of the     certificates.
                                                            cab file format.
                                                                               The certificates for
                                                                               the binaries aren't
                                                                               included in the
                                                                               cab file so the
                                                                               content will fail to
                                                                               publish. You can
                                                                               work around this

<!-- p.266 -->

 MessageID   Severity   Description                         Possible cause   Possible solution

                                                                             issue by finding
                                                                             the certificate in
                                                                             the Certificates
                                                                             node, unblocking
                                                                             it, then publish the
                                                                             update again. If
                                                                             you're publishing
                                                                             multiple updates
                                                                             signed with
                                                                             different
                                                                             certificates, you'll
                                                                             need to unblock
                                                                             each certificate
                                                                             that is used.

 11524       Error      Failed to publish update "ID" due   The update       Synchronize the
                        to missing update metadata.         may have been    update with
                                                            synchronized     Configuration
                                                            to WSUS          Manager before
                                                            outside of       attempting to
                                                            Configuration    publish it's
                                                            Manager.         content.

                                                                             If an external tool
                                                                             was used to
                                                                             publish the update
                                                                             as Metadata only,
                                                                             then use the same
                                                                             tool to publish the
                                                                             update content.

Working with third-party updates video
https://www.youtube-nocookie.com/embed/ai8rLCLtuTI?rel=0

PowerShell
You can use the following PowerShell cmdlets to automate the management of third-
party updates in Configuration Manager:

     Get-CMThirdPartyUpdateCatalog
     New-CMThirdPartyUpdateCatalog
     Remove-CMThirdPartyUpdateCatalog
     Set-CMThirdPartyUpdateCatalog

<!-- p.267 -->

     Publish-CMThirdPartySoftwareUpdateContent
     Get-CMThirdPartyUpdateCategory
     Set-CMThirdPartyUpdateCategory

Next step
  Deploy software updates

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.268 -->

Available third-party software update
catalogs
Article • 04/18/2024

Applies to: Configuration Manager (current branch)

The Third-Party Software Update Catalogs node in the Configuration Manager console
allows you to subscribe to third-party catalogs, publish their updates to your software
update point (SUP), and then deploy them to clients. You can add custom catalogs from
third-party vendors.

Third-party update catalogs available for
import
To make it easier to find custom catalogs, we're providing a list of links as a
convenience. Some catalogs are freely available and some catalogs have an additional
cost associated with them. This list includes catalogs that may only work with System
Center Updates Publisher and not the Third-Party Software Update Catalogs node in
the Configuration Manager console. Check with the catalog provider for details
including pricing, support, and if the catalog supports in-console third-party updates.

                                                                               ﾉ   Expand table

 Custom           URL
 catalog
 provider

 Adobe            Multiple catalogs are available from Adobe.
                  https://www.adobe.com/devnet-
                  docs/acrobatetk/tools/DesktopDeployment/sccm.html

 Centero          https://centero.fi/centero-software-manager/product-editions/#csm-for-mecm
 Software
 Manager

 Dell             Partner catalog available in the Third-Party Software Update Catalogs node
                  https://www.dell.com/support/article/sln311138/

                  https://downloads.dell.com/Catalog/DellSDPCatalogPC.cab

<!-- p.269 -->

 Custom          URL
 catalog
 provider

                 https://downloads.dell.com/Catalog/DellSDPCatalog.cab

 Fujitsu         https://support.ts.fujitsu.com/GFSMS/globalflash/FJSVUMCatalogForSCCM.cab

 HP              Partner catalog available in the Third-Party Software Update Catalogs node
                 https://hpia.hpcloud.hp.com/downloads/sccmcatalog/HpCatalogForSms.latest.cab

                 http://ftp.hp.com/pub/softlib/software/sms_catalog/HpCatalogForSms.latest.cab

 Ivanti Patch    https://www.ivanti.com.au/products/patch-management-for-mem
 for MEM

 Lenovo          Partner catalog available in the Third-Party Software Update Catalogs node
                 https://download.lenovo.com/luc/v3/LenovoUpdatesCatalogv3.cab

                 Lenovo updates catalog V3 information
                 https://thinkdeploy.blogspot.com/2020/06/lenovo-updates-catalog-v3-for-
                 sccm.html

                 Lenovo Patch
                 https://www.lenovo.com/us/en/software/lenovo-patch-sccm

 ManageEngine    https://www.manageengine.com/sccm-third-party-patch-management
 Patch Connect
 Plus

 Patch My PC     Full catalog
                 https://patchmypc.com/third-party-patch-management-for-sccm-and-intune

                 Limited catalog
                 https://patchmypc.com/frequently-asked-questions#trial-catalog

 SolarWinds      https://www.solarwinds.com/patch-manager/use-cases/third-party-patch-
 Patch           management-sccm
 Manager

Open this article from the Configuration
Manager console
Starting in Configuration Manager 2107, you can choose More Catalogs from the
ribbon in the Third-party software update catalogs node to get to this article. Right-

<!-- p.270 -->

clicking on Third-Party Software Update Catalogs node displays a More Catalogs menu
item. Selecting More Catalogs opens a link to this page.

Next steps
     Add custom catalogs for third party software updates
     Configure the SUP to synchronize the product into Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.271 -->

Example scenario to deploy and monitor
monthly software updates
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This topic provides an example scenario of how you can use software updates in
Configuration Manager to deploy and monitor the security software updates that
Microsoft releases monthly.

In this scenario, we follow the actions of the Configuration Manager administrator at
Woodgrove Bank. The administrator needs to create a software update deployment
strategy with the following conditions and requirements:

      Active software update deployment occurs one week after Microsoft releases the
      security software updates on the second Tuesday of each month. This event is
      typically referred to as Patch Tuesday.

      Software updates are downloaded and staged on distribution points. Then a
      deployment is tested to a subset of clients before the ConfigMgr Admin fully
      deploys the software updates in his production environment.

      The administrator must be able to monitor the software updates' compliance by
      month or by year.

      This scenario assumes that the software update point infrastructure has already
      been implemented. Use the following information to plan for and configure
      software updates in Configuration Manager.

                                                                                ﾉ   Expand table

 Process                                                                        Reference

 Review the key concepts for software updates.                                  Introduction to
                                                                                software updates

 Plan for software updates. This information helps you to plan for capacity     Plan for software
 considerations, determine the software update point infrastructure, software   updates
 update point installation, synchronization settings, and client settings for
 software updates.

 Configure software updates. This information helps you to install and          Synchronize
 configure software update points in your hierarchy and helps to configure      software updates
 and synchronize software updates.

<!-- p.272 -->

 Process                                                                       Reference

 In this scenario, our ConfigMgr Admin configures the software updates
 synchronization schedule to occur on the second Wednesday of each month
 to ensure that they retrieve the latest security software updates from
 Microsoft.

The following sections in this topic provide example steps to help you to deploy and
monitor Configuration Manager security software updates in your organization.

Step 1: Create a software update group for
yearly compliance
The Configuration Manager administrator creates a software update group that can be
used to monitor compliance for all of the security software updates that they release in
2016. The admin performs the steps in the following table.

                                                                               ﾉ   Expand table

 Process                                                                      Reference

 From the All Software Updates node in the Configuration Manager console,     No additional
 the Configuration Manager administrator adds criteria to display only        information
 security software updates that are released or revised in year 2015 that
 meet the following criteria:

       Criteria: Date Released or Revised
       Condition: is greater than or equal to specific date
       Value: 1/1/2015
       Criteria: Update Classification
       Value: Security Updates
       Criteria: Expired
       Value: No

 ConfigMgr Administrator adds all of the filtered software updates to a new   Add software
 software update group with the following requirements:                       updates to an
                                                                              update group

       Name: Compliance Group - Microsoft Security Updates 2015
       Description: Software updates

<!-- p.273 -->

Step 2: Create an automatic deployment rule
for the current month
The Configuration Manager administrator creates an automatic deployment rule for the
security software updates that are released by Microsoft for the current month. The
admin performs the steps in the following table.

                                                                                 ﾉ   Expand table

 Process                                                                        Reference

 ConfigMgr Admin creates an automatic deployment rule with the following        Automatically
 requirements:                                                                  deploy software
                                                                                updates

    1. On the General tab, the ConfigMgr Admin configures the following:

            Specifies Monthly Security Updates for the name.
            Selects a test collection with limited clients.
            Selects Create a new Software Update Group.
            Verifies that Enable the deployment after this rule is run is not
            selected.

    2. On the Deployment Settings tab, the ConfigMgr Admin selects the
       default settings.
    3. On the Software Updates page, the ConfigMgr Admin configures the
      following property filters and search criteria:

            Date Released or Revised Last 1 month.
            Update Classification Security Updates.

    4. On the Evaluation page, the ConfigMgr Admin enables the rule to run
      on a schedule for the second Thursday of every month. The
      ConfigMgr Admin also verifies that his synchronization schedule is set
      to run on the second Wednesday of every month.
    5. The ConfigMgr Admin uses the default settings on the Deployment
       Schedule, User Experience, Alerts, and Download Settings pages.
    6. On the Deployment Package page, the ConfigMgr Admin specifies a
       new deployment package.
    7. The ConfigMgr Admin uses the default settings on the Download
      Location and Language Selection pages.

Step 3: Verify that software updates are ready
to deploy

<!-- p.274 -->

On the second Thursday of every month, the ConfigMgr Admin verifies that the software
updates are ready to deploy. The admin performs the following step.

                                                                                  ﾉ   Expand table

 Process                                                             Reference

 The ConfigMgr Admin verifies that software updates                  Software updates
 synchronization completed successfully.                             synchronization status

Step 4: Deploy the software update group
After the ConfigMgr Admin verifies that the software updates are ready to deploy, they
deploy the software updates. The admin performs the steps in the following table.

                                                                                  ﾉ   Expand table

 Process                                                                      Reference

 The ConfigMgr Admin creates two test deployments for the new software        Deploy software
 update group. The admin considers the following environments for each        updates
 deployment:

 Workstation test deployment: the ConfigMgr Admin considers the
 following for the workstation test deployment:

       Specifies a deployment collection that contains a subset of
       workstation clients to verify the deployment.
       Configures the deployment settings that are appropriate for the
       workstation clients in his environment.

 Server test deployment: the ConfigMgr Admin considers the following
 for the server test deployment:

       Specifies a deployment collection that contains a subset of server
       clients to verify the deployment.
       Configures the deployment settings that are appropriate for the
       server clients in his environment.

 The ConfigMgr Admin verifies that the test deployments have successfully     Software updates
 deployed.                                                                    deployment status

 The ConfigMgr Admin updates the two deployments with new collections         No additional
 that include his production workstations and servers.                        information

<!-- p.275 -->

Step 5: Monitor compliance for deployed
software updates
The ConfigMgr Admin monitors compliance of his software update deployments. The
admin performs the step in the following table.

                                                                              ﾉ   Expand table

 Process                                                                      Reference

 The ConfigMgr Admin monitors the software updates deployment status in the   Monitor
 Configuration Manager console and checks the software update deployment      software
 reports available from the console.                                          updates

Step 6: Add monthly software updates to the
yearly update group
The ConfigMgr Admin adds the software updates from the monthly software update
group to the yearly software update group. The admin performs the step in the
following table.

                                                                              ﾉ   Expand table

 Process                                                                   Reference

 The ConfigMgr Admin selects the software updates from the monthly         Add software
 software update group and adds the software updates to the software       updates to a
 updates group that were created for yearly compliance. The admin tracks   deployed update
 the software update compliance and creates various reports for his        group
 management.

The ConfigMgr Admin has successfully completed his monthly deployment for security
software updates. The admin continues to monitor and report on software update
compliance to ensure that the clients in his environment are within acceptable
compliance levels.

Recurring monthly process to deploy software
updates
After the first month that our ConfigMgr Admin deploys software updates, the admin
performs steps three through six to deploy the monthly security software updates

<!-- p.276 -->

released by Microsoft.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.277 -->

System Center Updates Publisher
Article • 06/20/2024

Applies to: System Center Updates Publisher

System Center Updates Publisher (Updates Publisher) is a stand-alone tool that enables
independent software vendors or line-of-business application developers to manage
custom updates. This custom updates management includes updates that have
dependencies, like drivers and update bundles.

Using Updates Publisher, you can:

      Import updates from external catalogs (non-Microsoft update catalogs).
      Modify update definitions including applicability, and deployment metadata.
      Export updates to external catalogs.
      Publish updates to an update server.

After you publish updates to an update server, you can then use Configuration Manager
to detect and deploy those updates to your managed devices.

  ） Important

  The System Center Updates Publisher (SCUP) and Integration with Configuration
  manager is unsupported starting January 31, 2024.

  "Support" in this context refers to both engineering and assisted technical support.
  No further engineering development will occur, and users are unable to receive
  phone or online assisted technical support.

  The information in this section is provided to help you plan for alternatives to using
  this feature, and will be removed in the future.

Workspaces
When you open Updates Publisher, it defaults to the Overview node of the Updates
Workspace.

<!-- p.278 -->

Updates Publisher has four workspaces to help organize it.

Updates Workspace: Use this workspace to create and manage software updates and
update bundles. This workspace includes assigning updates and bundles to a
publication, publishing, and exporting to another Updates Publisher repository.

Publications Workspace: This workspace is where you manage publications. A
publication is group of updates you create to simplify the export and publishing of the
updates.

Managing publications includes publishing updates to a server so your clients can find
and install them, exporting updates and bundles for use by other Updates Publisher
installations, or modifying the contents of or details of a publication.

Rules Workspace: Here is where you manage applicability rules that can be saved and
then used with updates you deploy. There are two types of rules:

     Installable rules – These rules help determine if a client should install an update.
     Installed rules – These rules verify if an update is already installed.

Catalogs Workspace: Use this workspace to add and manage software update catalogs.
This workspace includes the import of software updates from those catalogs to the

<!-- p.279 -->

Updates Publisher repository.

What's new in System Center Updates Publisher

  ７ Note

  The latest version of System Center Updates Publisher was released on November
  6, 2019. For more information, see the Release history section.

  ） Important

  The System Center Updates Publisher (SCUP) and Integration with Configuration
  manager will be deprecated on January 31, 2024.

There's a new authoring mode System Center Updates Publisher to help you author
your updates. When you enable authoring mode, a Categories Workspace is added to
the start screen. A new Detectoid button is also added to the Updates Workspace when
authoring mode is enabled.

To enable authoring mode
   1. In upper left corner of the console, click on the Updates Publisher Properties tab,
     and then choose Options.
   2. Go to the Authoring options.
   3. Check the box for Enable authoring mode.

<!-- p.280 -->

About the categories workspace
The categories workspace enables update authors to organize updates that belong
together. For instance, if you're an OEM, you might wish to organize your updates based
on models or product lines. You can define multiple categories and child categories but
not grand child categories as you're limited to two levels.
