---
title: "MS Exchange 2019 Install Error - Active Directory Operation Failed on dc.domain - Directory Object Not Found"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/774581/ms-exchange-2019-install-error-active-directory-op
question_id: 774581
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# MS Exchange 2019 Install Error - Active Directory Operation Failed on dc.domain - Directory Object Not Found

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/774581/ms-exchange-2019-install-error-active-directory-op (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Completely new install of MS Exchange 2019, installed all the prerequisites for the Mailbox role successfully and schema created across the 4 domain controllers in the environment.  

Had to manually create the schema on the root domain as the Exchange server was on the child domain, however schema replicated successfully across the domains in the environment.  

During the installation on the Exchange server, the installation stages will always stop at stage 8/12 (Installation of Mailbox role). Checked the logs and it returns the following error messages:  

[ERROR] Active Directory operation failed on dc.domain. The error is not retriable. Additional information: Directory object not found.  

Active Directory response: 0000208D: NameErr: DSID-03100288, problem 2001 (NO_OBJECT), data 0, best match of: 'DC= dc, Dc= dc, Dc= dc'  

[ERROR] The object does not exist  

[ERROR-REFERENCE] Id=MailboxServiceControlLast_05b3bbd421504e0c93fefa6d5d1ae590  

Component=EXCHANGE14:\Current\Release\Shared\Datacenter\Setup  

Setup is stopping now because of one or more critical errors  

Finished executing components tasks  

Ending process Install-MailboxRole  

P.S In the right security groups to execute the installation (Schema and Enterprise Admins).  

Any help or advice will be highly appreciated!

## Answer (community) — community member

*upvotes: 1 · updated: 2022-04-14*

I resolved the issue after several attempts, just to refer to the title of the question, that was related to not preparing the proper FSMO domain.  

For anyone who's had issues with installing Exchange 2019 on a root/child AD forest which has had a previously decommissioned Exchange server please follow to allow proper installation:  

-  Install all the Exchange pre-requisites on the server that sits within the child domain   

-  Run setup PrepareSchema and PrepareAD on the root FSMO, make sure the changes that the commands will apply to AD have been replicated through the forest i.e system mail boxes are present in the root AD.  

-  Then run the PrepareDomain:[child.domain] on the child domain.  

-  Proceed ahead with the installation on the Exchange server (on child domain) as normal - If during the any stage the setup was to fail during the installation - run the setup command using the /Mode:Upgrade switch - this should then force the install to complete and give you access to the Exchange Management Shell.  

-  On the shell run this command - Set-ADServerSettings -ViewEntireForest $true (return no result) (This will enable Exchange to view all the objects created during AD preparation). Then run - Get-Mailbox -Arbitration | select Name,Database - this will return all the system mail boxes residing in the root domain.  

-  Once you have carried out step 5 to fruition - most importantly, check whether your admin account has the attribute homeMDB pointing to a valid Exchange Database (result from using commands in step 5), if not, go on to one of the system mail boxes, right click and click on attribute editor and then confirm that the homeMDB attribute on it is point to the same Exchange server, copy and past this link into your Admin account, then restart the MS Exchange Information Store. Then you should be able to access the EAC and create other mail box users which then automatically populates their accounts with the homeMDB attribute pointing to a valid Exchange database.  

The steps where not followed in order when I resolved the issue, however any one has the same problem installing or upgrading exchange on a root/child AD forest can follow the steps to resolve their issue.  

Hello please tick and accept as answer

## Answer (community) — community member

*upvotes: 0 · updated: 2025-03-05*

Exchange 2019 CU 15 Stuck | Well-Known Object Error

Exchange setup needs the proper access to these well-known objects within Active Directory.

If these objects are deleted or corrupted, but still traces left in the Active Directory.

You will get the error related to Well-Known Object entry.

First these deleted entries needs to be removed from AD and then you will be able to prepare AD and install Exchange CU 15

To fix the issue, follow the step by step guide : https://techijack.com/exchange-2019-cu-15-upgrade-stuck-well-known-object-error/

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-03-16*

If you have a multi-domain forest, you need to run all the prep steps individually:    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2019    

So if you ran this already    

```
\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareSchema
```

Run the next two steps from the root domain as well from an elevated prompt with an account that has the necessary perms:    

```
\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAD
```

then:    

```
Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /PrepareAllDomains
```

Then confirm its replicated:    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prepare-ad-and-domains?view=exchserver-2019#how-do-you-know-this-worked    

Once done, run Exchange Setup again on that server
