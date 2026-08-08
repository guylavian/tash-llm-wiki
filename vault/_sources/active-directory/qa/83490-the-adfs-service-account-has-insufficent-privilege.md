---
title: "The ADFS service account has insufficent privileges to create the Account Activity database."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/83490/the-adfs-service-account-has-insufficent-privilege
question_id: 83490
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# The ADFS service account has insufficent privileges to create the Account Activity database.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/83490/the-adfs-service-account-has-insufficent-privilege (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I keep getting the error "The ADFS service account has insufficent privileges to create the Account Activity database." when running the ADFS Diagnostic.  It's the only error I get, everything else passes.  I have run the script that is supposed to resolve the problem but it does not (Update-AdfsArtifactDatabasePermission -Credential $cred).  It runs without error, but I keep getting the error in diagnostic.  I then went into management studio and tried to give my service account permission to everything related to that Adfs Artifact Database but the error continues.  Anybody have any ideas - I'm stuck.

## Answers

_No answers on this thread._
