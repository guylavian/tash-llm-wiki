---
title: "problem with an application that uses ldap to authenticate on AD."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/95876/problem-with-an-application-that-uses-ldap-to-auth
question_id: 95876
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# problem with an application that uses ldap to authenticate on AD.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/95876/problem-with-an-application-that-uses-ldap-to-auth (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When one of the 3 domain controllers is no longer reachable, the application, through the round robin dns, tries to request authentication also from the unreachable domain controller, going into error. How can I fix?    

Thanks.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-09-16*

Hello @Gabriele Martufi  ,

Thank you for posting here.

Based on the description "tries to request authentication also from the unreachable domain controller, going into error.", do we mean the ldap authentication for the application fails at last?

If so, what error message do we receive?

Meanwhile, we can check:

1.Check whether your computer with an application is in the same site as the unreachable DC?  

2.Whether all the 3 domain controllers have been configured to uses ldap to authenticate this application. Or whether we only configure LDAP authentication for the application using this unreachable domain controller.  

3.If we only configure the other two domain controllers (assue the other two DCs are also DNS servers) as the DNS server of the computer with application, check whether the issue persists.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-15*

Is one domain controller more available than the others (on-site vs over slow-link, etc)? Does your application have ability to configure 2 ldap servers? Might be worth it to configure MyADSite.local and DC2.MyADSite.local if possible. Or, although not ideal, the most reliable DC as the LDAP server.
