---
title: "Windows Server 2016 Active Directory - Event 4768 - User unable to login"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/977332/windows-server-2016-active-directory-event-4768-us
question_id: 977332
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
---
# Windows Server 2016 Active Directory - Event 4768 - User unable to login

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/977332/windows-server-2016-active-directory-event-4768-us (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Using a powershell script, I made a gang of user accounts for some students. Their user logon names were too long for some of them following this format (firstname.lastname.XXXX) - you can see how this could be longer than 20 characters for some people with long names.    

This wasn't an issue at all for some years, as we never wanted them to log in to domain machines. We only needed them to have email addresses on our On-Prem Exchange Server (2016).    

However, we were recently directed to install GoGuardian on these machines as we had too many students and not enough Chromebooks. So I set everything up for that, but forgot about the long names.    

Today I got hit with a slurry of students that couldn't log in to the domain-joined computer labs, so starting with the first student, I renamed his user logon name to something under 20 characters.    

Each logon attempt is met with "the password or username is not correct". I've reset the password on the user twice for good measure, and carefully typed the username in.    

Event viewer on the DC shows Event 4768. I could not find any other Event ID's associated with this student's login, and I'm trying to figure out what is going on here.    

I've double-checked Group Policy to ensure I didn't accidentally apply a policy to prevent anything, but shorter named students are able to log in just fine and all users share the same OU. All computers are in the same OU as each other as well.    

I can login to OWA with the same credentials that won't work for domain login.

## Answer (community) — Volunteer Moderator

*upvotes: 1 · updated: 2022-08-23*

Hi,    

Just to clarify are you using UPN (user logon name) or samaccountname to login to the devices?     

The samaccountname has 20 character limit and you can check the details over here - a-samaccountname    

This samaccountname attribute must be 20 characters or less to support earlier clients, and cannot contain any of these characters:    

"/ \ [ ] : ; | = , + * ? < >    

Example :    

Contoso\Joebloggs    

or    

The newer User Principal Name format that is comprised of the User Logon Name (not the legacy sAMAccountName) and the UPN Suffix assigned to the specific user account.    

Example :    

JoeBloggs@Company portal   .local    

Also to confirm did you confirm the username and password does not have any special characters, try the account and password in the notepad just in case
