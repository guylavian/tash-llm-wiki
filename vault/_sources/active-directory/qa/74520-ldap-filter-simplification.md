---
title: "LDAP filter simplification"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/74520/ldap-filter-simplification
question_id: 74520
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# LDAP filter simplification

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/74520/ldap-filter-simplification (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I have the following filter to select users from multiple groups.  

As these groups all have the same parent OU path, is there any way I can simplify this filter to remove the need to remote the common parent path for each sub-group ?  

Thank you.  

(&(objectCategory=user)(|(memberOf=CN=TEST1_NAMED,OU=CONTAINER3,OU=CONTAINER2,OU=Groups,OU=myCompany,DC=myDomain)(memberOf=CN=TEST2_NAMED,OU=CONTAINER3,OU=CONTAINER2,OU=Groups,OU=myCompany,DC=myDomain)(memberOf=CN=TEST3_NAMED,OU=CONTAINER3,OU=CONTAINER2,OU=Groups,OU=myCompany,DC=myDomain)(memberOf=CN=TEST4_NAMED,OU=CONTAINER3,OU=CONTAINER2,OU=Groups,OU=myCompany,DC=myDomain)(memberOf=CN=TEST5_NAMED,OU=CONTAINER3,OU=CONTAINER2,OU=Groups,OU=myCompany,DC=myDomain)  

(memberOf=CN=TEST6_NAMED,OU=CONTAINER3,OU=CONTAINER2,OU=Groups,OU=myCompany,DC=myDomain)))

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-31*

Hi,  

   

Just want to confirm the current situations.  

   

Please feel free to let us know if you need further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-28*

Hi,  

   

Just want to confirm the current situations.  

   

Please feel free to let us know if you need further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-24*

Hi,  

Thank you for posting in our forum.  

According to my knowledge and understanding, you can use the script method to achieve  

I suggest that you can post on the powershell forum, they can give you more professional answers  

Hope this information can help you  

Best wishes  

Vicky
