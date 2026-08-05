---
title: "ADFS 2.0: Can the outgoing claim be set to lowercase?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2648604/adfs-2-0-can-the-outgoing-claim-be-set-to-lowercas
question_id: 2648604
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 5
qa_tags: []
---
# ADFS 2.0: Can the outgoing claim be set to lowercase?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2648604/adfs-2-0-can-the-outgoing-claim-be-set-to-lowercas (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So I have a relying part trust set up to an external vendor's system. However they require all incoming claims to be in lowercase to authorize. Kind of strange, I know...

Anyway, is there a way to make sure that all outgoing claims are in lowercase characters? Basically I have it set up now to send the SAMAccountName from AD, but as is, the accounts are set up with the first letter in CAPS and the rest in lowercase. For instance
 "Smith-###". 

So far we've explored the following:

-  Simply changing the SAMAccountName in AD. It works but there is a snag. Doing this would cause issues with certificates generated that rely on that AD field (so it's out of the question at this point, too many certificates to fix, not enough bodies to
 help out).

-  Asking the vendor if they can put a data filter up to convert all incoming data to lowercase (using some type of "ToLower" function). They flat out said that this will not be accommodated.

So at this point I figured I may be able to use ADFS to simply convert before sending, but haven't found any documentation on how to do this. I'm 99% sure it cannot be done, but it doesn't hurt to ask right?

I appreciate any type of help with this! Let me know if additional information is required.

Thanks!

## Answers

_No answers on this thread._
