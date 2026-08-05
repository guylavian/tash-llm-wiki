---
title: "Installing Exchange Server 2019 on Server 2022 CU 13."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2186801/installing-exchange-server-2019-on-server-2022-cu
question_id: 2186801
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Installing Exchange Server 2019 on Server 2022 CU 13.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2186801/installing-exchange-server-2019-on-server-2022-cu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Currently I have 2 2016 Exchange Servers installed on 2 Server 2016. These are setup in a hybrid O365. 

The goal was to install 2 server 2022's and install Exchange 2019 and decom the 2016's. 

This has now happened on 4 servers on 2 different domains in the last 24 hours. I manually extended the schema without error.   

I manually installed all pre-req's and roles without error. I validated the Enterprise Admin access on my account. When installing Management Tools only on the new servers I receive these error's:  

[10/14/2023 00:45:44.0332] [2] [ERROR] The operation couldn't be performed because object 'EXCH-x' couldn't be found on 'DC-2.x'. 

[10/14/2023 00:45:44.0332] [2] [ERROR] The operation couldn't be performed because object 'EXCH-x' couldn't be found on 'DC-2.x'.  

[10/14/2023 00:45:44.0348] [2] Beginning processing Write-ExchangeSetupLog 

[10/14/2023 00:45:44.0348] [2] [WARNING] EXCH-x is not an Exchange Server.  Unable to set monitoring and server state to active.  Setup will continue. 

[10/14/2023 00:45:44.0348] [2] Ending processing Write-ExchangeSetupLog 

[10/14/2023 00:45:44.0348] [1] Finished executing component tasks. 

[10/14/2023 00:45:44.0363] [1] Ending processing Start-PostSetup 

[10/14/2023 00:45:44.0363] [0] The Exchange Server setup operation completed successfully.  

No error's are listed during the install process. By all accounts the installation was successful and the Exchange Shell is present along with the tools. However this is not an exchange server. It is not recognized as an exchange server.   

Last night when attempting to fix this on one of the domains, I did a complete uninstall/reinstall of the exchange servers and the pre-req's and was successful in the installation. It worked.   

I attempted to do this on the other 2 servers on the other domain and no joy. I attempted multiple times on the new domain that is a multi domain forest; and this error keeps coming up no matter what I do.   

Reviewing the emerging Exchange errors I do see this error is listed a few months back for CU12 about the Jan Security update but its specifying the "UINSTALL" not install that i'm attempting here. Other than this this error seems to be a mystery as far as I can tell in my research.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-16*

Hello Christopher L. Martinez

Thank you for posting in Microsoft Community forum.  

Based on the description, I understand your question is related to Exchange Server.   

Since there are no engineers dedicated to Exchange Server in this forum. In order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.  

Questions - Microsoft Q&A  

Click the "Ask a Question" button in the upper right corner to post your question and select "Exchange Server" tag.

Thank you for your understanding and support.  If you have any question or concern, please feel free to let us know.

Have a nice day.

Best Regards,

Hania Lian
