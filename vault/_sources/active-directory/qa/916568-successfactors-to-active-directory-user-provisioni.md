---
title: "SuccessFactors to Active Directory user provisioning service, wrong employment profile synced to AD"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/916568/successfactors-to-active-directory-user-provisioni
question_id: 916568
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# SuccessFactors to Active Directory user provisioning service, wrong employment profile synced to AD

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/916568/successfactors-to-active-directory-user-provisioni (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

When using SAP SuccessFactors to Active Directory User Provisioning model, for some users who has concurrent employments, we get the wrong profile synced to ActiveDirectory (not primary employment).     

For example, if we have a user who had concurrent employment and now he or she has only one job in SuccessFactors, we get all the data related to inactive employment of this user from SF to AD.     

At first, we were scoping users using personIdExternal.     

After reading this article we changed the scope and used userId. But nether or less there is no difference. We still get the wrong employment data and for terminated employments, the user in AD is also terminated.     

When I use the API and query the user, I got the correct profile. Is it a bug?    

```
https://{{endpoint}}/odata/v2/EmpJob/?$filter=userId eq '10451'&$format=json&$expand=departmentNav
```

Do you have any tips on how to scope users with primary active employment?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-18*

We had the same problem for concurrent employments and we have managed to find a solution to get the information from the main employment, details below:

1- Use personIdExternal as Key for User provisioning integration, this will provide to AD the payload including all (two or more) employment records linked to that person. 

2- You can find out whether an employment is main or secondary using field isPrimaryAssignment from the User entity. To get to this field, considering the standard integration uses PerPerson entity to start the query, you need to navigate PerPerson/employmentNav/userNav/isPrimaryAssignment.

3- In AD user Provisioning integration, where source fields are configured, for SuccessFactors Employment related fields to be mapped to AD, you need to add the following JSONPath to get the right information for Department, for example:

$.employmentNav..results[?(@.userNav.isPrimaryAssignment == true)]..jobInfoNav..results[?(@.emplStatusNav.externalCode == 'A' || @.emplStatusNav.externalCode == 'U' || @.emplStatusNav.externalCode == 'P')].departmentNav.externalCode

With this expression, you will receive the external code of the department assigned in the main active employment.

I hope this helps.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-15*

I have raised a service request and Afees helped me by suggesting the full-service restart as described in the article Restart synchronizationJob    

with the following criteria:    

{    

   "criteria" : { "resetScope" : "Full" }     

}    

It seems that this solved the issue.
