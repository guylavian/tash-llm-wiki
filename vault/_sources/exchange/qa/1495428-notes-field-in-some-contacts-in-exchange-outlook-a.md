---
title: "Notes field in some Contacts in Exchange - Outlook - ActiveSync lost most text in a few random cases"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1495428/notes-field-in-some-contacts-in-exchange-outlook-a
question_id: 1495428
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Notes field in some Contacts in Exchange - Outlook - ActiveSync lost most text in a few random cases

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1495428/notes-field-in-some-contacts-in-exchange-outlook-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A few months ago I migrated our Exchange to a new provider with a good and long-standing reputation. No issues so far -- except one.  

I recently noticed that in the Notes field for a certain Contact, most of the lengthy text that was in there has disappeared, leaving only the beginning of the text.  

It was gone from the local Windows 10 Outlook client, from the default Contacts app on the Samsung S22 Ultra Android phone using ActiveSync (and gone from the Outlook > Apps > Contacts module on the phone), and gone from OWA.  

I asked the Exchange hosting provider for advice and they couldn't think of a cause or solution, or a way to recover past copies.  

A few days ago, I noticed the same thing had occurred with another Contact I went into. This one had less text to start with and retained more text than the first case, and again it kept text at the beginning of the Notes field and lost all the rest (as if truncating it).  

Now I'm concerned. I have no idea how many more contacts this has occurred with, nor what to do to prevent it (let alone how to recover lost information).  

I've begun doing frequent exports from Outlook of my Contacts but that's not exactly a fix if there's something that's continuing to cause data deleation.  

There are no third-party apps on the phone or on any other phone, tablet, or laptop associated with this Exchange account. I'm only using Outlook and telling it to Sync Contacts with the device's Contacts app. And FWIW I'm 99% sure that at least in the second instance, if not both, I did not edit and save the Contact on the phone (but maybe I did -- not that that should account for this kind of data loss or truncating, but I suppose it might if I did in fact save the Contact on the phone).  

One thought I had is that the data may have been lost when the new Exchange host copied all the data from the mailbox from the previous Exchange host. I failed to create a PST export or pay the previous hosting company to make a backup for me before the migration. I was under severe pressure with the business and with the deadline before EOL with the previous Exchange host. All mailbox sizes (I moved six) seemed to indicate it went smoothly -- all were within about 10% or less of the size of the original mailbox. However, I'm 99% sure I recall having gone into one of those two Contacts and seen the entire Notes contents after the migration. I'm not positive, though. (The new Exchange host is trying to recover from a recent backup of theirs, which I think is only two weeks old.)  

Any suggestions would be greatly appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-15*

Thanks but frankly none of this helps me.
There are no filters or rules at play, and the data limit clearly is not the issue since plenty of text was and is in these and many other Notes fields in Contacts with no issues, and it randomly truncated in just a few and didn't leave even close to equal amounts.
As I said in the OP it's lost everywhere. Opening Outlook in Safe Mode would be useless.
While I understand the common troubleshooting step of a new profile in Outlook, that's not likely to be a factor when I have five devices syncing to this Exchange account and it's lost at all locations and lost in OWA. I'd have to reset all of them and the Exchange hosting company is the most well established in the business and their Tier 2 tech support supervisor agrees a new profile probably won't help.
Thank you for the effort in attempting to help, though.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-15*

Hello,

Welcome to our forum！

Based on the information you provided, it is recommended that you check if any rules or filters in Outlook are automatically deleting or truncating the Notes field. Additionally, please note that there is a limit to the amount of data that can be stored in the 'Notes' section of an Outlook contact. If the limit is exceeded, the excess data may be truncated or lost. Please check whether the notes of the two contacts in question are too long and exceed the limit.

Besides, have you tried opening Outlook in safe mode (WIN+R and type 'outlook.exe /safe') to see what happens? Also, we recommend creating a new profile and checking again.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.
