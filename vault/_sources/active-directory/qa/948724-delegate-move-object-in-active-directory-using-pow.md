---
title: "Delegate \"Move Object\" in Active Directory using Powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/948724/delegate-move-object-in-active-directory-using-pow
question_id: 948724
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Delegate "Move Object" in Active Directory using Powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/948724/delegate-move-object-in-active-directory-using-pow (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I want to delegate the task "Move Object" in Active Directory. As far as I found in the Internet I need    

-  delete object    

-  create object    

-  write CN, DN and RDN    

I'm using    

```
$aceAccessControlType = 'Allow'  
$aceActiveDirectoryRights = @('CreateChild', 'Delete')  
$aceInheritanceType = 'All'  
  
$aceObject.AddAccessRule((New-Object System.DirectoryServices.ActiveDirectoryAccessRule $delegateObjectSid,$aceActiveDirectoryRights,$aceAccessControlType,$objectType,$aceInheritanceType,$inheritedObjectType))
```

to create the permissions on the OU:    

```
Get-ACL AD:\'OU=Test OU Helmut,OU=IT,DC=domain,DC=local' | select -ExpandProperty Access | where { $PSItem.IdentityReference -eq 'DOMAIN\Move Computer Objects' }  
  
ActiveDirectoryRights : CreateChild, Delete  
InheritanceType       : Descendents  
ObjectType            : 00000000-0000-0000-0000-000000000000  
InheritedObjectType   : bf967a86-0de6-11d0-a285-00aa003049e2  
ObjectFlags           : InheritedObjectAceTypePresent  
AccessControlType     : Allow  
IdentityReference     : DOMAIN\Move Computer Objects  
IsInherited           : True  
InheritanceFlags      : ContainerInherit  
PropagationFlags      : InheritOnly  
  
[...]
```

I am able to create objects in the OU but not in sub OUs. If I delegate using the GUI the Properties look slightly different:    

```
ActiveDirectoryRights : CreateChild, DeleteChild  
InheritanceType       : All  
ObjectType            : bf967a86-0de6-11d0-a285-00aa003049e2  
InheritedObjectType   : 00000000-0000-0000-0000-000000000000  
ObjectFlags           : ObjectAceTypePresent  
AccessControlType     : Allow  
IdentityReference     : DOMAIN\Move Computer Objects  
IsInherited           : True  
InheritanceFlags      : ContainerInherit  
PropagationFlags      : None
```

ObjectFlags and PropagationFlags differ and even though I set "InheritanceType = All'" it results in "Descendants".    

I found https://learn.microsoft.com/en-us/dotnet/api/system.security.accesscontrol.objectaccessrule which has an construtor for both but I cannot create it:    

```
New-Object : A constructor was not found. Cannot find an appropriate constructor for type System.Security.AccessControl.ObjectAccessRule
```

What am I doing wrong, how can I set PropagationFlags and ObjectFlags? Do I at all?    

Thank you!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-31*

Both permissions together work, thank you. Even assigning your suggestion itself does what I need. I misunderstood the intercation of "ObjectType" and "InheritedObjectType". Thank you!    

Parent:    

```
ActiveDirectoryRights : ReadProperty, WriteProperty  
InheritanceType       : All  
ObjectType            : bf9679e4-0de6-11d0-a285-00aa003049e2  
InheritedObjectType   : 00000000-0000-0000-0000-000000000000  
ObjectFlags           : ObjectAceTypePresent  
AccessControlType     : Allow  
IdentityReference     : CONTOSO\Move User Objects  
IsInherited           : False  
InheritanceFlags      : ContainerInherit  
PropagationFlags      : None  
  
ActiveDirectoryRights : ReadProperty, WriteProperty  
InheritanceType       : All  
ObjectType            : bf96793f-0de6-11d0-a285-00aa003049e2  
InheritedObjectType   : 00000000-0000-0000-0000-000000000000  
ObjectFlags           : ObjectAceTypePresent  
AccessControlType     : Allow  
IdentityReference     : CONTOSO\Move User Objects  
IsInherited           : False  
InheritanceFlags      : ContainerInherit  
PropagationFlags      : None  
  
ActiveDirectoryRights : ReadProperty, WriteProperty  
InheritanceType       : All  
ObjectType            : bf967a0e-0de6-11d0-a285-00aa003049e2  
InheritedObjectType   : 00000000-0000-0000-0000-000000000000  
ObjectFlags           : ObjectAceTypePresent  
AccessControlType     : Allow  
IdentityReference     : CONTOSO\Move User Objects  
IsInherited           : False  
InheritanceFlags      : ContainerInherit  
PropagationFlags      : None  
  
ActiveDirectoryRights : CreateChild, DeleteChild  
InheritanceType       : All  
ObjectType            : bf967a86-0de6-11d0-a285-00aa003049e2  
InheritedObjectType   : 00000000-0000-0000-0000-000000000000  
ObjectFlags           : ObjectAceTypePresent  
AccessControlType     : Allow  
IdentityReference     : CONTOSO\Move User Objects  
IsInherited           : False  
InheritanceFlags      : ContainerInherit  
PropagationFlags      : None
```

Child:    

```
ActiveDirectoryRights : CreateChild, DeleteChild  
InheritanceType       : All  
ObjectType            : bf967a86-0de6-11d0-a285-00aa003049e2  
InheritedObjectType   : 00000000-0000-0000-0000-000000000000  
ObjectFlags           : ObjectAceTypePresent  
AccessControlType     : Allow  
IdentityReference     : CONTOSO\Move User Objects  
IsInherited           : True  
InheritanceFlags      : ContainerInherit  
PropagationFlags      : None  
  
ActiveDirectoryRights : ReadProperty, WriteProperty  
InheritanceType       : All  
ObjectType            : bf967a0e-0de6-11d0-a285-00aa003049e2  
InheritedObjectType   : 00000000-0000-0000-0000-000000000000  
ObjectFlags           : ObjectAceTypePresent  
AccessControlType     : Allow  
IdentityReference     : CONTOSO\Move User Objects  
IsInherited           : True  
InheritanceFlags      : ContainerInherit  
PropagationFlags      : None  
  
ActiveDirectoryRights : ReadProperty, WriteProperty  
InheritanceType       : All  
ObjectType            : bf96793f-0de6-11d0-a285-00aa003049e2  
InheritedObjectType   : 00000000-0000-0000-0000-000000000000  
ObjectFlags           : ObjectAceTypePresent  
AccessControlType     : Allow  
IdentityReference     : CONTOSO\Move User Objects  
IsInherited           : True  
InheritanceFlags      : ContainerInherit  
PropagationFlags      : None  
  
ActiveDirectoryRights : ReadProperty, WriteProperty  
InheritanceType       : All  
ObjectType            : bf9679e4-0de6-11d0-a285-00aa003049e2  
InheritedObjectType   : 00000000-0000-0000-0000-000000000000  
ObjectFlags           : ObjectAceTypePresent  
AccessControlType     : Allow  
IdentityReference     : CONTOSO\Move User Objects  
IsInherited           : True  
InheritanceFlags      : ContainerInherit  
PropagationFlags      : None
```

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-31*

```
$aceAccessControlType = 'Allow'  
$aceActiveDirectoryRights = @('CreateChild', 'Delete')  
$aceInheritanceType = 'All'  
$objectType = '00000000-0000-0000-0000-000000000000'  
$aceInheritedObjectType = 'bf967a86-0de6-11d0-a285-00aa003049e2'
```

This results in    

```
Get-ACL AD:\'OU=Test OU Helmut,OU=IT,DC=contoso,DC=com' | select -ExpandProperty Access | where { $PSItem.IdentityReference -eq 'CONTOSO\Move User Objects' }  
  
ActiveDirectoryRights : CreateChild, Delete  
InheritanceType       : All  
ObjectType            : 00000000-0000-0000-0000-000000000000  
InheritedObjectType   : bf967a86-0de6-11d0-a285-00aa003049e2  
ObjectFlags           : InheritedObjectAceTypePresent  
AccessControlType     : Allow  
IdentityReference     : CONTOSO\Move User Objects  
IsInherited           : False  
InheritanceFlags      : ContainerInherit  
PropagationFlags      : None  
  
Get-ACL AD:\'OU=SUB,OU=Test OU Helmut,OU=IT,DC=contoso,DC=com' | select -ExpandProperty Access | where { $PSItem.IdentityReference -eq 'CONTOSO\Move User Objects' }  
  
ActiveDirectoryRights : CreateChild, Delete  
InheritanceType       : Descendents  
ObjectType            : 00000000-0000-0000-0000-000000000000  
InheritedObjectType   : bf967a86-0de6-11d0-a285-00aa003049e2  
ObjectFlags           : InheritedObjectAceTypePresent  
AccessControlType     : Allow  
IdentityReference     : CONTOSO\Move User Objects  
IsInherited           : True  
InheritanceFlags      : ContainerInherit  
PropagationFlags      : InheritOnly
```

I'm able to create / delete in the main OU but not in the sub OU.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-31*

Hi @HelmutRitter-5914     

Can you share how you have defined $objectType and $inheritedObjectType?    

The reason the object and inheritance ID are different is because they are different permissions being assigned.    

The permission you set provides these permissions:    

    

As there is no ObjectType set, then the permissions is defined for all child objects, and only applies to     

Where the delegated permission set by the GUI provides this permission:    

    

This permission will be inherited by all descendants but only apply to computer objects.    

Gary.
