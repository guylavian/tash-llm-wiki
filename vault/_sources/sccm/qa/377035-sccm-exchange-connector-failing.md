---
title: "SCCM Exchange Connector failing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/377035/sccm-exchange-connector-failing
question_id: 377035
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# SCCM Exchange Connector failing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/377035/sccm-exchange-connector-failing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our exchange connector in SCCM was working.  

it has now stopped  

looking at the sync logs from sccm we see the following  

INFO: Start to process Conditional Access https://exchange/powershell.	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:08 PM	6432 (0x1920)  

CA is not enabled	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:08 PM	6432 (0x1920)  

INFO: End to process Conditional Access https://exchange/powershell.	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:08 PM	6432 (0x1920)  

Conditional Access is waiting for file change notification or timeout after 5 minutes.	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:08 PM	6432 (0x1920)  

INFO: Start to process CA Consistancy Checker for https://exchange/powershell.	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:08 PM	12104 (0x2F48)  

Exchange Connector run Consistancy Checker on the CA devices	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:08 PM	12104 (0x2F48)  

ERROR: Decryption failed.	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:09 PM	12104 (0x2F48)  

ERROR: Failed to get password for account DOMAIN\SccmExcCon	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:09 PM	12104 (0x2F48)  

ERROR: Failed to call Initialize of managed COM. error = Unknown error 0x87D20001	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:09 PM	12104 (0x2F48)  

INFO: Raise Exchange Connector connection failure alert.	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:09 PM	12104 (0x2F48)  

ERROR: Failed to initialize managed com instance. Error = Unknown error 0x87D20001, -2016280575	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:09 PM	12104 (0x2F48)  

INFO: End to process for Consistancy Checker https://exchange/powershell.	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:09 PM	12104 (0x2F48)  

ERROR: Decryption failed.	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:09 PM	700 (0x02BC)  

ERROR: Failed to get password for account DOMAIN\SccmExcCon	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:09 PM	700 (0x02BC)  

ERROR: Failed to call Initialize of managed COM. error = Unknown error 0x87D20001	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:09 PM	700 (0x02BC)  

INFO: Raise Exchange Connector connection failure alert.	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:09 PM	700 (0x02BC)  

ERROR: Failed to initialize managed com instance. Error = Unknown error 0x87D20001, -2016280575	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:09 PM	700 (0x02BC)  

INFO: End to process wipe/policy https://exchange/powershell.	SMS_EXCHANGE_CONNECTOR	29/04/2021 1:56:09 PM	700 (0x02BC)  

Wait for inbox notification timed out.	SMS_EXCHANGE_CONNECTOR	29/04/2021 2:01:08 PM	6432 (0x1920)

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-30*

Side question: Really? Are you truly using ConfigMgr and ActiveSync to manage mobile devices instead of a robust MDM (like Intune)?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-30*

Hi @Anonymous  ,    

Could you check SMS_EXCHANGE_CONNECTOR component & look for status ID 1015?    

According to the description, it seems that there might be something wrong with Account, we could reset the account or change other account to check if the problem is fixed. The account can be the computer account of the site server or a Windows user account.    

Here is the article about installing and configuring the Exchange connector:    

https://learn.microsoft.com/en-us/mem/configmgr/mdm/deploy-use/install-configure-exchange-connector    

And we could re-configure it referring to the following screenshot:    

    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
