---
title: "Exchange 2016 CU23 Update\\Setup Stuck on Languages (Step 8)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1160330/exchange-2016-cu23-updatesetup-stuck-on-languages
question_id: 1160330
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange 2016 CU23 Update\Setup Stuck on Languages (Step 8)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1160330/exchange-2016-cu23-updatesetup-stuck-on-languages (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Colleague,

I need urgent help and assistance. I have started exchange 2016 CU23 upgrade on one of the exchange node after putting the server into maintenance mode. The upgrade started 7 hour ago but i noticed its stuck/hang on language step no.8. Its not moving. I can only see in the logs

"Finished updating performance counter strings". 

Since the revert back / restore the VM is very hard process. I want the successful completion of upgrade. 

Thank you in advance while understanding this situation.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-16*

For the Error - "Event code: 3008 Event message: A configuration error has occurred"  

The fix is to change the websites application pool to use .NET CLR Version 4 rather than .NET CLR Version 2

So, open IIS, choose Application Pools from the left-hand navigation, Choose your app pool and click basic settings to open the dialog to change which .NET CLR Version to use.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-13*

@amit @Yuki

Thank you for your response.

We have already disabled AV on VM and also enabled the internet on the server. But still no luck.

We can only see the below in ExchangeSetup.log file.

"Finished updating performance counter strings".

And Some warning in Event viewer. 

"Event code: 3008 

 Event message: A configuration error has occurred"

Thank you all understanding this pain and appreciate further recommendation or steps.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-13*

Hi @Fayaz khan, 

The upgrade started 7 hour ago but i noticed its stuck/hang on language step no.8. Its not moving.

Based on my experience, this issue is often found to be related to antivirus software, in particular real-time protection. So, it's recommended to check if you have any antivirus software running on the server, disabling the real-time protection if it exists and see the result.

Below are some relevant links for your reference:

-  Exchange 2010 SP3 Installation hangs Language Pack Hell

-  Exchange Install Hangs on Languages Step  

   (Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.）

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-13*

Based on my research, one of the possible causes of this issue is the antivirus. The solution is to disable the real-time protection of your antivirus before installing or upgrading Exchange. Make sure you have all the exceptions in place, as outlined in this Microsoft TechNet article. 

See Exchange Install Hangs on Languages Step for more details.
