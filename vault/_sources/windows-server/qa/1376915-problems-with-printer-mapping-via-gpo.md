---
title: "Problems with printer mapping via GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1376915/problems-with-printer-mapping-via-gpo
question_id: 1376915
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Problems with printer mapping via GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1376915/problems-with-printer-mapping-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning all,

I have a question about an existing problem in our company.

Initial situation:

We distribute printer mapping via GPO.

We have created groups which we then assign to the GPOs as "target group addressing on element level".

I am in the same group as the user we are talking about.

Only difference is that we are in different OUs.

The GPO is linked at both OUs, so the printer should be mapped to both users without issue.

Result:

I get the GPO applied just like the user with the difference,

that I get the printer displayed and the user does not. How can this be?

I don't understand how this is technically possible, that one user gets the printer mapped and the other not, although both are in the same group and the GPO is linked to both OUs.

If someone could help me, I would be very grateful.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-28*

Hello Pierre Schapdick,  

Thank you for posting in Q&A forum.  

1.Based on the description above, I understand you configured printer GPO setting within User Configurations, am I right?  

2.What specific printer GPO setting did you configure?  

3.Based on this sentence “that I get the printer displayed and the user does not.”, Where did you see this difference?  

First  

Please check if the problematic user account can access the printer device.  

Second  

You can check the gpo apply result for the problematic user account.  

For checking User Configurations within gpresult, we can follow steps below.

1.Logon the machine using normal domain user account.

2.Create a folder named F1.

3.Open CMD (do not run as Administrator).

4.Type gpresult /h C:\F1\gpo.html and click Enter.

5.Open gpo.html and check printer gpo setting under "User Details".  

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

==========================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
