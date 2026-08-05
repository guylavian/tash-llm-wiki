---
title: "[Migrated from MSDN Exchange Dev]White list (domain or sender) - how to ByPass IPBlockListProvider"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/142318/migrated-from-msdn-exchange-dev-white-list-domain
question_id: 142318
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev]White list (domain or sender) - how to ByPass IPBlockListProvider

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/142318/migrated-from-msdn-exchange-dev-white-list-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Non-developer Exchange forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.

[MSDN Link]  

White list (domain or sender) - how to ByPass IPBlockListProvider

[Original post]  

Hi

I am running Exchange Server 2019 - Version 15.2  

I would like some help regarding White list, I have configured white list in two location but RBL List from the IPBlockListProvider is always blocking FIRSTLY the IP.

How to bypass any check (antispam, rbl list) for a specific domain?  

From example, I wanted to add ******@mybigspamtest.com to bypassed always by the AntiSpam.

1) From the ContentFilterConfig  

I added here: Set-ContentFilterConfig -BypassedSenderDomains mybigspamtest.com t  

result : if the IP is not from the RBL list (example SpamHaus), the antispam would not check this messager from mybigspamtest.com

But when the IP is blacklisted in the RBL List: this message is blocked and would not be received.

2) I test also to add this from the RULES with "ByPass spam filtering" but the Block List provider is always blocking first.

I am writing you also my configuration in my Transport agent policy is :

[PS] C:\Program Files\Microsoft\Exchange Server\V15\Scripts>Get-transportagent

So my question is how to bypass a domain or a specific sender correctly ?

many thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-29*

Any idea please?  

I want to bypass an IP or a Domain in the connection filtering.  

Currently, a server listed in RBL List from the IPBlockListProvider configured on exchange is not bypassed, I would like to know how can I do exception.  

thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-28*

I have a new problem, after having adding the whitelist with the IPAllowListProvider:  

-  RBL List (block) is not working anymore: my current IPBlockListProvider (SpamHaus...Spamcom..etc..) is not working even if I restat also the server or the ms exchangetransport.  

After removing the IPAllowListProvider with the commande line   

Remove-IPAllowListProvider -identity  

and restarted   

Restart-Service MSExchangeTransport  

IPBlockListProvider is working back.  

So this is a problem because I cannot bypass any Sender or any domain from the connection filtering.  

thank you for the help!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-28*

Hi, seems to work after setting this configuration bellow. I restart the Exchange service Transport but it take like 5 minutes before working.  

Good test has been done with this anonymous email test https://emkei.cz/  

There IP is blacklist from well known list like SpamHaus  

So after adding for example the domain "mybigtest.com", this is working fine and I could receive emails from a blacklist server.  

Last question, the microsoft documentation explain how to add the "white list domain":  

Add-IPBlockListProvider -Name "Contoso IP Block List Provider" -LookupDomain rbl.contoso.com -BitmaskMatch 127.0.0.1  

Is it important to add the  

 -BitmaskMatch 127.0.0.1   

?  

thank you.  

My Setup:  

[PS] C:\Program Files\Microsoft\Exchange Server\V15\Scripts>Get-IPAllowListProvidersConfig | Format-List *MailEnabled  

ExternalMailEnabled : True  

InternalMailEnabled : False  

[PS] C:\Program Files\Microsoft\Exchange Server\V15\Scripts>Add-IPAllowListProvider -Name "mybigtest.com" -LookupDomain mybigtest.com  

Name    LookupDomain Priority  

mybigtest.com mybigtest.com     1  

[PS] C:\Program Files\Microsoft\Exchange Server\V15\Scripts>Get-IPAllowListProvidersConfig | Format-List Enabled  

Enabled : True  

[PS] C:\Program Files\Microsoft\Exchange Server\V15\Scripts>Get-IPAllowListProvider  

Name      LookupDomain  Priority  

mybigtest mybigtest.com 1

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-28*

Thank you for your answer.    

This Exchange sever 2019 is deployed in a standalone server. This is a single server with all the mailbox installed on this server. I do not find the Edge role installed with my check Get-ServerComponentState and Get-TransportAgent as I wrote in the first post.    

I understand now better that the "Connection filter agent" is working before than the "Content filtering" but I could not find any settings how to bypass for a specific domain.    

MailFlow/Rules is not working, this work only for content filtering Step.    

The connection filter agent gives possibility to add and exclude an IP (Get-IPAllowListEntry) but not a domain or a specific mail address.    

My question is how to exclude a specific domain or email from the connection filter Agent?    

thank you

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-28*

Hi,    

Do you have an edge transport server configured with Connection filtering agent in your environment?    

According to this article:    

    

By default,the connection filter agent(which has the feature IPBlockListProvider)works first to filter the incoming mails.    

So you need to configure it to bypass the specific domains.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
