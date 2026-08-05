---
title: "Active Directory Best Practices"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/491651/active-directory-best-practices
question_id: 491651
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Active Directory Best Practices

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/491651/active-directory-best-practices (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My question is perhaps more philosophical than technical, but I'm hoping for informed opinions and understand there is no definitive or "best" answer.  

A coworker and I disagree on AD (security) groups. I believe they should be a reflection of the organization: i.e. the "Sales" group should contain only people in the Sales department, and not contain folks from Finance that need to see some Sales data.  

He says the opposite: Finance folks should be in the Sales group so they can get some reports or emails.  

My motivation is that I develop software for our company, including our intranet. I routinely create dashboards and reports for people and departments. What I want is to say "give me all the members of the Service group" and get a list of all our service technicians, service managers, and such. He says that instead I should be looking at AD job titles, asking for all users that have an array of titles to reflect who works in the Service department (since we currently have Finance and Execs in the AD "Service" group).  

I'm trying hard to see the validity of his point, but no matter what I consider, using groups in such the way he proposes is an anti-pattern. But that's not conducive to constructive conversation. I'm hoping some outside opinions my help me understand his position better.  

How do you, as an IT professional think AD groups should be laid out and maintained (besides the well-accepted guidelines for OUs, nesting, and such)?  

Thanks in advance for helping me avoid my own narrow-mindedness.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-07-27*

You can review microsoft's documentation here.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/best-practices-for-securing-active-directory    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-28*

Just checking if there's any progress or updates?  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-28*

Hello @Sean Hogge  ,    

Thank you for posting here.    

It is very grateful for yannara's suggestions and sharing. I am so glad that the information provided by yannara is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
