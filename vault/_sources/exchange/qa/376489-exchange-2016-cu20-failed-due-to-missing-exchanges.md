---
title: "Exchange 2016 CU20 failed due to missing \"exchangeserver.msi\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/376489/exchange-2016-cu20-failed-due-to-missing-exchanges
question_id: 376489
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange 2016 CU20 failed due to missing "exchangeserver.msi"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/376489/exchange-2016-cu20-failed-due-to-missing-exchanges (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016 Build 15.1.225.42.  Attempt to apply CU20 failed due to install asking for the "exchangeserver.msi" for the current build.  Exchange was setup by previous IT and only performed monthly Windows updates.  Unable to locate the .msi file and had to cancel the update.  However, it caused Exchange to stop functioning even after restore all services and reboot.  Last ditch effort to get Exchange back online, I restore Exchange from backup.  Now, OWA and EAC are up and running, but unable to send/ receive.  Outbound emails just stay in Outbox.  Verified Send/ receive connectors are correct.  

-   most importantly, how do I get mail flow back up and running?  

-   Once everything is working again, how can I patch it CU 20 without the missing "exchangeserver.msi"?  

Thanks in advance.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-05-06*

You can try to run the command from an elevated command prompt instead of a windows power shell. Also, in the command prompt, navigate to the network location of the Exchange 2016 installation files. You can take help from a similar thread -

https://social.technet.microsoft.com/Forums/exchange/en-US/f4d2f65c-d295-4b6a-a4fc-32101892e0ed/exchange-2013-sp-1-fails-msspeechsrtelecaesmsi?forum=exchangesvrdeploy.

Install with extracting the setup files to D:\Install\CU12, then ran the following command:  

.\setup /mode:upgrade /iacceptexchangeserverlicenseterms  

So copied the setup folder from the extracted folder: D:\Install\CU12 to C:\Program Files\Microsoft\Exchange Server\V15\bin** to make sure the setup folder with install files, then started the install again from the **D:\Install\CU12 folder, and then everything went fine and without a glitch.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-17*

Hi, for me this error came when trying to patch CU from PowerShell and not CommandPrompt. Once I did the command:  

setup /m:upgrade /IAcceptExchangeServerLicenseTerms  

from CMD (as admin) the error/warning went away.  

(this was patching from CU19 to CU21 Exchange 2016)  

Hope this helps, Sneaky_Pete

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-04-30*

Hi @Roget Luo  ,    

Now, OWA and EAC are up and running, but unable to send/ receive. Outbound emails just stay in Outbox.     

Do you mean both the internal and external mail flow don't work now? If this is the case, is there any NDR message when an external user sends a mail to your organization?    

By "restore Exchange from backup", do you mean you rebuilt the Exchange server from scratch?     

Please have a check and ensure the Exchange related services are up and running. Also its' suggested to have a look at the Event Viewer and see if any relevant errors are recorded out there.    

Regarding the missing "exchangeserver.msi" when you tried to upgrade to CU 20, would you please remove any personal information like domain name and then share the detailed error message so that we can help do further research on this?     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
