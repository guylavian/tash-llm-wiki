---
title: "Make exchange online signature device id dependent?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1164443/make-exchange-online-signature-device-id-dependent
question_id: 1164443
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# Make exchange online signature device id dependent?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1164443/make-exchange-online-signature-device-id-dependent (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So I wrote an exchange signature in html/css, refered to azuread informations to autofill, put the dependecies on the sender and everything works perfectly.

e.g.: 

Name  %%username%%

Phone %%phonenumber%%

Email  %%email%%

Now we do have a few colleagues which will send from only on email adress (i.e.: Mr. Miller, Mr. Stevens. Mrs. Rabbit, Mrs. Smith will all send from ******@test.com) and everyone needs their personal informations in the signature.

But since the dependency is set on sender (******@test.com) it won't recognize who of those actually send the email.

My question: Is there a "simple" way to make the signature device ID dependent? 

I do know it can be handled via IP-adress dependency, but we use dhcp protocoll, since we're completely online (Office 365, AzureAD, ExchangeOnline) and most of the users will switch between either in the home office or connected via VPN or via mobile data.

Second option is to manually (or via logonscript) save the signature with azuread references as a block locally, but since the whole block is formated in html/css, it's hard to code that (at least for me).

Best regards

## Answers

_No answers on this thread._
