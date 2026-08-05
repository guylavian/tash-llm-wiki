---
title: "PAC File GPO is not applied."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195184/pac-file-gpo-is-not-applied
question_id: 2195184
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 8
qa_tags: []
---
# PAC File GPO is not applied.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195184/pac-file-gpo-is-not-applied (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

i have created policy to push the proxy setting through PAC file to the clients using GPO. but some of users are doesn't does not apply this user policy(I can see policy in result /r but settings is not applied). If the same user login for the different endpoint that policy also does also  not apply(unable to see in the gpresult /r) instead old proxy policy is applied. PAC files is stored on IIS server in Same domain. Some users are applied the gpo policy without any issue.

have you guys' exposure to  this issue before or any troubleshooting suggestions.

Thank you,

Dinuka Darshana.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-06*

Hello DINUKADARSHANA,  

Thank you for posting in Microsoft Community forum.

1.Based on the description "Some users are applied the gpo policy without any issue.", did you put the working users and non-working users in the same OU?  

2.What user group policy setting about PAC file did you set?  

3.Have you set any security filtering or WMI filtering?  

For checking User Configurations within gpresult, we can follow steps below.

Logon the machine using normal domain user account (that apply the GPO setting).

Create a folder named F1.

Open CMD (do not run as Administrator).

Type gpresult /h C:\F1\gpo.html and click Enter.

Open gpo.html and check gpo setting under "User Details".

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
