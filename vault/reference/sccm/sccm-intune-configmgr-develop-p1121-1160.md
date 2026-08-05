---
title: "Configuration Manager SDK documentation — pages 1121-1160"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p1121-1160
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p1121-1160
family: sccm
documentKind: "doc"
abstract: "How to Add an Operating System Install Package in Configuration Manager Article • 10/04/2022 You add an operating system install package to Configuration Manager by creating and populating an instance of SMS_OperatingSystemInstallPackage. To add an operating system install packa"
---

# Configuration Manager SDK documentation — pages 1121-1160

<!-- p.1121 -->

How to Add an Operating System Install
Package in Configuration Manager
Article • 10/04/2022

You add an operating system install package to Configuration Manager by creating and
populating an instance of SMS_OperatingSystemInstallPackage.

To add an operating system install package
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Create an instance of SMS_OperatingSystemInstallPackage.

   3. Set at least the Name, PkgSourceFlag, and PkgSourcePath properties.

   4. Commit the changes.

Example
The following example method adds an operating system install package.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub AddOSInstallPackage(connection, name, description, path)

         Dim osInstallPackage

      Set osInstallPackage =
  connection.Get("SMS_OperatingSystemInstallPackage").SpawnInstance_()
      ' Populate the new package properties.
      osInstallPackage.Name = name
      osInstallPackage.Description = description

         osInstallPackage.PkgSourceFlag=2
         osInstallPackage.PkgSourcePath = path

         ' Write the package.
         osInstallPackage.Put_

  End Sub

<!-- p.1122 -->

  c#

  public void AddOSInstallPackage(
      WqlConnectionManager connection,
      string name,
      string description,
      string path)
  {
      try
      {
          // Create new operating system image package object.
          IResultObject osInstallPackage =
  connection.CreateInstance("SMS_OperatingSystemInstallPackage");

          // Populate operating system package properties.
          osInstallPackage["Name"].StringValue = name;
          osInstallPackage["Description"].StringValue = description;
          osInstallPackage["PkgSourceFlag"].IntegerValue =
  (int)PackageSourceFlag.StorageDirect;
          osInstallPackage["PkgSourcePath"].StringValue = path;

              // Save operating system package.
              osInstallPackage.Put();
        }
        catch (SmsException e)
        {
            Console.WriteLine();
            Console.WriteLine("Failed to create package. Error: " + e.Message);
            throw;
        }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter      Type                        Description

 connection     - Managed:                  A valid connection to the SMS Provider.
                 WqlConnectionManager
                - VBScript: SWbemServices

 name           - Managed: String           Name for the new operating system image
                - VBScript: String          package.

 description    - Managed: String           Description for the operating system image
                - VBScript: String          package.

 path           - Managed: Integer          Universal Naming Convention (UNC) path to the
                - VBScript: Integer         image Windows Image (WIM) file.

<!-- p.1123 -->

Compiling the Code
The C# example has the following compilation requirements:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
How to Assign a Package to a Distribution Point
About image management

Feedback
Was this page helpful?    Yes    No

<!-- p.1124 -->

Provide product feedback

<!-- p.1125 -->

How to Clear a PXE Advertisement For a
Configuration Manager Collection
Article • 10/04/2022

To clear a PXE advertisement for a Configuration Manager collection, you call the
ClearLastNBSAdvForCollection Method in Class SMS_Collection method.

Clearing a PXE advertisement forces the PXE server to re-evaluate the mandatory
advertisement that a PXE device must execute on the next PXE boot. It is most often
used when the last advertisement that was executed failed or when the advertisement
must be re-run. For information about clearing the PXE advertisement for a resource,
see How to Clear a PXE Advertisement for a Configuration Manager Resource.

To clear a PXE advertisement for a collection
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get the SMS_Collection object for the collection you want to clear the PXE
        advertisement for.

   3. Call the ClearLastNBSAdvForCollection method to clear the PXE advertisement for
        the collection.

Example
The following example clears the PXE advertisement for the collection that is identified
by the collectionID parameter.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ClearPxeAdvertisementCollection (connection, collectionID)

         On Error Resume Next
         Dim collection

      ' Get the collection.
      Set collection = connection.Get("SMS_Collection.CollectionID='" &
  collectionID & "'")

<!-- p.1126 -->

        result = collection.ClearLastNBSAdvForCollection

      if Err.number <> 0 Then
          WScript.Echo "Failed to clear PXE advertisement for collection: " &
  collectionID
          Exit Sub
      End If

  End Sub

  c#

  public void ClearPxeAdvertisementCollection(WqlConnectionManager connection,
  string collectionID)
  {
      try
      {
          // Get the collection.
          IResultObject collection =
  connection.GetInstance(@"SMS_Collection.CollectionID='" + collectionID +
  "'");

              Dictionary<string, object> inParams = new Dictionary<string, object>
  ();
          IResultObject outParams =
  collection.ExecuteMethod("ClearLastNBSAdvForCollection", inParams);

          if (outParams == null || outParams["StatusCode"].IntegerValue != 0)
          {
              Console.WriteLine
                  ("Failed to clear PXE advertisement for collection " +
  collection["Name"].ToString());
              return;
          }
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to clear PXE advertisement " + e.Message);
      }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter       Type                        Description

 connection      - Managed:                  A valid connection to the SMS Provider.
                  WqlConnectionManager
                 - VBScript: SWbemServices

<!-- p.1127 -->

 Parameter      Type                    Description

 collectionID   - Managed: String       The resource identifier. You can obtain this from the
                - VBScript: String      SMS_Collection class CollectionID property.

Compiling the Code
The C# example has the following compilation requirements:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
How to Clear a PXE Advertisement for a Configuration Manager Resource
About image management

<!-- p.1128 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1129 -->

How to Clear a PXE Advertisement for a
Configuration Manager Resource
Article • 10/04/2022

To clear a PXE advertisement for a Configuration Manager resource, you call the
SMS_Collection object ClearLastNBSAdvForMachines method.

Clearing PXE advertisement is used to re-advertise a mandatory advertisement that is
enabled for a PXE device or assigned to a collection. For information about clearing the
PXE advertisement for a collection, see How to Clear a PXE Advertisement For a
Configuration Manager Collection.

Clearing a PXE advertisement forces the PXE server to re-evaluate the mandatory
advertisement that a PXE device must execute on the next PXE boot. It is most often
used when the last advertisement that was executed failed or when the advertisement
must be re-run.

To clear a PXE advertisement for a resource
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Create the ClearLastNBSAdvForMachines method resource identifier array for the
        method parameters.

   3. Call the ClearLastNBSAdvForMachines method to clear the PXE advertisement for
        the resource.

Example
The following example clears the PXE advertisement for the resource identified by the
resourceID parameter.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ClearPxeAdvertisementResource(connection,resourceID)

         On Error Resume Next

<!-- p.1130 -->

     Dim resources
     Dim InParams

     ' Set up the Resource array parameter.
     resources = Array(1)
     resources(0) = resourceID

    Set InParams =
connection.Get("SMS_Collection").Methods_("ClearLastNBSAdvForMachines").InPa
rameters.SpawnInstance_
    InParams.ResourceIDs = resources

    connection.ExecMethod "SMS_Collection","ClearLastNBSAdvForMachines",
InParams

    if Err.number <> 0 Then
        WScript.Echo "Failed to clear PXE advertisement for resource: " &
resourceID
        Exit Sub
    End If

End Sub

c#

public void ClearPxeAdvertisementResource(WqlConnectionManager connection,
int resourceID)
{
    try
    {
        List<int> resourceIDs = new List<int>();
        Dictionary<string, object> inParams = new Dictionary<string, object>
();

          resourceIDs.Add(resourceID);
          inParams.Add("ResourceIDs", resourceIDs.ToArray());

        IResultObject outParams =
connection.ExecuteMethod("SMS_Collection","ClearLastNBSAdvForMachines",inPar
ams);

        if (outParams == null || outParams["StatusCode"].IntegerValue != 0)
        {
             Console.WriteLine
                 ("Failed to clear PXE advertisement for resource " +
resourceID);
             return;
        }
    }
    catch (SmsException e)
    {
        Console.WriteLine("Failed to PXE advertisement " + e.Message);

<!-- p.1131 -->

      }
  }

The example method has the following parameters:

                                                                              ﾉ     Expand table

 Parameter    Type                        Description

 connection   - Managed:                  A valid connection to the SMS Provider.
              WqlConnectionManager
              - VBScript: SWbemServices

 resourceID   - Managed: Integer          The resource identifier. You can obtain this from the
              - VBScript: Integer         SMS_Resource class ResourceId property.

Compiling the Code
The C# example has the following compilation requirements:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

<!-- p.1132 -->

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
How to Clear a PXE Advertisement For a Configuration Manager Collection
About image management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1133 -->

About Operating System Deployment
Driver Management
Article • 10/04/2022

In Configuration Manager, the driver catalog helps manage the cost and complexity of
deploying an operating system in an environment that contains different types of
computers and devices. By storing device drivers in the driver catalog and not with each
individual operating system image, the number of operating system images that is
needed is greatly reduced. For more information about the driver catalog, see Manage
drivers.

  ７ Note

  Before a driver can be used, it must be added to a driver package. For more
  information, see How to Create a Driver Package for a Windows Driver in
  Configuration Manager.

Driver Catalog Management
With the Configuration Manager Operating System Deployment server Windows
Management Instrumentation (WMI) classes you can manage the following:

      Driver import

      Driver packages

      Boot images

      Supported platforms

Driver Import
Using the SMS_Driver import methods, you can import the Windows drivers described
by .inf and Txtsetup.oem files into the driver catalog. For more information, see How to
Import a Windows Driver Described by an INF File into Configuration Manager and How
to Import a Windows Driver Described by an OEM File into Configuration Manager.

Before a driver can be used, it must be enabled. For more information, see How to
Enable or Disable a Windows Driver in Configuration Manager.

<!-- p.1134 -->

Driver Packages
Driver packages contain one or more Windows drivers. A driver package is an
SMS_DriverPackage object and is distributed in the same way as an SMS_Package

package. They both derive from SMS_PackageBaseClass.

For more information about creating a driver package, see How to Create a Driver
Package for a Windows Driver in Configuration Manager.

Boot Images
Windows device drivers that have been imported into the driver catalog can be added
to one or more boot images. Boot images are stored in SMS_BootImagePackage
objects. In an SMS_BootImagePackage object, Windows drivers are kept in an array of
referenced drivers. For more information, see How to add a Windows Driver to a
Configuration Manager Boot Image Package

Supported Platforms
Windows drivers can be configured to support specific platforms. The supported
platforms are stored in the driver package XML. For more information, see How to
Specify The Supported Platforms for a Driver.

Driver Categories
You can associate categories with Windows device drivers. For more information, see
How to Add a Category to a Windows Driver

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1135 -->

How to Import a Windows Driver
Described by an INF File into
Configuration Manager
Article • 10/04/2022

You can import a Windows driver that is described by an information (.inf) file, in
Configuration Manager, by using the CreateFromINF Method in Class SMS_Driver.

To import a Windows driver
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Call the CreateFromINF Method in Class SMS_Driver to get the initial SMS_Driver
      Server WMI Class management base object.

   3. Create an instance of SMS_Driver by using the management base object.

   4. Populate the SMS_Driver object.

   5. Commit the SMS_Driver object.

Example
The following example method creates an SMS_Driver object for a Windows driver by
using the supplied path and file name. The example also enables the driver by setting
the value of the IsEnabled property to true . The helper function GetDriverName is used
to get the name of the driver from the driver package XML.

  ７ Note

  The path parameter must be supplied as a Universal Naming Convention (UNC)
  network path, for example, \\localhost\Drivers\ATIVideo\.

In the example, the LocaleID property is hard-coded to English (U.S.). If you need the
locale for non-U.S. installations, you can get it from the SMS_Identification Server WMI
Class LocaleID property.

<!-- p.1136 -->

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ImportINFDriver(connection, path, name)

        Dim driverClass
        Dim inParams
        Dim outParams

        On Error Resume Next

        ' Obtain an instance of the class
        ' using a key property value.

        Set driverClass = connection.Get("SMS_Driver")

        ' Obtain an InParameters object specific
        ' to the method.
        Set inParams = driverClass.Methods_("CreateFromINF"). _
            inParameters.SpawnInstance_()

        ' Add the input parameters.
        inParams.Properties_.Item("DriverPath") = path
        inParams.Properties_.Item("INFFile") = name

      ' Call the method.
      ' The OutParameters object in outParams
      ' is created by the provider.
      Set outParams = connection.ExecMethod("SMS_Driver", "CreateFromINF",
  inParams)

     If Err <> 0 Then
           Wscript.Echo "Failed to add to the driver catalog: " + path + "\" +
  name
           Exit Sub
       End If

        outParams.Driver.IsEnabled =   True

      Dim LocalizedSettings(0)
      Set LocalizedSettings(0) =
  connection.Get("SMS_CI_LocalizedProperties").SpawnInstance_()
      LocalizedSettings(0).Properties_.item("LocaleID") = 1033
      LocalizedSettings(0).Properties_.item("DisplayName") = _
              GetDriverName(outParams.Driver.SDMPackageXML, "//DisplayName",
  "Text")

        LocalizedSettings(0).Properties_.item("Description") = ""
        outParams.Driver.LocalizedInformation = LocalizedSettings

        ' Save the driver.
        outParams.Driver.Put_

<!-- p.1137 -->

End Sub

Function GetDriverName(xmlContent, nodeName, attributeName)
    ' Load the XML Document
    Dim attrValue
    Dim XMLDoc
    Dim objNode
    Dim displayNameNode

     attrValue = ""
     Set XMLDoc = CreateObject("Microsoft.XMLDOM")
     XMLDoc.async = False
     XMLDoc.loadXML(xmlContent)

    'Check for a successful load of the XML Document.
    If xmlDoc.parseError.errorCode <> 0 Then
        WScript.Echo vbcrlf & "Error loading XML Document. Error Code : 0x"
& hex(xmldoc.parseerror.errorcode)
        WScript.Echo "Reason: " & xmldoc.parseerror.reason
        WScript.Echo "Parse Error line " & xmldoc.parseError.line & ",
character " & _
                      xmldoc.parseError.linePos & vbCrLf &
xmldoc.parseError.srcText

         GetXMLAttributeValue = ""
     Else
         ' Select the node
         Set objNode = xmlDoc.SelectSingleNode(nodeName)

        If Not objNode Is Nothing Then
             ' Found the element, now just pick up the Text attribute value
             Set displayNameNode =
objNode.attributes.getNamedItem(attributeName)
             If Not displayNameNode Is Nothing Then
                attrValue = displayNameNode.value
             Else
                WScript.Echo "Attribute not found"
             End If
        Else
             WScript.Echo "Failed to locate " & nodeName & " element."
        End If
    End If

    ' Save the results
    GetDriverName = attrValue
End Function

c#

public void ImportInfDriver(
    WqlConnectionManager connection,
    string path,

<!-- p.1138 -->

      string name)
{
      try
      {
            Dictionary<string, object> inParams = new Dictionary<string, object>
();

            // Set up parameters for the path and file name.
            inParams.Add("DriverPath", path);
            inParams.Add("INFFile", name);

        // Import the INF file.
        IResultObject result = connection.ExecuteMethod("SMS_Driver",
"CreateFromINF", inParams);

        // Create the SMS_Driver driver instance from the management base
object returned in result["Driver"].
        IResultObject driver =
connection.CreateInstance(result["Driver"].ObjectValue);

            // Enable the driver.
            driver["IsEnabled"].BooleanValue = true;

        List<IResultObject> driverInformationList =
driver.GetArrayItems("LocalizedInformation");

        // Set up the display name and other information.
        IResultObject driverInfo =
connection.CreateEmbeddedObjectInstance("SMS_CI_LocalizedProperties");
        driverInfo["DisplayName"].StringValue = GetDriverName(driver);
        driverInfo["LocaleID"].IntegerValue = 1033;
        driverInfo["Description"].StringValue = "";

            driverInformationList.Add(driverInfo);

            driver.SetArrayItems("LocalizedInformation", driverInformationList);

            // Commit the SMS_Driver object.
            driver.Put();
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to import driver: " + e.Message);
          throw;
      }
}

public string GetDriverName(IResultObject driver)
{
    // Extract
    XmlDocument sdmpackage = new XmlDocument();

      sdmpackage.LoadXml(driver.Properties["SDMPackageXML"].StringValue);

      // Iterate over all the <DisplayName/> tags.

<!-- p.1139 -->

      foreach (XmlNode displayName in
  sdmpackage.GetElementsByTagName("DisplayName"))
      {
      // Grab the first one with a Text attribute not equal to null.
          if (displayName != null && displayName.Attributes["Text"] != null
              && !string.IsNullOrEmpty(displayName.Attributes["Text"].Value))
          {
                  // Return the DisplayName text.
                  return displayName.Attributes["Text"].Value;
          }
      }
      // Default the driverName to the UniqueID.
      return driver["CI_UniqueID"].StringValue;
   }

The example method has the following parameters:

                                                                             ﾉ    Expand table

 Parameter    Type                   Description

 connection   - Managed:             A valid connection to the SMS Provider.
              WqlConnectionManager
              - VBScript:
              SWbemServices

 path         - Managed: String      A valid UNC network path to the folder that contains
              - VBScript: String     the driver contents. For example,
                                     \\Servers\Driver\VideoDriver.

 name         - Managed: String      The name of the .inf file. For example, ATI.inf.
              - VBScript: String

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

<!-- p.1140 -->

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
CreateFromINF Method in Class SMS_Driver
SMS_Driver Server WMI Class
How to Specify The Supported Platforms for a Driver

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1141 -->

How to Import a Windows Driver
Described by a Txtsetup.oem File into
Configuration Manager
Article • 10/04/2022

You can import a Windows driver that is described by a Txtsetup.oem file, in
Configuration Manager, by using the CreateFromOEM Method in Class SMS_Driver.
Configuration Manager can automatically create definitions for most drivers from just an
.inf file. However, when installing mass-storage drivers on pre-Windows Vista operating
systems, Configuration Manager also must have some information that is contained in
the Txtsetup.oem file. To facilitate this, CreateFromOEM creates SMS_Driver Server WMI
Class objects for each .inf file that is referenced in the Txtsetup.oem file. You then have
the opportunity to customize the driver properties before saving them.

  ７ Note

  If a driver manufacturer has provided a Txtsetup.oem file, you should import the
  driver by using this procedure instead of the .inf files if you plan to deploy
  Windows 2000, Windows XP, or Windows Server 2003.

To import a Windows driver
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Call the SMS_Driver class CreateFromOEM method to get a collection of
      management base objects.

   3. For the management base objects create an SMS_Driver object for each driver.

   4. Populate the SMS_Driver object.

   5. Commit the SMS_Driver object.

Example
The following example method creates an SMS_Driver object for a Windows driver by
using the supplied path and Txtsetup.oem file name. The example also enables the

<!-- p.1142 -->

driver by setting the value of the IsEnabled property to true . The helper function
GetDriverName is used to get the name of the driver from the driver package XML.

  ７ Note

  The path parameter must be supplied as a Universal Naming Convention (UNC)
  network path, for example, \\localhost\Drivers\VMSCSI\.

In the example, the LocaleID property is hard-coded to English (U.S.). If you need the
locale for non-U.S. installations, you can get it from the SMS_Identification Server WMI
Class LocaleID property.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ImportOemDriver(connection,path,name)

        Dim inParams
        Dim outParams
        Dim driver
        Dim driverClass

        On Error Resume Next

        Set driverClass = connection.Get("SMS_Driver")

      Set inParams =
  driverClass.Methods_("CreateFromOEM").inParameters.SpawnInstance_()

        ' Set the driver path and INF file.
        inParams.Properties_.item("DriverPath") = path
        inParams.Properties_.item("OEMFile") = name

        ' Execute the method.
            Set outParams = driverClass.ExecMethod_("CreateFromOEM", inParams)

        If Err <> 0 Then
            Wscript.Echo "Failed to import driver: " + path +"\" + name
            Exit Sub
        End If

        For Each driver In outParams.Drivers
            ' Set driver name and enable the driver.
            Dim LocalizedSettings
            LocalizedSettings = array(0)

            Set   LocalizedSettings(0) =

<!-- p.1143 -->

connection.Get("SMS_CI_LocalizedProperties").SpawnInstance_()
        LocalizedSettings(0).Properties_.item("LocaleID") = 1033
        LocalizedSettings(0).Properties_.item("DisplayName") = _
               GetDriverName(driver.Properties_.item("SDMPackageXML"),
"//DisplayName", "Text")
        LocalizedSettings(0).Properties_.item("Description") = ""
        driver.Properties_.item("LocalizedInformation") = LocalizedSettings
        driver.Properties_.item("IsEnabled") = true
        driver.Put_
    Next
End Sub

Function GetDriverName(xmlContent, nodeName, attributeName)
    ' Load the XML Document
    Dim attrValue
    Dim XMLDoc
    Dim objNode
    Dim displayNameNode

    attrValue = ""
    Set XMLDoc = CreateObject("Microsoft.XMLDOM")
    XMLDoc.async = False
    XMLDoc.loadXML(xmlContent)

    'Check for a successful load of the XML Document.
    If xmlDoc.parseError.errorCode <> 0 Then
        WScript.Echo vbcrlf & "Error loading XML Document. Error Code : 0x"
& hex(xmldoc.parseerror.errorcode)
        WScript.Echo "Reason: " & xmldoc.parseerror.reason
        WScript.Echo "Parse Error line " & xmldoc.parseError.line & ",
character " & _
                      xmldoc.parseError.linePos & vbCrLf &
xmldoc.parseError.srcText

        GetXMLAttributeValue = ""
    Else
        ' Select the node
        Set objNode = xmlDoc.SelectSingleNode(nodeName)

        If Not objNode Is Nothing Then
             ' Found the element, now just pick up the Text attribute value
             Set displayNameNode =
objNode.attributes.getNamedItem(attributeName)
             If Not displayNameNode Is Nothing Then
                attrValue = displayNameNode.value
             Else
                WScript.Echo "Attribute not found"
             End If
        Else
             WScript.Echo "Failed to locate " & nodeName & " element."
        End If
    End If

    ' Save the results

<!-- p.1144 -->

    GetDriverName = attrValue
End Function

c#

public void ImportOemDriver(
WqlConnectionManager connection,
string path,
string name)
{
    try
    {
        Dictionary<string, object> inParams = new Dictionary<string, object>
();

        // Set up parameters for the path and file name.
        inParams.Add("DriverPath", path);
        inParams.Add("OEMFile", name);

        // Import the INF file.
        IResultObject outParams = connection.ExecuteMethod("SMS_Driver",
"CreateFromOEM", inParams);

        // Create the driver instance from the management base object
returned in result["Drivers"].

        foreach (object obj in outParams["Drivers"].ObjectArrayValue)
        {
            IResultObject driver = connection.CreateInstance(obj);
            driver["IsEnabled"].BooleanValue = true;

            List<IResultObject> driverInformationList =
driver.GetArrayItems("LocalizedInformation");

            // Set up the display name and other information.
            IResultObject driverInfo =
connection.CreateEmbeddedObjectInstance("SMS_CI_LocalizedProperties");
            driverInfo["DisplayName"].StringValue = GetDriverName(driver);
            driverInfo["LocaleID"].IntegerValue = 1033;
            driverInfo["Description"].StringValue = "";

            driverInformationList.Add(driverInfo);

            driver.SetArrayItems("LocalizedInformation",
driverInformationList);

            // Commit the SMS_Driver object.
            driver.Put();
         }
     }
     catch (SmsException e)
     {
         Console.WriteLine("Failed to import driver: " + e.Message);

<!-- p.1145 -->

              throw;
      }
  }
  public string GetDriverName(IResultObject driver)
  {
      // Extract
      XmlDocument sdmpackage = new XmlDocument();

        sdmpackage.LoadXml(driver.Properties["SDMPackageXML"].StringValue);

      // Iterate over all the <DisplayName/> tags.
      foreach (XmlNode displayName in
  sdmpackage.GetElementsByTagName("DisplayName"))
      {
      // Grab the first one with a Text attribute not equal to null.
          if (displayName != null && displayName.Attributes["Text"] != null
              && !string.IsNullOrEmpty(displayName.Attributes["Text"].Value))
          {
                  // Return the DisplayName text.
                  return displayName.Attributes["Text"].Value;
          }
      }
      // Default the driverName to the UniqueID.
      return driver["CI_UniqueID"].StringValue;
   }

The example method has the following parameters:

                                                                            ﾉ    Expand table

 Parameter      Type                   Description

 Connection     - Managed:             A valid connection to the SMS Provider.
                WqlConnectionManager
                - VBScript:
                SWbemServices

 path           - Managed: String      A valid UNC network path to the folder that contains
                - VBScript: String     the driver contents. For example,
                                       \\Servers\Driver\VideoDriver.

 name           - Managed: String      The name of the Txtsetup.oem file. For example, you
                - VBScript: String     might have \\server\drivers\Video for path and
                                       Txtsetup.oem for name .

Compiling the Code
This C# example requires:

<!-- p.1146 -->

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See also
How to specify the supported platforms for a driver

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1147 -->

How to Create a Driver Package for a
Windows Driver in Configuration
Manager
Article • 10/04/2022

You create a package for an operating system deployment driver, in Configuration
Manager, by creating a SMS_DriverPackage Server WMI Class object. To add a driver to
the package, you call the AddDriverContent Method in Class SMS_DriverPackage.

Driver packages are used to store the content associated with drivers. When creating a
driver package, the source location should initially be an empty share that the SMS
Provider has read and write access to. When a driver is added to a driver package, using
AddDriverContent , the SMS Provider will copy the content from the driver source

location to a subdirectory in the driver package share.

It is necessary to add the content that is associated with a driver to a driver package and
assign it to a distribution point before the client can use it. You get the driver content
from the SMS_CIToContent Server WMI Class object where the CI_ID property matches
the driver identifier.

  ７ Note

  It is possible for multiple drivers to share the same content. This typically happens
  when there are multiple .inf files in the same directory.

AddDriverContent can be used to add multiple drivers to a package simultaneously. To
do this, add multiple content IDs. The bRefreshDPs parameter should be set to false if
another call will be made. This ensures the package is only updated on the distribution
point once.

When you call AddDriverContent , you specify a set of package source locations. Typically
this is the SMS_Driver Server WMI Class object ContentSourcePath property, but it can
be overridden if the provider does not have access to the original source location.

To create a driver package and add driver content
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

<!-- p.1148 -->

   2. Create an SMS_DriverPackage object.

   3. Set the PkgSourceFlag property of the SMS_DriverPackage object to 2 (Storage
        Direct).

   4. Commit the SMS_DriverPackage object.

   5. Get the SMS_DriverPackage object.

   6. Put the list of drivers that you want to add to the package in the AddDriverContent
        method ContentIDs in parameter.

   7. Put the list of driver content source paths in the AddDriverContent method
        ContentSourcePath in parameter.

   8. Call the AddDriverContent method.

   9. Call the RefreshPkgSource Method in Class SMS_DriverPackage to complete the
        operation.

 10. Assign the driver package to a distribution point. For more information, see How
        to Assign a Package to a Distribution Point.

Example
The following example method creates a package for a supplied driver identifier,
represented by the CI_ID property of the SMS_Driver Server WMI Class object. The
method also takes a new package name, description, and package source path as
parameters.

  ７ Note

  The packageSourcePath parameter must be supplied as a Universal Naming
  Convention (UNC) network path, for example, \\localhost\Drivers\ATIVideo\.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub CreateDriverPackage(connection, driverId, newPackageName,
  newPackageDescription, newPackageSourcePath)

         Dim newPackage

<!-- p.1149 -->

    Dim driver
    Dim packageSources
    Dim refreshDPs
    Dim content
    Dim path
    Dim contentIds
    Dim index
    Dim item

    ' Create the new driver package object.
    Set newPackage = connection.Get("SMS_DriverPackage").SpawnInstance_

    ' Populate the new package properties.
    newPackage.Name = newPackageName
    newPackage.Description = newPackageDescription
    newPackage.PkgSourceFlag = 2 ' Storage direct
    newPackage.PkgSourcePath = newPackageSourcePath

    ' Save the package.
    path=newPackage.Put_

    ' Get the newly created package (Do this to call AddDriverContent).
    Set newPackage=connection.Get(path)

    ' Get the driver
    Set driver = connection.Get("SMS_Driver.CI_ID=" & driverId )

    ' Get the driver content.
    Set content = connection.ExecQuery("Select * from SMS_CIToContent where
CI_ID=" & driverId)

    If content.Count = 0 Then
        Wscript.Echo "No content found"
        Exit Sub
    End If

    ' Create Array to hold driver content identifiers.
    contentIds = Array()
    ReDim contentIds(content.Count-1)
    index = 0

    For Each item In content
        contentIds(index) = item.ContentID
        index = index+1
    Next

    ' Create sources path Array.
    packageSources = Array(driver.ContentSourcePath)
    refreshDPs = False

    ' Add the driver content.
    Call newPackage.AddDriverContent(contentIds,packageSources,refreshDPs)
    wscript.echo "Done"

End Sub

<!-- p.1150 -->

c#

public void CreateDriverPackage(
    WqlConnectionManager connection,
    int driverId,
    string newPackageName,
    string newPackageDescription,
    string newPackageSourcePath)
{
    try
    {
        if (Directory.Exists(newPackageSourcePath) == false)
        {
            throw new DirectoryNotFoundException("Package source path does
not exist");
        }

        // Create new package object.
        IResultObject newPackage =
connection.CreateInstance("SMS_DriverPackage");

        IResultObject driver = connection.GetInstance("SMS_Driver.CI_ID=" +
driverId);

        newPackage["Name"].StringValue = newPackageName;
        newPackage["Description"].StringValue = newPackageDescription;
        newPackage["PkgSourceFlag"].IntegerValue =
(int)PackageSourceFlag.StorageDirect;
        newPackage["PkgSourcePath"].StringValue = newPackageSourcePath;

       // Save new package and new package properties.
       newPackage.Put();

       newPackage.Get();

        // Get the content identifier.
        List<int> contentIDs = new List<int>();
        IResultObject content =
connection.QueryProcessor.ExecuteQuery("Select * from SMS_CIToContent where
CI_ID=" + driverId);

       foreach (IResultObject ro in content)
       {
           contentIDs.Add(ro["ContentID"].IntegerValue);
       }

       // Get the package source.
       List<string> packageSources = new List<string>();
       packageSources.Add(driver["ContentSourcePath"].StringValue);

       Dictionary<string, Object> inParams = new Dictionary<string, object>
();

<!-- p.1151 -->

              inParams.Add("bRefreshDPs", true);
              inParams.Add("ContentIDs", contentIDs.ToArray());
              inParams.Add("ContentSourcePath", packageSources.ToArray());

          newPackage.ExecuteMethod("AddDriverContent", inParams);
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to create package. Error: " + ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                         ﾉ   Expand table

 Parameter               Type                        Description

 connection              - Managed:                  A valid connection to the SMS
                         WqlConnectionManager        Provider.
                         - VBScript: SWbemServices

 driverId                - Managed: Integer          The driver identifier
                         - VBScript: Integer         ( SMS_Driver.CI_ID ).

 newPackageName          - Managed: String           The name for the package.
                         - VBScript: String

 newPackageDescription   - Managed: String           A description for the new package.
                         - VBScript: String

 newPackageSourcePath    - Managed: String           A valid UNC network path to the
                         - VBScript: String          driver.

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

<!-- p.1152 -->

System.IO

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
SMS_Driver Server WMI Class
AddDriverContent Method in Class SMS_DriverPackage

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1153 -->

How to Add a Windows Driver to a
Configuration Manager Boot Image
Package
Article • 10/04/2022

In Configuration Manager, you add a Windows driver to an operating system
deployment boot image package by adding a reference to the required driver in the
SMS_BootImagePackage Server WMI Class ReferencedDrivers array property.

  ７ Note

  The ReferencedDrivers property is an array of an embedded SMS_Driver_Details
  object, and you can add more than one driver to the package. The objects in the
  array are added to the boot image package each time it is updated on the
  distribution point.

The location of the driver content is usually obtained from the SMS_Driver Server WMI
Class object ContentSourcePath property, but this can be overridden if the original driver
location is not available.

It might be necessary to add network or storage drivers to a boot image package so
that a task sequence can access the network and disk resources while in WinPE.

Drivers are added to the image only when the boot image is refreshed by calling the
RefreshPkgSource Method in Class SMS_BootImagePackage method.

Drivers are added to the image by using Windows Package Manager.

To add a Windows driver to a boot image package
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Get the SMS_BootImagePackage object for the boot image package that you want
      to add the driver to.

   3. Create and populate an embedded SMS_Driver_Details object to contain the
      driver details.

<!-- p.1154 -->

   4. Add the SMS_Driver_Details object to the ReferencedDrivers array property of the
        SMS_BootImagePackage object.

   5. Commit the SMS_BootImagePackage object changes.

Example
The following example method adds a Windows driver to a boot image package. The
package is identified by its PackageID property, and the driver is identified by its CI_ID
property.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub AddDriverToBootImagePackage(connection, driverId,packageId)

         Dim bootImagePackage
         Dim driver
         Dim referencedDrivers
         Dim driverDetails

      ' Get the boot image package and referenced drivers.
      Set bootImagePackage = connection.Get("SMS_BootImagePackage.PackageID='"
  & packageId &"'" )
      referencedDrivers = bootImagePackage.ReferencedDrivers

         ' Get the driver.
         Set driver = connection.Get("SMS_Driver.CI_ID=" & driverId )

         ' Create and populate the driver details.
         Set driverDetails = connection.Get("SMS_Driver_Details").SpawnInstance_
         driverDetails.ID=driverId
         driverDetails.SourcePath=driver.ContentSourcePath

         ' Add the driver details.
         ReDim Preserve referencedDrivers (Ubound (referencedDrivers)+1)
         Set referencedDrivers(Ubound(referencedDrivers))=driverDetails
         bootImagePackage.ReferencedDrivers=referencedDrivers

         bootImagePackage.Put_
         bootImagePackage.RefreshPkgSource

  End Sub

  c#

<!-- p.1155 -->

  public void AddDriverToBootImagePackage(
      WqlConnectionManager connection,
      int driverId,
      string packageId)
  {
      try
      {
          // Get the boot image package.
          IResultObject bootImagePackage =
  connection.GetInstance(@"SMS_BootImagePackage.packageId='" + packageId +
  "'");

          // Get the driver.
          IResultObject driver = connection.GetInstance("SMS_Driver.CI_ID=" +
  driverId);

          // Get the drivers that are referenced by the package.
          List<IResultObject> referencedDrivers =
  bootImagePackage.GetArrayItems("ReferencedDrivers");

          // Create and populate an embedded SMS_Driver_Details. This is added
  to the ReferencedDrivers array.
          IResultObject driverDetails =
  connection.CreateEmbeddedObjectInstance("SMS_Driver_Details");

          driverDetails["ID"].IntegerValue = driverId;
          driverDetails["SourcePath"].StringValue =
  driver["ContentSourcePath"].StringValue;

          // Add the driver details to the array.
          referencedDrivers.Add(driverDetails);

          // Add the array to the boot image package.
          bootImagePackage.SetArrayItems("ReferencedDrivers",
  referencedDrivers);

          // Commit the changes.
          bootImagePackage.Put();
          bootImagePackage.ExecuteMethod("RefreshPkgSource", null);
      }
      catch (SmsException e)
      {
          Console.WriteLine(e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                   ﾉ   Expand table

<!-- p.1156 -->

 Parameter    Type                            Description

 Connection   -                               A valid connection to the SMS Provider.
              Managed: WqlConnectionManager
              - VBScript: SWbemServices

 driverID     - Managed: String               The Windows driver identifier available in
              - VBScript: String              SMS_Driver.CI_ID .

 PackageID    - Managed: String               The boot image package identifier available in
              - VBScript: String              SMS_BootImagePackage.PackageID .

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

<!-- p.1157 -->

See Also
About Operating System Deployment Driver Management
How to Remove a Windows Driver from a Boot Image Package

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1158 -->

How to Remove a Windows Driver from
a Boot Image Package
Article • 10/04/2022

In Configuration Manager, you remove a Windows driver from an operating system
deployment boot image package by removing it from the ReferencedDrivers property
of the SMS_BootImagePackage Server WMI Class object.

  ７ Note

  The driver is not removed until the boot image package is refreshed and updated
  on the distribution points.

To remove a Windows driver from a boot image package
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Get the SMS_BootImagePackage object for the boot image package that contains
      the driver you want to remove.

   3. Remove the driver from the ReferencedDrivers property. The driver is identified by
      its configuration item identifier represented by the ID property of the
      SMS_Driver_Details Server WMI Class object. This identifier matches the CI_ID
      property of SMS_Driver .

   4. Commit the SMS_BootImagePackage object changes.

   5. Refresh the boot image package by calling RefreshPkgSource .

Example
The following example method removes the Windows driver from the boot image
package. The package is identified by its PackageID property and the driver is identified
by its CI_ID property.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

<!-- p.1159 -->

vbs

Sub RemoveDriverFromBootImagePackage(connection, driverId, packageId)
    Dim bootImagePackage
    Dim driver
    Dim driverDetails
    Dim newReferencedDrivers()
    Dim found
    Dim index

    ' Get the boot image package.
    Set bootImagePackage = connection.Get("SMS_BootImagePackage.PackageID='"
& packageId &"'" )

      found = False
      index=0

      ' Copy the contents and leave out the driver.
      For Each driver In bootImagePackage.ReferencedDrivers
          If driver.ID = driverID Then
               found=True
          Else
             Set newReferencedDrivers(index)=driver
             index = index + 1
          End If
      Next

    ' Update the referenced drivers.
    If found=True Then
        ReDim preserve
newReferencedDrivers(UBound(bootImagePackage.ReferencedDrivers)-1)
        bootImagePackage.ReferencedDrivers=newReferencedDrivers
        bootImagePackage.Put_
        bootImagePackage.RefreshPkgSource
   End If

End Sub

c#

public void RemoveDriverFromBootImagePackage(
    WqlConnectionManager connection,
    int driverId,
    string packageId)
{
    try
    {
        // Get the boot image package.
        IResultObject bootImagePackage =
connection.GetInstance(@"SMS_BootImagePackage.packageId='" + packageId +
"'");

          // Get the (SMS_Driver_Details) drivers referenced by the package.

<!-- p.1160 -->

          List<IResultObject> referencedDrivers =
  bootImagePackage.GetArrayItems("ReferencedDrivers");

          foreach (IResultObject ro in referencedDrivers)
          {
              if (ro["ID"].IntegerValue == driverId) // Remove the driver that
  matches driverId.
              {
                  referencedDrivers.Remove(ro);
                  break;
              }
          }

          bootImagePackage.SetArrayItems("ReferencedDrivers",
  referencedDrivers);

              // Commit the changes.
              bootImagePackage.Put();
              bootImagePackage.ExecuteMethod("RefreshPkgSource", null);
      }
      catch (SmsException e)
      {
          Console.WriteLine(e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                                 ﾉ    Expand table

 Parameter      Type                        Description

 Connection     - Managed:                  A valid connection to the SMS Provider.
                WqlConnectionManager
                - VBScript: SWbemServices

 driverID       - Managed: Integer          The Windows driver identifier available in
                - VBScript: Integer         SMS_Driver.CI_ID .

 PackageID      - Managed: String           The boot image package identifier available in
                - VBScript: String          SMS_BootImagePackage.PackageID .

Compiling the Code
This C# example requires:

Namespaces
