---
title: "adfs saml multiple relying party trusts applications logout problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/405394/adfs-saml-multiple-relying-party-trusts-applicatio
question_id: 405394
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# adfs saml multiple relying party trusts applications logout problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/405394/adfs-saml-multiple-relying-party-trusts-applicatio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have saml on ADFS. Everything works fine but I have more then one relying party trust. Then when I log in to my one webapp (relying party trust) and log out everything is fine.  

But when I log in to first web app and then to second one I can se that on adfs I have cookie: samleSession that combines two sessions and then when I logout from first web app I'm redirected to logout page on second web app and cookies from web site one are not deleted.  

Also on ad fs site I can see that there is samllogout cookie. From that moment it is impossible to logoiut from any app.  

What am I doing wrong?

## Answers

_No answers on this thread._
