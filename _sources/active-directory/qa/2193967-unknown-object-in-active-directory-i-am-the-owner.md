---
title: "Unknown Object in Active Directory - I Am the Owner of the Object"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193967/unknown-object-in-active-directory-i-am-the-owner
question_id: 2193967
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Unknown Object in Active Directory - I Am the Owner of the Object

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193967/unknown-object-in-active-directory-i-am-the-owner (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

OS:  

Server 2012 R2.  

The Issue:  

-  I have an organizational unit in Active Directory that started showing as "Unknown" recently.    

-  To my knowledge, an attempt to delete this OU did not happen, so it's not a case of "lingering objects" post delete.    

-  By checking the status of group policy on the servers I know live in that OU, I can see they are still getting their group policy updates  

-  I am unable to add new servers to the OU - cannot drag and drop into OU and the "move" option does not show the OU as an option.  

-  When I check the properties of the OU  

*  Both the "General" and "Object" tabs show: "The Active Directory Domain Services object could not be displayed.  Unable to view attribute or value.  You may not have permissions to view this object."  

*  The "Security" tab shows the access levels of various user groups.  When I go into "Advanced" under "Security" it shows I am the owner of this object.  

What I've tried:  

-  I followed the steps found here: https://support.microsoft.com/en-us/help/305104/you-cannot-delete-an-active-directory-object-of-unknown-type  

..but since I am already the owner, it didn't help me.  I even tried changing the owner from "Domain Admins" (of which I am a member of) to my own name, just to see if it would automagically 'wake up' for me, but that didn't work, so I changed the owner back
 to "Domain Admins".  

-  I tried running this command in Powershell to pull all OU's, but the OU in question did not get returned:  

Get-ADOrganizationalUnit -Filter 'Name -like "*"' | FT Name, DistinguishedName -A  

-  The goal of running the above ^^ command was to at least get a list of all servers living in that OU so I could recreate it.  

-  I followed the steps here, just in case we had accidentally set the owner to "Deny All", not the case: http://www.chicagotech.net/winissues/adpermission3.htm  

-  Lastly, I tried to navigate to CN=Deleted Objects just to confirm the object wasn't inadvertently deleted by a team member, no luck there either:  

https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd379509(v=ws.10)  

Requested Help:  

-  Any other ideas on how I could revive this OU?    

-  I really can't afford to lose all of the servers that live in this OU.  Is there any way to get the contents of the OU and move them to a new OU via Powershell command perhaps?  

-  In the state that it's in, I don't even think we are going to be able to delete this OU by right clicking on it + then selecting delete (I haven't tried, yet).  If I am able to recreate it, any ideas on how to delete the 'bad'/Unknown OU (Powershell maybe)?  

Thanks in advance!

## Answer (community) — community member

*upvotes: 0 · updated: 2018-01-19*

Hi,

Your question is beyond the scope of these Forums

This Community is mainly for home users and their computer problems, not business systems.

Kindly post your question in the TechNet Server Forums.

http://social.technet.microsoft.com/Forums/windowsserver/en-US/home?category=windowsserver

TechNet Forums: 

https://social.technet.microsoft.com/Forums/en-US/home

MSDN Forums:

https://social.msdn.microsoft.com/Forums/en-US/home

Cheers.
