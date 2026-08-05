---
title: "event id 3041 on Domain Controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/986036/event-id-3041-on-domain-controllers
question_id: 986036
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# event id 3041 on Domain Controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/986036/event-id-3041-on-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi I have a couple of Windows Server 2019 Domain Controllers where the 3041 event ID is showing: ![235770-image.png][1] I found this vulnerability, but to me is not totally clear, I will try to explain it (https://support.microsoft.com/en-us/topic/2020-ldap-channel-binding-and-ldap-signing-requirements-for-windows-kb4520412-ef185fb8-00f7-167d-744c-f299a66fc00a#bkmk_table2): - The article recommends to install the March, 2020 updates on the Domain Controllers, but I cannot get them, I tried to download them from this web site: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2017-8563 - What should I do on Windows clients machines? - Registry settings such as LDAPServerIntegrity and LdapEnforceChannelBinding, are they need to be modified? Thank you in advance. [1]: /api/attachments/235770-image.png?platform=QnA

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-07*

Yesterday I installed a 2208 cumulative update (KB5016690) on one DC, after the reboot, there were some warnings in the event viewer: 6038 - LsaSrv, 2886 – ActiveDirectory_DomainService, and 3041 LDAP Interface, today just the event ID 3041 showed.    

I looked it up on internet, and for the event ID 2886, there is a policy setting that people recommend: “Computer Configuration>Policies>Windows Settings>Security Settings>Local Policies>Security Options.    

Right-click on Domain Controller: LDAP Server Signing Requirements and select properties.    

Check off Define this Policy Setting.    

Select Require Signing in the drop-down box"    

I am not totally sure if this going to help because this were mainly applied on Windows Server 2008 operating system, there is nothing about Windows Server 2019. I am also not sure why the event ID 3041 is still showing. Is there any other recommendation?    

Regards,    

Abraham.
