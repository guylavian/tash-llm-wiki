---
title: "On Premise Exchange Server after wonky migration to Identity Hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/312503/on-premise-exchange-server-after-wonky-migration-t
question_id: 312503
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# On Premise Exchange Server after wonky migration to Identity Hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/312503/on-premise-exchange-server-after-wonky-migration-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We were hit with a ransomware attack back in 2019 and lost our Exchange Server 2016. We synced our users from Active Directory to 365 and gave them new mailboxes. Then, we reinstalled Exchange 2016 and restored our old mailboxes. We migrated users' messages from their old mailboxes on the restored-on-premise-server to their new 365 mailboxes. What does this give us? “Identity Hybrid”? The on-premise Exchange server is 2016 with CU19 installed on Windows 2016. It still has all the server roles and footprint as when it was a mailbox and transport server. I’m not confident in my AD setup as far as Exchange is concerned. I’d like to get that disk space back and clean up my environmCan ent. Can I remove the old unused mailboxes and the any link from the AD accounts to them? Can I remove the unused server roles from the server and from Active Directory. Can I migrate the 2016 server to a new server Exchange 2019 on Windows 2019 with only with only the hardware and functionality needed for “Identity Hybrid”? Or decomission the server and install a 2019 server on-premise for management?  

Sorry if I got the tags wrong, or composed the descripton of this mess poorly

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-04*

All mail flow is as expected.    

No issues there.    

I think this would work for me other than any aliases.    

I would also need my account creation to handle the enable-remotemailbox.    

Disable-Mailbox "mailbox identity"    

then    

Enable-RemoteMailbox "user identity" -RemoteRoutingAddress "user@Company portal   .mail.onmicrosoft.com"    

That leaves me seeing the user as "Mailbox Type" "Office 365" on my on premise server ecp.    

I think that is what I need to do, right?    

But now I will need to do that for ALL my users.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-29*

https://learn.microsoft.com/en-us/exchange/troubleshoot/user-and-shared-mailboxes/mailbox-exists-exo-onpremises    

From this article, I am able to     

Disable-Mailbox "mailbox identity"    

then     

Enable-RemoteMailbox "user identity" -RemoteRoutingAddress "user@Company portal   .mail.onmicrosoft.com"    

That leaves me seeing the user as "Mailbox Type" "Office 365" on my on premise server ecp.    

I think that is what I need to do, right?    

But now I will need to do that for ALL my users.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-26*

I am Scenario two.  

I am digesting the article  

My public folders are migrated but the on premise server still says.  

PublicFoldersEnabled : Local  

I'll keep reading

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-23*

I really can't remember how we migrated the messages.  

I think some sort of export / import.  

Can remember how we got Hybrid set up either.  

I don't think it was the wizard.  

There is a mailbox in the cloud currently used, and an unused mailbox containing the migrated messages on-premise,  for each user.  

I will follow your provided links asap.  

I thought I had some time carved out when I posted this.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-15*

Hi @LipschutzDavid-7193      

The official document here introduced about the What is hybrid identity with Azure Active Directory?    

What migration method did you use to finish this? "We migrated users' messages from their old mailboxes on the restored-on-premise-server to their new 365 mailboxes."     

Did you run the HCW to deploy a hybrid between your on-premise Exchange server and O365?     

And now the mailboxes are located in cloud and they still use AAD connect to sync from on-premise right? Correct me if I have any misunderstanding about your environment.    

If you run HCW before to deploy a hybrid, and you have all of mailboxes in Exchange Online. Do not need to manage my users from on-premises and no longer have a need for directory synchronization or password synchronization. Refer to the Scenario one in this official document.    

If you didn't deploy a hybrid previously, refer to this link: Convert Synced user to In Cloud Only User Account on Office365    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
