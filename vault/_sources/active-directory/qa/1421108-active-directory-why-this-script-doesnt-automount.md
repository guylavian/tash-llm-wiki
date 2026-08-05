---
title: "Active directory - Why this script doesn't automount home in H:"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1421108/active-directory-why-this-script-doesnt-automount
question_id: 1421108
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Active directory - Why this script doesn't automount home in H:

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1421108/active-directory-why-this-script-doesnt-automount (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This script configures the desired parameters for the user, as verified in the Active Directory Users & Computers properties screen. However, despite having access via the <server>\home<username> shared resource, the $homeDirectory is not being mounted on the H: drive.

Interestingly, after opening a user's properties in AD Users & Computers, and making changes to any field (e.g., address), the $homeDirectory is successfully mounted on the H: drive upon logging out and logging back in.

What could be causing this issue?

```
param(
  [Parameter(Mandatory=$true)][string]$UserName,
  [string]$ServerName = $env:COMPUTERNAME,
  [string[]]$DomainName = ([System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()).Name -split "\.",
  [string[]]$OrganizationUnits = @(),
  [string[]]$Groups = @(),
  [string]$DriveLetter = "H",
  [int]$PasswordLength = 8
)

$homeDirectory = "\\$ServerName\home\$UserName"
$profileDirectory = "\\$ServerName\profile\$UserName"
#$script = "\\$ServerName\$ScriptPath"
$pwdAllowedSymbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*-_,.;:"
$randomPassword = -join($pwdAllowedSymbols.ToCharArray() | Get-Random -Count $PasswordLength)

New-ADUser -Name $UserName -SamAccountName $UserName -UserPrincipalName "$UserName@$($DomainName -join '.')" -Path "OU=$($OrganizationUnits -join ',OU='),DC=$($DomainName -join ',DC=')" -AccountPassword (ConvertTo-SecureString "$randomPassword" -AsPlainText -Force) -Enabled $true

echo "$UserName $randomPassword" >> pwd.txt

foreach ($group in $Groups) {
    add-ADGroupMember -Identity $group -Members $UserName
}

Set-ADUser $UserName -HomeDrive $DriveLetter -HomeDirectory "$homeDirectory" -ProfilePath "$profileDirectory"

mkdir $homeDirectory

$acl = Get-Acl $homeDirectory

$rule1 = New-Object System.Security.AccessControl.FileSystemAccessRule("${UserName}", "FullControl", "None", "NoPropagateInherit", "Allow")
$rule2 = New-Object System.Security.AccessControl.FileSystemAccessRule("${UserName}", "FullControl", "ContainerInherit, ObjectInherit", "InheritOnly", "Allow")
$rule3 = New-Object System.Security.AccessControl.FileSystemAccessRule("Administradores", "FullControl", "None", "NoPropagateInherit", "Allow")
$rule4 = New-Object System.Security.AccessControl.FileSystemAccessRule("Administradores", "FullControl", "ContainerInherit, ObjectInherit", "InheritOnly", "Allow")

$acl.AddAccessRule($rule1)
$acl.AddAccessRule($rule2)
$acl.AddAccessRule($rule3)
$acl.AddAccessRule($rule4)

Set-Acl -Path $homeDirectory -AclObject $acl
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-09*

Maybe dump the user properties before and after you did the change and see what properties (other than the address for testing) changed after you saved?
