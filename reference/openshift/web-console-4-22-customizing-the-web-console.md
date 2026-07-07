---
title: "Customizing the web console in {product-title}"
type: reference
domain: openshift
slug: web-console-4-22-customizing-the-web-console
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/customizing-the-web-console
version: 4.22
family: web_console
documentKind: "Documentation"
---

# Customizing the web console in {product-title}

[id="customizing-web-console"]
= Customizing the web console in OpenShift Container Platform

[role="_abstract"]
You can customize the
OpenShift Container Platform
OpenShift Container Platform
web console to set
a custom logo, product name, links, notifications, and command-line downloads.
a custom logo and product name.
This is especially helpful if you need to tailor the web console to meet specific corporate or government requirements.

// Module included in the following assemblies:
//
// * web_console/customizing-the-web-console.adoc

[id="adding-a-custom-logo_{context}"]
= Adding a custom logo and product name

[role="_abstract"]
You can create custom branding by adding a custom logo or custom product name. You can set both or one without the other, as these settings are independent of each other.

.Prerequisites

* You must have administrator privileges.
* Create a file of the logo that you want to use. The logo can be a file in any common image format, including GIF, JPG, PNG, or SVG, and is constrained to a `max-height` of `60px`. Image size must not exceed 1 MB due to constraints on the `ConfigMap` object size.

.Procedure

. Import your logo file into a config map in the `openshift-config` namespace:
+
[source,terminal]
----
$ oc create configmap console-custom-logo --from-file /path/to/console-custom-logo.png -n openshift-config
----
+
[TIP]
====
You can alternatively apply the following YAML to create the config map:

[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: console-custom-logo
  namespace: openshift-config
binaryData:
  console-custom-logo.png: <base64-encoded_logo> ...
----
Replace `<base64-encoded_logo>` with a base64-encoded string of the logo.
====

. Edit the web console's Operator configuration to include `customLogoFile` and `customProductName`:
+
[source,terminal]
----
$ oc edit consoles.operator.openshift.io cluster
----
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
spec:
  customization:
    customLogoFile:
      key: console-custom-logo.png
      name: console-custom-logo
    customProductName: My Console
----
+
Once the Operator configuration is updated, it will sync the custom logo config map into the console namespace, mount it to the console pod, and redeploy.

. Check for success. If there are any issues, the console cluster Operator will report a `Degraded` status, and the console Operator configuration will also report a `CustomLogoDegraded` status, but with reasons such as `KeyOrFilenameInvalid` or `NoImageProvided`.
+
To check the `clusteroperator`, run:
+
[source,terminal]
----
$ oc get clusteroperator console -o yaml
----
+
To check the console Operator configuration, run:
+
[source,terminal]
----
$ oc get consoles.operator.openshift.io -o yaml
----

// Hiding in ROSA/OSD, as dedicated-admins cannot create resource "consolelinks"
// Module included in the following assemblies:
//
// * web_console/customizing-the-web-console.adoc

[id="creating-custom-links_{context}"]
= Creating custom links in the web console

.Prerequisites

* You must have administrator privileges.

.Procedure

. From *Administration* -> *Custom Resource Definitions*, click on
*ConsoleLink*.
. Select *Instances* tab
. Click *Create Console Link* and edit the file:
+
[source,yaml]
----
apiVersion: console.openshift.io/v1
kind: ConsoleLink
metadata:
  name: example
spec:
  href: 'https://www.example.com'
  location: HelpMenu <1>
  text: Link 1
----
<1> Valid location settings are `HelpMenu`, `UserMenu`, `ApplicationMenu`, and
`NamespaceDashboard`.
+
To make the custom link appear in all namespaces, follow this example:
+
[source,yaml]
----
apiVersion: console.openshift.io/v1
kind: ConsoleLink
metadata:
  name: namespaced-dashboard-link-for-all-namespaces
spec:
  href: 'https://www.example.com'
  location: NamespaceDashboard
  text: This appears in all namespaces
----
+
To make the custom link appear in only some namespaces, follow this example:
+
[source,yaml]
----
apiVersion: console.openshift.io/v1
kind: ConsoleLink
metadata:
  name: namespaced-dashboard-for-some-namespaces
spec:
  href: 'https://www.example.com'
  location: NamespaceDashboard
  # This text will appear in a box called "Launcher" under "namespace" or "project" in the web console
  text: Custom Link Text
  namespaceDashboard:
    namespaces:
    # for these specific namespaces
    - my-namespace
    - your-namespace
    - other-namespace
----
+
To make the custom link appear in the application menu, follow this example:
+
[source,yaml]
----
apiVersion: console.openshift.io/v1
kind: ConsoleLink
metadata:
  name: application-menu-link-1
spec:
  href: 'https://www.example.com'
  location: ApplicationMenu
  text: Link 1
  applicationMenu:
    section: My New Section
    # image that is 24x24 in size
    imageURL: https://via.placeholder.com/24
----

. Click *Save* to apply your changes.

// Hiding in ROSA/OSD, as dedicated-admins cannot patch resource "ingresses"
// Module included in the following assemblies:
//
// * web_console/customizing-the-web-console.adoc

[id="customizing-the-web-console-url_{context}"]
= Customizing console routes

For `console` and `downloads` routes, custom routes functionality uses the `ingress` config route configuration API. If the `console` custom route is set up in both the `ingress` config and `console-operator` config, then the new `ingress` config custom route configuration takes precedent. The route configuration with the `console-operator` config is deprecated.

[id="customizing-the-console-route_{context}"]
== Customizing the console route

You can customize the console route by setting the custom hostname and TLS certificate in the `spec.componentRoutes` field of the cluster `Ingress` configuration.

.Prerequisites

* You have logged in to the cluster as a user with administrative privileges.
* You have created a secret in the `openshift-config` namespace containing the TLS certificate and key. This is required if the domain for the custom hostname suffix does not match the cluster domain suffix. The secret is optional if the suffix matches.
+
[TIP]
====
You can create a TLS secret by using the `oc create secret tls` command.
====

.Procedure

. Edit the cluster `Ingress` configuration:
+
[source,terminal]
----
$ oc edit ingress.config.openshift.io cluster
----

. Set the custom hostname and optionally the serving certificate and key:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Ingress
metadata:
  name: cluster
spec:
  componentRoutes:
    - name: console
      namespace: openshift-console
      hostname: <custom_hostname> <1>
      servingCertKeyPairSecret:
        name: <secret_name> <2>
----
<1> The custom hostname.
<2> Reference to a secret in the `openshift-config` namespace that contains a TLS certificate (`tls.crt`) and key (`tls.key`). This is required if the domain for the custom hostname suffix does not match the cluster domain suffix. The secret is optional if the suffix matches.

. Save the file to apply the changes.

[NOTE]
====
Add a DNS record for the custom console route that points to the application ingress load balancer.
====

[id="customizing-the-download-route_{context}"]
== Customizing the download route

You can customize the download route by setting the custom hostname and TLS certificate in the `spec.componentRoutes` field of the cluster `Ingress` configuration.

.Prerequisites

* You have logged in to the cluster as a user with administrative privileges.
* You have created a secret in the `openshift-config` namespace containing the TLS certificate and key. This is required if the domain for the custom hostname suffix does not match the cluster domain suffix. The secret is optional if the suffix matches.
+
[TIP]
====
You can create a TLS secret by using the `oc create secret tls` command.
====

.Procedure

. Edit the cluster `Ingress` configuration:
+
[source,terminal]
----
$ oc edit ingress.config.openshift.io cluster
----

. Set the custom hostname and optionally the serving certificate and key:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Ingress
metadata:
  name: cluster
spec:
  componentRoutes:
    - name: downloads
      namespace: openshift-console
      hostname: <custom_hostname> <1>
      servingCertKeyPairSecret:
        name: <secret_name> <2>
----
<1> The custom hostname.
<2> Reference to a secret in the `openshift-config` namespace that contains a TLS certificate (`tls.crt`) and key (`tls.key`). This is required if the domain for the custom hostname suffix does not match the cluster domain suffix. The secret is optional if the suffix matches.

. Save the file to apply the changes.

[NOTE]
====
Add a DNS record for the custom downloads route that points to the application ingress load balancer.
====

// moved _Recognizing resource and project limits and quotas_ to modules/recognize-resource-limits-quotas.adoc in web-console.adoc

// Hiding in ROSA/OSD, as dedicated-admins cannot create resource "secrets" in openshift-config
// Module included in the following assemblies:
//
// * web_console/customizing-the-web-console.adoc

[id="customizing-the-login-page_{context}"]
= Customizing the login page

Create Terms of Service information with custom login pages. Custom login pages
can also be helpful if you use a third-party login provider, such as GitHub or
Google, to show users a branded page that they trust and expect before being
redirected to the authentication provider. You can also render custom error
pages during the authentication process.

[NOTE]
====
Customizing the error template is limited to identity providers (IDPs) that use redirects, such as request header and OIDC-based IDPs. It does not have an effect on IDPs that use direct password authentication, such as LDAP and htpasswd.
====

.Prerequisites

* You must have administrator privileges.

.Procedure

. Run the following commands to create templates you can modify:
+
[source,terminal]
----
$ oc adm create-login-template > login.html
----
+
[source,terminal]
----
$ oc adm create-provider-selection-template > providers.html
----
+
[source,terminal]
----
$ oc adm create-error-template > errors.html
----

. Create the secrets:
+
[source,terminal]
----
$ oc create secret generic login-template --from-file=login.html -n openshift-config
----
+
[source,terminal]
----
$ oc create secret generic providers-template --from-file=providers.html -n openshift-config
----
+
[source,terminal]
----
$ oc create secret generic error-template --from-file=errors.html -n openshift-config
----

. Run:
+
[source,terminal]
----
$ oc edit oauths cluster
----

. Update the specification:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
# ...
spec:
  templates:
    error:
        name: error-template
    login:
        name: login-template
    providerSelection:
        name: providers-template
----
+
Run `oc explain oauths.spec.templates` to understand the options.

// Hiding in ROSA/OSD, as dedicated-admins cannot create resource "consoleexternalloglinks"
// Module included in the following assemblies:
//
// * web_console/customizing-the-web-console.adoc

[id="defining-template-for-external-log-links_{context}"]
= Defining a template for an external log link

If you are connected to a service that helps you browse your logs, but you need
to generate URLs in a particular way, then you can define a template for your
link.

.Prerequisites

* You must have administrator privileges.

.Procedure

. From *Administration* -> *Custom Resource Definitions*, click on
*ConsoleExternalLogLink*.
. Select *Instances* tab
. Click *Create Console External Log Link* and edit the file:
+
[source,yaml]
----
apiVersion: console.openshift.io/v1
kind: ConsoleExternalLogLink
metadata:
  name: example
spec:
  hrefTemplate: >-
    https://example.com/logs?resourceName=${resourceName}&containerName=${containerName}&resourceNamespace=${resourceNamespace}&podLabels=${podLabels}
  text: Example Logs
----

// Hiding in ROSA/OSD, as dedicated-admins cannot create resource "consolenotifications"
// Module included in the following assemblies:
//
// * web_console/customizing-the-web-console.adoc

[id="creating-custom-notification-banners_{context}"]
= Creating custom notification banners

.Prerequisites

* You must have administrator privileges.

.Procedure

. From *Administration* -> *Custom Resource Definitions*, click on
*ConsoleNotification*.
. Select *Instances* tab
. Click *Create Console Notification* and edit the file:
+
[source,yaml]
----
apiVersion: console.openshift.io/v1
kind: ConsoleNotification
metadata:
  name: example
spec:
  text: This is an example notification message with an optional link.
  location: BannerTop <1>
  id="creating-custom-CLI-downloads_{context}"
= Customizing CLI downloads

You can configure links for downloading the CLI with custom link text and URLs,
which can point directly to file packages or to an external page that provides
the packages.

.Prerequisites

* You must have administrator privileges.

.Procedure

. Navigate to *Administration* -> *Custom Resource Definitions*.

. Select *ConsoleCLIDownload* from the list of Custom Resource Definitions (CRDs).

. Click the *YAML* tab, and then make your edits:
+
[source,yaml]
----
apiVersion: console.openshift.io/v1
kind: ConsoleCLIDownload
metadata:
  name: example-cli-download-links
spec:
  description: |
    This is an example of download links
  displayName: example
  links:
  - href: 'https://www.example.com/public/example.tar'
    text: example for linux
  - href: 'https://www.example.com/public/example.mac.zip'
    text: example for mac
  - href: 'https://www.example.com/public/example.win.zip'
    text: example for windows
----

. Click the *Save* button.

// Hiding in ROSA/OSD, as dedicated-admins cannot patch resource "customresourcedefinitions"
// Module included in the following assemblies:
//
// * web_console/customizing-the-web-console.adoc

[id="adding-yaml-examples-to-kube-resources_{context}"]
= Adding YAML examples to Kubernetes resources

You can dynamically add YAML examples to any Kubernetes resources at any time.

.Prerequisites

* You must have cluster administrator privileges.

.Procedure

. From *Administration* -> *Custom Resource Definitions*, click on *ConsoleYAMLSample*.

. Click *YAML* and edit the file:
+
[source,yaml]
----
apiVersion: console.openshift.io/v1
kind: ConsoleYAMLSample
metadata:
  name: example
spec:
  targetResource:
    apiVersion: batch/v1
    kind: Job
  title: Example Job
  description: An example Job YAML sample
  yaml: |
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: countdown
    spec:
      template:
        metadata:
          name: countdown
        spec:
          containers:
          - name: counter
            image: centos:7
            command:
            - "bin/bash"
            - "-c"
            - "for i in 9 8 7 6 5 4 3 2 1 ; do echo $i ; done"
          restartPolicy: Never
----
Use `spec.snippet` to indicate that the YAML sample is not the full YAML resource
definition, but a fragment that can be inserted into the existing YAML document
at the user's cursor.

. Click *Save*.

// Hiding in ROSA/OSD, as dedicated-admins cannot create resource "consoles"
// Module included in the following assembly:
//
// * web_console/customizing-the-web-console.adoc

[id="odc-customizing-user-perspectives_{context}"]
= Customizing user perspectives

The OpenShift Container Platform web console provides two perspectives by default, *Administrator* and *Developer*. You might have more perspectives available depending on installed console plugins. As a cluster administrator, you can show or hide a perspective for all users or for a specific user role. Customizing  perspectives ensures that users can view only the perspectives that are applicable to their role and tasks. For example, you can hide the *Administrator* perspective from unprivileged users so that they cannot manage cluster resources, users, and projects. Similarly, you can show the *Developer* perspective to users with the developer role so that they can create, deploy, and monitor applications.

You can also customize the perspective visibility for users based on role-based access control (RBAC). For example, if you customize a perspective for monitoring purposes, which requires specific permissions, you can define that the perspective is visible only to users with required permissions.

Each perspective includes the following mandatory parameters, which you can edit in the YAML view:

* `id`: Defines the ID of the perspective to show or hide
* `visibility`: Defines the state of the perspective along with access review checks, if needed
* `state`: Defines whether the perspective is enabled, disabled, or needs an access review check

[NOTE]
====
By default, all perspectives are enabled. When you customize the user perspective, your changes are applicable to the entire cluster.
====

// Hiding in ROSA/OSD, as dedicated-admins cannot create resource "consoles"
// Module included in the following assembly:
//
// * web_console/customizing-the-web-console.adoc

[id="odc-customizing-a-perspective-using-YAML-view_{context}"]
= Customizing a perspective using YAML view

.Prerequisites
* You must have administrator privileges.

.Procedure
. In the *Administrator* perspective, navigate to *Administration* -> *Cluster Settings*.
. Select the *Configuration* tab and click the *Console (operator.openshift.io)* resource.
. Click the *YAML* tab and make your customization:
.. To enable or disable a perspective, insert the snippet for *Add user perspectives* and edit the YAML code as needed:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
spec:
  customization:
    perspectives:
      - id: admin
        visibility:
          state: Enabled
      - id: dev
        visibility:
          state: Enabled
----
.. To hide a perspective based on RBAC permissions, insert the snippet for *Hide user perspectives* and edit the YAML code as needed:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
spec:
  customization:
    perspectives:
      - id: admin
        requiresAccessReview:
          - group: rbac.authorization.k8s.io
            resource: clusterroles
            verb: list
      - id: dev
        state: Enabled
----
.. To customize a perspective based on your needs, create your own YAML snippet:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
spec:
  customization:
    perspectives:
      - id: admin
        visibility:
          state: AccessReview
          accessReview:
            missing:
              - resource: deployment
                verb: list
            required:
              - resource: namespaces
                verb: list
      - id: dev
        visibility:
          state: Enabled
----

. Click *Save*.

// Hiding in ROSA/OSD, as dedicated-admins do not have sufficient permissions to read any cluster configuration
// Module included in the following assembly:
//
// * web_console/customizing-the-web-console.adoc

[id="odc-customizing-a-perspective-using-form-view_{context}"]
= Customizing a perspective using form view

.Prerequisites
* You must have administrator privileges.

.Procedure
. In the *Administrator* perspective, navigate to *Administration* -> *Cluster Settings*.
. Select the *Configuration* tab and click the *Console (operator.openshift.io)* resource.
. Click *Actions* -> *Customize* on the right side of the page.
. In the *General* settings, customize the perspective by selecting one of the following options from the dropdown list:
* *Enabled*: Enables the perspective for all users
* *Only visible for privileged users*: Enables the perspective for users who can list all namespaces
* *Only visible for unprivileged users*: Enables the perspective for users who cannot list all namespaces
* *Disabled*: Disables the perspective for all users
+
A notification opens to confirm that your changes are saved.
+
image::customizing-user-perspective.png[]
+
[NOTE]
====
When you customize the user perspective, your changes are automatically saved and take effect after a browser refresh.
====

// Hiding in ROSA/OSD, as Hive overwrites changes to console config
// Module included in the following assembly:
//
// * web_console/customizing-the-web-console.adoc

[id="odc_con_customizing-a-developer-catalog-or-its-sub-catalogs_{context}"]
= Developer catalog and sub-catalog customization

As a cluster administrator, you have the ability to organize and manage the Developer catalog or its sub-catalogs. You can enable or disable the sub-catalog types or disable the entire developer catalog.

The `developerCatalog.types` object includes the following parameters that you must define in a snippet to use them in the YAML view:

* `state`: Defines if a list of developer catalog types should be enabled or disabled.
* `enabled`: Defines a list of developer catalog types (sub-catalogs) that are visible to users.
* `disabled`: Defines a list of developer catalog types (sub-catalogs) that are not visible to users.

You can enable or disable the following developer catalog types (sub-catalogs) using the YAML view or the form view.

* `Builder Images`
* `Templates`
* `Devfiles`
* `Samples`
* `Helm Charts`
* `Event Sources`
* `Event Sinks`
* `Operator Backed`

// Hiding in ROSA/OSD, as Hive overwrites changes to console config
// Module included in the following assembly:
//
// * web_console/customizing-the-web-console.adoc

[id="odc_customizing-a-developer-catalog-or-its-sub-catalogs-using-the-yaml-view_{context}"]
= Customizing a developer catalog or its sub-catalogs using the YAML view

You can customize a developer catalog by editing the YAML content in the YAML view.

.Prerequisites

* An OpenShift web console session with cluster administrator privileges.

.Procedure

. In the *Administrator* perspective of the web console, navigate to *Administration* -> *Cluster Settings*.
. Select the *Configuration* tab, click the *Console (operator.openshift.io)* resource and view the *Details* page.
. Click the *YAML* tab to open the editor and edit the YAML content as needed.
+
For example, to disable a developer catalog type, insert the following snippet that defines a list of disabled developer catalog resources:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
...
spec:
  customization:
    developerCatalog:
      categories:
      types:
        state: Disabled
        disabled:
          - BuilderImage
          - Devfile
          - HelmChart
...
----

. Click *Save*.

[NOTE]
====
By default, the developer catalog types are enabled in the Administrator view of the Web Console.
====

// Hiding in ROSA/OSD, as dedicated-admins do not have sufficient permissions to read any cluster configuration
// Module included in the following assembly:
//
// * web_console/customizing-the-web-console.adoc

[id="odc_customizing-a-developer-catalog-or-its-sub-catalogs-using-the-form-view_{context}"]
= Customizing a developer catalog or its sub-catalogs using the form view

You can customize a developer catalog by using the form view in the Web Console.

.Prerequisites

* An OpenShift web console session with cluster administrator privileges.
* The Developer perspective is enabled.

.Procedure

. In the *Administrator* perspective, navigate to *Administration* -> *Cluster Settings*.
. Select the *Configuration* tab and click the *Console (operator.openshift.io)* resource.
. Click *Actions* -> *Customize*.
. Enable or disable items in the *Pre-pinned navigation items*, *Add page*, and *Developer Catalog* sections.
+
.Verification
After you have customized the developer catalog, your changes are automatically saved in the system and take effect in the browser after a refresh.
+
image::odc_customizing_developer_catalog.png[]

[NOTE]
====
As an administrator, you can define the navigation items that appear by default for all users. You can also reorder the navigation items.
====

[TIP]
====
You can use a similar procedure to customize Web UI items such as Quick starts, Cluster roles, and Actions.
====

// Hiding in ROSA/OSD, as dedicated-admins cannot patch resource "consoles"
// Module included in the following assembly:
//
// * web_console/customizing-the-web-console.adoc

[id="con_example-yaml-file-changes_{context}"]
= Example YAML file changes

You can dynamically add the following snippets in the YAML editor for customizing a developer catalog.

Use the following snippet to display all the sub-catalogs by setting the _state_ type to *Enabled*.
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
...
spec:
  customization:
    developerCatalog:
      categories:
      types:
        state: Enabled
----

Use the following snippet to disable all sub-catalogs by setting the _state_ type to *Disabled*:
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
...
spec:
  customization:
    developerCatalog:
      categories:
      types:
        state: Disabled
----

Use the following snippet when a cluster administrator defines a list of sub-catalogs, which are enabled in the Web Console.
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
...
spec:
  customization:
    developerCatalog:
      categories:
      types:
        state: Enabled
        enabled:
          - BuilderImage
          - Devfile
          - HelmChart
          - ...
----
