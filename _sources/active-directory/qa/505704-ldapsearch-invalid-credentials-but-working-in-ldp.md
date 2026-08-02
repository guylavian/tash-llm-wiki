---
title: "ldapsearch invalid credentials but working in ldp.exe"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/505704/ldapsearch-invalid-credentials-but-working-in-ldp
question_id: 505704
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# ldapsearch invalid credentials but working in ldp.exe

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/505704/ldapsearch-invalid-credentials-but-working-in-ldp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have this weird behavior connecting to our DC via ldap. The source is a linux machine and we ran ldapsearch to test ldap connectivity. The account we use always says invalid credentials(49). Now, I know you will say check the password or the binddn if correct. We tested this account using ldp.exe from another windows machine and this account was able to successfully bind. The weird thing is we tested a borrowed account from a different project and we ran ldapsearch from the linux machine using that borrowed account and was successful. We also created test accounts but still the test accounts wont work using ldapsearch command.  

Now we also test the account to another project and run ldapsearch still the account says invalid credentials.

## Answers

_No answers on this thread._
