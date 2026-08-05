---
title: "Configuration Manager SDK documentation — pages 521-560"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0521-0560
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0521-0560
family: sccm
documentKind: "doc"
abstract: "SMS_CollectionRuleQuery SMS_Collection SMS_UserInstancePermissions SMS_UserClassPermissions SMS_UserInstancePermissionNames SMS_UserClassPermissionNames See also SMS Provider fundamentals Feedback Was this page helpful?  Yes  No Provide product feedback How to Connect to an SM"
---

# Configuration Manager SDK documentation — pages 521-560

<!-- p.521 -->

      SMS_CollectionRuleQuery

      SMS_Collection

      SMS_UserInstancePermissions

      SMS_UserClassPermissions

      SMS_UserInstancePermissionNames

      SMS_UserClassPermissionNames

See also
SMS Provider fundamentals

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.522 -->

How to Connect to an SMS Provider in
Configuration Manager by Using
Managed Code
Article • 01/05/2024

To connect to an SMS Provider, use WqlConnectionManager.Connect. After it's
connected, WqlConnectionManager.Connect has methods to query, create, delete, and
otherwise use Configuration Manager Windows Management Instrumentation (WMI)
objects.

  ７ Note

  WqlConnectionManager.Connect is a WMI-specific derivation of
  ConnectionManagerBase.

If you're connecting to a local SMS Provider, you don't supply user credentials. If you're
connecting to a remote SMS Provider, you don't need to supply user credentials if the
current user/computer context has permissions on the remote SMS Provider.

If you don't have access privileges on the remote SMS Provider, or if you want to use a
different user account, then you must supply user credentials for a user account that has
access privileges.

WQLConnectionManager.Connection requires a SmsNamedValuesDictionary object.
This can be used to store cached information such as the computer name.

It's pre-populated with many values that can be used in your application.

                                                                          ﾉ    Expand table

 Value                   Description.

 ProviderLocation        The provider location. For example,

                         \\
                         <ComputerName>\ROOT\sms:SMS_ProviderLocation.SiteCode="XXX".

 ProviderMachineName     The provider computer. For example, \\ComputerName.

 Connection              The connection path. For example,
                         \\ComputerName\root\sms\site_XXX.

<!-- p.523 -->

 Value                    Description.

 ConnectedSiteCode        The site code for the Configuration Manager site that the connection is
                          connected to. For example, XXX.

 ServerName               The computer name, for example, COMPUTERNAME.

 SiteName                 The Configuration Manager site code. For example, Central Site.

 ConnectedServerVersion   The version for the connected server. For example, 4.00.5830.0000

 BuildNumber              The Configuration Manager installation build number. For example,
                          5830.

  ７ Note

  The SmsNamedValuesDictionary object is not the context qualifier information
  passed to the provider. For more information, see How to Add a Configuration
  Manager Context Qualifier by Using Managed Code.

To connect to the SMS Provider
   1. Create a SmsNamedValuesDictionaryObject.

   2. Create an instance of the WqlConnectionManager class and call the [Connect]
     method passing the server name, and if the server name is remote, the user name
     and password.

   3. Use the WqlConnectionManager object to connect to the provider.

Example
The following example method connects to the SMS Provider on a local or remote
computer. If servername is remote, the method uses the supplied user name and
password to connect to the remote computer. If you want to use the current user
context, for the remote connection, change the code so that it doesn't pass the user
name and password. If the connection is successful, a WqlConnectionManager object is
returned.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

<!-- p.524 -->

  public WqlConnectionManager Connect(string serverName, string userName,
  string userPassword)
  {
      try
      {
          SmsNamedValuesDictionary namedValues = new
  SmsNamedValuesDictionary();
          WqlConnectionManager connection = new
  WqlConnectionManager(namedValues);

           if (System.Net.Dns.GetHostName().ToUpper() == serverName.ToUpper())
           {
                // Connect to local computer.
                connection.Connect(serverName);
           }
           else
           {
                // Connect to remote computer.
                connection.Connect(serverName, userName, userPassword);
           }

           return connection;
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to Connect. Error: " + e.Message);
          return null;
      }
      catch (UnauthorizedAccessException e)
      {
          Console.WriteLine("Failed to authenticate. Error:" + e.Message);
          return null;
      }
  }

Compiling the Code

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

<!-- p.525 -->

Microsoft.ManagementConsole

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Microsoft.ManagementConsole

Robust Programming
The Configuration Manager exceptions that can be raised are SmsConnectionException
and SmsQueryException. These can be caught together with SmsException.

.NET Framework Security
UnauthorizedAccessException is raised when the wrong credentials are passed to
WqlConnectionManager.Connect.

See Also
SMS Provider fundamentals How to Add a Configuration Manager Context Qualifier
Using Managed Code
Objects overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.526 -->

How to Add a Configuration Manager
Context Qualifier by Using Managed
Code
Article • 10/10/2022

In Configuration Manager, to add a context qualifier by using the managed SMS
Provider, use the Context property which is a Dictionary object that holds context
qualifiers.

Typically you will add your application name to the ApplicationName context qualifier,
along with the computer name (MachineName) and Locale identifier (LocaleID).

To add Configuration Manager context qualifier
   1. Set up a connection to the SMS Provider. For more information, see How to
      Connect to an SMS Provider in Configuration Manager by Using Managed Code

   2. Get the SmsNamedValuesDictionary object from the WqlConnectionManager
      object that you get from step 1.

   3. Add the context qualifiers as required.

Example
The following C# example first adds a number of context qualifiers to a
WQLConnectionManager object Context dictionary property. It then displays a list of the
context qualifiers in dictionary object.

  ７ Note

  WqlConnectionManager derives from ConnectionManagerBase.

In the example, the LocaleID context qualifier is hard-coded to English (U.S.). If you
need the locale for non-U.S. installations, you can get it from the SMS_Identification
Server WMI Class LocaleID property.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

<!-- p.527 -->

  public void AddContextQualifiers(WqlConnectionManager connection)
  {
      try
      {
          connection.Context.Add("ApplicationName", "My application name");
          connection.Context.Add("MachineName","Computername");
          connection.Context.Add("LocaleID", @"MS\1033");

          foreach (KeyValuePair<string, object> namedValue in
  connection.Context)
          {
              Console.WriteLine(namedValue.Key);
              Console.WriteLine(namedValue.Value);
              Console.WriteLine();
          }
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to add context qualifier : " + e.Message);
      }
  }

The example method has the following parameters:

                                                                       ﾉ   Expand table

 Parameter     Type                       Description

 connection    - WqlConnectionManager     A valid connection to the SMS Provider.

Compiling the Code

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

<!-- p.528 -->

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
The Configuration Manager exceptions that can be raised are SmsConnectionException
and SmsQueryException. These can be caught together with SmsException.

See Also
Configuration Manager Context Qualifiers
How to Connect to a Configuration Manager Provider using Managed Code

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.529 -->

How to Connect to an SMS Provider in
Configuration Manager by Using WMI
Article • 01/05/2024

Before connecting to the SMS Provider for a local or remote Configuration Manager site
server, you first need to locate the SMS Provider for the site server. The SMS Provider
can be either local or remote to the Configuration Manager site server you're using. The
Windows Management Instrumentation (WMI) class SMS_ProviderLocation is present on
all Configuration Manager site servers, and one instance will contain the location for the
Configuration Manager site server you're using.

You can connect to the SMS Provider on a Configuration Manager site server by using
the WMI SWbemLocator object or by using the Windows Script Host GetObject method.
Both approaches work equally well on local or remote connections, with the following
limitations:

      You must use SWbemLocator if you need to pass user credentials to a remote
      computer.

      You can't use SWbemLocator to explicitly pass user credentials to a local computer.

      There are several different syntaxes that you can use to make the connection,
      depending on whether the connection is local or remote. After you're connected to
      the SMS Provider, you'll have an SWbemServices object that you use to access
      Configuration Manager objects.

  ７ Note

  If you need to add context qualifiers for the connection, see How to Add a
  Configuration Manager Context Qualifier by Using WMI.

To connect to an SMS provider
   1. Get a WbemScripting.SWbemLocator object.

   2. Set the authentication level to packet privacy.

   3. Set up a connection to the SMS Provider by using the SWbemLocator object
      ConnectServer method. Supply credentials only if it's a remote computer.

<!-- p.530 -->

   4. Using the SMS_ProviderLocation object ProviderForLocalSite property, connect to
        the SMS Provider for the local computer and receive a SWbemServices object.

   5. Use the SWbemServices object to access provider objects. For more information,
        see Objects overview.

Examples
The following example connects to the server. It then attempts to connect to the SMS
Provider for that server. Typically this will be the same computer. If it isn't,
SMS_ProviderLocation provides the correct computer name.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Function Connect(server, userName, userPassword)

         On Error Resume Next

         Dim net
         Dim localConnection
         Dim swbemLocator
         Dim swbemServices
         Dim providerLoc
         Dim location

         Set swbemLocator = CreateObject("WbemScripting.SWbemLocator")

         swbemLocator.Security_.AuthenticationLevel = 6 'Packet Privacy.

         ' If the server is local, do not supply credentials.
         Set net = CreateObject("WScript.NetWork")
         If UCase(net.ComputerName) = UCase(server) Then
             localConnection = true
             userName = ""
             userPassword = ""
             server = "."
         End If

         ' Connect to the server.
         Set swbemServices= swbemLocator.ConnectServer _
                 (server, "root\sms",userName,userPassword)
         If Err.Number<>0 Then
             Wscript.Echo "Couldn't connect: " + Err.Description
             Connect = null
             Exit Function
         End If

<!-- p.531 -->

       ' Determine where the provider is and connect.
       Set providerLoc = swbemServices.InstancesOf("SMS_ProviderLocation")

          For Each location In providerLoc
               If location.ProviderForLocalSite = True Then
                   Set swbemServices = swbemLocator.ConnectServer _
                    (location.Machine, "root\sms\site_" + _
                       location.SiteCode,userName,userPassword)
                   If Err.Number<>0 Then
                       Wscript.Echo "Couldn't connect:" + Err.Description
                       Connect = Null
                       Exit Function
                   End If
                   Set Connect = swbemServices
                   Exit Function
               End If
          Next
      Set Connect = null ' Failed to connect.
  End Function

The following sample connects to the remote server using PowerShell, and attempts an
SMS connection.

  powerShell

  $siteCode = ''
  $siteServer = 'server.domain'

  $credentials = Get-Credential
  $username = $credentials.UserName

  # The connector does not understand a PSCredential. The following command
  will pull your PSCredential password into a string.
  $password =
  [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.In
  teropServices.Marshal]::SecureStringToBSTR($credentials.Password))

  $NameSpace = "root\sms\site_$siteCode"
  $SWbemLocator = New-Object -ComObject "WbemScripting.SWbemLocator"
  $SWbemLocator.Security_.AuthenticationLevel = 6
  $connection =
  $SWbemLocator.ConnectServer($siteServer,$Namespace,$username,$password)

Compiling the Code
This C# example requires:

Comments

<!-- p.532 -->

The sample method has the following parameters:

                                                                        ﾉ   Expand table

 Parameter                   Type                        Description

 connection                  - Managed:
                              WqlConnectionManager
                             - VBScript: SWbemServices

 A valid connection to the
 SMS Provider.

 taskSequence                - Managed: IResultObject    A valid task sequence
                             - VBScript: SWbemObject     (SMS_TaskSequence).

 taskSequenceXML             - Managed: String           A valid task sequence XML.
                             - VBScript: String

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
Using script to pass the user name and password is a security risk and should be
avoided where possible.

The preceding example sets the authentication to packet privacy. This is the same
managed SMS Provider.

For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
SMS Provider fundamentals
How to Add a Configuration Manager Context Qualifier by Using WMI
Windows Management Instrumentation

Feedback

<!-- p.533 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.534 -->

How to Add a Configuration Manager
Context Qualifier by Using WMI
Article • 10/10/2022

In Configuration Manager, you add context qualifiers to a connection (SWbemServices)
or object (SWbemObject) by creating a SWbemNamedValueSet value set to hold the
context qualifiers. You then provide the SWbemNamedValueSet value set as a parameter
to connection and object methods.

in Configuration Manager, you can provide your application name (ApplicationName),
computer name (MachineName) and locale identifier (LocaleID).

In most cases, context qualifiers are not required. The main exception is accessing the
site control file where they are needed to set up session information. For more
information, see About the Configuration Manager Site Control File.

To add a Configuration Manager context qualifier
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Create a WbemScripting.SWbemNamedValueSet object and add the desired
      context qualifiers.

   3. Use the SWbemNamedValue value set you created in step two to pass context
      qualifiers to connection and object manipulation calls.

Example
The following VBScript example creates a SWbemNamedValueSet value set and adds
the supplied context qualifiers. The following code example demonstrates how to call
the method for use in an SMS_Package package object Put method call. For more
information about Configuration Manager objects, see Objects overview.

Dim context

Set context = CreateContextQualifiers("My application" , "My Computer" ,
"MS\1033")

package.Put_ , context

<!-- p.535 -->

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Function CreateContextQualifiers(applicationName, machineName, localeID)
      On Error Resume next
      Dim smsContext

        set smsContext = CreateObject("WbemScripting.SWbemNamedValueSet")

        ' Add the context qualifiers to the set.
        smsContext.Add "LocaleID", localeID
        smsContext.Add "MachineName", machineName
        smsContext.Add "ApplicationName", applicationName

        Set CreateContextQualifiers = smsContext

        If Err.Number<>0 Then
          WScript.Echo Err.Description
          CreateContextQualifiers = null
          Exit Function
      End If
  End Function

The example method has the following parameters:

                                                                                 ﾉ   Expand table

 Parameter         Type     Description

 applicationName   -        The ApplicationName context qualifier.
                   String

 machineName       -        The computer name qualifier.
                   String

 localeID          -        The locale identifier. For example, MS\1033 is English (U.S.). If you
                   String   need the locale for non-U.S. installations, you can get it from the
                            SMS_Identification Server WMI Class LocaleID property.

Compiling the Code
This VBScript example requires:

Robust Programming

<!-- p.536 -->

For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About the Configuration Manager Site Control File
Objects overview Configuration Manager Context Qualifiers
How to Connect to an SMS Provider in Configuration Manager by Using WMI
Windows Management Instrumentation

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.537 -->

How to Create an Application with the
Script Deployment Type
Article • 10/04/2022

Applications are new to Configuration Manager. Prior to Configuration Manager, a
package was the basic object that was used to install software. Now, a more flexible and
complete model exists for applications in Configuration Manager. Software based on
this new model is referred to as an application. Packages still exist in Configuration
Manager, but they are defined and behave in much the same manner as packages did in
Configuration Manager.

The application model defines a standard set of properties and metadata that is used by
the system to manage the lifecycle of the application. As applications are modeled, the
application itself can be a building block used to help define other applications in the
system. For example, .NET Framework can be defined as an application, and then it can
be referenced by a parent application as a dependency that must be present or installed
before the parent application is installed.

To Create an Application with the Script
Deployment Type
In order to get started with creating an application, the following section defines a
simple application and its basic properties. Assuming that all applications you create are
new from the Configuration Manager perspective, then adding a new application into
Configuration Manager is relatively straightforward. When applications may already
exist, and may have relationships to other applications, either through dependencies or
supersedence is more complicated and not covered in the example below.

A simple command-line program that demonstrates how to create the model and
persist to the database through the SMS Provider is shown below. As a sample, it
contains strings that are hard-coded, and should not be considered a real world
application for automating application creation. Additionally, there is minimal error
handling. However, this example should be enough to get you started.

Other references
For more information, see the following blog posts:

      How to Create a Basic App using the Configuration Manager 2012 Beta 2 SDK

<!-- p.538 -->

    Adam Meltzer's Configuration Manager blog

To Create an Application with the Script Deployment Type

  1. Initialize the provider connection and ApplicationFactory. (The application factory
    is a wrapper that makes creating the provider classes a little easier.)

  2. Create the application and the deployment type.

  3. Persist the application to the provider.

    To use this sample, create a new command-line C# application and copy and
    replace the code shown. You'll need to add references to the five assemblies below
    are all found in the adminconsole\bin directory:

    AdminUI.AppManFoundation.dll

    A wrapper encapsulating Configuration Manager provider functionality for creating
    applications.

    AdminUI.WqlQueryEngine.dll

    The WqlConnectionManager.

    Microsoft.ConfigurationManagement.ApplicationManagement.dll

    The core application model, used to serialize/deserialize applications.

    Microsoft.ConfigurationManagement.ApplicationManagement.MsiInstaller.dll

    An implementation of the Windows Installer and Script Deployment Types.

    Microsoft.ConfigurationManagement.ManagementProvider.dll

    The Configuration Manager managed WMI interface.

    After compiling and running the application, the output for the application will
    show this output when it is successful.

 C:\sms\AdminConsole\bin>ApplicationCreator.exe

 Connecting to the SMS Provider on computer [machinename].
 Initializing the ApplicationFactory.Creating application [app].
 Creating Script DeploymentType.
 Initializing the SMS_Application object with the model.
 Saving application, Title: [app], Scope: [ScopeId_D5230FF0-B439-44D9-906E-

<!-- p.539 -->

  00A330F2AE06].
  Successfully saved application.

Example
The following example method creates an application with the script deployment type
and persists into the Configuration Manager database.

  ７ Note

  This code is a sample. It doesn't contain error handling for all cases, nor
  demonstrate relationships such as dependencies and supersedence. It also doesn't
  demonstrate creating requirement rules for a deployment type.

  c#

  namespace ApplicationCreator
  {
      using System;
      using System.IO;
      using Microsoft.ConfigurationManagement.AdminConsole.AppManFoundation;
      using Microsoft.ConfigurationManagement.ApplicationManagement;
      using Microsoft.ConfigurationManagement.ManagementProvider;
      using
  Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine;
      class Program
      {
          static void Main(string[] args)
          {
              Initialize(Environment.MachineName);
              Application application = CreateApplication("app",
  "description",
  System.Globalization.CultureInfo.CurrentCulture.TwoLetterISOLanguageName);

  application.DeploymentTypes.Add(CreateScriptDt(application.Title,
  application.Description, "notepad.exe", "return 0;", null));
              Store(application);
          }

           private static AppManWrapper wrapper;
           private static ApplicationFactory factory;

          // Initializes the default authoring scope and establishes
  connection to the SMS Provider.
          // <param name="siteServerName">A string containing the name of the
  Configuration Manager site.</param>

           public static void Initialize(string siteServerName)

<!-- p.540 -->

       {
            Validator.CheckForNull(siteServerName, "siteServerName");
            Log("Connecting to the SMS Provider on computer [{0}].",
siteServerName);
            // Creates a connection to the SMS Provider.
            WqlConnectionManager connectionManager = new
WqlConnectionManager();
            connectionManager.Connect(siteServerName);
            Log("Initializing the ApplicationFactory.");
            // Initialize application wrapper and factory for creating the
SMS Provider application object.
            factory = new ApplicationFactory();
            wrapper = AppManWrapper.Create(connectionManager, factory) as
AppManWrapper;
        }

        // Inserts the provided application to the provided connected
Configuration Manager site.
        // <param name="application">An application object that will be
inserted into the Configuration Manager site.</param>

        public static void Store(Application application)
        {
            Validator.CheckForNull(application, "application");
            Validator.CheckForNull(wrapper, "wrapper");
            Exception ex = null;
            try
            {
                // Set the application into the provider object.
                wrapper.InnerAppManObject = application;
                Log("Initializing the SMS_Application object with the
model.");
                factory.PrepareResultObject(wrapper);
                Log("Saving application, Title: [{0}], Scope: [{1}].",
application.Title, application.Scope);
                // Save to the database.
                wrapper.InnerResultObject.Put();
            }
            catch (SmsException exception)
            {
                ex = exception;
            }
            catch (Exception exception)
            {
                ex = exception;
            }
            if (ex != null)
            {
                Log("ERROR saving application [{0}].", ex.Message);
                Log(ex);
            }
            else
            {
                Log("Successfully saved application.");
            }

<!-- p.541 -->

       }

        // Creates an Application object.
        // <param name="title">The title of the application that will be
visible in the admin console and in the Software Center and Portal.</param>
        // <param name="description">The description for the application.
</param>
        // <param name="language">The language of the resources supplied.
</param>

        public static Application CreateApplication(string title, string
description, string language)
        {
            Validator.CheckForNull(title, "title");
            Validator.CheckForNull(language, "language");
            Log("Creating application [{0}].", title);
            Application app = new Application { Title = title };
            app.DisplayInfo.DefaultLanguage = language;
             app.DisplayInfo.Add(new AppDisplayInfo { Title = title,
Description = description, Language = language });
            return app;
        }

        // Creates a Deployment Type with a Script Installer.
        // <param name="title">A string containing the title for the
Deployment Type (required).</param>
        // <param name="description"> A string containing the description
for the Deployment Type (optional).</param>
        // <param name="installCommandLine">A string containing the
installation command line for the installer (required).</param>
        // <param name="detectionScript">A string containing the script for
detection, this would most likely be separated out.
        // to a different method to support creating different detection
method types such as Windows Installer, EHD, and script. Additionally, in
the case
        // of script, the more likely scenario would be to load the script
from a file, read the file, and then set the value.</param>
        // <param name="contentFolder">The folder that will contain the set
of files that will represent the content for this Deployment Type.
Validation
        // should verify that this is a UNC path, otherwise the
Configuration Manager system will fail to create the content package
correctly.</param>
        // <returns>A deployment type object.</returns>

        public static DeploymentType CreateScriptDt(string title, string
description, string installCommandLine, string detectionScript, string
contentFolder)
        {
            Validator.CheckForNull(installCommandLine,
"installCommandLine");
            Validator.CheckForNull(title, "title");
            Validator.CheckForNull(detectionScript, "detectionScript");
            Log("Creating Script DeploymentType.");
            ScriptInstaller installer = new ScriptInstaller();

<!-- p.542 -->

              installer.InstallCommandLine = installCommandLine;
              installer.DetectionScript = new Script { Text = detectionScript,
  Language = ScriptLanguage.JavaScript.ToString() };
              // Only add content if specified and exists.
              if (Directory.Exists(contentFolder) == true)
              {
                  Content content =
  ContentImporter.CreateContentFromFolder(contentFolder);
                  if (content != null)
                  {
                      installer.Contents.Add(content);
                  }
              }
              DeploymentType dt = new DeploymentType(installer,
  ScriptInstaller.TechnologyId, NativeHostingTechnology.TechnologyId);
              dt.Title = title;
              return dt;
          }

            public static void Log(Exception exception)
            {
                Log("ERROR: [{0}] ", exception.Message);
                Log("Stack: [{0}]", exception.StackTrace);
                if (exception.InnerException != null)
                {
                    Log(exception.InnerException);
                }
            }

            public static void Log(string message, params object[] args)
            {
                Console.WriteLine(message, args);
            }
      }
  }

Namespaces
System

System.IO

Microsoft.ConfigurationManagement.AdminConsole.AppManFoundation

Microsoft.ConfigurationManagement.ApplicationManagement

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

<!-- p.543 -->

Assembly
AdminUI.AppManFoundation.dll

AdminUI.WqlQueryEngine.dll

Microsoft.ConfigurationManagement.ApplicationManagement.dll

Microsoft.ConfigurationManagement.ApplicationManagement.MsiInstaller.dll

Microsoft.ConfigurationManagementProvider.dll

AdminUI.DcmObjectWrapper.dll

DcmObjectModel.dll

For more information about error handling, see About Configuration Manager Errors.

See Also
SMS_Collection Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.544 -->

Application approval process
Article • 10/04/2022

One of the important scenarios for application management is providing a controlled
installation and uninstallation process for software that requires approval. To reduce the
overall load on the Configuration Manager infrastructure and improve performance, the
workflow doesn't require creating individual collections to manage installations and
uninstallations for each application.

Scenario 1: Applications must be approved
before they're installed
The IT administrator at Contoso uses Software Center to make software available to the
users. These applications must be approved before they're installed. The admin deploys
an application to all users and configures it to require approval.

The user browses the list of applications in Software Center but can't install the
application until the request is approved. The user submits the request from Software
Center and specifies the reason for the request. If the option, Approve application
requests for users per device is enabled, the user has to request approval from every
device where they want to install the application. The admin then approves or denies
the request for each of the user's devices where requests were made.

  ７ Note

  Configuration Manager doesn't enable this feature by default. Before using it,
  enable the optional feature Approve application requests for users per device. For
  more information, see Enable optional features from updates.

Software Center requires the user to submit the request for the application from their
device. The user sees this message in Software Center:

<!-- p.545 -->

                                                                                       

The user specifies why they want the application and submits the approval request:

                                                                                       

Once the admin approves the request, the user can install the application on their
device. If the user takes no action, the application is automatically installed for the user
during non-business hours.

<!-- p.546 -->

                                                                                   

Scenario 2: Integrate an application approval
system
The Northwind Traders has an existing application approval system, and the admin
wants to integrate the approval system with Configuration Manager.

The admin deploys an application to all users and configures it to require approval.
Then, the admin enables the Software Center client setting to Hide unapproved
applications in Software Center.

<!-- p.547 -->

                                                                               

With this option, the user doesn't see the application in Software Center until the
application request is approved for installation on the device. When approval is granted
via the organization's approval system, the orchestration system can make an approved
request for the user and their device in Configuration Manager. The orchestration
systems used the CreateApprovedRequest WMI method in Configuration Manager. This
method then uses the existing Configuration Manager application deployment
mechanism. It doesn't modify collection memberships, and it takes effect immediately.
The application is now available to the user in Software Center.

The admin can also configure the automation to automatically install the application on
the user's device. No other users will see the application as available in Software Center
until the approval is granted. This solution provides per-user and per-device control of
the software without the need to create separate collections.

The WMI method CreateApprovedRequest in the SMS_UserApplicationRequest class has
the following input parameters:

Required parameters
     ClientGUID - Unique identifier of the client

<!-- p.548 -->

     Username - Unique username of the user
     ApplicationID - Model name of the application

The ApplicationID is the ModelName property of the SMS_Application instance. This
value is the unique ID of the application without the version. For example,
ScopeId_21A9ED3B-D8C6-49DC-87A6-01F296182F14/Application_40243740-01f2-48db-abf0-

c95259986d94 .

Optional parameters
     Comments - Comments for the approved request to be displayed in the Software

     Center. By default, it specifies an empty string.

     AutoInstall - Install the application immediately after the request is approved. By

     default, this parameter is true.

        ７ Note

        In version 2006 and earlier, you could only call this method once for a specific
        app. Starting in version 2010, you can call this method more than once. If the
        AutoInstall parameter is $true , the client tries to install the app again.

The following code sample is a Windows PowerShell script that shows how to invoke the
WMI method for a specific user, machine, and application:

  PowerShell

  $machinename = $args[0]
  $username = $args[1]
  $appid = $args[2]
  $autoInstall = $args[3]
  $comments = $args[4]

  $scObj=Get-WmiObject -Namespace root\sms -Query 'select SiteCode from
  sms_providerlocation'
  $sitecode = $scObj.SiteCode
  $namespace ="root\sms\site_" + $sitecode
  $machine = Get-WmiObject -Namespace $namespace -Query "SELECT * FROM
  SMS_R_SYSTEM WHERE Name = '$machinename'"
  $clientGuid = $machine.SMSUniqueIdentifier
  Invoke-WmiMethod -Path "SMS_UserApplicationRequest" -Namespace $namespace -
  Name CreateApprovedRequest -ArgumentList @($appid, $autoInstall,
  $clientGuid, $comments, $username)

The following command line runs the sample script:

<!-- p.549 -->

  PowerShell

  .\CreateApprovedRequest.ps1 "MachineName" "Domain\User" "ScopeId_2E4DAE44-
  C9A0-4694-8B7A-474424C080D4/Application_88808a3a-86e4-4820-be59-aa7d61cb8c33
  "true" "Application has been approved"

The admin can still see the approved requests in the Configuration Manager console
from Software Library > Application Management > Approval Requests.

                                                                                        

Limitations
The current version of this application approval WMI method has the following
limitations:

   1. The CreateApprovedRequest method can be called only once for a unique machine
     ID, application ID, and username combination. It returns an error if the method is
     called with the same parameters more than once. The details about this error are in
      SMSProv.log .

   2. To enable the automatic install of the application, deploy the application to a
     collection of users or user groups before calling the WMI method. If you create the
     deployment after calling the WMI method, the application is made available to the
     user for install and won't be automatically installed.

Scenario 3: Revoke application approval
If the admin revokes the approval, or the application is no longer in use, uninstall the
application.

The admin revokes the approval of the application using the Configuration Manager
console, a PowerShell script, or WMI. Even if the application was already approved, the
admin can use the Deny option. Revoking the approval prevents the user from installing

<!-- p.550 -->

the application on their device. The same action also causes uninstallation of the
application on the user's device if the application was previously installed.

Learn more about the Deny-CMApprovalRequest cmdlet.

Prerequisites to revoke app approvals
   1. Set the Select these new settings to specify company information client setting to
     Yes.
   2. Enable the optional feature Approve application requests for users per device. For
     more information, see Enable optional features from updates.

Scenario 4: Machine-based pre-approved
requests
You can use the CreateApprovedRequest API to create a pre-approved request for a
device with no user required. This action allows you to install and uninstall applications
in real time. Currently this functionality is only available in the SDK. For machine-based
pre-approved requests to work, you must also enable the optional feature Approve
application requests for users per device. For more information, see Enable optional
features from updates.

Administrators can create a machine-available deployment that requires approval using
the New-CMApplicationDeployment cmdlet. Here's an example:

  PowerShell

  New-CMApplicationDeployment -CollectionName "All Systems" -Name "Test app" -
  DeployAction Install -DeployPurpose Available -ApprovalRequired $true -
  DistributionPointName 'DistributionPoint.domain.com" -DistributeContent

A deployment created with the requires approval flag set to true stays on the server
and can be used with larger collections. The user-request flow isn't yet available for
machine-targeted deployments that require approval. So, the application isn't visible in
Software Center until you create a pre-approved request to the individual device.

The following Windows PowerShell sample script shows how to invoke the WMI method
for a machine and application to create a pre-approved request:

  PowerShell

<!-- p.551 -->

  $machinename = $args[0]
  $appid = $args[1]
  $autoInstall = $args[2]
  $comments = $args[3]

  $scObj=Get-WmiObject -Namespace root\sms -Query 'select SiteCode from
  sms_providerlocation'
  $sitecode = $scObj.SiteCode
  $namespace ="root\sms\site_" + $sitecode
  $machine = Get-WmiObject -Namespace $namespace -Query "SELECT * FROM
  SMS_R_SYSTEM WHERE Name = '$machinename'"
  $clientGuid = $machine.SMSUniqueIdentifier
  Invoke-WmiMethod -Path "SMS_ApplicationRequest" -Namespace $namespace -Name
  CreateApprovedRequest -ArgumentList @($appid, $autoInstall, $clientGuid,
  $comments)

The following command line runs the sample script:

  PowerShell

  .\CreateApprovedRequestForMachine.ps1 "MachineName" "ScopeId_2E4DAE44-C9A0-
  4694-8B7A-474424C080D4/Application_88808a3a-86e4-4820-be59-aa7d61cb8c33
  "true" "Application has been approved"

Setting the autoInstall parameter to false has no effect in Configuration Manger for
machine-based pre-approved request. As soon as the pre-approved request is created
on the site, the device will attempt to install the application. You can deny the approval
request to remove the application from the device.

                                                                                     

Scenario 5: Reapprove a previously denied
application request
You can reapprove an application request that was previously denied. Reapproval is
available only through the SDK API. The following PowerShell sample script
demonstrates approving a request after it has been denied:

  PowerShell

<!-- p.552 -->

  $machinename = $args[0]
  $username = $args[1]
  $appid = $args[2]

  $scObj=Get-WmiObject -Namespace root\sms -Query 'select SiteCode from
  sms_providerlocation'
  $sitecode = $scObj.SiteCode
  $namespace ="root\sms\site_" + $sitecode
  $reqObj = Get-WmiObject -Namespace $namespace -Class
  SMS_UserApplicationRequest | Where {$_.ModelName -eq $appid -and
  $_.RequestedMachine -eq $machinename -and $_.User -eq $username }
  $reqObjPath = $reqObj.__PATH
  Invoke-WmiMethod -Path $reqObjPath -Name Approve

The following command line runs the sample script:

  PowerShell

  .\ReapproveRequest.ps1 "MachineName" "DomainName\Username"
  "ScopeId_2E4DAE44-C9A0-4694-8B7A-474424C080D4/Application_88808a3a-86e4-
  4820-be59-aa7d61cb8c33"

Scenario 6: Email notifications for application
approval requests
Administrators can configure email notifications for application approval requests. You
can specify application approvers during the application deployment. All approvers
receive an email notification when a user requests an application and can approve or
deny the request using the links provided in the email. You can also configure the cloud
management gateway to enable approving application requests outside of the internal
network.

Prerequisites for email notifications
     Starting in version 2107, the SMS Provider requires .NET version 4.6.2, and version
     4.8 is recommended. In version 2103 and earlier, this role requires .NET 4.5 or later.
     For more information, Site and site system prerequisites.

     Enable the optional feature Approve application requests for users per device. For
     more information, see Enable optional features from updates.

     If PKI certificate infrastructure isn't set up, enable Enhanced HTTP.

<!-- p.553 -->

       ７ Note

       The configuration for Enhanced HTTP is per primary site. If you enable it on
       any of the primary sites in a hierarchy, then Configuration Manager uses self-
       signed certificates on all providers. This behavior includes the CAS and other
       primary sites.

Configure email notifications
  1. In the Configuration Manager console, go to Administration > Site Configuration
    -> Sites.
  2. Select the top-level site in your hierarchy and select Configure Site Components in
    the ribbon.
  3. Select Email Notification to open the Properties dialog.
  4. Check Enable email notification for alerts and specify the port of your SMTP
    server. If you're using Microsoft 365, you can use the Microsoft 365 SMTP server.
  5. Enter the FQDN or IP address of the SMTP server.
  6. Select to Specify an account, select Set, then select New Account.
  7. Provide a username and password for the new account and click OK.
  8. Enter the Sender address for email alerts.
  9. Click Apply.
 10. You can test the SMTP server by sending an email sample. Select Test SMTP Server
    in the Email Notification Properties dialog.

          Review errors in NotiCtlr.log .
          It's recommended to configure SSL with a PKI certificate on the SMS Provider
          to successfully approve or deny the request in the internal network when
          cloud management gateway isn't set up. Otherwise, you'll see the page
          containing the warning "There is a problem with this security certificate".

<!-- p.554 -->

                                                                                      

Approve application requests outside of the internal
network
To approve application requests outside of the internal network, additional settings are
required:

   1. Enable Allow Configuration Manager cloud management gateway traffic in
     Administration > Site Configuration > Servers and Site Systems Roles > SMS
     Provider > Properties.
   2. Configure the cloud management gateway.
   3. Enable Microsoft Entra user Discovery.
   4. Configure the following settings for this native app (client app) in Microsoft Entra
     ID. These settings should be configured manually in the Azure portal      .

            Redirect URI: https://<CMG FQDN>/CCM_Proxy_ServerAuth/ImplicitAuth . Use
            the fully qualified domain name of the cloud management gateway (CMG)

<!-- p.555 -->

          service, for example, GraniteFalls.Contoso.com.

                                                                                   

          Manifest: Set oauth2AllowImplicitFlow to true. For example:
           "oauth2AllowImplicitFlow": true,

                                                                                   

Test the email approval process
Let's walk through the end-to-end scenario:

   1. You deploy an application as available to a user collection. On the Deployment
     Settings page, enable it for approval. Also, you enter a few email addresses to
     receive notification about application requests.

<!-- p.556 -->

                                                                                  

 2. The user sees the new application in Software Center and sends the request for it.
   The site sends the email notification within five minutes to the addresses specified
   in the application deployment.

 3. An email receiver chooses Approve or Deny. A success message is shown in the
   browser if the site successfully processed the application request.

        If an application request is approved or denied via email, the links expire and
        can't be used by anyone else.

Known issues

<!-- p.557 -->

1. A 404 error is shown after Approve or Deny links clicked.

          There isn't a certificate bound to the Admin Service. Check if the
          Configuration Manager-generated certificates feature is enabled. Otherwise,
          set up your own PKI certificates infrastructure.
          Check SMS_REST_PROVIDER.log for any errors.

2. There is a problem with this security certificate warning after Approve or
  Deny links are clicked.

          Configuration Manager-generated certificate isn't trusted by the web browser
          on the client. It's recommended to set up PKI certificates infrastructure when
          links are used in the internal network.

3. Service is unavailable, HTTP Error 503 message.

          Check if the Admin Service is running. On a provider machine, go to Task
          Manager > Details. Make sure there's an active process called
          sccmprovidergraph.exe

          Open the Configuration Manager Console, Administration > Site
          Configuration > Servers and Site Systems Roles > SMS Provider. Right click
          on Properties. Make sure that Allow Configuration Manager cloud management
          gateway traffic. is checked when email approval feature is intended to use

          with Cloud Management Gateway; and not checked when the feature is used
          to approve or deny requests in the internal network.

4. Links to approve or deny request through Cloud Management Gateway don't
  work.

          Verify that Microsoft Entra user Discovery is enabled.
          Make sure that e-mail address specified during application deployment
          belongs to your organization.

5. Email isn't sent when a user requested an application.

          Verify the email address is correct.
          Make sure email notifications for alerts are configured.
          Check NotiCtrl.log for errors.

6. Error in the Create Application Deployment wizard.

          Make sure you have rights to create a subscription. The subscription will be
          automatically created during application deployment.

<!-- p.558 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.559 -->

Deployment Type Extension Versioning
Article • 01/12/2024

Configuration Manager supports in-place versioning for minor upgrades and out-of-
place versioning for major upgrades.

Versioning

Minor Revisions
Configuration Manager supports in-place versioning for minor upgrades that are
backwards compatible. For in-place versioning, increment the version number.

Major Revisions
Configuration Manager supports out-of-place versioning for major upgrades that aren't
backwards compatible. For out-of-place versioning, it's necessary to create a new
extension and technology ID.

See Also
Configuration Manager Reference

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.560 -->

Extending Application Management
Overview
Article • 10/04/2022

By default, Application Management supports creating numerous deployment types
such as Windows Installer, Script Installer, Microsoft Application Virtualization, Nokia SIS
files and Windows Mobile Cabinet file deployment technologies. Partners that must
continue to use a specific deployment technology not natively supported by
Configuration Manager, can extend the Application Management model to support a
custom deployment type.

In Application Management, the application object is the high-level object that
Configuration Manager Administrators will create, deploy and monitor. The deployment
type object represents the technology that will be detected, installed and uninstalled on
the end-user systems. The Application Management model can be extended by creating
an instance of deployment type with a custom deployment technology.

The deployment type object is composed of multiple objects: deployment technology,
hosting technology, installer technology, content importer and the installer. The installer
object is a key extension point, as it provides the properties for a technology, as well as
the logic for detection, installation and uninstallation of the technology on the client
system.

Extending the application model requires extending the Configuration Manager
consoles and Configuration Manager clients that will leverage the custom deployment
type. On the server, the extension is accomplished through creating and registering a
custom deployment technology assembly and by extending Configuration Manager
console (adding custom property sheets and wizards). The client extension is
accomplished through extending WMI and adding a custom handler (a public COM
class and methods). It should be noted that the client extension closely maps to the
installer object, defined as part of the deployment type. The properties and methods
defined in the installer object map directly to the property values are stored in WMI and
the public COM methods defined in the custom handler.

In conceptualizing a custom deployment type, it might be useful to consider the in-
product handling of Windows Installer files (*.msi).

   Tip
