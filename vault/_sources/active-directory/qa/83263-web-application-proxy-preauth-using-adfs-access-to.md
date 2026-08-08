---
title: "Web Application Proxy - Preauth using ADFS, access to ADFS has to be public?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/83263/web-application-proxy-preauth-using-adfs-access-to
question_id: 83263
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Web Application Proxy - Preauth using ADFS, access to ADFS has to be public?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/83263/web-application-proxy-preauth-using-adfs-access-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to use WAP for public internet access to a intranet application.    

The intranet application uses ADFS SAML for SSO and authentication.    

Referring to this article https://learn.microsoft.com/en-us/windows-server/remote/remote-access/web-application-proxy/publishing-applications-using-ad-fs-preauthentication    

In the general flow, step 2:    

<quote>    

Web Application Proxy redirects the HTTPS request to the AD FS server with URL encoded parameters, including the resource URL and the appRealm (a relying party identifier).    

The user authenticates using the authentication method required by the AD FS server; for example, user name and password, two-factor authentication with a one-time password, and so on.    

</quote>    

In my testing, wap application external url is https://myapp1.example.com/, with configured WAP to use ADFS preauthentication.    

When i try to access https://myapp1.example.com/, i will get redirected to https://myadfs.localdomain.local/ for authentication.    

Does the ADFS server need to be publicly accessible?    

Do i need to enable ADFS proxy using a WAP passthrough? as shared in http://www.mistercloudtech.com/2015/11/25/how-to-install-and-configure-web-application-proxy-for-adfs/    

Shouldn't WAP internally help to resolve and response the content of https://myadfs.localdomain.local/ at the external url of https://myapp1.example.com/, like how other reverse proxy works?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-09-01*

The ADFS farm is also published through the WAP . The WAP is also an ADFS Proxy. If you want to use WAP with external client, the FQDN of your farm needs a public name. It requires a split-brain DNS (aka split-horizon). The name of your ADFS farm needs to be resolved to the public IP of your WAP for external clients, and the same name has to point to the local IP of your ADFS for internal clients.
