---
title: "Exchange ActiveSync (EAS) Base64 decoding issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2626800/exchange-activesync-eas-base64-decoding-issue
question_id: 2626800
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Exchange ActiveSync (EAS) Base64 decoding issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2626800/exchange-activesync-eas-base64-decoding-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am having a problem decoding the URL parameters for my exchange active sync. According to the documentation the URL parameters are either plain text or encoded with base 64.
When I look at the Microsoft example

POST /Microsoft-Server-ActiveSync?jAAJBAp2MTQwRGV2aWNlAApTbWFydFBob25l HTTP/1.1
Content-Type: application/vnd.ms-sync.wbxml
User-Agent: ASOM
Host: Contoso.com
Content-Length: 866

and i decode the URL parameters jAAJBAp2MTQwRGV2aWNlAApTbWFydFBob25l I get  v140Device SmartPhone

But in my system when i connect using either a windows phone or Windows Mail client I get the following

POST /Microsoft-Server-ActiveSync?jQMJCBBgMOo4NRIhymNelU6Z7jHTBDzZUJwLV2luZG93c01haWwHAQE= HTTP/1.1
Content-Type: application/vnd.ms-sync
User-Agent: WindowsMail/17.4.9600.16384
Host: *************
Content-Length: 4893

When I decode the URL parameters jQMJCBBgMOo4NRIhymNelU6Z7jHTBDzZUJwLV2luZG93c01haWwHAQE= i get 
`0ê85!Êc^Nî1Ó<ÙP WindowsMail

The example I took from the documentation found here https://www.google.co.uk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&ved=0CDgQFjAB&url=http%3A%2F%2Fdownload.microsoft.com%2Fdownload%2F5%2FD%2FD%2F5DD33FDF-91F5-496D-9884-0A0B0EE698BB%2F%5BMS-ASHTTP%5D.pdf&ei=\_0HMUr\_lOYe27QbyhYAg&usg=AFQjCNEPrHG-eKRggHHzwdGMYEwq40DI3A&sig2=cfu2LP2tjaJAjgimY\_lQ7w&bvm=bv.58187178,d.ZGU

I can't figure out why. Any help is appreciated as this is driving me mad.

## Answer (community) — community member

*upvotes: 0 · updated: 2014-01-07*

HI,

Your question is better suited for the TechNet forum.  These are IT Pros who will be better able to assist you in solving the problem.  Repost there.

http://technet.microsoft.com/en-us/exchange/fp179701.aspx
