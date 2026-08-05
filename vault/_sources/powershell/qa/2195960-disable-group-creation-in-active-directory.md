---
title: "Disable group creation in Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195960/disable-group-creation-in-active-directory
question_id: 2195960
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
---
# Disable group creation in Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195960/disable-group-creation-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I need to identify all the groups in the Active Directory which give permissions to create groups in the AD.  

Also I need to disable the creation of the on-prem groups.

Is this achievable? Any guidance is appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-25*

Hi,

You can try something like this to list the groups with the Create Group Object permission. Run this PowerShell script on your domain controller or some domain computer with the Active Directory RSAT tool.

$right = [System.DirectoryServices.ActiveDirectoryRights]"CreateChild"

$objects = @()

$OUs = Get-ADOrganizationalUnit -Filter *

$groups = Get-ADGroup -Filter *

Push-Location -Path AD:

$OUs | ForEach-Object {

    $OU=$_

    (Get-Acl -Path $OU).access | Where-Object { ($_.ActiveDirectoryRights -band $right) -and (($_.ObjectType -eq 'bf967a9c-0de6-11d0-a285-00aa003049e2') -or ($_.ObjectType -eq '00000000-0000-0000-0000-000000000000')) }|

    ForEach-Object {

        if( $_.IdentityReference.Translate('System.Security.Principal.SecurityIdentifier') -in $groups.sid) {

            $objects += [PSCustomObject]@{"OU"= $OU.DistinguishedName ; "group" = $_.IdentityReference}

        }

    }

}

Pop-Location

$objects

Best Regards,

Ian Xue

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-21*

Hello,   

Yes, I need to check which groups give permissions to create/delete groups in the whole domain.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-21*

Hi,

A group could have different permissions on different OUs. Do you want to check the permissions on all the OUs in your domain?

Best Regards,

Ian Xue

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-21*

Hello Daisy Zhou,  

The information you have provided is helpful. Thank you.  

However, we have a lot of OUs with a lot of groups. Is there any powershell command/script that can be executed to list all the groups with permissions to create groups?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-21*

Hello Slavi Petrov,  

Thank you for posting in Microsoft Community forum.  

To create a group in AD, you must be a member of the Domain Administrators group, or otherwise be delegated permissions to create new group accounts.  

First  

You can find the AD groups or AD user accounts in Domain Administrators.  

Second  

And find the AD groups or AD user accounts has permissions below.  

For example:  

In my test lab, if I delegate a user account or a group with permissions below, he/she will be able to create group in AD.  

1.Right click one OU or container and select "Delegate Control".  

2.Select "Create a custom task to delegate".  

  

3.Select "Only the following objects in this folder" and check "Group objects".  

And "Create selected objects in this folder" and "Delete selected objects in this folder".  

  

-  Check "General" and "Property-specific" and "Creation/deletion of specific child objects" under "Show these permissions".  

And check "Create All Child Objects" and "Delete All Child Objects" and "Read All Properties" and "Write All Properties".  

5.I can now create a group using the user account above.  

6.Check the permissions I delegated just now.  

  

In summary, you can remove user accounts or groups in Domain Administrators group so that he/she cannot be able to create AD group.  

Or you can uncheck the permissions "Create Group objects" and "Delete Group objects" for specific user accounts or groups so that he/she cannot be able to create AD group.  

Reference

Create a Group Account in Active Directory - Windows Security | Microsoft Learn

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
