---
title: "Will Active Directory work for me?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1194013/will-active-directory-work-for-me
question_id: 1194013
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Will Active Directory work for me?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1194013/will-active-directory-work-for-me (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am an IT technician and I am trying to gather some information on whether Active Directory works for my situation. I have about 50 potential users that are on our network. I am wanting to have a directory service that allows for a user to log on to any computer and have their account accessible with all their permissions, programs, etc regardless of computer on the network. I want it to also be able to use 2FA/MFA for more secure access to accounts. I have also seen where some systems can create custom images of Windows to supply their users with so that it has only the required software on it. Is all this possible with Active Directory?

## Answer (community) — Q&A User [Mvp]

*upvotes: 1 · updated: 2023-03-28*

Hi

quick addition to Dave's answer - the only thing Active Directory won't do natively is MFA/2FA, you'll need a 3rd party product such as DUO to achieve this.

Thanks

Michael

-  If the reply was helpful please upvote and/or accept as answer as this helps others in the community with similar questions. Thanks!

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2023-03-28*

Yes, it's possible. As to the software it sounds like you would better be served with a Remote Desktop services (terminal server) that has the software installed that's shared with the users.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-29*

What you really need based on your situation is a small-scale Active Directory environment, along with Windows Deployment services, which would allow you to create custom Windows images that contain only the required software. You can also set up something like System Center, though that might be too large for only 50 users, which can then allow users to pick from the Software Center from a list of organization approved software; I have that set up like that at work. Other ways of doing this...you can set up software on the network via Group Policy and MSIs, which will then allow users to select the option to install a program from the network, so that you didn't have users with software they didn't need for their particular tasks.Hope this gives you a bit more background.
