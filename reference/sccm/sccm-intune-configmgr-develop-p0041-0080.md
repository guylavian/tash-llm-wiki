---
title: "Configuration Manager SDK documentation — pages 41-80"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0041-0080
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0041-0080
family: sccm
documentKind: "doc"
abstract: "package[\"PackageID\"].StringValue, package[\"Name\"].StringValue); } } catch (SmsException ex) { Console.WriteLine(\"Failed to list packages. Error: \" + ex.Message); throw; } } public void CreatePackage(WqlConnectionManager connection, string newPackageName, string newPackageDescrip"
---

# Configuration Manager SDK documentation — pages 41-80

<!-- p.41 -->

package["PackageID"].StringValue, package["Name"].StringValue);
                 }
             }
             catch (SmsException ex)
             {
                 Console.WriteLine("Failed to list packages. Error: " +
ex.Message);
                 throw;
             }
        }

        public void CreatePackage(WqlConnectionManager connection, string
newPackageName, string newPackageDescription)
        {
            try
            {
                // Create new package object.
                IResultObject newPackage =
connection.CreateInstance("SMS_Package");

                // Populate new package properties.
                newPackage["Name"].StringValue = newPackageName;
                newPackage["Description"].StringValue =
newPackageDescription;

                // Save the new package and the new package properties.
                newPackage.Put();
                // The key value 'PackageID' is created on the put, so
getting the package object to output the unique 'PackageID' ('Name' is not
guaranteed to be unique).
                newPackage.Get();

                 // Output new package name.
                 Console.WriteLine("Created Package ID: {0} Package Name:
{1}", newPackage["PackageID"].StringValue, newPackage["Name"].StringValue);
             }
             catch (SmsException ex)
             {
                 Console.WriteLine("Failed to create package. Error: " +
ex.Message);
                 throw;
             }
        }

        public void ModifyPackage(WqlConnectionManager connection, string
existingPackageID)
        {
            try
            {
                // Get the specific package instance to modify (PackageID is
a key value).
                IResultObject packageToModify =
connection.GetInstance(@"SMS_Package.PackageID='" + existingPackageID +
"'");

<!-- p.42 -->

                  // Modify a package properties (in this case description).
                  packageToModify["Description"].StringValue = "This package
  has been modified. " + packageToModify["Description"].StringValue;

                     // Save the new package and the new package properties.
                     packageToModify.Put();
                 }
                 catch (SmsException ex)
                 {
                     Console.WriteLine("Failed to delete package. Error: " +
  ex.Message);
                     throw;
                 }
          }

          public void DeletePackage(WqlConnectionManager connection, string
  existingPackageID)
          {
              try
              {
                  // Get the specific package instance to delete (PackageID is
  a key value).
                  IResultObject packageToDelete =
  connection.GetInstance(@"SMS_Package.PackageID='" + existingPackageID +
  "'");

                  // Output package ID and name being deleted.
                  Console.WriteLine("Deleting Package ID: {0} Package Name:
  {1}", packageToDelete["PackageID"].StringValue,
  packageToDelete["Name"].StringValue);

                     // Delete the package.
                     packageToDelete.Delete();
                 }
                 catch (SmsException ex)
                 {
                     Console.WriteLine("Failed to delete package. Error: " +
  ex.Message);
                     throw;
                 }
          }

      }
  }

The example method has the following parameters:

                                                                    ﾉ   Expand table

<!-- p.43 -->

 Parameter               Type                   Description

 connection              - Managed:             A valid connection to the SMS Provider.
                         WqlConnectionManager

 newPackageName          - Managed: String      The name of the new package.

 newPackageDescription   - Managed: String      The description for the new package.

 existingPackageID       - Managed: String      An existing Package identifier. This is a key
                                                value for the SMS_Package class and is used to
                                                return a specific instance of the SMS_Package
                                                class. The ListPackages method in the sample
                                                above returns the names and PackageIDs of
                                                the current package instances.

Compiling the Code
The C# example requires:

Namespaces
System

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

mscorlib

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
Software distribution overview SMS_Package Server WMI Class

<!-- p.44 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.45 -->

Calling Configuration Manager Code
Snippets
Article • 10/10/2022

The following code samples show how to set up the calling code for the code examples
that are used throughout the Configuration Manager Software Development Kit (SDK).

Replace the SNIPPETMETHOD snippet with the snippet that you want to run. In most
cases you will need to make changes, such as adding parameters, to make the code
work.

For more information about remote Windows Management Instrumentation (WMI)
connections, see Connecting to WMI on a Remote Computer.

Example
  vbs

  Dim connection
  Dim computer
  Dim userName
  Dim userPassword
  Dim password 'Password object

  Wscript.StdOut.Write "Computer you want to connect to (Enter . for local): "
  computer = WScript.StdIn.ReadLine

  If computer = "." Then
       userName = ""
       userPassword = ""
  Else
       Wscript.StdOut.Write "Please enter the user name: "
       userName = WScript.StdIn.ReadLine

      Set password = CreateObject("ScriptPW.Password")
      WScript.StdOut.Write "Please enter your password:"
      userPassword = password.GetPassword()
  End If

  Set connection = Connect(computer,userName,userPassword)

  If Err.Number<>0 Then
      Wscript.Echo "Call to connect failed"
  End If

  Call SNIPPETMETHODNAME (connection)

<!-- p.46 -->

Sub SNIPPETMETHODNAME(connection)
   ' Insert snippet code here.
End Sub

Function Connect(server, userName, userPassword)

    On Error Resume Next

    Dim net
    Dim localConnection
    Dim swbemLocator
    Dim swbemServices
    Dim providerLoc
    Dim location

    Set swbemLocator = CreateObject("WbemScripting.SWbemLocator")

    swbemLocator.Security_.AuthenticationLevel = 6 'Packet Privacy

    ' If the server is local, don not supply credentials.
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

<!-- p.47 -->

End Function

c#

using System;
using System.Collections.Generic;
using System.Text;
using System.ComponentModel;
using Microsoft.ConfigurationManagement.ManagementProvider;
using Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine;

namespace ConfigurationManagerSnippets
{
    class Program
    {
        static void Main(string[] args)
        {
            // Setup snippet class.

              string computer = "";
              string userName = "";
              string password = "";

              SnippetClass snippets = new SnippetClass();

              Console.WriteLine("Computer you want to connect to (Enter . for
local): ");
              computer = Console.ReadLine();
              Console.WriteLine();

              if (computer == ".")
              {
                  computer = System.Net.Dns.GetHostName();
                  userName = "";
                  password = "";
              }
              else
              {
                  Console.WriteLine("Please enter the user name: ");
                  userName = Console.ReadLine();

                  Console.WriteLine("Please enter your password:");
                  password = snippets.ReturnPassword();
              }

            // Make connection to provider.
            WqlConnectionManager WMIConnection = snippets.Connect(computer,
userName, password);

              // Call snippet function and pass the provider connection
object.
              snippets.SNIPPETMETHODNAME(WMIConnection);

<!-- p.48 -->

        }
    }

    class SnippetClass
    {
        public WqlConnectionManager Connect(string serverName, string
userName, string userPassword)
        {
             try
             {
                 SmsNamedValuesDictionary namedValues = new
SmsNamedValuesDictionary();
                 WqlConnectionManager connection = new
WqlConnectionManager(namedValues);
                 if (System.Net.Dns.GetHostName().ToUpper() ==
serverName.ToUpper())
                 {
                      connection.Connect(serverName);
                 }
                 else
                 {
                      connection.Connect(serverName, userName, userPassword);
                 }
                 return connection;
             }
             catch (SmsException ex)
             {
                 Console.WriteLine("Failed to Connect. Error: " +
ex.Message);
                 return null;
             }
             catch (UnauthorizedAccessException ex)
             {
                 Console.WriteLine("Failed to authenticate. Error:" +
ex.Message);
                 return null;
             }
        }

        public void SNIPPETMETHODNAME(WqlConnectionManager connection)
        {
            // Insert snippet code here.
        }

        public string ReturnPassword()
        {
            string password = "";
            ConsoleKeyInfo info = Console.ReadKey(true);
            while (info.Key != ConsoleKey.Enter)
            {
                if (info.Key != ConsoleKey.Backspace)
                {
                    password += info.KeyChar;
                    info = Console.ReadKey(true);
                }

<!-- p.49 -->

                  else if (info.Key == ConsoleKey.Backspace)
                  {
                      if (!string.IsNullOrEmpty(password))
                      {
                          password = password.Substring
                          (0, password.Length - 1);
                      }
                      info = Console.ReadKey(true);
                  }
               }
               for (int i = 0; i < password.Length; i++)
                   Console.Write("*");
               return password;
           }
      }
  }

Compiling the Code

Namespaces
System

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

  ７ Note

  The assemblies are in the <Program Files>\Microsoft Endpoint
  Manager\AdminConsole\bin folder.

Runtime Requirements
For more information, see Configuration Manager Server Runtime Requirements.

Robust Programming

<!-- p.50 -->

The Configuration Manager exceptions that can be raised are SmsConnectionException
and SmsQueryException. These can be caught together with SmsException.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.51 -->

How to Encrypt Passwords or Data for a
Site
Article • 10/10/2022

In Configuration Manager, user accounts connect to site systems and Active Directory to
perform various tasks. Prior to System Center 2012 Configuration Manager, the Manage
Site Accounts tool (MSAC) was used to manage these user accounts. The MSAC tool has
been deprecated. Using a new WMI method, these account passwords can be encrypted
for a specific site. The following code snipped demonstrates how user account
passwords can be encrypted for a specific site.

To Encrypt Data for a Site
   1. Connect to the Configuration Manager site.

   2. Get the parameters for the EncryptDataEx Method in Class SMS_Site method.

   3. Add the data to be encrypted to the Data parameter.

   4. Add the site code of the specific site for which the data should be encrypted to the
      SiteCode parameter.

   5. Encrypt the data for the specified site by invoking the EncryptDataEx Method in
      Class SMS_Site.

   6. In this case, the encrypted string is output as a test.

Example
The following example encrypts data for a specific site.

  using System;
  using System.Management;

  namespace Encryption
  {
      class Program
      {
          static void Main(string[] args)
          {
              // SMS_Site::EncryptDataEx is a class level method,

<!-- p.52 -->

              // it will encrypt data for the site based on passed in site
  code.
              try
              {
                  ManagementScope scope = new
  ManagementScope(@"root\sms\site_ABC");
                  ManagementClass cls = new ManagementClass(scope.Path.Path,
  "SMS_Site", null);
                  // Set up input parameters.
                  ManagementBaseObject inParams =
  cls.GetMethodParameters("EncryptDataEx");
                  inParams["Data"] = @"pass123"; // data to be encrypted
                  inParams["SiteCode"] = @"ABC"; // encrypt the data for that
  specific site

                  // Get the encrypted data.
                  ManagementBaseObject outSiteParams =
  cls.InvokeMethod("EncryptDataEx", inParams, null);

                    // print the encrypted data

  Console.WriteLine(outSiteParams["EncryptedData"].ToString());
              }
              catch (ManagementException e)
              {
                  Console.WriteLine("Failed to execute method {0}",
  e.ToString());
              }
          }
      }
  }

Compiling the Code
The C# example requires:

Namespaces
System

System.Management

Assembly

Robust Programming

<!-- p.53 -->

For more information about error handling, see About Configuration Manager Errors.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.54 -->

About Configuration Manager Errors
Article • 01/05/2024

In Configuration Manager, when a Configuration Manager error occurs it's either a
Windows Management Instrumentation (WMI) or an SMS Provider error.

A WMI error is reported in an instance of __ExtendedStatus. An SMS Provider error is
reported in an instance of SMS_ExtendedStatus .

How you process an error depends on the programming language that you're using.

Error Handling with WMI
In VBScript the error object Number property is non-zero if an error occurs during
synchronous operation. Typically, you check this value after making changes to, or
querying, the SMS Provider. In an asynchronous operation you receive an error object of
the OnCompleted callback function.

After you get the error object instance, you can check the __Class property to determine
the origin of the error. WMI creates an instance of __ExtendedStatus for WMI errors, and
the SMS Provider creates an instance of SMS_ExtendedStatus for SMS Provider errors.
SMS_ExtendedStatus is derived from __ExtendedStatus. The details of an SMS Provider

error can also be found in SMSProv.log.

For more information, see How to Handle Configuration Manager Synchronous Errors by
Using WMI.

How to Handle Configuration Manager Asynchronous Errors by Using WMI.

Error Handling with the Managed SMS Provider
To handle Configuration Manager errors by using the managed SMS Provider, you catch
the Configuration Manager-specific exceptions.

                                                                               ﾉ   Expand table

 Exception               Description

 SmsQueryException       SmsQueryException is raised when a Configuration Manager query error
                         occurs. It provides exception information specific to Configuration
                         Manager ( SMS_ExtendedStatus ) and also encapsulates any WMI
                         exceptions raised.

<!-- p.55 -->

 Exception                  Description

                            SmsQueryException.ErrorCode maps to the equivalent
                            System.ManagementException exception code.

                            SmsQueryException.ExtendStatusCode maps to the SMS Provider error
                            code raised in SMS_ExtendedStatus.ErrorCode .

 SmsConnectionException     SmsConnectionException is raised when the connection to WMI is lost.

 SmsException               SmsException is the base class from which SmsQueryException and
                            SmsConnectionException derive. It's never raised but can be caught to
                            catch both SmsQueryException and SmsConnectionException .

Accessing the __ExtendedStatus and the
SMS_ExtendedStatus objects
Because the __ExtendedStatus and SMS_ExtendedStatus aren't wrapped by the managed
SMS Provider, you must use the System.Management ManagedException object.

If you don't need access to the error WMI objects, you can get access to an exception
details string in SMSException.Details.

For more information about handling synchronous exceptions, see How to Handle
Configuration Manager Synchronous Errors by Using Managed Code.

For more information about handling asynchronous exceptions, see How to Handle
Configuration Manager Asynchronous Errors by Using Managed Code.

See Also
About errors How to Handle Configuration Manager Synchronous Errors by Using WMI
How to Handle Configuration Manager Asynchronous Errors by Using WMI
Configuration Manager Asynchronous Errors by Using Managed Code
How to Handle Configuration Manager Synchronous Errors by Using Managed Code

Feedback
Was this page helpful?      Yes      No

Provide product feedback

<!-- p.56 -->

How to Handle Configuration Manager
Asynchronous Errors by Using Managed
Code
Article • 10/10/2022

To handle a Configuration Manager error that is raised during an asynchronous query,
you test the RunWorkerCompletedEventArgs parameter Error Exception property that is
passed to the SmsBackgroundWorker.QueryProcessorCompleted event handler. If Error
is not null , an exception has occurred and you use Error to discover the cause.

If Error is an SmsQueryException, you can use it to get to the underlying
__ExtendedException or SMS_ExtendedException . Because the managed SMS Provider

library does not wrap these exceptions you will need to use the System.Management
namespace ManagementException object to access them.

To handle an asynchronous query error
   1. Create an asynchronous query.

   2. In the asynchronous query SmsBackgroundWorker.QueryProcessorCompleted
       event handler, implement the code in the following example.

   3. Run the asynchronous query. To test the exception handler, pass a badly formed
       query string such as Select & from &&& to the QueryProcessorBase.ProcessQuery
       method.

Example
The following example implements a SmsBackgroundWorker.QueryProcessorCompleted
event handler.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  c#

  void bw1_QueryProcessorCompleted(object sender, RunWorkerCompletedEventArgs
  e)
  {
      if (e.Error != null)
      {

<!-- p.57 -->

          Console.WriteLine("There was an Error");
          if (e.Error is SmsQueryException)
          {
              SmsQueryException queryException = (SmsQueryException)e.Error;
              Console.WriteLine(queryException.Message);

              // Get either the __ExtendedStatus or SMS_ExtendedStatus object
  and display various properties.
              ManagementException mgmtExcept = queryException.InnerException
  as ManagementException;

              if (mgmtExcept != null)
              {
                  if
  (string.Equals(mgmtExcept.ErrorInformation.ClassPath.ToString(),
  "SMS_ExtendedStatus", StringComparison.OrdinalIgnoreCase) == true)
                  {
                      Console.WriteLine("Configuration Manager provider
  exception");
                  }

                  else if
  (string.Equals(mgmtExcept.ErrorInformation.ClassPath.ToString(),
  "__ExtendedStatus", StringComparison.OrdinalIgnoreCase) == true)
                  {
                      Console.WriteLine("WMI exception");
                  }
                  Console.WriteLine(mgmtExcept.ErrorCode.ToString());

  Console.WriteLine(mgmtExcept.ErrorInformation["ParameterInfo"].ToString());

  Console.WriteLine(mgmtExcept.ErrorInformation["Operation"].ToString());

  Console.WriteLine(mgmtExcept.ErrorInformation["ProviderName"].ToString());
              }

          }
          if (e.Error is SmsConnectionException)
          {
              Console.WriteLine("There was a connection error :" +
  ((SmsConnectionException)e.Error).Message);
              Console.WriteLine(((SmsConnectionException)e.Error).ErrorCode);
          }
      }

      Console.WriteLine("Done...");
  }

The example method has the following parameters:

                                                                 ﾉ   Expand table

<!-- p.58 -->

 Parameter    Type                          Description

 sender       - Object                      The source of the event.

 e            -                             The event data.
              RunWorkerCompletedEventArgs
                                            For more information, see
                                            RunWorkerCompletedEventArgs Class.

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

System.Management

System.ComponentModel

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

System.Management

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also

<!-- p.59 -->

About errors

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.60 -->

How to Handle Configuration Manager
Synchronous Errors by Using Managed
Code
Article • 10/10/2022

To handle a Configuration Manager error that is raised in a synchronous query, you
catch the SmsQueryException exception. Because this exception is also caught by
SMS_Exception], you can catch it and the SmsConnectionException exception in the
same catch block.

If the exception that is caught in an SMS_Exception is an SmsQueryException, you can
use it to get to the underlying __ExtendedException or SMS_ExtendedException . Because
the managed SMS Provider library does not wrap these exceptions, you will need to use
the System.Management namespace ManagementException object to access them.

  ７ Note

  For clarity, most examples in this documentation simply re-throw exceptions. You
  can replace them with the following example if you want more informative
  exception information.

To handle a synchronous query error
   1. Write code to access the SMS Provider.

   2. Use the following example code to catch the SmsQueryException and
       SmsConnectionException exceptions.

Example
The following C# example function attempts to open a nonexistent SMS_Package
package. In the exception handler, the code determines what type of error has been
raised and displays its information.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  c#

<!-- p.61 -->

public void ExerciseException(WqlConnectionManager connection)
{
    try
    {

        IResultObject package =
connection.GetInstance(@"SMS_Package.PackageID='UNKNOWN'");
        Console.WriteLine("Package Name: " + package["Name"].StringValue);
        Console.WriteLine("Package Description: " +
package["Description"].StringValue);

    }
    catch (SmsException e)
    {
        if (e is SmsQueryException)
        {
            SmsQueryException queryException = (SmsQueryException)e;
            Console.WriteLine(queryException.Message);

            // Get either the __ExtendedStatus or SMS_ExtendedStatus object
and display various properties.
            ManagementException mgmtExcept = queryException.InnerException
as ManagementException;

            if (mgmtExcept != null)
            {
                if
(string.Equals(mgmtExcept.ErrorInformation.ClassPath.ToString(),
"SMS_ExtendedStatus", StringComparison.OrdinalIgnoreCase) == true)
                {
                    Console.WriteLine("Configuration Manager provider
exception");
                }

                else if
(string.Equals(mgmtExcept.ErrorInformation.ClassPath.ToString(),
"__ExtendedStatus", StringComparison.OrdinalIgnoreCase) == true)
                {
                    Console.WriteLine("WMI exception");
                }
                Console.WriteLine(mgmtExcept.ErrorCode.ToString());

Console.WriteLine(mgmtExcept.ErrorInformation["ParameterInfo"].ToString());

Console.WriteLine(mgmtExcept.ErrorInformation["Operation"].ToString());

Console.WriteLine(mgmtExcept.ErrorInformation["ProviderName"].ToString());
            }

        }
        if (e is SmsConnectionException)
        {
            Console.WriteLine("There was a connection error :" +
((SmsConnectionException)e).Message);

<!-- p.62 -->

                  Console.WriteLine(((SmsConnectionException)e).ErrorCode);
              }
      }
  }

The example method has the following parameters:

                                                                          ﾉ   Expand table

 Parameter         Type                       Description

 connection        - WqlConnectionManager     A valid connection to the provider.

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

System.Management

System.ComponentModel

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

System.Management

Robust Programming

<!-- p.63 -->

For more information about error handling, see About Configuration Manager Errors.

See Also
About errors How to Handle Configuration Manager Asynchronous Errors by Using
Managed Code

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.64 -->

How to Handle Configuration Manager
Asynchronous Errors by Using WMI
Article • 10/10/2022

In Configuration Manager, when an error occurs in an asynchronous call, the error
object is passed as the second parameter to the OnCompleted method. Inside your
OnCompleted implementation, you check the error object the same as you would for a

synchronous call.

You determine if there is an error by checking the HResult parameter of the
OnCompleted method.

Example
This VBScript sample displays error information if there is a error during an
asynchronous operation. To test, change the query to an invalid query such as Select *
From ????? .

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub sink_OnCompleted(HResult, oErr, oCtx)
      WScript.Echo "All collections returned"

      if HResult <> 0 Then
      ' Determine the type of error.
          If oErr.Path_.Class = "__ExtendedStatus" Then
              WScript.Echo "WMI Error: "& oErr.Description
          ElseIf ExtendedStatus.Path_.Class = "SMS_ExtendedStatus" Then
              WScript.Echo "Provider Error: "& oErr.Description
              WScript.Echo "Code: " & oErr.ErrorCode
          End If
      End If
      bdone = true
  End sub

.NET Framework Security

<!-- p.65 -->

Using script to pass the user name and password is a security risk and should be
avoided where possible.

See Also
About errors
WMI SDK
How to Handle Configuration Manager Synchronous Errors by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.66 -->

How to Handle Configuration Manager
Synchronous Errors by Using WMI
Article • 10/10/2022

You handle synchronous errors, in Configuration Manager, by inspecting the
SWbemLastError object when an error occurs. An error has occurred when the error

object Number property is non-zero.

  ７ Note

  In VBScript you should declare that you want to resume running the script if an
  error occurs. Otherwise, the script will end when an error condition occurs. To do
  this, use the On Error Resume Next declaration in your script.

Example
The following VBScript example displays the most recent error information that is
available from the SWbemLastError object. You can use the following code, which tries to
get an invalid SMS_Package package to test it.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ExerciseError(connection)

        On Error Resume next

        Dim packages
        Dim package

        ' Run the query.
        Set package = connection.Get("SMS_Package.PackageID='UNKNOWN'")

        If Err.Number<>0 Then
            Call DisplayLastError
        End If

  End Sub

<!-- p.67 -->

  vbs

  Sub DisplayLastError
      Dim ExtendedStatus

        ' Get the error object.
        Set ExtendedStatus = CreateObject("WbemScripting.SWBEMLastError")

      ' Determine the type of error.
      If ExtendedStatus.Path_.Class = "__ExtendedStatus" Then
          WScript.Echo "WMI Error: "& ExtendedStatus.Description
      ElseIf ExtendedStatus.Path_.Class = "SMS_ExtendedStatus" Then
          WScript.Echo "Provider Error: "& ExtendedStatus.Description
          WScript.Echo "Code: " & ExtendedStatus.ErrorCode
      End If
  End Sub

See Also
About errors
WMI SDK

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.68 -->

Configuration Manager Objects
Overview
Article • 10/10/2022

The Configuration Manager objects are instances of Configuration Manager-specific
Windows Management Instrumentation (WMI) classes that are managed by the SMS
Provider. The Configuration Manager object class categories are described in the
following table.

                                                                              ﾉ       Expand table

 Configuration Manager     Description
 Object Class Category

 Software distribution     Objects associated with the software distribution feature of
                           Configuration Manager, such as advertisement, collection, package,
                           and program objects.

 Scheduling                Organizes scheduled Configuration Manager events, such as
                           inventory updates.

 Site                      Contains information about Configuration Manager sites.

 Security                  Describes the permissions granted to users and user groups to
                           operate on specific Configuration Manager-secured objects, such as
                           program and package objects.

 Query                     Describes Configuration Manager site database queries.

 Resource                  Populated when Configuration Manager discovers potential client
                           computers, users, user groups, and other types of objects within the
                           boundaries of the site.

 Inventory                 Provides the structure for inventory operations on Configuration
                           Manager client systems, users, and user groups.

 Software metering         Describes the metered Configuration Manager resources, such as
                           program files.

 Status and summarizer     Indicates the status of Configuration Manager sites, components,
                           and software distribution operations.

 Collected files           Contains information about files collected from clients.

DebugView

<!-- p.69 -->

To show SMS Provider object property values in the Configuration Manager console
results pane, start the console with the following command line:

<InstallationDirectory>\Microsoft.ConfigurationManagement.exe /SMS:DebugView=1

For more information, see Configuration Manager console command-line options.

See Also
Configuration Manager Association Classes
Configuration Manager Bit Field Properties
Configuration Manager console command-line options Configuration Manager Date
and Time Formats
Configuration Manager Embedded Objects
Configuration Manager Extended WMI Query Language
Objects overview Configuration Manager Lazy Properties
About errors Configuration Manager Object Security
Configuration Manager Special Queries

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.70 -->

Configuration Manager Object Security
Article • 10/10/2022

Delegate Verb
The delegate verb in Configuration Manager provides administrators with a way of
allowing users to assign to other users the instance permissions to an object in a very
limited way. The rights that a user is allowed to assign (or revoke) to other users are
limited to the instance rights that have been explicitly granted to that user. When a user
creates a secured object, that user is automatically granted explicit instance rights to
that object (usually read, modify, and delete).

To some extent, these explicitly granted rights provide the user with a certain level of
ownership of the object. With the delegate right, this ownership is extended to the
control of the default group of instance rights. To limit which rights a user can delegate,
only rights explicitly granted to them (not a group to which they belong) can be
delegated. A user can also remove other users (or groups) instance rights if the user has
the delegate permission and explicit rights to an object (this is why a user is said to own
an object if they have explicit instance rights). Users with administrator rights still have
full control of administering permissions.

A common scenario for using the delegate verb is when a user has created and
delegated rights for an object type and wants to create an object and allow members of
a user group to see it. They create an instance of the object and then delegate read
permissions for the instance to the user group.

The delegate verb is applicable to the following Configuration Manager classes:

      SMS_Collection

      SMS_Package

      SMS_Advertisement

      SMS_Site

      SMS_Query

      SMS_Report

      SMS_MeteredProductRule

<!-- p.71 -->

System Resource (SMS_R_System) as a Secured
Resource
Secured resources are resources (the SMS_R_* classes) that require collection read rights
to be viewed. If the user has class-level collection read rights, the user can see all the
instances of a secured resource. If the user only has instance-level read rights to certain
collections, the user only has rights to see resources that are members of those
collections. SMS_R_User and SMS_R_UserGroup are secured resources in SMS 2.0. In SMS
2003, SMS_R_System (the system resource) is also a secured resource.

Inventory instances (SMS_G_System_*) are secured similarly with the read resource verb.
If a user has class-level rights, that user can see inventory data belonging to all
resources. If the user doesn't have class-level rights, the user can see only inventory data
for inventory that belongs to resources that are members of collections to which the
user has instance-level read resource rights. Conversely, if a user has read resource
rights to a collection, a user can see the inventory data for the members of that
collection. This hasn't been affected by the change in security to SMS_R_System . Read
resource rights can't be granted to a user without granting read rights. When a user
doesn't have the appropriate class-level collection rights, resource security is enforced
through collection limiting.

Securing File Submissions to a Configuration
Manager Server
The recommended location for copying data discovery record (DDR) files and Managed
Information Format (MIF) files that not related to existing Configuration Manager clients
is directly in the site server inboxes. This requires administrator level permissions on the
site server to be granted to the application that is copying these files. These are located
as follows:

DDR files: <SMS>/inboxes/ddm.box

MIF files: <SMS>/inboxes/inventry.box

See Also
Objects overview Configuration Manager Association Classes
Configuration Manager Bit Field Properties
Configuration Manager Date and Time Formats
Configuration Manager Embedded Objects

<!-- p.72 -->

Configuration Manager Extended WMI Query Language
Configuration Manager Lazy Properties
Configuration Manager Special Queries
About errors

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.73 -->

Configuration Manager Embedded
Objects
Article • 10/10/2022

Configuration Manager embedded objects do not exist by themselves in the Common
Information Model (CIM) repository — they exist within other objects. As a result, you
cannot use Windows Management Instrumentation (WMI) to enumerate, query, get, or
put embedded objects. You can only retrieve and store embedded objects through the
parent instance.

Embedded objects are commonly used when accessing the site control file. In this case,
special embedded objects, such as properties and property lists are used.

When a class or method contains an embedded object of an abstract type, such as
SMS_ScheduleToken , you store and retrieve classes that are inherited from it. For example,

instead of using SMS_ScheduleToken , you use one of the embedded objects inherited
from it, such as SMS_ST_RecurWeekly .

See Also
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.74 -->

Configuration Manager Association
Classes
Article • 10/10/2022

In Configuration Manager, an association allows you to logically relate the instances of
two classes. Typically, an association consists of two key properties (which are paths, or
pointers, that uniquely identify the location of the other class instances), but an
association can also contain additional properties. The provider uses the key properties
to retrieve the requested data.

Although association classes provide a convenient means to collect related information,
they are inherently slow. If performance is an issue, you should consider collecting the
related information yourself.

  ７ Note

  Association classes are read-only except for the SMS_CollectToSubCollect_a class.
  Association class names are suffixed with _a.

The following table shows the association classes.

                                                                                  ﾉ     Expand table

 Association class                   Description

 SMS_AdvertToSourceSite_a            Relates an advertisement with the site that created the
                                     advertisement.

 SMS_BaseAssociation                 An abstract class that is the base class for all Configuration
                                     Manager association classes. It has no properties.

 SMS_CollectionMember_a              Relates a collection with its member resources.

 SMS_CollectionToPkgAdvert_a         Relates an advertisement with its target collection.

 SMS_CollectToSubCollect_a           Relates a collection with its parent collection.

 SMS_ObjectToClassPermissions_a      Relates a secured object with various users that have class
                                     permissions on the object.

 SMS_ObjectToInstancePermissions_a   Relates a secured object with users that have permissions
                                     for an instance of a secured object.

 SMS_PackageToAdvert_a               Relates an advertisement to the package it advertises.

<!-- p.75 -->

 Association class                  Description

 SMS_PackageToSourceSite_a          Relates a package to the site that created the package.

 SMS_PDFPkgToPDFProgram_a           Relates a package definition file package to package
                                    definition file programs that are part of the package.

 SMS_PkgToPkgAccess_a               Relates a package with the user accounts that are used to
                                    access a package on its distribution points.

 SMS_PkgToPkgProgram_a              Relates a package with the programs that form the
                                    package.

 SMS_PkgToPkgServer_a               Relates a package with its distribution points.

 SMS_SCFToSCI_a                     Relates a site control file with the site control items that
                                    make up the current site control file.

 SMS_SCFToSite_a                    Relates a site control file with the site to which it belongs.

 SMS_SiteToROOTColl_a               Relates a site with the root of the collections that belong to
                                    it.

 SMS_SiteToSiteID_a                 Relates a site with its identifying information.

 SMS_SiteToSubSite_a                Defines the hierarchy of sites by relating a site with its
                                    subsites.

See Also
Configuration Manager Bit Field Properties
Configuration Manager Date and Time Formats
Configuration Manager Embedded Objects
Configuration Manager Extended WMI Query Language
Objects overview Configuration Manager Lazy Properties
About errors Configuration Manager Object Security
Configuration Manager Special Queries

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.76 -->

Configuration Manager Date and Time
Formats
Article • 10/10/2022

Actions, in Configuration Manager, that include date and time values are common, such
as get current date and time, 50 days from today is what date?, or find out what day of
the week falls on a certain date. When you write queries or compose reports from
information that is stored in the Configuration Manager site database, you can express
the date and time in any valid SQL format. An example is any expression that has a SQL
Server datetime data type or that can be converted implicitly, such as an appropriately
formatted character string (for example, "1998.10.31").

The times that are stored in the Configuration Manager site database can be local or in
Coordinated Universal Time (UTC). Status Message Viewer can convert to local time, but
queries and reports cannot. What you see might be seven hours later than expected, if
local time is Pacific Daylight time. Therefore, the user must be aware of the following:

Status messages are all in UTC.

Offers can be in UTC or local time, depending on a switch that is set in the Configuration
Manager console. The property in SMS_Advertisement is AssignedScheduleIsGMT
( true / false ).

Inventory is always in local time.

This property is lazy , but you can view it by using WBEMtest.

Depending on the context, you might encounter time notations in the following format:

19981118175900000000+***

The following information corresponds to the values in the previous example.

                                                                          ﾉ   Expand table

 Value                      Description

 1998                       Year

 11                         Month

 18                         Day

 1759                       Hour

<!-- p.77 -->

 Value                     Description

 00                        Second

 000000                    Microsecond

 +***                      Offset from local time

The following table lists valid datetime formats that you can use.

                                                                           ﾉ    Expand table

 Style number without       Style number with       Type             Output Style
 century                    century

 -                          0 or 100                Default          mon dd yyyy hh:mm

 1                          101                     USA              mm/dd/yyyy

 1                          102                     ANSI             yyyy.mm.dd

 3                          103                     British/French   dd/mm/yyyy

 4                          104                     German           dd.mm.yyyy

 5                          105                     Italian          dd-mm-yyyy

 6                          106                     –                dd-mon-yyyy

 7                          107                     –                mon.dd.yyy

 –                          8 or 108                –                hh:mm:ss

 –                          9 or 109                –                mon dd yyyy

                                                                     hh:mi:ss:mmmAM (or
                                                                     PM)

 10                         110                     USA              mm-dd-yy

 11                         111                     JAPAN            yy/mm/dd

 12                         112                     ISO              yymmdd

 –                          13 or 113               –                dd mon yyyy

                                                                     hh:mi:ss:mmm (24 h)

 14                         114                     –                hh:mi:ss:mmm (24 h)

<!-- p.78 -->

Besides full datetime formats, you can also use datepart formats, which are also valid
for Query Builder or for writing reports from the Configuration Manager site database.
Datepart formats provide only part of the full datetime format (for example, the year or

just the day of the month). The following table lists valid datepart formats.

                                                                            ﾉ   Expand table

 Datepart value                     Abbreviations                  Limits

 Year                               Yy                             1753-9999

 Month                              Mm                             1-12

 Day                                Dd                             1-31

 Hour                               Hh                             1-23

 Minute                             Mi                             0-59

 Second                             Ss                             0-59

 Millisecond                        Ms                             0-999

See also
Objects overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.79 -->

Configuration Manager Bit Field
Properties
Article • 10/10/2022

Some Configuration Manager object properties are implemented as bit fields, where
individual binary bits of an integer (usually a uint32 data type) are used as Boolean
flags to store information. These properties can be difficult to interpret at the user
interface because the bit field is often displayed as a decimal number.

For example, the Security User Class Permissions object ( SMS_UserClassPermissions )
contains an integer property called ClassPermissions , which is defined as an int32 data
type with the following bit flags:

                                                                           ﾉ   Expand table

 Bit              Value

 0                READ

 1                MODIFY

 2                DELETE

 3                DISTRIBUTE

 4                CREATE_CHILD

 5                REMOTE_CONTROL

 6                ADVERTISE

 7                MODIFY_RESOURCE

 8                ADMINISTER

 9                DELETE_RESOURCE

 10               CREATE

 11               VIEW_COLL_FILE

 12               READ_RESOURCE

 13               DELEGATE

 14               METER

<!-- p.80 -->

 Bit             Value

 15              MANAGESQLCOMMAND

 16              MANAGESTATUSFILTER

A typical value of this bit field might be 10100000111. Bit 0 is the least significant bit (on
the right) and the other bits are counted right to left. Therefore, in this example, the
available class permissions include READ, MODIFY, DELETE, ADMINISTER, and CREATE,
corresponding to bit fields 0, 1, 2, 8, and 10, respectively.

The difficulty arises when the binary number 10100000111 appears as the decimal
number 1287 in a Configuration Manager console display and in how you interpret the
bits. The solution is to open the Windows Calculator application (Calc.exe, in the
Accessories group). Use the Scientific view, set the calculator for decimal mode, and
enter 1287. Use the radio buttons of the calculator to convert to a binary display. The
binary bit field 10100000111 appears. You can read the selected bit flags from this
display.

  ７ Note

  In a typical bit field property, many of the bits are unused and have no defined
  meaning.

See Also
Configuration Manager Association Classes
Configuration Manager Date and Time Formats
Configuration Manager Embedded Objects
Configuration Manager Extended WMI Query Language
Objects overview Configuration Manager Lazy Properties
About errors Configuration Manager Object Security
Configuration Manager Special Queries

Feedback
Was this page helpful?      Yes    No

Provide product feedback
