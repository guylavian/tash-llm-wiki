---
title: "What is the GPO needed to enalbe windows server audit logging for account lockout"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/62180/what-is-the-gpo-needed-to-enalbe-windows-server-au
question_id: 62180
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# What is the GPO needed to enalbe windows server audit logging for account lockout

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/62180/what-is-the-gpo-needed-to-enalbe-windows-server-au (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to identify where a user account lockout keeps happening, by searching for the source in our DC's event logs -> Windows Logs -> Security, but I am not seeing any lock out events in our domain controller. I can see other successful logon/logoff events for all users, but nothing matching ID 4740 User Account Lockout. My hunch is that this is not enabled/being logged, and I was hoping to find the right GPO setting to enable this.  Is it the GPO for Computer Policies -> Windows Settings -> Security Settings -> Local Policies -> Audit Policy -> Audit User Account Management ? Or is there another one? Please help!!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-14*

Did you check all of the DC's? You can try and use this tool -> https://www.microsoft.com/en-us/download/details.aspx?id=15201 It queries all of the DC's on the network.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-14*

In the corresponding Group Policy Object (or Local policy if you configured auditing there)  

-  Go to Computer Configuration - Policies - Security Settings - Local Policies - Audit Policy  

-  Make sure Audit Account Management is set to Success  

If you use Advanced Audit Policy please check the following setting:  

-  Go to Computer Configuration - Policies - Security Settings - Advanced Audit Policy Configuration - Audit Policies - Account management  

-  Make sure Audit User Account Management is set to Success  

Even if Group Policy Object is configured correctly there might still be some conflicts that prevent GP from applying correctly.  

To find out the effective audit policy on a DC, execute the following command auditpol /get /category:* In the output check that User Account Management is set to Success

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-08-10*

Hi,  

Based on experience,  you are right .  

If you can't find any events about the account lockout , then we need to enable the audit policy on the Domain controllers under[Computer Configuration\Windows Settings\Security Settings\Local Policies\Audit Policy\Audit account management]   

You can enable or disable it as your requirements.  

According to the audit events on PDC determine which clients or DCs sent the failed authentication request. If the failed authentication request was sent by a DC, then we should gather the audit event on the DC. So we can find out which clients sent the BAD password.  

After we get the workstations IP, then we need enable Audit Logon Events – Failure and Audit Process Tracking for this client, then analyze the event log to find out which process or apps send the BAD passwod.  

Best Regards,
