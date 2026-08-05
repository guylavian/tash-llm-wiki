---
title: "Certificates not propagating via GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/228644/certificates-not-propagating-via-gpo
question_id: 228644
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Certificates not propagating via GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/228644/certificates-not-propagating-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have a user Tom in AD    

    

My AD must be structured correctly because for SQL Server in the same domain, user permission is assigned only to BBLabInternalUsers group, and user Tom can connect to the data.    

I want to send him a Column Master Key via Group Policy to decrypt some columns, but the certificate doesn't propagate: The GPO looks like this:    

    

I am using gpupdate /force on the client computer but cannot see the certificate on the client computer. Any suggestions gratefully received,    

Jack

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-13*

Looks like the note I posted 3 hrs ago was wrong - I checked again and the certificate was pushed to the client machine. Maybe I ran gpupdate a bit too soon.  

Unfortunately, it doesn't enable the client to decrypt the columns in the SQL table, but I guess that's a separate problem.  

Thanks for your assistance,  

Jack

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-13*

FanFan, thanks very much, you are pointing me in the right direction!  

But no luck yet. I removed the certificate from the Computer Configuration and imported it to User Configuration / Windows Settings / Security Settings / Public Key   

Policies / Trusted People. Then I deleted the link to the OU and linked the GPO to the domain.  

But the user still cannot see the certificate after gpupdate /force.  

Did I miss something?  

Jack

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-13*

Thanks for the link. It says: "Next step is to link gpo either domain, OU (organization unit) or site." It then shows 'right-click a domain, and select Link Existing GPO'. If I do that, yes, it does push the certificate to the client machine, but I don't want to do that for the the entire domain. I want it to push the certificate to the user's personal certificate store on the client machine.  

If I right-click on the OU and select Link Existing GPO, it fails to push the certificate to the client machine (after gpupdate / force).  

Thanks again, but not quite there.  

Jack

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-13*

@Auntiejack       

Please verify the below url for setup process.     

How to Deploy SSL Certificate on a Computers Using GPO    

Let me know if any help required.    

----------    

Please don’t forget to `"Accept the answer"` and` up-vote` wherever the information provided helps you, this can be beneficial to other community members.
