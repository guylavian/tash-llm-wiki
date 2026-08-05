---
title: "How to get ActiveSync working with Exchange 2016 mailbox server when Exchange 2010 server is Transport Hub and Client Access"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/385881/how-to-get-activesync-working-with-exchange-2016-m
question_id: 385881
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# How to get ActiveSync working with Exchange 2016 mailbox server when Exchange 2010 server is Transport Hub and Client Access

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/385881/how-to-get-activesync-working-with-exchange-2016-m (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In the process of migrating from Exchange 2010 to Exchange 2016.  

Exchange 2010 currently has all our production mailboxes and is working with ActiveSync, Outlook Anywhere, and OWA.  

When I move a mailbox from the Exchange 2010 server to the Exchange 2016 server I am unable to connect to ActiveSync as I normally would. I assume this is because Exchange 2010 cannot read Exchange 2016 mailboxes.  

What would be the best way to move mailboxes from Exchange 2010 to Exchange 2016 and allow ActiveSync to still work without having to reconfigure our devices to point to a different mail server internet domain for the Exchange 2016 server? Is this possible without reconfiguring the end user ActiveSync devices or moving all of our mailboxes at the same time to the Exchange 2016 server and keeping the same domain settings, just changing the internal routing to the Exchange 2016 server?  

I haven't tested Outlook on the LAN to see if autodiscover will pick up the Exchange 2016 server and work that way nor have I tested Outlook Anywhere yet. I assume getting ActiveSync to work will be a similar process for autodiscover and Outlook Anywhere (pointing the mail server domain to the Exchange 2016 server).

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-05-07*

Hi @Quentin Roberts  ,    

When I move a mailbox from the Exchange 2010 server to the Exchange 2016 server I am unable to connect to ActiveSync as I normally would.    

Is there any detailed error message when this occurs? Are you able to connect normally if reconfiguring the decive(Although noramally this is not necessary as I know.)?    

Any clues if performing an Exchange ActiveSync test using Microsoft Remote Connectivity Analyzer?    

In case it is due to the delay after moving the mailbox, please try to manually recycle the following two applications pools in IIS on Exchange 2016 server and see if it works:    

-  MSExchangeAutodiscoverAppPool     

-  MSExchangeSyncAppPool     

Furthermore, after Exchange 2016 was introduced into the environment, have you completed the post-installation configurations like updating the autodiscover SCP, configuring the URLs for Exchange 2016 virtual directories, updating the DNS records to point to Exchange 2016 server and so on? For more details, you may generate a checklist using the official tool Exchange Deployment Assistant or refer to the guidance in the links below:     

EXCHANGE 2010 TO EXCHANGE 2016 MIGRATION – PART 3    

EXCHANGE 2010 TO EXCHANGE 2016 MIGRATION – PART 4    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Addtionally, if you have any anti-virus software or firewall configured in the environment, it's suggested to try temporarily disabling it to help troubleshoot the issue. As based on my research, similar issues could be related to the NAT policy that still pointing to Exchange 2010, see:    

Activesync Authentication Fails after Mailbox Move    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
