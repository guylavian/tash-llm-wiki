---
title: "Working with Helm releases"
type: reference
domain: openshift
slug: applications-4-22-odc-working-with-helm-releases
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/odc-working-with-helm-releases
version: 4.22
family: applications
documentKind: "Documentation"
---

# Working with Helm releases

[id="odc-working-with-helm-releases"]
= Working with Helm releases

You can use the web console to create, update, roll back, or delete a Helm release.

// Module included in the following assemblies:

// applications/working_with_helm_charts/odc-working-with-helm-releases.adoc

[id="odc-creating-helm-release-from-url_{context}"]
= Installing a Helm release from a URL

[role="_abstract"]
A Helm release is a deployed instance of a Helm chart within your OpenShift Container Platform cluster. You can install charts from the developer catalog or by using a direct chart URL. Using a direct URL avoids the need for a configured Helm repository. However, this method circumvents the validation provided by the developer catalog. Use the direct URL method only when a chart is not available from the developer catalog or configured repositories.

[WARNING]
====
Installing a Helm chart from a direct URL bypasses the validation checks provided by the developer catalog. Install charts only from URLs you trust, because unverified charts can introduce security risks to your cluster. When possible, use charts from the developer catalog or a configured Helm repository instead.
====

.Prerequisites
* You've logged in to the OpenShift Container Platform web console.
* You have the necessary project permissions to install a Helm chart.
* You have a URL for a Helm chart.

.Procedure
. In the OpenShift Container Platform web console, select **Ecosystem > Helm** from the navigation menu. The **Helm** view opens.
. In the **Project** drop-down menu, select the project where you want to install the Helm release; for example, **default**.
. From the **Helm Releases** tab, click **Create**.
. Select **Helm chart URL**. The **Install Helm chart from URL** view opens.
. In the **Chart URL** field, enter the URL for the Helm chart you want to install.
+
NOTE: For Helm charts stored in an OCI-compliant registry, the URL must use the `oci://` protocol; for example, `oci://quay.io/organization/repository/chart-name`.
+
. In the **Release name** field, enter a name for the Helm release you want to install.
. In the **Chart version** field, enter the chart version number if it is not detected automatically.
. Click **Next**. The **Configure Helm release** view opens.
* Review the configuration. Make sure that *Chart URL*, *Release name*, and *Chart version* are correct.
. For the **Configure via** option, select either **Form view** or **YAML view**.
* Choose **Form view** (the default) for a guided configuration of standard parameters.
* Choose **YAML view** if you need to modify advanced settings that are not available in the form view.
+
NOTE: The **Form view** might not display every field from your Helm chart. For full control over all configuration parameters, select **YAML view**.
+
. Click **Install**. The **Helm Releases** tab opens and, if the release installation is successful, its status is **Deployed**.

.Verification
* The new Helm release is listed in the table on the **Helm Releases** tab.
* The **Status** column for the Helm release displays **Deployed**.

[role="_additional-resources"]
.Additional resources

* Official Helm documentation
* Quay OCI artifact support for Helm charts

[id="odc-upgrading-helm-release_{context}"]
= Upgrading a Helm release

[role="_abstract"]
You can upgrade a Helm release to use a new chart version or update your release configuration.

.Procedure

. In the *Topology* view, select the Helm release to see the side panel.
. Click *Actions > Upgrade Helm Release*.
. On the *Upgrade Helm Release* page, if you can edit the *Chart Version* field, select the chart version you want to upgrade to, edit the values as needed, then click *Upgrade* to create a revision of the Helm release. The *Helm Releases* page shows both revisions.
+
NOTE: If you installed the Helm chart using a direct URL, you can't change *Chart Version*. Instead, edit the values in *Form view* or *YAML view*.

[id="odc-rolling-back-helm-release_{context}"]
= Rolling back a Helm release

If a release fails, you can rollback the Helm release to a previous version.

.Procedure
To rollback a release using the *Helm* view:

. In the *Developer* perspective, navigate to the *Helm* view to see the *Helm Releases* in the namespace.
. Click the Options menu {kebab} adjoining the listed release, and select *Rollback*.
. In the *Rollback Helm Release* page, select the *Revision* you want to rollback to and click *Rollback*.
. In the *Helm Releases* page, click on the chart to see the details and resources for that release.
. Go to the *Revision History* tab to see all the revisions for the chart.
+
.Helm revision history
image::odc_helm_revision_history.png[]
+
. If required, you can further use the Options menu {kebab} adjoining a particular revision and select the revision to rollback to.

[id="odc-deleting-helm-release_{context}"]
= Deleting a Helm release

.Procedure
. In the *Topology* view, right-click the Helm release and select *Delete Helm Release*.
. In the confirmation prompt, enter the name of the chart and click *Delete*.

[id="additional-resources_{context}"]
[role="_additional-resources"]
== Additional resources

* OpenShift web console
