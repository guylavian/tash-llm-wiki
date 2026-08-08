---
title: "Set \"Search engine used in the address bar\" via GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1659566/set-search-engine-used-in-the-address-bar-via-gpo
question_id: 1659566
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-edge-edge-development", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Set "Search engine used in the address bar" via GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1659566/set-search-engine-used-in-the-address-bar-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello-

Can someone please tell me how to set "Search engine used in the address bar" via GPO, to something other than Bing?  I have found various answers across the web and none seems consistent or sufficient.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-30*

Hi @Bryce I  ,

For the "Search engine used in the address bar" setting, you need to configure the following policies to (forcibly) set it to other search engines:

-  Enable DefaultSearchProviderEnabled

-  Configure DefaultSearchProviderSearchURL. An example value if you want to use Google Search: `https://google.com/search?q={searchTerms}`

-  (Optional) Configure DefaultSearchProviderName to give it a display name.

Here's the result:
And any input in the address bar turns to the Google Search result as expected.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread. 

Best Regards,

Shijie Li
