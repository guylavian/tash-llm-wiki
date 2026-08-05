---
title: "ADFS - OWA with Keycloak"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193283/adfs-owa-with-keycloak
question_id: 2193283
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 5
qa_tags: []
---
# ADFS - OWA with Keycloak

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193283/adfs-owa-with-keycloak (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,   

I have a problem related to OWA. I receive a SAML request from the keycloak, which is my IDP for ADFS. ADFS later sends a WS-Federation request to OWA. The page is redirected to the endpoint /owa/auth/errorfe.aspx?msg=WrongAudienceUriOrBadSigningCert. In the logs it shows me the following information: ID1044: An encrypted security token was received at the relying party which could not be decrypted. Configure the relying party with a suitable decryption certificate. Current relying party decryption certificate info: No Certificate Configured.

In the ADFS settings, in the certificates tab, I have certificates attached as Token-Decrypting and as Token-Signing. When receiving messages from Adfs, OWA displays in the logs the certificate with which this request was signed, cn=test.

In relying party trusts, as OWA I have encryption and signature certificate cn=test.

After using the command Get-ADFSCertificate all fields show the certificate cn=test.

Where could there be an error that OWA cannot load the certificate to decrypt the adfs message? Any commands that will help display the OWA certificate configuration?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-20*

Hello adfslos,    

thank you for posting on the Microsoft Community Forums.     

Based on the description, I understand that your issue is related to OWA.    

Since there are no engineers dedicated to OWA in this forum. In order to be able to deal with your questions quickly and efficiently, I recommend that you repost your questions in the Q&A forum, where there will be a dedicated engineer to provide you with a professional and effective response.    

Here is a link to the Q&A forum: https://learn.microsoft.com/en-us/answers/questions/   

 Have a nice day.    

Best regards,   

Lei
