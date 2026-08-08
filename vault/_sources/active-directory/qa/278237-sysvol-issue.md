---
title: "Sysvol issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/278237/sysvol-issue
question_id: 278237
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Sysvol issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/278237/sysvol-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have a singel domain with 3 DC's .2 of them is server 2008 R2 and 1 is a VM server 2012 R2. Last week we had a issue with our domain and we had to restore the VM server 2012 R2. I have siezed all the FSMO roles from the DC 2008 R2 and cleaned up the metadata for one of the server 2008 R2 DCs and othere one didn't cleanup yet.  

Now when on the VM DC that has all FSMO role click on the default domain policy  get the this message  

Permissions for this GPO in the SYSVOL folder are inconsistent with those in Active Directory, click yes to set permission.  

Should we go ahed with Yes option? or we can correct this issue some other way?  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-18*

Thanks for your reply,  

This artical talking aobut DC that running the server 2008 R2, my issue is on server 2012 R2, but removed DC's are server 2008 R2.  

Can we use the steps for 2012 r2 as well?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-18*

Hello @Shahin Mortazave  ,    

Thank you for posting here.    

Based on the following article, if you have permissions to modify security on the default GPOs, select OK in response to the message that is mentioned in the Symptoms section. This action modifies the ACLs on the Sysvol part of the Group Policy Object and makes them consistent with the ACLs on the Active Directory component.     

Reference    

"Permissions for this GPO in the SYSVOL folder are inconsistent with those in Active Directory" message when you run GPMC    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/permissions-this-gpo-inconsistent    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou
