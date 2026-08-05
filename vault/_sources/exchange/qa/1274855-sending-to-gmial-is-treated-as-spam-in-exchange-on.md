---
title: "Sending to Gmial is treated as spam in Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1274855/sending-to-gmial-is-treated-as-spam-in-exchange-on
question_id: 1274855
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Sending to Gmial is treated as spam in Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1274855/sending-to-gmial-is-treated-as-spam-in-exchange-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
I am currently using the Microsoft 365 service.

I have my own domain. When I send an email to Gmail, I receive an undeliverable email with the message "Rejected due to suspected spam".

Therefore, I set SPF / DKIM / DMARC, checked the normality, and tried again, but the result was the same.

Next, I did the ownership registration in Postmaster Tools on Google's side and it was successfully registered, but again the result was the same.

In addition, mail is returned as spam even if it is a simple mail such as "test" or plain text.

Error Code is 550.5.7.350, so I didn't get any useful information by looking it up.

Originally, I should have asked Google, but it will take more than two weeks to reply, so I posted it here.

If anyone has a similar case, I would appreciate it if you could teach me.

Thank you.
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-03*

Hi,

You wrote "after you've set up a valid reverse DNS record for your IP address".

But I cannot set up it. Because, I don't know the IP address of Exchange online.

And I cannot find any document about set up method of reverse DNS record of Exchange online.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-03*

Hi @ Adol，

If you can send emails to external recipients other than Gmail account, the problem is still in the Gmail  spam filter.

If you're still unable to send mail to gmail after you've set up a valid reverse DNS record for your IP address and set up SPF and DKIM records, I recommend waiting for Google's support to respond .

In addition, you can also refer to this article to see if it works：https://support.google.com/a/answer/81126?hl=zh-Hans

(Note: Microsoft provides third-party contact information to help you find additional information about this topic. This contact information may change without notice. Microsoft does not guarantee the accuracy of third-party contact information.)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
