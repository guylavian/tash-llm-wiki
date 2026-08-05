---
title: "Configuration Manager SDK documentation — pages 561-600"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0561-0600
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0561-0600
family: sccm
documentKind: "doc"
abstract: "A complete sample project implementing a custom deployment type for Remote Desktop Protocol (*.rdp) files is provided separately for reference. The discussion throughout the Extending Application Management section leverages the Remote Desktop Protocol sample project for example"
---

# Configuration Manager SDK documentation — pages 561-600

<!-- p.561 -->

 A complete sample project implementing a custom deployment type for Remote
 Desktop Protocol (*.rdp) files is provided separately for reference. The discussion
 throughout the Extending Application Management section leverages the Remote
 Desktop Protocol sample project for examples and illustration.

Overview

Server
 1. Create a Custom SDK Assembly

    The custom SDK assembly contains an interface implementation of both the
    Hosting Technology and Installer Technology. The AssemblySuffix should
    correspond to whatever is specified for AssemblySuffix attribute in the
    DeploymentTechnology.xml file, for example
    Microsoft.ConfigurationManagement.ApplicationManagement.
    <AssemblySuffix>.dll.

    a. Deployment Technology - The DeploymentTechnology class is the object that is
       registered with the Configuration Manager Application Model SDK. When
       implementing a new deployment technology you must implement a class that
       derives from this class. The new class instance will define the deployment
       technology used to deploy a specific application to devices.

    b. Hosting Technology - The HostingTechnology class is used to define run time
       interaction and configuration for technologies.

    c. Installer Technology – The InstallerTechnology class is used to define specific
       metadata about the detection, installation and uninstallation of the application.

    d. Installer – The Installer class is used to define properties and methods used on
       the client to actually detect, install and uninstall the application.

    e. Content Importer - The ContentImporter class is used to allow custom
       technologies to be able to read a specific content file and create the
       corresponding DeploymentType object using information obtained from the
       content file. For example, the Windows Installer content importer reads
       Windows Installer files (*.msi) and is able to populate Title, Description
       properties of the Installer DeploymentType object and create the Detect, Install
       and Uninstall actions for the Installer.

<!-- p.562 -->

      f. Resources – To support the Installer, a custom XML schema should be included
        as part of the assembly. The schema file (XSD) file must be included as a
        resource in the assembly.

   2. Create the Registration XML Files

     As part of defining a custom application management deployment technology,
     create three registration files/digests. These registration files/digests are used to
     register the Deployment Technology with Configuration Manager.

     a. DeploymentTechnology.xml - Digest of the Deployment Technology.

     b. HostingTechnology.xml - Digest of the Hosting Technology.

      c. InstallerTechnology.xml - Digest of the Installer Technology.

   3. Create the UI Extension

     To extend the Configuration Manager console, create a UX assembly, custom
     property sheets and wizards.

     The assembly should correspond to following naming convention:
     AdminUI.DeploymentType.<AssemblySuffix>.dll.

     a. AdminUI.DeploymentType.<AssemblySuffix>.dll

        Required – Contains UX implementation, which is then bound to the
        Configuration Manager console using the following XML files:

     b. CreateApp_<TechnologyId>.xml

        Required – Extension XML for the Create Application Wizard.

      c. CreateDeploymentWizard_<TechnologyId>.xml

        Required - Extension XML for the Deployment Type Wizard.

     d. <TechnologyId>DeploymentTypePropertySheet.xml

        Required - Standard Property Page XML for the Deployment Type property
        page.

Client
The client extension is accomplished through extending WMI and adding a custom
handler (public COM class and methods). It should be noted that the client extension

<!-- p.563 -->

closely maps to the Installer object, defined as part of the DeploymentType. Property
values are stored in WMI and the public COM methods map to detection, installation
and uninstallation.

   1. Create an AppSynclet MOF File

     To define a custom synclet MOF file, create an instance of the CCM_AppHandlers
     class. The new class instance will identify the custom client-side handler.
     Additionally, create instances of the CCM_HandlerSynclet class which will store
     install, uninstall and detect property values which can be used by the
     corresponding client-side handler methods.

   2. Create a Client-side Handler

     The custom client-side handler needs to implement a public COM interface and
     methods (InstallApp, UninstallApp and DiscoveryApp). The methods will be called
     by the Configuration Manager client framework. However, the actual functionality
     of the methods is defined by the client-side handler developer.

Installation
   1. How to Create the Configuration Manager Deployment Type Extension File
     (*.cmdtx)

      a. Create an empty directory to stage its contents

     b. Create and copy the following files into this directory:

         i. DeploymentTechnology.xml - A digest of the Deployment Technology

         ii. HostingTechnology.xml - A digest of the Hosting Technology

        iii. InstallerTechnology.xml - A digest of the Installer Technology

        iv. The custom SDK Assembly
           (Microsoft.ConfigurationManagement.ApplicationManagement.
           <AssemblySuffix>.dll) - Contains interface implementation of both the
           Hosting Technology and Installer Technology Note: the AssemblySuffix
           should correspond to whatever is specified for AssemblySuffix attribute in
           the DeploymentTechnology.xml file.

         v. HostingApplication.zip - Optional. Importable application that represents the
           Hosting Application, which includes content (if any). This should be created
           using the Export feature on the Applications node, in the Configuration
           Manager console.

<!-- p.564 -->

     vi. HandlerApplication.zip - Optional. Importable application that represents the
        Handler Application for the client, which includes content (if any). This should
        be created using the Export feature on the Applications node, in the
        Configuration Manager console.

   c. Use the method DeploymentTypeExtender.CreateExtension, which is located in
     Microsoft.ConfigurationManagement.ApplicationManagement namespace, to
     create the Deployment Type Extension (*.cmdtx) file based on the content in the
     staging directory.

       // Summarizes progress from CreateExtension method to a log file or
       the console.
       // <param name="summaryText">Summary text to be presented</param>
       public void Summarize(string summaryText)
       {
             System.Console.WriteLine(summaryText);
             return;
       }
       // Creates a new Deployment Type Extension using the specified
       source path
       // <param name="sourcePath">Source path used to create the
       Deployment Type Extension</param>
       // <param name="deploymentTypeExtensionFilePath">Resulting
       Deployment Type Extension file</param>
       private void CreateDeploymentTypeExtensionFile(string sourcePath,
       string deploymentTypeExtensionFilePath)
       {
             DeploymentTypeExtender.CreateExtension(sourcePath,
       deploymentTypeExtensionFilePath, this.Summarize);
             return;
       }

2. How to Create the Windows Installer File (*.msi)

  After the *.cmdtx is created, create a Windows Installer file (*.msi) which contains
  the *.cmdtx file and UX files. The Installer will be responsible for installing the UX
  files in the correct locations.

  a. Install the UX files in the correct locations. Basically, this will involve including
     the following files (with respect to Deployment Type Extensions):

      i. AdminUI.DeploymentType.<AssemblySuffix>.dll

        Required – Contains UX implementation, which is then bound to the
        Configuration Manager console using the following XML files:

<!-- p.565 -->

        ii. CreateApp_<TechnologyId>.xml

          Required – Extension XML for the Create Application Wizard.

       iii. CreateDeploymentWizard_<TechnologyId>.xml

          Required - Extension XML for the Deployment Type Wizard.

       iv. <TechnologyId>DeploymentTypePropertySheet.xml

          Required - Standard Property Page XML for the Deployment Type property
          page.

     b. Register the *.cmdtx

       The Windows Installer file (*.msi) should contain code/script to invoke the
       DeploymentTypeExtender.Extend method, which is located in the
       Microsoft.ConfigurationManagement.ApplicationManagement namespace. This
       will then register the extension files for a given site server computer. For a
       Configuration Manager administrator console computer, this will initialize the
       cache for that user.

          using DCM =
          Microsoft.ConfigurationManagement.AdminConsole.DesiredConfigurationM
          anagement;
           [...]
              ConnectionManagerBase connectionManager = new
          WqlConnectionManager();
              connectionManager.Connect("SiteServerName");
              DeploymentTypeExtender.Extend(@"C:\PartnerTechnology.cmdtx", new
          DCM.ConsoleDcmConnection(connectionManager, null),
          @"\\SiteServerName\root\sms\site_SITECODE");

Namespaces
Microsoft.ConfigurationManagement.AdminConsole

Microsoft.ConfigurationManagement.AdminConsole.AppManFoundation

Microsoft.ConfigurationManagement.AdminConsole.CreateDT

Microsoft.ConfigurationManagement.AdminConsole.DesiredConfigurationManagement

Microsoft.ConfigurationManagement.ApplicationManagement

<!-- p.566 -->

Microsoft.ConfigurationManagement.ApplicationManagement.Serialization

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.ConnectionManagerBase

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assemblies
AdminUI.AppManFoundation

AdminUI.CreateDT

AdminUI.DcmObjectWrapper.dll

AdminUI.WqlQueryEngine.dll

Microsoft.ConfigurationManagement.exe

Microsoft.ConfigurationManagement.ApplicationManagement.dll

Microsoft.ConfigurationManagement.ApplicationManagement.Extender.dll

Microsoft.ConfigurationManagement.ManagementProvider.dll

See Also
Configuration Manager Reference

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.567 -->

How to Define the Deployment
Technology
Article • 10/04/2022

To define a custom application management deployment technology, implement the
Microsoft.ConfigurationManagement.ApplicationManagement.DeploymentTechnology class.

The new class instance will define the deployment technology used to deploy a specific
application to devices.

The DeploymentTechnology class is the object that is registered with the Configuration
Manager Application Model SDK. The DeploymentTechnology class contains references
to three different types of objects that compose the technology. When implementing a
new deployment technology you must implement a class that derives from this class.

In the Remote Desktop Protocol (RDP) sample project, a new deployment technology is
required for Remote Desktop Protocol (RDP) files. Deployment support for RDP files is
not built in to Configuration Manager, so a custom deployment technology is required.

  ） Important

  The DeploymentTechnology class name must match the class specified in the
  DeploymentTechnology.xml file.

To define a custom deployment technology
   1. Implement the
      Microsoft.ConfigurationManagement.ApplicationManagement.DeploymentTechnology

      class using the
      Microsoft.ConfigurationManagement.ApplicationManagement.DeploymentTechnology

      constructor. The string parameters are string values that uniquely identify the RDP
      Deployment Technology.

        ７ Note

        The class constructor requires multiple instances of the string parameter that
        identifies the technology.

<!-- p.568 -->

     The following example from the RDP sample project demonstrates how to define a
     deployment technology.

       namespace Microsoft.ConfigurationManagement.ApplicationManagement
       {
           //    Deployment technology used by RDP files.
           public class RdpDeploymentTechnology : DeploymentTechnology
           {
               // Initializes a new instance of the "RdpDeploymentTechnology"
       class.
                 public RdpDeploymentTechnology()
                    : base(Common.TechnologyId, Common.TechnologyId,
       Common.TechnologyId)
               {
               }
           }
       }

     In the RDP sample project, the string parameter is defined as a constant in the
     Common class of the local project.

       //   Internal ID of the technology.
       public const string TechnologyId = "Rdp";

Namespaces

Microsoft.ConfigurationManagement.ApplicationManagement

Microsoft.ConfigurationManagement.ApplicationManagement.Serialization

Assemblies
Microsoft.ConfigurationManagement.ApplicationManagement.dll

.NET Framework Security

See Also
How to Define the Hosting Technology
How To Define the Installer Technology

<!-- p.569 -->

Configuration Manager Reference

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.570 -->

How to Define the Hosting Technology
Article • 10/04/2022

To define a custom application management hosting technology, implement the
Microsoft.ConfigurationManagement.ApplicationManagement.HostingTechnology class. The

new class instance will define the hosting technology for a specific file type.

The HostingTechnology class supports run time interaction and configuration for
technologies. The class contains the hosting rules as defined in the
HostingTechnology.xml file. If needed, additional methods and properties can be added
to this class, though in most cases the existing base should be sufficient.

In the Remote Desktop Protocol (RDP) sample project, a new hosting technology is
required to handle Remote Desktop Protocol (RDP) files. Hosting support for RDP files is
not built in to Configuration Manager, so a custom hosting technology is required.

  ） Important

  The HostingTechnology class name must match the class specified in the
  HostingTechnology.xml file.

To define a custom hosting technology
   1. Implement the
      Microsoft.ConfigurationManagement.ApplicationManagement.HostingTechnology

      class using the
      Microsoft.ConfigurationManagement.ApplicationManagement.HostingTechnology

      constructor.

      In the example, a string constant, defined in the Common class of the local project,
      is used for the string parameter. While the boolean parameter
      ( Microsoft.ConfigurationManagement.ApplicationManagement.HostingTechnology.IsR
      emote ) is set directly to true.

      The following example from the RDP sample project demonstrates how to define a
      hosting technology.

  // Defines the hosting technology for RDP files. Hosting support for RDP
  files is not built in, so a custom

<!-- p.571 -->

  // hosting technology is needed on the client.
  public class RdpHostingTechnology : HostingTechnology
  {
      //   Initializes a new instance of the "RdpHostingTechnology" class.
      public RdpHostingTechnology()
         : base(Common.TechnologyId, true)
      {
      }
  }

In the RDP sample project, a string constant for the TechnologyId is defined in the
Common class of the local project.

  //   Internal ID of the technology.
  public const string TechnologyId = "Rdp";

Namespaces

Microsoft.ConfigurationManagement.ApplicationManagement

Microsoft.ConfigurationManagement.ApplicationManagement.Serialization

Assemblies
Microsoft.ConfigurationManagement.ApplicationManagement.dll

.NET Framework Security

See Also
How to Define the Deployment Technology
How To Define the Installer Technology
Configuration Manager Reference

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.572 -->

How To Define the Installer Technology
Article • 10/04/2022

To define the application management installer technology, implement the
Microsoft.ConfigurationManagement.ApplicationManagement.DeploymentTechnology.Instal

lerTechnology class. The new class instance will define the installer technology used to

install a specific application to devices.

The installer technology is a key extension point for extending the application model.
This class is used to define specific metadata about the installation and detection of the
technology on client systems concepts such as Detect, Install, and Uninstall.

In the Remote Desktop Protocol (RDP) sample project, a new installer technology is
required for Remote Desktop Protocol (RDP) files. Deployment support for RDP files is
not built-in to Configuration Manager, so a custom installer technology is required.

  ） Important

  The InstallerTechnology class name must match the class specified in the
  InstallerTechnology.xml file.

To define a custom installer technology
   1. Implement the InstallerTechnology class using the
      Microsoft.ConfigurationManagement.ApplicationManagement.InstallerTechnology

      constructor.

      The following example from the RDP sample project demonstrates how to define
      an installer technology.

        namespace RdpTechnology
        {
            //    Installer technology for RDP.
            public class RdpInstallerTechnology : InstallerTechnology
            {
                // Initializes a new instance of the "RdpInstallerTechnology"
        class.
                  public RdpInstallerTechnology()
                     : base(Common.TechnologyId, typeof(RdpInstaller),
        typeof(RdpContentImporter))
                {

<!-- p.573 -->

                  }
             }
        }

     In the RDP sample project, the string parameter is defined in the Common class.
     The RdpInstaller and RdpContentImporter classes are also defined in the RDP
     sample project.

        //    Internal ID of the technology.
               public const string TechnologyId = "Rdp";

Namespaces
Microsoft.ConfigurationManagement.ApplicationManagement

Microsoft.ConfigurationManagement.ApplicationManagement.Serialization

Assemblies

Microsoft.ConfigurationManagement.ApplicationManagement.dll

.NET Framework Security

See Also
How to Define the Deployment Technology
How to Define the Hosting Technology
Configuration Manager Reference

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.574 -->

How to Define the Content Importer
Article • 10/04/2022

To define the application management deployment technology content importer, use an
instance of the
Microsoft.ConfigurationManagement.ApplicationManagement.ContentImporter class. The

new class instance will define the content importer used by the installer.

The ContentImporter class provides an interface level design where custom technologies
can instantiate and populate DeploymentType objects for a specific technology. The
concept for this class is that the given technology importer is able read a specific
content file and create the corresponding DeploymentType object (with installer) using
information obtained from the content. For example, the Windows Installer technology
reads *.msi files and is able to populate Title, Description properties of the
DeploymentType object and create the Detect, Install and Uninstall actions for the
installer.

In the Remote Desktop Protocol (RDP) sample project, a new content importer is
required for Remote Desktop Protocol (RDP) files. Content import support for RDP files
is not built-in to Configuration Manager, so a custom content importer is required.

Basic Overview of Defining a Custom Importer

   1. Create a custom instance of the ContentImporter class.

   2. Override the FileTypes property and return the file types/extensions specific to the
      technology.

   3. Override the CreateDeploymentType method to create a custom deployment type
      by importing the required properties from a content file.

   4. Override the UpdateDeploymentType method to update a custom installer type
      with the settings from a content file.

   5. Helper functions: Include for completeness and to code readability are two helper
      functions. ProcessFileLine is a helper function called from the
      UpdateDeploymentType method to process each line of a content file and load the
      values to custom installer type. ParseType is a helper function called from the
      ProcessFileLine helper function. The ParseType helper function parses an .rdp file
      type designation and converts it into a .NET Type.

To define a custom content importer

<!-- p.575 -->

1. Create an instance of the
  Microsoft.ConfigurationManagement.ApplicationManagement.ContentImporter class

  using the
  Microsoft.ConfigurationManagement.ApplicationManagement.ContentImporter

  constructor.

  The following example from the RDP sample project demonstrates how to define
  an Content importer.

     //   Content importer for .rdp files used by the RDP installer.
     public class RdpContentImporter : ContentImporter

2. Override the
  Microsoft.ConfigurationManagement.ApplicationManagement.ContentImporter.FileTy

  pes property and define the file types supported by the content importer.

  The following example from the RDP sample project demonstrates how to override
  the FileTypes property.

     // File types supported by the content importer.
     public override IList<FileType> FileTypes
     {
         get
         {
              return Common.RdpFileTypes;
         }
     }

  In the RDP sample project, the FileTypes value is defined in the Common class of
  the project.

     //   This defines the file extensions supported by this content
     importer.
     internal static readonly FileType[] RdpFileTypes = new[] { new FileType
     { Name = "RDP", Description = "Remote Desktop Configuration profile",
     Extensions = new[] { "rdp" } } };

3. Override the
  Microsoft.ConfigurationManagement.ApplicationManagement.ContentImporter.Create

<!-- p.576 -->

  DeploymentType method to manage the creation of a custom deployment type by

  importing the required properties from a content file.

  The following example from the RDP sample project demonstrates how to override
  the CreateDeploymentType method.

    // Creates a new deployment type from a content file.
    public override DeploymentType CreateDeploymentType(string contentFile,
    object context)
    {
        Validator.CheckForNull(contentFile, "contentFile");
        DeploymentType deploymentType = new
    DeploymentType(Common.TechnologyId) { Title =
    Path.GetFileNameWithoutExtension(contentFile) };
        UpdateDeploymentType(deploymentType, contentFile);
        return deploymentType;
    }

  In the RDP sample project, the string parameter for DeploymentType is defined in
  the Common class of the local project.

    // Internal ID of the technology.
    public const string TechnologyId = "Rdp";

4. Override the
  Microsoft.ConfigurationManagement.ApplicationManagement.ContentImporter.Update
  DeploymentType method to update a deployment type with the settings from a

  content file.

  The following example from the RDP sample project demonstrates how to override
  the UpdateDeploymentType method.

    // Updates an existing deployment type installer with settings from
    content file.
    public override void UpdateDeploymentType(DeploymentType dt, string
    contentFile, object context)
    {
        Validator.CheckForNull(dt, "dt");
        Validator.CheckForNull(contentFile, "contentFile");
                    RdpInstaller installer = dt.Installer as RdpInstaller;
        if (null == installer)
        {

<!-- p.577 -->

            throw new ArgumentOutOfRangeException("dt", dt.Installer,
    @"Installer type is not supported by this content importer.");
        }
        if (false == File.Exists(contentFile))
        {
            throw new FileNotFoundException("Content file was not found: "
    + contentFile, contentFile);
        }
        string[] fileText = File.ReadAllLines(contentFile);
        fileText.ForEach(l => ProcessFileLine(l, installer));
        installer.Filename = Path.GetFileName(contentFile);
        installer.Contents.Clear();
        installer.Contents.Add(new Content());
        installer.Contents[0].Files.Add(new ContentFile());
        installer.Contents[0].Location =
    Path.GetDirectoryName(contentFile);
        installer.Contents[0].Files[0].Name =
    Path.GetFileName(contentFile);
        return;
    }

5. ProcessFileLine is a helper function called from the UpdateDeploymentType
  method to process each line of a content file and load the values to custom
  installer type.

    //   Processes a line in an .rdp file to set corresponding RdpInstaller
    properties.
    private static void ProcessFileLine(string line, RdpInstaller
    installer)
    {
    if (string.IsNullOrEmpty(line))
        {
            Trace.TraceInformation("Skipping line, it is empty.");
            return;
        }
        string[] elements = line.Split(':');
        if (elements.Length < 2)
        {
            Trace.TraceError("Unexpected elements length: {0}. Skipping.",
    elements.Length);
            return;
        }
        string elementName = elements[0];
        Type elementType = ParseType(elements[1]);
        string elementValueAsString = (elements.Length == 3) ? elements[2]
    : string.Empty;
        object elementValue = (false ==
    string.IsNullOrEmpty(elementValueAsString)) ?
    Convert.ChangeType(elementValueAsString, elementType) : null;
        Trace.TraceInformation("Name: {0} Type: {1} Value: {2} ({3})",
    elementName, elementType, elementValue, elementValueAsString);

<!-- p.578 -->

    if (string.IsNullOrEmpty(elementValueAsString) || null ==
elementValue)
    {
        Trace.TraceWarning("Could not parse element value. Skipping.");
        return;
    }
    switch (elementName.ToLowerInvariant())
    {
        case "username":
             installer.Username = elementValueAsString;
             break;
        case "redirectprinters":
             installer.RedirectPrinters = (1 == (int)elementValue);
             break;
        case "redirectsmartcards":
             installer.RedirectSmartCards = (1 == (int)elementValue);
             break;
        case "alternate shell":
             installer.RemoteApplication = elementValueAsString;
             break;
        case "keyboardhook":
             installer.KeyboardMode = (RdpKeyboardMode)
(int)elementValue;
             break;
        case "audiomode":
             installer.AudioMode = (RdpAudioMode)(int)elementValue;
             break;
        case "desktopheight":
             installer.DesktopHeight = (int)elementValue;
             break;
        case "desktopwidth":
             installer.DesktopWidth = (int)elementValue;
             break;
        case "full address":
             installer.FullAddress = elementValueAsString;
             string[] tokens = elementValueAsString.Split(':');
             ushort port = 0;
             if (tokens.Length > 1)
             {
                 bool canParse = ushort.TryParse(tokens[1], out port);
                 if (false == canParse)
                 {
                     Trace.TraceError("Improperly formatted port.
Skipping.");
                 }
                 installer.RemoteServerPort = port;
             }
             installer.RemoteServerName = tokens[0];
             break;
        case "screen mode id":
             int screenMode = (int)elementValue;
             if (screenMode == 1 || screenMode == 2)
             {
                 installer.FullScreen = (1 == screenMode) ? false :
true;

<!-- p.579 -->

                      }
                      else
                      {
                          Trace.TraceError("Invalid screen mode: {0}. Skipping.",
       screenMode);
                   }
                   break;
               default:
                   Trace.TraceWarning("Unrecognized property: {0}. Skipping",
       elementName);
                   break;
           }
       }

    ParseType is a helper function called from the ProcessFileLine helper function. The
    ParseType helper function parses an .rdp file type designation and converts it into
    a .NET Type.

       //   Helper Function: Parses a .rdp file type designation and converts
       into a .NET Type.
       private static Type ParseType(string type)
       {
       switch (type.ToLowerInvariant())
           {
               case "s":
                   return typeof(string);
               case "i":
                   return typeof(int);
               case "b":
                   return typeof(string);
               default:
                   Trace.TraceInformation("Unrecognized type: {0}.", type);
                   return typeof(string);
           }
       }

Namespaces

Microsoft.ConfigurationManagement.ApplicationManagement

Microsoft.ConfigurationManagement.ApplicationManagement.Serialization

Assemblies
Microsoft.ConfigurationManagement.ApplicationManagement.dll

<!-- p.580 -->

See Also
Configuration Manager Reference

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.581 -->

How to Define the Installer
Article • 10/04/2022

To define the application management deployment technology installer, use an instance
of the Microsoft.ConfigurationManagement.ApplicationManagement.Installer class. The
new class instance will define the properties and methods used on the client to actually
install the application.

The Installer class has three abstract methods (CreateDetectionAction,
CreateInstallAction, CreateUninstallAction) allowing the Installer to specify the Action
objects that will be used on the client for detection, installation and uninstall.

Corresponding client-side implementation is required for the end to end Installer to
work correctly. The client-side implementation is covered in How to Define the Client-
side Handler.

In the Remote Desktop Protocol (RDP) sample project, a new installer is required for
Remote Desktop Protocol (RDP). Installation support for RDP is not built-in to
Configuration Manager, so a custom installer is required.

Basic Overview of Defining a Custom Installer

   1. Create a custom instance of the
      Microsoft.ConfigurationManagement.ApplicationManagement.Installer class.

   2. Override the Technology property and return the TechnologyId string specific to
      the technology.

   3. Override the
      Microsoft.ConfigurationManagement.ApplicationManagement.Installer.CreateDetect
      Action method and create a custom detection method specific to the technology.

   4. Override the
      Microsoft.ConfigurationManagement.ApplicationManagement.Installer.CreateInstal

      lAction method and create a custom installation method specific to the

      technology.

   5. Override the
      Microsoft.ConfigurationManagement.ApplicationManagement.Installer.CreateUninst
      allAction method and create a custom uninstallation method specific to the

      technology.

<!-- p.582 -->

  6. Create the general properties required to install the custom technology on the
    client.

To define a custom installer
  1. Create an instance of the
    Microsoft.ConfigurationManagement.ApplicationManagement.Installer class using

    the Microsoft.ConfigurationManagement.ApplicationManagement.Installer
    constructor.

    The following example from the RDP sample project demonstrates how to create
    the custom class.

       //   Installer class for a specific technology. The Installer class
       defines properties and methods used on the client to actually install
       the application.
       public class RdpInstaller : Installer

  2. Override the
    Microsoft.ConfigurationManagement.ApplicationManagement.Installer.Technology

    property to return the correct value for the custom installer technology.

    The following example from the RDP sample project demonstrates how to override
    the Technology property.

       // RDP Installer Technology string
       public override string Technology
       {
           get
           {
               return Common.TechnologyId;
           }
       }

    In the RDP sample project, the string parameter for InstallerTechnologyId is
    defined as a constant in the Common class of the project.

       //     Internal ID of the technology.
               public const string TechnologyId = "Rdp";

<!-- p.583 -->

3. Override the
  Microsoft.ConfigurationManagement.ApplicationManagement.Installer.CreateDetect

  Action method and create a custom action specific to the custom technology.

  The following example from the RDP sample project demonstrates how to override
  the CreateDetectAction method.

    //   Creates an Action used for detection. On the client, this sequence
    is used to validate if the application is installed.
    public override Action CreateDetectAction()
    {
        Action detectionAction = new Action { Provider =
    Common.TechnologyId };

        detectionAction.Arguments.Add(new Argument("Filename",
    typeof(string), this.Filename));
        detectionAction.Arguments.Add(new Argument("InstallFolder",
    typeof(string), this.InstallFolder));
        detectionAction.Arguments.Add(new Argument("FullAddress",
    typeof(string), this.FullAddress));
        detectionAction.Arguments.Add(new Argument("RemoteApplication",
    typeof(string), this.RemoteApplication));
        detectionAction.Arguments.Add(new Argument("RemoteApplicationMode",
    typeof(bool), false));

         return detectionAction;
    }

4. Override the
  Microsoft.ConfigurationManagement.ApplicationManagement.Installer.CreateInstal
  lAction method and create a custom action specific to the custom technology.

  The following example from the RDP sample project demonstrates how to override
  the CreateInstallAction method.

    //   Creates an Action used for installation. On the client, this
    sequence defines the properties needed to install the application.
    public override Action CreateInstallAction()
    {
        Action installationAction = new Action { Provider =
    Common.TechnologyId };
        installationAction.Arguments.Add(new Argument("Filename",
    typeof(string), this.Filename));
        installationAction.Arguments.Add(new Argument("InstallFolder",
    typeof(string), this.InstallFolder));
        installationAction.Arguments.Add(new Argument("FullScreen",

<!-- p.584 -->

    typeof(int), (true == this.fullScreen) ? 1 : 0));
        installationAction.Arguments.Add(new Argument("DesktopWidth",
    typeof(int), this.desktopWidth));
        installationAction.Arguments.Add(new Argument("DesktopHeight",
    typeof(int), this.desktopHeight));
        installationAction.Arguments.Add(new Argument("AudioMode",
    typeof(int), (int)this.AudioMode));
        installationAction.Arguments.Add(new Argument("FullAddress",
    typeof(string), this.FullAddress));
        installationAction.Arguments.Add(new Argument("RemoteServerName",
    typeof(string), this.RemoteServerName));
        installationAction.Arguments.Add(new Argument("RemoteServerPort",
    typeof(int), this.RemoteServerPort));
        installationAction.Arguments.Add(new Argument("RemoteApplication",
    typeof(string), this.RemoteApplication));
        installationAction.Arguments.Add(new
    Argument("RemoteApplicationMode", typeof(bool), false));
        installationAction.Arguments.Add(new
    Argument("ConstructRdpOnClient", typeof(bool),
    this.ConstructRdpOnClient));
        installationAction.Arguments.Add(new Argument("KeyboardMode",
    typeof(int), (int)this.KeyboardMode));
        installationAction.Arguments.Add(new Argument("RedirectPrinters",
    typeof(int), (true == this.RedirectPrinters) ? 1 : 0));
        installationAction.Arguments.Add(new Argument("RedirectSmartCards",
    typeof(int), (true == this.RedirectSmartCards) ? 1 : 0));
        installationAction.Arguments.Add(new Argument("Username",
    typeof(string), this.Username));
        // Adds any references to content to the action.
        if (this.ConstructRdpOnClient == false && this.Contents.Count > 0)
        {
            foreach (Content content in this.Contents)
            {
                 installationAction.Contents.Add(new ContentRef(content));
            }
        }
        return installationAction;
    }

5. Override the
  Microsoft.ConfigurationManagement.ApplicationManagement.Installer.CreateUninst
  allAction method and create a custom action specific to the custom technology.

  The following example from the RDP sample project demonstrates how to override
  the CreateUninstallAction method.

    public override Action CreateUninstallAction()
    {
        Action uninstallAction = new Action { Provider =
    Common.TechnologyId };

<!-- p.585 -->

        uninstallAction.Arguments.Add(new Argument("Filename",
    typeof(string), this.Filename));
        uninstallAction.Arguments.Add(new Argument("InstallFolder",
    typeof(string), this.InstallFolder));
        return uninstallAction;
    }

6. Create addition properties and methods used on the client to install the custom
  technology.

  The following example from the RDP sample project demonstrates the creation of
  properties and methods used on the client to install the RDP application.

    // Default height for the RDP window.
    public const int DefaultDesktopHeight = 768;
    // Default width for the RDP window
    public const int DefaultDesktopWidth = 1024;
    // Default storage location for RDP files created using this Installer
    public const string DefaultInstallFolder =
    @"%USERPROFILE%\Desktop\Remote Desktop Connections";
    private RdpAudioMode audioMode;
    private bool constructRdpOnClient;private int desktopHeight;
    private int desktopWidth;
    private bool fullScreen;
    private string installFolder;
    private RdpKeyboardMode keyboardMode;
    private string filename;
    private bool redirectPrinters;
    private bool redirectSmartCards;
    private string remoteApplication;
    private string fullAddress;
    private string remoteServerName;
    private ushort remoteServerPort;
    private string username;
    // Audio mode for the RDP connection. The default is BringToComputer.
    public RdpAudioMode AudioMode
    {
        get
        {
            return audioMode;
        }
        set
        {
            SetProp("AudioMode", ref audioMode, value);
        }
    }
    // If true, the RDP file will be constructed locally on the client. If
    false, the RDP file will live on the server and will be downloaded as
    content.
    [Mandatory]

<!-- p.586 -->

public bool ConstructRdpOnClient
{
    get
    {
        return constructRdpOnClient;
    }
    set
    {
        SetProp("ConstructRdpOnClient", ref constructRdpOnClient,
value);
    }
}
// Height of the remote desktop window. This setting is ignored if
FullScreen = true.
[Default(DefaultDesktopHeight)]
public int DesktopHeight
{
    get
    {
        return desktopHeight;
    }
    set
    {
        SetProp("DesktopHeight", ref desktopHeight, value);
    }
}
// Width of the remote desktop window. This setting is ignored if
FullScreen = true.
[Default(DefaultDesktopWidth)]
public int DesktopWidth
{
    get
    {
        return desktopWidth;
    }
    set
    {
        SetProp("DesktopWidth", ref desktopWidth, value);
    }
}
// If true, full screen window will be used.
public bool FullScreen
{
    get
    {
        return fullScreen;
    }
    set
    {
        SetProp("FullScreen", ref fullScreen, value);
    }
}
// Directory on the client where the RDP file will be stored. This is
part of Detection.
[Mandatory][Default(DefaultInstallFolder)]

<!-- p.587 -->

public string InstallFolder
{
    get
    {
        return installFolder;
    }
    set
    {
        SetProp("InstallFolder", ref installFolder, value);
    }
}
// Keyboard mode to use for the RDP session. Default is <see cref =
"RdpKeyboardMode.FullScreenOnly" />
[Default(RdpKeyboardMode.FullScreenOnly)]
public RdpKeyboardMode KeyboardMode
{
    get
    {
        return keyboardMode;
    }
    set
    {
        SetProp("KeyboardMode", ref keyboardMode, value);
    }
}
// Name of the RDP profile. This is part of Detection.
[Mandatory]public string Filename
{
    get
    {
        return filename;
    }
    set
    {
        SetProp("Filename", ref filename, value);
    }
}
// If true, local printers will be redirected to the remote computer.
Default is true.
[Default(true)]public bool RedirectPrinters
{
    get
    {
        return redirectPrinters;
    }
    set
    {
        SetProp("RedirectPrinters", ref redirectPrinters, value);
    }
}
// If true, local smart cards will be redirected to the remote
computer. Default is true.
[Default(true)]
public bool RedirectSmartCards
{

<!-- p.588 -->

    get
    {
          return redirectSmartCards;
    }
    set
    {
          SetProp("RedirectSmartCards", ref redirectSmartCards, value);
    }
}
// Remote application to run. Setting to %WINDIR%\system32\notepad.exe
for example will remote only the notepad.exe application. If
unspecified, remote shell will be used. Default is unspecified.
public string RemoteApplication
{
    get
    {
        return remoteApplication;
    }
    set
    {
        SetProp("RemoteApplication", ref remoteApplication, value);
    }
}
// Remote server name for the RDP connection.
[MaxLength(254)]
public string RemoteServerName
{
    get
    {
        return remoteServerName;
    }
    set
    {
        SetProp("RemoteServerName", ref remoteServerName, value);
    }
}
// Remote server port for the RDP connection. Default is 3389.
public string FullAddress
{
    get
    {
        return fullAddress;
    }
    set
    {
        SetProp("FullAddress", ref fullAddress, value);
    }
}
//   Remote server port for the RDP connection. Default is 3389.
[Default((ushort)3389)][Range(Min = (ushort)1, Max = (ushort)65534)]
public ushort RemoteServerPort
{
    get
    {
        return remoteServerPort;

<!-- p.589 -->

             }
             set
             {
                   SetProp("RemoteServerPort", ref remoteServerPort, value);
             }
        }
        // RDP Installer Technology string
        public override string Technology
        {
            get
            {
                return Common.TechnologyId;
            }
        }
        //   Username to use for the remote desktop connection.
        public string Username
        {
            get
            {
                return username;
            }
            set
            {
                SetProp("Username", ref username, value);
            }
        }

Namespaces
Microsoft.ConfigurationManagement.ApplicationManagement

Microsoft.ConfigurationManagement.ApplicationManagement.Serialization

Assemblies

Microsoft.ConfigurationManagement.ApplicationManagement.dll

See Also
Configuration Manager Reference

Feedback
Was this page helpful?    Yes    No

<!-- p.590 -->

Provide product feedback

<!-- p.591 -->

How to Define the Resources
Article • 10/04/2022

To support the Installer, a custom XML schema should be included as part of the
assembly. The schema file (XSD) file must be included as a resource in the assembly.

  ） Important

  The custom XML schema name must use the following naming convention:

      1. <InstallerClassName>_XmlSchema.xsd

        In the case of the RDP sample, the Installer implementation is called
        RdpInstaller, therefore the XML schema file for that technology is called
        RdpInstaller_XmlSchema.xsd.

As part of the resource documentation, a localizable title and description the technology
should be created.

  ） Important

  The Title and Desciption should use the following naming conventions:

      1. <DeploymentTechnologyClassName>_Title
        2. <DeploymentTechnologyClassName>_Description

To define a custom schema file
   1. Create the custom schema file.

      The following example from the RDP sample project demonstrates how to define a
      custom schema file.

        XML

        <?xml version="1.0" encoding="utf-8"?>
        <xs:schema id="RdpInstaller" version="1" elementFormDefault="qualified"
        targetNamespace="http://schemas.microsoft.com/SystemsManagement/2009/Ap
        plicationManagement"
        xmlns="http://schemas.microsoft.com/SystemsManagement/2009/ApplicationM
        anagement" xmlns:xs="http://www.w3.org/2001/XMLSchema">
          <xs:complexType name="RdpInstaller">

<!-- p.592 -->

            <xs:complexContent mixed="false">
              <xs:extension base="Installer">
                <xs:sequence>
                  <xs:element name="InstallFolder" type="string256" />
                  <xs:element name="Filename" type="string256" />
                  <xs:element name="ConstructRdpOnClient" type="xs:byte" />
                  <xs:element name="FullAddress" type="string256" minOccurs="0"
       />
                 <xs:element name="RemoteApplication" type="string256"
       minOccurs="0" />
                 <xs:element name="FullScreen" type="xs:byte" minOccurs="0" />
                 <xs:element name="DesktopWidth" type="int" minOccurs="0" />
                 <xs:element name="DesktopHeight" type="int" minOccurs="0" />
                 <xs:element name="AudioMode" type="string64" minOccurs="0" />
                 <xs:element name="RemoteServerName" type="string64"
       minOccurs="0" />
                 <xs:element name="RemoteServerPort" type="string64"
       minOccurs="0" />
                 <xs:element name="KeyboardMode" type="int" minOccurs="0" />
                 <xs:element name="RedirectPrinters" type="xs:byte"
       minOccurs="0" />
                 <xs:element name="RedirectSmartCards" type="xs:byte"
       minOccurs="0" />
                 <xs:element name="Username" type="string64" minOccurs="0" />
                 <xs:element name="ContentFilename" type="string256"
       minOccurs="0" />
               </xs:sequence>
             </xs:extension>
           </xs:complexContent>
         </xs:complexType>
       </xs:schema>

Namespaces
Microsoft.ConfigurationManagement.ApplicationManagement

Microsoft.ConfigurationManagement.ApplicationManagement.Serialization

Assemblies

Microsoft.ConfigurationManagement.ApplicationManagement.dll

.NET Framework Security

See Also

<!-- p.593 -->

How to Define the Hosting Technology
How To Define the Installer Technology
Configuration Manager Reference

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.594 -->

How to Define the Deployment
Technology Registration File
Article • 10/04/2022

To define a deployment technology registration file, create an XML file based on the
http://schemas.microsoft.com/SystemCenterConfigurationManager/2009/AppMgmtDigest

schema. This registration file is Used in the installation process, and it registers the
custom deployment technology with Configuration Manager. The deployment
technology registration file is required for the installation of the custom deployment
technology.

To define the deployment technology registration file
   1. Create a deployment technology registration file.

      The following example from the RDP sample project demonstrates how to define a
      deployment technology registration file.

        <AppMgmtDigest
        xmlns="http://schemas.microsoft.com/SystemCenterConfigurationManager/20
        09/AppMgmtDigest" xmlns:xsi="http://www.w3.org/2001/XMLSchema-
        instance">
          <DeploymentTechnology AuthoringScopeId="GLOBAL"
        LogicalName="RdpDeploymentTechnology" TechnologyId="Rdp"
        AssemblySuffix="Rdp" Version="1">
            <HostingTechnology>GLOBAL/RdpHostingTechnology</HostingTechnology>

        <InstallerTechnology>GLOBAL/RdpInstallerTechnology</InstallerTechnology
        >
          </DeploymentTechnology>
        </AppMgmtDigest>

                                                                              ﾉ   Expand table

 Attributes            Description

 AuthoringScopeID      AuthoringScopeId will always be "GLOBAL".

 LogicalName           LogicalName must match the name of the SDK class created in the SDK
                       assembly.

<!-- p.595 -->

 Attributes            Description

 TechnologyId          Technology must match the constant declared and used in the SDK
                       assembly.

 AssemblySuffix        AssemblySuffix must match the filename of the SDK assembly
                       (Microsoft.ConfigurationManagement.ApplicationManagement.
                       < AssemblySuffix >.dll).

 Version               Version is the version number for the release of the deployment type
                       extension. This version number is used for in-place revisions.

                                                                                 ﾉ   Expand table

 Element                 Description

 HostingTechnology       The HostingTechnology element must be
                         "GLOBAL/< ClassNameForHostingTechnology >".

 InstallerTechnology     The InstallerTechnology element must be
                         "GLOBAL/< ClassNameForInstallerTechnology >".

See Also
How to Define the Hosting Technology Registration File
How to Define the Installer Technology Registration File
Configuration Manager Reference

Feedback
Was this page helpful?      Yes        No

Provide product feedback

<!-- p.596 -->

How to Define the Hosting Technology
Registration File
Article • 10/04/2022

To define a hosting technology registration file, create an XML file based on the
http://schemas.microsoft.com/SystemCenterConfigurationManager/2009/AppMgmtDigest

schema. Used in the installation process, the registration file registers the custom
hosting technology with Configuration Manager. The hosting technology registration
file is required for the installation of the custom hosting technology.

To define the hosting technology registration file
   1. Create a hosting technology registration file.

      The following example from the RPC sample project demonstrates how to define a
      hosting technology registration file.

        <AppMgmtDigest
        xmlns="http://schemas.microsoft.com/SystemCenterConfigurationManager/20
        09/AppMgmtDigest" xmlns:xsi="http://www.w3.org/2001/XMLSchema-
        instance">
          <HostingTechnology AuthoringScopeId="GLOBAL"
        LogicalName="RdpHostingTechnology" HostingId="Rdp" AssemblySuffix="Rdp"
        Version="1">
            <Requirements>
              <Rule
        xmlns="http://schemas.microsoft.com/SystemsCenterConfigurationManager/2
        009/06/14/Rules" id="Rule_63d22cd6-7f11-4769-8900-9c0ff5c177c5"
        Severity="None">
                <Annotation>
                   <DisplayName Text="Operating System" />
                   <Description Text="" />
                </Annotation>
                <OperatingSystemExpression>
                   <Operator>OneOf</Operator>
                   <Operands>
                     <RuleExpression RuleId="Windows/All_x86_Windows_XP" />
                     <RuleExpression
        RuleId="Windows/x86_Windows_XP_Professional_Service_Pack_3" />
                     <RuleExpression
        RuleId="Windows/All_x64_Windows_Server_2003_Non_R2" />
                     <RuleExpression
        RuleId="Windows/All_x86_Windows_Server_2003_Non_R2" />
                     <RuleExpression
        RuleId="Windows/All_x64_Windows_Server_2003_R2" />

<!-- p.597 -->

             <RuleExpression
RuleId="Windows/All_x86_Windows_Server_2003_R2" />
             <RuleExpression
RuleId="Windows/x64_Windows_Server_2003_R2_original_release_SP1" />
             <RuleExpression
RuleId="Windows/x86_Windows_Server_2003_R2_original_release_SP1" />
             <RuleExpression
RuleId="Windows/All_x64_Windows_XP_Professional" />
             <RuleExpression
RuleId="Windows/x64_Windows_Server_2003_SP2" />
             <RuleExpression
RuleId="Windows/x86_Windows_Server_2003_SP2" />
             <RuleExpression
RuleId="Windows/x64_Windows_XP_Professional_SP2" />
             <RuleExpression RuleId="Windows/All_x64_Windows_Vista" />
             <RuleExpression RuleId="Windows/All_x86_Windows_Vista" />
             <RuleExpression
RuleId="Windows/All_x64_Windows_Server_2008" />
             <RuleExpression
RuleId="Windows/All_x86_Windows_Server_2008" />
             <RuleExpression RuleId="Windows/x64_Windows_Vista_SP1" />
             <RuleExpression RuleId="Windows/x86_Windows_Vista_SP1" />
             <RuleExpression
RuleId="Windows/x64_Windows_Server_2008_original_release" />
             <RuleExpression
RuleId="Windows/x86_Windows_Server_2008_original_release" />
             <RuleExpression
RuleId="Windows/x64_Windows_Server_2008_SP2" />
             <RuleExpression
RuleId="Windows/x86_Windows_Server_2008_SP2" />
             <RuleExpression RuleId="Windows/x64_Windows_Vista_SP2" />
             <RuleExpression RuleId="Windows/x86_Windows_Vista_SP2" />
             <RuleExpression
RuleId="Windows/All_x64_Windows_Server_2008_R2" />
             <RuleExpression RuleId="Windows/All_x64_Windows_7_Client"
/>
             <RuleExpression RuleId="Windows/All_x86_Windows_7_Client"
/>
             <RuleExpression RuleId="Windows/x64_Windows_7_Client" />
             <RuleExpression RuleId="Windows/x86_Windows_7_Client" />
             <RuleExpression RuleId="Windows/x64_Windows_Server_2008_R2"
/>
           </Operands>
         </OperatingSystemExpression>
       </Rule>
     </Requirements>
   </HostingTechnology>
</AppMgmtDigest>

                                                           ﾉ   Expand table

<!-- p.598 -->

 Attributes           Description

 AuthoringScopeID     AuthoringScopeId will always be "GLOBAL".

 LogicalName          LogicalName must match the name of the SDK class created in the SDK
                      assembly for HostingTechnology.

 HostingId            HostingId must match the constant declared and used in the SDK assembly
                      for HostingTechnolgy.

 AssemblySuffix       AssemblySuffix must match the filename of the SDK assembly
                      (Microsoft.ConfigurationManagement.ApplicationManagement.<
                      AssemblySuffix >.dll).

 Version              Version is the version number for the release of the deployment type
                      extension. This version number is used for in-place revisions.

                                                                                   ﾉ   Expand table

 Element          Description

 Requirements     The requirements section is based on DCM requirement rules. The supported
                  platforms for the custom technology must be specified here.

See Also
How to Define the Deployment Technology Registration File
How to Define the Installer Technology Registration File
Configuration Manager Reference

Feedback
Was this page helpful?      Yes      No

Provide product feedback

<!-- p.599 -->

How to Define the Installer Technology
Registration File
Article • 10/04/2022

To define an installer technology registration file, create an XML file based on the
http://schemas.microsoft.com/SystemCenterConfigurationManager/2009/AppMgmtDigest

schema. Used in the installation process, the registration file registers the custom
installer technology with Configuration Manager. The deployment technology
registration file is required for the installation of the custom installer technology.

To define the installer technology registration file
   1. Create an installer technology registration file.

      The following example from the RPC sample project demonstrates how to define
      an installer technology registration file.

        <AppMgmtDigest
        xmlns="http://schemas.microsoft.com/SystemCenterConfigurationManager/20
        09/AppMgmtDigest" xmlns:xsi="http://www.w3.org/2001/XMLSchema-
        instance">
          <InstallerTechnology AuthoringScopeId="GLOBAL"
        LogicalName="RdpInstallerTechnology" InstallerId="Rdp"
        AssemblySuffix="Rdp" Version="1" />
        </AppMgmtDigest>

                                                                               ﾉ   Expand table

 Attributes            Description

 AuthoringScopeID      AuthoringScopeId will always be "GLOBAL".

 LogicalName           LogicalName must match the name of the SDK class created in the SDK
                       assembly for InstallerTechnology.

 HostingId             HostingId must match the constant declared and used in the SDK assembly
                       for InstallerTechnolgy.

 AssemblySuffix        AssemblySuffix must match the filename of the SDK assembly
                       (Microsoft.ConfigurationManagement.ApplicationManagement.
                       < AssemblySuffix >.dll).

<!-- p.600 -->

 Attributes          Description

 Version             Version is the version number for the release of the deployment type
                     extension. This version number is used for in-place revisions.

See Also
How to Define the Deployment Technology Registration File
How to Define the Hosting Technology Registration File
Configuration Manager Reference

Feedback
Was this page helpful?      Yes     No

Provide product feedback
