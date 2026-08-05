---
title: "AD CS autoenrollment - what makes the client renew a still-valid, OID-matching cert when the template's major version never changes?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5927234/ad-cs-autoenrollment-what-makes-the-client-renew-a
question_id: 5927234
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
answer_author_roles: ["Independent Advisor"]
---
# AD CS autoenrollment - what makes the client renew a still-valid, OID-matching cert when the template's major version never changes?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5927234/ad-cs-autoenrollment-what-makes-the-client-renew-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Setup: Enterprise CA, version 2 certificate template, machine autoenrollment via GPO with "Update certificates that use certificate templates" enabled. The certificate is matched to the template by OID.

Behavior: A machine certificate is issued with about one year of validity. The client then renews it every one to two days. In the lifecycle log this is recorded as Action = Renew, with an Old-to-New thumbprint link, the same template OID, and a new key each time. Because it is a Renew with an Old-to-New link (not an Enroll), the client clearly found the existing valid certificate in the store and chose to supersede it. So this is the certificate update/renew path, not the "no satisfying certificate found" path.

What I have already ruled out

•	Expiry / renewal overlap - The superseded certificate still has nearly its full lifetime remaining at the moment it is renewed.

•	Template version - We never increment the major version. Template edits only ever change the minor revision, and in some renewal cycles the template was not changed at all. So a "template version is greater" comparison cannot be the trigger.

My question

After the client has matched an existing, time-valid certificate to the template by OID, what conditions in the update/renew path cause it to renew or supersede that certificate, other than (a) expiry/overlap and (b) a higher major version? In particular, are any of the following evaluated, and in what order of precedence:

•	A superseded-templates relationship (this template listed in another template's Superseded Templates list).

•	A renewal/overlap period configured greater than or equal to the validity period, which would leave the certificate permanently inside its renewal window.

•	The same template OID published on more than one issuing CA.

•	A per-property comparison such as CSP/KSP, minimum key size or algorithm, EKU / application policies, or subject/SAN built from Active Directory differing from the stored certificate on each pass.

The real blocker

Is there an ETW/WPP trace or debug switch that logs the specific condition the engine used to decide the certificate had to be renewed? Verbose autoenrollment logging (certutil -setreg Enroll\LogLevel 4) and the CAPI2 Operational log both record that a renewal happened, but not why. If there is a trace provider GUID I can capture with logman or tracelog, that is exactly what I need.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-06-22*

Hi, 

The behavior you are seeing is driven by a per-property comparison mismatch. When the autoenrollment task runs, it evaluates the machine's current Active Directory attributes against the extensions stamped on the local certificate. If your certificate template is configured to build the subject name from Active Directory, but the Certificate Authority drops or alters certain attributes during issuance due to security configurations or DNS discrepancies, the client detects this mismatch. The client assumes its current certificate is inaccurate and requests a renewal, but the Certificate Authority simply strips the attribute again, plunging the machine into a continuous renewal loop every time the policy refreshes.

The other theoretical triggers you mentioned do not fit the observed behavior. An overlapping renewal period where the window exceeds the validity period would trigger aggressive, immediate renewal requests upon every Group Policy background refresh, rather than a delayed one to two-day cycle. Furthermore, a superseded templates relationship or multiple issuing authorities would not natively cause this specific loop unless they enforce conflicting issuance policies, which ultimately leads right back to the property mismatch scenario.

To capture the engine's decision logic, you must move beyond standard event logging. The verbose autoenrollment logging you enabled via certutil modifies the HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography\AutoEnrollment registry key to increase the log level, but this and the CAPI2 operational logs only record the final outcome of an operation. They do not capture the internal evaluation math. You must utilize Event Tracing for Windows to capture the debug-level process as it happens. By running the built-in logman utility to trace the AutoEnrollment provider at GUID F0DB7EF8-B6F3-4005-9937-FEB77B9E1B43 and the CertEnroll provider at GUID 54164045-7C50-4905-963F-E5BC1EEF0CCA, you will expose the exact programmatic check forcing the renewal path during a machine policy update.

Domic
