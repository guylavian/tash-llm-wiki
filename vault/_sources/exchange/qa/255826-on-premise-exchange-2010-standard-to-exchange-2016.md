---
title: "on-premise Exchange 2010 Standard to Exchange 2016 Standard \"Office 365 Hybrid message\" preventing setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/255826/on-premise-exchange-2010-standard-to-exchange-2016
question_id: 255826
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# on-premise Exchange 2010 Standard to Exchange 2016 Standard "Office 365 Hybrid message" preventing setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/255826/on-premise-exchange-2010-standard-to-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, we are in the process of performing a test migration (test environment) from an on-premise Exchange 2010 Standard server to a new Exchange 2016 Standard server. The plan is to install a new mailserver next to the old one, install Exchange 2016 and then migrate mailboxes and roles over to the new server. Eventually we will be able to decommission the old mailserver.  

The old mailserver in the domain is running Windows 2008R2 with Exchange 2010 Standard (fully patched)  

The new mailserver will be running Windows Server 2016 with Exchange 2016 Standard. I believe Exchange 2010 cannot be directly migrated to Exchange 2019 so we thought it would be best to take the step from 2010 to 2016 first.   

During the pre-requisites check when verifying and setting the new Active Directory Schema during the Exchange 2016 install we run into an error that prevents the setup to continue:  

HybridConfigurationDetectionException: A hybrid deployment with Office 365 has been detected. Please ensure that you are running setup with the /TenantOrganizationConfig switch. To use the TenantOrganizationConfig switch you must first connect to your Exchange Online tenant via PowerShell and execute the following command: "Get-OrganizationConfig | Export-Clixml -Path MyTenantOrganizationConfig.XML".  

The steps sound clear except the problem is there is no Office365 hybrid setup. At least not anymore. In the past a previous admin tried out a few things with Office365 many years ago. That Exchange Online / Office365 tenant no longer exists and the old "hybrid test" was never removed properly it seems.  

Now it seems I cannot continue the setup of the new mailserver as I have no way to obtain this XML file because there is no Office365 environment anymore. I have not found a good way to simply disable or remove this "hybrid" setup from the Exchange 2010 server itself to tell it to just be a true on-premise server.   

What would be the best next step to try and continue the setup of the new on-premise Exchange 2016 server? Is there any way to bypass this?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-03*

So it turned out that this "Hybrid" message preventing me from continuing the setup only happens when I try to install Exchange 2016 from command line. I have now just tried the GUI installer from the Exchange 2016 ISO and then it never mentions this hybrid thing, not once. I am able to continue the setup without any problems. The only thing that needed to be done was to raise the forest and domain functional level first which was still sitting at "2008" and needed to be 2008R2 or higher.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-02*

Though unsupported, you can use adsiedit and remove that object and see if that works    

At least you can see if that object even exists :    

https://blog.rmilne.ca/2020/07/15/remove-hybridconfiguration-cmdlet/
