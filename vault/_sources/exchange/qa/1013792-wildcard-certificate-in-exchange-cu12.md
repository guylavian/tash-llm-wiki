---
title: "Wildcard certificate in Exchange CU12"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1013792/wildcard-certificate-in-exchange-cu12
question_id: 1013792
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Wildcard certificate in Exchange CU12

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1013792/wildcard-certificate-in-exchange-cu12 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

As you already may know MS has removed the possibility to create/renew certificates in GUI ( ECP certificate request has been deprecated in Exchange 2019 CU12 and higher and in Exchange 2016 CU23 and higher. ) Instead the EPS should be used and there's the example (in the article posted above) for creating a wildcard certificate request (along with the "ordinary" SAN certificate and the single-name certificate) that I followed and got the following results:

1) create a wildcard certificate:

Wildcard certificate request  

These examples create certificate request files for wildcard certificates with the following properties:

SubjectName: .contoso.com in the United States, which requires the value C=US,CN=.contoso.com.  

RequestFile: \FileServer01\Data\Contoso Wildcard Cert.<cer or pfx>  

FriendlyName: Contoso.com Wildcard Cert

$txtrequest = New-ExchangeCertificate -PrivateKeyExportable $True -GenerateRequest -FriendlyName "Contoso.com Wildcard Cert" -SubjectName "C=US,CN=*.contoso.com"  

[System.IO.File]::WriteAllBytes('\FileServer01\Data\Contoso Wildcard Cert.req', [System.Text.Encoding]::Unicode.GetBytes($txtrequest))

-  I just used contoso.net instead of contoso.com:

2) Since I already have in my network the configured Windows-based CA I had no issues requesting the wildcard certificate and importing it into Exchange 2019 CU12:  

  

3)  

No single issue - so far so good... but when I tried to access https://mail.contoso.net I got this:  

-  Edge displays ~the same error (~"Certificate's common name is wrong" - can't publish a picture as it had stopped throwing it after proceeding as not secure).

4) I then created and imported the "ordinary" SAN certificate - again, according to the article above - and it worked out perfectly:

Q1: Is it a bug (either in Exchange or in the documentation) or CU12 can't work with wildcard certificates (I had not any issues with them up to CU11, even using the same CA)?

Q2: What was the purpose of removing this functionality from GUI (I know that's a rhetorical question but...) ???

Thank you in advance,  

Michael

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-19*

hm, if they changed the EPS-command then why they didn't allow the GUI to work if all GUI-like menus, commands, etc are all eventually go to the relative EMS commands??? Sounds strange to me :(    

Anyway, as far as I understand there should not be any difference between gui in PS...in theory...

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-19*

P.S. And yes, there were no issues with wildcard certificate in the same domain with CU11!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-19*

Yea, but now it uses the " FileData" paramater to export and import. I assume its more secure and/or they discovered some exploit of the previous way it was handled.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-19*

"Thats interesting, because I would think Exchange is not the issue here but the browser are the ones saying its bad." - I thought about it and tested it in the two different browsers... if it is still the browsers to blame then...it's rather strange that the two different browsers displays ~the same error...    

"To prevent misuse of UNC paths by attackers, we are removing parameters that take UNC paths as inputs from the Exchange Server PowerShell cmdlets"  - mmm... maybe I don't understand anything but the examples above show    

Wildcard certificate request    

These examples create certificate request files for wildcard certificates with the following properties:    

SubjectName: .contoso.com in the United States, which requires the value C=US,CN=.contoso.com.    

RequestFile: \FileServer01\Data\Contoso Wildcard Cert.<cer or pfx>    

FriendlyName: Contoso.com Wildcard Cert    

Isn't the \FileServer01\Data\Contoso Wildcard Cert path not the UNC path???

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-19*

Thats interesting, because I would think Exchange is not the issue here but the browser are the ones saying its bad.    

Are you saying the wildcard worked before CU12?    

For the other question, it was a security thing to remove the ability to use a UNC path:    

https://support.microsoft.com/en-us/topic/changes-in-exchange-server-powershell-cmdlets-and-exchange-admin-center-for-unc-path-inputs-kb5014278-36af1640-4389-4ff1-b805-d1d63715a0dd
