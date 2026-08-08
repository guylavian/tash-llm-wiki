---
title: "How to increase EWS search-mailboxes results more than 100"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2109326/how-to-increase-ews-search-mailboxes-results-more
question_id: 2109326
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to increase EWS search-mailboxes results more than 100

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2109326/how-to-increase-ews-search-mailboxes-results-more (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I use EWS to perform searches on mailboxes. My account is at discovery management group. When I try to search mailboxes with filter "from:<sender> and subject:'<subject>' " with a mail scope of 500 mailboxes, I only get 100 result. I increased "DiscoveryMaxStatsSearchMailboxes" throttling policy 100 to 500. But still i only get 100 results.

Is there anyone faced and solved this problem?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-23*

Hello, @11348524,

Welcome to the Microsoft Q&A platform!

Based on your description, I understand that you have already adjusted the "DiscoveryMaxStatsSearchMailboxes" throttling policy, but you still failed to adjust the results limit from 100 to 500.

To solve this problem, please try to perform the following steps.

1.      Review EWS Limits: Make sure you are aware of all the limits imposed by EWS and adjust your application design accordingly. This includes understanding the default throttling policies and how they apply to your searches.

2.      Check Throttling Policies: Ensure that other relevant throttling policies are adjusted. For example, the "DiscoveryMaxMailboxes" and "DiscoveryMaxMailboxesResultsOnly" settings might also need to be increased.

3.      Adjust the Search Filter: Modify the search filter by adding a "$top" parameter to your filter query. This parameter specifies the number of items to return in the search results.

4.      Pagination: Implement pagination in your search queries. This involves breaking down the search into smaller chunks and iterating through the results. You can use the "Paging" property in EWS to handle this.

For more information about how to achieve these, you can click on EWS throttling in Exchange | Microsoft Learn for reference.

If the answer is helpful please click on ACCEPT ANSWER as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

Best Wishes,

Alex Zhang
