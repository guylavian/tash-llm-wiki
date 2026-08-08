---
title: "ADFS SAML setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4191369/adfs-saml-setup
question_id: 4191369
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# ADFS SAML setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4191369/adfs-saml-setup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have questions regarding ADFS SAML configuration.

I have been charged with setting up ADFS SAML and connecting our system with clarity safetyzone.

I am using Using windows serv 2019 platform for the servers. I have created a test environment that has a domain controller, server with ADCS, and another server with ADFS.  I have a certificate created within the ADCS server and I installed ADFS on the
 respective server.  I verified after installation of the role and configuring an adfs administrator that the adfs administrator can sign into the  https://sts.contoso.com/adfs/ls/idpinitiatedsignon.aspx,  I created a windows test account and logged into the
 adfs server for testing purposes and when navigating to the https://sts.contoso.com/adfs/ls/ and attempting to sign in with that user, I get an error:

An error occurred

An error occurred. Contact your administrator for more information.

Error details

Activity ID: f68cc99a-b6e5-40dc-1a00-0080000000e5Error details: MSIS7065: There are no registered protocol handlers on path /adfs/ls/ to process the incoming request.Node name: 85253664-435b-4d04-8775-d4b96854cb12Error time: Mon, 02 Nov 2020 20:11:16 GMTCookie:
 enabledUser agent string: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36

I have everyone permitted for intranet access in the Access Control Policies.

Am i missing something?  Once i can verify that a standard user can login, then i can move on to the step of setting up the appropriate claims/trusts.

Does anyone have experience with this and maybe even experience with the Clarity Safety Zone platform?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2020-11-02*

Hi Joseph,

I'm Independent Advisor not Microsoft employee or support person. I have deep enough Windows knowledge and you may trust me. It's a pleasure for me to help others and I'll do all my best to help you.

You are talking about corporate environment. It is more effective to ask such questions at Q&A forum    https://docs.microsoft.com/en-us/answers/index.... 

It is oriented to admins and corporate users, and this forum - to home users so local experts may have no corresponding knowledge, sorry.
