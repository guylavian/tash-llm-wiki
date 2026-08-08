---
title: "CIPackageInfo Structure"
type: reference
domain: sccm
slug: develop-cipackageinfo-structure
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/develop/reference/core/clients/client-classes/cipackageinfo-structure
family: develop
documentKind: "reference"
abstract: "In Configuration Manager, the CIPackageInfo structure contains package information for a configuration item."
---

# CIPackageInfo Structure

# CIPackageInfo Structure
In Configuration Manager, the `CIPackageInfo` structure contains package information for a configuration item.

## Syntax

```
struct CIPackageInfo
{
      LPWSTR szTypeName;
      LPWSTR szPackageName;
      LPWSTR szPackageVersion;
      LPWSTR szNamespace;
};
```

## Members
 szTypeName
 Name of the configuration item.

 szPackageName
 Name of the package.

 szPackageVersion
 Version of the package.

 szNamespace
 Namespace used by the package software.

## See Also
 [Compliance Settings (DCM) Client Interfaces](../../../../../develop/reference/core/clients/client-classes/compliance-settings--dcm--client-interfaces.md)
 [ICIINFO::GetDependantPackages Method](../../../../../develop/reference/core/clients/client-classes/iciinfo--getdependantpackages-method.md)
