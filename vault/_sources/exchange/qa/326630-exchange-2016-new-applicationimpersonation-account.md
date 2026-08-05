---
title: "Exchange 2016 New ApplicationImpersonation Account Not Working After CU19"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/326630/exchange-2016-new-applicationimpersonation-account
question_id: 326630
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 New ApplicationImpersonation Account Not Working After CU19

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/326630/exchange-2016-new-applicationimpersonation-account (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are running Exchange 2016 on Server 2016. After we were informed by Microsoft that we needed to upgrade to CU19 we installed it on the same day.    

Unfortunately it broke our ApplicationImpersonation account that was using the Administrator account. Specifically it has broken a program called Mailstore.    

Mailstore Support said they were confident Microsoft would fix the issue in CU20 but this hasn't happened. We installed CU20 (15.1.2242.4) and rebooted the Exchange server and the problem still exists.    

Mailstore Support said that a work-around would be to create a new ApplicationImpersonation as a lowly user, but I have created the account and assigned it the ApplicationImpersonation role, but Mailstore (the program) just says that the credentials were rejected by EWS:    

An error has occurred.    

Authentication failed (EWS). Check user name and password. If the password is correct, try specifying your UPN Logon (e.g. user@keyman  .com) or DOMAIN\username in the user name field.    

I have tried different username formats but all are rejected.    

Interestingly Vipre Email Security seems to be working fine, but it was set up with ApplicationImpersonation as a lowly user from Day 1.    

Has anyone else seen this? Am I barking up the wrong tree? Any ideas how to get ApplicationImpersonation to work?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-23*

I would open a ticket with Microsoft Support and report this

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-23*

[PS] C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Exchange Server 2016>Get-ManagementRoleAssignment -Role ApplicationImpersonation| fl Name, User, CustomRecipientWriteScope

Name : ApplicationImpersonation-Hygiene Management  

User : DOMAIN/Microsoft Exchange Security Groups/Hygiene Management  

CustomRecipientWriteScope :

Name : ApplicationImpersonation-Organization Management-Delegating  

User : DOMAIN/Microsoft Exchange Security Groups/Organization Management  

CustomRecipientWriteScope :

Name : VIPRE Email Security  

User : DOMAIN/Users/Vipre  

CustomRecipientWriteScope :

Name : MailStore Impersonation  

User : DOMAIN/Users/Mailstore  

CustomRecipientWriteScope :

[PS] C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Exchange Server 2016>Get-ManagementRoleAssignment -I  

dentity "MailStore Impersonation" | fl

RunspaceId : b9f05ce8-6484-4f96-9825-128b81492fd9  

DataObject : MailStore Impersonation  

User : DOMAIN/Users/Mailstore  

AssignmentMethod : Direct  

Identity : MailStore Impersonation  

EffectiveUserName : Mailstore  

AssignmentChain :  

RoleAssigneeType : User  

RoleAssignee : DOMAIN/Users/Mailstore  

Role : ApplicationImpersonation  

RoleAssignmentDelegationType : Regular  

CustomRecipientWriteScope :  

CustomConfigWriteScope :  

RecipientReadScope : Organization  

ConfigReadScope : None  

RecipientWriteScope : Organization  

ConfigWriteScope : None  

Enabled : True  

RoleAssigneeName : Mailstore  

IsValid : True  

ExchangeVersion : 0.11 (14.0.550.0)  

Name : MailStore Impersonation  

DistinguishedName : CN=MailStore Impersonation,CN=Role Assignments,CN=RBAC,CN=First  

Organization,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=DOMAIN,DC=local  

Guid : 59255a4b-6592-4385-baec-47b3820b0de3  

ObjectCategory : DOMAIN/Configuration/Schema/ms-Exch-Role-Assignment  

ObjectClass : {top, msExchRoleAssignment}  

WhenChanged : 19/03/2021 1:34:17 PM  

WhenCreated : 19/03/2021 1:34:17 PM  

WhenChangedUTC : 19/03/2021 12:34:17 AM  

WhenCreatedUTC : 19/03/2021 12:34:17 AM  

OrganizationId :  

Id : MailStore Impersonation  

OriginatingServer : SERVER.DOMAIN  

ObjectState : Unchanged
