---
title: "Question on LDAPS server certificate selection and openssl"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194815/question-on-ldaps-server-certificate-selection-and
question_id: 2194815
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Question on LDAPS server certificate selection and openssl

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194815/question-on-ldaps-server-certificate-selection-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 2 Root Certificate Authorities setup in my domain. 

Previously LDAPS was using a sever certificate from RootCA1. 

Suddenly LDAPS is using a server certificate from RootCA2. 

How does the LDAPS server certificate selection work?  Why all of a sudden would  it start using a server certificate from RootCA2. 

I want to make sure it continues to use the server certificate from RootCA2 and not switch back to RootCA1. 

Also does anyone know how to map the server certificate output from openssl to an actual server certificate? I have exported all the certificates.  In my personal store and opened them with notepad and none of them actually match my server certificate. Im trying to understand which server certficate LDAPs is using on RootCA2.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-08*

I managed to delete the certificate.  I needed to delete the certificate template to stop the certificate from reappearing.  The certificate template was set to Auto Enroll on the Security tab.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-08*

Hi Erik,

Thank you so much for your response.

If I delete the older certificate it keeps reappearing with a new date.  I connected to each Domain Controller and deleted it from the Personal folder but it reappears.

How do I permanently delete the older certificate?  What would be causing it to reappear?
