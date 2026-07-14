# opencode session ses_0a81a3a81ffe5rvKj7VK4UQJzP — 2026-07-12 22:55
model: google/gemma-4-12b-qat

## USER
Answer this question from the wiki: **Our RHBK 26 cluster slowed to a crawl during a login storm last night. I know
RHBK caps its request queue at 1000 by default and sheds anything above that
with 503s, so the storm shouldn't have caused memory pressure — but the pods
OOMed anyway. What are we missing? **

Run the mechanized QUERY pipeline first — it routes, retrieves, graph-expands,
gates, and synthesizes in one shot (orchestrated through the LangGraph StateGraph
by default; degrades to the same nodes linearly when langgraph is absent):

- Preferred: call the `wikikb` MCP tool `ask` with the question (add `domain`
  and `tier` when known).
- CLI equivalent: `PYTHONPATH=_meta _meta/.venv-online/bin/python -m wikikb ask
  "Our RHBK 26 cluster slowed to a crawl during a login storm last night. I know
RHBK caps its request queue at 1000 by default and sheds anything above that
with 503s, so the storm shouldn't have caused memory pressure — but the pods
OOMed anyway. What are we missing? " --json` (plain `python3` also works — linear fallback; check the
  `orchestrator` field).

If the returned answer is thin or extractive, deepen it per "Operation: QUERY"
in `CLAUDE.md` (repo root = vault root): read `index.<domain>.md` + candidate
pages' `title:`/`summary:`, open page bodies only when needed, then grep the
in-vault raw tier (`reference/<domain>/` for corpus-backed domains,
`_sources/<domain>/` for notes-first ones).

Then **end the answer with the two-group References section (RH ground-truth +
Wiki/`web:`) mandated by "Operation: QUERY" in `CLAUDE.md`**, and file the answer
back as `questions/<slug>.md` (full frontmatter, `status: draft`, banner rules).

Never edit the immutable `reference/`, `_sources/`, or `references/`. Offline only.

## ASSISTANT-REASONING
The user is asking a specific question about Red Hat Build of Keycloak (RHBK) 26 behavior during a login storm.
The question describes a scenario where the request queue is capped at 1000, but pods still OOM (Out of Memory).
I need to use the `wikikb_ask` tool to find the answer.

Plan:
1. Call `wikikb_ask` with the provided question.
2. If the answer is thin, I will need to deep dive into the RHBK domain.
3. I'll identify the domain (RHBK / Keycloak).
4. I'll perform the "Operation: QUERY" steps: read index, summarize/read candidate pages, and grep the reference tier.
5. Synthesize the final answer.
6. File the answer as a new question page.

Let's start by calling `wikikb_ask`.

## TOOL wikikb_ask({"domain": "keycloak/RHBK", "question": "Our RHBK 26 cluster slowed to a crawl during a login storm last night. I know RHBK caps its request queue at 1000 by default and sheds anything above that with 503s, so the storm shouldn't have caused memory pressure \u2014 but the pods OOMed anyway. What are)
### OUTPUT
{"query": "Our RHBK 26 cluster slowed to a crawl during a login storm last night. I know RHBK caps its request queue at 1000 by default and sheds anything above that with 503s, so the storm shouldn't have caused memory pressure — but the pods OOMed anyway. What are we missing?", "orchestrator": "langgraph", "domain": "keycloak/RHBK", "confident": true, "thin": true, "banner": [], "guard": [], "answer": "[extractive fallback — no model answer (gateway returned no answer: http://127.0.0.1:11434)] top sources: (no candidates)\n\n## References (canonical)\n\n### RH ground-truth\n- No verified RH ground-truth source was cited.\n\n### Wiki\n- No synthesized Wiki page was used.", "cited": [], "grounding_fail": false, "ungrounded_identifiers": [], "grounding_basis": null, "withheld": false, "references": [], "reference_groups": {"rh_ground_truth": [], "wiki": []}, "session_tokens_served": 28869}

## TOOL wikikb_route({"q": "RHBK request queue OOM login storm"})
### OUTPUT
{"domains": ["keycloak", "active-directory", "openshift"], "confident": false, "session_tokens_served": 28888}

## TOOL wikikb_search({"domain": "keycloak/RHBK", "q": "request queue OOM memory pressure login storm"})
### OUTPUT


## TOOL wikikb_search({"domain": "keycloak", "q": "request queue OOM memory pressure login storm"})
### OUTPUT
[{"id": "rhbk-26-4-updates-for-26-4-10", "title": "Chapter 5. Updates for 26.4.10 - Red Hat build of Keycloak 26.4 Release Notes", "score": 15.318131410721913, "snippet": "…ger a Denial of Service (DoS) by sending a highly compressed SAMLRequest by the SAML Redirect Binding. The server fails to enforce size limits during DEFLATE decompression, leading to an OutOfMemoryError (OOM) and process termination. - CVE-2026-2603 A SAML Id…"}, {"id": "rhbk-26-2-concepts-threads", "title": "Chapter 5. Concepts for configuring thread pools - Red Hat build of Keycloak 26.2 High Availability Guide", "score": 4.567575480886051, "snippet": "…e without the client knowing if the request has been processed. To limit the number of queued requests in Red Hat build of Keycloak, set an additional Quarkus configuration option. Configure http-max-queued-requests to specify a maximum queue length to allow f…"}, {"id": "rhbk-26-2-concepts-memory-and-cpu-sizing", "title": "Chapter 6. Concepts for sizing CPU and memory resources - Red Hat build of Keycloak 26.2 High Availability Guide", "score": 4.165119039185487, "snippet": "…In containers, Keycloak allocates 70% of the memory limit for heap-based memory. It will also use approximately 300 MB of non-heap-based memory. To calculate the requested memory, use the calculation above. As memory limit, subtract the non-heap memory from t…"}, {"id": "rhbk-26-6-multi-cluster-introduction", "title": "Chapter 3. Multi-cluster deployments - Red Hat build of Keycloak 26.6 High Availability Guide", "score": 3.602830485614192, "snippet": "…ocates 70% of the memory limit for heap-based memory. It will also use approximately 300 MB of non-heap-based memory. To calculate the requested memory, use the calculation above. As memory limit, subtract the non-heap memory from the value above and divide th…"}, {"id": "rhbk-26-6-getting-started-scaling-and-tuning", "title": "Chapter 2. Scaling - Red Hat build of Keycloak 26.6 Getting Started Guide", "score": 3.55784598651681, "snippet": "…istent sessions or remote Data Grid and you experience memory issues, it is best to fully diagnose the problem and revisit the Concepts for sizing CPU and memory resources guide. Adjusting the memory request and limit is preferable to horizontal scaling. Consu…"}]

## TOOL wikikb_read_page({"slug": "rhbk-26-2-concepts-threads"})
### OUTPUT


## TOOL glob({"pattern": "index.keycloak*.md"})
### OUTPUT
/Users/guylavian/Downloads/skills/llm-wiki/index.keycloak.md

## TOOL read({"filePath": "/Users/guylavian/Downloads/skills/llm-wiki/index.keycloak.md"})
### OUTPUT
<path>/Users/guylavian/Downloads/skills/llm-wiki/index.keycloak.md</path>
<type>file</type>
<content>
1: # keycloak — routing index
2: 
3: _Generated by `python3 -m wikikb index` — do not hand-edit. The per-domain routing surface for the `keycloak` domain (titles + summaries) read during the tiered QUERY cheap pass; regenerate after ingest._
4: **236 pages.**
5: 
6: 
7: ## Topics (27)
8: - [[access-token-validation-resource-server]] — A resource server must cryptographically verify every inbound access token — signature, expiry, issuer, audience, and scope — before granting any access; skipping or weakening any of these checks is the most common single point of privilege-escalation in OAuth2 APIs.
9: - [[authentication-flows]] — An authentication flow is an ordered container of executions and sub-flows (screens, authenticators, actions) that runs during login, registration, reset-credentials and brokering; requirement types on each element decide whether and how it runs.
10: - [[bff-token-handler]] — A Backend-for-Frontend (BFF) acts as a confidential OAuth client that runs the Authorization Code + PKCE flow on behalf of a SPA, stores all tokens server-side, and exposes only encrypted HttpOnly session cookies to the browser — eliminating token theft via XSS as an attack vector.
11: - [[fine-grained-authorization]] — RHBK Authorization Services turn a confidential client into a centralized policy decision point: you register protected [[authorization-resources-scopes|resources and scopes]], attach reusable [[authorization-policy-types|policies]] via [[authorization-permissions|permissions]], and enforce decisions with a [[policy-enforcer|Policy Enforcement Point]] — going beyond plain role checks to combine ABAC, RBAC, UBAC, CBAC, and rule-based access control.
12: - [[ha-cross-site]] — Running RHBK across multiple clusters/sites for resilience, using external Infinispan / Red Hat Data Grid for cross-site session replication
13: - [[identity-brokering]] — RHBK acts as an identity broker — an intermediary that delegates authentication to external identity providers (social, OIDC, SAML) and then issues its own token to the client, so applications only ever integrate with RHBK.
14: - [[jwt-validation-pitfalls]] — A catalogue of the ways JWT validation goes wrong — algorithm confusion, skipped signature checks, header-injection, and cross-token misuse — so reviewers can predict the faults a broken implementation will produce.
15: - [[keycloak-overview]] — Keycloak (Red Hat build of Keycloak) is a standalone single sign-on server securing web apps and REST services over OIDC/OAuth2/SAML — apps redirect to it, never see credentials, and receive signed tokens. The spine page: core concepts (realm, client, tokens) plus the map to the domain's per-area topics.
16: - [[ldap-user-federation]] — How RHBK's built-in LDAP/AD provider (User Storage SPI) turns directory users into RHBK users — governed by storage/import mode and edit mode, with LDAP mappers for attributes/groups/roles and a truststore for LDAPS.
17: - [[observability-stack]] — RHBK exposes built-in health probes, Prometheus/OpenMetrics metrics, and OpenTelemetry traces (plus preview OTel logs/metrics), most of it served on the dedicated management port `9000`, so a single deployment feeds a centralized observability stack with no extra sidecars.
18: - [[oidc-client-best-practices]] — How to write app code that talks to RHBK/Keycloak so flow choice, client auth, token refresh, validation, logout, and session loss behave correctly — RHBK-grounded rules plus RFC 9700 upstream best practice.
19: - [[operator-advanced-config]] — The advanced knobs on the [[keycloak-cr]] beyond DB/hostname/TLS: trusted certificates, Pod customization, scheduling, secret references, resources, ingress, and admin bootstrapping
20: - [[operator-deployment]] — The end-to-end path for running RHBK on OpenShift: install the Operator via OLM, provision DB/hostname/TLS prerequisites, then declare a `Keycloak` custom resource that the Operator reconciles into a StatefulSet, Service, and (optionally) Ingress
21: - [[production-checklist]] — Going to production with `kc.sh start` means satisfying RHBK's secure-by-default requirements: TLS, an explicit hostname, a real database, a proxy/cluster topology, and observability kept internal.
22: - [[realm-administration]] — A realm is the isolated security domain in which Keycloak/RHBK manages users, applications, roles, and groups; one deployment hosts many realms, all isolated from one another.
23: - [[rhbk-ha-architectures]] — RHBK ships two documented HA shapes: a single OpenShift cluster (optionally spread across availability zones) using embedded Infinispan, and a two-site Active/Passive deployment using an external Red Hat Data Grid with synchronous replication. The guide prioritizes consistency over availability
24: - [[rhsso-to-rhbk-migration]] — Moving from legacy Red Hat Single Sign-On 7.6 to Red Hat Build of Keycloak (RHBK), the supported successor product — and, by the same machinery, upgrading between RHBK versions
25: - [[saml-clients-and-migration]] — How SAML service-provider apps integrate with RHBK as IdP, which SAML adapters survive the RH-SSO→RHBK move, and what changes — distinct from the OIDC story
26: - [[securing-apps-oidc-saml]] — RHBK is an OAuth2 / OpenID Connect / SAML 2.0 compliant server; you secure an application by registering it as a *client* in a realm and having it speak one of those protocols, ideally via the framework's native support rather than a Keycloak adapter
27: - [[security-hardening-checklist]] — Consolidated mitigations from the \"Mitigating security threats\" chapter — host validation, TLS, brute force, token leakage, redirect URIs, FAPI/OAuth 2.1, and session limits — for hardening an RHBK realm/deployment.
28: - [[server-config-migration]] — Mapping each RH-SSO 7.6 `standalone.xml` subsystem (datasource, TLS, cache, hostname, truststore, vault, JVM) to the equivalent RHBK `kc.

## USER
Our RHBK 26 cluster slowed to a crawl during a login storm last night. I know
RHBK caps its request queue at 1000 by default and sheds anything above that
with 503s, so the storm shouldn't have caused memory pressure — but the pods
OOMed anyway. What are we missing? 

## ASSISTANT-REASONING
The user is asking about a specific scenario in Red Hat Build of Keycloak (RHBK) 26 where pods OOMed (Out Of Memory) during a login storm, despite a request queue cap of 1000. I need to find the reason for this behavior in the wiki/corpus.

Plan:
1. Use `wikikb_ask` to get the initial answer.
2. If the answer is thin, use `wikikb_route` to find the domain, then perform a more thorough search/read using `wikikb_search` and `wikikb_read_page`.
3. Specifically look for "request queue", "OOM", "login storm", and "RHBK 26" in the `keycloak/RHBK` domain.
4. Synthesize the answer based on the findings.
5. Provide the answer with the mandated References section and file it as a `questions/<slug>.md` file.

First step: `wikikb_ask` with the question.

## TOOL wikikb_ask({"domain": "keycloak/RHBK", "question": "Our RHBK 26 cluster slowed to a crawl during a login storm last night. I know RHBK caps its request queue at 1000 by default and sheds anything above that with 503s, so the storm shouldn't have caused memory pressure \u2014 but the pods OOMed anyway. What are)
### OUTPUT
{"query": "Our RHBK 26 cluster slowed to a crawl during a login storm last night. I know RHBK caps its request queue at 1000 by default and sheds anything above that with 503s, so the storm shouldn't have caused memory pressure — but the pods OOMed anyway. What are we missing?", "orchestrator": "langgraph", "domain": "keycloak/RHBK", "confident": true, "thin": true, "banner": [], "guard": [], "answer": "[extractive fallback — no model answer (gateway returned no answer: http://127.0.0.1:11434)] top sources: (no candidates)\n\n## References (canonical)\n\n### RH ground-truth\n- No verified RH ground-truth source was cited.\n\n### Wiki\n- No synthesized Wiki page was used.", "cited": [], "grounding_fail": false, "ungrounded_identifiers": [], "grounding_basis": null, "withheld": false, "references": [], "reference_groups": {"rh_ground_truth": [], "wiki": []}, "session_tokens_served": 29676}

## TOOL wikikb_search({"domain": "keycloak/RHBK", "q": "request queue 1000 OOM login storm"})
### OUTPUT


## ASSISTANT-REASONING
The previous `wikikb_search` failed because I didn't have a valid domain or it wasn't recognized in that way. I should check the available domains first to see how `keycloak/RHBK` is represented. I'll check `index.md` or use `wikikb_route`.

Actually, the user gave a specific domain in the query: "RHBK 26 cluster". The `wikikb_route` tool is designed for this.

## TOOL wikikb_route({"q": "Our RHBK 26 cluster slowed to a crawl during a login storm last night. I know RHBK caps its request queue at 1000 by default and sheds anything above that with 503s, so the storm shouldn't have caused memory pressure \u2014 but the pods OOMed anyway. What are we missing?"})
### OUTPUT
{"domains": ["openshift"], "confident": true, "session_tokens_served": 29687}

## TOOL wikikb_ask({"domain": "openshift", "question": "Our RHBK 26 cluster slowed to a crawl during a login storm last night. I know RHBK caps its request queue at 1000 by default and sheds anything above that with 503s, so the storm shouldn't have caused memory pressure \u2014 but the pods OOMed anyway. What are we )
### OUTPUT
{"query": "Our RHBK 26 cluster slowed to a crawl during a login storm last night. I know RHBK caps its request queue at 1000 by default and sheds anything above that with 503s, so the storm shouldn't have caused memory pressure — but the pods OOMed anyway. What are we missing?", "orchestrator": "langgraph", "domain": "openshift", "confident": true, "thin": false, "banner": ["out-of-coverage: scenarios not in ['conceptual'] (H1)", "provisional: status!=reviewed and inferred>=extracted (21>=13) (L)"], "guard": [], "answer": "⚠️ out-of-coverage: scenarios not in ['conceptual'] (H1) | provisional: status!=reviewed and inferred>=extracted (21>=13) (L)\n\n[extractive fallback — no model answer (gateway returned no answer: http://127.0.0.1:11434)] top sources: networking-4-22-about-user-defined-networks, tutorials-zookeeper, tasks-debug-running-pod, concepts-system-metrics, concepts-swap-memory-management\n\n## References (canonical)\n\n### RH ground-truth\n- `ref:networking-4-22-about-user-defined-networks` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/about-user-defined-networks\n- `ref:tutorials-zookeeper` — https://kubernetes.io/docs/tutorials/stateful-application/zookeeper\n- `ref:tasks-debug-running-pod` — https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod\n- `ref:concepts-system-metrics` — https://kubernetes.io/docs/concepts/cluster-administration/system-metrics\n- `ref:concepts-swap-memory-management` — https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management\n- `ref:applications-4-22-deployment-strategies` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/deployment-strategies\n- `ref:applications-4-22-managing-deployment-processes` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/managing-deployment-processes\n- `ref:applications-4-22-what-deployments-are` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/what-deployments-are\n- `ref:authentication-4-22-configuring-internal-oauth` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/configuring-internal-oauth\n- `ref:authentication-4-22-managing-security-context-constraints` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/managing-security-context-constraints\n- `ref:authentication-4-22-osd-admin-roles` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/osd-admin-roles\n- `ref:authentication-4-22-understanding-and-managing-pod-security-admission` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/understanding-and-managing-pod-security-admission\n- `ref:authentication-4-22-using-rbac` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/using-rbac\n- `ref:concepts-cron-jobs` — https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs\n- `ref:concepts-daemonset` — https://kubernetes.io/docs/concepts/workloads/controllers/daemonset\n- `ref:concepts-deployment` — https://kubernetes.io/docs/concepts/workloads/controllers/deployment\n- `ref:concepts-horizontal-pod-autoscale` — https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale\n- `ref:concepts-job` — https://kubernetes.io/docs/concepts/workloads/controllers/job\n- `ref:concepts-manage-resources-containers` — https://kubernetes.io/docs/concepts/configuration/manage-resources-containers\n- `ref:concepts-network-policies` — https://kubernetes.io/docs/concepts/services-networking/network-policies\n- `ref:concepts-persistent-volumes` — https://kubernetes.io/docs/concepts/storage/persistent-volumes\n- `ref:concepts-pod-lifecycle` — https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle\n- `ref:concepts-rbac-good-practices` — https://kubernetes.io/docs/concepts/security/rbac-good-practices\n- `ref:concepts-service` — https://kubernetes.io/docs/concepts/services-networking/service\n- `ref:concepts-service-accounts` — https://kubernetes.io/docs/concepts/security/service-accounts\n- `ref:concepts-statefulset` — https://kubernetes.io/docs/concepts/workloads/controllers/statefulset\n- `ref:machine-configuration-4-22-index` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_configuration/index\n- `ref:microshift-rest-api-4-22-pod-v1` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_rest_api/pod-v1\n- `ref:networking-4-22-ingress-operator` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/ingress-operator\n- `ref:networking-4-22-nw-configuring-routes` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/nw-configuring-routes\n- `ref:openshift-images-4-22-create-images` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/openshift_images/create-images\n- `ref:operators-4-22-olm-troubleshooting-operator-issues` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/olm-troubleshooting-operator-issues\n- `ref:operators-4-22-olm-understanding-olm` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/olm-understanding-olm\n- `ref:operators-4-22-olm-understanding-operatorgroups` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/olm-understanding-operatorgroups\n- `ref:operators-4-22-olm-what-operators-are` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operators/olm-what-operators-are\n- `ref:storage-4-22-understanding-persistent-storage` — https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/understanding-persistent-storage\n- `