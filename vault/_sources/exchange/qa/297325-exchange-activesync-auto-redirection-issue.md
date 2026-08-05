---
title: "Exchange ActiveSync auto redirection issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/297325/exchange-activesync-auto-redirection-issue
question_id: 297325
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Exchange ActiveSync auto redirection issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/297325/exchange-activesync-auto-redirection-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Tech Community,  

I recently setup Exchange Hybrid with on-premises Exchange 2013 with CU23 for a customer. Customer has on-premises Active Directory as abc.local and two primary SMTP domains as abc.com and xyz.com.  

Email flow, mailbox move and rest of the things look pretty good but for users having SMTP abc.com can't get their mobile app auto redirected to Office 365 URL..... meaning, as soon as we move users to office 365 their mobile devices stop receiving emails while users who are using xyz.com domain they are not facing this issue regardless of Android or iOS device. Please note, these mobile devices are on latest OS and using native app and Microsoft Outlook app.  

During troubleshooting, we found out that Exchange Target OWA URL which was setup by Hybrid Wizard is appearing as: http://oultook.office.com/xyz.com  

Please suggest, what could be the issue? Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-09*

@    

Thanks for the information you provided.    

According to my research on the test result with on-premises users. Please make sure that the account is already enabled inheritance. The picture below shows the enabled state. Are you providing complete test results? Is there any other error generation besides "FolderSync"?    

    

For the test results of Exchange online users, is this the result after reconfiguration? According to the result, the ActiveSync connection is successful.    

In addition, reconfiguration of the account is a routine operation. If the user's connection issue can be solved successfully, it is recommended that you use this method.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-04*

Hi @Muhammad Sheeraz Ansari   ,  

Are there any errors displayed?  

Except for mobile devices, is there any problem with the migrated mailboxes using OWA or the Outlook client on the computer to log in?  

1.Please reconfigure mailbox account on mobile device.

2.Confirm that ActiveSync is enabled for the user and the mobile device isn’t blocked by ActiveSync quarantine rule.

3.Test Exchange Online ActiveSync access externally by using Remote Connectivity Analyzer. If any error is displayed, please share with us. But please noted that covering your personal information.  

Please refer to: Remote Connectivity Analyzer

4.Please run the following commands in on-premises Exchange to ensure that the “remoteroutingaddress” of migrated mailbox is corresponds to "Domainnames" in the organizational relationship.

```
Get-Remotemailbox -Identity  | fl RemoteRoutingAddress  
Get-OrganizationRelationship | FL Identity, domainnames
```

For more information: Exchange ActiveSync device settings with Exchange hybrid deployments

For the value of Exchange Target OWA URL, I checked the domain name configured by default with the same name as the local AD in the lab environment. But as long as your xyz.com domain has been verified in Office 365, I think this will not affect the use of mobile device.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
