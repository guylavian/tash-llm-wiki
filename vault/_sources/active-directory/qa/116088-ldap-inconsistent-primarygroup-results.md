---
title: "LDAP Inconsistent PrimaryGroup results"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/116088/ldap-inconsistent-primarygroup-results
question_id: 116088
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee", "MicrosoftVendor"]
---
# LDAP Inconsistent PrimaryGroup results

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/116088/ldap-inconsistent-primarygroup-results (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have a Microsoft 2019 AD Server that gives inconsistent results when queried for all groups that a specific user is member of.  

The query is as follows:  

(&(objectClass=group)(member:1.2.840.113556.1.4.1941:=CN=user1,CN=Users,DC=our_domain,DC=our_domain_suffix))  

Now I am aware that primary groups should not be part of the result, but the behavior we get is that when the user is a member of "Domain Users" (the primary group) and some more groups, the result of the query is ALL those groups AND the Domain Users group (unexpected), but when the only group of the user is Domain Users the result is empty (as expected).  

Can somebody explain this please?  

Thanks!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-10-27*

Hello @EA  ，

Thank you for your update. And I am sorry for the late reply.

I did a test in my lab. And I can reproduce the problem as you mentioned.

1.I have three users (u5,u6 and u7).  

-   Here is memberof for three users one by one.  

    Primary group: Domain Users.  

    

Primary group: Domain Users.  

Primary group: Domain Users.  

3.Here is ldap search result for three users one by one.  

Primary group: Domain Users (there is no primary group of the result) (Expected).  

Primary group: Domain Users (there is no primary group of the result) (Expected).  

Primary group: Domain Users (there is no primary group of the result), but there is Domain Users of the search result, because in such case, non-primary group (group00) belongs to primary group (Domain Users) (Unexpected).  

In summary, if there is non-primary group belongs to primary group, the result will appear primary group. I suggest we can check if you have the same situation.

Hope the information above is helpful. If anything is unclear, please feel free to let us know.

Best Regards，  

Daisy Zhou

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-08*

Like you said, primary groups are not displayed for a user as it is a constructed group membership. Usually you can retrieve the same by modifying the search filter to include the well known identifier 513 for domain users group. However your issue will require extensive investigation and would request you to open a support ticket at https://support.microsoft.com/en-in/supportforbusiness/ for detailed analysis.
