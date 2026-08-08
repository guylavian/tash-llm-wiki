---
title: "Unable to download certificate chain from AD CS CertSrv (An unexpected error has occurred: The Certification Authority Service has not been started.)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1464183/unable-to-download-certificate-chain-from-ad-cs-ce
question_id: 1464183
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Unable to download certificate chain from AD CS CertSrv (An unexpected error has occurred: The Certification Authority Service has not been started.)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1464183/unable-to-download-certificate-chain-from-ad-cs-ce (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After having this issue and searching for weeks, I found my own solution.  I've not found this solution anywhere. I wanted to document it, so that other people didn't have the struggles that I did. 

I received the following error when selecting the  "Download a CA certificate, certificate chain, or CRL" link on my CA Web Enrollment server. "An unexpected error has occurred: The Certification Authority Service has not been started."

My CA Environment

1 - Offline Root (Certificate Authority)

1 - Intermediate CA (Certificate Authority, Certificate Authority Web Enrollment)

1 - Web Server (Certificate Authority Web Enrollment, Online Responder, Certificate Enrollment Policy Web Service-UsernamePassword, Certificate Enrollment Web Service-UsernamePassword)

For additional security and control I use a service account for IIS and do not use the Application user (pass-through authentication).  

I could select "Download a CA certificate, certificate chain, or CRL" from my Intermediate CA's (CertSrv) and it functioned perfectly.  However, if I select the same link hosted on my Web Server I would get "An unexpected error has occurred: The Certification Authority Service has not been started." The fact that it worked on my Intermediate CA server tells me that the service is started.  I found a bunch of articles making suggestions like adding it as a Trusted Site, underlying issues with delegation, don't use AD CS, etc.  None of which actually worked for me.  

The fact that my Intermediate CA server did not have the same issue that my web servers did, had me thinking it was a delegation issue.  I started by by changing from using a service account for IIS physical path credentials to using Application user (pass-through authentication) to determine if it was a service account delegation issue.  It was not.  I started playing with multiple IIS configurations and finally landed on my solution.  Once I changed the Physical Path Credentials Logon Type from Network to ClearText everything started working.   I tried Batch and Interactive as well with no luck.  I only made this change on my Web Server and not my intermediate CA server.  My intermediate CA is still using network.  I'm not sure why it functions differently on one vs the other. My best guess is that it has something to do with IIS being configured for CEP/CES UsernamePassword and not using Kerberos.  I don't like using Clear Text for credentials but since it is being used for accessing a local path I don't believe that it is passing credentials in clear text over the network.

## Answers

_No answers on this thread._
