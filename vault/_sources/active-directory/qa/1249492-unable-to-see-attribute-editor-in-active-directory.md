---
title: "Unable to see attribute editor in active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1249492/unable-to-see-attribute-editor-in-active-directory
question_id: 1249492
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unable to see attribute editor in active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1249492/unable-to-see-attribute-editor-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey team,
I have  enabled the advanced features in ADUC view menu but I am unable to see the attribute editor on user properties.
Thank you for your help.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-20*

Hello Jennifer,
Thank you for posting in our Q&A forum.  

You can check if there is 11,{c7436f12-a27f-4cab-aaca-2bd27ed1b773} value for AdminPropertyPages under CN=configuration, DC=[your domain], DC=local, CN=DisplaySpecifiers, CN=your language ,CN=User-Display (for example US English is 409, so CN=409)  

If there is no value, you can add 11,{c7436f12-a27f-4cab-aaca-2bd27ed1b773} here.  

Similar thread for your references.  

https://community.spiceworks.com/topic/1996690-missing-attribute-editor-tab-in-aduc

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
If the Answer is helpful, please click "Accept Answer" and upvote it.
