---
title: "managed favorites in active dir. domain via gpo not updating loading"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2380087/managed-favorites-in-active-dir-domain-via-gpo-not
question_id: 2380087
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# managed favorites in active dir. domain via gpo not updating loading

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2380087/managed-favorites-in-active-dir-domain-via-gpo-not (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

months ago i activated the managed favorites gpo succsesfully as a computer policy in our domain. we use chromium edge.

the fav. folder appeard in edge as expected.

now i added some new bookmarks to the html file that uses the gpo, and nothing happend. nu update.

i made a new bookmark file, imported the newest admx files ecc. 

edge isn´t updating. alway shows the old favs.

when i disable the managed favorites option, favs are gone.

i saved a new html file to the share where gpo picks it, but no result.

when i look in the registry of the computer, (Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge) i see that the gpo´s are applied, path´s are correct with the new file.

there is also a path Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\MicrosoftEdge

where under internet settings\provisionedfavorites  i see the correct favs.

but in edge the fav folder is not visible.

i also tried to make a registry entry hidefirstrunexperience, cause i red this maybe prevent the favs being loaded.

but no result.

what is wrong?

tx for any help

kurt

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2021-05-07*

Hello qpix666,

I'm John an Independent Advisor and a Windows user like you. I'll be happy to assist you today.

I want to apologize that this is just a consumer forum. Due to the scope of your question, I recommend posting your query on Microsoft Site Q&A which is a technical community platform where most of the members were IT professionals that would greatly help you with the issue. They have IT experts there that can assist you better especially about Windows Servers, Active Directory and Group Policy configurations, etc.

Microsoft Site Q&A

https://docs.microsoft.com/en-us/answers/products/

Kind regards,

John DeV

Independent Advisor
