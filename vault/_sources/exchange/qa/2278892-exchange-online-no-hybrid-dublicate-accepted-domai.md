---
title: "Exchange online, no Hybrid, dublicate accepted Domain with cnf record in name"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2278892/exchange-online-no-hybrid-dublicate-accepted-domai
question_id: 2278892
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange online, no Hybrid, dublicate accepted Domain with cnf record in name

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2278892/exchange-online-no-hybrid-dublicate-accepted-domai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hy everyone,

i have the problem that the domain.com CNF:xxxxxxxxxxx was created while adding my costumers domain to M365.

Then i could not set up a new User. Because it was possible to chose between 2 Domains with the same name and after an error because of the double domains.

so i deletet the origin domain.com

but it doesnt delete the cnf recordet one.

I tried with powershell... azure... exchange online.

not possible to delete the record on the accepteddomains

i created once more the record of the domain in m365.

now it was just the one with the cnf..... after the name.

Now it is not possible to log in in Outlook or other mail programs...

I think because the mail is ******@domain.com and not ******@domain.com CNF:xxxxxxxxxx

Any ideas what i can do?

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-05-27*

Hi @Vinc Sturzenegger  

Thank you for posting your question in the Microsoft Q&A forum.

What errors do you get when try to remove this CNF record from accepted domain?

Do you still have the domain "domain.com" in your tenant?

Here are some suggestions for you to give a try:

-  If this domain still exists in your tenant, please confirm that no users or groups use this domain and force to remove this domain from Microsoft Entra ID .   Remove-MsolDomain -DomainName "domain.com" -Force

-  Wait for some time and check if this domain is deleted or released successfully:   Get-MsolDomain | Where-Object { $_.DomainName -like "domain.com" } | FL Name, Status, Authentication

-  Then use the following command to get and remove accepted domain with CNF from Exchange Online:   Get-AcceptedDomain   Remove-AcceptedDomain "domain_name"

If issue still occurs when you delete the accepted domain, please provide the screenshot here and don't forget to cover your domain name and other personal information.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
