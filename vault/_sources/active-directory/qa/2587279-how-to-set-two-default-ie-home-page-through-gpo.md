---
title: "How to set two default IE home page through GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2587279/how-to-set-two-default-ie-home-page-through-gpo
question_id: 2587279
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 6
qa_tags: []
---
# How to set two default IE home page through GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2587279/how-to-set-two-default-ie-home-page-through-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi 

I have a group policy for internet settings  created which has been working fine now on active directory installed on windows 2003.

I already have home page address  and now i want to add a second home page please advice if i can just add a semicolon and then add the second home page .

for example

www.google.com ; www.msn.com

is this the way to do it or there is another way ?

Thanking you in advance for your advice

Rabelani

## Answer (community) — community member

*upvotes: 0 · updated: 2013-08-21*

Hi, Rabelani,

What version of Windows and Internet Explorer are you using?

How to use Group policy to configure home page settings

http://www.grouppolicy.biz/2010/02/how-to-use-group-policy-to-configure-home-page-settings-part-1/

Multiple IE home page can be set using Group Policy Preferences under User Configuration > Preferences > Control Panel Settings > Internet Settings .... then create a new IE7 or IE8 Internet Setting and configure the home pages from there...  

OR  

If you are using IE8 you can also use the native group policy settings "Disable changing secondary home page settings" and "Disable changing home page settings" to configure a users home page.
