---
title: "Exchange 2016 OWA legacy logoff mode"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/210669/exchange-2016-owa-legacy-logoff-mode
question_id: 210669
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 OWA legacy logoff mode

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/210669/exchange-2016-owa-legacy-logoff-mode (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have been using the unofficial fix from INFSC to enable the legacy logoff mode.  The fix no longer works in our environment with CU18 and CU19.   Anyone tried it with CU18 or CU19?  thanks  

THE FIX :  

Edit Exchange\V15\ClientAccess\Owa\prem\15.1.1034.26\scripts\microsoft.owa.core.models.js  

Add this line  

$(document).ready(function(){ $('._ho2_2').click(function () { $('body > div:last-child ._abs_c div[role=menu] > div > div:last-child > button').on('click', function () { window.location.href= './logoff.owa' }) })  });  

Save & iisreset*  

Original thread:  htps://social.technet.microsoft.com/Forums/en-US/71462d67-f05b-4d74-af63-b22f3dea35d7/exchange-2016-logoff-does-not-generate-logoff-request?forum=Exch2016GD#889ee5b4-16d7-442b-8926-aaee43e757b1

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-28*

We use a F5 to pre-authenticate HTTPS request to Exchange, so cannot use Exchange FBA.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-28*

Does the workround that changing authentication to form based authentification work for you?    

https://social.technet.microsoft.com/Forums/ie/en-US/1314ed16-48e3-4813-96c7-a5465a83c61d/owaecp-signout-does-not-logoff-user-or-closes-session?forum=exchangesvrclients    

https://www.franken.pro/blog/outlook-web-access-sign-out-broken-after-exchange-2016-cu-4-and-basic-401-authentication    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
