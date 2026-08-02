---
title: "PowerShell - Connecting to ExchangeOnline - Can no longer add/enable Remote Routing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2282243/powershell-connecting-to-exchangeonline-can-no-lon
question_id: 2282243
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# PowerShell - Connecting to ExchangeOnline - Can no longer add/enable Remote Routing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2282243/powershell-connecting-to-exchangeonline-can-no-lon (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

First time posting,

Last year I could use the following command on an account without issues (we are a hybrid migration of O365):

Enable-RemoteMailbox TEST -RemoteRoutingAddress ******@OurDomain.mail.onmicrosoft.com -PrimarySmtpAddress ******@OurDomain.org

nor can I even try to set the remote routing with this command:

set-remotemailbox -identity ******@OurDomain.org -RemoteRoutingAddress ******@OurDomain.mail.onmicrosoft.com

Now I cant, I get some error about it not knowing the command or some other rubbish.

For obvious reasons I need to have those remote routing addresses added to the account, which is a lot easier than having to get into the Admin Center and type them in one by one.

I know all about the initial set up (not that I have received a new computer or anything, its the same Windows Laptop), as I still haev all of that documented. With the initial set up being:

install-module exchangeonlinemanagement

install-module msonline

install-module azuread

Not that I needed the azuread part, as this the accounts were going to be cloud only accounts via an Import into O365 and then a license assignment that included EOL.

When I open up PowerShell as Admin, and run the command "connect-exchangeonline" I get the box for username, password and the authenticator app passcode, and it signs me in without issue, so I am connected to ExchangeOnline.

So, any ideas why this suddenly doesn't work?

Ive tried using the built in Terminal, powershell 7, and one older version of PS and still get the same error.

Any ideas how I can set the remote routing added to an account once connected to ExchangeOnline

because Im bloody lost as to why this no longer works, even though I obviously get authenticated on connection to it.

Any help is appreciated,

JH

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-06-10*

Seeing as there are no other posts, and this might get lost on the reply comment on the previous reply, I did wonder about that, so I opened some ports, RDP'd to it, and opened Exchange Management Shell, made sure it had the modules, and yet got the same error, about some command or other not found.. bear in mind these are copied form the very text file I used in the past..... btu also know I used to be able to run those commands on my laptop.. directly from my laptop without issue, I didnt have to be on our exchange server. But I did try again, same error, closed the ports and back to square one....

not being a fan of PowerShell - I thought I left programming 40 years ago.... That was enough for me, not you say they are depreciated and I need to use Graph SDK for PowerShell, or the Entra PowerShell module.... No idea about Graph..... name rebranding? no idea at all what that means..... not ever had to use Entra anything - other than once.. hence that part in the first post.... why is MS making this so damn impossible..... "give me the commands I need, let them run any time I need to run them, and stop removing, updating them with zero communication to us.. the users"..

Sorry Im on a rant, but I need that remote routing done, otherwise Im doing them one by damn one and that really.. and I mean really pisses me off.. Any other thoughts or suggestions? because your suggestion doesnt work either - sorry....

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-06-09*

The cmdlets you are referring to should be run against your on-premises Exchange server, not Exchange Online. Therefore, make sure you have a remote PowerShell session to your on-premises infrastructure established, if you are not leveraging the EMS directly.

On a side note, both the MSOnline and AzureAD modules are now deprecated. If you need to run any cmdlets against Entra ID, use the Graph SDK for PowerShell, or the Entra PowerShell module.
