---
title: "Cannot Replace Existing ADFS Communication Certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1253700/cannot-replace-existing-adfs-communication-certifi
question_id: 1253700
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Cannot Replace Existing ADFS Communication Certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1253700/cannot-replace-existing-adfs-communication-certifi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm currently trying to replace my soon to expire ADFS communication cert with the Powershell command
Set-Adfssslcertificate and using a thumbprint from a cert that's already been installed on the server.
However I keep getting this error.
The socket connection was aborted. This could be caused by an error processing your message or a receive timeout being exceeded by the remote host, or an underlying network resource issue. Local socket timeout was '00:01:00'.
I haven't been able to find anything helpful in event viewer. It just stops the service right after I run the command and I have to manually start it again.
I've tried this multiple times at different times so I don't think this is some one-off network error. The service has been working fine as well.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-04-24*

-  Ensure that the new certificate you're trying to install is valid, has a private key, and is in the correct certificate store on the server.

-  Make sure you're running the PowerShell command prompt with administrator privileges

-  Before attempting the certificate replacement again, restart the Active Directory Federation Services (AD FS) service on the server. You can do this using the Services management console or by running the following PowerShell command:

```
Restart-Service adfssrv
```

-  You can try increasing the timeout value by setting the execution time limit for the ADFS service. To do this, open the ADFS Management Console, expand "Services," click "Endpoints," and then modify the execution time limit for the relevant endpoints

-  Update ADFS configuration: If the issue persists, you can try updating the ADFS configuration

```
Set-AdfsSslCertificate -Thumbprint "your_certificate_thumbprint"
Update-AdfsSslCertificate
```
