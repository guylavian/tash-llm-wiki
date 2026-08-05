---
title: "unable to delete old exchange SSL certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/108565/unable-to-delete-old-exchange-ssl-certificate
question_id: 108565
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# unable to delete old exchange SSL certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/108565/unable-to-delete-old-exchange-ssl-certificate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

I have imported and installed a new ssl certificate in our Exchange server and then ran  a HCM wizard and select a new certificate for the send connector. however when I tried to delete the previous certificate below error message has popped up. one thing is the previous certificate also vaild till 25/11/2020 and we have renewed early. but I think it won't be a problem with deleting a previous one since we already installed a new certificate. we have only one exchange server in our environment.    

appreciate any one can help here to resolve this.    

    

    

    

    

    

Thanks,    

Dilan

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-09-28*

@Dilan Nanayakkara       

Agree with AndyDavid. Since you have assigned the new certificate to POP, IMAP, IIS, SMTP services, and if you also have re-run HCW, the mail flow should work well with the new certificate. You can remove the old cert from Personal store, then try to delete the old certificate again.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
