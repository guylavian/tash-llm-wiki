---
title: "Replace adfs certificate error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/394122/replace-adfs-certificate-error
question_id: 394122
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Replace adfs certificate error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/394122/replace-adfs-certificate-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I use the command to modify the adfs certificate    

Set-AdfsAlternateTlsClientBinding -Thumbprint “”    

But there is an error as shown below    

I only have one ADFS server    

    

Then I ran this command as a local administrator    

The error has changed    

    

But my certificate is a wildcard certificate    

 *.contoso.com    

I read the following official documents，Recommend me to run the following command    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/ad-fs-support-for-alternate-hostname-binding-for-certificate-authentication    

Set-AdfsAlternateTlsClientBinding -Member ADFS1.contoso.com -Thumbprint '<thumbprint of cert>'    

But I see this command is no different from the command I ran, except that a member is specified    

And this command also returned the same error    

    

I just want to replace an adfs https certificate    

This certificate is no different from the first one, it is a wildcard certificate, *.contoso.com    

I don't understand where is the problem that I can't replace the certificate

## Answers

_No answers on this thread._
