---
title: "Configure People Picker in SharePoint Server Subscription Edition - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-configure-people-picker-subscription-edition
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/configure-people-picker-subscription-edition
family: administration
documentKind: "how-to"
abstract: "Learn how to configure the People Picker web control in SharePoint Subscription Edition."
---

# Configure People Picker in SharePoint Server Subscription Edition - SharePoint Server

Note

Configure People Picker in SharePoint Server Subscription Edition

# Configure People Picker in SharePoint Server Subscription Edition

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

When modern authentication (a trusted identity provider) such as SAML 1.1 or OIDC 1.0 is used, the People Picker control can't search, resolve, and validate users and groups without writing a custom claim provider through C#. In SharePoint Server Subscription Edition, the People Picker has been enhanced to allow resolving users and groups based on their profiles in the User Profile Application (UPA).

UPA must be configured to synchronize users and groups from the trusted identity provider membership store. This allows the People Picker to only resolve valid users and groups without requiring a custom claims provider. For more information, see Enhanced People Picker for modern authentication.

This article will help you to configure People Picker in SharePoint Server Subscription Edition using PowerShell cmdlets.

People Picker supports LDAPS (TLS connection encryption)

## People Picker supports LDAPS (TLS connection encryption)

As organizations become more aware of the risks of unencrypted communication over a network, some are choosing to implement policies that require encryption for all network connections. HTTP is one of the most common protocols that organizations want to protect, but there are other network communication protocols as well. One of those is the Lightweight Directory Access Protocol (LDAP), which is used by applications to access directory services. The SharePoint People Picker feature uses LDAP to look up users and groups in Active Directory forests and domains. LDAP isn't an encrypted protocol by default, although there are several options to enable encryption with it.

To facilitate organizations that require encryption for LDAP traffic, the SharePoint People Picker feature has added support for Secure LDAP (LDAPS) in SharePoint Server Subscription Edition Version 23H2. This allows the People Picker to use TLS connection encryption to protect LDAP traffic to TCP ports 636 and 3269.

To enable Secure LDAP (LDAPS) in the SharePoint People Picker, use the `SecureSocketsLayer` switch parameter with the `Set-SPPeoplePickerConfig` and `Add-SPPeoplePickerSearchADDomain` PowerShell cmdlets.

Examples:

- `Set-SPPeoplePickerConfig -WebApplication https://team.contoso.local -SecureSocketsLayer`

- `Add-SPPeoplePickerSearchADDomain -WebApplication https://team.contoso.local -DomainName "contoso.local" -SecureSocketsLayer`

For more information, see Plan for People Picker in SharePoint.

PowerShell cmdlets to configure People Picker

## PowerShell cmdlets to configure People Picker

With SharePoint Server Subscription Edition, you can use PowerShell cmdlets to configure the People Picker settings instead of `stsadm.exe` commands.

Get-SPPeoplePickerConfig

### Get-SPPeoplePickerConfig

Use the following PowerShell cmdlet to get People Picker settings of a specified Web application.

```
Get-SPPeoplePickerConfig
   -WebApplication <SPWebApplicationPipeBind>
   [-AssignmentCollection <SPAssignmentCollection>]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

For more information, see `Get-SPPeoplePickerConfig`.

Set-SPPeoplePickerConfig

### Set-SPPeoplePickerConfig

Use the `Set-SPPeoplePickerConfig` cmdlet to configure the following People Picker settings of a specified Web application:

- Customized query filter sent to AD with People Picker query

- Customized query sent to AD with People Picker query

- The amount of time before AD search time-out

- Whether the People Picker control should only return the site collection users when clicking the "Check Names" button

- Whether the People Picker control should only return the site collection users when using the "Select People and Groups" dialog box

- Whether return only non-Active Directory users when the Web application uses form-based authentication

```
Set-SPPeoplePickerConfig
   -WebApplication <SPWebApplicationPipeBind>
   [-ActiveDirectoryCustomFilter <String>]
   [-ActiveDirectoryCustomQuery <String>]
   [-ActiveDirectorySearchTimeout <Int32>]
   [-PeopleEditorOnlyResolveWithinSiteCollection]
   [-OnlySearchWithinSiteCollection]
   [-NoWindowsAccountsForNonWindowsAuthenticationMode]
   [-AssignmentCollection <SPAssignmentCollection>]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

For more information, see `Set-SPPeoplePickerConfig`.

Add-SPPeoplePickerSearchADDomain

### Add-SPPeoplePickerSearchADDomain

Use this cmdlet to add a forest or domain to the list that the People Picker uses when searching for users.

```
Add-SPPeoplePickerSearchADDomain
   -WebApplication <SPWebApplicationPipeBind>
   -DomainName <String>
   [-IsForest]
   [-Index <Int32>]
   [-Credential <PSCredential>]
   [-AssignmentCollection <SPAssignmentCollection>]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

For more information, see `Add-SPPeoplePickerSearchADDomain`.

Clear-SPPeoplePickerSearchADDomain

### Clear-SPPeoplePickerSearchADDomain

Use this cmdlet to clear the list of People Picker search forests and domains for a specified Web application.

```
Clear-SPPeoplePickerSearchADDomain
     -WebApplication <SPWebApplicationPipeBind>
     [-AssignmentCollection <SPAssignmentCollection>]
     [-WhatIf]
     [-Confirm]
     [<CommonParameters>]
```

For more information, see `Clear-SPPeoplePickerSearchADDomain`.

Get-SPPeoplePickerSearchADDomain

### Get-SPPeoplePickerSearchADDomain

Use this cmdlet to return all Active Directory forests or domains that the People Picker uses when searching for users.

```
Get-SPPeoplePickerSearchADDomain
   -WebApplication <SPWebApplicationPipeBind>
   [-AssignmentCollection <SPAssignmentCollection>]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

For more information, see `Get-SPPeoplePickerSearchADDomain`.

Remove-SPPeoplePickerSearchADDomain

### Remove-SPPeoplePickerSearchADDomain

Use this cmdlet to remove a forest of domain from the list that the People Picker uses when searching for users.

```
Remove-SPPeoplePickerSearchADDomain
      -WebApplication <SPWebApplicationPipeBind>
      -DomainName <String>
      [-IsForest]
      [-UserName <String>]
      [-AssignmentCollection <SPAssignmentCollection>]
      [-WhatIf]
      [-Confirm]
      [<CommonParameters>]
```

For more information, see `Remove-SPPeoplePickerSearchADDomain`.

Add-SPPeoplePickerDistributionListSearchDomain

### Add-SPPeoplePickerDistributionListSearchDomain

Use this cmdlet to add a domain to the People Picker distribution list search domains.

```
Add-SPPeoplePickerDistributionListSearchDomain
   -WebApplication <SPWebApplicationPipeBind>
   -DomainName <String>
   [-Index <Int32>]
   [-AssignmentCollection <SPAssignmentCollection>]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

For more information, see `Add-SPPeoplePickerDistributionListSearchDomain`.

Clear-SPPeoplePickerDistributionListSearchDomain

### Clear-SPPeoplePickerDistributionListSearchDomain

Use this cmdlet to clear the list of People Picker distribution list search domains.

```
Clear-SPPeoplePickerDistributionListSearchDomain
     -WebApplication <SPWebApplicationPipeBind>
     [-AssignmentCollection <SPAssignmentCollection>]
     [-WhatIf]
     [-Confirm]
     [<CommonParameters>]
```

For more information, see `Clear-SPPeoplePickerDistributionListSearchDomain`.

Get-SPPeoplePickerDistributionListSearchDomain

### Get-SPPeoplePickerDistributionListSearchDomain

Use this cmdlet to return all domains in the People Picker distribution list search domains.

```
Get-SPPeoplePickerDistributionListSearchDomain
   -WebApplication <SPWebApplicationPipeBind>
   [-DomainName <String>]
   [-AssignmentCollection <SPAssignmentCollection>]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

For more information, see `Get-SPPeoplePickerDistributionListSearchDomain`.

Remove-SPPeoplePickerDistributionListSearchDomain

### Remove-SPPeoplePickerDistributionListSearchDomain

Use this cmdlet to remove a domain from the People Picker distribution list search domains.

```
Remove-SPPeoplePickerDistributionListSearchDomain
      -WebApplication <SPWebApplicationPipeBind>
      -DomainName <String>
      [-AssignmentCollection <SPAssignmentCollection>]
      [-WhatIf]
      [-Confirm]
      [<CommonParameters>]
```

For more information, see `Remove-SPPeoplePickerDistributionListSearchDomain`.

Add-SPPeoplePickerServiceAccountDirectoryPath

### Add-SPPeoplePickerServiceAccountDirectoryPath

Use this cmdlet to add an OU to People Picker service account directory path list.

```
Add-SPPeoplePickerServiceAccountDirectoryPath
   -WebApplication <SPWebApplicationPipeBind>
   -OrganizationalUnitName <String>
   [-Index <Int32>]
   [-AssignmentCollection <SPAssignmentCollection>]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

For more information, see `Add-SPPeoplePickerServiceAccountDirectoryPath`.

Clear-SPPeoplePickerServiceAccountDirectoryPath

### Clear-SPPeoplePickerServiceAccountDirectoryPath

Use this cmdlet to clear the OUs of People Picker service account directory path list.

```
Clear-SPPeoplePickerServiceAccountDirectoryPath
     -WebApplication <SPWebApplicationPipeBind>
     [-AssignmentCollection <SPAssignmentCollection>]
     [-WhatIf]
     [-Confirm]
     [<CommonParameters>]
```

For more information, see `Clear-SPPeoplePickerServiceAccountDirectoryPath`.

Remove-SPPeoplePickerServiceAccountDirectoryPath

### Remove-SPPeoplePickerServiceAccountDirectoryPath

Use this cmdlet to remove an OU from People Picker service account directory path list.

```
Remove-SPPeoplePickerServiceAccountDirectoryPath
      -WebApplication <SPWebApplicationPipeBind>
      -OrganizationalUnitName <String>
      [-AssignmentCollection <SPAssignmentCollection>]
      [-WhatIf]
      [-Confirm]
      [<CommonParameters>]
```

For more information, see `Remove-SPPeoplePickerServiceAccountDirectoryPath`.

See also

## See also

- Configure People Picker in SharePoint Server

- Plan for People Picker in SharePoint

Additional resources

## Additional resources

- Last updated on 
		2023-09-12
