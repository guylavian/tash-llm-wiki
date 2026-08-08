---
title: "How to fix EX:/O=HOSTING13/OU=EXCHANGE ADMINISTRATIVE GROUP (FYDIBOHF23SPDLT)/CN-RECIPIENTS/CN=52A0735C2FA94286B93039550B08FFA0 on Apple Mail"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2071235/how-to-fix-ex-o-hosting13-ou-exchange-administrati
question_id: 2071235
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to fix EX:/O=HOSTING13/OU=EXCHANGE ADMINISTRATIVE GROUP (FYDIBOHF23SPDLT)/CN-RECIPIENTS/CN=52A0735C2FA94286B93039550B08FFA0 on Apple Mail

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2071235/how-to-fix-ex-o-hosting13-ou-exchange-administrati (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When I am using Reply All on the Sent Items on my iOS running 17.6.1, beside my name shows a weird code EX:/O=HOSTING13/OU=EXCHANGE ADMINISTRATIVE GROUP (FYDIBOHF23SPDLT)/CN-RECIPIENTS/CN=52A0735C2FA94286B93039550B08FFA0.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-17*

Hi,@Shannyn Gem

Thanks for posting your question in the Microsoft Q&A forum.

It looks like you're seeing an Exchange Legacy Distinguished Name (DN) next to your name when using the Reply All feature on your iOS device.

If your From address is the same as the address the message was sent to, Outlook can properly identify your address and will not include it in a 'reply to all'.

When Outlook is confused, the possible causes include:

-  The Reply to address in File > Account Settings > More Settings is not the same as your account email address. When people reply to your address, Outlook sees that address as belonging to someone else.

-  Outlook is using the x500 address, not the SMTP address (Exchange mailboxes only)

-  You have one or more contacts in Outlook for your own GAL entry and one contains the wrong address. Outlook is resolving to the copy in your Contacts, not the GAL. (Exchange mailboxes only)

-  This problem often occurs with older versions of Outlook, are you using the latest version of Outlook?

It is recommended that you update Outlook and then re-add the user.

If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.
