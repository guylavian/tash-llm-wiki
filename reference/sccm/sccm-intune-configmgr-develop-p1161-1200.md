---
title: "Configuration Manager SDK documentation — pages 1161-1200"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p1161-1200
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p1161-1200
family: sccm
documentKind: "doc"
abstract: "System System.Collections.Generic System.Text Microsoft.ConfigurationManagement.ManagementProvider Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine Assembly microsoft.configurationmanagement.managementprovider adminui.wqlqueryengine Robust Programming For more"
---

# Configuration Manager SDK documentation — pages 1161-1200

<!-- p.1161 -->

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
About Operating System Deployment Driver Management
How to Add a Windows Driver to a Configuration Manager Boot Image Package

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1162 -->

How to Enable or Disable a Windows
Driver in Configuration Manager
Article • 10/04/2022

You enable or disable a Windows driver in the operating system deployment driver
catalog, in Configuration Manager, by setting the IsEnabled property of the SMS_Driver
Server WMI Class object. A driver can be disabled to prevent it from being installed by
the Auto Apply Driver action in a task sequence.

To enable or disable a Windows driver
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get the SMS_Driver object for the driver you want to enable or disable.

   3. Set the IsEnabled property to true to enable the driver, or to false to disable the
        driver.

   4. Commit the SMS_Driver object changes.

Example
The following example method enables or disables a driver depending on the value of
the enableDriver parameter.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub EnableDriver(connection,driverID,vEnableDriver)

              ' Get the driver.
              Set driver = connection.Get("SMS_Driver.CI_ID=" & driverID)

              ' Set the flag.
              driver.IsEnabled=vEnableDriver

              ' Commit changes.
              driver.Put_

<!-- p.1163 -->

  End Sub

  c#

  public void EnableDriver(
      WqlConnectionManager connection,
      int driverID,
      bool enableDriver)
  {
      try
      {
          // Get the driver.
          IResultObject driver = connection.GetInstance("SMS_Driver.CI_ID=" +
  driverID);

              // Set the flag.
              driver["IsEnabled"].BooleanValue = enableDriver;

              // Commit the changes.
              driver.Put();
       }
       catch (SmsException e)
       {
           Console.WriteLine("Failed: " + e.Message);
           throw;
       }
  }

The example method has the following parameters:

                                                                               ﾉ   Expand table

 Parameter       Type                        Description

 connection      - Managed:                  A valid connection to the SMS Provider.
                  WqlConnectionManager
                 - VBScript: SWbemServices

 driverID        - Managed: Integer          The Windows driver identifier available in
                 - VBScript: Integer         SMS_Driver.CI_ID .

 enableDriver    - Managed: String           Flag to enable or disable the driver.
                 - VBScript: String
                                             true - The driver is enabled.

                                             false - The driver is disabled.

<!-- p.1164 -->

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

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1165 -->

How to Delete a Windows Driver from
Configuration Manager
Article • 10/04/2022

You delete a Windows driver from the operating system deployment driver catalog, in
Configuration Manager, by deleting its SMS_Driver Server WMI Class object. When you
delete a driver, its definition is deleted, and it is no longer matched by the apply driver
action task sequences. However, if the content associated with the driver was added to a
driver package, or if the driver was added to a boot image package, the content remains
there until the packages are updated.

To delete a Windows driver
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get the SMS_Driver object for the driver that you want to delete.

   3. Delete the SMS_Driver object.

Example
The following example method deletes a driver identified by its CI_ID property value.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub DeleteDriver(connection,driverID)

             ' Get the driver.
             Set driver = connection.Get("SMS_Driver.CI_ID=" & driverID)

             ' Commit changes.
             driver.Delete_

  End Sub

  c#

<!-- p.1166 -->

  public void DeleteDriver(WqlConnectionManager connection,
                           int driverID)
  {
      try
      {
          // Get the driver.
          IResultObject driver = connection.GetInstance("SMS_Driver.CI_ID=" +
  driverID);

              // Delete the driver.
              driver.Delete();
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to delete driver: " + e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                               ﾉ   Expand table

 Parameter      Type                            Description

 connection     -                               A valid connection to the SMS Provider.
                Managed: WqlConnectionManager
                - VBScript: SWbemServices

 driverID       - Managed: Integer              The Windows driver identifier available in
                - VBScript: Integer             SMS_Driver.CI_ID .

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

<!-- p.1167 -->

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1168 -->

How to Delete a Driver Package in
Configuration Manager
Article • 10/04/2022

You delete an operating system deployment driver package, in Configuration Manager,
by deleting its SMS_DriverPackage object.

  ７ Note

  Windows drivers that are referenced by the driver package are not deleted.

To delete a driver package
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get the SMS_DriverPackage object for the driver that you want to delete.

   3. Delete the SMS_DriverPackage object.

Example
The following example method deletes a driver package identified by its package
identifier.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub DeleteDriverPackage(connection,packageID)

          ' Get the driver.
          Set driverPackage = connection.Get("SMS_DriverPackage.PackageID='" &
  packageID & "'")

              ' Delete the driver package.
              driverPackage.Delete_

  End Sub

  c#

<!-- p.1169 -->

  public void DeleteDriverPackage(
      WqlConnectionManager connection,
      string packageId)
  {
      try
      {
          // Get the driver package.
          IResultObject driverPackage =
  connection.GetInstance("SMS_DriverPackage.packageId='" + packageId + "'");

              // Delete the driver package.
              driverPackage.Delete();
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to delete driver package: " + e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                                 ﾉ   Expand table

 Parameter      Type                            Description

 Connection     -                               A valid connection to the SMS Provider.
                Managed: WqlConnectionManager
                - VBScript: SWbemServices

 packageID      - Managed: String               - The driver package identifier available in
                - VBScript: String              SMS_DriverDriverPackage.PackageID.

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

<!-- p.1170 -->

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1171 -->

How to Specify the Supported Platforms
for a Driver
Article • 10/04/2022

In Configuration Manager, you specify the supported platforms of a driver in the
SDMPackageXML property XML of the driver's SMS_Driver Server WMI Class object. The

XML contains a node PlatformApplicabilityConditions to which you add
PlatformApplicabilityCondition elements for each platform the driver supports.

  ７ Note

  You should add only platforms that are listed in a SMS_SupportedPlatforms Server
  WMI Class object. Drivers can only be conditioned for major operating system
  releases, that is, it is not possible to target drivers at service packs.

  Ｕ Caution

  The supported platforms portion of SDMPackageXML is the only part of the CI-XML
  schema that can be edited. You should not make changes to other parts of the
  XML.

  The following XML demonstrates a driver that supports two platforms. For more
  information about the supported platforms schema, see Operating System
  Deployment Driver Supported Platforms Schema.

  <PlatformApplicabilityConditions>
      <PlatformApplicabilityCondition DisplayName="All x64 Windows XP
  Professional" MaxVersion="5.20.9999.9999" MinVersion="5.20.3790.0" Name="Win
  NT" Platform="x64">
          <Query1>SELECT * FROM Win32_OperatingSystem WHERE BuildNumber =
  '3790' AND OSType=18 AND ProductType=1</Query1>
          <Query2>SELECT * FROM Win32_Processor WHERE Architecture=9 AND
  DataWidth=64</Query2>
          </PlatformApplicabilityCondition>
      <PlatformApplicabilityCondition DisplayName="All x86 Windows 2000"
  MaxVersion="5.00.9999.9999" MinVersion="5.00.0000.0" Name="Win NT"
  Platform="I386">
          <Query1>SELECT * FROM Win32_OperatingSystem WHERE BuildNumber =
  '2195' AND OSType=18 AND ServicePackMajorVersion >= 4</Query1>
          <Query2>SELECT * FROM Win32_Processor WHERE Architecture=0</Query2>

<!-- p.1172 -->

      </PlatformApplicabilityCondition>
  </PlatformApplicabilityConditions>

To validate the platform applicability requirements, use the SMS_SupportedPlatforms
Server WMI Class class Condition property for the required platform.

To specify the supported platforms for a driver
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get the SMS_Driver Server WMI Class object for the driver. The driver is identified
        by the key property CI_ID . For information about getting objects by using a key
        property, see How to Read a Configuration Manager Object by Using Managed
        Code

   3. Update the driver XML.

   4. Commit the changes back to the SMS Provider.

Example
The following example method adds a supported platform to the driver that is identified
by objDriver . For example, the following calling code adds Windows XP Professional
x64 operating system to the driver objDriver list of supported platforms. You can get
the details for a specific platform from its SMS_SupportedPlatforms object instance.

AddSupportedPlatform objDriver, "All x64 Windows XP Professional",

"5.20.9999.9999","5.20.3790.0", "Win NT","x64", "SELECT * FROM

Win32_OperatingSystem WHERE BuildNumber = 3790 AND OSType=18 AND ProductType=1",
"SELECT * FROM Win32_Processor WHERE Architecture=9 AND DataWidth=64"

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub AddSupportedPlatform( objDriver, sDisplayName, sMaxVersion, sMinVersion,
  sName, sPlatform, sQuery1, sQuery2 )

         Dim xmlDoc
         Dim objPlatformNode
         Dim objAttr
         Dim objQuery1Node

<!-- p.1173 -->

    Dim objQuery2Node
    Dim objPlatformsNode
    Dim objDriverNode

    ' Load the SDM Package XML.
    Set xmlDoc = CreateObject("Msxml2.DOMDocument.6.0")

    xmlDoc.async = False
    xmlDoc.loadXML(objDriver.Properties_.item("SDMPackageXML"))
    xmlDoc.setProperty _

"SelectionNamespaces","xmlns:dcm='http://schemas.microsoft.com/SystemsCenter
ConfigurationManager/2006/03/24/DesiredConfiguration'"

    ' Create a new platform node.
    Set objPlatformNode = xmlDoc.createNode _
    ( 1, "PlatformApplicabilityCondition", _

"http://schemas.microsoft.com/SystemsCenterConfigurationManager/2006/03/24/D
esiredConfiguration")

    ' Set DisplayName.
    Set objAttr = xmlDoc.createAttribute("DisplayName")
    objAttr.value = sDisplayName
    objPlatformNode.setAttributeNode(objAttr)

    ' Set MaxVersion.
    Set objAttr = xmlDoc.createAttribute("MaxVersion")
    objAttr.value = sMaxVersion
    objPlatformNode.setAttributeNode(objAttr)

    ' Set MinVersion.
    Set objAttr = xmlDoc.createAttribute("MinVersion")
    objAttr.value = sMinVersion
    objPlatformNode.setAttributeNode(objAttr)

    ' Set Name.
    Set objAttr = xmlDoc.createAttribute("Name")
    objAttr.value = sName
    objPlatformNode.setAttributeNode(objAttr)

    ' Set Platform.
    Set objAttr = xmlDoc.createAttribute("Platform")
    objAttr.value = sPlatform
    objPlatformNode.setAttributeNode(objAttr)

    ' Set Query1.
    Set objQuery1Node = xmlDoc.createNode(1, "Query1",
"http://schemas.microsoft.com/SystemsCenterConfigurationManager/2006/03/24/D
esiredConfiguration")
    objQuery1Node.text = sQuery1
    objPlatformNode.appendChild(objQuery1Node)

    ' Set Query2.
    Set objQuery2Node = xmlDoc.createNode(1, "Query2",

<!-- p.1174 -->

"http://schemas.microsoft.com/SystemsCenterConfigurationManager/2006/03/24/D
esiredConfiguration")
    objQuery2Node.text = sQuery2
    objPlatformNode.appendChild(objQuery2Node)

    ' Append to platforms node.
    Set objPlatformsNode =
xmlDoc.selectSingleNode("/dcm:DesiredConfigurationDigest/dcm:Driver/dcm:Plat
formApplicabilityConditions")
    objPlatformsNode.appendChild(objPlatformNode)

    ' Increment the version number.
    Set objDriverNode =
xmlDoc.selectSingleNode("/dcm:DesiredConfigurationDigest/dcm:Driver")
    Set objAttr = objDriverNode.attributes.getNamedItem("Version")
    objAttr.value = objAttr.value + 1

     ' Save the object.
     objDriver.Properties_.item("SDMPackageXML") = xmlDoc.xml
     objDriver.Put_

End Sub

c#

public void AddSupportedPlatform(
    IResultObject driver,
    string displayName,
    string maxVersion,
    string minVersion,
    string name,
    string platform,
    string query1,
    string query2)
{
    try
    {
        XmlDocument xmlDoc = new XmlDocument();
        xmlDoc.LoadXml(driver["SDMPackageXML"].StringValue);

        string dcmXmlNamespace =
"http://schemas.microsoft.com/SystemsCenterConfigurationManager/2006/03/24/D
esiredConfiguration";
        XmlNode condition = xmlDoc.CreateNode
         (XmlNodeType.Element, "PlatformApplicabilityCondition",
dcmXmlNamespace);

        XmlAttribute displayNameAttribute =
xmlDoc.CreateAttribute("DisplayName");
        displayNameAttribute.Value = displayName;
        condition.Attributes.SetNamedItem(displayNameAttribute);

          XmlAttribute osMaxVersionAttribute =

<!-- p.1175 -->

xmlDoc.CreateAttribute("MaxVersion");
        osMaxVersionAttribute.Value = maxVersion;
        condition.Attributes.SetNamedItem(osMaxVersionAttribute);

        XmlAttribute osMinVersionAttribute =
xmlDoc.CreateAttribute("MinVersion");
        osMinVersionAttribute.Value = minVersion;
        condition.Attributes.SetNamedItem(osMinVersionAttribute);

       XmlAttribute osNameAttribute = xmlDoc.CreateAttribute("Name");
       osNameAttribute.Value = name;
       condition.Attributes.SetNamedItem(osNameAttribute);

        XmlAttribute osPlatformAttribute =
xmlDoc.CreateAttribute("Platform");
        osPlatformAttribute.Value = platform;
        condition.Attributes.SetNamedItem(osPlatformAttribute);

       // Create <Query1/> and <Query2/> child nodes.
       // Then attach to <PlatformApplicabilityCondition/>.
       XmlNode query1Node = xmlDoc.CreateNode
           (XmlNodeType.Element, "Query1", dcmXmlNamespace);
       query1Node.InnerText = query1;
       condition.AppendChild(query1Node);

       XmlNode query2Node = xmlDoc.CreateNode
           (XmlNodeType.Element, "Query2", dcmXmlNamespace);
       query2Node.InnerText = query2;
       condition.AppendChild(query2Node);

        XmlNode platformsNode = xmlDoc["DesiredConfigurationDigest"]
["Driver"]["PlatformApplicabilityConditions"];

           if (platformsNode == null)
       {
             Console.WriteLine("empty");
       }

       platformsNode.AppendChild(condition);

        XmlNode driverNode = xmlDoc["DesiredConfigurationDigest"]["Driver"];
        if (driverNode != null)
        {
             int driverVersion =
int.Parse(driverNode.Attributes.GetNamedItem("Version").Value) + 1;
             driverNode.Attributes.GetNamedItem("Version").Value =
(driverVersion + 1).ToString();
        }
        else
        {
             throw new XmlException("Unable to find <Driver/> node while
AddingSupportedPlatforms");
        }

       // Add the package XML to the driver.

<!-- p.1176 -->

              StringBuilder xmlText = new StringBuilder();
              xmlDoc.WriteContentTo(new XmlTextWriter(new StringWriter(xmlText)));
              driver["SDMPackageXML"].StringValue = xmlText.ToString();

             driver.Put();
      }
      catch (SmsException e)
      {
          Console.WriteLine("failed to add supported platform to driver " +
  e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                                   ﾉ   Expand table

 Parameter       Type                 Description

 driver          - Managed:           - A valid SMS_Driver object. For more information, see How
                  IResultObject       to Import a Windows Driver Described by an INF File into
 objDriver       - VBScript:          Configuration Manager.
                 SWbemObject

 displayName     - Managed:           The display name for the condition shown in the
                  String              Configuration Manager console.
 sDisplayName    - VBScript: String

 maxVersion      - Managed:           The maximum supported version.
                  String
 sMaxVersion     - VBScript: String

 minVersion      - Managed:           The minimum supported version.
                  String
 sMinVersion     - VBScript: String

 name            - Managed:           The operating system name.
                  String
 sName           - VBScript: String

 platform        - Managed:           The platform name.
                  String
 sPlatform       - VBScript: String

 query1          - Managed:           The first query used to identify the client platform.
                  String
 sQuery1         - VBScript: String

<!-- p.1177 -->

 Parameter     Type                 Description

 query2        - Managed:           The second query used to identify the client platform.
               String
 sQuery2       - VBScript: String

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

System.Xml

System.IO

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also

<!-- p.1178 -->

SMS_SupportedPlatforms Server WMI Class
Objects overview How to Connect to an SMS Provider in Configuration Manager by
Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Move a Step to a Different Operating System Deployment Task Sequence Group
How to Create an Operating System Deployment Task Sequence Group
How to Remove a Step From an Operating System Deployment Group
Task sequence overview SMS_SupportedPlatforms Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1179 -->

How to Add a Category to a Windows
Driver
Article • 10/04/2022

In Configuration Manager, you add a category to a Windows driver by adding the
unique identifier for the category to the SMS_Driver Server WMI
Class CategoryInstance_UniqueIDs array property. The array contains one or more string
identifiers that match the SMS_CategoryInstance Server WMI
Class CategoryInstance_UniqueID property value. There is an instance of
SMS_CategoryInstance Server WMI Class object for each category in the system.

  ７ Note

  The unique identifier for a driver category is prepended with the text
  "DriverCategories". Other category types have different text.

A category has localization information, and it is from the SMS_CategoryInstance Server
WMI Class LocalizedCategoryInstanceName property that the display name of the
category is obtained.

To add a category to a Windows driver
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Get the SMS_Driver object for the driver you want to add a category to.

   3. Get the category name identifier from the SMS_CategoryInstance Server WMI Class
      object that matches the desired category.

   4. Add the category identifier to the SMS_Driver Server WMI Class object
      CategoryInstance_UniqueIDs array property.

   5. Commit the SMS_Driver Server WMI Class changes.

Example
The following example method adds a category to a Windows driver. driverID is a valid
SMS_Driver Server WMI Class object. For more information, see About Operating System

<!-- p.1180 -->

Deployment Driver Management.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub AddDriverCategory(connection,driver,categoryName)

         Dim categories
         Dim category
         Dim driverCategoryID
         Dim categoryID
         Dim results
         Dim existingCategory

      ' Find the category that matches the supplied category name.
      Set results = _
        connection.ExecQuery("SELECT * From SMS_CategoryInstance WHERE
  LocalizedCategoryInstanceName = '" _
        + categoryName+ "'")

         ' If the category was found, add it to the driver.
         For Each category in results

          If IsNull(driver.CategoryInstance_UniqueIDs) or UBound
  (driver.CategoryInstance_UniqueIDs) = -1 Then
              ' It is empty. Add the category.
              driver.CategoryInstance_UniqueIDs =
  Array(category.CategoryInstance_UniqueID)
           Else

                ' Determine if the category is already applied to the driver.
                For each existingCategory in driver.CategoryInstance_UniqueIDs
                    if existingCategory = category.CategoryInstance_UniqueID
  Then
                        WScript.Echo "Already added"
                        Exit Sub
                    End If
                Next

              ' Add the category.
              categories = driver.CategoryInstance_UniqueIDs
              Redim Preserve categories (UBound
  (driver.CategoryInstance_UniqueIDs)+1)
              categories (Ubound (categories)) =
  category.CategoryInstance_UniqueID
              driver.CategoryInstance_UniqueIDs = categories
          End If

          driver.Put_
      Next
  End Sub

<!-- p.1181 -->

  c#

  public void AddDriverCategory(
      WqlConnectionManager connection,
      IResultObject driver,
      string categoryName)
  {
      try
      {
          // Get the category.
          IResultObject results = connection.QueryProcessor.ExecuteQuery(
          "SELECT * From SMS_CategoryInstance WHERE
  LocalizedCategoryInstanceName = '" + categoryName + "'");

         ArrayList driverCategories = new
  ArrayList(driver["CategoryInstance_UniqueIDs"].StringArrayValue);//;driverCa
  tegories);

          foreach (IResultObject category in results)
          {
               foreach (string driverCategory in driverCategories)
               {
                   // Do nothing if the driver already has the category.
                   if (driverCategory ==
  category["CategoryInstance_UniqueID"].StringValue)
                   {
                       Console.WriteLine("Already exists");
                       return;
                   }
             }

              // Add the category to the action.

  driverCategories.Add(category["CategoryInstance_UniqueID"].StringValue);
          }

          // Update the driver.
          driver["CategoryInstance_UniqueIDs"].StringArrayValue =
  (string[])driverCategories.ToArray(typeof(string));
          driver.Put();

       }
       catch (SmsException e)
       {
           Console.WriteLine("Failed to add the category" + e.Message);
           throw;
       }
  }

The example method has the following parameters:

                                                                    ﾉ   Expand table

<!-- p.1182 -->

 Parameter      Type                      Description

 Connection     - Managed:                A valid connection to the SMS Provider.
                WqlConnectionManager
                - VBScript:
                SWbemServices

 driver         - Managed:                The Windows driver. It is an instance of SMS_Driver
                IResultObject             Server WMI Class.
                - VBScript: SWbemObject

 categoryName   - Managed: String         The name of an existing category. This matches the
                - VBScript: String        SMS_CategoryInstance Server WMI Class
                                          LocalizedCategoryInstanceName property.

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

<!-- p.1183 -->

For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About Operating System Deployment Driver Management
How to Remove a Category from a Windows Driver

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1184 -->

How to Remove a Category from a
Windows Driver
Article • 10/04/2022

In Configuration Manager, you remove a category from a Windows driver by removing
the unique identifier for the category from the SMS_Driver Server WMI Class
CategoryInstance_UniqueIDs array property.

To remove a category from a Windows driver
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get the SMS_Driver object for the driver that you want remove the category from.

   3. Get the category name identifier from the SMS_CategoryInstance Server WMI Class
        object that matches the desired category.

   4. Remove the category identifier from the SMS_Driver Server WMI Class object
        CategoryInstance_UniqueIDs array property.

   5. Commit the SMS_Driver Server WMI Class changes.

Example
The following example method removes a category from a Windows driver. driverID is
a valid SMS_Driver Server WMI Class object. For more information, see About Operating
System Deployment Driver Management.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub RemoveDriverCategory(connection,driver,categoryName)

         Dim results
         Dim driverCategoryID
         Dim category
         Dim categories
         Dim i

         If IsNull(driver.CategoryInstance_UniqueIDs) _

<!-- p.1185 -->

            or UBound (driver.CategoryInstance_UniqueIDs) = -1 Then
         ' There are no categories, so quit.
         Wscript.Echo "No categories found"
         Exit Sub
     End If

     Set results = _
      connection.ExecQuery("SELECT * From SMS_CategoryInstance WHERE
LocalizedCategoryInstanceName = '" _
      + categoryName+ "'")

     ' If the category was found, delete, if it is there, from the driver.
     For Each category In results

        ' Destination for copied categories.
        categories = Array(driver.CategoryInstance_UniqueIDs)
        i=0

        For Each driverCategoryID in driver.CategoryInstance_UniqueIDs
             If driverCategoryID = category.CategoryInstance_UniqueID Then
                 ' Found it, so skip it.
                  Redim Preserve categories (UBound(categories))
             Else
                 ' Copy the category.
                 categories(i) = driverCategoryID
                 i=i+1
             End If
        Next

        ' Make sure the array is empty.
        if i = 0 Then
            Redim categories(-1)
        End If

           driver.CategoryInstance_UniqueIDs = categories
           driver.Put_
    Next
End Sub

c#

public void RemoveDriverCategory(WqlConnectionManager connection,
    IResultObject driver,
    string categoryName)
{
    try
    {
        // Get the category.
        IResultObject results =
            connection.QueryProcessor.ExecuteQuery(
            "SELECT * From SMS_CategoryInstance WHERE
LocalizedCategoryInstanceName = '"
            + categoryName

<!-- p.1186 -->

                  + "'");

          ArrayList driverCategories = new
  ArrayList(driver["CategoryInstance_UniqueIDs"].StringArrayValue);

              // Remove the category from the driver.
              foreach (IResultObject category in results)
              {

  driverCategories.Remove(category["CategoryInstance_UniqueID"].StringValue);
          }

          // Update the driver.
          driver["CategoryInstance_UniqueIDs"].StringArrayValue =
  (string[])driverCategories.ToArray(typeof(string));
          driver.Put();
      }
      catch(SmsException e)
      {
          Console.WriteLine("Failed to remove category :" + e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                               ﾉ   Expand table

 Parameter       Type                            Description

 Connection      -                               A valid connection to the SMS Provider.
                 Managed: WqlConnectionManager
                 - VBScript: SWbemServices

 driver          - Managed: IResultObject        The Windows driver. It is an instance of
                 - VBScript: SWbemObject         SMS_Driver Server WMI Class.

 categoryName    - Managed: String               The name of an existing category. This matches
                 - VBScript: String              the SMS_CategoryInstance Server WMI Classe
                                                 LocalizedCategoryInstanceName property.

Compiling the Code
This C# example requires:

Namespaces
System

<!-- p.1187 -->

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
About Operating System Deployment Driver Management
How to Add a Category to a Windows Driver

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1188 -->

About Configuration Manager Custom
Actions
Article • 10/04/2022

You can create custom actions that can be used with existing Configuration Manager
actions.

Custom actions are command-line actions that calls an application. The application can
be a process, a script or other commands that you specify in a Managed Object Format
(MOF) file description.

For more information, see About Configuration Manager Custom Action Client
Applications.

To allow users to configure your custom action, you can create a custom action control
that integrates into the Task Sequence Editor.

Creating a custom action control requires the following steps.

Creating the Custom Action Control
To create a custom action control, you use Visual Studio 2005 to create a Windows
control that implements two classes.

The control that is displayed in the Task Sequence Editor is the first class, which derives
from the SMSOsdEditorPageControl class. In this class, you define the user interface
and the data transfer to and from the action. When a custom action is created, the
control's PropertyManager makes the custom action's properties available for use. These
are the properties that are defined in the custom action MOF file.

The second class implements the options control, and it derives from the
TaskSequenceOptionControl class.

For more information about creating a custom control in Visual Studio, see How to
Create a Configuration Manager Custom Action Control.

  ７ Note

  The Configuration Manager SDK sample CustomTasksequenceAction shows how to
  create a custom task sequence action control and MOF.

<!-- p.1189 -->

Supporting Help
You cannot integrate your control's Help with the Configuration Manager console F1 key
Help support. If a user presses F1 in your control, the control does nothing. However,
you can implement Help in your control by using a mechanism of your choice to open
the Help .chm file. For example, you can add a Help button that opens your Help .chm
file.

Creating the Custom Action MOF File
Each Configuration Manager action is defined in the task sequence provider MOF file,
_tasksequenceprovider.mof. A custom action extends this MOF file with a description for
the custom action class. You should create the description of your custom action in a
separate MOF file.

For more information, see About the Configuration Manager Custom Action MOF File
and How to Create a MOF File for a Configuration Manager Custom Action.

Deploying the Custom Action Control
Assembly
After the custom action control assembly is created, it must be copied to the same
directory as the Adminui.tasksequenceeditor.dll. Typically this directory is in
%ProgramFiles%\Microsoft Configuration Manager\AdminUI\bin.

Using the Custom Action Control
To use the custom action, you create and edit a task sequence in the Configuration
Manager console. Clicking Add displays a list of categories, and you should see the
custom action listed in the category that you specified in the custom action MOF file.

After you select it, you will see the control that you have created. The action behaves
like the default Configuration Manager actions. You can add conditions to the action
and you can move the action within the task sequence.

For more information, see How to Use a Configuration Manager Custom Action.

Feedback

<!-- p.1190 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1191 -->

About Configuration Manager custom
action client applications
Article • 10/04/2022

The task sequence in Configuration Manager does custom action operations during
client deployment. The application can be a process, a script, or other commands. The
requirements for the application are defined in a Managed Object Format (MOF) file.
Example requirements include the operating environment, command-line arguments,
properties, and return codes. They're added to the task sequence environment when the
action is processed.

Custom action MOF file
The MOF file for a custom action is similar to the following example:

  Managed Object Format

  [   CommandLine("smsswd.exe /run:%1 abc.exe %2"),
      : (custom ui control and category qualifiers for action)
      ]
  class MyCustomAction : SMS_TaskSequence_Action
  {
      [TaskSequencePackage, CommandLineArg(1)]
      string          PackageIDForAbcExe;

       [CommandLineArg(2), AllowedLen("1-32000")]
       string          AbcCommandLineArgs;

       [SuccessCodes, Not_Null]
       string          AbcSuccessCodes = "0 3010";

       string             SomeOtherPropertyThatAbcNeeds;

       string             SupportedEnvironment = "WinPEandFullOS";
  };

The MOF file describes the information that is needed for the custom action application
input, environment, properties, and deployment package information.

For more information, see About the Configuration Manager custom action MOF file.

Application input

<!-- p.1192 -->

Custom actions have to run unattended, so the application shouldn't prompt for user
input. All inputs should be received from either the command line, the task sequence
environment, or from a data file.

The command line for the action application is set, in the MOF file, by using the Run
command line built-in action.

For example:

  Managed Object Format

  CommandLine("smsswd.exe /run:PackageID abc.exe [any abc.exe command line
  args]"

Application processing
The task sequence application runs the custom action operations. It must be aware of its
operating environment and have access to the task sequencing environment variables,
report progress, and return completion codes.

Environment
The MOF file should specify the operating environment with the
SMS_TaskSequence_Action Server WMI Class SupportedEnvironment property. The
available environments are Windows PE ( WinPE ), full operating system ( FullOS ), or both
environments ( WinPEandFullOS ).

The choice of environment depends on the circumstances. For example, pre-operating
install configuration will likely be done in the Windows PE environment. For more
information, see Infrastructure requirements for OS deployment. Updates to currently
installed operating systems will use the full operating system environment. For example,
software or driver installation. Operating system environment agnostic tasks such as
reboots or the creation of network connections, can be performed by using both
environment settings.

Processing
During processing, you access the task sequence variables defined by the MOF file by
using the TSEnvironment COM automation object. For more information, see How to Use
Task Sequence Variables in a Running Configuration Manager Task Sequence.

<!-- p.1193 -->

If the operation takes a long time, you can report progress to the task sequence
environment and display a progress indicator by using the ProgressUI client COM
automation class. For more information, see About reporting Configuration Manager
custom action progress.

Completion
The application should set the SuccessCodes environment variable as a return value
when it's completed.

                                                                          ﾉ   Expand table

 Return                                    Description

 0                                         Success

 Non-zero                                  Failure

If a reboot is required after the application finishes, the SMSTSRebootRequested
environment variable should be set. For more information, see Task sequence variables.
For information about setting environment variables, see How to use task sequence
variables in a running Configuration Manager task sequence.

Deployment
To be used by Configuration Manager, the custom action application must be available
from a Configuration Manager package. The administrator can create the package by
using either the Configuration Manager console or by using a programming language.
For more information, see How to create a package.

The package identifier must be available for the deployment to work. Typically the MOF
file declares a property to hold it, as in the following example:

     Managed Object Format

     [TaskSequencePackage, CommandLineArg(1)]
     string PackageIDForAbcExe;

     ７ Note

     The package identifier is the SMS_Package Server WMI Class PackageID property.

<!-- p.1194 -->

The package identifier is obtained from the administrator, when the custom action is
edited in the task sequence editor.

To enable this behavior, your custom action control can use a text edit control in its
implementation to get the package identifier from the administrator. For an example
that uses a text control, see How to create a Configuration Manager custom action
control.

When used by the administrator, the custom action control is edited as part of a task
sequence by using the task sequence editor. When saved by the task sequence editor,
an SMS_TaskSequencePackage Server WMI Class is created to hold the task sequence,
including the custom action.

The task sequence package is then advertised to clients along with the custom action
package that is referenced by the custom action. For more information, see How to
create an advertisement.

When the custom action is run on the client, the package identifier for the custom
action is supplied as a command-line parameter, from which the binary files for the
custom action are extracted and run.

The package identifier is provided by using the /run command-line parameter to
Smsswd.exe.

Pre-network partition and pre-partition setup
If you need to configure disk or network connectivity before you have a disk partition
and before you have network connectivity, you need to create an application to do
these tasks. Your application should be placed in a custom boot image by using the
Windows Assessment and Deployment Kit (ADK). For more information, see Windows
ADK scenarios for IT Pros.

  ７ Note

  Adding files to the boot image file can increase the minimum RAM requirements
  and can, due to low memory conditions, cause task sequences to fail in unexpected
  ways.

Then import the image into Configuration Manager as a custom image. For more
information, see Add a boot image.

<!-- p.1195 -->

The application, any supporting files, and the custom SMSTS.INI should be placed in the
Windows folder.

To use the application, use the custom boot image in a task sequence that contains a
pre-partition/network step.

See also
About Configuration Manager custom actions

About the Configuration Manager custom action MOF file

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1196 -->

About Configuration Manager Custom
Action MOF Files
Article • 10/04/2022

In Configuration Manager, operating system deployment actions are defined in the
Managed Object Format (MOF) file, %ProgramFiles%\Microsoft Configuration
Manager\bin\i386\_tasksequenceprovider.mof.

When you create a custom action, you must create a MOF file that declares your custom
action. You then use Mofcomp.exe to add your changes to the SMS Provider. For more
information, see How to Create a MOF File for a Configuration Manager Custom Action.

The administrator configures the custom action, as defined by the MOF file, by using a
custom action control. For more information, see About Configuration Manager Custom
Actions.

MOF File Content
A custom action derives from SMS_TaskSequence_Action Server WMI Class. The MOF file
declaration includes a class definition and various qualifiers for the command line, task
sequence variables, category, and custom action control assembly location.

Properties declared in a class, except those with the CommandLineArg qualifier, are
available as task sequence variables during client deployment. For more information, see
How to Use Task Sequence Variables in a Running Configuration Manager Task
Sequence.

The namespace for the custom action is \\root\SMS_Site_SITECODE. When the MOF file
is compiled, the custom action is made a child of SMS_TaskSequence_Action Server WMI
Class.

  ７ Note

  For an example MOF, see the task sequence action MOF that is declared in
  _tasksequenceprovider.mof.

The section of the MOF file for the custom action declaration will look similar to the
following example:

<!-- p.1197 -->

  [   CommandLine("smsswd.exe /run:%1 Application.exe /user:%2"),
      VariablePrefix("MyCustomActionPrefix"),
      ActionCategory("My Custom Action Category,7,1"),
      ActionName{"ConfigMgrTSAction.dll",
  "ConfigMgrTSAction.Properties.Resources", "ConfigMgrTSAction"},
      ActionUI{"ConfigMgrTSAction.dll",
  "ConfigMgrTSAction","ConfigMgrTSActionControl",
  "ConfigureTSActionOptions"}
      ]
  class ConfigMgrTSActionControl : SMS_TaskSequence_Action
  {
      [TaskSequencePackage, CommandLineArg(1)]
      string          PackageIDForApplicationExe;

       [Not_Null, CommandLineArg(2)]
       string          User;

       [VariableName("CustomLocation")]
       string          Location;

  };

The complete MOF also specifies the namespace and other information,

For the complete MOF for this sample, see How to Create a MOF File for a Configuration
Manager Custom Action.

Command Line
The command line for the action is described in the CommandLine class qualifier. It
defines the application that is called and the various arguments that can be supplied.
For each command-line argument, there is a CommandLineArg class qualifier for the
argument on the corresponding class property.

CommandLine typically takes the form:

CommandLine("smsswd.exe /run:%1 Application.exe %2 %3")

Smsswd.exe is used to run a program within a package. It requires the following
arguments:

                                                                         ﾉ   Expand table

<!-- p.1198 -->

 Argument          Description

 /run:%1           Identifies the package that the application is in. %1 is the package identifier
                   (SMS_Package Server WMI Class PackageID property).

 Application.exe   The custom action application that is performed.

 %2 - %n           One or more command-line arguments for Application.exe.

The command-line substitution strings, %1, %2 and so forth, are defined by the
CommandLineArg class qualifier. For example, the following declares %1.

  [TaskSequencePackage, CommandLineArg(1)]
  string          PackageIDForApplicationExe;

With the custom action control, you use the PackageIDForApplicationExe property to
configure the package identifier.

  ７ Note

  Properties declared with the CommandLineArg qualifier are not available as task
  sequence variables during client deployment.

Action Category
An action can be associated with a specific category, in the task sequence editor drop
down menu, by using the ActionCategory class qualifier.

  ７ Note

  Do not use a category that is already in use by another action.

The syntax is:

ActionCategory{CategoryName,ActionOrder,CategoryOrder}

CategoryName

The category name.

<!-- p.1199 -->

ActionOrder

The action order within the category.

CategoryOrder

The category order within all categories.

The default Configuration Manager categories that you can add an action to are:

     General

     Disks

     User State

     Images

     Drivers

     Settings

     You can also create a new category by specifying a new category in the
     ActionCategory class qualifier. For example, the following MOF file creates a new

     category called My Custom Category. The action is placed second within the
     category and the category is placed fifth overall.

     ActionCategory{"My Custom Category",2,5"},

ActionName
The ActionName class qualifier defines the custom action control name. The qualifier has
the following syntax:

ActionName{"Assembly", "Namespace.Properties.Resources", "Control"}

Assembly

The assembly that contains the action control.

Namespace.Properties.Resources

The namespace for the resource that contains the displayed action name strings. For
more information, see How to Create a Configuration Manager Custom Action Control.

Control

The control that contains the string resources.

Action User Interface

<!-- p.1200 -->

The ActionUI class qualifier defines the location of the assembly and classes that are
used by an action. The qualifier has the following syntax:

ActionUI{"Assembly","Namespace", "Control", "Option control"}

Assembly

The assembly that contains the action control.

Namespace

The namespace that the action control resides in.

Control

The action control displayed in the task sequence editor. It hosts the option control
page.

Option control

The page used to manage action options, in the task sequence editor.

Multiple control tabs can be implemented by including more control class names
separated by commas. For example:

ActionUI{"Assembly","Namespace", "Control1", "Control2", "Control3", "Option control"}

Action Variables
The VariableName qualifier is used to override the default variable name for a property.

A class property can be defined as a task sequence variable by adding the VariableName
class qualifier. In the example above, the property MessageTimeout is an action variable
with the name RebootTimeout .

If the VariablePrefix class qualifier is used, the variables are prefixed with the class
qualifier value.

For more information about variable usage, see How to Use Task Sequence Variables in
a Running Configuration Manager Task Sequence

Properties

Qualifiers

There are several qualifiers that can be applied to the MOF properties. The following are
commonly used:
