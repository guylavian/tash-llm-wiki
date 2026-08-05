---
title: "Administration service documentation"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-adminservice
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-adminservice
family: sccm
documentKind: "doc"
abstract: "Tell us about your PDF experience. Administration service documentation Developer documentation for the Configuration Manager REST API About administration service ｅ OVERVIEW What is the administration service? ｃ HOW-TO GUIDE How to set up How to use What is the administration s"
---

# Administration service documentation

<!-- p.1 -->

                                                          Tell us about your PDF experience.

Administration service documentation
Developer documentation for the Configuration Manager REST API

  About administration service

  ｅ OVERVIEW
  What is the administration service?

  ｃ HOW-TO GUIDE
  How to set up

  How to use

<!-- p.2 -->

What is the administration service in
Configuration Manager?
Article • 11/07/2023

Applies to: Configuration Manager (current branch)

The SMS Provider provides API interoperability access over HTTPS, called the
administration service. The administration service is a representational state transfer
(REST) API based on the Open Data (OData) v4 protocol.

The administration service currently has two layers or routes:

      Administration service > WMI > SQL:
      https://<SMSProviderFQDN>/AdminService/wmi/<ClassName>

      The WMI route supports both GET and POST commands to over 700 classes.

      Administration service > OData/SQL:
      https://<SMSProviderFQDN>/AdminService/v1.0/<ClassName>

      This versioned route (v1.0) supports new Configuration Manager functionality.

The <ClassName> value is a valid Configuration Manager class name. The administration
service class names are case-sensitive. Make sure to use the proper capitalization. For
example, SMS_Site .

Scenarios
Configuration Manager natively uses the administration service for the following
features:

      Email approval of apps

      View recently connected consoles

      The Security node of the console

      Microsoft Intune tenant attach

      Community hub

      Managing console extensions

<!-- p.3 -->

In addition, you can develop custom solutions with the administration service, for
example:

     Replace a custom web service to access information from the site.

     In PowerShell scripts that you run directly from the Configuration Manager
     console. For more information, see Create and run PowerShell scripts from the
     Configuration Manager console.

     A PowerShell script in a task sequence. This action lets you access information from
     the site without requiring a custom web service to interface with the WMI provider.
     For more information, see Task sequence steps - Run PowerShell Script.

     Access site data from Power BI using the OData connector option.

Prerequisites
Configure the following prerequisites on the server that hosts the SMS Provider role:

     In version 2006 and earlier, enable the Windows server role Web Server (IIS).
     Starting in version 2010, this role is no longer required.

     Starting in version 2107, the SMS Provider requires .NET version 4.6.2, and version
     4.8 is recommended. In version 2103 and earlier, this role requires .NET 4.5 or later.
     For more information, Site and site system prerequisites.

     You may need to enable secure HTTPS communication with a trusted certificate.
     For more information, see Enable secure HTTPS communication.

To access the administration service, your user account needs to be an administrative
user in Configuration Manager. If you access the administration service via a cloud
management gateway, you need to have an account in Microsoft Entra ID.

For more information on scalability of the SMS Provider and administration service, see
Size and scale numbers.

  ７ Note

  For any machine with the Configuration Manager console, if it's using a proxy
  server, the console fails to connect to the administration service. For example, when
  trying to access the Security nodes, you may see errors that the administration
  service isn't enabled or available. The SmsAdminUI.log file shows errors such as,
  Failed to get a response for OData query.

<!-- p.4 -->

  To work around this issue, either remove the proxy configuration from the machine,
  or make the following configuration change:

     1. Manually edit the following XML file: C:\Program Files (x86)\Microsoft
        Endpoint

        Manager\AdminConsole\bin\Microsoft.ConfigurationManagement.exe.config

     2. Configure the <defaultproxy> behavior with one of the following options:
         a. Set enabled="false"
        b. Add the FQDN of the SMS Provider to the <bypasslist> .

        For more information, see <defaultProxy> Element (Network Settings).

Next steps
  How to set up the administration service

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.5 -->

How to set up the administration
service in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the steps in this article to set up the administration service on your SMS Provider.
Before you start, read the administration service Prerequisites.

Enable secure HTTPS communication
Configure the administration service to use a secure HTTPS connection to protect the
data in transit across the network.

Starting in version 2010, you no longer need to enable IIS on the SMS Provider for the
administration service. The site creates a self-signed certificate for the SMS Provider, and
automatically binds it without requiring IIS. If you previously had IIS installed on the
SMS Provider, you can remove it. Then restart the SMS_REST_PROVIDER component.
Remember that you need to open HTTPS port 443 on your firewall.

The administration service automatically uses the site's self-signed certificate. This
behavior helps reduce the friction for easier use of the administration service. The site
always generates this certificate. The administration service ignores the Enhanced HTTP
site setting, as it always uses the site's certificate even if no other site system is using
Enhanced HTTP. You can still manually bind a PKI-based server authentication certificate.
If you've already bound a PKI certificate to port 443 on the SMS Provider server, the
administration service uses that existing certificate.

Use a server authentication certificate

  ７ Note

  By default, the administration service automatically uses the site's self-signed
  certificate. You can still manually bind a PKI-based server authentication certificate.
  Before you can bind your PKI-based certificate, manually unbind the site's self-
  signed certificate from port 443 on the SMS Provider.

There are two primary methods of using a server authentication certificate:

<!-- p.6 -->

     From your organization's public key infrastructure (PKI)

        If your environment already has a PKI, you can use it to issue a server
        authentication certificate for the SMS Provider. This certificate is similar to the
        certificate you would use for a management point or distribution point. For
        more information, see PKI certificate requirements.

        Most enterprise PKI implementations add the trusted root CAs to Windows
        clients. For example, using Active Directory Certificate Services with group
        policy. If you issue the certificate from a CA that your clients don't automatically
        trust, add the CA trusted root certificate to clients. You can scope this trust to
        only the clients that need to access the administration service.

     Use a certificate from a public and globally trusted certificate provider. Windows
     clients include trusted root certificate authorities (CAs) from these providers. By
     using a server authentication certificate issued by one of these providers, your
     clients automatically trust it.

Once you have a server authentication certificate for the SMS Provider, you need to
manually bind it to port 443 in IIS on the server that hosts the SMS Provider role.

First, add the certificate to the server. Import the certificate into the local machine's
Personal store. Then use one of the following options to bind the certificate:

Bind the certificate with IIS
If the server with the SMS Provider role has the IIS Management Console, use the Edit
Bindings action on the default web site. Add port 443, and specify your certificate from
the machine's certificate store.

  ７ Note

  The SMS Provider role doesn't require IIS. This procedure is using the IIS console to
  bind the certificate. These certificate bindings are for the machine, not any specific
  service.

Bind the certificate with netsh

Use the netsh command line to bind the certificate:

netsh http add sslcert ipport=0.0.0.0:443 certhash=<thumbprint> appid={<GUID>}

<!-- p.7 -->

Where <thumbprint> is the thumbprint of the installed certificate, and <GUID> is a
random GUID.

   Tip

  Use the Windows PowerShell cmdlet New-Guid to generate a random GUID.

For example:

netsh http add sslcert ipport=0.0.0.0:443
certhash=5aef9c1f348d4d1c8675309ca3363c2a5d3b617d appid={e9f0631d-6d1c-41b4-9617-

454705f9c011}

Enable internet access
You can use the administration service on-premises only, or you can enable it for access
through the cloud management gateway (CMG). Some scenarios require access to the
administration service from the internet, such as tenant attach or app approvals via
email.

Before you can configure the SMS Provider to allow CMG traffic, first set up a CMG. For
more information, see Overview of CMG.

Then use the following process to enable the administration service through the CMG:

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Servers and Site System Roles node.

   2. Select the server with the SMS Provider role.

          Tip

         On the ribbon, in the Home tab, select Servers with Role and then select SMS
         Provider. This action shows you the site systems with that role.

   3. In the details pane, select the SMS Provider role, and select Properties in the
     ribbon on the Site Role tab.

   4. Select the option to Allow Configuration Manager cloud management gateway
     traffic for administration service.

<!-- p.8 -->

To access the administration service from the internet, replace the SMS Provider FQDN
with the CMG endpoint. For example:

https://CONTOSO.CLOUDAPP.NET/CCM_Proxy_MutualAuth/72186325152220500/AdminService

   Tip

  To get the value for this endpoint, use the following steps:

       Create a CMG. For more information, see Set up a CMG.

       On an active client, open a Windows PowerShell command prompt as an
       administrator.

       Run the following command:

          PowerShell

          (Get-WmiObject -Namespace Root\Ccm\LocationServices -Class
          SMS_ActiveMPCandidate | Where-Object {$_.Type -eq "Internet"}).MP

Enable console usage

  ７ Note

  Starting in version 2111, the option to Enable the Configuration Manager console
  to use the administration service is removed. The administration service is always
  on, so the console will use it when needed.

Enable some nodes of the Configuration Manager console to use the administration
service. This change allows the console to communicate with the SMS Provider over
HTTPS instead of via WMI.

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node. In the ribbon, select
     Hierarchy Settings.

   2. On the General page, select the option to Enable the Configuration Manager
     console to use the administration service.

<!-- p.9 -->

This change only affects the following nodes under the Security node in the
Administration workspace:

        Administrative Users
        Security Roles
        Security Scopes
        Console Connections

When you select one of these nodes, if the following error message displays:

Configuration Manager can't connect to the administration service

Review the information below the error. Then verify that the administration service is
enabled, configured, and functional. For more information including log files to review,
see the Verify section.

Verify
When the site installs the administration service, it logs activity to the
RESTPROVIDERSetup.log file in the Configuration Manager installation directory. By
default this path is C:\Program Files\Microsoft Configuration Manager\logs .

The site tracks the health state of the administration service in the
SMS_REST_PROVIDER.log file. You can see the service start and information about the
certificate.

Test the administration service by doing a simple query in a web browser, for example:

https://smsprovider.contoso.com/adminservice/v1.0/$metadata

The administration service logs its activity to the adminservice.log file on the SMS
Provider server in the Configuration Manager installation directory.

For the above metadata query, the log file shows the following lines:

  log

  Processing incoming request for resource
  [https://smsprovider.contoso.com/adminservice/v1.0/%24metadata], method:
  [GET], User - [CONTOSO\jqadmin]
  ...
  Completing request with response code [200] reason [OK]

Next steps

<!-- p.10 -->

  How to use the administration service

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.11 -->

How to use the administration service in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager uses the administration service REST API in several native
scenarios. You can also use the administration service for your own custom scenarios.

  ７ Note

  The examples in this article all use the FQDN of the server that hosts the SMS
  Provider role. If you access the administration service remotely through a CMG, use
  the CMG endpoint instead of the SMS Provider FQDN. For more information, see
  Enable internet access.

Direct query
There are several ways that you can directly query the administration service:

      Web browser
      PowerShell
      A third-party tool to send HTTPS GET or PUT requests to the web service

The next sections cover the first two methods.

  ） Important

  The administration service class names are case-sensitive. Make sure to use the
  proper capitalization. For example, SMS_Site .

Web browser
You can use a web browser to easily query the administration service. When you specify
a query URI as the browser's URL, the administration service processes the GET request,
and returns the result in JSON format. Some web browsers may not display the result in
an easy to read format.

<!-- p.12 -->

PowerShell
Make direct calls to this service with the Windows PowerShell cmdlet Invoke-
RestMethod.

For example:

  PowerShell

  Invoke-RestMethod -Method 'Get' -Uri
  "https://SMSProviderFQDN/AdminService/wmi/SMS_Site" -UseDefaultCredentials

This command returns the following output:

  Output

  @odata.context                                                      value
  --------------                                                      -----
  https://SMSProviderFQDN/AdminService/wmi/$metadata#SMS_Site
  {@{@odata.etag=FC1; __LAZYPROPERTIES=System.Objec...

The following example drills down to more specific values:

  PowerShell

  ((Invoke-RestMethod -Method 'Get' -Uri
  "https://SMSProviderFQDN/AdminService/wmi/SMS_Site" -
  UseDefaultCredentials).value).Version

The output of this command is the specific version of the site: 5.00.8968.1000

Call PowerShell from a task sequence

You can use the Invoke-RestMethod cmdlet in a PowerShell script from the Run
PowerShell Script task sequence step. This action lets you query the administration
service during a task sequence.

For more information, see Task sequence steps - Run PowerShell Script.

Power BI Desktop
You can use Power BI Desktop to query data in Configuration Manager via the
administration service. For more information, see What is Power BI Desktop?

<!-- p.13 -->

  1. In Power BI Desktop, in the ribbon, select Get Data, and select OData feed.

  2. For the URL, specify the administration service route. For example,
     https://smsprovider.contoso.com/AdminService/wmi/

  3. Choose Windows Authentication.

  4. In the Navigator window, select the items to use in your Power BI dashboard or
     report.

                                                                                   

Example queries

Get more details about a specific device
https://<ProviderFQDN>/AdminService/wmi/SMS_R_System(<ResourceID>)

For example:
https://smsprovider.contoso.com/AdminService/wmi/SMS_R_System(16777219)

v1 Device class examples

<!-- p.14 -->

         Get all devices: https://<ProviderFQDN>/AdminService/v1.0/Device

         Get single device:
         https://<ProviderFQDN>/AdminService/v1.0/Device(<ResourceID>)

         Run CMPivot on a device:

           rest

           Verb: POST
           URI:
           https://<ProviderFQDN>/AdminService/v1.0/Device(<ResourceID>)/AdminServ
           ice.RunCMPivot
           Body: {"InputQuery":"<CMPivot query to run>"}

         See CMPivot job result:

           rest

           Verb: GET
           URI:
           https://<ProviderFQDN>/AdminService/v1.0/Device(<ResourceID>)/AdminServ
           ice.CMPivotResult(OperationId=<Operation ID of the CM Pivot job>)

         See which collections a device belongs to:
         https://<ProviderFQDN>/AdminService/v1.0/Device(16777219)/ResourceCollectionMe

         mbership?$expand=Collection&$select=Collection

Filter results with startswith
This example URI only shows collections whose names start with All .

https://<ProviderFQDN>/AdminService/wmi/SMS_Collection?
$filter=startswith(Name,'All') eq true

Run a static WMI method
This example invokes the GetAdminExtendedData method on the SMS_AdminClass
that takes parameter named Type with value 1 .

  rest

  Verb: Post
  URI: https://<ProviderFQDN>/AdminService/wmi/SMS_Admin.GetAdminExtendedData

<!-- p.15 -->

  Body: {"Type":1}

Next steps
Custom properties for devices

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.16 -->

How to view authorization failure
message in administration service.
Article • 04/11/2023

Applies to version 2303 or later.

You can view audit messages about authorization failure in admin service along with
request details and status messages.

These messages are shown in 'All Status Message' at 'Status Message Queries' in
'Monitoring' ribbon. Previously these failures were logged in log files.

With the audit messages we intend to avoid inconvenience of log files rollback. Details
about the user, resource access attempts and the number of attempts for all the
authorized requests made by user in a day are available. You can also audit read
operations for HTTPS requests and for cloud-initiated operations. This is to help admins
to scope permission and roles of users while also determining if there are any malicious
users.

  ７ Note

  All unauthorized requests are aggregated for 24 hours before being sent to the
  status message viewer. The status message viewer includes a count of the total
  number of unauthorized requests received by administration service a day before.

Steps to view the audit messages:
   1. Navigate to Monitoring on the console.

   2. Select Status Message Queries in the System Status Folder.

   3. From the list of all queries, right click on the "All Status Messages" query.

   4. From the pop up, click on Show Messages.

<!-- p.17 -->

5. Select the duration of status messages from the “All Status Messages” pop-up
  window.

6. After clicking the OK button all the messages will be shown in Status Messages
  viewer

7. You can then filter messages related to only Unauthorized Users.

8. Click on funnel icon on top bar to show "Filter Status Message" popup.

9. In Filter Status Messages popup fill Message ID as 11618

<!-- p.18 -->

 10. All the messages related to unauthorized users request will be filtered out with
     message description. Details about the user and their action will be shown.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.19 -->

Custom properties for devices
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Many customers have other data that's external to Configuration Manager but useful for
deployment targeting, collection building, and reporting. This data is typically non-
technical in nature, not discoverable on the client, and comes from a single external
source. For example, a central IT Infrastructure Library (ITIL) system or asset database,
which has some of the following device attributes:

      Physical location
      Organizational priority
      Category
      Cost center
      Department

Starting in version 2107, you can use the administration service to set this data on
devices. The site stores the property's name and its value in the site database as the
Device Custom Properties class. You can then use the custom properties in
Configuration Manager for reporting or to create collections.

Starting in version 2111, you can create and edit these custom properties in the
Configuration Manager console. This new user interface makes it easier to view and edit
these properties.

  ７ Note

  You can use unicode characters for custom property values, but not the property
  names. For more information, see Unicode and ASCII support in Configuration
  Manager.

Prerequisites
The account that makes the API calls requires the following permissions on a collection
that contains the target device:

      To set properties: Modify Resource
      To view properties: Read Resource
      To remove properties: Delete Resource

<!-- p.20 -->

Set properties via UI
Applies to version 2111 or later

   1. In the Configuration Manager console, go to the Assets and Compliance
      workspace, and select the Devices node.

   2. Select a device, and then in the ribbon select Properties

   3. Switch to the Custom Properties tab.

   4. Select the gold star icon    to create a new custom property. Provide a name for
      the property and set a value for this device. Select OK to save the properties.

Set properties via API
Applies to version 2107 or later

To set properties on a device, use the SetExtensionData API. Make a POST call to the
URI

<!-- p.21 -->

https://<SMSProviderFQDN>/AdminService/v1.0/Device(<DeviceResourceID>)/AdminService
.SetExtensionData with a JSON body. The resource ID is an integer value, for example

16777345 .

This JSON example sets two name-value pairs for the device's asset tag and location:

     JSON

     {
         "ExtensionData": {
           "AssetTag":"0580255",
           "Location":"Dublin"
         }
     }

View properties
Use the GetExtensionData API to view your custom properties.

To view properties on a single device, make a GET call to the URI
https://<SMSProviderFQDN>/AdminService/v1.0/Device(<DeviceResourceID>)/AdminService
.GetExtensionData .

To view properties on all devices, make a GET call to the URI
https://<SMSProviderFQDN>/AdminService/v1.0/Device/AdminService.GetExtensionData .

This call returns property values from devices to which you have read permission.

Remove properties
To remove properties values from all devices, use the DeleteExtensionData API without
a device ID. Include a device resource ID to only remove properties from a specific
device. Make a POST call to the URI
https://<SMSProviderFQDN>/AdminService/v1.0/Device/AdminService.DeleteExtensionDat
a.

Create a collection
Use the following steps to create a collection with a query rule based on the custom
properties:

     1. In the Configuration Manager console, Create a collection.

<!-- p.22 -->

2. On the Membership Rules page, in the Add Rule list, select Query rule.

3. In the Query Rule Properties window, specify a Name for the query. Then select
  Edit Query Statement.

4. In the Query Statement Properties window, switch to the Criteria tab. Then select
  the golden asterisk ( * ) to add new criteria.

5. In the Criterion Properties window, Select the following values:

       Attribute class: Device Custom Properties
       Attribute: PropertyName

6. Select an Operator and then specify the name of the property as the Value.

  At this point, the Criterion Properties window should look similar to the following
  image:

  Select OK to save the criterion.

7. Repeat the steps to add a criterion for the PropertyValue attribute.

  At this point, the collection Query Statement Properties window should look similar
  to the following image:

<!-- p.23 -->

  8. Select OK to close all property windows. Then complete the wizard to create the
     collection.

Example WQL statement
You can also use the following sample query. In the query statement properties window,
select Show Query Language to paste the query statement.

  SQL

  select
  SMS_R_SYSTEM.ResourceID,SMS_R_SYSTEM.ResourceType,SMS_R_SYSTEM.Name,SMS_R_SY
  STEM.SMSUniqueIdentifier,SMS_R_SYSTEM.ResourceDomainORWorkgroup,SMS_R_SYSTEM
  .Client
  from SMS_R_System inner join SMS_G_System_ExtensionData on
  SMS_G_System_ExtensionData.ResourceId = SMS_R_System.ResourceId
  where SMS_G_System_ExtensionData.PropertyName = "AssetTag" and
  SMS_G_System_ExtensionData.PropertyValue = "0580255"

  ７ Note

<!-- p.24 -->

  To use custom properties WQL statements with incremental collection updates, use
  Configuration Manager version 2107 with the update rollup or later.

Next steps
How to use the administration service

Create a collection

How to manage clients

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.25 -->

Administration service frequently asked
questions (FAQ)
Applies to: Configuration Manager (current branch, technical preview branch, long-term servicing
branch)

Technical
Should I rewrite my existing automation to use the
administration service?
It depends. There are some benefits to using the administration service over other APIs like
WMI or PowerShell. For example, some PowerShell cmdlets loop on a single interaction, so
there's multiple calls to set up, query, and tear down. With the administration service, the same
query may be faster as it makes a single call for the group.

Existing WMI and PowerShell cmdlets are still supported and will continue to work.
Configuration Manager may only expose some new features through the administration
service, and not have comparable WMI or PowerShell APIs.

What if an existing WMI class or method doesn't
work over the administration service?
If you find an existing WMI class or method that doesn't GET or PUT as expected, send a frown
to inform the engineering team. For more information, see Product feedback.

Are Swagger definitions available?
No, the administration service currently doesn't publish an OpenAPI (Swagger) document         .

Remote access
Can I use the administration service with internet-
based client management?
No, internet-based client management (IBCM) doesn't support exposing the SMS Provider role
to the internet. For internet access to the administration service, you need a cloud
management gateway. For more information, see Enable internet access.

<!-- p.26 -->

Isn't it too risky to open this API to the internet?
It depends upon your organization's risk level, and what controls you use or put in place to
help mitigate the risks:

     The administration service still uses Configuration Manager built-in role-based
     authorization.

     Control access to the web service with the certificate trust. If a device doesn't trust the
     certificate chain, a user on that device can't query the administration service.

     Add additional security layers. For example, Azure App Proxy.

Can I use it with Conditional Access?
Yes, and that configuration is easiest if you use Azure App Proxy.

Miscellaneous
How do I learn about what's new with the
administration service in each Configuration
Manager release?
For more information, see Release notes.

<!-- p.27 -->

Administration service release notes
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Changes in version 2006
The WMI route is now case-insensitive. For example, in version 2002, you had to specify
AdminService/wmi/SMS_Site . Now in version 2006, you can also use

AdminService/wmi/sms_site

Changes in version 2002
Starting in version 2002, the administration service automatically uses the site's self-
signed certificate. This change helps reduce the friction for easier use of the
administration service. The site always generates this certificate. Now the administration
service ignores the Enhanced HTTP site setting, as it always uses the site's certificate
even if no other site system is using Enhanced HTTP. For more information, see Enable
secure HTTPS communication.

New properties for the v1.0 Device class:

      Events on a device: Device(<ResourceID>)/Events
      Application on a device: Device(<ResourceID>)/AvailableApplications?
      $expand=Application

      Boundary groups on a device: Device(<ResourceID>)/BoundaryGroups?
      $expand=BoundaryGroup

Changes in version 1910
      The WMI route now supports static WMI methods. For example:

        rest

        Verb: Post
        URI:
        https://<ProviderFQDN>/AdminService/wmi/SMS_Admin.GetAdminExtendedData
        Body: {"Type":1}

<!-- p.28 -->

   The Configuration Manager console now sends console connection health
   information through the administration service.

   Use OData query options startswith and endswith on WMI route. For example:
    https://<ProviderFQDN>/AdminService/wmi/SMS_Collection?

   $filter=startswith(Name,'All') eq true

   Use the Power BI Desktop feature to get data from an OData feed. You can then
   see all WMI entities and their objects in Power BI Desktop to create custom
   reports.

   The v1.0 route exposes the Device class. For example:
    https://<ProviderFQDN>/AdminService/v1.0/Device

  Tip

 For more examples, see How to use the administration service.

Classes available to the WMI route in version 1910
   SMS_ReplicationGroup
   SMS_BoundaryGroup
   SMS_G_System_DISK
   SMS_G_System_LOGICAL_DISK
   SMS_G_System_OPERATING_SYSTEM
   SMS_G_System_PARTITION
   SMS_G_System_PHYSICAL_DISK
   SMS_G_System_PHYSICAL_MEMORY
   SMS_G_System_X86_PC_MEMORY
   SMS_DistributionDPStatus
   SMS_WinPEOptionalComponentInfo
   SMS_OSDeploymentKitWinPEOptionalComponent
   SMS_WinPEOptionalComponentInBootImage
   SMS_G_System_AdvancedThreatProtectionHealthStatus
   SMS_SearchFolder
   SMS_DPStatusDetails

Feedback

<!-- p.29 -->

Was this page helpful?      Yes    No

Provide product feedback
