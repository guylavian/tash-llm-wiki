---
title: "Configuration Manager SDK documentation — pages 601-640"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0601-0640
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0601-0640
family: sccm
documentKind: "doc"
abstract: "How to Define the UI Extension Assembly Article • 10/04/2022 The custom wizard assembly is responsible for collecting any data passed in from the Configuration Manager console, and passing it on to the wizard. The assembly should be named, AdminUI.DeploymentType.< AssemblySuffix"
---

# Configuration Manager SDK documentation — pages 601-640

<!-- p.601 -->

How to Define the UI Extension
Assembly
Article • 10/04/2022

The custom wizard assembly is responsible for collecting any data passed in from the
Configuration Manager console, and passing it on to the wizard. The assembly should
be named, AdminUI.DeploymentType.< AssemblySuffix>.dll.

To define the UI extension assembly
   1. Below is an example of how the UI extension interfaces with the UI. Review the
      example in the RDP sample project for complete/specific information on defining
      the UI Extension Assembly.

        //
        // Applies the AppManWrapper around PropertyManager to simplify
        interaction with the AppMgmt SDK and its corresponding WMI classes.
        //
        private void BindSdk()
        {
             //
             // Checks if AppManWrapper has been applied to the PropertyManager
        yet.
             //
             AppManWrapper appManWrapper = this.PropertyManager as
        AppManWrapper;

            if (appManWrapper == null)
            {
                //
                // Applies the AppManWrapper around the PropertyManager.
                //
                this.PropertyManager = appManWrapper =
        AppManWrapper.WrapExisting(this.PropertyManager, new
        ApplicationFactory()) as AppManWrapper;
            }
            //

            // Retrieves references to the Application and DeploymentType
        objects.
            //
            this.application = appManWrapper.InnerAppManObject as Application;
            this.deploymentType =
        appManWrapper.AppData.ContainsKey(AppDataDeploymentType) ?
        appManWrapper.AppData[AppDataDeploymentType] as DeploymentType : null;

<!-- p.602 -->

    return;
}
//
// Loads the values into the UI.
//
private void LoadIntoUI()
{
    //
    // Checks if the Deployment Type has not been created yet.
    //
    if (this.deploymentType == null)
    {
        //
        // Sets defaults for the user.
        //
        this.ApplyDefaults();
        this.ApplyFormState();

        return;
    }

    RdpInstaller rdpInstaller = this.deploymentType.Installer as
RdpInstaller;

    //
    // Checks if content is associated with the installer, which means
the RDP is being distributed through the content server.
    //
    bool installerHasContentFile = (rdpInstaller.Contents.Count > 0 &&
rdpInstaller.Contents[0].Files.Count > 0);

    //
    // Adjusts the radio buttons according to content settings.
    //
    this.distributeThroughContentServerRadioButton.Checked =
(installerHasContentFile == true);
    this.constructOnClientRadioButton.Checked =
(installerHasContentFile == false);

    //
    // Loads each value into the UI.
    //
    this.deploymentTypeNameTextBox.Text = this.deploymentType.Title;
    this.clientRdpFileTextBox.Text =
Path.Combine(rdpInstaller.InstallFolder, rdpInstaller.Filename);
    this.serverRdpFileTextBox.Text = installerHasContentFile ?
Path.Combine(rdpInstaller.Contents[0].Location,
rdpInstaller.Contents[0].Files[0].Name) : string.Empty;
    this.remoteMachineTextBox.Text = rdpInstaller.FullAddress;
    this.userNameTextBox.Text = rdpInstaller.Username;
    this.displayWidthTextBox.Text =
string.Format(CultureInfo.InvariantCulture, "{0}",
rdpInstaller.DesktopWidth);
    this.displayHeightTextBox.Text =

<!-- p.603 -->

string.Format(CultureInfo.InvariantCulture, "{0}",
rdpInstaller.DesktopHeight);
    this.fullScreenCheckBox.Checked = rdpInstaller.FullScreen;
    this.audioComboBox.SelectedIndex = (int)rdpInstaller.AudioMode;
    this.keyboardComboBox.SelectedIndex =
(int)rdpInstaller.KeyboardMode;
    this.redirectPrinterCheckBox.Checked =
rdpInstaller.RedirectPrinters;
    this.redirectSmartCardsCheckBox.Checked =
rdpInstaller.RedirectSmartCards;
    this.remoteProgramCheckBox.Checked =
string.IsNullOrEmpty(rdpInstaller.RemoteApplication) == false;
    this.remoteProgramFileTextBox.Text =
Path.GetFileName(rdpInstaller.RemoteApplication);
    this.remoteStartUpPathTextBox.Text =
Path.GetDirectoryName(rdpInstaller.RemoteApplication);

    //
    // Adjusts the form according to state.
    //
    this.ApplyFormState();

    return;
}

//
  // Saves the values from the UI.
//
private void SaveFromUI()
{
     //
     // In the case of the wizard, the new Deployment Type instance
will be available in UserData once the user has navigated from the
creation page.
     //
     if (this.deploymentType == null &&
this.UserData.ContainsKey(UserDataDeploymentType) == true)
     {
         this.deploymentType = this.UserData[UserDataDeploymentType] as
DeploymentType;
     }

    RdpInstaller rdpInstaller = this.deploymentType.Installer as
RdpInstaller;

    //
    // Checks if content should be associated with the installer (which
means the RDP is being distributed through the content server).
    //
    if (this.distributeThroughContentServerRadioButton.Checked == true)
    {
        if (rdpInstaller.Contents.Count <= 0)
        {
            rdpInstaller.Contents.Add(new Content());
        }

<!-- p.604 -->

       if (rdpInstaller.Contents[0].Files.Count <= 0)
       {
           rdpInstaller.Contents[0].Files.Add(new ContentFile());
       }

        rdpInstaller.Contents[0].Location =
Path.GetDirectoryName(this.serverRdpFileTextBox.Text);
        rdpInstaller.Contents[0].Files[0].Name =
Path.GetFileName(this.serverRdpFileTextBox.Text);
    }
    else
    {
        rdpInstaller.Contents.Clear();
    }

    //
    // Collects the desktop dimensions.
    //
    int desktopWidth = RdpInstaller.DefaultDesktopWidth, desktopHeight
= RdpInstaller.DefaultDesktopHeight;
    int.TryParse(this.displayWidthTextBox.Text, out desktopWidth);
    int.TryParse(this.displayHeightTextBox.Text, out desktopHeight);

    //
    // Saves each value from UI.
    //    this.deploymentType.Title =
this.deploymentTypeNameTextBox.Text;
    rdpInstaller.InstallFolder =
Path.GetDirectoryName(this.clientRdpFileTextBox.Text);
    rdpInstaller.Filename =
Path.GetFileName(this.clientRdpFileTextBox.Text);
    rdpInstaller.ConstructRdpOnClient =
this.constructOnClientRadioButton.Checked;
    rdpInstaller.FullAddress = this.remoteMachineTextBox.Text;
rdpInstaller.Username = this.userNameTextBox.Text;
    rdpInstaller.DesktopWidth = desktopWidth;
    rdpInstaller.DesktopHeight = desktopHeight;
    rdpInstaller.FullScreen = this.fullScreenCheckBox.Checked;
    rdpInstaller.AudioMode =
(RdpAudioMode)this.audioComboBox.SelectedIndex;
    rdpInstaller.KeyboardMode =
(RdpKeyboardMode)this.keyboardComboBox.SelectedIndex;
    rdpInstaller.RedirectPrinters =
this.redirectPrinterCheckBox.Checked;
    rdpInstaller.RedirectSmartCards =
this.redirectSmartCardsCheckBox.Checked;
    rdpInstaller.RemoteApplication = this.remoteProgramCheckBox.Checked
? Path.Combine(this.remoteStartUpPathTextBox.Text,
this.remoteProgramFileTextBox.Text) : string.Empty;

    this.SplitFullAddressIntoServerNameAndPort(rdpInstaller);

    return;
}

<!-- p.605 -->

Namespaces
Microsoft.ConfigurationManagement.AdminConsole

Microsoft.ConfigurationManagement.AdminConsole.AppManFoundation

Microsoft.ConfigurationManagement.AdminConsole.CreateDT

Microsoft.ConfigurationManagement.ApplicationManagement

Microsoft.ConfigurationManagement.ApplicationManagement.Application

Microsoft.ConfigurationManagement.ManagementProvider.ConnectionManagerBase

System.Collections.Generic

System.ComponentModel

System.Diagnostics

System.Drawing

System.Globalization

System.IO

System.Linq

System.Windows.Forms

Assemblies
Microsoft.ConfigurationManagement.ApplicationManagement

Microsoft.ConfigurationManagement.DialogFramework

Microsoft.ConfigurationManagement

Microsoft.ConfigurationManagement.ManagementProvider

AdminUI.AppManFoundation

AdminUI.CreateDT

See Also
Configuration Manager Reference

<!-- p.606 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.607 -->

How to Define the Create Application
Wizard XML File
To define the custom deployment technology XML file, create an XML file based on the
https://schemas.microsoft.com/SystemsManagementServer/2005/03/ConsoleFramework schema.

The XML file for the Create Application Wizard should be named,
CreateApp_<TechnologyID>.xml.

To define the create application wizard XML file
  1. Create a Create Application Wizard XML file.

     The following example from the RDP sample project shows how to define the Create
     Application Wizard XML file. Wizards aren't extensible for the UI. However, by creating
     this custom deployment technology XML, the contents of the wizard now include the
     ability to create an RDP deployment type.

       XML
       <?xml version="1.0" encoding="utf-8"?>
       <SmsFormData
       xmlns="https://schemas.microsoft.com/SystemsManagementServer/2005/03/ConsoleFra
       mework" FormatVersion="1">
         <Form Id="{FD19DEC6-81ED-447B-9D88-3AAD7DE499F1}" CustomData="CreateApp"
       FormType="PropertySheet" ForceRefresh="true">
           <Pages>
             <Page Assembly="AdminUI.DeploymentType.Rdp.dll"
       Namespace="RdpTechnology.AdminConsole" VendorId="Partner Company Name" Id="
       {6802BC91-30EF-49A5-80F6-D4902CD5181C}"
       Type="RdpDeploymentTechnologyPageControl" />
           </Pages>
         </Form>
       </SmsFormData>

See Also
Configuration Manager Reference

Last updated on 12/18/2025

<!-- p.608 -->

How to Define the Create Deployment
Type Wizard XML File
Article • 10/04/2022

To define the custom create deployment type wizard XML file, create an XML file based
on the
http://schemas.microsoft.com/SystemsManagementServer/2005/03/ConsoleFramework

schema. The XML file for the Create Application Wizard should be named
CreateDeploymentWizard_<TechnologyID>.xml.

To define the create deployment type wizard XML file
   1. Create a Create Deployment Type Wizard XML file.

      The following example from the RDP sample project demonstrates how to define
      the Deployment Type Wizard XML file.

         XML

         <?xml version="1.0" encoding="utf-8"?>
         <SmsFormData
         xmlns="http://schemas.microsoft.com/SystemsManagementServer/2005/03/Con
         soleFramework" FormatVersion="1">
           <Form Id="{FD19DEC6-81ED-447B-9D88-3AAD7DE499F1}"
         CustomData="CreateDT" FormType="PropertySheet" ForceRefresh="true">
             <Pages>
               <Page Assembly="AdminUI.DeploymentType.Rdp.dll"
         Namespace="RdpTechnology.AdminConsole" VendorId="Partner Company Name"
         Id="{6802BC91-30EF-49A5-80F6-D4902CD5181C}"
         Type="RdpDeploymentTechnologyPageControl" />
             </Pages>
           </Form>
         </SmsFormData>

See Also
Configuration Manager Reference

Feedback

<!-- p.609 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.610 -->

How to Define the Deployment Type
Property Sheet XML File
Article • 10/04/2022

To define the custom deployment type property page XML file, create an XML file based
on the
http://schemas.microsoft.com/SystemsManagementServer/2005/03/ConsoleFramework

schema. The XML file for the deployment type property sheet should be named
<TechnologyID>DeploymentTypePropertySheet.xml.

To define the deployment type property page XML file
   1. Create a deployment type property sheet XML file.

      The following example from the RPC sample project shows how to define the
      deployment type property sheet XML file.

         XML

         <?xml version="1.0" encoding="utf-8" ?>
         <SmsFormData xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns:xsd="http://www.w3.org/2001/XMLSchema" FormatVersion="1"
         xmlns="http://schemas.microsoft.com/SystemsManagementServer/2005/03/Con
         soleFramework">
           <Form Id="f1908d6f-1ef8-4304-a229-c521c8e33713"
         FormType="PropertySheet">
             <Resources>
               <Title Name="_AppTitle" />
               <Icon Name="_AppIcon" />
             </Resources>
             <Assembly Name="AdminUI.DeploymentType.Rdp.dll"
         Namespace="RdpTechnology.AdminConsole"/>
             <Pages>
               <Page VendorId="Partner Company Name" Id="{8A248387-62CB-4253-
         8255-47E9723BC40D}" Type="RdpDeploymentTechnologyPageControl" />
             </Pages>
           </Form>
         </SmsFormData>

See Also
Configuration Manager Reference

<!-- p.611 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.612 -->

How to Define the AppSynclet MOF File
Article • 10/04/2022

To define a custom synclet MOF file, create an instance of the CCM_AppHandlers class.
The new class instance identifies the custom client-side handler. Also, create instances of
the CCM_HandlerSynclet class to store, detect, install and uninstall property values.

The client extension maps closely to the Installer object, defined as part of the
DeploymentType. Property values are stored in WMI and the public COM methods in
the client-side handler map to detection, installation and uninstallation.

In this example, a new custom synclet MOF file is required for Remote Desktop Protocol
(RDP) files. Support for RDP files isn't built in to Configuration Manager, so a custom
synclet MOF file is required.

To define a custom synclet MOF file
   1. Create an instance of the CCM_AppHandlers class. This class associates the synclet
      with the custom client-side handler. The HandlerCLSID value is the globally unique
      identifier that identifies the custom client-side handler's COM object. This, and the
      other class instances are stored in WMI under root\ccm\cimodels.

      The following example from the RDP sample project demonstrates how to define a
      custom synclet MOF file.

        //*********************************************************************
        *********
        //
        // The following are the registrations of the Rdp handler
        //
        //*********************************************************************
        *********
        instance of CCM_AppHandlers
        {
            HandlerName     = "Rdp";
            HandlerCLSID    = "{4A1FFE05-FEF1-41E3-8DE1-732474E5983D}";
        };

   2. Creates custom instance of the CCM_HandlerSynclet class to store the Detect action
      property values.

<!-- p.613 -->

  The following example from the RDP sample project demonstrates how to define a
  custom synclet MOF file.

    //*********************************************************************
    *********
    //
    // Rdp_Detect_Synclet
    //
    //*********************************************************************
    *********
    class Rdp_Detect_Synclet : CCM_HandlerSynclet
    {
        [ Not_Null ]
        string       FileName;

         [ Not_Null ]
         string       InstallFolder;

         [ Not_Null ]
         string       FullAddress;

         string       RemoteApplication;
         boolean      RemoteApplicationMode;
    };

3. Create a custom instance of the CCM_HandlerSynclet class to store the Install action
  property values.

  The following example from the RDP sample project demonstrates how to define a
  custom synclet MOF file.

    //*********************************************************************
    *********
    //
    // Rdp_Install_Synclet
    //
    //*********************************************************************
    *********
    class Rdp_Install_Synclet : CCM_HandlerSynclet
    {
        [ Not_Null ]
        string Filename;

         [ Not_Null ]
         string InstallFolder;
         sint32 FullScreen;
         sint32 DesktopWidth;

<!-- p.614 -->

            sint32 DesktopHeight;
            sint32 AudioMode;
            string FullAddress;
            string RemoteServerName;
            sint32 RemoteServerPort;
            string RemoteApplication;
            boolean RemoteApplicationMode;
            boolean ConstructRdpOnClient;
            sint32 KeyboardMode;
            sint32 RedirectPrinters;
            sint32 RedirectSmartCards;
            string Username;
            string ContentFilename;
       };

  4. Create a custom instance of the CCM_HandlerSynclet class to store the Uninstall
    action property values.

    The following example from the RDP sample project demonstrates how to define a
    custom synclet MOF file.

       //*********************************************************************
       *********
       //
       // Rdp_Uninstall_Synclet
       //
       //*********************************************************************
       *********
       class Rdp_Uninstall_Synclet : CCM_HandlerSynclet
       {
           [ Not_Null ]
           string FileName;

            [ Not_Null ]
            string InstallFolder;
       };

See Also
Configuration Manager Reference

Feedback

<!-- p.615 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.616 -->

How to Define the Client-side Handler
Article • 10/04/2022

The custom client-side handler needs to implement a public COM interface and
methods. The below methods will be called by the Configuration Manager client
framework.

The client extension maps closely to the Installer object, defined as part of the
DeploymentType. Property values are stored in WMI and the public COM methods in
the client-side handler map to detection, installation and uninstallation.

  ） Important

  The COM object's globally unique identifier needs to be registered in WMI; see the
  topic How to Define the AppSynclet MOF File.

A complete example of implementing the public COM interface and methods is
provided for reference. Below are examples of key methods.

   1. InstallApp Method

   2. UninstallApp Method

   3. DiscoverApp Method

To define a custom client-side handler
   1. In the client-side handler, create an instance of the InstallApp method class. This
      method will be called by client framework.

      The following example from the RDP sample project demonstrates how to define
      an InstallApp method.

        //*********************************************************************
        **
        HRESULT CRdpHandler::InstallApp
        (
            __in HANDLE                 hUserToken,
            __in IWbemClassObject *     pHandlerSynclet,
            __in LPCWSTR                szLocalContentPath
        )
        {

<!-- p.617 -->

    CComPtr<IWbemClassObject>         spHandlerSynclet;
    RdpInstallationParam rdpInstallationParam;
    wstring sContentPath;
    wstring sSourceFileName;
    wstring sDestFileName;
    wstring sInstallFolder;
    HRESULT hrResult = S_OK;
    assert(pHandlerSynclet!=NULL);
    sContentPath=szLocalContentPath;
    spHandlerSynclet=pHandlerSynclet;

    //Read synclet
    hrResult =
GetInstallationParamFromSynclet(spHandlerSynclet,rdpInstallationParam);
    if(FAILED(hrResult)) {return hrResult;}

    hrResult =
ExpandSystemEnvironmentStrings(hUserToken,rdpInstallationParam.InstallF
older.c_str(),sInstallFolder);
    if(FAILED(hrResult)) {return hrResult;}

    if (!IsDirectoryExists(sInstallFolder.c_str()))
    {
        hrResult = RecursiveCreatePath(sInstallFolder.c_str(),NULL);
        if(FAILED(hrResult)) {return hrResult;}
    }
    sDestFileName = sInstallFolder + L"\\" +
rdpInstallationParam.Filename;
    if (rdpInstallationParam.ConstructRdpOnClient)
    {
        hrResult =
ConstructRdpFile(sDestFileName,rdpInstallationParam);
    }
    else
    {
        sSourceFileName = sContentPath + L"\\" +
rdpInstallationParam.ContentFilename;

       //Check if the specific RDP file exists in file system
       if(!IsFileExist( sSourceFileName.c_str()))
       {
           return HRESULT_FROM_WIN32( ERROR_FILE_NOT_FOUND);
       }

if(CopyFile(sSourceFileName.c_str(),sDestFileName.c_str(),false)==0)
        {
            hrResult = HRESULT_FROM_WIN32(GetLastError());
        }
    }
        return hrResult;
}

<!-- p.618 -->

2. In the client-side handler, create an instance of the UninstallApp method class. This
  method will be called by the client framework.

  The following example from the RDP sample project demonstrates how to define
  an UninstallApp method.

     //*********************************************************************
     **
     //
     // CRdpHandler::UninstallApp
     //
     // Purpose: Delete an Rdp file per the uninstalation synclet.
     //
     // Parameters:
     //
     // Return values:
     //      S_OK - Success: Success
     //      All other return values indicate failure.
     //
     //*********************************************************************
     *
     HRESULT CRdpHandler::UninstallApp
     (
         __in HANDLE                 hUserToken,
         __in IWbemClassObject *     pHandlerSynclet
     )
     {
         CComPtr<IWbemClassObject>         spHandlerSynclet;
         RdpUninstallationParam rdpUninstallationParam;
         wstring sRdpFileFullPath;
         HRESULT hrResult = S_OK;

         assert(pHandlerSynclet!=NULL);

          spHandlerSynclet = pHandlerSynclet;
          hrResult =
     GetUninstallationParamFromSynclet(spHandlerSynclet,rdpUninstallationPar
     am);
          if(FAILED(hrResult)) {return hrResult;}

         wstring sInstallFolder = rdpUninstallationParam.InstallFolder;

         hrResult =
     ExpandSystemEnvironmentStrings(hUserToken,rdpUninstallationParam.Instal
     lFolder.c_str(),sInstallFolder);    if(FAILED(hrResult)) {return
     hrResult; }

         sRdpFileFullPath = sInstallFolder + L"\\" +
     rdpUninstallationParam.Filename;

         if(IsFileExist(sRdpFileFullPath.c_str()))

<!-- p.619 -->

         {
             if(DeleteFile(sRdpFileFullPath.c_str())==0)
             {
                 return HRESULT_FROM_WIN32(GetLastError());
             }
         }
         return hrResult;
    }

3. In the client-side handler, create an instance of the DiscoverApp method class. This
  method will be called by client framework.

  The following example from the RDP sample project demonstrates how to define a
  DiscoverApp method.

    //*********************************************************************
    **
    //
    // CRdpHandler::DiscoverApp
    //
    // Purpose: check if an Rdp file is installed per detect synclet
    //
    // Parameters:
    //      __in HANDLE hUserToken: the user token. If it is null, the
    action is for computer. If it is not NULL, the action is for the user
    //      __in LPCWSTR                    szDeploymentTypeId: the id of
    the deployment type.
    //      __in DWORD                      dwDeploymentTypeRevision: The
    revision of the deployment type
    //      __out AppDeploymentTypeData *   pDetectResult: The detection
    result
    //
    // Return values:
    //      S_OK - Success:
    //      All other return values indicate failure.
    //
    //*********************************************************************
    *
    STDMETHODIMP CRdpHandler::DiscoverApp
    (
        __in HANDLE                     hUserToken,
        __in LPCWSTR                    szDeploymentTypeId,
        __in DWORD                      dwDeploymentTypeRevision,
        __out AppDeploymentTypeData *   pDetectResult
    )
    {
        CComPtr<IWbemClassObject>         spHandlerSynclet;
        CString              sTargetedSyncletPath;
        RdpDiscoverParam    rdpDiscoverParam;
        AppDetectState      eDetectState;

<!-- p.620 -->

           HRESULT hrResult = S_OK;

           assert(pDetectResult!=NULL);

           // Initial return
           ZeroMemory(pDetectResult, sizeof(AppDeploymentTypeData));

           // Load the synclet

       sTargetedSyncletPath.Format(L"Rdp_Detect_Synclet.ActionType=\"Detect\",
       AppDeliveryTypeId=\"%s\",Revision=%d", szDeploymentTypeId,
       dwDeploymentTypeRevision);
           BSTR bsTargetedSyncletPath = sTargetedSyncletPath.AllocSysString();
           hrResult = m_pSvc->GetObject(bsTargetedSyncletPath,0,
       NULL,&spHandlerSynclet,NULL);
           ::SysFreeString(bsTargetedSyncletPath);

           if(FAILED(hrResult)) {return hrResult;}

           // Populate information from synclet to discovery param.
           hrResult =
       GetDiscoverParamFromSynclet(spHandlerSynclet,rdpDiscoverParam);

           if(FAILED(hrResult)) {return hrResult;}

           // Discover it
           hrResult = DiscoverIndividualApp(
                       hUserToken,
                       rdpDiscoverParam,
                       eDetectState);

           if(FAILED(hrResult)) {return hrResult;}

           // Return result
           if (appDetectInstalled == eDetectState)
           {
               hrResult = AllocInitDetectData(pDetectResult, 1);
               if(FAILED(hrResult)) {return hrResult;}

               hrResult = MarkDetectItem(
                           pDetectResult->pData,
                           rdpDiscoverParam.AppDeliveryTypeId,
                           dwDeploymentTypeRevision,
                           S_OK);
               if(FAILED(hrResult)) {return hrResult;}
           }
           return hrResult;
       }

See Also
Configuration Manager Reference

<!-- p.621 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.622 -->

How to Create the Deployment Type
Extension File (*.cmdtx)
Article • 10/04/2022

The application management extension must be installed on each Configuration
Manager administrator console computer that will create a custom deployment
technology. The first step in installing the application management extension files is to
create a deployment type extension file (*.cmdtx).

To Create the ConfigMgr Deployment Type Extension File
(*.cmdtx)
   1. Create an empty directory to stage the contents.

   2. Create and copy the following files previously created into the empty directory:

      a. DeploymentTechnology.xml

         Required. A digest of the Deployment Technology

      b. HostingTechnology.xml

         Required. A digest of the Hosting Technology

      c. InstallerTechnology.xml

         Required. A digest of the Installer Technology

      d. The custom SDK Assembly
         (Microsoft.ConfigurationManagement.ApplicationManagement.
         {AssemblySuffix}.dll)

         Required. Contains interface implementation of both the Hosting Technology
         and Installer Technology Note: the AssemblySuffix should correspond to
         whatever is specified for AssemblySuffix attribute in the
         DeploymentTechnology.xml file.

      e. HostingApplication.zip

         Optional. Importable application that represents the Hosting Application, which
         includes content (if any). This should be created using the Export feature on the
         Applications node, in the Admin Console.

<!-- p.623 -->

     f. HandlerApplication.zip

       Optional. Importable application that represents the Handler Application for the
       client, which includes content (if any). This should be created using the Export
       feature on the Applications node, in the Admin Console.

  3. Use the method DeploymentTypeExtender.CreateExtension, which is located in
    Microsoft.ConfigurationManagement.ApplicationManagement namespace, to
    create the Deployment Type Extension (*.cmdtx) file based on the content in the
    staging directory.

       C#

       // Summarizes progress from CreateExtension method to a log file or the
       console.
       // <param name="summaryText">Summary text to be presented</param>
       public void Summarize(string summaryText)
       {
             System.Console.WriteLine(summaryText);
             return;
       }
       // Creates a new Deployment Type Extension using the specified source
       path
       // <param name="sourcePath">Source path used to create the Deployment
       Type Extension</param>
       // <param name="deploymentTypeExtensionFilePath">Resulting Deployment
       Type Extension file</param>
       private void CreateDeploymentTypeExtensionFile(string sourcePath,
       string deploymentTypeExtensionFilePath)
       {
             DeploymentTypeExtender.CreateExtension(sourcePath,
       deploymentTypeExtensionFilePath, this.Summarize);
             return;
       }

Namespaces

Microsoft.ConfigurationManagement.ApplicationManagement

Microsoft.ConfigurationManagement.ApplicationManagement.Serialization

Assemblies

Microsoft.ConfigurationManagement.ApplicationManagement.dll

Microsoft.ConfigurationManagement.ApplicationManagement.Extender.dll

<!-- p.624 -->

See Also
Configuration Manager Reference

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.625 -->

How to Create the Windows Installer
File (*.msi)
Article • 10/04/2022

After the Deployment Type Extension file (*.cmdtx) is created, you're expected to
generate a Windows Installer file (*.msi) which contains the *.cmdtx file and the UX files.
The Windows Installer needs to copy the files into the correct locations and register the
custom extension with the site server.

The basic contents of the Windows Installer file are shown below:

To Create the Windows Installer File (*.msi)
   1. Generate a Windows Installer file which contains the *.cmdtx file, and UX files. The
      Windows Installer file is responsible for installing the UX files in the correct
      locations, using the standards defined by the Admin Console team. Basically, this
      will involve including the following files:

      a. UX Assembly, for example, AdminUI.DeploymentType.<AssemblySuffix>.dll

         This file is required and contains the UX implementation, which is then bound to
         the Configuration Manager console using the below XML files.

         The Installer should copy this file to sms\AdminConsole\bin.

      b. CreateApp_<TechnologyID>.xml

         This file is required and provides the console extension for the Create
         Application Wizard.

<!-- p.626 -->

     The Installer should copy this file to
     sms\AdminConsole\XmlStorage\Extensions\Forms.

   c. CreateDeploymentWizard_<TechnologyID>.xml

     This file is required and provides the console extension for the Create
     Deployment Type Wizard.

     The Installer should copy this file to
     sms\AdminConsole\XmlStorage\Extensions\Forms.

  d. <TechnologyID>DeploymentTypePropertySheet.xml

     This file is required and provides the Deployment Type property page.

     The Installer should copy this file to sms\AdminConsole\XmlStorage\Forms.

2. The Windows Installer file should contain code to invoke the
  DeploymentTypeExtender.Extend method, which is located in the
  Microsoft.ConfigurationManagement.ApplicationManagement namespace. This
  will then register the extension files for a given site server computer. For an
  administrator console computer, this initializes the cache for that user. The Extend
  method call requires the *.cmdtx file created earlier.

  a. Make a standard WqlConnectionManager connection to the site server.

  b. Call the Extend method, passing the *cmdtx file, the ConnectionManagerBase
     object through an instance of ConsoleDcmConnection for the method
     connection parameter, and the connection path (example below).

    ２ Warning

    In order to use ConsoleDcmConnection, you will need to add an assembly
    reference to AdminUI.DcmObjectWrapper.dll.

    using DCM =
    Microsoft.ConfigurationManagement.AdminConsole.DesiredConfigurationMana
    gement;

    [...]

        ConnectionManagerBase connectionManager = new
    WqlConnectionManager();
        connectionManager.Connect("SiteServerName");

<!-- p.627 -->

           DeploymentTypeExtender.Extend(@"C:\RdpTechnology.cmdtx", new
       DCM.ConsoleDcmConnection(connectionManager, null),
       @"\\SiteServerName\root\sms\site_ABC");

  3. Client Installation (HandlerApplication.zip)

    To install the client extension files, either as part of the HandlerApplication or as a
    separate installation:

     a. Compile the AppSynclet MOF file. On the client, compile the custom synclet
       MOF file to create the necessary instance of the CCM_AppHandler class and the
       corresponding instances of the CCM_HandlerSynclet classes.

          C:\> mofcomp appsynclet_<technologyid>

     b. Copy the handler .dll to the Configuration Manager client directory and register
       the .dll on the system.

          C:\> regsvr32 <technologyid>handler.dll

       ７ Note

       The handler .dll must be compiled to match the operating system – either 32-
       bit or 64-bit.

Namespaces

Microsoft.ConfigurationManagement.ApplicationManagement

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assemblies
AdminUI.DcmObjectWrapper.dll

AdminUI.WqlQueryEngine.dll

<!-- p.628 -->

DcmObjectModel.dll

Microsoft.ConfigurationManagement.ApplicationManagement.dll

Microsoft.ConfigurationManagement.ApplicationManagement.Extender.dll

Microsoft.ConfigurationManagement.ManagementProvider.dll

See Also
Configuration Manager Reference

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.629 -->

Verifying the Application Management
Extension
Article • 10/04/2022

Server

Verify the new Deployment Type is available in the console

   1. In the Configuration Manager console, click Software Library.

   2. In the Software Library workspace, expand Application Management, and then
      click Applications.

   3. On the Home tab, in the Create group, click Create Application.

   4. In the Type field, verify that the new deployment type is available in the pull-down
      menu.

      The image below shows an example from the RDP sample project.

<!-- p.630 -->

  Tip

 For more information on using the Create Application Wizard, see Create
 applications.

Create an application using the Create Application Wizard

  1. In the Configuration Manager console, click Software Library.

  2. In the Software Library workspace, expand Application Management, and then
    click Applications.

  3. On the Home tab, in the Create group, click Create Application.

  4. In the Type field, select the new deployment type from the pull-down menu.

  5. Continue through the wizard until successful completion.

  Tip

<!-- p.631 -->

 For more information on using the Create Application Wizard, see Create
 applications.

Create a deployment type using the Create Deployment Type
Wizard
  1. In the Configuration Manager console, click Software Library.

  2. In the Software Library workspace, expand Application Management, and then
    click Applications.

  3. Select an application and then, on the Home tab, in the Application group, click
    Create Deployment Type to create a new deployment type for this application.

  4. In the Type field, select the new deployment type from the pull-down menu.

  5. Continue through the wizard until successful completion.

  Tip

 For more information on using the Create Application Wizard, see Create
 applications.

Check the Deployment Type Properties

  1. In the Configuration Manager console, click Software Library.

  2. In the Software Library workspace, expand Application Management, and then
    click Applications.

  3. Select an application and then select the Deployment Type tab, in the Summary
    group.

  4. Select a deployment type and then select the Deployment Type tab, and then click
    Properties in the Properties group to display the deployment type properties.

Verify the corresponding SMS_Application instance was created for
the application

  1. Load Windows Management Instrumentation Tester (WBEMTEST.EXE).

  2. Connect to the root\sms\site_<sitecode> namespace.

<!-- p.632 -->

  3. Click Query, and then enter the below query:

        SELECT * FROM SMS_Application WHERE LocalizedDisplayName =
        '<NameofApplication>'

  4. The results should appear similar to the below list:

    SMS_Application.CI_ID=<Number>

Verify the digest associated with the Deployment Type contains the
properties from the new technology

  1. Connect to the CM_<sitecode> database.

  2. Load Microsoft SQL Server Management Studio, and click New Query.

  3. Enter the below SQL query:

        SELECT SDMPackageDigest
        FROM CI_ConfigurationItems ci
        JOIN CI_LocalizedProperties lp ON (lp.CI_ID = ci.CI_ID)
        WHERE ci.CIType_ID = 21 AND lp.DisplayName = '<NameofApplication>'

  4. The results should appear similar to the below list:

 text

      <AppMgmtDigest
 xmlns="http://schemas.microsoft.com/SystemCenterConfigurationManager/...

  5. Double-click the result value to view the digest.

Client

Deploy application to client using the corresponding Deployment
Type
  1. In the Configuration Manager console, click Software Library.

<!-- p.633 -->

  2. In the Software Library workspace, expand Application Management, and then
    click Applications.

  3. In the Applications list, right-click the application you want to deploy and click
    Deploy.

  4. Continue through the wizard until successful completion.

Force user and device policy to be retrieved on the client
  1. On the client, in Control Panel, double-click the Configuration Manager icon, and
    then select the Actions tab.

  2. Select Machine Policy Retrieval & Evaluation Cycle, and then click Run Now.

  3. Select User Policy Retrieval & Evaluation Cycle, and then click Run Now.

Verify that synclets are distributed and compiled on the client (they
will be stored in root\ccm\cimodels namespace)

  1. Load Windows Management Instrumentation Tester (WBEMTEST.EXE).

  2. Connect to the root\ccm\cimodels namespace.

  3. Click Query, and then enter the below query:

          select * from ccm_handlersynclet

  4. The results should appear similar to the below list:

    <Technology>Detect_Synclet.ActionType="Detect",AppDeliveryTypeId="ScopeId\ ...

    <Technology>Install_Synclet.ActionType="Install" ,AppDeliveryTypeId="ScopeId\ ...

    <Technology>Uninstall_Synclet.ActionType="Uninstall" ,AppDeliveryTypeId="ScopeId
    ...

Ensure that each action performs as expected on the client
  1. Verify that the deployment action performs correctly.

 ７ Note

<!-- p.634 -->

  The deployment settings will impact validation of each action on the client.

        Available - If the application is deployed to a user, the user sees the published
        application in the Application Catalog and can request it on demand. If the
        application is deployed to a device, the user will see it in the Software Center
        and can install it on demand.
           Required - The application is deployed automatically, according to the
           configured schedule. However, a user can track the application deployment
           status and install the application before the deadline by using the Software
           Center.

See Also
Configuration Manager Reference

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.635 -->

About Configuration Manager WMI
programming
Article • 10/10/2022

Programming the Configuration Manager client Windows Management Instrumentation
(WMI) provider differs according to the programming language you use.

C#
If you use C#, use the System.Management namespace. It provides access to a rich set
of management information and management events about the system, devices, and
applications that are instrumented to the WMI infrastructure.

  ７ Note

  The managed Configuration Manager library is for use with a Configuration
  Manager site server and cannot be used to access client WMI namespaces.

For more information about connecting to the Configuration Manager client WMI
namespace by using the System.Management namespace, see How to connect to the
Configuration Manager client WMI namespace by using System.Management.

For more information about using Configuration Manager client WMI namespace
objects by using the System.Management namespace, see How to read a WMI object by
using System.Management.

For more information about using the System.Management namespace, see
System.Management Namespace.

VBScript
If you use VBScript, you access and use Configuration Manager client WMI objects by
using the same coding techniques that are used for accessing other WMI objects,
including the Configuration Manager WMI objects. For more information, see the
Windows Management Instrumentation.

Client WMI namespace

<!-- p.636 -->

The Configuration Manager client WMI namespace begins at \\<client>\root\ccm . For
example, root\ccm contains the SMS_Client class that can be used to get and set client
information.

See also
     How to call a WMI class method by using System.Management
     How to connect to the Configuration Manager client WMI namespace by using
     System.Management
     How to perform an asynchronous query by using System.Management
     How to perform a synchronous query by using System.Management
     How to read a WMI object by using System.Management
     Windows Management Instrumentation
     System.Management namespace

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.637 -->

How to Connect to the Configuration
Manager Client WMI Namespace by
Using System.Management
Article • 10/10/2022

To connect to the Configuration Manager client Windows Management Instrumentation
(WMI) provider, you create a ManagementScope object in the \\Client\root\ccm
namespace.

You use the ManagementScope object to read and query WMI objects. For example, How
to Read a WMI Object Using System.Management.

To connect to the Configuration Manager client WMI
provider
   1. In Visual Studio, create a new Visual C# Console Project.

   2. Add a reference to the System.Management assembly.

   3. In the C# source code, add a reference to the System.Management namespace
       with the following code.

   4. using System.Management;

   5. Create a new class and add the following connection example code.

Example
The following C# code example creates and returns a ManagementScope object on the
root\ccm namespace.

For information about calling the sample code, see How to Call a WMI Class Method by
Using System.Management.

  c#

  public ManagementScope Connect()
  {
      try
      {

<!-- p.638 -->

            return new ManagementScope(@"root\ccm");
       }
       catch (System.Management.ManagementException e)
       {
           Console.WriteLine("Failed to connect", e.Message);
           throw;
       }
  }

Compiling the Code

Namespaces
System

System.Management

Assembly
System.Management.dll

Robust Programming
The exception that can be raised is System.Management.ManagementException.

See Also
About Configuration Manager WMI Programming
How to Call a WMI Class Method by Using System.Management
How to Perform an Asynchronous Query by Using System.Management
How to Perform a Synchronous Query by Using System.Management
How to Read a WMI Object by Using System.Management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.639 -->

How to Read a WMI Object by Using
System.Management
Article • 10/10/2022

To read a Configuration Manager client Windows Management Instrumentation (WMI)
object, in Configuration Manager, you use a ManagementObject object to read the WMI
object.

To read a WMI object
   1. Set up a connection to the Configuration Manager client WMI namespace. For
       more information, see How to Connect to the Configuration Manager Client WMI
       Namespace by Using System.Management.

   2. Create a ManagementObject object.

   3. Create a ManagementPath object with the ManagementScope path you obtain from
       step one.

   4. Assign the ManagementPath object to the ManagementObject path property.

   5. Call the ManagementObject object Get method to get the object from the WMI
       provider.

   6. Use the ManagementObject object to read the WMI provider object properties.

Example
The following C# code example gets the Configuration Manager client WMI object
SMS_Client object and displays its properties.

For information about calling the sample code, see How to Call a WMI Class Method by
Using System.Management.

  c#

  void ReadObject(ManagementScope scope)
  {
      try // Gets an instance of a CCM_InstalledComponent.
      {
          // Get the object.

<!-- p.640 -->

          ManagementObject obj = new ManagementObject();
          ManagementPath path = new ManagementPath(scope.Path +
  ":CCM_InstalledComponent.Name='SMSClient'");

             obj.Path = path;
             obj.Get();

             // Display a single property.
             Console.WriteLine(obj["DisplayName"].ToString());

             // Display all properties.
             foreach (PropertyData property in obj.Properties)
             {
                 Console.WriteLine(property.Name + " " + property.Value);
             }
         }
         catch (ManagementException e)
         {
             Console.WriteLine("Failed to get component: " + e.Message);
             throw;
         }
  }

This example method has the following parameters:

                                                                          ﾉ   Expand table

 Parameter    Type               Description

 scope        -                  The client management scope. The namespace should be
               ManagementScope   root\ccm.

Compiling the Code

Namespaces
System

System.Management

Assembly
System.Management

Robust Programming
