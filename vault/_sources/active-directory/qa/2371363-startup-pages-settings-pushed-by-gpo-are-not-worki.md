---
title: "Startup pages settings pushed by GPO are not working?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2371363/startup-pages-settings-pushed-by-gpo-are-not-worki
question_id: 2371363
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 8
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Startup pages settings pushed by GPO are not working?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2371363/startup-pages-settings-pushed-by-gpo-are-not-worki (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am having trouble with the startup page policy pushed by the GPO.

88.0.705.68 (Official build) (64-bit) with latest ADMX  

In computer policy:

Microsoft Edge - Default Settings (users can override)

enable and set 'Site to open when the browser starts' & 'Action to take on startup' is set to 'Open a list of URLs'

And I know the policies are applied by checking under Edge://policy

Both settings are set to Recommended level and the Status shows 'OK' but the browser still opens up a new blank tab instead of specified addresses.

If I configure the same thing under the regular 'Microsoft Edge - Default Settings' where users cannot override, the browser does load specified websites but this time, users are not allowed to change the homepage settings which I do not want to enforce.

Anyone had the same problem or have any insights to fix this problem?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2021-02-11*

Hello jlee1FX,

I'm John an Independent Advisor and a Microsoft user like you. I'll be happy to assist you today.

I want to apologize that this is just a consumer forum. Due to the scope of your question, I recommend posting your query on our sister forum Microsoft Site Q&A which is a technical community platform where most of the members were IT professionals that would greatly help you with the issue. They have IT experts there that can assist you better especially about Windows Servers, Active Directory and Group Policy configurations, etc.

Microsoft Site Q&A

https://docs.microsoft.com/en-us/answers/products/

Sincerely,

John DeV

Independent Advisor
