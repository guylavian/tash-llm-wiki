---
title: "The sysvol permissions for one or more GPOs on this domain controller are not in sync with the permissions for the GPOs on the baseline domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/149354/the-sysvol-permissions-for-one-or-more-gpos-on-thi
question_id: 149354
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# The sysvol permissions for one or more GPOs on this domain controller are not in sync with the permissions for the GPOs on the baseline domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/149354/the-sysvol-permissions-for-one-or-more-gpos-on-thi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi we have a problem,     

we have 8 DC (all DC is windows server 2016 , we change permission one of GPO in my primary dc, but in gpmc we see error in acl permission , this is my screenshoot     

when we click detect now 8 DC just in progress, anyone can help? maybe anyone know to solve this problem?    

Thanks

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-07-05*

Hi,  

this issue has happened to me as well, the problem disappeared after the domain controllers were restarted due to maintenance. Or at least you can try to restart DFS and DFSR services as the issue relates to GPO ACLs not replicating to other domain controllers.  

Another reason of ACLs not in sync can be a bug where Domain Admins ACEs are duplicated on GPOs. If the GPOs were created earlier before this was fixed by Microsoft, their duplicate ACEs are unchanged.  

In case you see duplicite ACE "Domain Admins":(OI)(CI)(F)" in your GPO using icacls command, you can fix it be removing ACE and granting it again:  

icacls "{GPO UID}" /remove:g "<localdomain>\Domain Admins"  

icacls "{GPO UID}" /grant "<localdomain>\Domain Admins":(OI)(CI)(F)  

More information on this: https://social.technet.microsoft.com/Forums/ie/en-US/f16b0af1-8772-4f96-a9ac-fac47943e8e9/sysvol-permissions-for-one-or-more-gpo-are-not-in-sync?forum=ws2016

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-03*

Hi,    

If the new ACLs are not replicated on all domain controllers, you can perform a non-authoritative restore for sysvol replication.    

force-authoritative-non-authoritative-synchronization    

Please don't forget to mark this reply as answer if it help your to fix your issue
