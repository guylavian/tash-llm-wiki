---
title: "Audit Monitoring - Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/98336/audit-monitoring-domain-controller
question_id: 98336
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Audit Monitoring - Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/98336/audit-monitoring-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I have 8 domain controllers and some of the admins have RSAT - Remote server administration tool locally installed on Windows 10 machines.  

For resetting the password or any other activity they do it locally which is not getting logged in domain controller audit security event. Is there a way we can monitor this RSAT activity. Please suggest

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2020-09-18*

You can create a group policy targeting your domain controllers to enable Security Audit, specifically "Audit account management", you can find the documentation about these events here: https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-account-management    

So, you need to configure auditing under Computer Configuration\Windows Settings\Security Settings\Local Policies\Audit Policy.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-09-23*

Hi,    

Based on my understanding, even the changes were made from the workstation ,the events for the account management should be also logged on the DCs.    

Even we manage the accounts from the workstations, the opteration should by done by connect to the DCs.     

I also did a test : i try to change password and create new user accounts through RSAT from the workstation, the management events were logged on the DCs.    

So i would recommend you check if the the audit policy was on the DCs by :    

Configure the settings to success and failure through the Advanced Audit Policy.    

    

Then run gpupdate /force on the DC and run command :gpresult /h to confirm if the policy was applied successfully.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-20*

Yes we tried this option but still the local computer audit information is not stored in the domain controller.  

Only changes on Domain Controller is getting stored. Please let me know if there is any other way we can monitor this
