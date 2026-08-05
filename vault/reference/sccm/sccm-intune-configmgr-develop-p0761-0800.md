---
title: "Configuration Manager SDK documentation — pages 761-800"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0761-0800
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0761-0800
family: sccm
documentKind: "doc"
abstract: "If the form is an extension of an existing property sheet, you must determine whether the property sheet already exists in the Extensions\\Forms folder, then add your property page to that property sheet. When the Configuration Manager console loads, it loads property sheets in t"
---

# Configuration Manager SDK documentation — pages 761-800

<!-- p.761 -->

If the form is an extension of an existing property sheet, you must determine whether
the property sheet already exists in the Extensions\Forms folder, then add your property
page to that property sheet.

When the Configuration Manager console loads, it loads property sheets in the
Extensions\Forms folder in preference to existing property sheets.

You should use the VendorId attribute of the Page element, because this allows other
vendors to identify and avoid changing your extensions.

Removing a Form
To remove a form that does not extend an existing property sheet, remove the property
sheet XML file from the folder %ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\XmlStorage\Extensions\Forms.

To remove a property page that you have added to an existing property sheet, you must
take the following actions with the property sheet:

     Check the property pages for VendorIDs other than Microsoft Corporation. If none
     exist then it is safe to delete the property sheet XML file from the
     Extensions\Forms folder.

     If other VendorIDs exist, remove your property page XML from the property sheet,
     and leave the property sheet in the Extensions\Forms folder.

Views

Installing a View
To install a view, copy the view assembly to the %ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\bin folder, or to your application's installation folder.

If you are deploying to a folder other than %ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\bin, the node XML< Assembly > element should include the
assembly filename and the full path to the file. For more information, see How to Create
Node XML for a Configuration Manager Console View.

You must also copy the node XML that integrates the view into the Configuration
Manager console to the %ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\XmlStorage\Extensions\Nodes\<GUID folder>, where <GUID>

<!-- p.762 -->

is the GUID identifier for the node that the action applies to. For more information, see
the "Nodes" section later in this topic.

Removing a View
To remove a view, delete the view assembly from the %ProgramFiles%\Microsoft
Endpoint Manager\AdminConsole\bin folder. You must ensure that no other extension is
referencing the view before you delete it. You must also delete the view's node XML file
from the %ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\XmlStorage\Extensions\Nodes\<GUID> folder, where <GUID>
is the GUID identifier for the node that the action applies to.

Custom Management Classes

Installing a Custom Management Class
Copy the management class assembly to either %ProgramFiles%\ Microsoft Endpoint
Manager\AdminConsole\bin or to your application's installation folder.

To install a custom management class XML file, copy the file to the
%ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\XmlStorage\Extensions\ManagementClasses folder. Because all
custom management classes are placed in this folder, you must ensure that your XML
file has a unique name. It is suggested that you use your company name as part of the
file name.

Removing a Custom Management Class
To remove a custom management class, delete the custom management class XML file.
If there are no other XML files in the folder then it is safe to remove the folder.

Nodes

Installing a Node
To install a node, create a folder %ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\XmlStorage\Extensions\Nodes\<GUID> , where <GUID> is the
GUID identifier of the Configuration Manager console parent node. Copy the node XML
file to the GUID folder. For more information, see About console nodes.

<!-- p.763 -->

Removing a Node
To remove a node, delete the node XML file from the %ProgramFiles%\Microsoft
Endpoint Manager\AdminConsole\XmlStorage\Extensions\Nodes\<GUID> folder.

See Also
About Configuration Manager Console Extension
About Configuration Manager console actions About console forms About console
management classes About console nodes About console views

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.764 -->

Console extension registration though
community hub
Article • 10/04/2022

Console extension authors can contribute extensions they've written to the community
hub. Community hub users can download the extensions and manage the installation of
them across their Configuration Manager hierarchy. Contributing extensions through
Community hub supersedes the previous deployment process.

Version information
To download console extensions from the Community hub, you'll need either:

      A technical preview version of Configuration Manager
      Configuration Manager version 2103 or later

You can test your own signed extensions by importing them locally with the following
versions:

      A technical preview version of Configuration Manager
      Configuration Manager version 2103 or later

You can import an unsigned extension locally. Unsigned extensions are for local import
and testing purposes only. Unsigned extensions can't be submitted to Community hub.
Importing an unsigned extension requires one of the following versions:

      Technical preview version 2105.2 or later.
      Configuration Manager version 2107 or later

Starting in version 2111, you can import both signed and unsigned extensions using the
Import Console Extension wizard.

Prerequisites
To register a console extension in the community hub for Configuration Manager
admins to download, you'll need the following prerequisites:

      Meet all of the prerequisites for contributing to community hub

      Configuration Manager Full Administrator with All scope rights.

<!-- p.765 -->

     A valid payload in an authenticode-signed .cab file once you're ready to publish.
     Your .cab file must contain the following items:
        A manifest file named manifest.xml
        The author and version of the extension must be listed in the manifest.xml
        All relevant files for the extension must be in the .cab file
             Each file must be listed in the manifest and have the correct name and
             SHA256 hash

Create an extension
Creating your extension for community hub isn't much different from how it was done
previously. However, there's no longer a need to install the files in their respective
%ProgramFiles%\Microsoft Endpoint Manager\AdminConsole\XmlStorage\Extensions folder.
This is part of the function of the new manifest.xml file. You can still create the
following items:

     Actions
     Forms
     Management classes
     Nodes
     Views
     Integrate your own custom wizards into the Configuration Manager console by
     using a wizard framework of your choice
        You can't create wizards by using the existing Configuration Manager console
        framework.
        You can't modify or remove steps from the existing Configuration Manager
        wizards.

   Tip

  From community hub's GitHub repository, you can download a sample extension's
  cab file    .

Create a valid payload cab file
Once you have the files for your extension created, you'll create the manifest.xml file,
then package them all together in an authenticode-signed .cab file.

<!-- p.766 -->

     A valid payload in an authenticode-signed .cab file. Your .cab file must contain
     the following items:
        A manifest file named manifest.xml
        The author and version of the extension must be listed in the manifest.xml
        All relevant files for the extension must be in the .cab file
           Each file must be listed in the manifest and have the correct name and
           SHA256 hash

Manifest.xml format:

  XML

  <CustomExtensionManifest ExtensionID="{A GUID to identify this extension}"
  Name="{Name of the extension to be shown in the Console Extension node}"
  Description="{Description of the extension to be shown in the Console
  Extension node" Version="{The version of the extension to be shown in the
  Console Extension node. For example:1.0}" Author="{The author of the
  extension to be shown in the Console Extension node}">
      <Deployments>
          <ActionExtensionDeployment ParentNode="{the GUID that identify the
  folder/node you want to place the action under}">
              <FileList>
                  <File Name="{The name of the xml file that defines the
  action. For example: MyAction.xml}">
                      <Hash Algorithm="sha256">{The SHA256 hash of this file}
  </Hash>
                  </File>
              </FileList>
          </ActionExtensionDeployment>
          <NodeExtensionDeployment ParentNode="{the GUID that identify the
  folder you want to place the node under}">
              <FileList>
                  <File Name="{The name of the xml file that defines the node.
  For example: MyNode.xml}">
                      <Hash Algorithm="sha256">{The SHA256 hash of this file}
  </Hash>
                  </File>
              </FileList>
          </NodeExtensionDeployment>
          <FormExtensionDeployment>
              <FileList>
                  <File Name="{The name of the xml file that defines the form.
  For example: MyForm.xml}">
                      <Hash Algorithm="sha256">{The SHA256 hash of this file}
  </Hash>
                  </File>
                  <File Name="{The name of the dll file that defines the form.
  For example: MyForm.dll}">
                      <Hash Algorithm="sha256">{The SHA256 hash of this file}
  </Hash>
                  </File>

<!-- p.767 -->

              </FileList>
          </FormExtensionDeployment>
          <ManagementClassExtensionDeployment>
              <FileList>
                  <File Name="{The name of the xml file that defines the WMI
  class. For example: MyClass.xml}">
                      <Hash Algorithm="sha256">{The SHA256 hash of this file}
  </Hash>
                  </File>
                  <File Name="{The name of the dll file that defines the WMI
  class. For example: MyClass.dll}">
                      <Hash Algorithm="sha256">{The SHA256 hash of this file}
  </Hash>
                  </File>
              </FileList>
          </ManagementClassExtensionDeployment>
          <ViewExtensionDeployment>
              <FileList>
                  <File Name="{The name of the dll file that defines the view.
  For example: MyView.dll}">
                      <Hash Algorithm="sha256">{The SHA256 hash of this file}
  </Hash>
                  </File>
              </FileList>
          </ViewExtensionDeployment>
          <CabExtensionDeployment>
              <FileList>
                  <File Name="{The name of the cab file to deploy.
  CabExtensionDeployment is used when your payload cab file contains a cab
  within it that needs to be deployed. For example: MyCab.cab}">
                      <Hash Algorithm="sha256">{The SHA256 hash of this file}
  </Hash>
                  </File>
              </FileList>
          </CabExtensionDeployment>
      </Deployments>
  </CustomExtensionManifest>

Example manifest.xml file:

  XML

  <CustomExtensionManifest ExtensionID="808b9ce3-e574-49be-82be-64ed35d800c5"
  Name="Nice Console Node and Console Action Extension" Description="Very
  Useful Extension" Version="1.1" Author="Me">
      <Deployments>
          <NodeExtensionDeployment ParentNode="d61498cb-7b3f-4748-ae3e-
  026674fb0cbd">
              <FileList>
                  <File Name="Test.xml">
                      <Hash
  Algorithm="sha256">543F2947AEA734B6833F275091AC6A159C0FCD341373D6E53062E3728
  1B602B3</Hash>

<!-- p.768 -->

                  </File>
              </FileList>
          </NodeExtensionDeployment>
        <ActionExtensionDeployment ParentNode="172d85e7-bb7a-4479-a6a2-
  768f175b75cb">
          <FileList>
            <File Name="Test2.xml">
              <Hash
  Algorithm="sha256">C60FB69B86BF9B2E924FF272292CA2C97864D636B8190C95DC9260496
  51A002E</Hash>
            </File>
          </FileList>
        </ActionExtensionDeployment>
      </Deployments>
  </CustomExtensionManifest>

Register the extension to a site for testing
When you have your extension built and packaged into an authenticode-signed .cab
file, you can test it in a Configuration Manager lab environment. You'll do this by posting
it through the administration service. Once the extension is inserted into the site, you
can approve it and install it locally from the Console Extensions node.

  ） Important

  For local testing, you can import unsigned console extensions when you use
  version 2107 or later. For more information and additional import methods, see
  Import console extensions.

   1. Run the following PowerShell script after editing the $adminServiceProvider and
     $cabFilePath :

           $adminServiceProvider - The top-level SMSProvider server where the

           administration service is installed
           $cabFilePath - Path to the extension's authenticode-signed .cab file

        PowerShell

        $adminServiceProvider = "SMSProviderServer.contoso.com"
        $cabFilePath = "C:\Testing\MyExtension.cab"
        $adminServiceURL =
        "https://$adminServiceProvider/AdminService/v1/ConsoleExtensionMetadata
        /AdminService.UploadExtension"
        $cabFileName = (Get-Item -Path $cabFilePath).Name
        $Data = Get-Content $cabFilePath
        $Bytes = [System.IO.File]::ReadAllBytes($cabFilePath)

<!-- p.769 -->

        $base64Content = [Convert]::ToBase64String($Bytes)

        $Headers = @{
            "Content-Type" = "Application/json"
        }

        $Body = @{
                     CabFile = @{
                         FileName = $cabFileName
                         FileContent = $base64Content
                     }
                 } | ConvertTo-Json

        $result = Invoke-WebRequest -Method Post -Uri $adminServiceURL -Body
        $Body -Headers $Headers -UseDefaultCredentials

        if ($result.StatusCode -eq 200) {Write-Host "$cabFileName was published
        successfully."}
        else {Write-Host "$cabFileName publish failed. Review AdminService.log
        for more information."}

   2. In the Configuration Manager console, go to Administration > Overview >
     Updates and Servicing > Console Extensions.

   3. Select your extension, then choose Approve Installation.

   4. To install the extension on the current console, select Install under Local Extension.

   5. Rerunning the PowerShell script with the same extension and the same version will
     overwrite the current existing one.

Share your extension on community hub
Applies only to technical preview versions of Configuration Manager

Make sure you've joined the community hub and that you've accepted the invite after
your join request is approved. You contribute extensions the same way you would
contribute other community hub objects. However, for there are additional
requirements and additional information you need to supply for an extension. When
you contribute a console extension to Community hub, the content must be signed.
Content for console extensions isn't hosted by Microsoft. When you contribute your
item, you'll be asked to provide a location to the signed .cab file along with other
information for the extension. The following items are required for contributing
extensions:

     Content URL: Location for the downloadable .cab file
     SHA-256 hash of the content: SHA-256 hash of the .cab file

<!-- p.770 -->

     License URL: URL of the license for the extension, such as https://mit-license.org/
     Privacy statement URL: URL of your privacy statement

  ） Important

  If you import an extension locally into the console by posting it through the
  administration service, the download will fail if you attempt to download the same
  extension from the Community hub. To test the download of your extension from
  Community hub, delete the imported extension and then download from
  Community hub.

Next steps
     Contribute to community hub
     Use the community hub
     Import console extensions

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.771 -->

Configuration Manager Actions
Article • 10/04/2022

Configuration Manager console actions are tasks or commands that are performed by
making context menu or action panel selections. There are a number of standard action
types such as cut, paste, and properties. You can also add your own custom actions to
perform tasks such as running programs and displaying dialog boxes. You can restrict
the availability of actions to such criteria as regular expressions, security permissions,
and method call results.

In the Configuration Manager console, actions are defined in XML by the
ActionDescription element.

Standard Actions
A custom action can be associated with several standard actions. For example, a
ShowDialog action can be associated with a Properties standard action. In this case, a

property page is integrated into the properties property sheet for a selected object.

The standard actions are:

      Delete

      Refresh

      Properties

Custom Actions
You can define the following custom actions.

                                                                             ﾉ   Expand table

 Action                              Description

 Configuration Manager Executable    Runs a program or opens a file by using the program
 Action                              registered with Windows.

 Configuration Manager ShowDialog    Opens a dialog box.
 Action

 Configuration Manager Report        Opens a report.
 Action

<!-- p.772 -->

 Action                                Description

 Configuration Manager                 Defines the type and assembly for a method that is called.
 AssemblyType Action

 Configuration Manager Group           Creates a menu group, also known as a submenu.
 Action

 Separator                             Creates a separator (line) under an action.

Adding Custom Actions
The steps for adding a new custom action to the Configuration Manager console are:

   1. Create the action XML file. The name you choose for the file should have the .xml
     extension. The arrangement of the actions in the context menu and actions pane is
     based on the alphabetical ordering of the file names in the actions folder.

   2. Deploy the action XML. The custom action XML file is placed in the
     %ProgramFiles%\Microsoft Endpoint
     Manager\AdminConsole\XmlStorage\Extensions\Actions folder under the GUID
     named folder of the Configuration Manager console node.

     For example, to create an action that is displayed on the software updates node
     you would have following folder structure:

     AdminConsole\XmlStorage\Extensions\Actions\f5445252-da1d-450f-a772-
     7c3d3cb929fb\myfilename.xml

     For more information, see How to Create a Configuration Manager Action.

     For more information about the Configuration Manager console nodes, see About
     console nodes.

Conditional Actions
Actions can be made available (displayed) according to specified conditions. The
conditions are defined by the following:

                                                                                     ﾉ   Expand table

 Condition             Description

 Regular expression    The action is made available depending on a defined search pattern.

<!-- p.773 -->

 Condition               Description

 Method call             The action is made available depending on the result of a method call.

 Security                The action is made available depending on the security permissions of the
 permissions             selected item.

For more information, see Configuration Manager Conditional Actions.

See Also
Configuration Manager Action XML
How to Create a Configuration Manager Action
About Configuration Manager console actions About console forms About console
views How to Find a Configuration Manager Node GUID

Feedback
Was this page helpful?       Yes          No

Provide product feedback

<!-- p.774 -->

Configuration Manager Action XML
Article • 10/04/2022

Every Configuration Manager action is defined by an ActionDescription XML element
that defines the action type and other information that is used by the Configuration
Manager console to display the action. An ActionDescription element has a variety of
child elements that provide information specific to the action type and also conditional
tests made before the action is displayed.

The following XML example describes an action that runs a command prompt, creates
.txt file and opens that .txt file in notepad. The ActionDescription element Class
attribute denotes an executable action and the Executable element provides both the
path of the executable and the parameters to pass to that executableThe ShowOn
element tells the console to make this action available both on the context menu and
the default home tab of the ribbon menu.

  <ActionDescription Class="Executable" DisplayName="ExecutableActionName"
  Description="ExecutableActionDescription"> <ShowOn>
  <string>DefaultHomeTab</string>    <string>ContextMenu</string> </ShowOn>
  <ResourceAssembly>    <Assembly>UIExtensionsDemo.dll</Assembly>
  <Type>UIExtensionsDemo.Resources.resources</Type> </ResourceAssembly>
  <ImagesDescription>    <ResourceAssembly>
  <Assembly>UIExtensionsDemo.dll</Assembly>
  <Type>UIExtensionsDemo.Resources.resources</Type>    </ResourceAssembly>
  <ImageResourceName>ActionIcon</ImageResourceName> </ImagesDescription>
  <Executable>    <FilePath>cmd</FilePath>    <Parameters>/C "echo
  ##SUB:__RELPATH## > %temp%\relpath.txt & notepad %temp%\relpath.txt"
  </Parameters> </Executable></ActionDescription>

The default actions used by the Configuration Manager console are defined in the XML
files located in the %ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\XmlStorage\ConsoleRoot\ folder. The XML files for custom
actions can be placed in the %ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\XmlStorage\Extensions\Actions folder under the appropriate
Configuration Manager console node. The Configuration Manager console node is
identified by a folder named with the GUID of the Configuration Manager console
folder.

The following are typical attributes for an ActionDescription element:

                                                                         ﾉ   Expand table

<!-- p.775 -->

 Attribute                Description

 ActionVerb               Indicates whether the action is associated with a standard action.

 Class                    The action type, for example, ShowDialog.

 DisplayName              The text displayed in the context menu.

 MnemonicDisplayName      The mnemonic display name.

 Description              The action description.

 ImageDescription         Information about the action's icon.

 SelectionMode            Determines when the action is displayed, as follows:

                          Single (default). Action is shown only when the selection set contains a
                          single item.

                          Multiple. Action is shown when the selection set contains more than
                          one item.

                          Both. Action is shown when one or more items are selected.

For a complete list of attributes, see ActionDescription.

There are a number of child elements for any given action type.

See Also
About Configuration Manager console actions Configuration Manager AssemblyType
Action
Configuration Manager Conditional Actions
Configuration Manager Executable Action
Configuration Manager Group Action
Configuration Manager Report Action
Configuration Manager ShowDialog Action
How to Create a Configuration Manager Action
How to Find a Configuration Manager Node GUID

Feedback
Was this page helpful?    Yes     No

<!-- p.776 -->

Provide product feedback

<!-- p.777 -->

Configuration Manager Conditional
Actions
Article • 10/04/2022

Configuration Manager actions can be displayed according to specified conditions. The
conditions are defined by the following:

      Regular expressions

      Method calls

      Security permissions

Regular Expressions
Regular expressions allow you to apply string-based search patterns. The following
elements specify a regular expression for an action:

                                                                                   ﾉ   Expand table

 Element               Description

 MatchPattern          Specifies the pattern to search for.

 MatchValueToTest      Specifies the value to compare against. The value following ##Sub is a
                       property on the selected object. The property must not be lazy and must exist
                       on the select object.

The following action displays a dialog box whenever the specified pattern
(MS_ASYNC_RAS) matches the selected object's AddressType property:

  <ActionDescription ActionVerb="Properties" Class="ShowDialog"> <ShowOn>
  <string>DefaultContextualTab</string> <!-- Show on Ribbon -->
  <string>ContextMenu</string> <!-- Show on Context Menu -->   </ShowOn>
  <MatchPattern>MS_ASYNC_RAS</MatchPattern>
   <MatchValueToTest>##SUB:AddressType##</MatchValueToTest>
   <DialogId>AsyncRasSenderAddress</DialogId></ActionDescription>

Method Calls

<!-- p.778 -->

An action can be shown depending on the result of a method call. The
ActionDescription child element ActionStateAssembly defines the assembly, type, and

method to be called. If the method returns true , the action is shown; if the method
returns false , the action is hidden.

The following XML calls a method named EnableDecrementPriorityMenu in the assembly
AdminUI.Addresses.dll:

  <ActionDescription>
   <ShowOn>
      <string>DefaultContextualTab</string> <!-- Show on Ribbon -->
  <string>ContextMenu</string><!-- Show on Context Menu --> </ShowOn>
  <ActionStateAssembly>
    <Assembly>AdminUI.Addresses.dll</Assembly>
  <Type>Microsoft.ConfigurationManagement.AdminConsole.Addresses.AddressUtilit
  yClass</Type>
    <Method>EnableDecrementPriorityMenu</Method> </ActionStateAssembly>
  </ActionDescription>

The method is implemented in a .NET Framework assembly with the following signature:

public static bool EnableDecrementPriority(object sender, ScopeNode scopeNode,
ActionDescription action, ResultObjectBase resultObject)

For more information about calling methods in a .NET Framework assembly, see
Configuration Manager AssemblyType Action.

Security Permissions
You can restrict the availability of an action by applying security restrictions to the
selected object or object class.

Object Instance Permissions
You can restrict the availability of an action by applying required permissions to the
selected object. In the following XML example, the following elements specify the
instance permissions for the selected object:

                                                                            ﾉ   Expand table

<!-- p.779 -->

 Element                           Description

 InstancePermissions               The parent element to the list of instance permissions.

 SecurityFlagsDetailDescription    The security flags that must be set for the action to work.

In the following XML example, the Delete action for a selected object is available only if
the user has modify permissions:

  <ActionDescription ActionVerb="Delete" Class="Default" SelectionMode="Both"
  InstanceDependsOn="SMS_Site">
  <ShowOn> <string>DefaultContextualTab</string> <!-- Show on Ribbon -->
  <string>ContextMenu</string> <!-- Show on Context Menu --></ShowOn>
  <InstancePermissions><SecurityFlagsDetailDescription BitName="Modify"
  BitValue="2" DependsOn="1" /></InstancePermissions>
  </ActionDescription>

Object Class Permissions
You can use the ClassPermissions element to set the object class permissions required
for an action. ActionSecurityDescription describes the object class and the required
permissions for that object class. The following XML example describes the permissions
required for SMS collections:

  <ClassPermissions> <ActionSecurityDescription ClassObject="SMS_Collection"
  RequiredPermissions="1280" />
  </ClassPermissions>

Permission Values
The permission values for the RequiredPermissions attribute are the same as for the
SecurityFlagsDetailDescription class and are as follows:

                                                                               ﾉ   Expand table

 Permission                                      Values               Depends on

 Read                                            1                    None

 Modify                                          2                    1

<!-- p.780 -->

 Permission                                 Values    Depends on

 Delete                                     4         1

 Distribute                                 8         1

 CreateChild                                16        1

 RemoteControl                              32        None

 Advertise                                  64        1

 ModifyResource                             128       1

 Administer                                 256       7

 DeleteResource                             512       1

 Create                                     1024      None

 ViewCollectedFiles                         2048      1

 ReadResource                               4096      1

 Delegate                                   8192      None

 Meter                                      16384     1

 ManageSqlCommand                           32768     1

 ManageStatusFilter                         65536     1

 ManageFolder                               131072    1

 NetworkAccess                              262144    1

 ImportMachineEntry                         524288    1

 CreateMediaCertificate                     1048576   1

 ModifyCollectionSetting                    2097152   1

 ManageOsdCertificate                       4194304   1

See Also
Configuration Manager Actions
Configuration Manager Action XML
Configuration Manager AssemblyType Action
Configuration Manager Executable Action

<!-- p.781 -->

Configuration Manager Group Action
Configuration Manager Report Action
Configuration Manager ShowDialog Action
How to Create a Configuration Manager Action
How to Find a Configuration Manager Node GUID

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.782 -->

Configuration Manager Executable
Action
Article • 10/04/2022

In Configuration Manager, the executable action runs a program or opens a file by using
the program registered with Windows for that file type.

The following attributes and elements are specific to an action that runs a program:

      The ActionDescription element Class attribute is set to Executable .

      The Executable element is parent to FilePath``, the path to the program, and to
      Parameters , the parameters passed to the executable.

Sample Executable Action XML

  <ActionDescription Class="Executable" DisplayName="Test Action (execute)"
  MnemonicDisplayName="A test item" Description="A test item Description">
    <ShowOn>
      <string>DefaultHomeTab</string>
      <string>ContextMenu</string>
    </ShowOn>
    <!--<ResourceAssembly>
      <Assembly>Microsoft.ConfigurationManagement.dll</Assembly>

  <Type>Microsoft.ConfigurationManagement.AdminConsole.Properties.Resources.re
  sources</Type>
    </ResourceAssembly>-->
    <!--<ImagesDescription>
      <ExternalImage>
        <Assembly>AdminUI.Package.dll</Assembly>

  <Type>Microsoft.ConfigurationManagement.AdminConsole.Package.SmsPackageUtils
  </Type>
        <Method>ShowPackageLockedIcon</Method>
      </ExternalImage>
      <ResourceAssembly>
        <Assembly>AdminUI.UIResources.dll</Assembly>

  <Type>Microsoft.ConfigurationManagement.AdminConsole.UIResources.Properties.
  Resources.resources</Type>
      </ResourceAssembly>
      <ImageResourceName>New</ImageResourceName>
    </ImagesDescription>-->
    <!--<ImagesDescription AliasProperty="OwnedByThisSite">

<!-- p.783 -->

      <ResourceAssembly>
        <Assembly>AdminUI.UIResources.dll</Assembly>

  <Type>Microsoft.ConfigurationManagement.AdminConsole.UIResources.Properties.
  Resources.resources</Type>
      </ResourceAssembly>
      <AliasResourceAssembly>
        <Assembly>AdminUI.UIResources.dll</Assembly>

  <Type>Microsoft.ConfigurationManagement.AdminConsole.UIResources.SMS_Collect
  ion-OwnedByThisSite.resources</Type>
      </AliasResourceAssembly>
      <ImageResourceName>CollectionsIcon</ImageResourceName>
    </ImagesDescription>-->
    <!--<ActionStateAssembly>
      <Assembly>AdminUI.Report.dll</Assembly>

  <Type>Microsoft.ConfigurationManagement.AdminConsole.Report.ReportsUtilityCl
  ass</Type>
      <Method>EnableReportMenu</Method>
      -->
    <!--Method signature: public static bool EnableMenu(object sender,
  ScopeNode scopeNode, ActionDescription action, ResultObjectBase
  resultObject)-->
    <!--
    </ActionStateAssembly>-->
    <!--<InstancePermissions>
      <SecurityFlagsDetailDescription BitName="Delete" BitValue="4"
  DependsOn="1" />
    </InstancePermissions>-->
    <!--<MatchPattern>[^1]</MatchPattern>
    <MatchValueToTest>##SUB:Order##</MatchValueToTest>-->
    <Executable>
      <FilePath>https://go.microsoft.com/fwlink/?LinkId=67307</FilePath>
    </Executable>
  </ActionDescription>

Other elements and attributes are documented in ActionDescription.

See Also
Configuration Manager Actions
How to Create a Configuration Manager Action
How to Find a Configuration Manager Node GUID

Feedback

<!-- p.784 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.785 -->

Configuration Manager ShowDialog
Action
Article • 10/04/2022

The ShowDialog action, in Configuration Manager, opens a property sheet or regular
dialog box in the Configuration Manager console. With the ShowDialog action, you can
display existing dialog boxes or extension dialog boxes that you create.

The following attributes and elements are specific to an action that opens a dialog box:

      The ActionDescription element Class attribute is set to ShowDialog .

      The DialogID element is the identifier for a property sheet or dialog box displayed
      in a dialog. It matches the name of the form XML file in the
      %ProgramFiles%\Microsoft Endpoint
      Manager\AdminConsole\XmlStorage\Extensions\Forms folder.

Sample ShowDialog Action XML
The following XML shows how to show a dialog box with the identifier PrototypeForm:

  <ActionDescription Class="ShowDialog" DisplayName="Test Action (dialog)"
  MnemonicDisplayName="Mnemonic" Description="Description">
  <ShowOn>              <string>DefaultHomeTab</string>
  <string>ContextMenu</string>           </ShowOn>
   <DialogId>PrototypeForm</DialogId>
  </ActionDescription>

Sample Properties ShowDialog Action XML
The following attributes and elements are specific to an action that adds a property
page to a properties property sheet:

      The ActionDescription element ActionVerb attribute is set to Properties .

      The DialogID element identifies a property sheet containing the property page to
      be displayed in the Properties dialog.

<!-- p.786 -->

     The following XML shows how to integrate a property page ( PrototypeForm ) into a
     properties context menu option:

  <ActionDescription ActionVerb="Properties" Class="ShowDialog"> <ShowOn>
  <string>DefaultHomeTab</string>    <string>ContextMenu</string> </ShowOn>
  <DialogId>PrototypeForm</DialogId>
  </ActionDescription>

For more information about creating and showing dialog boxes, see About console
forms.

See Also
About Configuration Manager Dialog Boxes
Configuration Manager Actions
How to Create a Configuration Manager Action
How to Create Form XML for a Configuration Manager Property Sheet
How to Create Form XML for a Configuration Manager Dialog Box
How to Find a Configuration Manager Node GUID

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.787 -->

Configuration Manager Report Action
Article • 10/04/2022

The report action displays a Configuration Manager report in the Configuration
Manager console.

The following attributes and elements are specific to an action that opens a report box:

      The ActionDescription element Class attribute is set to Report.

      The ReportDescription element ReportName attribute is the GUID of the report to
      be displayed. The GUID maps to the SMS_Report class ReportGUID property.

  ７ Note

  An alternative method to load a report is to use the executable action to launch the
  report's URL. This will display the report in a new window rather than in the
  Configuration Manager console.

Sample Report Action XML
The following XML demonstrates how to display a report, identified by its GUID, in the
Configuration Manager console:

  <ActionDescription Class="Report" DisplayName="Test Action (report)"
  MnemonicDisplayName="Mnemonic" Description="Description"> <ShowOn>
  <string>DefaultContextualTab</string> <!-- RIBBON -->
  <string>ContextMenu</string> <!-- Context Menu -->    </ShowOn>
   <ReportDescription ReportName="05874720-1D08-4CF7-B182-5F9D065BEAE5">
   </ReportDescription>
  </ActionDescription>

See Also
Configuration Manager Actions
How to Create a Configuration Manager Action
How to Find a Configuration Manager Node GUID
How to Find a Configuration Manager Node GUID

<!-- p.788 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.789 -->

Configuration Manager AssemblyType
Action
Article • 10/04/2022

The AssemblyType action defines the type and assembly for a method that is called by
the Configuration Manager console.

  ７ Note

  The XML and C# code in this topic is available in the Dialog Prototype sample in
  the Configuration Manager SDK.

The following attributes and elements are specific to an action that calls a method in an
assembly:

      The Class attribute of the ActionDescription element is set to AssemblyType .

      The ActionAssembly element has a number of child elements that are used to
      define the method and assembly.

      The Assembly element identifies the assembly that contains the method. If the
      assembly is in a folder other than %ProgramFiles%\Microsoft Endpoint
      Manager\AdminConsole\bin folder then the Assembly element should include the
      assembly filename and the full path to the file.

      The Type element contains the namespace and class for the method.

      The Method element contains the name of the method to be called.

Method
The method signature is:

  public static void Method(object, ScopeNode, ActionDescription,
  IResultObject, PropertyDataUpdated, Status)

Where the parameters are as follows:

<!-- p.790 -->

object

The object calling the method.

ScopeNode

The Configuration Manager console node that was active when the action was called.

ActionDescription

The ActionDescription class instance that initiated the action.

IResultObject

The selected object, or null if there is no selected object.

PropertyDataUpdated

The delegate to open to provide update information for the Configuration Manager
console view.

Status

Allows control of the Configuration Manager console busy status indicator.

Example Implementation
The following is an example implementation of the method.

  public static void Method(object sender, ScopeNode scopeNode,
  ActionDescription action, IResultObject resultObject, PropertyDataUpdated
  dataUpdatedDelegate, Status status)
  {
      if (resultObject != null)
      {
          MessageBox.Show(string.Format("The {0} package was selected",
  resultObject["Name"].StringValue));
      }
      else
      {
          MessageBox.Show("No package was selected");
      }
  }

AssemblyType Action XML
The following XML example demonstrates how to call a method, Method , in a class,
SampleClass . The method is in the assembly AdminUI.PrototypeDialog.dll .

<!-- p.791 -->

  <ActionDescription Class="AssemblyType" DisplayName="Test Action (method)"
  MnemonicDisplayName="Mnemonic" Description="Description">
    <ShowOn>
      <string>DefaultHomeTab</string>
      <string>ContextMenu</string>
    </ShowOn>
    <ActionAssembly>
      <Assembly>AdminUI.PrototypeDialog.dll</Assembly>

  <Type>Microsoft.ConfigurationManagement.AdminConsole.PrototypeDialog.Example
  Class</Type>
      <Method>Method</Method>
      <!--Method signature: public static void Method(object sender, ScopeNode
  scopeNode, ActionDescription action, IResultObject resultObject,
  PropertyDataUpdated dataUpdatedDelegate, Status status)-->
    </ActionAssembly>
  </ActionDescription>

See Also
How to Create a Configuration Manager Action
Configuration Manager Actions
Configuration Manager Action XML
How to Find a Configuration Manager Node GUID

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.792 -->

Configuration Manager Group Action
Article • 10/04/2022

In Configuration Manager, the Group action creates a menu group, also known as a
submenu, for related actions.

The following attributes and elements are specific to an action that creates a group of
context menu items:

      The < ActionDescription > element Class attribute is set to Group.

      The < DisplayName > attribute is the group name displayed in the context menu.

      The < GroupAsRegion > Boolean attribute specifies whether or not to display this
      group as a region on the ribbon bar.

      The < ActionGroups > element is a list of actions (< ActionDescription > elements)
      displayed in the context menu group.

Group Action XML
The following XML demonstrates a group of actions named New Group Name:

  <ActionDescription Class="Group" GroupAsRegion="true" DisplayName="New Group
  Name" MnemonicDisplayName="MnemonicNewGroupName"
  Description="NewGroupNameDescription"> <ShowOn>
  <string>DefaultContextualTab</string> <!-- RIBBON -->
  <string>ContextMenu</string> <!-- Context Menu -->    </ShowOn>
  <ActionGroups>
      <ActionDescription Class="Executable" DisplayName="Test Action
  (execute)" MnemonicDisplayName="A test item" Description="A test item
  Description">          <ShowOn>
  <string>DefaultContextualTab</string> <!-- RIBBON -->
  <string>ContextMenu</string> <!-- Context Menu -->       </ShowOn>
  <Executable>
        <FilePath>https://go.microsoft.com/fwlink/?LinkId=67307</FilePath>
      </Executable>
      </ActionDescription>
      <ActionDescription Class="Report" DisplayName="Test Action (report)"
  MnemonicDisplayName="Mnemonic" Description="Description">
      <ShowOn>         <string>DefaultContextualTab</string> <!-- RIBBON --
  >        <string>ContextMenu</string> <!-- Context Menu -->       </ShowOn>
  <ReportDescription Id="05874720-1D08-4CF7-B182-5F9D065BEAE5">
        </ReportDescription>
      </ActionDescription>

<!-- p.793 -->

    </ActionGroups>
  </ActionDescription>

See Also
About Configuration Manager console actions How to Create a Configuration Manager
Action
How to Find a Configuration Manager Node GUID

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.794 -->

How to Create a Configuration Manager
Action
Article • 10/04/2022

To create a Configuration Manager console action, in Configuration Manager, you create
an XML file that populates an ActionDescription XML element for the action. You must
then copy the XML file to the %ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\XmlStorage\Extensions\Actions\GUID folder.

For sample XML for each action type, see the following:

      Configuration Manager Executable Action

      Configuration Manager ShowDialog Action

      Configuration Manager Report Action

      Configuration Manager AssemblyType Action

      Configuration Manager Group Action

      For information about deploying the action XML, see Configuration Manager
      Console Extension Deployment.

To add an executable action to the Configuration
Manager console
   1. If the Configuration Manager console is open, close it.

   2. In Notepad, create an empty text file named MyConfigurationManagerNote.txt and
      save it to C:\.

   3. In Notepad, create an XML file that contains the following XML:

        <ActionDescription Class="Executable" DisplayName="Make a Note"
        MnemonicDisplayName="Note" Description = "Make a note about software
        updates">    <ShowOn>      <string>DefaultContextualTab</string> <!--
        RIBBON -->     <string>ContextMenu</string> <!-- Context Menu -->
        </ShowOn>       <Executable>
          <FilePath>Notepad.exe</FilePath>
          <Parameters>C:\MyConfigurationManagerNote.txt</Parameters>

<!-- p.795 -->

         </Executable>
        </ActionDescription>

   4. Save the XML file in the folder <%Program Files%> Microsoft Endpoint
     Manager\AdminConsole\XmlStorage\Extensions\Actions\f5445252-da1d-450f-
     a772-7c3d3cb929fb. The GUID identifies the software updates folder. The file name
     can be anything with an .xml extension, but it does alphabetically affect the
     ordering of actions in the context-sensitive menu and in the actions pane. If it is
     not already created, you must create the Extensions\Actions\f5445252-da1d-450f-
     a772-7c3d3cb929fb folder structure. Be sure to save the file as type All Files .

   5. Start the Configuration Manager console.

     In the Configuration Manager console, right-click the Software Updates node
     under Computer Management, and then click Make a Note. Notepad opens the
     text file.

See Also
Configuration Manager Actions
Configuration Manager Action XML
Configuration Manager Executable Action
How to Find a Configuration Manager Node GUID

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.796 -->

About Configuration Manager Console
Forms
Article • 10/04/2022

You can extend the Configuration Manager console with new Windows forms.
Specifically, you can add form-based dialog boxes and property sheets. A user accesses
these forms from Configuration Manager actions that you define.

  ７ Note

  Wizards are another Windows form that is used by the Configuration Manager
  console, but you cannot extend or add wizards by using the Configuration Manager
  console framework. You can, however, run your own wizard solution by using
  Configuration Manager actions.

In Configuration Manager, forms are stored in .NET Framework assemblies that are
called by the Configuration Manager console after the appropriate action is selected.

Creating an Extension Form
To write an extension form, you do the following:

      Create the extension form assembly.

      Create the extension form action XML.

      Create the extension form XML.

Create the Extension Form Assembly

Property sheets
A property sheet is made up of one or more property pages that you define. You can
also integrate property pages into existing Configuration Manager property sheets.

To create a property sheet, you create a Windows Control Library project in Visual
Studio. In this project, you create a class that inherits from the
Microsoft.ConfigurationManagement.AdminConsole.SmsPageControl class. This class
implements the control you want to display on a property page. In a property sheet, you

<!-- p.797 -->

create an SmsPageControl class for each property page that you need. The Property
Sheet Prototype sample in the Configuration Manager SDK has a complete solution that
you can use. For more information, see How to Create a Configuration Manager
Property Sheet.

Dialog boxes

A dialog box in Configuration Manager is displayed like a typical modeless dialog box.
You create an SMSPageControl and specify "Dialog" in the Form XML. For more
information, see How to Create a Configuration Manager Dialog Box.

Create the Form Action XML
An action describes the type of extension that is called, and where the action is placed in
the Configuration Manager console user interface. For an extension form, you use the
ShowDialog action type to display the form. For more information, see How to Create

Action XML for a Configuration Manager Property Sheet.

For more information about actions, see About Configuration Manager console actions.

Create the Form Property Sheet XML
Whether or not the form is a property sheet, the form has a form XML file that defines
the assembly, namespace, and type of the form. In property sheets, it defines the order
of the property pages on the property sheet. There is a property sheet XML file for every
Configuration Manager console form.

  ７ Note

  The Configuration Manager console property sheet XML files are stored in
  %ProgramFiles%\Microsoft Endpoint Manager\AdminConsole\XmlStorage\Forms.

When you create a new form, you create a new property sheet XML file. If you are
adding a new property page to an existing property sheet, you merge the property page
XML with an existing property sheet XML file.

  ７ Note

  Extension property sheets are stored in %ProgramFiles%\Microsoft Endpoint
  Manager\AdminConsole\XmlStorage\Extensions\Forms.

<!-- p.798 -->

For more information about form XML deployment, see Configuration Manager Console
Extension Deployment.

Depending on whether you are displaying a dialog box or a property sheet, the
FormType attribute values must be set.

                                                                        ﾉ   Expand table

 FormType                       Description

 PropertySheet                  The form is a property sheet.

 Dialog                         The form is a dialog box.

When an action is selected, the Configuration Manager console uses the property sheet
XML to determine which assembly is needed to load and display the form.

For more information, see How to Create Form XML for a Configuration Manager
Property Sheet.

Managing Object Data in a Form
A Configuration Manager form can be passed custom data and also, from the results
pane, the objects returned from a query. Selected objects from the results pane are
made available to a form through a PropertyManager object. For more information, see
How to Use Objects Passed to a Configuration Manager Form. You can bind a form
control to objects passed in to the form's PropertyManager . For more information, see
How to Bind Configuration Manager Data to a Form.

The Configuration Manager console serializes Configuration Manager objects passed
into a form when the form is dismissed.

Queries
You can perform both synchronous and asynchronous queries in forms by using the
managed SMS Provider. You get the
Microsoft.ConfigurationManagement.AdminConsole.SmsPageControl.QueryProcessor
object from the form's PropertyManager ConnectionManager. After it is obtained, the
code is identical to the SMS Provider examples. For an example of a synchronous query,
see How to Perform a Synchronous Configuration Manager Query by Using Managed
Code.

<!-- p.799 -->

For an example of an asynchronous query, see How to Perform an Asynchronous
Configuration Manager Query by Using Managed Code.

See Also
How to Add a Property Page to an Existing Configuration Manager Property Sheet
How to Bind Configuration Manager Data to a Form
How to Create a Configuration Manager Property Sheet
How to Create Action XML for a Configuration Manager Dialog Box
How to Create Action XML for a Configuration Manager Property Sheet
How to Create a Configuration Manager Dialog Box
How to Create Form XML for a Configuration Manager Dialog Box
How to Create Form XML for a Configuration Manager Property Sheet
How to Use Objects Passed to a Configuration Manager Form

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.800 -->

How to Create a Configuration Manager
Property Sheet
Article • 10/04/2022

To create a Configuration Manager console property sheet, in Configuration Manager,
you create a .NET Framework assembly that inherits from the following class:

                                                                         ﾉ   Expand table

 Class                     Description

 SmsPageControl            The control displayed on the property page.

The following procedures show you how to create a Configuration Manager property
sheet assembly by using Visual Studio. The property sheet displays a property page that
contains a button. When it is clicked, the button displays the name of a package
selected in the Configuration Manager console Packages node.

After you have successfully built the dialog box assembly, you must do the following to
integrate it into the Configuration Manager console:

   1. Define and deploy the form XML that links the selected action to the assembly you
      create in this topic. For more information, see How to Create the Form XML for a
      Configuration Manager Property Sheet.

   2. Define and deploy the action XML for displaying the context menu that the user
      selects. For more information, see How to Create Action XML for a Configuration
      Manager Property Sheet.

      When you have created the property sheet assembly and XML, right-click a
      package in the Configuration Manager console tree Packages node results pane,
      and select the menu item Show my Property Sheet. A property sheet is displayed.
      You can enhance the control by accessing the package that was selected in the
      Configuration Manager console. For more information, see How to Use Objects
      Passed to a Configuration Manager Forms.

Create the Control Class
The following procedure creates the control for the property sheet.
