---
title: "MSExchange ActiveSync 1100"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2120631/msexchange-activesync-1100
question_id: 2120631
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# MSExchange ActiveSync 1100

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2120631/msexchange-activesync-1100 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello. About once a month I see this error:

Exchange ActiveSync device requests for your users are being blocked. This problem frequently occurs when the HTTP OPTIONS method request isn't allowed by the firewall. Please check the firewall that filters requests in front of your Client Access server and the Microsoft-Server-ActiveSync virtual directory.

What can it be related to ?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-20*

Hi, @Андрей Михалевский

 

Thank you for posting your question in the Microsoft Q&A forum.

 

According to your description, you are encountering an error message that blocks the user's Exchange ActiveSync device request. You can try the following steps to see if they can resolve the issue:

-  Follow the error prompts to check the firewall that filters the request in front of the Client Access server and the Microsoft-Server-ActiveSync virtual directory to see if HTTP OPTIONS method requests are allowed.

-  Try assigning the Exchange Server group to modify the user object permissions to inherit permissions from the object's parent.

-  Open Active Directory Users and Computers, go to View > Advanced Features, find the user object and double-click to view the properties.

-  Go to Security > Advanced, enable Include inheritable permissions from the parent of this object, and select OK twice.

-  Is your Exchange Server updated with the latest security updates? If not, you can try updating and then connecting.

Refer to: https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/troubleshoot-activesync-with-exchange-server#determine-impact

If you have any questions, please feel free to contact me. If the answer is helpful, please click "Accept Answer" because it can help other members of the Microsoft Q&A community who have encountered similar problems and are looking for solutions. Thank you.

 

Best,

Jeanne
