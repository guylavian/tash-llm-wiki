---
title: "Account operators group in Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/230754/account-operators-group-in-active-directory
question_id: 230754
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Account operators group in Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/230754/account-operators-group-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I need to create delegate administration access in Active Directory but i have some difficulties to find the best practise for this.  

I've read many posts where answers advised to let Account operators group empty but i never found any explanations about the reason.  

Can you explain me where is the risk with that group please ? Can someone escalade to admin account or privilege with this access ?  

Thanks !  

Sorry for my English ;)  

Damien

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2021-01-14*

Hi,     

The idea is to reduce number of the member of group with privilege and add only users who need this high privlege .Because when a account with high privilege compromised , it can make a huge damage.    

I invite you to read this article to get more details about group with high privileage in active directory:    

review-and-reduce-the-number-of-accounts-in-highly-privileged-administrative-groups    

----------    

Please don't forget to mark helpful reply as answer

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-01-14*

Some details here on groups.    

https://learn.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#active-directory-default-security-groups-by-operating-system-version    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-14*

Thank you Patrick.  

I've read this article before but I think I was more confused after reading it than before.  

In the article, Microsoft says in the second paragraph that "Members of the Account Operators group cannot manage the Administrator user account,... Server Operators," and in the purple note that "This group is considered a service administrator group because it can modify Server Operators".  

My english is certainly bad but manage and modify seems to be the same thing, right?  

During my tests, I couldn't be able to change anything in Server Operators group (membership, no Security tab, group scope) when I used my delegate account member of Account Operators.   

If it's the only reason, I have no clues to say it's dangerous in my situation...
