---
title: "Issues After migration from Office365 to Exchange 2019 Servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1179089/issues-after-migration-from-office365-to-exchange
question_id: 1179089
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Issues After migration from Office365 to Exchange 2019 Servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1179089/issues-after-migration-from-office365-to-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have very Serious Problem in my company that after we have successfully migrated all mailboxes from on cloud to on premises Exchange Server 2019 all users have suffering they can view the address book and mail tip can not been seen in any new mail in the top said can view any mail tip right now check later and also the calendar is not sharing the free/busy of any users even if they have meeting at the same time and i check calendar and sharing permissions all times from outlook side and server side didn't work and also the automatic reply also not working, Please find the screen shots,

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-10*

Hi @ahmed saad  ,

For further troubleshooting, I would like to confirm the following with you:

1.Did you recreate a new profile after you migrated?

2.Can you configure OOF and view busy/free messages in OWA?

If this issue still occurs in the new profile, please refer to the steps in this link to get the URL of OOF or OAB: Enable and collect logs for profile creation issues - Outlook | Microsoft Learn

Then visit these URLs through browser to see if them can be accessed successfully. If the page doesn't appear, go to your internal DNS server and add the record to point to the internal IP address.

Please refer to this link for detailed steps: SOLVED: "Your automatic reply settings cannot be displayed because the server is currently unavailable. Try again later" (microsoft.com)

Kindy note:Microsoft provides third-party contact information to help you find additional information about this topic. This contact information may change without notice. Microsoft does not guarantee the accuracy of third-party contact information.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
