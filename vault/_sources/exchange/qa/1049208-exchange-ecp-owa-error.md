---
title: "Exchange ECP/OWA error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1049208/exchange-ecp-owa-error
question_id: 1049208
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange ECP/OWA error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1049208/exchange-ecp-owa-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Recently renewed SSL Certificate on Exchange 2019     

Everything seem to work OK but iPhones not connecting or Android    

If I rest user password - I can setup account on Andiod but Manually    

Auto discover not working    

So I rekeys the SSL and Added the services and activated the new SSL    

Checked ECP/OWA - worked OK    

Deleted the  Old SSL    

Android / iOS still won't connect    

Now when I try to connect to ecp or owa  - I receive an error    

PR_CONNECT_RESET_ERROR - no webpage displayed!    

HELP!!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-17*

Hi @Chris Stephens  ,    

Please verify that the IIS site bindings on Exchange Back End and Default Website have the correct certificates. Finally, reset IIS.    

Therefore, in addition to checking the Exchange back end that ManuPhilip says, it is also recommended that you check the Default Web site.    

Click on Default Web Site. Select Bindings. Go through and edit all the types https with port 443.    

Select the third-party certificate. Click OK.    

From an administrator command prompt, run IISReset.    

For renewing Exchange certificates and checking IIS site bindings, please refer to the following articles:    

renew-microsoft-exchange-certificate    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-15*

Have you checked if the 'Exchange Backend' has a correct certificate assigned in IIS console?    

    

Similarly, check other bindings also and see the certificate assignments are fine there too    

Reset IIS after fixing those assignments and try again    

----------    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
