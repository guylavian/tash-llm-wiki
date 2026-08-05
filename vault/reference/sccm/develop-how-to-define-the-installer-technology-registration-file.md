---
title: "Define the Installer Technology Registration File"
type: reference
domain: sccm
slug: develop-how-to-define-the-installer-technology-registration-file
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/apps/how-to-define-the-installer-technology-registration-file
family: develop
documentKind: "how-to"
abstract: "Learn how to register the custom installer technology with Configuration Manager using an XML file."
---

# Define the Installer Technology Registration File

# How to Define the Installer Technology Registration File
To define an installer technology registration file, create an XML file based on the `http://schemas.microsoft.com/SystemCenterConfigurationManager/2009/AppMgmtDigest` schema. Used in the installation process, the registration file registers the custom installer technology with Configuration Manager.  The deployment technology registration file is required for the installation of the custom installer technology.

### To define the installer technology registration file

1.  Create an installer technology registration file.

     The following example from the RPC sample project demonstrates how to define an installer technology registration file.

    ```
    <AppMgmtDigest xmlns="http://schemas.microsoft.com/SystemCenterConfigurationManager/2009/AppMgmtDigest" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <InstallerTechnology AuthoringScopeId="GLOBAL" LogicalName="RdpInstallerTechnology" InstallerId="Rdp" AssemblySuffix="Rdp" Version="1" />
    </AppMgmtDigest>
    ```

|Attributes|Description|
|----------------|-----------------|
|AuthoringScopeID|AuthoringScopeId will always be "GLOBAL".|
|LogicalName|LogicalName must match the name of the SDK class created in the SDK assembly for InstallerTechnology.|
|HostingId|HostingId must match the constant declared and used in the SDK assembly for InstallerTechnolgy.|
|AssemblySuffix|AssemblySuffix must match the filename of the SDK assembly (Microsoft.ConfigurationManagement.ApplicationManagement.<`AssemblySuffix`>.dll).|
|Version|Version is the version number for the release of the deployment type extension. This version number is used for in-place revisions.|

## See Also
 [How to Define the Deployment Technology Registration File](../../develop/apps/how-to-define-the-deployment-technology-registration-file.md)
 [How to Define the Hosting Technology Registration File](../../develop/apps/how-to-define-the-hosting-technology-registration-file.md)
 [Configuration Manager Reference](../../develop/reference/configuration-manager-reference.md)
