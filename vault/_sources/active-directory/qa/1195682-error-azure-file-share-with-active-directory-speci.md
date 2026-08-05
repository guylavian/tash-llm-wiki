---
title: "Error Azure File share with Active Directory Specified Network Password Not Correct"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1195682/error-azure-file-share-with-active-directory-speci
question_id: 1195682
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-files", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Error Azure File share with Active Directory Specified Network Password Not Correct

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1195682/error-azure-file-share-with-active-directory-speci (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I've been reviewing forums and still cannot find a solution to this error. I'm trying to set-up an Azure fileshare, so it is accessible via Active Directory based authentication. I'm going round in circles - so any help would be appreciated !

We have Azure AD connect running successfully and synching Users and groups. I have followed instructions from Microsoft - https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-ad-ds-enable :

-  Enabled AD authentication 

-  Registered my storage account with AD on-premise

-  Have set-up a private end-point for the storage account - which has a DNS record

-  Have created an AD group with members from AD - which have Synched to Azure AD

-  Have assigned that group the SMB contributor role for the storage account. Note currently I am not worried about ACLs and folder level permissions so have not set any up.

-  I login to a windows VM that is domain joined to the on-premise AD

-  When I try to use the Azure script, when I have logged in with the user who is a member of the permissioned group,  that is provided in the "Connect" option - the connection to port 445 is successful, but I get the error when it tried to map the network drive:

```
New-PSDrive -Name Z -PSProvider FileSystem -Root "\\.file.core.windows.net\" -Persist
   New-PSDrive : The specified network password is not correct
   At line:2 char:1
   + New-PSDrive -Name Z -PSProvider FileSystem -Root "\\ ...
   + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       + CategoryInfo          : InvalidOperation: (Z:PSDriveInfo) [New-PSDrive], Win32Exception
       + FullyQualifiedErrorId : CouldNotMapNetworkDrive,Microsoft.PowerShell.Commands.NewPSDriveCommand
```

It does not seem to be using the logged in user's credentials. NOTE: due to our security policies, I have to login to the VM via a remote desktop machine - so it is my desktop-->Remote VM (Azure) --> Windows VM used for connecting to Azure File share.

I have tried using credentials by creating a "PSCredential" Object just to test ,but that didn't work - also it's not a viable option as the target is to have multiple users and service account accessing, and we don't want them to have to hardcode credentials.

Thanks in advance

Fas

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-04*

Hello there,
Can you please cross verify port 445 is enabled
If few Internet provider have blocked port 445, please refer to this article.
SMB has always been a network file sharing protocol. As such, SMB requires network ports on a computer or server to enable communication to other systems. SMB uses either IP Port 445 . 445 is an important port because it is used by default for all SMB communication. Windows uses it for various functions since SMB serves as the network protocol at the application level.
Azure: Summary of ISPs that Allow / Disallow Access from Port 445
https://social.technet.microsoft.com/wiki/contents/articles/32346.azure-summary-of-isps-that-allow-disallow-access-from-port-445.aspx
Hope this resolves your Query !!
--If the reply is helpful, please Upvote and Accept it as an answer--
