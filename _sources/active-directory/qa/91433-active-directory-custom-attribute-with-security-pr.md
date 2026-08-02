---
title: "Active Directory custom attribute with security principal editor"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/91433/active-directory-custom-attribute-with-security-pr
question_id: 91433
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory custom attribute with security principal editor

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/91433/active-directory-custom-attribute-with-security-pr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to create a custom attribute with security principal editor. I've created a custom attribute "TestA1" with the same type as "member" attribute but when I'm editing my custom attribute it has only multi-valued string editor.    

    

Any ideas how to do it?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-15*

Hello. Thank you for your research.  

It's sad. I hope we will be able to fix it in the future, because this option is the most valuable in active directory.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-09-11*

Hello @Splendidus  ,

Thank you for posting here.

Based on the description above, I did a test in my lab and I got the same result as you.

1.I Add a attribute (test1) with Syntax--Distingguished Name and multi-valued.  

2.Bind the attribute to group object.

3.We can see the attribute Syntax is the same as member attribute.  

4.The result below is the same as you.  

I am not sure whether we can get the display of custom attribute as the attribute "member". Maybe we can, I ma sorry I can not find a way to acheve the result currently.

It seems that for the attribute "member“, we can search the object of the specfic member in the domain.

However, for the most other attributes (single value and multi value), we need to type the value of these attributes.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
