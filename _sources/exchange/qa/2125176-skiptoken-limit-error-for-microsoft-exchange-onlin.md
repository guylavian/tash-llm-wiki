---
title: "$skiptoken limit error for Microsoft Exchange online Reporting web service API"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2125176/skiptoken-limit-error-for-microsoft-exchange-onlin
question_id: 2125176
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-development", "office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# $skiptoken limit error for Microsoft Exchange online Reporting web service API

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2125176/skiptoken-limit-error-for-microsoft-exchange-onlin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I was working on integrating MessageTrace report API as a part of my SIEM integration:  

`https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MessageTrace[?ODATA options]`  

I have noticed that, whenever my $skiptoken reaches the limit `999999 ` , it throws the following error with 500 status code:  

`{`` ``"odata.error": {`` ``"code": "UnknownError",`` ``"message": {`` ``"lang": "",`` ``"value": "An error has occurred on the server."`` ``}`` ``}`` ``}`  

Is there any limitations on $skiptoken value from the API itself? It was working fine for the `999998` value. If $skiptoken value `999999 `exists, for example,   

`"odata.nextLink": "../../reportingwebservice/reporting.svc/MessageTrace?$filter=StartDate%20eq%20DateTime'2024-12-02T00%3A00%3A00Z'%20and%20EndDate%20eq%20DateTime'2024-12-02T23%3A59%3A59Z'&$skiptoken=999999"`  

 how can we request the data from next set of events?

Can someone let me know, is there any max limit from API side or the $skiptoken?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-03*

Hi @Swarada Jalukar

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, you have encountered the problem of 500 errors when $skiptoken reaches the limit, and you want to know if there is any maximum limit on the API side or $skiptoken.

First of all, regarding API limits, Microsoft Graph API (including Message Tracking API) has specific rate limits. Usually, it is limited to a maximum of 60 requests per minute and a maximum of 1,000 requests per hour. These limits may vary depending on the request type and the specific API endpoint used.

Regarding $skiptoken, it is usually used for paginated query results. Depending on different APIs and services, the maximum limit of $skiptoken may vary, depending on the implementation of the API.

If you have any questions, please feel free to contact me. If the answer is helpful, please click "Accept Answer" because it can help other members of the Microsoft Q&A community who have encountered similar problems and are looking for solutions. Thank you.

Best,

Jeanne
