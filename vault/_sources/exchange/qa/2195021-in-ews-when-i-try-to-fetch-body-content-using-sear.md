---
title: "In EWS,When I try to fetch body content using SearchFilter::ContainsSubstring this filter, I am unable to get the all mails with that content"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195021/in-ews-when-i-try-to-fetch-body-content-using-sear
question_id: 2195021
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# In EWS,When I try to fetch body content using SearchFilter::ContainsSubstring this filter, I am unable to get the all mails with that content

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195021/in-ews-when-i-try-to-fetch-body-content-using-sear (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

For example, I need to fetch the mails which contains the words "keep for con", ews does not return the mail which has "arkeep for con".

though "arkeep for convea" sentence contains my filter word "keep for convea", having that "ar" in the prefix restrict ews to fetch that mail. Is this a default behaviour ?  

Someone please help.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-25*

Hi Sakthikumaran,

Thank you for posting in the Microsoft Community Forum.

The behavior you're experiencing with the Exchange Web Services (EWS) when using the `SearchFilter::ContainsSubstring` filter is likely due to how substring matching works with this filter. 

The `ContainsSubstring` filter looks for occurrences of the specified substring within the target field. However, it doesn't perform a "word boundary" check, meaning it will match any substring that contains the specified text, regardless of whether it's part of a larger word or not. 

In your example, when you search for the substring "keep for con", it will match any string that contains those characters in that order, regardless of what comes before or after it. So, "arkeep for convea" matches because it contains "keep for con" as a substring. 

If you want to ensure that only whole words are matched, you might need to implement additional logic to filter the results after retrieving them from EWS. This could involve checking each matched string to see if it's part of a larger word or not. 

Alternatively, if your EWS implementation supports more advanced search capabilities, you may look into using regular expressions (if supported) or other more sophisticated search filters to achieve the desired behavior.

Best regards

Neuvi Jiang
