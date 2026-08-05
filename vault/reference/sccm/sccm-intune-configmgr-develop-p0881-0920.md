---
title: "Configuration Manager SDK documentation — pages 881-920"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0881-0920
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0881-0920
family: sccm
documentKind: "doc"
abstract: "About Updating an Existing Resource Instance Article • 10/04/2022 When the Data Discovery Manager (DDM), in Configuration Manager, finds an existing resource that matches the data discovery record (DDR), the resource instance is updated; otherwise, a new instance is created. The"
---

# Configuration Manager SDK documentation — pages 881-920

<!-- p.881 -->

About Updating an Existing Resource
Instance
Article • 10/04/2022

When the Data Discovery Manager (DDM), in Configuration Manager, finds an existing
resource that matches the data discovery record (DDR), the resource instance is
updated; otherwise, a new instance is created. The DDM uses the following approach to
find a resource match.

Unique Identifier Specified by DDR
If the DDR specifies the unique identifier property for the resource, it is used to find a
matching resource instance.

If more than one match is found (in the case of cloned computers) or if a match is not
found by using the specified unique identifier, the key properties are used to find a
matching resource. All key values must match those of an existing resource. In the case
of cloned computers, the DDM determines a match that is based on the first key match
found.

No Unique Identifier Specified by DDR
If the DDR does not specify the unique identifier property, the key property values are
used to find a matching resource. The DDM determines a match that is based on any
single key value matching the same key value of an existing resource. In the case of
multiple key matches, the match with the most matching keys is chosen.

In both cases, the record that was most recently discovered is chosen in the event of a
tie.

Before you update an existing instance, you must know the key properties and unique
identifier of the resource type. You can run the following query against the
Configuration Manager SQL Server database to determine the key properties for a
resource class.

   SELECT * FROM DiscPropertyDefs WHERE (Flags & 0x8) = 0x8

<!-- p.882 -->

To determine the unique identifier property, use (Flags & 0x2) = 0x2 in the WHERE
clause. The following table shows the unique identifier and key properties for the
system, user, and user group resource classes.

                                                                          ﾉ    Expand table

 Resource            Property String                     Flag

 System              NetbiosName                         Key.

                     MAC Address                         Key.

                     SMS Unique Identifier               Unique Identifier.

 User                Unique User Name                    Key, unique identifier.

 User Group          Unique Usergroup Name               Key, unique identifier.

System resources use a GUID value for the unique identifier that is stored on the
Configuration Manager client in the system registry. For more information, see How to
Get the Unique Identifier Value for a Client.

For an example that updates the system resource type, see How to Add New Properties
to an Existing Resource Type.

Heartbeat DDR Processing
A Heartbeat DDR is processed if it comes with a time stamp that is earlier than any other
DDR (except a Heartbeat DDR). A DDR with a time stamp that is later than the client's
current site database time stamp for that discovery method is rejected. The only
exception is a Heartbeat DDR, which will be processed.

See Also
How to Get the Unique Identifier Value for a Client
How to Add New Properties to an Existing Resource Type

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.883 -->

About Creating a Data Discovery Record
Article • 10/04/2022

To create data discovery records (DDRs), you must use the SMSRsGenCtl.dll and the
functions that are described in the following table. These functions create a single DDR
that can be process by Data Discovery Manager (DDM). The order in which you call the
functions is important; you must call DDRNew before calling any of the functions that add
properties. The order in which you add properties to your class is arbitrary. However, the
last function you call must be DDRWrite to create the DDR. The DDR must then be
manually copied to the SMS\Inboxes\Auth\Ddm.box directory.

DDRs that fail to process are moved to the SMS\Inboxes\Ddm.box\Bad_ddrs directory. If
you have logging turned on, you can view the DDM.log file for an explanation of the
failure. After fixing the source of the errors, you can rerun your program to load the
DDR.

C programmers can use the SMSRsGen.dll file to access the DDR functions. Visual Basic
programmers can use the SMSRsGenCtl.dll to access the DDR methods. These methods
have the same name and parameters as the C library functions.

Because the SMSResGen control is not thread safe, do not try to create more than one
instance of the class.

The SMSResGen method has the following functions:

  ） Important

  The function DDRSendToSMS , available in previous releases of the SDK and in versions
  of SMSRsGen.dll and SMSRsGenCtl.dll , has been deprecated and should not be
  used with Configuration Manager.

DDRNew
Creates a new DDR.

DDRAddInteger
Adds an integer property to the DDR.

DDRAddString
Adds a string property to the DDR.

DDRAddIntegerArray
Adds an integer array property to the DDR.

<!-- p.884 -->

DDRAddStringArray
Adds a string array property to the DDR.

DDRWrite
Writes the DDR to a file.

See Also
Configuration Manager SDK
SMSResGen COM Automation Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.885 -->

About the Unique Identifier Value for a
Resource
Article • 10/04/2022

In Configuration Manager, the Configuration Manager unique identifier property for a
new resource class is optional. If you report inventory data for the resource, you must
include this property. The Configuration Manager unique identifier value must be
unique — it relates your resource discovery data to your inventory data (SMS_G_xxx).
Typically, hardware resources use a GUID to uniquely identify individual resources.

The format of the Configuration Manager unique identifier value is as follows.

  <ID Type>:<ID Value>

For example, Configuration Manager uses a GUID to identify Configuration Manager
clients.

  GUID:4976DCD4-CAAE-11D2-8E00-00104BCC3648

You can use any <ID Type> and <ID Value> values to identify a new resource. However,
when discovering data for an existing resource type, you should follow the convention
that is used by that resource type.

See Also
How to Get the Unique Identifier Value for a Client

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.886 -->

How to Get the Unique Identifier Value
for a Client
Article • 10/04/2022

When you discover system resource data for a client, in Configuration Manager, you
must specify the client's unique identifier value in the data discovery record (DDR), such
as:

  DDRAddString("SMS Unique Identifier",
               "GUID:12345678-1234-1234-1234-123456789012", 64,
               ADDPROP_GUID | ADDPROP_KEY);

The client's unique identifier can be found in Windows Management Instrumentation
(WMI) at:

  root\ccm:CCM_Client=@:ClientId

Procedures

To identify the client's unique identifier in WMI

      1. Connect to the CCM namespace (root\ccm).

      2. Load the CCM_Client class.

      3. Enumerate through the objects in the CCM_Client class and display the unique
        identifier (ClientId).

Example

Description
The following example method shows how to obtain the client's unique identifier from
WMI by connecting to the CCM namespace, loading the CCM_Client class and getting
the ClientId property.

<!-- p.887 -->

  ） Important

  The following C# example requires the System.Management namespace.

For information about calling the sample code, see How to Call a Configuration
Manager Object Class Method by Using WMI

Code
  vbs

  Sub GetClientUniqueID()

        ' Get a connection to the root\ccm namespace on the local system.
        Set objWMIService = GetObject("winmgmts:\\.\root\ccm")

      ' Get all objects in the CCM_Client class.
      set allCCMClientObjects = objWMIService.ExecQuery("Select * from
  CCM_Client")

      ' Loop through the available objects (only one) and display ClientId
  value.
      For Each eachCCMClientObject in allCCMClientObjects
         wscript.echo "ClientId (GUID): " & eachCCMClientObject.ClientId
      Next

  End Sub

  c#

  public void GetClientUniqueID()
  {
      try
      {
          // Define the scope (namespace) to connect to.
          ManagementScope inventoryAgentScope = new
  ManagementScope(@"root\ccm");

          // Load the class to work with (CCM_Client).
          ManagementClass inventoryClass = new
  ManagementClass(inventoryAgentScope.Path.Path, "CCM_Client", null);

          // Query the class for the objects (create query, create searcher
  object, execute query).
          ObjectQuery query = new ObjectQuery("SELECT * FROM CCM_Client");
          ManagementObjectSearcher searcher = new
  ManagementObjectSearcher(inventoryAgentScope, query);

<!-- p.888 -->

           ManagementObjectCollection queryResults = searcher.Get();

          // Loop through the available objects (only one) and display the
  ClientId value.

           foreach (ManagementObject result in queryResults)
           {
               Console.WriteLine("ClientId (GUID): " + result["ClientId"]);
           }
      }

      catch (System.Management.ManagementException ex)
      {
          Console.WriteLine("Failed to get client ID (GUID). Error: " +
  ex.Message);
          throw;
      }
  }

Comments

Compiling the Code
This C# example requires:

Namespaces
System.Management

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
How to Call a WMI Class Method by Using System.Management

<!-- p.889 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.890 -->

How to Add New Properties to an
Existing Resource Type
Article • 10/04/2022

In Configuration Manager, when the Data Discovery Manager (DDM) detects that your
data discovery record (DDR) contains a property that does not exist in the resource
class, the property is added to the resource class. Depending on the data type of the
new property, previous instances of the resource will contain either a zero or an empty
string ("") for the value of the new property. You should specify all the class properties
when you update an existing resource class. However, do not include the seven
properties that the DDM creates for you. When the DDM creates a new resource class, it
adds these additional properties to the class:

      ResourceID

      AgentName

      AgentSite

      AgentTime

      Name

      ResourceType

      SMSAssignedSite

      For a description of these properties, see SMS_R_System . In addition to creating
      these properties, the DDM creates an instance of SMS_ResourceMap for the new
      ResourceType value.

To add properties to an existing resource type
   1. Get a specific instance of an existing resource.

   2. Create a new instance of the SMSResGen class.

   3. Create a new DDR using the NewDDR method.

   4. Add properties to the DDR using the ADDPROP_ methods.

   5. Write the new DDR to a file using the DDRWrite method.

<!-- p.891 -->

Example
The following example creates a DDR that adds the OrganizationalUnit property to the
SMS_R_System class. You can then use this property to create collections based on

departments and distribute software accordingly. If your organization uses Active
Directory, you can use the information it contains to populate the OrganizationalUnit
property.

The following example shows the key, name, and GUID properties that you use to
update the system resource class.

  vbs

  Sub CreateDDRToAddNewPropertiesToAnExistingResourceType()

        ' Define variables.
        Dim resourceID
        Dim existingResource
        Dim newDDR
        Dim siteCode
        Dim organizationalUnit

        ' Set variables.
        resourceID = 5
        siteCode = "TQ1"
        organizationalUnit = "Test OU"

      ' Get a specific resource (client) object using the resourceID value.
      Set existingResource = GetObject("winmgmts:root/sms/site_" & siteCode &
  ":SMS_R_System.ResourceID=" & resourceID & "")

        ' Load an instance of the SMSResGen.dll.
        Set newDDR = CreateObject("SMSResGen.SMSResGen.1")

        ' Create a new DDR using the DDRNew method.
        newDDR.DDRNew "System", "Department Discovery", siteCode

      ' Add properties to the new DDR using the DDRAdd methods.
      newDDR.DDRAddInteger "Client", existingResource.Client, ADDPROP_NONE
      newDDR.DDRAddString "Client Version", existingResource.ClientVersion,
  15, ADDPROP_NONE
      newDDR.DDRAddStringArray "IP Addresses", existingResource.IPAddresses,
  64, ADDPROP_NONE
      newDDR.DDRAddStringArray "IP Subnets", existingResource.IPSubnets, 64,
  ADDPROP_NONE
      newDDR.DDRAddString "Last Logon User Domain",
  existingResource.LastLogonUserDomain, 64, ADDPROP_NONE
      newDDR.DDRAddString "Last Logon User Name",
  existingResource.LastLogonUserName, 255, ADDPROP_NONE
      newDDR.DDRAddStringArray "MAC Addresses", existingResource.MACAddresses,

<!-- p.892 -->

64, ADDPROP_KEY
    newDDR.DDRAddString "NetBIOS Name", existingResource.NetbiosName, 64,
ADDPROP_NAME
    newDDR.DDRAddString "Operating System Name and Version",
existingResource.OperatingSystemNameandVersion, 64, ADDPROP_NONE
    newDDR.DDRAddString "Resource Domain OR Workgroup",
existingResource.ResourceDomainORWorkgroup, 64, ADDPROP_NONE
    newDDR.DDRAddStringArray "Resource Names",
existingResource.ResourceNames, 128, ADDPROP_NONE
    newDDR.DDRAddStringArray "SMS Installed Sites",
existingResource.SMSInstalledSites, 3, ADDPROP_NONE
    newDDR.DDRAddString "SMS Unique Identifier",
existingResource.SMSUniqueIdentifier, 64, ADDPROP_GUID OR ADDPROP_KEY
    newDDR.DDRAddStringArray "System Roles", existingResource.SystemRoles,
32, ADDPROP_NONE

    ' The new property that is being added.
    newDDR.DDRAddString "Organizational Unit", OrganizationalUnit, 64,
ADDPROP_NONE

     ' Write new DDR to file.
     newDDR.DDRWrite "NewDDR_AddToExistingResource.DDR"
     wscript.echo "Created new DDR."

End Sub

c#

public void
CreateDDRToAddNewPropertiesToAnExistingResourceType(WqlConnectionManager
connection)
{
    try
    {
        // Define and set the required variables.
        int resourceID = 5;
        string siteCode = "TQ1";
        string organizationalUnit = "Test OU";

          // Get a specific resource (client) object using the resourceID
value.
        IResultObject existingResource =
connection.GetInstance(@"SMS_R_SYSTEM.ResourceID='" + resourceID + "'");

          // Create the SMSResGenClass instance.
          SMSRSGENCTLLib.SMSResGen newDDR = new SMSRSGENCTLLib.SMSResGen();

          // Create a new DDR using the DDRNew method.
          newDDR.DDRNew("System", "Department Discovery", siteCode);

          // Add properties to the new DDR using the DDRAddInteger,

<!-- p.893 -->

DDRAddString and DDRAddStringArray methods.
        newDDR.DDRAddInteger("Client",
existingResource["Client"].IntegerValue,
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_NONE);
        newDDR.DDRAddString("Client
Version",existingResource["ClientVersion"].StringValue, 15,
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_NONE);
        newDDR.DDRAddStringArray("IP
Addresses",existingResource["IPAddresses"].StringArrayValue, 64,
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_NONE);
        newDDR.DDRAddStringArray("IP Subnets",
existingResource["IPSubnets"].StringArrayValue, 64,
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_NONE);
        newDDR.DDRAddString("Last Logon User
Domain",existingResource["LastLogonUserDomain"].StringValue, 255,
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_NONE);
        newDDR.DDRAddString("Last Logon User
Name",existingResource["LastLogonUserName"].StringValue, 64,
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_KEY);
        newDDR.DDRAddStringArray("MAC
Addresses",existingResource["MACAddresses"].StringArrayValue, 32,
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_NAME);
        newDDR.DDRAddString("NetBIOS
Name",existingResource["NetbiosName"].StringValue, 64,
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_NONE);
        newDDR.DDRAddString("Operating System Name and
Version",existingResource["OperatingSystemNameandVersion"].StringValue, 64,
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_NONE);
        newDDR.DDRAddStringArray("Resource
Names",existingResource["ResourceNames"].StringArrayValue, 128,
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_NONE);
        newDDR.DDRAddStringArray("SMS Installed
Sites",existingResource["SMSInstalledSites"].StringArrayValue, 3,
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_NONE);
        newDDR.DDRAddString("SMS Unique
Identifier",existingResource["SMSUniqueIdentifier"].StringValue, 64,
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_GUID |
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_KEY);
        newDDR.DDRAddStringArray("System
Roles",existingResource["SystemRoles"].StringArrayValue, 32,
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_NONE);

        // The new property that is being added.
        newDDR.DDRAddString("Organizational Unit", organizationalUnit, 64,
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_ARRAY |
SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_NONE);

       // Write new DDR to file.
       newDDR.DDRWrite("NewDDR_AddToExistingResource.DDR");
       Console.WriteLine("Created new DDR.");
    }
    catch (SmsException ex)
    {
        Console.WriteLine("Failed to create DDR. Error: " + ex.Message);
        throw;

<!-- p.894 -->

       }
  }

The example method has no parameters.

Compiling the Code

  ） Important

  This VBScript and C# examples require smsrsgen.dll and smsrsgenctl.dll,
  respectively. Both files are included as a part of the downloadable Configuration
  Manager SDK (in the "Redistributables" folder).

  The file smsrsgenctl.dll is a 32-bit dll and must be registered on the system that
  will run the application. In addition, the application using smsrsgenctl.dll should be
  compiled as an x86 application.

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.895 -->

How to Create a Data Discovery Record
Article • 10/04/2022

The data discovery record (DDR), in Configuration Manager, specifies the resource type,
the discovery process, the site that discovered the resource, and the resource properties.
Configuration Manager provides six library functions that you use to create your own
DDRs. For more information. see About Creating a Data Discovery Record.

To create a data discovery record
   1. Create a new instance of the SMSResGen class.

   2. Create a new DDR by using the NewDDR method.

   3. Add properties to the DDR by using the ADDPROP_ methods.

   4. Write the new DDR to a file by using the DDRWrite method.

Example
The following example creates a DDR.

  vbs

  Sub CreateNewDDR()

        ' Define constants.
        Const ADDPROP_NONE = &H0
        Const ADDPROP_GUID = &H2
        Const ADDPROP_KEY   = &H8
        Const ADDPROP_ARRAY = &H10

        ' Define variables.
        Dim newDDR
        Dim siteCode
        Dim computerName
        Dim siteName
        Dim newIPAddress(2), newIPSubnet(2), newMACAddress(2)

        ' Load variables with values.
        siteCode = "ABC"
        computerName="ComputerName"
        siteName="Active Directory Site Name"
        newIPAddress(0)="123.234.12.23"
        newIPAddress(1)="123.234.12.32"

<!-- p.896 -->

     newIPSubnet(0)="123.234.12.0"
     newIPSubnet(1)="123.234.12.0"
     newMACAddress(0)="00:02:A5:B1:11:68"
     newMACAddress(1)="00:02:A5:B1:11:69"

     ' Load an instance of the SMSResGen.dll.
     Set newDDR=CreateObject("SMSResGen.SMSResGen.1")

     ' Create a new DDR using the DDRNew method.
     newDDR.DDRNew "System", "CustomAgent", siteCode

    ' Add properties to the new DDR using the DDRAddString method and the
previously defined variables.
    newDDR.DDRAddString "NetBIOS Name", computerName, 64, ADDPROP_KEY
    newDDR.DDRAddString "AD Site Name", siteName, 64, ADDPROP_NONE

    ' Add properties to the new DDR using the DDRAddStringArray method and
the previously defined variables.
    newDDR.DDRAddStringArray "IP Addresses",
Array(newIPAddress(0),newIPAddress(1)), 64, ADDPROP_ARRAY
    newDDR.DDRAddStringArray "MAC Addresses",
Array(newMACAddress(0),newMACAddress(1)), 64, ADDPROP_ARRAY OR ADDPROP_KEY
    newDDR.DDRAddStringArray "IP Subnets",
Array(newIPSubnet(0),newIPSubnet(1)), 64, ADDPROP_ARRAY

     ' Write new DDR to file.
     newDDR.DDRWrite "NewDDR.DDR"
     wscript.echo "Created new DDR."

End Sub

c#

public void CreateNewDDR()
{
    try
    {
        // Define and set the required variables.
        string Computer = "ComputerName";
        string SiteName = "Active Directory Site Name";
        string[] IPAddress = new string[] { "123.234.12.23",
"123.234.12.32" };
        string[] IPSubnet   = new string[] { "123.234.12.0", "123.234.12.0"
};
        string[] MACAddress = new string[] { "00:02:A5:B1:11:68",
"00:02:A5:B1:11:68" };
        string siteCode = "TQ1";

          // Create the SMSResGenClass instance.
          SMSRSGENCTLLib.SMSResGen newDDR = new SMSRSGENCTLLib.SMSResGen();

<!-- p.897 -->

           // Create a new DDR using the DDRNew method.
           newDDR.DDRNew("System", "CustomAgent", siteCode);

          // Add properties to the new DDR using the DDRAddString method and
  the previously defined variables.
          newDDR.DDRAddString("NetBIOS Name", Computer, 64,
  SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_KEY);
          newDDR.DDRAddString("AD Site Name", SiteName, 64,
  SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_NONE);

          // Add properties to the new DDR using the DDRAddStringArray method
  and the previously defined variables.
          newDDR.DDRAddStringArray("IP Subnets", IPAddress, 64,
  SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_ARRAY);
          newDDR.DDRAddStringArray("MAC Addresses", MACAddress, 64,
  SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_ARRAY |
  SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_KEY);
          newDDR.DDRAddStringArray("IP Subnets", IPSubnet, 64,
  SMSRSGENCTLLib.DDRPropertyFlagsEnum.ADDPROP_ARRAY);

           // Write new DDR to file.
           newDDR.DDRWrite("NewDDR.DDR");
           Console.WriteLine("Created new DDR.");
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to create DDR. Error: " + ex.Message);
          throw;
      }
  }

Compiling the Code

  ） Important

  This VBScript and C# examples require smsrsgen.dll and smsrsgenctl.dll,
  respectively. Both files are included as a part of the downloadable Configuration
  Manager SDK (in the "Redistributables" folder).

  The file smsrsgenctl.dll is a 32-bit dll and must be registered on the system that will
  run the application. In addition, the application using smsrsgenctl.dll should be
  compiled as an x86 application.

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

<!-- p.898 -->

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See also
SMSResGen COM Automation Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.899 -->

About Configuration Manager Inventory
Article • 10/10/2022

You can use Configuration Manager to collect hardware and software inventory from
Configuration Manager clients by enabling the client agents on a site-by-site basis.

When the hardware inventory client agent is enabled for Configuration Manager sites,
hardware inventory data gives you system information (such as available disk space,
processor type, and operating system) about each computer. When the software
inventory client agent is enabled, you can inventory information, such as the specific file
types and versions that are present on client computers. The software inventory client
agent can also collect information about files that are inventoried on client systems.
Configuration Manager software inventory can also collect files, not just details about
the files, from client computers. With file collection, you specify a set of files to be
copied from clients to the Configuration Manager site server that the clients are
assigned to.

  ７ Note

  For more information, see Introduction to hardware inventory.

About Collecting Hardware Inventory
When it's enabled, the Configuration Manager hardware inventory client agent
automatically collects detailed information about the hardware characteristics of clients
in a Configuration Manager site. By using this feature, you can collect a wide variety of
information about client computers, such as memory, operating system, and peripherals
for client computers.

The hardware inventory feature collects data from client computers by querying several
data stores on client computers, such as the registry and Windows Management
Instrumentation (WMI) namespace classes. The hardware inventory client agent doesn't
query for all possible WMI classes, but it does provide the ability to report on
approximately 1,500 hardware properties from almost 100 different WMI classes, by
default.

About Collecting Software Inventory

<!-- p.900 -->

When it's enabled, the Configuration Manager software inventory client agent can
collect software inventory data directly from files (such as .exe files) by inventorying the
file header information. Configuration Manager can also inventory unknown files—files
that don't have detailed information in their file headers. This provides a flexible, easy-
to-maintain software inventory method. You can also have Configuration Manager
collect copies of files that you specify. You can view software inventory and collected file
information for a client by using Resource Explorer.

About NOIDMIF and IDMIF Files
Management Information Format (MIF) files can be used to extend hardware inventory
information that is collected from clients by the Configuration Manager hardware
inventory client agent. During hardware inventory, the information that is stored in MIF
files is added to the client inventory report and stored in the site database, where you
can use the data in the same ways that you use default client inventory data. Two MIF
files can be used when performing client hardware inventories: NOIDMIF and IDMIF.

By default, NOIDMIF and IDMIF file information isn't inventoried by Configuration
Manager sites. To enable NOIDMIF and IDMIF file information to be inventoried,
NOIDMIF and IDMIF collection must be enabled. You can choose to enable one or both
types of MIF file collection for Configuration Manager sites on the MIF Collection tab of
the hardware inventory client agent properties.

  ） Important

  Before you can add information from MIF files to the Configuration Manager
  database, you must create or import class information for them. For more
  information, see the sections To add a new inventory class and To import
  hardware inventory classes in How to Extend Hardware Inventory in
  Configuration Manager.

NOIDMIF Files
Standard MIF files that are used in Configuration Manager hardware inventory are called
NOIDMIF files. NOIDMIF files don't contain a unique identifier for the data.
Configuration Manager automatically associates NOIDMIF file data with the client that
the NOIDMIF file is collected from when reporting inventory information.

  ７ Note

<!-- p.901 -->

  NOIDMIF files themselves are not sent to the site server during a client hardware
  inventory cycle. The information that is contained within the NOIDMIF file is
  collected and added to the client inventory report.

If the classes defined in an inventoried NOIDMIF file don't already exist in the
Configuration Manager site database, new inventory class tables are created in the site
database to store the inventoried information. Subsequent inventories will inventory the
data stored in the NOIDMIF file and update the existing inventory data for the client in
the site database. If the NOIDMIF file is removed from the client, all the classes and
properties relating to the NOIDMIF file are deleted from the current inventory
information for the client in the site database.

For NOIDMIF file information to be inventoried by default, the NOIDMIF file must be
stored in the following directory on Configuration Manager clients:

%Windir%\System32\CCM\Inventory\Noidmifs

IDMIF Files
Custom MIF files, called IDMIF files, can also be used in Configuration Manager
hardware inventory. IDMIF files contain a unique ID and aren't associated with the
computer they're collected from. IDMIF files can be used to collect inventory data about
devices that aren't Configuration Manager clients; for example, a shared network printer,
DVD player, photocopier, or similar equipment that isn't associated with a client-specific
computer.

When IDMIF collection is enabled for a site, IDMIF files are collected only if they are
within the size limit that is specified for custom MIF files defined in the General tab of
the hardware inventory client agent properties.

  ） Important

  Because IDMIF files are not associated with a Configuration Manager client, they
  are collected by the hardware inventory client agent and sent to the site server
  along with the client hardware inventory report. Depending on the maximum
  custom MIF size specified for the site, IDMIF collection might cause increased
  network bandwidth usage during client inventories and should be planned for
  before enabling IDMIF file collection.

IDMIF files are identical to NOIDMIF files, with these exceptions:

<!-- p.902 -->

     IDMIF files must have a delta header that provides architecture, and a unique ID.
     NOIDMIF files are automatically given a similar header by the system during
     processing on the client.

     IDMIF files must include a top-level group with the same class as the architecture
     being added or changed, and that group must include at least one property.

     Like NOIDMIF files, IDMIF files have key properties that must be unique. Any class
     that has more than one instance must have at least one key property defined, or
     subsequent instances overwrite previous instances.

     Removing IDMIF files from clients doesn't cause the associated data in the site
     database to be deleted during subsequent hardware inventories.

     IDMIF file information isn't added to client inventory reports and sent as MIF files
     across the network to be processed at the site server.

     For IDMIF file information to be inventoried by default, the IDMIF file must be
     stored in the following directory on Configuration Manager clients:

     %Windir%\System32\CCM\Inventory\Idmifs

See Also
Configuration Manager Software Development Kit
Initiate Asset Intelligence synchronization

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.903 -->

How to Enable Hardware Inventory
Article • 10/10/2022

You enable or disable the Hardware Inventory Client Agent, in Configuration Manager,
by modifying the site control file settings.

To enable or disable the Hardware Inventory Client Agent
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Hardware Inventory Client Agent section of the site
        control file by using the SMS_SCI_ClientComp class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

Example
The following example method enables or disables the Hardware Inventory Client Agent
by using the SMS_SCI_ClientComp class to connect to the site control file and change
properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub EnableDisableHardwareInventoryClientAgent(swbemServices, swbemContext,
  siteCode, enableDisableFlag)

      ' Load site control file and get hardware inventory client client agent
  section.
      swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteCode & """", "Refresh", , , swbemContext
      Set objSWbemInst =
  swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
  Component',Sitecode='" & siteCode & "',ItemName='Hardware Inventory Agent'",
  , swbemContext)

         ' Display client agent settings before changing the properties.
         Wscript.Echo " "
         Wscript.Echo "Properties - Before Change"
         Wscript.Echo "---------------------------"
         Wscript.Echo objSWbemInst.ClientComponentName

<!-- p.904 -->

     Wscript.Echo objSWbemInst.Flags & " (0 = Disabled, 1 = Enabled)"

    ' Set client agent by setting the Flags value to     0 or 1 using the
enableDisableFlag variable.
    objSWbemInst.Flags = enableDisableFlag

    ' Save the new client agent settings.
    objSWbemInst.Put_ , swbemContext
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Commit", , , swbemContext

    ' Refresh in-memory copy of the site control file and get the client
component section.
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Refresh", , , swbemContext
    Set objSWbemInst =
swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
Component',Sitecode='" & siteCode & "',ItemName='Hardware Inventory Agent'",
, swbemContext)

     ' Display the client agent settings after change.
     Wscript.Echo " "
     Wscript.Echo "Properties - After Change"
     Wscript.Echo "---------------------------"
     Wscript.Echo objSWbemInst.ClientComponentName
     Wscript.Echo objSWbemInst.Flags & " (0 = Disabled, 1 = Enabled)"

End Sub

c#

public void EnableDisableHardwareInventoryClientAgent(WqlConnectionManager
connection,
                                                      string siteCode,
                                                      string
enableDisableFlag)

{
     try
     {
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
Component',SiteCode='" + siteCode + "',ItemName='Hardware Inventory
Agent'");

           // Display client agent settings before changing the properties.
           Console.WriteLine();
           Console.WriteLine("Properties - Before Change");
           Console.WriteLine("---------------------------");

Console.WriteLine(siteDefinition["ClientComponentName"].StringValue);

<!-- p.905 -->

          Console.WriteLine(siteDefinition["Flags"].StringValue + " (0 =
  Disabled, 1 = Enabled)");

          // Set client agent by setting "Flags" value to 0 or 1 by using the
  enableDisableFlag variable.
          siteDefinition["Flags"].StringValue = enableDisableFlag;

             // Save the settings.
             siteDefinition.Put();

          // Verify the change by reconnecting and getting the value again.
          IResultObject siteDefinition2 =
  connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
  Component',SiteCode='" + siteCode + "',ItemName='Hardware Inventory
  Agent'");

             // Display client agent settings after changing the properties.
             Console.WriteLine();
             Console.WriteLine("Properties - After Change");
             Console.WriteLine("--------------------------");

  Console.WriteLine(siteDefinition2["ClientComponentName"].StringValue);
          Console.WriteLine(siteDefinition2["Flags"].StringValue + " (0 =
  Disabled, 1 = Enabled)");
      }

       catch (SmsException ex)
       {
           Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
           throw;
       }

  }

The example method has the following parameters:

                                                                             ﾉ   Expand table

 Parameter          Type                       Description

 - connection       - Managed:                 A valid connection to the SMS Provider.
 - swbemServices     WqlConnectionManager
                    - VBScript:
                    SWbemServices

 swbemContext       - VBScript: SWbemContext   A valid context object. For more information,
                                               see How to Add a Configuration Manager
                                               Context Qualifier by Using WMI.

 siteCode           - Managed: String          The site code.
                    - VBScript: String

<!-- p.906 -->

 Parameter           Type                  Description

 enableDisableFlag   - Managed: String     Determines whether the Hardware Inventory
                     - VBScript: String    client agent is enabled or disabled.

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Configuration Manager Software Development Kit
About Configuration Manager Inventory
About the Configuration Manager Site Control File

<!-- p.907 -->

How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.908 -->

How to Configure Hardware Inventory
Settings
Article • 10/10/2022

You set the Hardware Inventory Client Agent settings, in Configuration Manager, by
modifying the necessary site control file settings.

To modify the Hardware Inventory Client Agent settings
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Hardware Inventory Client Agent section of the site
        control file by using the SMS_SCI_ClientComp class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

Example
The following example sets the Hardware Inventory Client Agent settings by using the
SMS_SCI_ClientComp class to connect to the site control file and change properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ConfigureHardwareInventoryClientAgentSettings(swbemServices,        _
                                                    swbemContext,         _
                                                    siteCode,             _
                                                    newInventorySchedule, _
                                                    newMIFSize,           _
                                                    newMIFCollection)

      ' Load site control file and get the SMS Software Update Point system
  resource section.
      swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteCode & """", "Refresh", , , swbemContext

         Query = "SELECT * FROM SMS_SCI_ClientComp " & _
         "WHERE ClientComponentName = 'Hardware Inventory Agent' " & _
         "AND SiteCode = '" & siteCode & "'"

<!-- p.909 -->

    Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

    ' Only one instance is returned from the query.
    For Each SCIComponent In SCIComponentSet

        ' Set the client agent by setting the Flags value to 0 or 1 using
the enableDisableClientAgent variable.
        wscript.echo " "
        wscript.echo "Hardware Inventory Agent"
        wscript.echo "Current value " & SCIComponent.Flags

       ' Modify the value.
       SCIComponent.Flags = enableDisableClientAgent
       wscript.echo "New value " & enableDisableClientAgent

       'Loop through the array of embedded SMS_EmbeddedProperty instances.
       For Each vProperty In SCIComponent.Props

              ' Setting: Inventory Schedule
              If vProperty.PropertyName = "Inventory Schedule" Then
                  wscript.echo " "
                  wscript.echo vProperty.PropertyName
                  wscript.echo "Current value " & vProperty.Value2

                  'Modify the value.
                  vProperty.Value2 = newInventorySchedule
                  wscript.echo "New value " & newInventorySchedule
              End If

              ' Setting: Maximum 3rd Party MIF Size
              If vProperty.PropertyName = "Maximum 3rd Party MIF Size" Then
                  wscript.echo " "
                  wscript.echo vProperty.PropertyName
                  wscript.echo "Current value " & vProperty.Value

                  ' Modify the value.
                  vProperty.Value = newMIFSize
                  wscript.echo "New value " & newMIFSize
              End If

              ' Setting: MIF Collection
              If vProperty.PropertyName = "MIF Collection" Then
                  wscript.echo " "
                  wscript.echo vProperty.PropertyName
                  wscript.echo "Current value " & vProperty.Value

                  ' Modify the value.
                  vProperty.Value = newMIFCollection
                  wscript.echo "New value " & newMIFCollection
              End If

       Next

       ' Update the component in your copy of the site control file. Get

<!-- p.910 -->

the path
        'to the updated object, which could be used later to retrieve the
instance.
        Set SCICompPath = SCIComponent.Put_(wbemChangeFlagUpdateOnly,
swbemContext)

     Next

    ' Commit the change to the actual site control file.
    Set InParams =
swbemServices.Get("SMS_SiteControlFile").Methods_("CommitSCF").InParameters.
SpawnInstance_
    InParams.SiteCode = siteCode
    swbemServices.ExecMethod "SMS_SiteControlFile", "CommitSCF", InParams, ,
swbemContext

End Sub

c#

public void
ConfigureHardwareInventoryClientAgentSettings(WqlConnectionManager
connection,
                                                    string siteCode,
                                                    string
enableDisableClientAgent,
                                                    string
newInventorySchedule,
                                                    string newMIFSize,
                                                    string newMIFCollection)
{
    try
    {
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
Component',SiteCode='" + siteCode + "',ItemName='Hardware Inventory
Agent'");

        // Setting: Enable Client Agent
        // Enable or disable the client agent by setting the Flags value to
0 or 1 using the enableDisableClientAgent variable.
        Console.WriteLine();
        Console.WriteLine("Hardware Inventory Client Agent");
        Console.WriteLine("Current value: " +
siteDefinition["Flags"].StringValue);

          // Change value using the enableDisableClientAgent value passed in.
          siteDefinition["Flags"].StringValue = enableDisableClientAgent;
          Console.WriteLine("New value    : " + enableDisableClientAgent);

        foreach (KeyValuePair<string, IResultObject> kvp in
siteDefinition.EmbeddedProperties)

<!-- p.911 -->

       {
            // Create temporary working copy of embedded properties.
            Dictionary<string, IResultObject> embeddedProperties =
siteDefinition.EmbeddedProperties;

             // Setting: Inventory Schedule
             if (kvp.Value.PropertyList["PropertyName"] == "Inventory
Schedule")
             {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
kvp.Value.PropertyList["PropertyName"]);

                 // Change value using the newInventorySchedule value passed
in.
                embeddedProperties["Inventory Schedule"]
["Value2"].StringValue = newInventorySchedule;
                Console.WriteLine("New value    : " + newInventorySchedule);
            }

             // Setting: Maximum 3rd Party MIF Size
             if (kvp.Value.PropertyList["PropertyName"] == "Maximum 3rd Party
MIF Size")
             {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
kvp.Value.PropertyList["PropertyName"]);

                // Change value using the newMIFSize value passed in.
                embeddedProperties["Maximum 3rd Party MIF Size"]
["Value"].StringValue = newMIFSize;
                Console.WriteLine("New value    : " + newMIFSize);
            }

            // Setting: MIF Collection
            if (kvp.Value.PropertyList["PropertyName"] == "MIF Collection")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
kvp.Value.PropertyList["PropertyName"]);

                // Change value using the newMIFCollection value passed in.
                embeddedProperties["MIF Collection"]["Value"].StringValue =
newMIFCollection;
                Console.WriteLine("New value    : " + newMIFCollection);
            }

             // Store the settings that have changed.
             siteDefinition.EmbeddedProperties = embeddedProperties;
       }

       // Save the settings.

<!-- p.912 -->

              siteDefinition.Put();

       }

       catch (SmsException ex)
       {
           Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
           throw;
       }

  }

The example method has the following parameters:

                                                                               ﾉ   Expand table

 Parameter                  Type                       Description

 - connection               - Managed:                 A valid connection to the SMS Provider.
 - swbemServices            WqlConnectionManager
                            - VBScript:
                            SWbemServices

 swbemContext               - VBScript: SWbemContext   A valid context object. For more
                                                       information, see How to Add a
                                                       Configuration Manager Context Qualifier
                                                       by Using WMI.

 siteCode                   - Managed: String          The site code.
                            - VBScript: String

 enableDisableClientAgent   - Managed: String          A value to enable or disable the client
                            - VBScript: String         agent.

                                                       Disabled - 0

                                                       Enabled - 1

 newInventorySchedule       - Managed: String          A value to set the inventory schedule.
                            - VBScript: String

 newMIFSize                 - Managed: String          A value to set the maximum size of the
                            - VBScript: String         hardware inventory MIF.

                                                       Default is 512.

 newMIFCollection           - Managed: String          A value to enable or disable MIF
                            - VBScript: String         collection.

<!-- p.913 -->

 Parameter                  Type                   Description

                                                   Collect:

                                                   No (MIF) files - 0

                                                   NOIDMIF files - 4

                                                   IDMIF files - 8

                                                   Both NOIDMIF and IDMIF files - 12

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

<!-- p.914 -->

See Also
About Configuration Manager Inventory
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class
About schedules How to Create a Schedule Token

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.915 -->

Requirements of IDMIF files
Article • 10/10/2022

Two delta header comments are required for an IDMIF file. Other comments are
optional. The comments you must include are:

      The name of the architecture you want to create or modify:
      //Architecture<ArchitectureName>

      A unique ID for this instance: //UniqueID<UniqueID>

The unique ID can be any unique ID. Each architecture has one or more instances within
the SMS site database. The unique ID is the key for this specific instance.

Also, although it is not required, you should use the agent name, especially with a large
or complicated custom MIF file that might be updated by more than one agent:
//AgentID<AgentName>

If you do not include this attribute, hardware inventory might overwrite the information
your IDMIF file places in the SMS site database.

The agent name enables you to independently create and modify the System
architecture. Others who modify the architecture can use a different agent name. They
can then remove or modify the parts of the architecture that are associated with that
agent, independently of the modifications of other agents.

There is another requirement of any IDMIF file. Whenever you create an IDMIF file, you
must include a group within the IDMIF file with the same class name as the architecture
you are creating or modifying. This group is known as the top-level group.

Also, if you create any class that has more than one instance, you must include at least
one key value within the class, to avoid having each instance overwrite previous
instances.

  ） Important

  The formatting of the comments must be exactly the same as that given here. The
  only part that you can change is the part in italics. The < and > characters must be
  included.

IDMIF files must be stored in the following folder on Advanced Clients:
%Windir%\System32\CCM\Inventory\Idmifs

<!-- p.916 -->

IDMIF files must be stored in the following folder on Legacy Clients:
%Windir%\MS\SMS\Idmifs

The safest method on both clients is to use the folder the following registry key points
to:

HKLM\Software\Microsoft\SMS\Client\Configuration\Client Properties\IDMIF
Directory

The following is an example of a simple IDMIF file:

  //Architecture<System>
  //UniqueID<3b93b13a-afb4-40cf-86d4-3ad1aaaa8414>

  Start Component
      Name = "Workstation"
      Start Group
          Name = "System"
          ID = 1
          Class = "System"
          Key = 1,2,3
              Start Attribute
                  Name = "Name"
                  ID = 1
                  Access = READ-ONLY
                  Storage = Specific
                  Type = String(255)
                  Value = "MachineName8d16380a-3928-4ef1-b4f3-fdc557d4af9b"
              End Attribute
              Start Attribute
                  Name = "SMSID"
                  ID = 2
                  Access = READ-ONLY
                  Storage = Specific
                  Type = String(255)
                  Value = "8d16380a-3928-4ef1-b4f3-fdc557d4af9b"
              End Attribute
              Start Attribute
                  Name = "SystemType"
                  ID = 3
                  Access = READ-ONLY
                  Storage = Specific
                  Type = String(255)
                  Value = "Test Type"
              End Attribute
      End Group

<!-- p.917 -->

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Configuration Manager Software Development Kit
About Configuration Manager Inventory
How to Configure Hardware Inventory Settings

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.918 -->

How to Reset the Hardware Inventory
Cache
Article • 10/10/2022

In Configuration Manager, you reset the hardware inventory cache by connecting to the
inventory agent namespace and deleting the inventory action status instance for
hardware inventory.

To reset the hardware inventory cache
   1. Connect to the inventory agent namespace (root\ccm\invagt).

   2. Delete the inventory action status instance for hardware inventory ({00000000-
        0000-0000-0000-000000000001}).

Example
The following example method shows how to reset the hardware inventory cache by
connecting to the inventory agent namespace and deleting the inventory action status
instance for hardware inventory.

For information about calling the sample code, see How to Call a Configuration
Manager Object Class Method by Using WMI

  vbs

  Sub ResetHardwareInventoryCache()

          ' Get a connection to the "root\ccm\invagt" namespace.
         Dim locator
         Set locator = CreateObject("WbemScripting.SWbemLocator")
         Dim services
         Set services = locator.ConnectServer( , "root\ccm\invagt")

      ' Delete the specified InventoryActionStatus instance.
      services.Delete "InventoryActionStatus.InventoryActionID='{00000000-
  0000-0000-0000-000000000001}'"

         ' Display message.
         wscript.echo "Reset Hardware Inventory cache."

  End Sub

<!-- p.919 -->

  c#

  // How to Reset the Hardware Inventory Cache
  public void ResetHardwareInventoryCache()
  {
      try
      {
          // Define the scope (namespace).
          ManagementScope inventoryAgentScope = new
  ManagementScope(@"root\ccm\invagt");

          // Load the class that you want to work with.
          ManagementClass inventoryClass = new
  ManagementClass(inventoryAgentScope.Path.Path, "InventoryActionStatus",
  null);

          // Query the class for the InventoryActionID object (create query,
  create searcher object, execute query).
          ObjectQuery query = new ObjectQuery("SELECT * FROM
  InventoryActionStatus WHERE InventoryActionID = '{00000000-0000-0000-0000-
  000000000001}'");
          ManagementObjectSearcher searcher = new
  ManagementObjectSearcher(inventoryAgentScope, query);
          ManagementObjectCollection queryResults = searcher.Get();

          // Enumerate the collection to get to the result (there should only
  be one item returned from the query).
          foreach (ManagementObject result in queryResults)
          {
              // Display message and delete the object.
              Console.WriteLine("Resetting Hardware Inventory cache.");
              result.Delete();
          }
      }

       catch (System.Management.ManagementException ex)
       {
           Console.WriteLine("Failed to run action. Error: " + ex.Message);
           throw;
       }
  }

Compiling the Code
This C# example requires:

Namespaces

<!-- p.920 -->

System.Management

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Configuration Manager Software Development Kit
About Configuration Manager Inventory

Feedback
Was this page helpful?      Yes    No

Provide product feedback
