---
title: "While receiving an ATTR35 error in Exchange, it cites the problem as being sent to the wrong O365 region.  However, a known KB doesn't state this."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1631796/while-receiving-an-attr35-error-in-exchange-it-cit
question_id: 1631796
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# While receiving an ATTR35 error in Exchange, it cites the problem as being sent to the wrong O365 region.  However, a known KB doesn't state this.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1631796/while-receiving-an-attr35-error-in-exchange-it-cit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Customer is attempting to configure SMTP settings in a third-party application, Sage 300, hosted outside of Microsoft Exchange Online and Azure, and receiving the following error:  451 4.4.62 Mail sent to the wrong Office 365 region, ATTR35.  As part of troubleshooting, we reviewed the KB article at - https://learn.microsoft.com/en-us/exchange/troubleshoot/email-delivery/wrong-office-365-region-exo.  However, nowhere in the KB article cited is there ANY mention about regions, geography, data sovereignty, etc. where "region" might actually play a part.

I am trying to confirm that despite the text of the error message, does the geo-location data for a given IP used in SMTP connections to Exchange Online play a part in receiving this error message?   The KB article makes no mention of verifying the region or location of an IP being used.   I'm seeking perspective to confirm that despite the words used in the error message, it doesn't 'really' have anything to do with the geo-location data for the IP.  If in fact it does, then from my perspective, the KB article should state this as well.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-04-25*

Hi @Bert Buri  

Please check your firewall regarding inbound and outbound rules using 25/TCP.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-26*

Hi @Bert Buri  

As stated in the document you mentioned, the error is due to the incorrect destination value for Microsoft 365 set in the MX record or smart host. So based on my understanding, the text "Mail sent to the wrong Office 365 region" makes sense to some degree, as it indicates that the mail was sent to a different region from where the recipient is located. 

However, agree with you on that the KB article could state it more clearly and I've tried submitting this via the Feedback button below the article. You can also do it from your end so that this feedback might be put in a higher priority.   

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
