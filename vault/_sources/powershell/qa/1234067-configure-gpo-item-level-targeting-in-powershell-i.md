---
title: "Configure GPO item level targeting in PowerShell instead of GUI"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1234067/configure-gpo-item-level-targeting-in-powershell-i
question_id: 1234067
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
---
# Configure GPO item level targeting in PowerShell instead of GUI

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1234067/configure-gpo-item-level-targeting-in-powershell-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there a way to add multiple computers to the "Item Level Targeting" section of a GPO using PowerShell, instead of doing each one manually in the GUI?  

For example, I have a GPO that edits registry entries.  I have five separate reg changes listed in the policy and I want to add a different list of computer names to the Item Level Targeting section of each entry in the GPO, using the OR variable for each hostname.  

I have a script I am working with but it returns errors ( I have removed reg entry and actual hostnames from script).

```
Import-Module GroupPolicy

$GPOName = "YourGPOName"
$RegistryKeys = @{
    "Key1" = "HKLM:\Software\YourCompany\YourProduct\Key1"
    "Key2" = "HKLM:\Software\YourCompany\YourProduct\Key2"
    "Key3" = "HKLM:\Software\YourCompany\YourProduct\Key3"
    "Key4" = "HKLM:\Software\YourCompany\YourProduct\Key4"
    "Key5" = "HKLM:\Software\YourCompany\YourProduct\Key5"
}
$ComputerLists = @{
    "Key1" = @("Computer1", "Computer2", "Computer3")
    "Key2" = @("Computer4", "Computer5", "Computer6")
    "Key3" = @("Computer1", "Computer3", "Computer5")
    "Key4" = @("Computer2", "Computer4", "Computer6")
    "Key5" = @("Computer1", "Computer6")
}

foreach ($RegistryKey in $RegistryKeys.Values) {
    foreach ($ComputerList in $ComputerLists[$RegistryKeys.Keys[$RegistryKeys.Values.IndexOf($RegistryKey)]]) {
        $Target = New-GPItemLevelTargetingComputerItem -ComputerName $ComputerList -LogicalOperator Or
        Add-GPItemLevelTargetingEntry -Name $GPOName -Target $Target -ItemLevelTarget "Registry" -RegistryKey $RegistryKey
    }
}
```

Thank you,

## Answer (community) — community member

*upvotes: 2 · updated: 2023-04-14*

This is the error I get:

```
Index operation failed; the array index evaluated to null.
At line:2 char:31
+ ... uterList in $ComputerLists[$RegistryKeys.Keys[$RegistryKeys.Values.In ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (:) [], RuntimeException
    + FullyQualifiedErrorId : NullArrayIndex
 
Index operation failed; the array index evaluated to null.
At line:2 char:31
+ ... uterList in $ComputerLists[$RegistryKeys.Keys[$RegistryKeys.Values.In ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (:) [], RuntimeException
    + FullyQualifiedErrorId : NullArrayIndex
 
Index operation failed; the array index evaluated to null.
At line:2 char:31
+ ... uterList in $ComputerLists[$RegistryKeys.Keys[$RegistryKeys.Values.In ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (:) [], RuntimeException
    + FullyQualifiedErrorId : NullArrayIndex
 
Index operation failed; the array index evaluated to null.
At line:2 char:31
+ ... uterList in $ComputerLists[$RegistryKeys.Keys[$RegistryKeys.Values.In ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (:) [], RuntimeException
    + FullyQualifiedErrorId : NullArrayIndex
 
Index operation failed; the array index evaluated to null.
At line:2 char:31
+ ... uterList in $ComputerLists[$RegistryKeys.Keys[$RegistryKeys.Values.In ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (:) [], RuntimeException
    + FullyQualifiedErrorId : NullArrayIndex
```
