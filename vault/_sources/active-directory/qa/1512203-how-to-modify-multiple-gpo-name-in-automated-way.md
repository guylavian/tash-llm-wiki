---
title: "How to modify multiple GPO name in automated way?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1512203/how-to-modify-multiple-gpo-name-in-automated-way
question_id: 1512203
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to modify multiple GPO name in automated way?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1512203/how-to-modify-multiple-gpo-name-in-automated-way (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,
Is there any way to modify the multiple GPOs name in automated way? 
Thanks!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-26*

Hello Khushi kumari,

Thank you for posting in Q&A forum.

Unfortunately, there is no way to automatically change the names of multiple GPOs at the same time.
However, I think there may be script to implement this function.

In my opinion, if the number of GPOs is not particularly large, it is recommended that you click on the Group Policy Object to manually change the Group Policy Name.

If you must want to try to use script to rename GPOs, you can try to write a script file according to your needs or search such a similar script on the Internet. And in the script you may need to specify the source GPO name and the target GPO name.

Thank you for your understanding. I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,
Daisy Zhou

If the Answer is helpful, please click "Accept Answer" and upvote it.
