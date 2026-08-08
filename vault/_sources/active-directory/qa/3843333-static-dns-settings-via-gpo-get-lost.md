---
title: "Static DNS settings via GPO get lost!!!!"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3843333/static-dns-settings-via-gpo-get-lost
question_id: 3843333
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Static DNS settings via GPO get lost!!!!

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3843333/static-dns-settings-via-gpo-get-lost (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I need your help with the following issue:

I want to have static DNS settings for my home remote users using group policy. My plan is this:

I created a ps1 script with the Set-DnsClientServerAddress or netsh interface ip set dns command for the ethernet and Wi-Fi Interface of the clients.  I put the script on a group policy

The user connects to his home network, gets dynamic IP Address and DNS address from his home router and gets access to Internet

Then he logins to the company VPN and the group policy is applied (after 120 minutes max)

The DNS settings of the clients network adapters change according to the script settings

OK so far.....

Now the problem:

When I disconnect from the VPN the static DNS settings disappear. The network adapters  DNS settings revert backup to auto!

 This is not what I need!!! I want the static DNS settings to stay permanently.

Why is this happening? Is there something I can do? 

Kind regards

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2022-03-09*

Hello Charilaos,

Good day! I'm John Dev a Windows user like you and I'll be happy to assist you today.

I want to apologize that this is just a consumer forum. Due to the scope of your question, I recommend posting your query on Microsoft Site Q&A which is a technical community platform where most of the members were IT professionals that would greatly help you with the issue. They have IT experts there that can assist you better especially about Windows Servers, Active Directory and Group Policy configurations, etc.

Microsoft Site Q&A

https://docs.microsoft.com/en-us/answers/topics...

windows-dhcp-dns

https://docs.microsoft.com/en-us/answers/topics...

Kind regards,

John DeV

Independent Advisor
