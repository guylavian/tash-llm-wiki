---
title: "All about Active Directory CNF object finding validation and removing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/101494/all-about-active-directory-cnf-object-finding-vali
question_id: 101494
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# All about Active Directory CNF object finding validation and removing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/101494/all-about-active-directory-cnf-object-finding-vali (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,  

I need to know all about CNF , How to validate the CNF object and which object i need to keep and which one i have to remove with live example"  

Also, How to rename CNF object ?  

I really appreciate if anyone can help me please.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-09-22*

Hi,    

CNF stands for conflict, it is appended to the common name along with a GUID when a duplicate object exists with the same name.    

For example, object ABC is renamed to be CNF:guid, where "" represents a reserved character, "CNF" is a constant that indicates a conflict resolution, and "guid" represents a printable representation of the objectGuid attribute value.    

This will cause an event ID 12292 to be logged in the system event log on the domain controller. You must clean up Active Directory to resolve this error.    

Following command exmaples can be used to find the CNF     

dsquery * -filter "(cn=cnf:)"    

dsquery * forestroot -gc -attr distinguishedName -scope subtree -filter[RETURN]    

"(|(cn=\0ACNF:)(ou=\0ACNF:))"    

dsquery * forestroot -gc -attr distinguishedName -scope  subtree  -limit 0 -filter "(name=\0ACNF:)" > CNF_Objects.txt    

dsquery * -d yourdomain.com -attr distinguishedName -scope  subtree  -limit 0 -filter "(name=\0ACNF:)" > CNF_Objectstxt    

To remove or rename the CNF,you can do it from the ADSI or ADUC :    

    

Following link for your reference:    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/bb727059(v=technet.10)?redirectedfrom=MSDN    

https://social.technet.microsoft.com/Forums/windowsserver/en-US/80538405-488a-4128-ae0c-5624ce616ae4/adsi-edit-cnf?forum=winserverDS
