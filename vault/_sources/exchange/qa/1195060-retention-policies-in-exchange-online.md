---
title: "Retention policies in Exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1195060/retention-policies-in-exchange-online
question_id: 1195060
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Retention policies in Exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1195060/retention-policies-in-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

I have a question regarding Retention policy.

I can see there are 3 different tags under retention Tag.

1- For whole mailbox

2- For Default folders

3- For those folder which user has created manually.

If I will create all 3 tags with different names but when I will create a retention policy and add all 3 tags in the same policy. In that case what tag will be applied?

Second question is: Is it best practice to create this kind of tags and add them into same policy?

Regards

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-03-31*

Any folder-specific tags will be applied to the corresponding folder, all other folders will follow the Default tag retention settings. Personal tags (#3) can only be assigned manually, so none of them will apply even if you include them in the policy. For such tags, including in policy basically means "give the user the option to manually assign this tag".

For more details, refer to the official documentation: https://learn.microsoft.com/en-us/exchange/security-and-compliance/messaging-records-management/retention-tags-and-policies

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-04-05*

Hi @HASSAN BIN NASIR DAR  , 

For detailed explanations on the 3 types of retention tags, hopefully you can find the table below helpful:  

If I will create all 3 tags with different names but when I will create a retention policy and add all 3 tags in the same policy. In that case what tag will be applied?

As described in the table above, #1. DPT (Default policy tag) would be applied to all untagged items in the mailbox; #2. RPT (Retention policy tag) would be applied to default folders like Inbox, Deleted Items, etc. in the mailbox; #3. Personal tag would not be applied to any item unless the user manually assigns a personal tag to items or folders in the mailbox.

Second question is: Is it best practice to create this kind of tags and add them into same policy?

You can definitely create a retention policy with all the 3 types of retention tags as they don't conflict with each other.   

See Create a retention policy for Exchange Online.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
