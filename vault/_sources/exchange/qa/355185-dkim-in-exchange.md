---
title: "DKIM IN Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/355185/dkim-in-exchange
question_id: 355185
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# DKIM IN Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/355185/dkim-in-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I set up an exchange server and now my problem is that the dkim I defined is correct and I got a score of 10/10 in the email test, but when sending an email to Gmail or Outlook, the emails sent are sent to spam if When I look at the source of the message, both in Gmail and in outlook, dkim is shown as a pass.  

 Thanks for guiding me.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-14*

Hi @navid Talesh       

What's your Exchange server version?    

I agree with the reply above from alex, have you configured the SPF and DMARC record for your organization as well?    

Refer to the official document to leaarn about how SPF record works here: How Microsoft 365 uses Sender Policy Framework (SPF) to prevent spoofing    

In addition, we could also use the MXTOOLBOX to check the records configured for your domain: https://mxtoolbox.com/    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-14*

Hello dear Alex  

I am from https://www.mail-tester.com/  

I used it for testing and got a score of 10/10. I also used Exchange dkim signer software to create a dkim record.  

And inside the message source in Gmail, dkim is considered passed. But it puts the message in the spam.  

It should be noted that my internal domain name is different from my external domain name, and I used a policy in Exchange to specify that all emails be sent under my external domain name.  

Thank you very much Navid

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-13*

Hi Navid,  

have you already setup public TXT records for SPF and/or DMARC?  

If yes, please search for the message header "Authentication-Results" and check, if SPF, DKIM and DMARC passes.  

The DKIM Test you describe may just verify, if the DKIM signature in the message header for the domain your server is signing for is valid.  

It does not necessarily mean that the signing domain is the same of the sender: / from: header domain.  

By the way, which test did you utilize?  

Regards, Alex
