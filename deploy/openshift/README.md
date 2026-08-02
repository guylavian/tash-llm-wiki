# llm-wiki MCP server on OpenShift — operator runbook

Four flat manifests + a Containerfile. No kustomization.yaml — with one Deployment/Service/Route/
Secret and a single environment, an overlay tool has nothing to reduce; `oc apply -f deploy/openshift/`
applies the lot directly. No Helm chart for the same reason (one release, no parameterization that
earns templating).

**Architecture (given, not relitigated here):** the vault is baked into the image — read-only at
query time, versioned in git. Content updates ship as a new image tag, never a live write to a
mounted volume. No RWX PVC, no S3, no sidecar data pod.

## Files

| File | What |
|---|---|
| `Containerfile` | slim serving image, `lexical` (default) or `dense` build target |
| `deployment.yaml` | Deployment, 2 replicas, restricted-v2-safe, probes on `/health` |
| `service.yaml` | ClusterIP Service, port 8642 |
| `route.yaml` | edge-TLS Route, `haproxy.router.openshift.io/timeout: 60s` |
| `secret.example.yaml` | **example only** — real creation is one `oc create secret` command |

## 1. Build

From the repo root (build context matters — the Containerfile does explicit `COPY <path>` lines,
not `COPY .`):

```bash
# lexical (default) — zero pip installs, ~215MB content layer
docker build -f deploy/openshift/Containerfile -t llm-wiki-mcp:v0.1.0 .

# dense — + vendored embedding model/index + numpy/sentence-transformers/torch-cpu (~700MB+ of wheels)
docker build -f deploy/openshift/Containerfile --target dense -t llm-wiki-mcp:v0.1.0-dense .
```

Tag with something you can trace back to a vault state — a git tag (see §4), not `:latest`.

## 2. Push to the OpenShift internal registry

If the cluster hasn't exposed its internal registry externally yet (one-time, cluster-admin):

```bash
oc patch configs.imageregistry.operator.openshift.io/cluster \
  --patch '{"spec":{"defaultRoute":true}}' --type=merge
```

Then, from a machine with `docker`/`podman` and `oc` (this dev machine has `docker` but neither
`podman` nor `oc` — see the Verification section):

```bash
REGISTRY=$(oc registry info)                        # e.g. default-route-openshift-image-registry.apps.<cluster>
oc registry login                                    # or: podman login -u kubeadmin -p $(oc whoami -t) $REGISTRY
docker tag llm-wiki-mcp:v0.1.0 $REGISTRY/<namespace>/llm-wiki-mcp:v0.1.0
docker push $REGISTRY/<namespace>/llm-wiki-mcp:v0.1.0
```

**Cluster-native alternative** (no local docker/podman needed — lets the cluster's own Buildah do the
build from this same Containerfile):

```bash
oc new-build --binary --name=llm-wiki-mcp --strategy=docker -n <namespace>
# BuildConfig defaults to a Dockerfile at the repo root; point it at this one:
oc patch bc/llm-wiki-mcp -p \
  '{"spec":{"strategy":{"dockerStrategy":{"dockerfilePath":"deploy/openshift/Containerfile"}}}}'
oc start-build llm-wiki-mcp --from-dir=. --follow -n <namespace>
```

## 3. Deploy

```bash
oc project <namespace>

# real secret creation (never the placeholder in secret.example.yaml):
oc create secret generic llm-wiki-mcp-token --from-literal=token="$(openssl rand -hex 32)"

oc apply -f deploy/openshift/deployment.yaml   # edit the `image:` field first to your pushed tag
oc apply -f deploy/openshift/service.yaml
oc apply -f deploy/openshift/route.yaml

oc rollout status deployment/llm-wiki-mcp
oc get route llm-wiki-mcp -o jsonpath='{.spec.host}{"\n"}'
```

## 4. Roll out a content update

The vault is baked in, so a content change is a new image, never a live write:

```bash
git tag v2026-08-01                     # tag the vault state you're shipping
git push origin v2026-08-01

git checkout v2026-08-01
docker build -f deploy/openshift/Containerfile -t $REGISTRY/<namespace>/llm-wiki-mcp:v2026-08-01 .
docker push $REGISTRY/<namespace>/llm-wiki-mcp:v2026-08-01

oc set image deployment/llm-wiki-mcp \
  llm-wiki-mcp=$REGISTRY/<namespace>/llm-wiki-mcp:v2026-08-01
oc rollout status deployment/llm-wiki-mcp
```

`oc set image` triggers a normal rolling update — both replicas are stateless (the server never
issues an `Mcp-Session-Id`; see `mcp.py`), so there's no draining/affinity concern during the roll.

## 5. Rollback

```bash
oc rollout history deployment/llm-wiki-mcp          # list revisions
oc rollout undo deployment/llm-wiki-mcp             # back to the previous revision
oc rollout undo deployment/llm-wiki-mcp --to-revision=N
```

## 6. Verify

```bash
oc get pods -l app=llm-wiki-mcp
oc logs deployment/llm-wiki-mcp

ROUTE=$(oc get route llm-wiki-mcp -o jsonpath='{.spec.host}')
TOKEN=$(oc get secret llm-wiki-mcp-token -o jsonpath='{.data.token}' | base64 -d)   # -D on macOS

curl -s https://$ROUTE/health                                                       # no auth needed
curl -s -H "Authorization: Bearer $TOKEN" "https://$ROUTE/route?q=ldap+federation"
curl -s -H "Authorization: Bearer $TOKEN" -X POST https://$ROUTE/mcp \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

Unauthenticated non-`/health` calls should 401; a bad/missing token on `POST /mcp` should also 401;
`GET /mcp` and `DELETE /mcp` should both 405 (spec-legal declines, not errors — see `route.yaml`'s
comment and `serve.py`'s docstring).

This session verified the equivalent behavior locally (no `docker`/`oc` build, per the task's
instruction not to run one — see the task's own Verification block for the exact commands and
output): `/health` 200 without a token; `/route`, `/search`, `/mcp` 401 without a token and 200 with
the correct one; `GET /mcp` and `DELETE /mcp` 405; `POST /mcp` with an `Origin` header not in the
(default-empty) allowlist 403; `initialize` / `tools/list` / `tools/call` / `notifications/initialized`
(202, empty body) all round-tripping correctly.

**Image build + container smoke test — done 2026-08-02.** `docker build -f
deploy/openshift/Containerfile -t llm-wiki-mcp:v0.1.0 .` from the vault root succeeds (526 MB,
`lexical` target). The image was then run under this Deployment's actual security posture —
`--user 1000670000:0` (an arbitrary UID, as `restricted-v2`'s `MustRunAsRange` injects),
`--read-only`, `--cap-drop ALL` — and passed: `/health` 200 unauthenticated with all 9 domains
resident; 401 without a token and 200 with it; legacy `initialize` negotiating `2025-11-25`; modern
`server/discover`; a header/body mismatch rejected 400; and a real `ask` tool call returning a
gated, banner-carrying answer. This closes the "never built, never run" gap the paragraph above
described. It does **not** cover `oc`/OpenShift admission itself — no cluster was available here.

## 7. Point n8n's MCP Client Tool at this Route

Deep-research RESEARCH 1/2 (this repo, 2026-07-27) grounds every choice below.

1. **Node & transport.** Use n8n's built-in **MCP Client Tool** (`n8n-nodes-langchain.toolmcp`, or
   the standalone **MCP Client** node for calling it outside an AI Agent — both share the same
   transport/auth code per RESEARCH 1). Set **Transport = HTTP Streamable** (`httpStreamable`). There
   is an open, unresolved n8n bug (#24967) where the transport dropdown can silently desync from what
   the node actually sends (falls back to raw SSE `GET`s and can retry-storm) — **force it via an
   Expression** (`={{ "httpStreamable" }}`) rather than trusting the dropdown selection, per RESEARCH
   1's finding, and restart the n8n instance after.
2. **URL.** `https://<route-host>/mcp` — the exact path this server implements (`POST /mcp`; `GET`/
   `DELETE /mcp` both 405, which the reference MCP TypeScript SDK — what n8n is built on — treats as
   an expected non-error per RESEARCH 2, not a failure).
3. **Auth.** Credential type **Bearer Auth** (`httpBearerAuth`) — RESEARCH 1: "Bearer Auth is
   implemented as Header auth with `Authorization: Bearer <token>`", which is exactly what this
   server's `_check_auth()` expects. Paste the value from `oc get secret llm-wiki-mcp-token
   -o jsonpath='{.data.token}' | base64 -d` into the credential.
4. **Tool scoping.** If you restrict "Tools to Include" to a subset (e.g. `ask`+`search` only) instead
   of `All`, RESEARCH 1 flags an open n8n bug (#23421) where the Bearer token is sometimes NOT sent on
   tool-call requests in that mode — verify with a live call before relying on scoped tool access in
   production; it fails closed here (401), not open, since this server has no default-allow path.
5. **Sessions.** Nothing to configure — this server never issues an `Mcp-Session-Id` (deliberate,
   spec-legal "stateless mode" per RESEARCH 2), which matches n8n's own client behavior (RESEARCH 1/2:
   n8n's node "seems to send each request in a stateless manner" today regardless).
6. **Origin.** n8n's node is a backend HTTP client, not a browser, so it won't send an `Origin` header
   — this server's default (deny only a *present* Origin not in an empty allowlist) never affects it.
   Leave `WIKIKB_MCP_ALLOWED_ORIGINS` unset unless you add a browser-based caller later.
7. **Route timeout.** `route.yaml` sets `haproxy.router.openshift.io/timeout: 60s` (justified in that
   file's comment). If calls still time out under load, also check the cluster's IngressController-
   wide `tuningOptions.clientTimeout` (cluster-admin, default 30s) — a per-Route annotation can't
   override a shorter cluster-wide client timeout (RESEARCH 1).
8. **Tool schemas.** This server's four tools (`ask`/`search`/`route`/`read_page`) use flat JSON
   Schemas — no `$ref`/`$defs`/`oneOf` — which sidesteps n8n's known schema-to-Zod conversion bugs
   (#25964, #15603) that silently corrupt nested schemas (RESEARCH 1). No change needed; noted so a
   future tool addition keeps this property.

## 8. MCP protocol eras — why n8n keeps working, and what changes when it upgrades

MCP revision **2026-07-28** is a breaking split, and the spec names the two halves
(`basic/versioning#terminology`):

- **Legacy** (`2025-11-25` and earlier) — a session opened by an `initialize` handshake. This is
  what n8n's bundled TypeScript SDK and Claude Code send **today**.
- **Modern** (`2026-07-28`+) — no handshake at all. Version, client identity and capabilities ride
  in each request's `_meta`, mirrored into required `MCP-Protocol-Version` / `Mcp-Method` /
  `Mcp-Name` HTTP headers. The GET SSE stream and protocol-level sessions were **removed**.

The spec's compatibility matrix is blunt: **"Modern client / Legacy server: Fails."** So as of
2026-08-02 this server is **dual-era** — it reads the era off each request (presence of
`params._meta["io.modelcontextprotocol/protocolVersion"]`) and never from connection state:

| Request | Path |
|---|---|
| no modern `_meta` | the original legacy code, byte-for-byte unchanged — **nothing about today's n8n wiring changes** |
| modern `_meta` | `server/discover` (a MUST for modern servers), `resultType: "complete"`, `_meta.serverInfo`, header↔body validation → 400 `-32020`, unknown version → 400 `-32022` with the supported list, missing required `_meta` → 400 `-32602`, unknown method → **404** `-32601` |

Two things this deployment already did are now *mandated* rather than merely permitted: `GET`/
`DELETE /mcp` → 405, and never minting or echoing an `Mcp-Session-Id`. §7's guidance is unaffected —
keep `httpStreamable`, keep the Bearer credential. When n8n's SDK moves to the modern era, it will
start sending the new headers and this server will simply answer in that era; no config change here.

`selftest.py` #81 pins both eras in one server start, including a `legacy_no_resulttype` assertion
whose only job is to catch the modern envelope leaking into the legacy path — the failure mode that
would break the real consumer while every modern check still passed.

## Known limitation (by design)

`PUT /upload` (opt-in `--allow-upload`, not passed in this Deployment's CMD) and `ask ... file_back`
both need a writable vault mount. Neither is used here — the baked-in-image architecture means a
content contribution goes through git + a new image build (§4), not a live write to a read-only pod.
Calling `file_back: true` against this deployment will error (read-only filesystem); that's expected.

## Housekeeping

`_meta/Dockerfile` and `_meta/docker-compose.yml` build a Kuzu TKG backend that was **removed** from
the codebase 2026-07-05 (`graphiti_backend.py` is gone; `selftest.py` asserts it stays gone). They are
dead and should be deleted — left in place per this task's instructions, not touched here.
