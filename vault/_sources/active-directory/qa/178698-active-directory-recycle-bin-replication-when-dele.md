---
title: "Active Directory Recycle Bin Replication (When Deleted Timestamp)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/178698/active-directory-recycle-bin-replication-when-dele
question_id: 178698
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Active Directory Recycle Bin Replication (When Deleted Timestamp)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/178698/active-directory-recycle-bin-replication-when-dele (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I think I've found a bug (or undocumented feature) of the AD Recycle Bin. I noticed the behavior in a production environment and have successfully replicated it in a lab environment. I'll start with the boring screenshots.    

    

    

    

Note in the above image that DC001 & DC002 existed on or prior to 2020-09-26. DC003 was promoted on 2020-11-26. Now to demonstrate the behavior.    

    

    

Note the "when deleted" timestamps in the above screenshot when the client system is querying DC001. Before taking the next screenshot I turned off DC001 and DC002, leaving only DC003.    

    

After restarting ADAC, lo and behold! We've invented a time machine!    

    

So what's going on here? Is this a "feature" of some kind which is in place to prevent some kind of recycling edge case? What happens when DC001 or DC002 recycles a deleted object? Will DC003 also set the object to recycled in its database? Or will it be delayed for the two month period? Why is this attribute not replicated to (new) domain controllers? Newly deleted objects are consistent across all DCs. I find this quite strange and would be interested if any AD experts or engineers could offer comment.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-29*

Ok. I think i have the answer. The whenChanged timestamp is different because when the object gets synced from one DC to another, the CN attribute is updated locally on a domain controller. In the above case, I pulled up replication metadata for the object using Get-ADReplicationAttributeMetadata "objectguid" DC1 -IncludeDeletedObjects. Found that the CN attribute was written locally.

For reference, DC1 is my initial DC where the objects were deleted, DC2 was promoted post deletion.

AttributeName : cn  

AttributeValue : 1 DEL:644a2714-a8d7-4085-be29-4f6d8f546595  

FirstOriginatingCreateTime :  

IsLinkValue : False  

LastOriginatingChangeDirectoryServerIdentity : CN=NTDS Settings,CN=dc2,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=domain,DC=xyz  

LastOriginatingChangeDirectoryServerInvocationId : dff517d6-5643-4284-bdce-2dd7aa21e933  

LastOriginatingChangeTime : 11/29/2020 5:48:31 AM  

LastOriginatingChangeUsn : 8359  

LastOriginatingDeleteTime :  

LocalChangeUsn : 8359  

Object : CN=1\0ADEL:644a2714-a8d7-4085-be29-4f6d8f546595,CN=Deleted  

Objects,DC=domain,DC=xyz  

Server : dc2.domain.xyz  

Version : 1

However the object will be recycled at the same time on both the domain controllers as isdeleted time is same on both DC's.

Replication metadata for isdeleted attribute on Dc1

AttributeName : isDeleted  

AttributeValue : True  

FirstOriginatingCreateTime :  

IsLinkValue : False  

LastOriginatingChangeDirectoryServerIdentity : CN=NTDS Settings,CN=DC1,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=domain,DC=xyz  

LastOriginatingChangeDirectoryServerInvocationId : a5068914-cafa-4a65-852d-e51f93b30e3e  

LastOriginatingChangeTime : 11/28/2020 6:58:16 PM  

LastOriginatingChangeUsn : 24633  

LastOriginatingDeleteTime :  

LocalChangeUsn : 24633  

Object : CN=1\0ADEL:644a2714-a8d7-4085-be29-4f6d8f546595,CN=Deleted Objects,DC=domain,DC=xyz  

Server : DC1.domain.xyz

Version : 1

Replication metadata for isdeleted attribute on Dc2

AttributeName : isDeleted  

AttributeValue : True  

FirstOriginatingCreateTime :  

IsLinkValue : False  

LastOriginatingChangeDirectoryServerIdentity : CN=NTDS Settings,CN=DC1,CN=Servers,CN=Default-First-Site-Name,CN=Sit  

es,CN=Configuration,DC=domain,DC=xyz  

LastOriginatingChangeDirectoryServerInvocationId : a5068914-cafa-4a65-852d-e51f93b30e3e  

LastOriginatingChangeTime : 11/28/2020 6:58:16 PM  

LastOriginatingChangeUsn : 24633  

LastOriginatingDeleteTime :  

LocalChangeUsn : 8359  

Object : CN=1\0ADEL:644a2714-a8d7-4085-be29-4f6d8f546595,CN=Deleted  

Objects,DC=domain,DC=xyz  

Server : dc2.domain.xyz  

Version : 1

Hope this clarifies why we have this behavior.

Please don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-28*

Hi,  

I don't think that is a replication issue because there is no attribute WhenDeleted it should be a bug on the directory administrative center wizard.  

When a object is deleted , it will be moved temporary to recycle bin (deleted objects).  

If you want know when this object was deleted you can use the following powershell command to display the value of the attribute whenChanged :  

```
get-adobject -filter "samaccountname -eq ''Accountname'" -includedeletedobjects -properties WhenChanged
```

Please don't forget to mark this reply as answer if it help you to fix your issue
