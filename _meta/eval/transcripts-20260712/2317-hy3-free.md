# opencode session ses_0a8058e3dffe7jL0vn1OdJWMjm — 2026-07-12 23:17
model: hy3-free

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
Let me start by running the mechanized QUERY pipeline via the wikikb ask tool. The question mentions RHBK (Red Hat build of Keycloak), so domain is keycloak.

Let me first run the gate. The question names a specific token: "request queue at 1000 by default" — this is about a config option. The token might be something like `http-max-queued-requests` or similar. Let me first search the corpus.

Actually, let me follow instructions: Run the wikikb ask tool first. But I should also do the GATE analysis on the token. The question mentions "request queue at 1000 by default" and "503s". The token being referenced is the request queue cap. Let me think about what token this is in Keycloak/RHBK. In Quarkus, Keycloak has `http-max-queued-requests` which defaults to 10000 actually... wait, the question says 1000. Let me search.

Let me run the wikikb ask tool and also grep the reference tier for tokens.

Let me start.

## ASSISTANT
I'll run the mechanized QUERY pipeline first via the wikikb `ask` tool, then deepen by inspecting the raw corpus.

## TOOL wikikb_ask({"question": "Our RHBK 26 cluster slowed to a crawl during a login storm last night. I know RHBK caps its request queue at 1000 by default and sheds anything above that with 503s, so the storm shouldn't have caused memory pressure \u2014 but the pods OOMed anyway. What are we missing?", "domain": "k)
### OUTPUT
{"query": "Our RHBK 26 cluster slowed to a crawl during a login storm last night. I know RHBK caps its request queue at 1000 by default and sheds anything above that with 503s, so the storm shouldn't have caused memory pressure — but the pods OOMed anyway. What are we missing?", "orchestrator": "langgraph", "domain": "keycloak", "confident": true, "thin": false, "banner": [], "guard": [], "answer": "[extractive fallback — no model answer (gateway returned no answer: http://127.0.0.1:11434)] top sources: rhbk-26-4-fips, rhbk-26-0-fips, rhbk-26-2-fips, rhbk-26-6-single-cluster-introduction, rhbk-26-2-concepts-memory-and-cpu-sizing\n\n## References (canonical)\n\n### RH ground-truth\n- `ref:rhbk-26-4-fips` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/server_configuration_guide/fips-\n- `ref:rhbk-26-0-fips` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_configuration_guide/fips-\n- `ref:rhbk-26-2-fips` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/server_configuration_guide/fips-\n- `ref:rhbk-26-6-single-cluster-introduction` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/high_availability_guide/single-cluster-introduction-\n- `ref:rhbk-26-2-concepts-memory-and-cpu-sizing` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/high_availability_guide/concepts-memory-and-cpu-sizing-\n- `ref:_ref-keycloak-high_availability_guide` — vault reference note\n- `ref:_ref-keycloak-operator_guide` — vault reference note\n- `ref:_ref-keycloak-server_administration_guide` — vault reference note\n- `ref:_ref-keycloak-server_configuration_guide` — vault reference note\n- `ref:_ref-keycloak-server_installation_and_configuration_guide` — vault reference note\n- `ref:references/high-availability` — vault reference note\n- `ref:references/rhbk-troubleshooting-kb` — vault reference note\n- `ref:references/server-configuration` — vault reference note\n- `ref:rhbk-26-0-concepts-memory-and-cpu-sizing` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/high_availability_guide/concepts-memory-and-cpu-sizing-\n- `ref:rhbk-26-0-concepts-multi-site` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/high_availability_guide/concepts-multi-site-\n- `ref:rhbk-26-0-concepts-threads` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/high_availability_guide/concepts-threads-\n- `ref:rhbk-26-0-user-storage-federation` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_administration_guide/user-storage-federation\n- `ref:rhbk-26-2-concepts-multi-site` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/high_availability_guide/concepts-multi-site-\n- `ref:rhbk-26-2-deploy-aws-accelerator-loadbalancer` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/high_availability_guide/deploy-aws-accelerator-loadbalancer-\n- `ref:rhbk-26-2-deploy-infinispan-kubernetes-crossdc` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/high_availability_guide/deploy-infinispan-kubernetes-crossdc-\n- `ref:rhbk-26-2-deploy-keycloak-kubernetes` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/high_availability_guide/deploy-keycloak-kubernetes-\n- `ref:rhbk-26-2-operate-synchronize` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/high_availability_guide/operate-synchronize-\n- `ref:rhbk-26-4-admin-rest-api` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/server_developer_guide/admin_rest_api\n- `ref:rhbk-26-4-assembly-managing-users-server-administration-guide` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/server_administration_guide/assembly-managing-users_server_administration_guide\n- `ref:rhbk-26-4-caching` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/server_configuration_guide/caching-\n- `ref:rhbk-26-4-db` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/server_configuration_guide/db-\n- `ref:rhbk-26-4-multi-cluster-introduction` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/high_availability_guide/multi-cluster-introduction-\n- `ref:rhbk-26-4-user-storage-federation` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/server_administration_guide/user-storage-federation\n- `ref:rhbk-26-4-user-storage-spi` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/server_developer_guide/user-storage-spi\n- `ref:rhbk-26-6-getting-started-scaling-and-tuning` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/getting_started_guide/getting-started-scaling-and-tuning-\n- `ref:rhbk-26-6-multi-cluster-introduction` — https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.6/html/high_availability_guide/multi-cluster-introduction-\n\n### Wiki\n- [[access-token-validation-resource-server]]\n- [[active-active-invalid-grant-token-refresh]]\n- [[active-passive-failover-sessions-lost]]\n- [[active-passive-session-consistency-failover]]\n- [[cap-concurrent-auth-sessions-per-root-session]]\n- [[distributed-caches]]\n- [[ldap-password-change-propagation-delay]]\n- [[parallel-user-import-silent-failure]]\n- [[passthrough-roundrobin-login-loop]]\n- [[rhbk-oscp-scaling-resources]]", "cited": ["rhbk-26-4-fips", "rhbk-26-0-fips", "rhbk-26-2-fips", "rhbk-26-6-single-cluster-introduction", "rhbk-26-2-concepts-memory-and-cpu-sizing", "_ref-keycloak-high_availability_guide", "_ref-keycloak-operator_guide", "_ref-keycloak-server_administration_guide", "_ref-keycloak-server_configuration_guide", "_ref-keycloak-server_installation_and_configuration_guide", "references/high-availability", "references/rhbk-troub

## ASSISTANT-REASONING
The wikikb ask returned an extractive fallback (no model answer because the gateway returned no answer). I need to deepen it by reading candidate pages and grepping the reference tier.

But first, let me apply the GATE. The question names specific tokens that I need to verify in the corpus:
1. The premise that RHBK caps its request queue at 1000 by default and sheds anything above that with 503s.

The token here is the request queue cap. In Keycloak/RHBK, the relevant config option is `http-max-queued-requests` (which corresponds to Quarkus `quarkus.http.max-queued-requests`). Let me check the actual default. Actually, the Keycloak default for `http-max-queued-requests` is... let me search the corpus.

Let me also consider: the question's premise might be WRONG (the whole point of the question "What are we missing?" suggests the premise that the queue cap protects against OOM is flawed). The key insight in Keycloak/RHBK is that:
- The HTTP request queue (`http-max-queued-requests`, default 10000 in Quarkus, NOT 1000) is only one part. 
- There's also the thread pool sizing, the database connection pool, infinispan caches, etc.
- The actual OOM cause during a login storm: each login holds memory for authentication sessions, user objects, etc. The request queue only limits concurrent HTTP connections, but login processing spawns work. Also, the default heap settings, and importantly the fact that login storms cause many in-flight authentications that hold memory.
- Also `spi-login-request-concurrency` or something about concurrent login requests.

Let me search the corpus for the actual relevant tokens. Let me grep the reference tier.

Actually I should follow the wiki-query operation: read index.keycloak.md, candidate pages' title/summary, then grep reference tier. Let me do this properly.

Let me grep for the relevant tokens in the reference directory.

Let me run several searches in parallel:
1. `http-max-queued-requests` or `max-queued-requests` in reference
2. `http-max-queued-requests` env form `KC_HTTP_MAX_QUEUED_REQUESTS`
3. memory sizing / OOM related
4. threads
5. db pool

Let me first find the reference directory and the index.

Let me do parallel gre

## ASSISTANT
The `ask` tool fell back to an extractive mode (no model answer — Ollama gateway unavailable). I'll now run the GATE on the question's claimed tokens and deepen the answer by reading the synthesis layer + grepping the raw corpus.

## TOOL glob({"pattern": "reference/keycloak/*.md"})
### OUTPUT
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-operate-site-online.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhsso-7-5-getting-started-overview.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-admin-permissions.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-updates-for-26-2-15.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhsso-7-4-release-changes.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-fips.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/doc-security-keycloak-authorization-2.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-customizing-keycloak.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/_ref-keycloak-api_documentation.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-removed.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-token-exchange.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-bootstrap-admin-recovery.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-enforcer-overview.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-supported.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/doc-configuring-central-auth-generic-oidc-settings.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-other-changes.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-overview-2.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-mod-auth-mellon.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-sso-protocols.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhsso-7-0-sso-protocols.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-concepts-memory-and-cpu-sizing.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-assigning-permissions-using-roles-and-groups.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/doc-assembly-enabling-configuring-the-keycloak-plugin-assembly-installing-configuring-jfrog-2.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-6-techpreview.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-6-upgrading.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-nodejs-adapter.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-6-server-developer-guide.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-updates-for-26-2-8.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-deploy-keycloak-kubernetes.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-caching.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-admin-client.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-6-overview.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-db.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-upgrading-red-hat-build-of-keycloak-adapters.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-deploy-aws-accelerator-loadbalancer.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/doc-7078462.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-vault-spi.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-multi-cluster-introduction.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-keycloak-truststore.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/doc-2342861.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhsso-7-4-overview.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-authorization-services-guide.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-user-storage-federation.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhsso-7-5-policy-overview.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-6-overview-2.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-migration-changes.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-api-documentation.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-6-deprecated.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-db.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-configuration-production.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-client-registration.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhsso-7-4-identity-broker.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-bblocks-multi-site.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-concepts-threads.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-6-migrating-red-hat-single-sign-on-7-6-to-red-hat-build-of-keycloak.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhsso-7-6-database.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-authz-client.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhsso-7-6-themes.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-upgrading-the-red-hat-build-of-keycloak-client-libraries.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/doc-3419601.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhsso-7-6-assembly-managing-clients-server-administration-guide.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-logging.md
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/doc-7072930.md
/Users/guylavian/Do

## TOOL glob({"pattern": "index.keycloak.md"})
### OUTPUT
/Users/guylavian/Downloads/skills/llm-wiki/index.keycloak.md

## TOOL grep({"pattern": "max-queued-requests|queued.?requests|http-max-queued", "path": "reference/keycloak", "include": "*.md"})
### OUTPUT
Found 44 matches
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-concepts-threads.md:
  Line 47: By default, Red Hat build of Keycloak will queue all incoming requests infinitely, even if the request processing stalls. This will use additional memory in the Pod, can exhaust resources in the load balancers, and the requests will eventually time out on the client side without the client knowing if the request has been processed. To limit the number of queued requests in Red Hat build of Keycloak, set an additional Quarkus configuration option.

  Line 48: Configure http-max-queued-requests

  Line 50: When this setting is active, requests that exceed the number of queued requests will return with an HTTP 503 error. Red Hat build of Keycloak logs the error message in its log.


/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-multi-cluster-introduction.md:
  Line 128: Network latency and latency spikes amplify in the response time of the service and can lead to queued requests, timeouts, and failed requests. Networking problems can cause downtimes until the failure detection isolates problematic nodes.

  Line 165: By default, Red Hat build of Keycloak will queue all incoming requests infinitely, even if the request processing stalls. This will use additional memory in the Pod, can exhaust resources in the load balancers, and the requests will eventually time out on the client side without the client knowing if the request has been processed. To limit the number of queued requests in Red Hat build of Keycloak, set an additional Quarkus configuration option.

  Line 166: Configure http-max-queued-requests

  Line 168: When this setting is active, requests that exceed the number of queued requests will return with an HTTP 503 error. Red Hat build of Keycloak logs the error message in its log.

  Line 790: To enable load shedding, limit the number of queued requests.

  Line 794: - name: http-max-queued-requests


/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-deploy-keycloak-kubernetes.md:
  Line 57: To enable load shedding, limit the number of queued requests.

  Line 61: - name: http-max-queued-requests


/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-concepts-threads.md:
  Line 36: By default, Red Hat build of Keycloak will queue all incoming requests infinitely, even if the request processing stalls. This will use additional memory in the Pod, can exhaust resources in the load balancers, and the requests will eventually time out on the client side without the client knowing if the request has been processed. To limit the number of queued requests in Red Hat build of Keycloak, set an additional Quarkus configuration option.

  Line 37: Configure http-max-queued-requests

  Line 39: When this setting is active, requests that exceed the number of queued requests will return with an HTTP 503 error. Red Hat build of Keycloak logs the error message in its log.


/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-configuration-production.md:
  Line 35: 2.4. Limit the number of queued requests

  Line 37: Load shedding should be implemented on all levels, including the load balancers in your environment. In addition to that, there is a feature in Red Hat build of Keycloak to limit the number of requests that can’t be processed right away and need to be queued. By default, there is no limit set. Set the option http-max-queued-requests

  Line 38: to limit the number of queued requests to a given threshold matching your environment. Any request that exceeds this limit would return with an immediate 503 Server not Available


/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-6-single-cluster-introduction.md:
  Line 153: Network latency and latency spikes amplify in the response time of the service and can lead to queued requests, timeouts, and failed requests. Networking problems can cause downtimes until the failure detection isolates problematic nodes.

  Line 185: By default, Red Hat build of Keycloak will queue all incoming requests infinitely, even if the request processing stalls. This will use additional memory in the Pod, can exhaust resources in the load balancers, and the requests will eventually time out on the client side without the client knowing if the request has been processed. To limit the number of queued requests in Red Hat build of Keycloak, set an additional Quarkus configuration option.

  Line 186: Configure http-max-queued-requests

  Line 188: When this setting is active, requests that exceed the number of queued requests will return with an HTTP 503 error. Red Hat build of Keycloak logs the error message in its log.

  Line 1079: To enable load shedding, limit the number of queued requests.

  Line 1083: - name: http-max-queued-requests


/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-single-cluster-introduction.md:
  Line 151: Network latency and latency spikes amplify in the response time of the service and can lead to queued requests, timeouts, and failed requests. Networking problems can cause downtimes until the failure detection isolates problematic nodes.

  Line 178: By default, Red Hat build of Keycloak will queue all incoming requests infinitely, even if the request processing stalls. This will use additional memory in the Pod, can exhaust resources in the load balancers, and the requests will eventually time out on the client side without the client knowing if the request has been processed. To limit the number of queued requests in Red Hat build of Keycloak, set an additional Quarkus configuration option.

  Line 179: Configure http-max-queued-requests

  Line 181: When this setting is active, requests that exceed the number of queued requests will return with an HTTP 503 error. Red Hat build of Keycloak logs the error message in its log.

  Line 448: To enable load shedding, limit the number of queue

## ASSISTANT-REASONING
Now I have critical findings. The GATE:

The question's premise claims: "RHBK caps its request queue at 1000 by default". 

The token here is `http-max-queued-requests` (the actual config option). Let me check its default. The corpus says: "By default, Red Hat build of Keycloak will queue all incoming requests infinitely" and "By default, there is no limit set." So the default for `http-max-queued-requests` is NOT 1000 — it is UNLIMITED (no limit). The 1000 value appears in an example in `rhbk-26-0-deploy-keycloak-kubernetes.md` line 37: `value: "1000"`. That is a suggested/custom value, not the default.

So the user's premise "RHBK caps its request queue at 1000 by default" is FALSE. The actual default is unlimited (infinite). This is the key "what are we missing" answer!

So the user is missing:
1. The default is UNLIMITED — there is no cap by default. So the queue grows without bound = memory pressure = OOM. The 1000 they think of is an example value someone set, OR they misremember. Actually wait — the question says "I know RHBK caps its request queue at 1000 by default". The corpus clearly states default is no limit. So either:
   - Their cluster doesn't actually have `http-max-queued-requests` set to 1000 (maybe they think it's the default but it's not set at all → unlimited → OOM), OR
   - They set it to 1000 themselves.

Either way, the key insight: by default there is NO limit; requests queue infinitely and consume Pod memory. If they assumed the default is 1000, that assumption itself is wrong.

But the question asks "what are we missing?" — pointing to deeper causes. Let me dig into the actual OOM causes during a login storm. The relevant concepts:
- memory-and-cpu-sizing
- threads
- database connections
- infinispan caches
- auth sessions

Let me read the key reference files to understand the full picture: concepts-memory-and-cpu-sizing, concepts-threads, and the production configuration about queued requests, plus the troubleshooting KB.

Let me also check the GATE for the token. The question doesn't name `http-max-queued-requests` explicitly — it describes "request queue at 1000 by default". The token in question (the config option that caps the request queue) is `http-max-queued-requests`. It EXISTS in the corpus. Good.

But the premise about "default 1000" is wrong. So I must flag that the default is unlimited. Let me confirm by reading the relevant reference pages carefully.

Let me read:
- rhbk-26-2-concepts-threads.md (full)
- rhbk-26-2-concepts-memory-and-cpu-sizing.md (full)
- rhbk-26-2-configuration-production.md (full, about queued requests + other prod settings)
- references/rhbk-troubleshooting-kb.md or server-configuration

Let me also search for OOM / memory / heap / OutOfMemory related tokens.

Let me do parallel reads and greps.

## ASSISTANT
Key finding already: the corpus states the **default** for `http-max-queued-requests` is *no limit* (infinite queue), and `1000` only appears as an example value. That contradicts the question's premise. Let me dig into the memory/thread/OOM mechanics and confirm.

## TOOL read({"filePath": "/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-concepts-threads.md"})
### OUTPUT
<path>/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-concepts-threads.md</path>
<type>file</type>
<content>
1: ---
2: title: "Chapter 5. Concepts for configuring thread pools - Red Hat build of Keycloak 26.2 High Availability Guide"
3: type: reference
4: domain: keycloak
5: slug: rhbk-26-2-concepts-threads
6: tier: reference
7: source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/high_availability_guide/concepts-threads-
8: guide: high_availability_guide
9: version: 26.2
10: family: rhbk
11: documentKind: "Documentation"
12: primary: true
13: abstract: "Understand concepts for avoiding resource exhaustion and congestion. This section is intended when you want to understand the considerations and best practices on how to configure thread pools connection pools for Red Hat build of Keycloak. For a configuration where this is applied, visit Deploying Red Hat build of Keycloak for HA with the Operator. 5.1. Concepts 5.1.1. JGroups communications JGro…"
14: ---
15: 
16: # Chapter 5. Concepts for configuring thread pools - Red Hat build of Keycloak 26.2 High Availability Guide
17: 
18: Chapter 5. Concepts for configuring thread pools
19: Understand concepts for avoiding resource exhaustion and congestion.
20: This section is intended when you want to understand the considerations and best practices on how to configure thread pools connection pools for Red Hat build of Keycloak. For a configuration where this is applied, visit Deploying Red Hat build of Keycloak for HA with the Operator.
21: 5.1. Concepts
22: 5.1.1. JGroups communications
23: JGroups communications, which is used in single-site setups for the communication between Red Hat build of Keycloak nodes, benefits from the use of virtual threads which are available in OpenJDK 21 when at least four cores are available for Red Hat build of Keycloak. This reduces the memory usage and removes the need to configure thread pool sizes. Therefore, the use of OpenJDK 21 is recommended.
24: 5.1.2. Quarkus executor pool
25: Red Hat build of Keycloak requests, as well as blocking probes, are handled by an executor pool. Depending on the available CPU cores, it has a maximum size of 50 or more threads. Threads are created as needed, and will end when no longer needed, so the system will scale up and down automatically. Red Hat build of Keycloak allows configuring the maximum thread pool size by the http-pool-max-threads
26: configuration option. See Deploying Red Hat build of Keycloak for HA with the Operator for an example.
27: When running on Kubernetes, adjust the number of worker threads to avoid creating more load than what the CPU limit allows for the Pod to avoid throttling, which would lead to congestion. When running on physical machines, adjust the number of worker threads to avoid creating more load than the node can handle to avoid congestion. Congestion would result in longer response times and an increased memory usage, and eventually an unstable system.
28: Ideally, you should start with a low limit of threads and adjust it accordingly to the target throughput and response time. When the load and the number of threads increases, the database connections can also become a bottleneck. Once a request cannot acquire a database connection within 5 seconds, it will fail with a message in the log like Unable to acquire JDBC Connection
29: . The caller will receive a response with a 5xx HTTP status code indicating a server side error.
30: If you increase the number of database connections and the number of threads too much, the system will be congested under a high load with requests queueing up, which leads to a bad performance. The number of database connections is configured via the Database
31: settings db-pool-initial-size
32: , db-pool-min-size
33: and db-pool-max-size
34: respectively. Low numbers ensure fast response times for all clients, even if there is an occasionally failing request when there is a load spike.
35: 5.1.3. Load Shedding
36: By default, Red Hat build of Keycloak will queue all incoming requests infinitely, even if the request processing stalls. This will use additional memory in the Pod, can exhaust resources in the load balancers, and the requests will eventually time out on the client side without the client knowing if the request has been processed. To limit the number of queued requests in Red Hat build of Keycloak, set an additional Quarkus configuration option.
37: Configure http-max-queued-requests
38: to specify a maximum queue length to allow for effective load shedding once this queue size is exceeded. Assuming a Red Hat build of Keycloak Pod processes around 200 requests per second, a queue of 1000 would lead to maximum waiting times of around 5 seconds.
39: When this setting is active, requests that exceed the number of queued requests will return with an HTTP 503 error. Red Hat build of Keycloak logs the error message in its log.
40: 5.1.4. Probes
41: Red Hat build of Keycloak’s liveness probe is non-blocking to avoid a restart of a Pod under a high load.
42: The overall health probe and the readiness probe can in some cases block to check the connection to the database, so they might fail under a high load. Due to this, a Pod can become non-ready under a high load.
43: 5.1.5. OS Resources
44: In order for Java to create threads, when running on Linux it needs to have file handles available. Therefore, the number of open files (as retrieved as ulimit -n
45: on Linux) need to provide head-space for Red Hat build of Keycloak to increase the number of threads needed. Each thread will also consume memory, and the container memory limits need to be set to a value that allows for this or the Pod will be killed by Kubernetes.

(End of file - total 45 lines)
</content>

## TOOL read({"filePath": "/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-configuration-production.md"})
### OUTPUT
<path>/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-configuration-production.md</path>
<type>file</type>
<content>
1: ---
2: title: "Chapter 2. Configuring Red Hat build of Keycloak for production - Red Hat build of Keycloak 26.2 Server Configuration Guide"
3: type: reference
4: domain: keycloak
5: slug: rhbk-26-2-configuration-production
6: tier: reference
7: source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/server_configuration_guide/configuration-production-
8: guide: server_configuration_guide
9: version: 26.2
10: family: rhbk
11: documentKind: "Documentation"
12: abstract: "Prepare Red Hat build of Keycloak for use in production. A Red Hat build of Keycloak production environment provides secure authentication and authorization for deployments that range from on-premise deployments that support a few thousand users to deployments that serve millions of users. This chapter describes the general areas of configuration required for a production ready Red Hat build of Ke…"
13: ---
14: 
15: # Chapter 2. Configuring Red Hat build of Keycloak for production - Red Hat build of Keycloak 26.2 Server Configuration Guide
16: 
17: Chapter 2. Configuring Red Hat build of Keycloak for production
18: Prepare Red Hat build of Keycloak for use in production.
19: A Red Hat build of Keycloak production environment provides secure authentication and authorization for deployments that range from on-premise deployments that support a few thousand users to deployments that serve millions of users.
20: This chapter describes the general areas of configuration required for a production ready Red Hat build of Keycloak environment. This information focuses on the general concepts instead of the actual implementation, which depends on your environment. The key aspects covered in this chapter apply to all environments, whether it is containerized, on-premise, GitOps, or Ansible.
21: 2.1. TLS for secure communication
22: Red Hat build of Keycloak continually exchanges sensitive data, which means that all communication to and from Red Hat build of Keycloak requires a secure communication channel. To prevent several attack vectors, you enable HTTP over TLS, or HTTPS, for that channel.
23: To configure secure communication channels for Red Hat build of Keycloak, see Configuring TLS and Configuring outgoing HTTP requests.
24: To secure the cache communication for Red Hat build of Keycloak, see Configuring distributed caches.
25: 2.2. The hostname for Red Hat build of Keycloak
26: In a production environment, Red Hat build of Keycloak instances usually run in a private network, but Red Hat build of Keycloak needs to expose certain public facing endpoints to communicate with the applications to be secured.
27: For details on the endpoint categories and instructions on how to configure the public hostname for them, see Configuring the hostname (v2).
28: 2.2.1. Exposing the Red Hat build of Keycloak Administration APIs and UI on a different hostname
29: It is considered a best practice to expose the Red Hat build of Keycloak Administration REST API and Console on a different hostname or context-path than the one used for the public frontend URLs that are used e.g. by login flows. This separation ensures that the Administration interfaces are not exposed to the public internet, which reduces the attack surface.
30: Access to REST APIs needs to be blocked on the reverse proxy level, if they are not intended to be publicly exposed.
31: For details, see Configuring the hostname (v2).
32: 2.3. Reverse proxy in a distributed environment
33: Apart from Configuring the hostname (v2), production environments usually include a reverse proxy / load balancer component. It separates and unifies access to the network used by your company or organization. For a Red Hat build of Keycloak production environment, this component is recommended.
34: For details on configuring proxy communication modes in Red Hat build of Keycloak, see Configuring a reverse proxy. That chapter also recommends which paths should be hidden from public access and which paths should be exposed so that Red Hat build of Keycloak can secure your applications.
35: 2.4. Limit the number of queued requests
36: A production environment should protect itself from an overload situation, so that it responds to as many valid requests as possible, and to continue regular operations once the situation returns to normal again. One way of doing this is rejecting additional requests once a certain threshold is reached.
37: Load shedding should be implemented on all levels, including the load balancers in your environment. In addition to that, there is a feature in Red Hat build of Keycloak to limit the number of requests that can’t be processed right away and need to be queued. By default, there is no limit set. Set the option http-max-queued-requests
38: to limit the number of queued requests to a given threshold matching your environment. Any request that exceeds this limit would return with an immediate 503 Server not Available
39: response.
40: 2.5. Production grade database
41: The database used by Red Hat build of Keycloak is crucial for the overall performance, availability, reliability and integrity of Red Hat build of Keycloak. For details on how to configure a supported database, see Configuring the database.
42: 2.6. Running Red Hat build of Keycloak in a cluster
43: To ensure that users can continue to log in when a Red Hat build of Keycloak instance goes down, a typical production environment contains two or more Red Hat build of Keycloak instances.
44: Red Hat build of Keycloak runs on top of JGroups and Infinispan, which provide a reliable, high-availability stack for a clustered scenario. In the default setup, communication between the nodes is encrypted using TLS.
45: To find out more about using multiple nodes, the different caches and an appropriate stack for your environment, see Configuring distri

## TOOL grep({"pattern": "OutOfMemory|OOM|heap|Xmx|memory pressure|memory in the Pod|exhaust", "path": "reference/keycloak", "include": "*.md"})
### OUTPUT
Found 100 matches (more matches available)
/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-concepts-threads.md:
  Line 47: By default, Red Hat build of Keycloak will queue all incoming requests infinitely, even if the request processing stalls. This will use additional memory in the Pod, can exhaust resources in the load balancers, and the requests will eventually time out on the client side without the client knowing if the request has been processed. To limit the number of queued requests in Red Hat build of Keycloak, set an additional Quarkus configuration option.


/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhsso-7-5-getting-started-overview.md:
  Line 92: to theapp-authz-jee-vanilla/config


/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhsso-7-4-reference.md:
  Line 71: | GC_MAX_HEAP_FREE_RATIO | Maximum percentage of heap free after GC to avoid shrinking. | 40 |

  Line 73: | GC_TIME_RATIO_MIN_HEAP_FREE_RATIO | Minimum percentage of heap free after GC to avoid expansion. | 20 |

  Line 77: This is used to calculate a default initial heap memory based the maximal heap memory. The default is 100 which means 100% of the maximal heap is used for the initial heap size. You can skip this mechanism by setting this value to 0 in which case no | 100 |

  Line 79: It is used to calculate a default maximal heap memory based on a containers restriction. If used in a Docker container without any memory constraints for the container then this option has no effect. If there is a memory constraint then | 40 |


/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-concepts-threads.md:
  Line 13: abstract: "Understand concepts for avoiding resource exhaustion and congestion. This section is intended when you want to understand the considerations and best practices on how to configure thread pools connection pools for Red Hat build of Keycloak. For a configuration where this is applied, visit Deploying Red Hat build of Keycloak for HA with the Operator. 5.1. Concepts 5.1.1. JGroups communications JGro…"

  Line 19: Understand concepts for avoiding resource exhaustion and congestion.

  Line 36: By default, Red Hat build of Keycloak will queue all incoming requests infinitely, even if the request processing stalls. This will use additional memory in the Pod, can exhaust resources in the load balancers, and the requests will eventually time out on the client side without the client knowing if the request has been processed. To limit the number of queued requests in Red Hat build of Keycloak, set an additional Quarkus configuration option.


/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-0-getting-started-scaling-and-tuning.md:
  Line 26: Before increasing the amount of memory available to the JVM, in particular when experiencing an out of memory error, it is best to determine what is contributing to the increased footprint using a heap dump. Excessive response times may also indicate the HTTP work queue is too large and tuning for load shedding would be better than simply providing more memory. See the following section.


/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhsso-7-6-reference.md:
  Line 72: | GC_MAX_HEAP_FREE_RATIO | Maximum percentage of heap free after GC to avoid shrinking. | 40 |

  Line 74: | GC_TIME_RATIO_MIN_HEAP_FREE_RATIO | Minimum percentage of heap free after GC to avoid expansion. | 20 |

  Line 78: This is used to calculate a default initial heap memory based the maximal heap memory. The default is 100 which means 100% of the maximal heap is used for the initial heap size. You can skip this mechanism by setting this value to 0 in which case no | 100 |

  Line 80: It is used to calculate a default maximal heap memory based on a containers restriction. If used in a Docker container without any memory constraints for the container then this option has no effect. If there is a memory constraint then | 40 |


/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-4-multi-cluster-introduction.md:
  Line 150: Understand concepts for avoiding resource exhaustion and congestion.

  Line 158: Understand concepts for avoiding resource exhaustion and congestion.

  Line 165: By default, Red Hat build of Keycloak will queue all incoming requests infinitely, even if the request processing stalls. This will use additional memory in the Pod, can exhaust resources in the load balancers, and the requests will eventually time out on the client side without the client knowing if the request has been processed. To limit the number of queued requests in Red Hat build of Keycloak, set an additional Quarkus configuration option.

  Line 176: Understand concepts for avoiding resource exhaustion and congestion.

  Line 186: - In containers, Keycloak allocates 70% of the memory limit for heap-based memory. It will also use approximately 300 MB of non-heap-based memory. To calculate the requested memory, use the calculation above. As memory limit, subtract the non-heap memory from the value above and divide the result by 0.7.

  Line 239: (1250 MB expected memory usage minus 300 non-heap-usage, divided by 0.7)


/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/doc-7135882.md:
  Line 48: Lazy Deletion Logic: To maintain high performance—especially in environments with high session churn (e.g., 1,500 sessions/minute)—Keycloak does not execute a synchronous DELETE query the exact millisecond a session expires. Doing so would cause excessive database lock contention and connection pool exhaustion.


/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/doc-security-keycloak-authorization-2.md:
  Line 517: scope, based on the configuration set in theapplication.properties


/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/doc-3419601.md:
  Line 9: abstract: "Xmx & Xms parameters in Red Hat Single Sign-On use defaults values. If out of memory exce

## ASSISTANT-REASONING
Now I have a comprehensive picture. Let me apply the GATE carefully.

TOKEN: The question describes a config option "RHBK caps its request queue at 1000 by default". The actual token for this is `http-max-queued-requests`. Does it exist? YES. It appears verbatim in the corpus many times.

VERDICT for the token: EXISTS. But the PREMISE about its default is wrong — the corpus says default is "no limit set" / "queue all incoming requests infinitely". So the user is misinformed: there is no default cap of 1000. The 1000 value appears only as an example (in rhbk-26-0-deploy-keycloak-kubernetes.md line 37, and in the threads doc's worked example explaining a 1000 queue → 5s wait at 200 req/s).

So the gate result:
- TOKEN: `http-max-queued-requests` (the option that caps the request queue). VERBATIM_MATCH: yes. VERDICT: EXISTS.
- But the default value claim "1000 by default" is FALSE per the corpus.

Now the deeper answer to "what are we missing?" The OOM causes during a login storm, even if a queue cap is set:

1. **The queue cap default is NOT 1000 — it's unlimited.** If they never actually set `http-max-queued-requests`, the queue grows infinitely and consumes Pod memory directly ("This will use additional memory in the Pod"). So the assumption that requests are shed at 1000 is itself the gap — likely it was never set.

2. **The HTTP request queue is only ONE memory/resource dimension.** Even with the queue capped, the actual in-flight login requests are processed by the Quarkus executor pool (http-pool-max-threads, default max 50+ threads depending on cores). Each in-flight login holds:
   - Thread stack memory (each thread consumes memory; container memory limits must allow for it or Pod is killed).
   - DB connections: db-pool-max-size. Under a login storm, threads queue for DB connections; if pool exhausted, requests fail after 5s with "Unable to acquire JDBC Connection" but the threads themselves still consume resources and contention causes congestion → more memory.
   - Authentication sessions in-memory (Infinispan caches): a login storm creates many authentication sessions, which consume heap.
   - Non-heap memory ~300 MB baseline; heap is 70% of container memory (MaxRAMPercentage=70). If the container memory limit is set too low, the heap is small, and a storm pushes it over → OOM kill.

3. **Worker threads vs CPU limits (throttling/congestion):** On Kubernetes, if worker threads exceed what the CPU limit allows, the Pod is throttled → congestion → longer response times → increased memory usage → unstable system → OOM. So even with a queue cap, misconfigured thread pool + CPU limit mismatch causes memory blowup.

4. **Heap dump / memory limit not set:** If memory limit unset, heap can grow up to 70% of total container memory and isn't returned to OS readily. The sizing doc explains the 70% heap / 300MB non-heap calc. For load shedding, the getting-started doc explicitly says: "Before increasing the amount of memory available to the JVM, in particular when experiencing an out of memory error, it is best to determine what is contributing to the increased footprint using a heap dump. Excessive response times may also indicate the HTTP work queue is too large and tuning for load shedding would be better than simply providing more memory."

5. **Readiness probe failure under load:** readiness probe can block checking DB connection and fail under high load → Pod becomes non-ready → load balancer sheds but also the request queue inside Keycloak still grows.

6. **JWT token cache exhaustion CVE-2025-2559:** a trusted client with long-lived JWT tokens can cause memory exhaustion due to unbounded token caching. Possibly relevant if the "login storm" involves token reuse, but more of a security note.

Let me also verify the env var form. The CLI↔env-var duality: `http-max-queued-requests` as an additionalOption maps to `KC_HTTP_MAX_QUEUED_REQUESTS`? Actually in Keycloak the build option format `http-max-queued-requests` maps to env

## ASSISTANT
I have the core mechanics. Let me pull the full memory-sizing and scaling/tuning pages to ground the OOM diagnosis precisely before writing the answer.

## TOOL read({"filePath": "/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-concepts-memory-and-cpu-sizing.md"})
### OUTPUT
<path>/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-concepts-memory-and-cpu-sizing.md</path>
<type>file</type>
<content>
1: ---
2: title: "Chapter 6. Concepts for sizing CPU and memory resources - Red Hat build of Keycloak 26.2 High Availability Guide"
3: type: reference
4: domain: keycloak
5: slug: rhbk-26-2-concepts-memory-and-cpu-sizing
6: tier: reference
7: source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/high_availability_guide/concepts-memory-and-cpu-sizing-
8: guide: high_availability_guide
9: version: 26.2
10: family: rhbk
11: documentKind: "Documentation"
12: primary: true
13: abstract: "Understand concepts for avoiding resource exhaustion and congestion. Use this as a starting point to size a product environment. Adjust the values for your environment as needed based on your load tests. 6.1. Performance recommendations Warning Performance will be lowered when scaling to more Pods (due to additional overhead) and using a cross-datacenter setup (due to additional traffic and operat…"
14: ---
15: 
16: # Chapter 6. Concepts for sizing CPU and memory resources - Red Hat build of Keycloak 26.2 High Availability Guide
17: 
18: Chapter 6. Concepts for sizing CPU and memory resources
19: Understand concepts for avoiding resource exhaustion and congestion.
20: Use this as a starting point to size a product environment. Adjust the values for your environment as needed based on your load tests.
21: 6.1. Performance recommendations
22: - Performance will be lowered when scaling to more Pods (due to additional overhead) and using a cross-datacenter setup (due to additional traffic and operations).
23: - Increased cache sizes can improve the performance when Red Hat build of Keycloak instances running for a longer time. This will decrease response times and reduce IOPS on the database. Still, those caches need to be filled when an instance is restarted, so do not set resources too tight based on the stable state measured once the caches have been filled.
24: - Use these values as a starting point and perform your own load tests before going into production.
25: Summary:
26: - The used CPU scales linearly with the number of requests up to the tested limit below.
27: Recommendations:
28: - The base memory usage for a Pod including caches of Realm data and 10,000 cached sessions is 1250 MB of RAM.
29: - In containers, Keycloak allocates 70% of the memory limit for heap-based memory. It will also use approximately 300 MB of non-heap-based memory. To calculate the requested memory, use the calculation above. As memory limit, subtract the non-heap memory from the value above and divide the result by 0.7.
30: For each 15 password-based user logins per second, allocate 1 vCPU to the cluster (tested with up to 300 per second).
31: Red Hat build of Keycloak spends most of the CPU time hashing the password provided by the user, and it is proportional to the number of hash iterations.
32: For each 120 client credential grants per second, 1 vCPU to the cluster (tested with up to 2000 per second).*
33: Most CPU time goes into creating new TLS connections, as each client runs only a single request.
34: - For each 120 refresh token requests per second, 1 vCPU to the cluster (tested with up to 435 refresh token requests per second).*
35: - Leave 150% extra head-room for CPU usage to handle spikes in the load. This ensures a fast startup of the node, and enough capacity to handle failover tasks. Performance of Red Hat build of Keycloak dropped significantly when its Pods were throttled in our tests.
36: -
37: When performing requests with more than 2500 different clients concurrently, not all client information will fit into Red Hat build of Keycloak’s caches when those are using the standard cache sizes of 10000 entries each. Due to this, the database may become a bottleneck as client data is reloaded frequently from the database. To reduce the database usage, increase the
38: users
39: cache size by two times the number of concurrently used clients, and therealms
40: cache size by four times the number of concurrently used clients.
41: Red Hat build of Keycloak, which by default stores user sessions in the database, requires the following resources for optimal performance on an Aurora PostgreSQL multi-AZ database:
42: For every 100 login/logout/refresh requests per second:
43: - Budget for 1400 Write IOPS.
44: - Allocate between 0.35 and 0.7 vCPU.
45: The vCPU requirement is given as a range, as with an increased CPU saturation on the database host the CPU usage per request decreases while the response times increase. A lower CPU quota on the database can lead to slower response times during peak loads. Choose a larger CPU quota if fast response times during peak loads are critical. See below for an example.
46: 6.1.1. Measuring the activity of a running Red Hat build of Keycloak instance
47: Sizing of a Red Hat build of Keycloak instance depends on the actual and forecasted numbers for password-based user logins, refresh token requests, and client credential grants as described in the previous section.
48: To retrieve the actual numbers of a running Red Hat build of Keycloak instance for these three key inputs, use the metrics Red Hat build of Keycloak provides:
49: -
50: The user event metric
51: keycloak_user_events_total
52: for event typelogin
53: includes both password-based logins and cookie-based logins, still it can serve as a first approximate input for this sizing guide. -
54: To find out number of password validations performed by Red Hat build of Keycloak use the metric
55: keycloak_credentials_password_hashing_validations_total
56: . The metric also contains tags providing some details about the hashing algorithm used and the outcome of the validation. Here is the list of available tags:realm
57: ,algorithm
58: ,hashing_strength
59: ,outcome
60: . -
61: Use the user event metric
62: keycloak_user_events_total
63: for the event typesr

## TOOL read({"filePath": "/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-getting-started-scaling-and-tuning.md"})
### OUTPUT
<path>/Users/guylavian/Downloads/skills/llm-wiki/reference/keycloak/rhbk-26-2-getting-started-scaling-and-tuning.md</path>
<type>file</type>
<content>
1: ---
2: title: "Chapter 2. Scaling - Red Hat build of Keycloak 26.2 Getting Started Guide"
3: type: reference
4: domain: keycloak
5: slug: rhbk-26-2-getting-started-scaling-and-tuning
6: tier: reference
7: source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/getting_started_guide/getting-started-scaling-and-tuning-
8: guide: getting_started_guide
9: version: 26.2
10: family: rhbk
11: documentKind: "Documentation"
12: abstract: "Scale and tune your Red Hat build of Keycloak installation. After starting Red Hat build of Keycloak, consider adapting your instance to the required load using these scaling and tuning guidelines: minimize resource utilization achieve target response times minimize database pool contention resolve out of memory errors, or excessive garbage collection overhead provide higher availability via horiz…"
13: ---
14: 
15: # Chapter 2. Scaling - Red Hat build of Keycloak 26.2 Getting Started Guide
16: 
17: Chapter 2. Scaling
18: Scale and tune your Red Hat build of Keycloak installation.
19: After starting Red Hat build of Keycloak, consider adapting your instance to the required load using these scaling and tuning guidelines:
20: - minimize resource utilization
21: - achieve target response times
22: - minimize database pool contention
23: - resolve out of memory errors, or excessive garbage collection overhead
24: - provide higher availability via horizontal scaling
25: 2.1. Vertical Scaling
26: As you monitor your Red Hat build of Keycloak workload, check to see if the CPU or memory is under or over utilized. Consult Concepts for sizing CPU and memory resources to better tune the resources available to the Java Virtual Machine (JVM).
27: Before increasing the amount of memory available to the JVM, in particular when experiencing an out of memory error, it is best to determine what is contributing to the increased footprint using a heap dump. Excessive response times may also indicate the HTTP work queue is too large and tuning for load shedding would be better than simply providing more memory. See the following section.
28: 2.1.1. Common Tuning Options
29: Red Hat build of Keycloak automatically adjusts the number of used threads based upon how many cores you make available. Manually changing the thread count can improve overall throughput. For more details, see Concepts for configuring thread pools. However, changing the thread count must be done in conjunction with other JVM resources, such as database connections; otherwise, you may be moving a bottleneck somewhere else. For more details, see Concepts for database connection pools.
30: To limit memory utilization of queued work and to provide for load shedding, see Concepts for configuring thread pools.
31: If you are experiencing timeouts in obtaining database connections, you should consider increasing the number of connections available. For more details, see Concepts for database connection pools.
32: 2.1.2. Vertical Autoscaling
33: Some platforms, such as Kubernetes, provide mechanisms to vertically autoscale. Vertical autoscaling is not recommended for Red Hat build of Keycloak if it requires restarting the server instance, which is currently the case for Java on Kubernetes. You can consider instead providing higher CPU and/or memory limits to allow your JVM to adapt within those limits as needed.
34: 2.2. Horizontal Scaling
35: A single Red Hat build of Keycloak instance is susceptible to availability issues. If the instance goes down, you experience a full outage until another instance comes up. By running two or more cluster members on different machines, you greatly increase the availability of Red Hat build of Keycloak.
36: A single JVM has a limit on how many concurrent requests it can handle. Additional server instances can provide roughly linear scaling of throughput until associated resources, such as the database or distributed caching, limit that scaling.
37: In general, consider allowing the Red Hat build of Keycloak Operator to handle horizontal scaling concerns. When using the Operator, set the Keycloak custom resource spec.instances
38: as desired to horizontally scale. For more details, see Deploying Red Hat build of Keycloak for HA with the Operator.
39: If you are not using the Operator, please review the following:
40: - Higher availability is possible of your instances are on separate machines. On Kubernetes, use Pod anti-affinitity to enforce this.
41: Use distributed caching; for multi-site clusters, use external caching for cluster members to share the same state. For details on the relevant configuration, see Configuring distributed caches. The embedded Infinispan cache has horizontal scaling considerations including:
42: - Your instances need a way to discover each other. For more information, see discovery in Configuring distributed caches.
43: - This cache is not optimal for clusters that span multiple availability zones, which are also called stretch clusters. For embedded Infinispan cache, work to have all instances in one availability zone. The goal is to avoid unnecessary round-trips in the communication that would amplify in the response times. On Kubernetes, use Pod affinity to enforce this grouping of Pods.
44: - This cache does not gracefully handle multiple members joining or leaving concurrently. In particular, members leaving at the same time can lead to data loss. On Kubernetes, use a StatefulSet with the default serial handling to ensure Pods are started and stopped sequentially, using a deployment is not supported or recommended.
45: To avoid losing service availability when a whole site is unavailable, see the high availability guide for more information on a multi-site deployment. See Multi-site deployments.
46: 2.2.1. Horizontal Autoscaling
47: Horizontal autoscaling allows for addin

## ASSISTANT-REASONING
Now I have comprehensive grounding. Let me also verify there's a wiki page I should reference and possibly there's an existing question/page on this topic. Let me check the index.keycloak.md and the rhbk-oscp-scaling-resources page, plus the questions/ dir for any existing related page.

Actually, I have enough to write a strong answer. Let me also quickly check the deploy-keycloak-kubernetes reference to see the exact 1000 example context and the additionalOptions, and the env var form. But I think I have enough.

Let me now formulate the answer per the GATE contract.

GATE:
- The question describes "RHBK caps its request queue at 1000 by default". The token for the request-queue cap is `http-max-queued-requests`. 
  - TOKEN: `http-max-queued-requests`
  - VERBATIM_MATCH: yes (it appears verbatim many times)
  - VERDICT: EXISTS
- But the PREMISE that the *default* is 1000 is false. The corpus explicitly says: "By default, there is no limit set" and "By default, Red Hat build of Keycloak will queue all incoming requests infinitely." The `1000` value appears only as an illustrative example (workload: ~200 req/s × 5s = 1000; and as a sample `value: "1000"` in a kubernetes deploy snippet).

So the answer's "what are we missing" has two layers:
1. The default cap is NOT 1000 — it's unlimited. So if they never set `http-max-queued-requests`, the queue grows without bound and itself uses Pod memory ("This will use additional memory in the Pod"). That alone can cause OOM. The 503 load-shedding never triggers because there is no limit. This is the most likely "missing" piece.
2. Even IF the queue is capped at 1000, the request queue is only one memory dimension. A login storm still consumes memory through:
   - In-flight request processing by the Quarkus executor pool (`http-pool-max-threads`, default up to 50+ threads). Each thread consumes memory; container memory limits must allow or Pod is killed.
   - Database connection pool (`db-pool-max-size` etc.). Under storm, threads queue for DB connections; "Unable to acquire JDBC Connection" after 5s, 5xx to caller — but contention/congestion increases response times and memory.
   - Authentication sessions in distributed caches (Infinispan) — many concurrent logins = many auth sessions in heap.
   - Worker threads exceeding CPU limit → throttling → congestion → more memory → unstable → OOM. The sizing guide warns performance dropped significantly when Pods were throttled.
   - Heap sizing: container uses 70% of memory limit for heap; ~300 MB non-heap. If memory limit too low, heap small → OOM under storm. If memory limit unset, heap grows to 70% of total container memory and isn't returned to OS easily.
   - Readiness probe can block on DB check under load → Pod non-ready → but internal queue still grows.

And the getting-started guidance: under OOM, take a heap dump to find the contributor; "Excessive response times may also indicate the HTTP work queue is too large and tuning for load shedding would be better than simply providing more memory."

So the practical "what are we missing":
- Set `http-max-queued-requests` explicitly (it is NOT 1000 by default — default is unlimited). This is the #1 miss.
- But don't rely on it alone; cap the executor pool (`http-pool-max-threads`) to your CPU limit to avoid throttling/congestion, size the DB pool, set a proper container memory limit, and load-shed at the LB too.
- Diagnose the actual footprint with a heap dump rather than just adding memory.

Now the references section required: two-group References (RH ground-truth + Wiki/web:). And file the answer as questions/<slug>.md with full frontmatter, status: draft, banner rules.

Let me determine banner rules. The answer is grounded in the corpus (extractive), so banners: I should include a banner like "This answer is grounded in RH documentation." Since the wikikb ask returned confident: true but thin: false, though it was extractive. I'll set banners appropriately. The CLAUDE.md banner rules: 

## ASSISTANT
Now I have the full grounding. Let me check the `CLAUDE.md` spec for the `questions/` page frontmatter + banner rules, and glance at the existing `rhbk-oscp-scaling-resources` wiki page for cross-linking.

## TOOL read({"filePath": "/Users/guylavian/Downloads/skills/llm-wiki/CLAUDE.md"})
### OUTPUT
<path>/Users/guylavian/Downloads/skills/llm-wiki/CLAUDE.md</path>
<type>file</type>
<content>
1: # Keycloak/RHBK LLM Wiki — Schema & Operating Manual
2: 
3: This directory is an **LLM-maintained knowledge wiki** layered on top of the
4: immutable raw tiers inside the vault (`reference/<domain>/`, `_sources/<domain>/`) and `references/` (in-vault). It follows Andrej
5: Karpathy's "LLM Wiki" pattern: raw sources stay frozen, the wiki is the
6: *compiled, cross-linked synthesis* that compounds across sessions, and this file
7: is the schema that tells you how to read and grow it.
8: 
9: > **Read this file first** whenever you are asked to ingest a source, answer a
10: > question against the wiki, or lint it.
11: 
12: ---
13: 
14: ## The three layers
15: 
16: | Layer | Location | Mutability | Role |
17: |---|---|---|---|
18: | **Raw sources** (in-vault) | `reference/<domain>/` (imported doc bodies, one note per source), `_sources/<domain>/` (hand notes), `references/` (in-vault) | **IMMUTABLE** — never edit these notes | Ground truth per domain. Keycloak: **800 doc bodies as reference notes** in `reference/keycloak/` + a gated-KB pointer index; 12 curated reference guides. (Original harvest archived at `../corpora.bak/`.) |
19: | **Synthesis** | `wiki/{topics,entities,questions}/` | LLM-maintained | Distilled topic/entity pages + answered questions, all cross-linked, all carry `domain:` |
20: | **Schema** | this `CLAUDE.md` | Human + LLM | Conventions and the ingest / query / lint workflows |
21: 
22: **Hard rule:** writes go *only* to the synthesis layer of this vault. **Obsidian/the vault rules all the
23: data** — there is no external corpus or query tool. Within `wiki/`, the synthesis
24: layer (`topics/ entities/ questions/`) is LLM-maintained, but the raw tiers —
25: `reference/<domain>/` (imported doc bodies) and `_sources/<domain>/` (hand notes) —
26: are **immutable** (never edit them), as is `references/` (in-vault). The raw layer is
27: regenerable from a harvest; the synthesis is downstream of it.
28: 
29: ---
30: 
31: ## Directory layout
32: 
33: ```
34: <repo-root>/  ← the Obsidian vault root IS the repo root (open it in Obsidian); rules ALL the data
35:     ├── CLAUDE.md           # this schema (single source of truth for the operations)
36:     ├── SKILL.md · AGENTS.md # skill trigger manifest + agent bootstrap pointer
37:     ├── references/         # curated reference guides (ref: tier — in-vault since 2026-07-07)
38:     ├── index.md            # global router → links per-domain indexes + cross-domain MOCs
39:     ├── index.<domain>.md   # per-domain routing index (titles + summaries); generated by index.py
40:     ├── topics/             # synthesis pages per theme  (e.g. ldap-user-federation.md)
41:     ├── entities/           # one page per concrete thing: feature, config option, CLI flag, SPI
42:     ├── questions/          # answered queries, filed back as durable pages
43:     ├── reference/<domain>/ # IMMUTABLE imported doc bodies, one Markdown note per source + _gated-kb-index.md
44:     ├── _sources/<domain>/  # raw hand-written note staging (notes-first domains)
45:     └── _meta/              # tooling — NOT content (excluded from all scanners)
46:         ├── pyproject.toml  #   package metadata + ruff/pytest config (NO pip install required)
47:         ├── .manifest.json  #   delta manifest: ingested sources → pages
48:         ├── taxonomy.md     #   controlled vocab: domains, areas, kinds, versions
49:         ├── eval/           #   eval + gate cases + committed goldens (cases.jsonl, baseline.eval*.out)
50:         ├── wikikb/         #   the toolchain PACKAGE — grouped into concern subpackages
51:         │   ├── __init__.py · __main__.py   #   package + `python3 -m wikikb <tool>` dispatcher (layout-independent CLI)
52:         │   ├── paths.py        #   single home for project paths (WIKI/REF/META/EVAL) — no per-file __file__ math
53:         │   ├── retrieval/      #   kb · route · expand · embed   (search, routing, graph-expand, optional dense)
54:         │   ├── build/          #   index · manifest · crosslink · tags · backfill   (wiki build & maintenance)
55:         │   ├── corpus/         #   corpus_to_vault · docs_to_corpus · adoc_to_corpus · pdf_to_corpus · migrate_native   (corpus ingestion/migration)
56:         │   ├── quality/        #   lint (+ Confidence gate) · coverage (tiers-covered/H1) · evaluate (recall+cost scoreboard)
57:         │   ├── online/         #   cost · llm   (OPTIONAL token/$/latency + local-first LiteLLM gateway)
58:         │   ├── graph/          #   OPTIONAL LangGraph QUERY/INGEST StateGraphs (nodes/query_graph/ingest_graph)
59:         │   └── tkg/            #   temporal + cross-domain knowledge graph: model · store · versions · tkg (CLI)
60:         └── tests/          #   selftest.py + gate_probe.py + gate_page_probe.py + cost_probe.py + conftest.py
61: ```
62: 
63: > **Running the tools (no install):** the toolchain is the importable package `wikikb` under
64: > `_meta/`. Run a tool with the dispatcher **`python3 -m wikikb <tool> …`** (e.g. `python3 -m wikikb
65: > kb --domain keycloak search "…"`) **from `_meta/`** (or anywhere with `PYTHONPATH=<repo>/_meta`).
66: > The dispatcher keeps the CLI stable regardless of which subpackage a tool lives in; the direct form
67: > `python3 -m wikikb.<group>.<tool>` (e.g. `wikikb.retrieval.kb`) also works. After any batch of page
68: > writes, **`python3 -m wikikb build`** runs the whole regen chain in one verb (tags normalize/backfill
69: > → crosslink --apply → index → tkg ingest → lint) so the routing index can't silently go stale. Run
70: > the tests with `python3 _meta/tests/selftest.py`. No `pip install` is needed — the air-gap "copy-and-run" model
71: > is preserved (`pip install -e .` from `_meta/` is an OPTIONAL convenience that adds `wikikb-<tool>`
72: > console commands).
73: 
74: - **topics/** — broad, multi-source syntheses. "How LDAP federation works end to e

## ASSISTANT-REASONING
Now I have the full protocol. Let me check the taxonomy to confirm keycloak's tiers-covered, so I set the question_tier correctly and banner. The question is a support-kb / break-fix scenario. Let me check tiers-covered for keycloak.

Actually, the wikikb ask returned `confident: true` and `thin: false`, and tier was support-kb. The domain keycloak — let me check if support-kb is in tiers-covered. If not, I need an H1 banner. But this answer is extractive (grounded in corpus). Let me check the taxonomy quickly.

Actually, the instruction says the question is a "support-kb" tier. Let me check _meta/taxonomy.md. But also, I can set `question_tier: support-kb` and add the banner if needed. Let me read taxonomy for keycloak tiers-covered.

Actually, I recall keycloak's tiers-covered likely includes conceptual, support-kb, scenarios. Let me verify quickly. Also I want the existing `rhbk-oscp-scaling-resources` wiki page for cross-linking. Let me read both.

Let me check taxonomy and the wiki page.

## ASSISTANT
Let me verify the domain's `tiers-covered` (for the banner) and read the existing scaling wiki page to cross-link.

## TOOL bash({"command": "grep -n -A6 \"domain: keycloak\" /Users/guylavian/Downloads/skills/llm-wiki/_meta/taxonomy.md | head -40"})
### OUTPUT
100:- domain: keycloak
101-- areas: [realm, authn, authz, clients, tokens, federation, brokering, users, operator, ha, observability, server-config, migration, spi, iac, security, troubleshooting]
102-- shape: corpus-backed
103-- sources: [corpora/keycloak/, _sources/keycloak/]
104-- review-moc: sso-implementation-review
105-- tiers-covered: [conceptual, support-kb]   # product guides + RH KB Solution notes (documentKind: Solution)
106-


## TOOL read({"filePath": "/Users/guylavian/Downloads/skills/llm-wiki/wiki/rhbk-oscp-scaling-resources.md"})
### OUTPUT


## ASSISTANT-REASONING
So keycloak's `tiers-covered: [conceptual, support-kb]`. The question is `support-kb` tier, which IS covered. So no H1 banner needed. Good. The wiki pages are probably under `wiki/topics/` etc., not `wiki/` root. Let me find the actual location of the wiki synthesis pages. The glob earlier for reference was `reference/keycloak/*.md`. The wiki synthesis pages are under `wiki/`. Let me check.

Actually the `rhbk-oscp-scaling-resources` slug appeared in the `ask` Wiki list. Let me find it.

## TOOL bash({"command": "ls /Users/guylavian/Downloads/skills/llm-wiki/wiki/ 2>/dev/null; echo \"---questions---\"; ls /Users/guylavian/Downloads/skills/llm-wiki/wiki/questions/ 2>/dev/null | head; echo \"---find scaling page---\"; find /Users/guylavian/Downloads/skills/llm-wiki/wiki -name \"rhbk-oscp-scaling-r)
### OUTPUT
questions
---questions---
ad-maximum-limits.md
ad-recycle-bin-enable-when.md
kc-sh-fips-enforcement-level.md
new-adfinegrainedpasswordpolicysilo.md
security-admin-console-confidential-lockout.md
vlan-trunking-ios-xe.md
windows-dc-locator.md
---find scaling page---


## ASSISTANT-REASONING
The wiki synthesis layer only has `questions/` populated so far (no topics/entities yet apparently). The `rhbk-oscp-scaling-resources` slug isn't a file — it was a wiki link candidate from the ask tool but the page may not exist (wanted page). Let me just create the question page.

Now let me write the question page under `wiki/questions/`. Slug: `rhbk-login-storm-oom-queue-cap`. Let me name it `rhbk-login-storm-oom-missing-queue-cap`.

Let me craft the answer following the protocol:

GATE block first (per the system prompt's required output contract). Wait — the system prompt at the top is the GATE for token-based questions. The question names a token: "RHBK caps its request queue at 1000 by default". The relevant token is `http-max-queued-requests`. Let me run the GATE per the system prompt.

Actually the system prompt's OUTPUT CONTRACT requires I output the GATE block (TOKEN, VERBATIM_MATCH, VERDICT) at the very start. So I must include that. Let me do it.

TOKEN: The token the question asks about. The question references "request queue" capped "at 1000 by default". The actual config option is `http-max-queued-requests`. The question does NOT name it verbatim, but it's describing that option. Per the GATE, I should identify the token being asked about. The token is `http-max-queued-requests`. It appears verbatim in the corpus → VERDICT = EXISTS.

But the default-value claim "1000 by default" is false. The token EXISTS but its stated default is wrong. I'll handle this in the answer: the option exists, but the default is unlimited, not 1000.

Hmm, but the GATE is about whether the TOKEN exists. `http-max-queued-requests` exists. So VERDICT = EXISTS. Then under EXISTS I answer normally citing where it appears, including its documented default/behavior. The documented default is "no limit set" / "queue all incoming requests infinitely". I must state that.

So the GATE block:
TOKEN: http-max-queued-requests
VERBATIM_MATCH: yes
VERDICT: EXISTS

Then answer. But the user's framing "caps at 1000 by default" is a false premise. Per the answering protocol point 3: "Distinguish what was asked from the actual correct approach. If the question embeds a false premise... give the actual correct way." So I explain the option exists but default is unlimited, and then the deeper "what are we missing."

Now, the answer. Let me structure:

1. GATE block.
2. The premise correction: `http-max-queued-requests` exists, but by default there is NO limit (infinite queue). The 1000 is only an example. So if they believe the default protects them, that belief is the gap.
3. Even with the queue capped, a login storm drives OOM through other memory dimensions:
   - Quarkus executor pool (`http-pool-max-threads`, default max 50+ threads). Each thread consumes memory; container limits must allow or Pod killed.
   - DB connection pool (`db-pool-max-size` etc.) exhaustion under storm → congestion → more memory.
   - Auth sessions in Infinispan caches (heap).
   - CPU-limit throttling → congestion → memory blowup (sizing guide warns perf dropped significantly when throttled).
   - Heap sizing: 70% of memory limit for heap, ~300 MB non-heap. If memory limit too low or unset.
   - Readiness probe blocks under load → Pod non-ready but internal queue still grows.
4. The guidance: under OOM, take a heap dump to find the contributor; tuning load shedding (queue cap) is better than throwing memory at it. Set the queue cap explicitly, cap threads to CPU, size DB pool, set memory limit, load-shed at LB.

Let me gather the precise line citations:
- `http-max-queued-requests` default unlimited: rhbk-26-2-configuration-production.md:36-39 ("By default, there is no limit set"). And rhbk-26-2-concepts-threads.md:36 ("By default, Red Hat build of Keycloak will queue all incoming requests infinitely"). 
- 503 on exceed: rhbk-26-2-concepts-threads.md:39.
- 1000 example: rhbk-26-2-concepts-threads.md:38 ("a queue of 1000 would lead to maximum waiting times of around 5 seconds"

## ASSISTANT
I have everything needed. Key finding: the option `http-max-queued-requests` **exists**, but its documented **default is unlimited** — the `1000` in the question is only an example value, not the default. That's the central "missing" piece. Let me file the answer page.

## TOOL write({"filePath": "/Users/guylavian/Downloads/skills/llm-wiki/wiki/questions/rhbk-login-storm-oom-queue-cap.md", "content": "---\ntitle: \"RHBK login storm OOMed despite the request-queue cap \u2014 what was missing\"\ntype: question\ndomain: keycloak\nslug: rhbk-login-storm-oom-queue-cap\nsummary: >\n  )
### OUTPUT
Wrote file successfully.

## ASSISTANT-REASONING
Now let me present the answer to the user. The response should include the GATE block at the top (OUTPUT CONTRACT), the answer, the two-group References, and a short chat summary per protocol point 7.

Let me write the final response.

## ASSISTANT
## GATE

```
TOKEN: http-max-queued-requests
VERBATIM_MATCH: yes
VERDICT: EXISTS
```

The token exists verbatim in the corpus — but the question's *premise* ("RHBK caps its request queue at 1000 by default") is false. The documented default is **no limit at all**; `1000` is only an example value. That false assumption is the first thing you're missing.

---

## What you're missing

**1. There is no default queue cap — the queue is infinite by default.**
RHBK documents this explicitly: *"By default, there is no limit set. Set the option `http-max-queued-requests` … Any request that exceeds this limit would return with an immediate 503"* (`rhbk-26-2-configuration-production.md:36-39`); and *"By default, Red Hat build of Keycloak will queue all incoming requests infinitely"* (`rhbk-26-2-concepts-threads.md:36`).

The `1000` you remember appears **only as an illustration**: a workload of ~200 req/s × 5 s ≈ 1000 (`rhbk-26-2-concepts-threads.md:38`), and as a sample `value: "1000"` in a k8s snippet (`rhbk-26-0-deploy-keycloak-kubernetes.md:37`). So if you believed a "default 1000 cap" was protecting you, **it never was active** — the queue grew unbounded during the storm, and the docs warn *"this will use additional memory in the Pod"* (`rhbk-26-2-concepts-threads.md:36`), driving the OOM directly. The 503 shedding only triggers once `http-max-queued-requests` is set explicitly.

**2. Even with the queue capped, a login storm OOMs through other memory dimensions** (none addressed by the queue cap):
- **Executor pool (`http-pool-max-threads`)** — each worker thread consumes memory, and *"the container memory limits need to be set to a value that allows for this or the Pod will be killed by Kubernetes"* (`rhbk-26-2-concepts-threads.md:24-27,43-45`). Mismatched thread count vs CPU limit → throttling → congestion → more memory.
- **DB connection pool (`db-pool-max-size` etc.)** — under a storm threads queue for a connection and fail with *"Unable to acquire JDBC Connection"* after 5 s (`rhbk-26-2-concepts-threads.md:28-34`); the pool is *"often exhausted, and there are threads queuing for a connection"* (`rhbk-26-2-metrics-for-troubleshooting.md:25`).
- **Authentication sessions** held in the Infinispan caches (`rhbk-26-2-concepts-memory-and-cpu-sizing.md:117`) spike with concurrent logins.
- **CPU throttling** — *"Performance … dropped significantly when its Pods were throttled"*; 150% CPU head-room is recommended (`rhbk-26-2-concepts-memory-and-cpu-sizing.md:35`).
- **Heap floor** — 70% of the memory limit to heap + ~300 MB non-heap (`rhbk-26-2-containers.md:216-234`); an unset/low limit tips it over, and unset heaps *"are returned to the OS reluctantly"*.
- **Readiness probe blocks under load** → Pod goes non-ready while the internal (unbounded) queue keeps growing (`rhbk-26-2-concepts-threads.md:40-42`).

**3. The fixes you're missing:** set `http-max-queued-requests` explicitly (and at the LB); cap `http-pool-max-threads` to your CPU limit with 150% head-room; right-size `db-pool-max-size`; set a real container memory limit; and **diagnose with a heap dump before throwing RAM at it** — *"Excessive response times may also indicate the HTTP work queue is too large and tuning for load shedding would be better than simply providing more memory"* (`rhbk-26-2-getting-started-scaling-and-tuning.md:27`).

*(Inferred: the prime suspect is that the queue cap was never actually set, since the default is unlimited; if it was set, look next at thread-count-vs-CPU throttling and DB-pool exhaustion. Separate security path: CVE-2025-2559 unbounded JWT token caching — `rhbk-26-0-red-hat-build-of-keycloak-26-0.md:52`.)*

---

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)
- `kb:rhbk-26-2-concepts-threads` — Concepts for configuring thread pools (HA Guide 26.2), §5.1.2–5.1.5
- `kb:rhbk-26-2-configuration-production` — Configuring RHBK for production (Server Config Guide 26.2), §2.4
- `kb:rhbk-26-2-concepts-memory-and-cpu-sizing` — Concepts for sizing CPU and memory (HA Guide 26.2), §6.1
- `kb:rhbk-26-2-getting-started-scaling-and-tuning` — Scaling (Getting Started Guide 26.2), §2.1
- `kb:rhbk-26-2-containers` — Container heap percentages
- `kb:rhbk-26-0-deploy-keycloak-kubernetes` — example `http-max-queued-requests` value `"1000"`
- `kb:rhbk-26-0-red-hat-build-of-keycloak-26-0` — CVE-2025-2559 JWT token cache exhaustion
- `kb:rhbk-26-2-metrics-for-troubleshooting` — DB connection pool exhaustion metric

### Wiki
- Newly filed: [[rhbk-login-storm-oom-queue-cap]] (this answer)
- Wanted (not yet written): [[rhbk-oscp-scaling-resources]], [[sso-implementation-review]]
- No pre-existing synthesis page was used; the answer was derived directly from the `reference/keycloak/` ground-truth tier.

---

**Chat summary:** Filed as `wiki/questions/rhbk-login-storm-oom-queue-cap.md` (`status: draft`). The request-queue cap `http-max-queued-requests` exists, but its **default is unlimited** — the "1000" is only an example — so an unconfigured cluster never sheds load and the unbounded queue itself eats Pod memory. A login storm also OOMs via executor threads, the DB pool, auth-session caches, and CPU throttling. Cite: `rhbk-26-2-concepts-threads.md:36`, `rhbk-26-2-configuration-production.md:36-39`, `rhbk-26-2-getting-started-scaling-and-tuning.md:27`.