---
title: "Configuration Manager SDK documentation — pages 801-840"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0801-0840
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0801-0840
family: sccm
documentKind: "doc"
abstract: "To create the Visual Studio project 1. In Visual Studio 2010, on the File menu, point to New, and then click Project to open the New Project dialog box. 2. From the list of Visual C#, Windows projects, select the Windows Forms Control Library project template, and then type Conf"
---

# Configuration Manager SDK documentation — pages 801-840

<!-- p.801 -->

To create the Visual Studio project
  1. In Visual Studio 2010, on the File menu, point to New, and then click Project to
    open the New Project dialog box.

  2. From the list of Visual C#, Windows projects, select the Windows Forms Control
    Library project template, and then type ConfigMgrControl in the Name box.

  3. Click OK to create the Visual Studio project.

  4. In Solution Explorer, right-click the project and select Properties. On the
    Application tab, change Target framework to .NET Framework 4.

  5. In Solution Explorer, right-click UserControl1.cs, click Rename, and then change
    the name to ConfigMgrControl.cs.

  6. In Solution Explorer, right-click References and then click Add Reference.

  7. In the Add Reference dialog box, click the Browse tab, navigate to
    %ProgramFiles%\Microsoft Endpoint Manager\AdminConsole\bin and then
    select microsoft.configurationmanagement.exe,
    Microsoft.ConfigurationManagement.DialogFramework.dll and
    microsoft.configurationmanagement.managementprovider.dll . Click OK to add
    the assemblies as project references.

  8. In Solution Explorer, right-click ConfigMgrControl.cs, and then click View Code.

  9. In the source code, change the namespace to
    Microsoft.ConfigurationManagement.AdminConsole.ConfigMgrPropertySheet

 10. Change the class ConfigMgrControlPage so that it derives from SmsPageControl .

 11. In Solution Explorer, right-click ConfigMgrControl.Designer.cs, and then click View
    Code.

 12. In the source code, change the namespace to
    Microsoft.ConfigurationManagement.AdminConsole.ConfigMgrPropertySheet

 13. In ConfigMgrControl.cs, Add the following new constructor to the
    ConfigMgrControlPage class:

       public ConfigMgrControlPage (SmsPageData pageData) : base(pageData)
       {

<!-- p.802 -->

             InitializeComponent();
        }

 14. Add the following method to initialize the control:

        public override void InitializePageControl()
        {
           base.InitializePageControl();
        }

Deploy the Assembly
The following procedure builds and copies the assembly that you have created to the
Configuration Manager console assemblies folder. For important information about
deploying Configuration Manager console extensions, see About Configuration
Manager Administrator Console Extension Deployment.

To deploy the property sheet assembly

   1. Build the project. The assembly should be created as \Visual Studio
     2010\Projects\ConfigMgrControl\ConfigMgrControl\bin\Debug\ConfigMgrControl.
     dll.

   2. Copy the assembly to the folder %ProgramFiles%\Microsoft Endpoint
     Manager\AdminConsole\bin.

See Also
How to Add a Property Page to an Existing Configuration Manager Property Sheet
How to Create Action XML for a Configuration Manager Property Sheet
How to Create Form XML for a Configuration Manager Property Sheet
How to Use Objects Passed to a Configuration Manager Forms

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.803 -->

How to Create Form XML for a
Configuration Manager Property Sheet
Article • 10/04/2022

In Configuration Manager, to create the form XML for a Configuration Manager
property sheet, you create an XML file that describes an SmsFormData .

Every Configuration Manager console form extension has an associated form XML file
that describes the assembly, the type of the form to be displayed, and—in the case of
property sheets—how the property pages are organized. The property sheet XML file is
referenced by the action XML when an action is selected.

  ７ Note

  The name of the form XML file is significant because it is used in the action XML to
  identify the form XML.

The following procedure demonstrates how to create the form XML file for the control
and property page you created in How to Create a Configuration Manager Property
Sheet.

After completing the following procedure, you must create an action to load the
property sheet. For more information, see How to Create Action XML for a Configuration
Manager Property Sheet.

  ７ Note

  To see the form XML used by the Configuration Manager console, see
  %ProgramFiles%\AdminConsole\XmlStorage\Forms. These can be useful for
  creating your own form XML.

To create the form XML for a property sheet
   1. If it is open, close the Configuration Manager console.

   2. In Notepad, create an XML file that contains the following XML:

         XML

<!-- p.804 -->

       <?xml version="1.0" encoding="utf-8"?>
       <SmsFormData
       xmlns="http://schemas.microsoft.com/SystemsManagementServer/2005/03/Con
       soleFramework" FormatVersion="1">
         <Form Id="PROPERTYSHEETGUID" CustomData="SomeData"
       FormType="PropertySheet" ForceRefresh="true">
           <Assembly Name="ConfigMgrControl.dll"
       Namespace="Microsoft.ConfigurationManagement.AdminConsole.ConfigMgrProp
       ertySheet" />
           <Pages>
             <Page VendorId="YOURCOMPANY" Id="VENDORGUID"
       Type="ConfigMgrControlPage" />
           </Pages>
         </Form>
       </SmsFormData>

  3. In Visual Studio 2010, on the Tools menu, click Create GUID.

  4. In the Create GUID dialog box, in the GUID format panel, select Registry Format.

  5. Click New GUID, and then click Copy.

  6. In the XML above, paste the GUID into PROPERTYSHEETGUID. A single opening {
     and a single closing } must wrap the GUID. For example, {ab60b75e-b64a-44c0-
     ad63-d96d289f39ca} .

  7. Repeat steps 3 through 5, and paste the GUID into VENDORGUID.

  8. In the preceding XML, change YOURCOMPANY to your company name.

  9. Save the XML file in the folder
     %ProgramFiles%\AdminConsole\XmlStorage\Extensions\Forms with the file name
     ConfigMgrPropertySheet.xml. Be sure to save the file as type All Files . If the
     Extensions folder and Forms folder do not yet exist, create them.

 10. Start the Configuration Manager console, and select the action you defined in How
     to Create Action XML for a Configuration Manager Property Sheet.

     The property sheet you created in How to Create a Configuration Manager
     Property Sheet appears.

See Also
About Configuration Manager Forms
How to Create Action XML for a Configuration Manager Property Sheet
How to Create a Configuration Manager Property Sheet

<!-- p.805 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.806 -->

How to Add a Property Page to an
Existing Configuration Manager
Property Sheet
Article • 10/04/2022

To add a property page to an existing property sheet, in Configuration Manager, you
add the property page XML to the property sheet's XML file. For existing Configuration
Manager property sheets, you copy the existing property XML file to the
XmlStorage\Extensions\Forms folder from XmlStorage\Forms. When the Configuration
Manager console loads, it will use the XML it finds in the XmlStorage\Extensions\Forms
folder in preference to existing forms in XmlStorage\Forms.

Because multiple vendors can extend existing property sheets, you must deploy and
remove your property sheets with care. For more information, see About Configuration
Manager Administrator Console Extension Deployment.

The following procedure demonstrates how to add a property page to the Properties
page for a package. To complete it. you will first need to create a property page. For
more information, see How to Create a Configuration Manager Property Sheet.

To add a property page to a Properties property sheet
   1. Copy the package.xml file from %ProgramFiles%\Microsoft Endpoint
      Manager\AdminConsole\XmlStorage\Forms to %ProgramFiles%\Microsoft
      Endpoint Manager\AdminConsole\XmlStorage\Extensions\Forms.

   2. In the package.xml file, add the following property page XML (you should place it
      below the other <Page> elements, near the end of the file):

        <Page VendorId="My Company" Id="{3F52B74A-373A-4c97-A142-C93E230948F8}"
        Assembly="ConfigMgrControl"
        Namespace="Microsoft.ConfigurationManagement.AdminConsole.ConfigMgrProp
        ertySheet" Type="ConfigMgrControlPage" />

   3. In Visual Studio 2010, on the Tools menu, click Create GUID.

   4. In the Create GUID dialog box, in the GUID format panel, select Registry Format.

   5. Click New GUID, and then click Copy.

<!-- p.807 -->

   6. In the XML above, paste the GUID into PROPERTYSHEETGUID. A single opening {
     and a single closing } must wrap the GUID. For example, {ab60b75e-b64a-44c0-
     ad63-d96d289f39ca} .

   7. Save the file, and start the Configuration Manager console.

   8. Using the Packages node results pane, right-click a package, and then click
     Properties. The properties dialog box is displayed with your property page.

See Also
About Configuration Manager Forms
How to Create Form XML for a Configuration Manager Property Sheet
How to Create a Configuration Manager Property Sheet

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.808 -->

How to Create Action XML for a
Configuration Manager Property Sheet
Article • 10/04/2022

In Configuration Manager, to display a property sheet or dialog box in the Configuration
Manager console, you create a ShowDialog action. Like other actions, the ShowDialog
action defines a context menu and action pane action that the user selects to show the
dialog box. To define the ShowDialog action, you create an XML file that describes a
ActionDescription element.

For more information about property sheet and dialog box actions, see Configuration
Manager ShowDialog Action.

The following procedure creates the action XML for showing the property sheet you
created in How to Create a Configuration Manager Property Sheet. You must also
complete How to Create Form XML for a Configuration Manager Property Sheet before
completing the following procedure.

To create action XML for a property sheet
   1. If it is open, close the Configuration Manager console.

   2. In Notepad, create an XML file that contains the following XML:

        XML

        <?xml version="1.0"?>
        <ActionDescription Description="DisplayDescription"
        DisplayName="DisplayName" SynchronousAction="true" Class="ShowDialog"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
           <ShowOn>       <string>DefaultHomeTab</string>
               <string>ContextMenu</string>
           </ShowOn>
           <DialogId>Package</DialogId>
        </ActionDescription>

   3. Save the XML file in the folder
      %ProgramFiles%\AdminConsole\XmlStorage\Extensions\Actions\9c69b0aa-a27c-
      43c9-8c26-5f964106a881. The GUID value identifies packages in the results pane.
      The file name can be anything with an .xml extension. Be sure to save the file as

<!-- p.809 -->

     type All Files . If they do not exist, create the Actions folder and Actions
     subfolder.

   4. Load the Configuration Manager console, and in the console tree Packages node,
     right-click a package in the results pane, and then click DisplayName. A property
     sheet appears.

See Also
How to Create a Configuration Manager Property Sheet
How to Add a Property Page to an Existing Configuration Manager Property Sheet
How to Create Form XML for a Configuration Manager Property Sheet
How to Find a Configuration Manager Node GUID

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.810 -->

How to Create a Configuration Manager
Dialog Box
Article • 10/04/2022

These procedures show you how to create a modeless dialog box assembly, in
Configuration Manager, by using Visual Studio.

Creating the dialog box is very similar to creating a property sheet. You create a class
derived from SmsPageControl and an XML file to describe the dialog.

For more information about the property manager, see How to Use Objects Passed to a
Configuration Manager Forms.

After you have successfully built the dialog box assembly, you must do the following to
integrate it into the Configuration Manager console:

   1. Define and deploy the form XML that links the selected action to the assembly you
      create in this topic. For more information, see How to Create Form XML for a
      Configuration Manager Dialog Box.

   2. Define and deploy the action XML for displaying the context menu that the user
      selects. For more information, see How to Create Action XML for a Configuration
      Manager Dialog Box.

      When you have created the dialog assembly and XML, right-click a package in the
      Configuration Manager console tree Packages node, and then click Show my
      Dialog Box. A dialog box appears with a button on it. Clicking the button displays
      a message box containing the name of the package you selected.

Create the Control Class
The following procedure creates the control for the dialog box.

To create the Visual Studio project
   1. In Visual Studio 2010, on the File menu, point to New, and then click Project to
      open the New Project dialog box.

   2. From the list of Visual C#, Windows projects, select the Windows Control Library
      project template, and type ConfigMgrDialogControl in the Name box.

<!-- p.811 -->

 3. Click OK to create the Visual Studio project.

 4. In Solution Explorer, right-click UserControl1.cs, click Rename, and change the
   name to ConfigMgrDialogControl.cs.

 5. In Solution Explorer, right-click References, and then click Add Reference.

 6. In the Add Reference dialog box, click the Browse tab, navigate to
   %ProgramFiles%\Microsoft Endpoint Manager\AdminConsole\bin and then
   select microsoft.configurationmanagement.exe,
   microsoft.configurationmanagement.managementprovider.dll,
   Microsoft.ConfigurationManagement.DialogFoundation.dll and
   AdminUI.DialogFoundation.dll. Click OK to add the assemblies as project
   references.

 7. In Solution Explorer, right-click ConfigMgrDialogControl.cs and then click View
   Code.

 8. In the source code, change the namespace to
   Microsoft.ConfigurationManagement.AdminConsole.ConfigMgrDialogBox

 9. Change the class ConfigMgrDialogControl so that it derives from SmsCustomDialog .

10. In Solution Explorer, right-click ConfigMgrDialogControl.Designer.cs and then
   click View Code.

11. In the source code, change the namespace to
   Microsoft.ConfigurationManagement.AdminConsole.ConfigMgrDialogBox

12. Change the class ConfigMgrDialogControl so that it derives from SmsCustomDialog .

13. In ConfigMgrDialogControl.cs, add the following code to initialize the control:

      public override bool Initialize(System.Reflection.Assembly assembly,
      SmsFormData formData, SmsPageData pageData)
      {
          base.Initialize(assembly, formData, pageData);
          return true;
      }

14. In Solution Explorer, right-click ConfigMgrDialogControl.cs and select View
   Designer.

<!-- p.812 -->

 15. In the Toolbox, click the Common Controls tab, and then double-click Button. A
     button named button1 is added to your control on the User Control Designer.

 16. In the User Control Designer, double-click button1 and type the following code in
     the button1_Click method source code displayed:

        MessageBox.Show( PageData.PropertyManager["Name"].StringValue);

Deploy the Assembly
The following procedure builds and copies the assembly that you have created to the
Configuration Manager console assemblies folder. For important information about
deploying Configuration Manager console extensions, see About Configuration
Manager Console Extension Deployment.

To deploy the dialog box assembly

   1. Build the project, and depending on where you created your project, your Visual
     Studio installation, the assembly is created as \Visual Studio
     2010\Projects\ConfigMgDialogControl\ConfigMgrDialogControl\bin\Debug\Confi
     gMgrDialogControl.dll.

   2. Copy the assembly to the folder %ProgramFiles%\Microsoft Endpoint
     Manager\AdminConsole\bin.

See Also
How to Add a Property Page to an Existing Configuration Manager Property Sheet
How to Create Action XML for a Configuration Manager Property Sheet
How to Create Form XML for a Configuration Manager Property Sheet
How to Use Objects Passed to a Configuration Manager Forms

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.813 -->

How to Create Form XML for a
Configuration Manager Dialog Box
Article • 10/04/2022

In Configuration Manager, to create the form XML for a Configuration Manager dialog
box, you create an XML file that describes a SmsFormData.

The form XML is similar to the property sheet form XML with the following exceptions:

      FormType must be set to Dialog .

      The following procedure demonstrates how to create the form XML file for the
      dialog box you created in How to Create a Configuration Manager Dialog Box.

To create the form XML for a dialog box
   1. If it is open, close the Configuration Manager console.

   2. In Notepad, create an XML file that contains the following XML:

        <?xml version="1.0" encoding="utf-8"?>
        <SmsFormData FormatVersion="1.0"
        xmlns="http://schemas.microsoft.com/SystemsManagementServer/2005/03/Con
        soleFramework">
          <Form Id="{DIALOGGUID}" CustomData="User Properties"
        FormType="CustomDialog" >
            <Assembly Name="ConfigMgrDialogControl"
        Namespace="Microsoft.ConfigurationManagement.AdminConsole.ConfigMgrDial
        ogBox" ClassType="ConfigMgrDialogControl"/>
          </Form>
        </SmsFormData>

   3. In Visual Studio 2010, on the Tools menu, click Create GUID.

   4. In the Create GUID dialog box, in the GUID format panel, select Registry Format.

   5. Click New GUID, and then click Copy.

   6. In the XML above, paste the GUID into DIALOGGUID. Be sure to keep the open {
      and closing } in the XML.

<!-- p.814 -->

   7. Save the XML file in the folder,
     %ProgramFiles%\AdminConsole\XmlStorage\Extensions\Forms with the file name
     ConfigMgrDialogControl.xml. The file name must match the DialogId element of
     the action XML. If the Extensions folder does not yet exist, create it. Be sure to save
     the file as type All Files .

   8. Start the Configuration Manager console, and select the action you defined in How
     to Create Action XML for a Configuration Manager Dialog Box.

     The property sheet you created in How to Create a Configuration Manager Dialog
     Box appears.

See Also
How to Create a Configuration Manager Dialog Box
How to Create Action XML for a Configuration Manager Dialog Box
How to Create Form XML for a Configuration Manager Property Sheet

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.815 -->

How to Create Action XML for a
Configuration Manager Dialog Box
Article • 10/04/2022

In Configuration Manager, to display a dialog box in the Configuration Manager
console, you create a Configuration Manager ShowDialog Action action. To define the
ShowDialog action, you create an XML file that describes a ActionDescription element.

The following procedure creates the action XML for showing a dialog box. You must
complete the procedures in the How to Create a Configuration Manager Dialog Box and
How to Create Form XML for a Configuration Manager Dialog Box topics before you
complete this procedure.

  ７ Note

  The dialog identifier < DialogId > must match the file name, without the XML
  extension, of the form XML you created in How to Create Form XML for a
  Configuration Manager Dialog Box.

To create an action for a dialog box
   1. If it is open, close the Configuration Manager console.

   2. In Notepad, create an XML file that contains the following XML:

        <ActionDescription Class="ShowDialog" DisplayName="Show my Dialog Box"
        MnemonicDisplayName="Mnemonic" Description="Description"> <ShowOn>
        <string>DefaultContextualTab</string> <!-- RIBBON -->
        <string>ContextMenu</string> <!-- Context Menu -->    </ShowOn>
         <DialogId>ConfigMgrDialogControl</DialogId>
        </ActionDescription>

   3. Save the XML file in the folder,
      %ProgramFiles%\AdminUI\XmlStorage\Extensions\Actions\32815086-cce9-42de-
      95a4-0941da31114e. The GUID value identifies packages in the results pane. The
      file name can be anything with an .xml extension. Be sure to save the file as type
      All Files .

<!-- p.816 -->

   4. Start the Configuration Manager console, and in the console tree Packages node,
     right-click a package in the results pane, and then click Show my Dialog Box. A
     dialog box appears.

See Also
How to Create a Configuration Manager Dialog Box
How to Create Form XML for a Configuration Manager Dialog Box
How to Create Action XML for a Configuration Manager Property Sheet
How to Use Objects Passed to a Configuration Manager Forms
How to Bind Configuration Manager Data to a Form

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.817 -->

How to Use Objects Passed to a
Configuration Manager Form
Article • 10/04/2022

In Configuration Manager, you use the SmsPageControl.PropertyManager object to
access objects that are selected in the Configuration Manager console.

  ７ Note

  If no object is selected in the Configuration Manager console, an empty
  PropertyManager object is created and passed to the form. This can be used for
  creating new objects.

The form manages the serialization of objects in the PropertyManager object, and any
changes you make are automatically saved when you click OK, or they are abandoned
when you click Cancel.

Depending on the SelectionMode attribute of the action's ActionDescription element,
more than one object can be passed to the PropertyManager object. Changes that you
make by using the PropertyManager object are then applied to all objects that are
passed in. If you want to access the individual objects, you must cast the
PropertyManager object to a ResultObjectsManager. You then access the objects
through the ResultObjectsManager object collection.

For more information, see Configuration Manager Action XML.

For information about getting the property manager in a dialog box, see How to Create
a Configuration Manager Dialog Box.

Displaying the Package Name
The following procedure demonstrates using a PropertyManager object to access a
single object passed to a property sheet. Clicking a button displays a message box that
contains the name of a selected package. To complete these steps, you must first
perform the actions in the following topics:

      How to Create a Configuration Manager Property Sheet

      How to Create Form XML for a Configuration Manager Property Sheet

      How to Create Action XML for a Configuration Manager Property Sheet

<!-- p.818 -->

To display the package name
   1. If the Configuration Manager console is open, close it.

   2. In Visual Studio 2010, open the project you created in How to Create a
     Configuration Manager Property Sheet.

   3. In Solution Explorer, right-click ConfigMgrControl.cs, and then click View
     Designer.

   4. In the Toolbox, click the Common Controls tab, and then double-click Button. A
     button named button1 is added to your control on the User Control Designer.

   5. In the User Control Designer, double-click button1 and type the following code in
     the button1_Click method source code that is displayed:

        MessageBox.Show(string.Format("The {0} package was selected",
        PropertyManager["Name"].StringValue));

   6. Build the project and copy the assembly to the %ProgramFiles%\Microsoft
     Endpoint Manager\AdminConsole\bin folder.

   7. Open the Configuration Manager console, and navigate to the Packages node
     under Software Distribution.

   8. Right-click a package, and then click Show my Dialog Box. The dialog box is
     displayed.

   9. Click the button, and the name of the package is displayed in the dialog box.

See Also
About Configuration Manager Forms
How to Bind Configuration Manager Data to a Form

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.819 -->

How to Bind Configuration Manager
Data to a Form
Article • 10/04/2022

In Configuration Manager, to bind Configuration Manager console data to a property
sheet, you use the DataBindings property of the property sheet's control class.

The DataBindings property is used to bind to the objects in the form's Property
Manager . After an object changes, mark the object as changed with SetDirtyFlag. This

ensures that the object is serialized properly when the dialog box is dismissed.

To bind Configuration Manager data to a form
   1. If the Configuration Manager console is open, close it.

   2. In Visual Studio 2010, open the project you created in How to Create a
      Configuration Manager Property Sheet.

   3. In Solution Explorer, right-click ConfigMgrControl.cs, and then click View
      Designer.

   4. In the Toolbox, click the Common Controls tab, and then double-click TextBox. A
      field named textBox1 is added to your control on the User Control Designer.

   5. In Solution Explorer, right-click ConfigMgrControl.cs, and then click View Source.

   6. Add the following code to the InitializePageControl method:

        textBox1.DataBindings.Add("Text", PropertyManager["Name"],
        "StringValue");

   7. In Solution Explorer, right-click ConfigMgrPropertySheet.cs, and then click View
      Designer.

   8. Double-click the text box you added. A new event handler, TextChanged , is created.

   9. In textBox1_TextChanged, add the following code to set the dirty flag when text is
      changed: Dirty = true;

<!-- p.820 -->

 10. Build the project and copy the assembly to %ProgramFiles%\Microsoft Endpoint
     Manager\AdminConsole\bin.

 11. Open the Configuration Manager console, and navigate to the Packages node
     under Software Distribution.

 12. Right-click a package, and then click Show My Property Sheet.

     In the property sheet that is displayed, the text box displays the name of the
     selected package.

 13. Type a new name for the package, and then click OK.

     In the Configuration Manager console results pane, the package name is changed
     to the name you entered.

See Also
How to Use Objects Passed to a Configuration Manager Forms
About Configuration Manager Forms

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.821 -->

About Configuration Manager Console
Management Classes
Article • 10/04/2022

Configuration Manager uses XML to define management classes whose instances
contain data that can be viewed from within the Configuration Manager console.
Custom management classes can be created and added within the console architecture.

The XML for a management class defines the name and the properties of the class.

For information about node XML, see Configuration Manager Console Management
Class XML.

See Also
About Configuration Manager console actions About console forms About console
views How to Create a Configuration Manager Administrator Console Node
How to Find a Configuration Manager Node GUID
Configuration Manager Console Node XML

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.822 -->

Configuration Manager Console
Management Class XML
Article • 10/04/2022

The management classes XML for the Configuration Manager console are located
%ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\XmlStorage\ConsoleRoot\ManagementClassDescriptions.xml
file. Your extension management class XML files, however, must be placed in the
AdminConsole\XmlStorage\Extensions\ManagementClasses\ folder.

The following XML defines an extension management class called "MyClass". The
"MyClass" node is a subclass of the SMS_SiteControlItem management class, which is
defined in the ConsoleRoot\ManagementClassDescriptions.xml.

  <ManagementClassDescription Name="MyClass"
  SuperclassName="SMS_SiteControlItem" SecurityObjectAlias="SMS_Site">
  <Properties>          <ManagementClassPropertyDescription Name="RoleName"/>
  <ManagementClassPropertyDescription Name="SiteCode" />     </Properties>
  </ManagementClassDescription>

You can also expose your own custom management class that is defined within an
assembly. For example, the XML below defines a management class called _SDK . The
_SDK class is defined in a custom assembly. Note that the management class must be

defined using .NET from within the referenced assembly.

  <ManagementClassDescription Name="_SDK">        <Properties>
  <ManagementClassPropertyDescription Name="MyProperty1"/>
  <ManagementClassPropertyDescription Name="MyProperty2"/>
  <ManagementClassPropertyDescription Name="MyProperty3"/>       </Properties>
  <ResourceAssembly>         <Assembly>UIExtensionsDemo.dll</Assembly>
  <Type>UIExtensionsDemo.ConnectionManager._SDK.resources</Type>
  </ResourceAssembly>       <ImagesDescription>           <ResourceAssembly>
  <Assembly>UIExtensionsDemo.dll</Assembly>
  <Type>UIExtensionsDemo.Resources.resources</Type>    </ResourceAssembly>
  <ImageResourceName>ViewIcon</ImageResourceName>       </ImagesDescription>
  </ManagementClassDescription>

See also

<!-- p.823 -->

About console management classes

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.824 -->

About Configuration Manager Console
Nodes
Article • 10/04/2022

Configuration Manager uses XML to define the nodes and their content, that you see in
the Configuration Manager console. New nodes can be added anywhere in the existing
node hierarchy.

The XML for a node describes the navigation pane, results pane, and action pane, and
the resources that are needed by each pane to display the node.

When writing a new node, consider the following:

      The position of the node in the hierarchy. Each node is uniquely identified by a
      GUID. For an example, see How to Create a Configuration Manager Administrator
      Console Node.

      The node hierarchy. The node structure is hierarchical, and you can nest nodes as
      deeply as you require. You can also use regular expressions to determine whether
      a node should be displayed. For an example, see How to Create a Configuration
      Manager Administrator Console Node.

      Actions. You can define actions that the user selects in the Configuration Manager
      console. You can use an action to launch forms, run programs, call methods, show
      reports, and define action menus. For more information, see Configuration
      Manager Actions.

      Queries. You can define queries that populate the navigation pane and results
      pane with SMS Provider objects. You can specify regular expressions to pick the
      properties that are displayed from the objects queried. For an example, see
      Configuration Manager Administrator Console RootNodes Element.

      Security. You can secure a node based on security flags that you specify. For an
      example that sets security for an action, see Configuration Manager Conditional
      Actions.

      Views. You can launch views in the Configuration Manager console at desired
      nodes. For more information about views, see About console views.

  ７ Note

<!-- p.825 -->

  The Configuration Manager SDK includes a sample XML file and GUID folder for a
  node that displays the available collections. The GUID folder is the namespace
  identifier for the tools node

For information about node XML, see Configuration Manager Console Node XML.

See Also
About Configuration Manager console actions About console forms About console
views How to Create a Configuration Manager Administrator Console Node
How to Find a Configuration Manager Node GUID
Configuration Manager Console Node XML

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.826 -->

Configuration Manager Console Node
XML
Article • 10/04/2022

The node XML for the Configuration Manager console is in workspace XML files located
in the %ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\XmlStorage\ConsoleRoot\ folder. Your extension node XML
files, however, are placed in the folder AdminConsole\XmlStorage\Extensions\Nodes\
<GUID>, where <GUID> is the namespace GUID identifier for the parent node.

The following XML defines an extension node called "MyNode". The "MyNode" node is
defined as a child of the Site Configuration node (d61498cb-7b3f-4748-ae3e-
026674fb0cbd) in the Administration workspace of the Configuration Manager console.
"MyNode" is associated with a
Microsoft.ConfigurationManagement.AdminConsole.ConsoleView.ViewDescription
type which is a grid view that ships with Configuration Manager. When the node is
selected, it will cause a grid view to appear in the view panel. The grid view displays two
properties (RoleName and SiteCode) of each MyClass custom management class
instance that is returned by the WQL query.

  ７ Note

  The UIExtensionsDemo.dll referenced below is an example of referencing a custom
  assembly.

  <RootNodeDescription NamespaceGuid="d61498cb-7b3f-4748-ae3e-026674fb0cbd"
  Id="MyNode" DisplayName="NodeName" Description="NodeDescription">
  <ResourceAssembly>     <Assembly>UIExtensionsDemo.dll</Assembly>
  <Type>UIExtensionsDemo.Resources.resources</Type> </ResourceAssembly>
  <ImagesDescription>     <ResourceAssembly>
  <Assembly>UIExtensionsDemo.dll</Assembly>
  <Type>UIExtensionsDemo.Resources.resources</Type>      </ResourceAssembly>
  <ImageResourceName>NodeIcon</ImageResourceName> </ImagesDescription>
  <ViewAssemblyDescriptions>     <ViewAssemblyDescription>
  <Assembly>AdminUI.ConsoleView.dll</Assembly>
  <Type>Microsoft.ConfigurationManagement.AdminConsole.ConsoleView.ViewDescrip
  tion</Type>      <CustomData>         <ConfigurationData
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <PropertyItemsData>                 <Properties>

<!-- p.827 -->

  <string>RoleName</string>                       <string>SiteCode</string>
  </Properties>                      <ClassName>MyClass</ClassName>
  </PropertyItemsData>            </ConfigurationData>        </CustomData>
  </ViewAssemblyDescription>    </ViewAssemblyDescriptions> <Actions>
  </Actions>    <Queries>    <QueryDescription NamespaceGuid="81957874-9c03-
  4261-84eb-3cf6c31bf251" Type="WQL">              <Query>SELECT * FROM
  SMS_SCI_SysResUse</Query>
  <ReturnedClassType>MyClass</ReturnedClassType>         </QueryDescription>
  </Queries>\</RootNodeDescription>

The important elements are:

                                                                          ﾉ   Expand table

 Element                                     Description

 RootNodeDescription                         Describes the root node for the node.

 Configuration Manager Console RootNodes     Root node for describing the node.
 Element

 NodeDescription                             Parent for nodes describing the tree view and
                                             result pane.

 RootNodeDescription.resourceAssembly        The assembly from which to load resources
                                             for this node instance.

 ActionDescription.imageDescription          The assembly containing the icon and other
                                             image resources used by the node.

 ActionDescription.viewAssemblyDescription   The view type of the node.

Node hierarchy
Define cascading nodes in the following manner:

  XML

  <RootNodeDescription>
    <ChildNodes>
        <RootNodeDescription>
                 <ChildNodes>
                 ...
                 </ChildNodes>
        </RootNodeDescription>
    </ChildNodes>
  </RootNodeDescription>

<!-- p.828 -->

See also
How to Create a Configuration Manager Console Node About console nodes

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.829 -->

Configuration Manager Console
RootNodes Element
Article • 10/04/2022

RootNodes elements are the topmost nodes for a feature. For example, software

distribution.

The RootNodes element is responsible for rendering a node. It defines the queries and
layout that are used to display the results pane and any dynamic nodes that are added
to the Configuration Manager console tree node. The NodeDescription node defines
these user interface elements.

A root node has one type of child node, <ChildNodes>.

Child Nodes
ChildNode elements are static nodes that appear under the root node for a feature. For

example, Packages is a child node of the software distribution node. Child nodes appear
under the ChildNodes node and each child node is described by a RootNodeDescription
node. Each child node may have further child nodes described in a child RootNode
element.

Describing the Tree View Pane and Results Pane
As a child of RootNodes , NodeDescription provides a description of the tree view pane
and results pane used in the Configuration Manager console. NodeDescription includes
the following three child elements:

      QueryDescription

      DetailsPaneDescription

QueryDescription
The QueryDescription element can be used to query the SMS Provider for objects to be
displayed in the node. The QueryDescription element includes the following attributes:

                                                                        ﾉ   Expand table

<!-- p.830 -->

 Attribute           Description

 NamespaceGuid       The node that the query applies to.

 Type                The type of the query. Typically this is a WQL query.

 DisplayName         Displays text strings for the name and description in the Configuration
 Description         Manager console. Typically, though you will use the results of the query. The
                     code examples in the next section display the name property of the
                     collection.

The following elements are some of the child elements of QueryDescription :

                                                                                  ﾉ   Expand table

 Element                Description

 Query                  The WQL query that is used to populate the node.

 ReturnedClassType      The type of the Configuration Manager or custom object returned.

DetailPaneDescription
The DetailsPaneDescription element is used to define the details panel associated with
a particular node. The DetailsPaneDescription element includes the following attributes:

                                                                                  ﾉ   Expand table

 Attribute              Description

 ObjectClass            The object type that the details pane applies to.

The following elements are some of the child elements of DetailsPaneDescription :

                                                                                  ﾉ   Expand table

 Element                Description

 PanePageDescription    Defines the details page that should load in the details pane. Includes the
                        assembly where the page is located, the page title, and query that should
                        be run in order to retrieve any data for display.

Below is an XML example of a DetailsPaneDescription element definition. The details
pane is targeted at a SMS_Package type and returns all SMS_Package objects that are

<!-- p.831 -->

included in the selected SMS_Package object. The returned collection is then displayed in
a grid view. The properties for display are defined in the PropertyList element.

  <DetailsPaneDescription ObjectClass="SMS_Package">     <PanePageDescription
  ObjectClass="SMS_Package" PageGuid="ce027fe6-ffd8-4825-ad7b-029c39e97327"
  Description="ProgramsTabDescription">    <ResourceAssembly>
  <Assembly>AdminUI.Program.dll</Assembly>
  <Type>Microsoft.ConfigurationManagement.AdminConsole.Program.Properties.Reso
  urces.resources</Type>    </ResourceAssembly>
  <PageTitle>ProgramsTabName</PageTitle>    <QuerySettingsDescription
  QueryClass="SMS_Program">     <Queries>       <QueryDescription
  NamespaceGuid="d13e9848-2c76-418c-ab96-9a2940aaf0de" Type="WQL"
  DisplayName="##SUB:ProgramName##" Description="##SUB:ProgramName##">
  <Query>SELECT * FROM SMS_Program WHERE PackageId='##SUB:PackageId##'</Query>
  <ReturnedClassType>SMS_Program</ReturnedClassType>          <Actions>
  </Actions>      </QueryDescription> </Queries>     <PropertyList>
  <PropertyDescription Name="ProgramName" />        <PropertyDescription
  Name="CommandLine" />        <PropertyDescription Name="Run" />
  <PropertyDescription Name="DiskSpaceReq" />       <PropertyDescription
  Name="Comment" />     </PropertyList>   </QuerySettingsDescription>
  </PanePageDescription></DetailsPaneDescription>

See Also
How to Create a Configuration Manager Administrator Console Node
About Configuration Manager Administrator Console Nodes
How to Find a Configuration Manager Node GUID

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.832 -->

Configuration Manager Console
ResourceAssembly Element
Article • 10/04/2022

In Configuration Manager, the ResourceAssembly element defines the resources that are
used by the node. The following XML defines the assembly,
AdminUI.CollectionProperty.dll , and the type of the resource within the assembly.

  <ResourceAssembly>
      <Assembly>AdminUI.CollectionProperty.dll</Assembly>

  <Type>Microsoft.ConfigurationManagement.AdminConsole.CollectionProperty.Prop
  erties.Resources.resources</Type>
  </ResourceAssembly>

See Also
About Configuration Manager Administrator Console Nodes
How to Find a Configuration Manager Node GUID
Configuration Manager Console Node XML

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.833 -->

How to Create a Configuration Manager
Console Node
Article • 10/04/2022

In Configuration Manager, to create a Configuration Manager console node, you create
an XML description of the node and add it to the %ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\Extensions\Nodes\<GUID> folder. GUID is the GUID
namespace for the parent node.

The following procedure shows how to add a new node to the Configuration
ManagerSite Configuration node. The new node displays the available collections.

To create a Configuration Manager console node
   1. If the Configuration Manager console is open, close it.

   2. In the Configuration Manager SDK, locate the XML file, CollectionsNode.XML.

   3. If it does not already exist, create a folder named Nodes in
      %ProgramFiles%\AdminConsole\XmlStorage\Extensions\.

   4. In the Nodes folder, create a folder named d61498cb-7b3f-4748-ae3e-026674fb0cbd .
      This GUID identifies the Site Configuration node.

   5. Copy the XML file to the GUID folder.

   6. Start the Configuration Manager console, and in the console tree, navigate to the
      Site Configuration node. You should see a new Collections node.

See Also
About Configuration Manager Administrator Console Nodes
Configuration Manager Console Node XML
How to Find a Configuration Manager Node GUID

Feedback
Was this page helpful?    Yes    No

<!-- p.834 -->

Provide product feedback

<!-- p.835 -->

How to find a Configuration Manager
console node GUID
Article • 10/04/2022

Globally Unique Identifiers (GUIDs) are used to identify parts of the Configuration
Manager console. For example, the action you create in How to Create a Configuration
Manager Action is placed on the Site Configuration node in the console tree view by
using the GUID 9770fc1b-0885-40e7-8a83-5dfc5eaaa8c2.

Elements that contain the namespaceGuid attribute are part of the console. For example,
the following element declares the software updates node:

<RootNodeDescription NamespaceGuid="392b72f3-1c83-42e1-90ed-611798bc0dd0"

Id="SmsSoftwareUpdatesNode" DisplayName="SUMName" Description="SUMDescription"
HelpTopic="9af099dc-3713-463d-bd50-0e4cd07c48fb">

Determining the correct GUID for your Configuration Manager console extension to use
can be difficult because you must navigate through console root XML files to the correct
element.

One approach is to open any of the console root XML files in Visual Studio and collapse
all the XML nodes. After the XML is collapsed, expand ConsoleNodesRootDescription and
then RootNodeDescription .

RootNodeDescription contains further RootNodeDescription elements for each of the

major Configuration Manager features displayed in the Configuration Manager console
tree view. By expanding these nodes, you can navigate to the required part of the
Configuration Manager console and get the GUID from the appropriate XML element.

Namespace GUIDs can be associated with several types of elements. For more
information, see Configuration Manager Console Node XML.

See also
About console nodes Configuration Manager Console Node XML

Feedback

<!-- p.836 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.837 -->

About Configuration Manager Console
Views
Article • 10/04/2022

Configuration Manager console views are displayed in the results pane of the
Configuration Manager console. You can create your own views and make them
available anywhere in the tree view hierarchy.

Creating the View Assembly
To create a view, you must define a class within that implements the IConsoleView2
interface.

After you create the class and build the assembly, place it in the
%ProgramFiles%\Microsoft Endpoint Manager\AdminConsole\bin folder where it is
loaded by the Configuration Manager console.

For more information, see How to Create a Configuration Manager Administrator
Console View.

Creating the Node XML
The view is integrated into the Configuration Manager console when you create an XML
file that describes the location, queries, actions, and resources that are needed for the
node that displays the view. The node XML file is placed in the
%ProgramFiles%\Microsoft Endpoint
Manager\AdminConsole\ConsoleRoot\Extensions\Nodes folder, under a folder that is
named with the GUID of the parent node for the node.

For more information, see How to Create Node XML for a Configuration Manager
Administrator Console View.

For more information about node XML, see About console nodes.

Help

F1 Help

<!-- p.838 -->

You can add F1 Help support to your views by specifying the HelpID attribute of the
view QueryDescription element in the node XML. In the HelpID attribute you specify the
path to the .chm file and the topic that you want to display in the following format:

HelpID="<path to chm>::<path to topic><topic name>.htm"

For example, the following QueryDescription element declaration loads the "How to
Create a Package" topic from the Configuration Manager .chm. The .chm is assumed to
be in c:\chm.

  ７ Note

  The assembly referenced below (ConfigMgrObjectsControl.dll) is created in the
  How to Create a Configuration Manager Console Custom View.

  <ViewAssemblyDescriptions>     <ViewAssemblyDescription>          <Assembly>
  ConfigMgrObjectsControl.dll </Assembly>         <Type>
  Microsoft.ConfigurationManagement.AdminConsole.ConfigMgrObjectsView.ConfigMg
  rObjectsViewDescription </Type>    <CustomData>             <ConfigurationData
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <PropertyItemsData>                <Properties>
  <string>MyProperty1</string>            <string>MyProperty2</string>
  </Properties>                     <ClassName>_SDK</ClassName>
  </PropertyItemsData>    </ConfigurationData>           </CustomData>
  </ViewAssemblyDescription>    </ViewAssemblyDescriptions>    <Actions>
  </Actions>    <Queries>      <QueryDescription NamespaceGuid="a4b9867e-8fc8-
  4fae-8a1a-0c798c22e010" Type="WQL"
  HelpTopic="C:\chm\SystemCenterConfigurationManager_SDK.chm::/html/2c295b3b-
  e23c-4084-ad4a-8bba328ef6fc.htm">           <Query>GetData</Query>
  <ReturnedClassType>_SDK</ReturnedClassType>          <Actions>
  <ActionDescription Class="ShowDialog" DisplayName="ShowDialogActionName"
  Description="ShowDialogActionDescription">                  <ShowOn>
  <string>DefaultHomeTab</string>
  <string>ContextMenu</string>               </ShowOn>
  <ResourceAssembly>
  <Assembly>UIExtensionsDemo.dll</Assembly>
  <Type>UIExtensionsDemo.Resources.resources</Type>
  </ResourceAssembly>              <ImagesDescription>
  <ResourceAssembly>
  <Assembly>UIExtensionsDemo.dll</Assembly>
  <Type>UIExtensionsDemo.Resources.resources</Type>      </ResourceAssembly>
  <ImageResourceName>ActionIcon</ImageResourceName> </ImagesDescription>
  <DialogId>MyDialog</DialogId>           </ActionDescription>       </Actions>
  </QueryDescription> </Queries>

<!-- p.839 -->

For more information about using the QueryDescription element, see How to Create
Node XML for a Configuration Manager Console View.

Custom Help
You can also display your own .chm outside of the F1 Help system. For example, you can
add a button to your form that opens your Help .chm. For more information about
opening Help from Windows forms, see the Help class in the .NET Framework Class
Library.

See Also
About console extensions How to Create a Configuration Manager Console
How to Create Node XML for a Configuration Manager Console View

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.840 -->

How to Create a Configuration Manager
Console Custom View
Article • 10/04/2022

In Configuration Manager, to create a custom console view, you must create two .NET
Framework classes. If you do not wish to create your own custom view control, see How
to Create Node XML for a Configuration Manager Console View for more information.

The following procedure creates a view that displays a custom control. In this case, the
view displays the string content of a label control.

The procedures in this topic create a "My View" console extension node that displays.
beneath the Site Configuration console node in the Administration workspace. When
you click the "My View" node, your custom view control will load into the Configuration
Manager console.

Creating a Custom View
The following procedures create an extension node with a custom view control.

Create the View Controller Class
The following procedure creates the OverviewControllerBase derived class. The
controller class's Content property is set contain your custom control. In the example
below, the Content property is assigned a simple label control.

To create a console view class

      Create the following new class. In this case, your custom control is a simple label
      control:

        public class MyViewController : OverviewControllerBase{   public
        MyViewController(): base()   {}   public override void EndInit()   {
        base.EndInit();     this.Content = new Label() { Content = "My Content"
        };   }}

Create the View Description Class
