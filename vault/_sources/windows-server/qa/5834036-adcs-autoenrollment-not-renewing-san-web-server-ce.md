---
title: "ADCS Autoenrollment Not Renewing SAN Web Server Certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5834036/adcs-autoenrollment-not-renewing-san-web-server-ce
question_id: 5834036
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
answer_author_roles: ["Independent Advisor"]
---
# ADCS Autoenrollment Not Renewing SAN Web Server Certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5834036/adcs-autoenrollment-not-renewing-san-web-server-ce (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Creating a thread and asking for help cause I didn't find any information due to the specificity of this setup.

Scenario

Testing auto-renewal of a Web Server (for HTTPS scenarios) certificate with SANs in ADCS, using the AutoEnrollment Capability:

Template uses “Supply in the request” (needed for SAN aliases, URLS)

Certificate issued via certlm.msc (Local Computer)

SAN entries are correctly applied

Certificate is valid and works

But the Auto-renewal, through AutoEnrollment GPO setup does not occur.

Template Configuration:

-  Based on duplicated builtin Web Server template

-  Validity: 1 week (Short like that so I can see the renewing happening for test).

-  Renewal: 4 days (Short like that so I can see the renewing happening for test).

-  Subject Name: Supply in request

-  EKU: Server Authentication

-  Permissions:  G-CERTRENEW-BRA (Group created to contain the Servers that will enroll and autoenroll, don`t wanna use Authenticated Computers): Read, Enroll, AutoEnroll

-  Template is published

GPO (Confirmed via RSOP)

Computer Configuration

-  → Public Key Policies

-  → Certificate Services Client – Auto-Enrollment

-  Enabled

-  Enroll + Renew enabled

-  Update templates enabled

Client Validation

-  Computer is in G-CERTRENEW-BRA

-  Membership confirmed via gpresult

-  Reboot performed after group assignment

-  Diagnostics Performed

-  certutil -pulse → no renewal triggered

-  certutil -store my:

-  Template extension present

-  Private key present

-  SAN present

-  No relevant autoenrollment events found

Working Comparison (Important)

-  A Kerberos Authentication template in the same environment:

-  Also uses Supply in request

-  Also uses SAN

-  Autoenrollment works and renews successfully

Autoenrollment does not renew the Web Server certificate, even though:

Template + permissions + GPO are correct

SAN is present and valid

Somewhat similar Kerberos template does renew successfully

Question

What conditions cause ADCS autoenrollment to ignore a valid certificate for renewal, specifically for:

Web Server templates

Using Supply in request (SAN)

Initially enrolled via certlm.msc

If needed, I can provide:

Full certutil -v -store my outputs

Template screenshots

CA configuration details

We can check specific events, but I didn`t find any info in Event Viewer in CertificateServicesClient-LifeCycle-System, it only says cert is about to expire, and then expired.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-03-23*

Hello,

The behavior you’re seeing is tied to how autoenrollment evaluates certificates against template rules. Autoenrollment will only renew a certificate if the subject name and key usage match the template exactly and if the certificate was originally enrolled through autoenrollment. When you issue a Web Server certificate manually via certlm.msc with “Supply in the request” for SANs, the certificate is valid, but autoenrollment does not consider it eligible for renewal because the subject information was supplied interactively rather than through the autoenrollment engine. That’s why your Kerberos Authentication template renews correctly — it is designed to be autoenrolled and the subject is handled consistently by the client.

For Web Server templates, the critical limitation is that autoenrollment does not re‑supply SANs on renewal. If the template requires “Supply in the request,” autoenrollment cannot generate the SAN list again without user input, so it silently skips renewal. This is by design in ADCS. Microsoft’s documentation notes that autoenrollment only renews certificates where the subject name is built automatically from AD attributes or is fixed in the template.

To make renewal work, you have two supported options. Either configure the template to build the subject name automatically (for example, using DNS name from AD or service principal name) so autoenrollment can regenerate it, or use a scripted enrollment process with certreq or PowerShell that re‑submits the SANs when the certificate is near expiry. In practice, many environments handle Web Server SAN certificates with manual enrollment or automation scripts rather than relying on autoenrollment, precisely because of this limitation.

So the condition that causes autoenrollment to ignore your Web Server certificate is the “Supply in the request” subject requirement. Autoenrollment cannot renew certificates that depend on user‑supplied SANs. If you need SANs and renewal without manual steps, you’ll need to redesign the template to use AD attributes for subject name, or implement a scheduled enrollment script to re‑issue the certificate before expiry.

I hope you've found something useful here. If it helps you get more insight into the issue, it's appreciated to accept the answer. Should you have more questions, feel free to leave a message. Have a nice day!

Domic Vo.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-03-23*

Autoenrollment skips renewal and instead triggers new enrollment whenever the template’s validity and renewal periods are configured with unsupported values. In that case, the existing certificate is not treated as renewable, so no renewal is attempted even though the certificate is valid and about to expire.

From the documented behavior:

-  Autoenrollment runs every 8 hours.

-  For a certificate to be renewed, both of these must be true:

-  At least 80% of the validity period has elapsed.

-  The certificate is within the renewal period.

-  For “normal” renewal behavior, the renewal period must be:

-  Greater than 8 hours, and

-  Less than 20% of the validity period.

-  If the validity/renewal combination is unsupported, autoenrollment:

-  Skips renewal, and

-  Triggers a new enrollment request instead of a renewal, which can change behavior (for example, requiring CA manager approval again, or simply not matching the existing cert as renewable).

In the scenario described (1‑week validity, 4‑day renewal):

-  Validity: 7 days

-  20% of validity: 1.4 days

-  Renewal period configured: 4 days (> 20% of validity)

This violates the “less than 20% of the validity period” rule, so the template’s validity/renewal configuration is unsupported for autoenrollment renewal. As a result, autoenrollment ignores the existing Web Server certificate for renewal and behaves as if a new enrollment is needed.

This explains why:

-  The Web Server certificate (short validity, long renewal window) does not renew via autoenrollment.

-  Another template (e.g., Kerberos Authentication) with different validity/renewal settings can renew successfully, even though it also uses “Supply in request” and SAN.

To make renewal work for the Web Server template via autoenrollment:

-  Adjust the template’s validity and renewal periods so that:

-  Renewal period > 8 hours, and

-  Renewal period < 20% of validity.

-  Confirm the effective values with:

-  `certutil -dstemplate <TemplateName>` and check:

-  `pKIExpirationPeriod` (validity)

-  `pKIOverlapPeriod` (renewal)

-  After changing the template, force autoenrollment on the client (`certutil -pulse`) and monitor again.

When configured within these constraints, autoenrollment will treat the existing Web Server certificate as renewable once 80% of its validity has elapsed and it is within the (now supported) renewal window.

References:

-  Approval required for certificate renewals when certificate autoenrollment configured

-  Error 0x80090022 NTE_SILENT_CONTEXT when CEP/CES autoenrollment using KBR fails on non-domain-joined clients
