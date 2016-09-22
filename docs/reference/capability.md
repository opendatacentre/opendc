# Capability
___

Within the context of **k8sdc**, a *Capability* is the definition of a set of desired attributes that apply to a particular domain within an IT system, i.e. cluster management, monitoring, logging, etc.  A *Capability* is implemented by a [*Solution*](solution.md) and there can be more than one equivalent *Solution* to a *Capability*, leaving the choice of which *Solution* to use up to the end user.
___


## Current Capabilities

The *Capabilities* that are currently implemented within **k8sdc** are listed in the following table.

| Capability Name  | Solutions     |
|:-----------------|:--------------|
| [Cluster Management][cap_clust_man]          | [Cluster Management (Kubernetes)][sol_clust_man_kub]                   |
| [Distributed Block Storage][cap_dist_blk_st] | [Distributed Block Storage (Ceph)][sol_dist_blk_st_ceph]               |
| [Identity Management][cap_ident_man]         | [Identity Management (OpenDJ+Keycloak)][sol_ident_man_opendj_keycloak] |
| [HTTP/S Reverse Proxy][cap_https_rev_proxy]  | [HTTP/S Reverse Proxy (Traefik)][sol_https_rev_proxy_traefik]          |
| [Metrics][cap_metrics]                       | [Metrics (Prometheus)][sol_metrics_prom]                               |
| [Logging][cap_logging]                       | [Logging (ELK+Kafka)][sol_logging_elk_kafka]                           |
| [Job Management][cap_job_management]         | [Job Management (Jenkins)][sol_job_management_jenkins]                 |
| [Artifact Storage][cap_art_st]               | [Artifact Storage (Artifactory)][sol_art_st_artifactory]               |
| [Image Repository][cap_image_repo]           | [Image Repository (Portus)][sol_image_repo_portus]                     |


[cap_clust_man]:     capabilities/cluster_management.md
[sol_clust_man_kub]: solutions/cluster_management_kubernetes.md

[cap_dist_blk_st]:      capabilities/distributed_block_storage.md
[sol_dist_blk_st_ceph]: solutions/distributed_block_storage_ceph.md

[cap_ident_man]:                 capabilities/identity_management.md
[sol_ident_man_opendj_keycloak]: solutions/identity_management_opendj_keycloak.md

[cap_https_rev_proxy]:         capabilities/https_reverse_proxy.md
[sol_https_rev_proxy_traefik]: solutions/https_reverse_proxy_traefik.md

[cap_metrics]:      capabilities/metrics.md
[sol_metrics_prom]: solutions/metrics_prometheus.md

[cap_logging]:           capabilities/logging.md
[sol_logging_elk_kafka]: solutions/logging_elk_kafka.md

[cap_job_management]:         capabilities/job_management.md
[sol_job_management_jenkins]: solutions/job_management_jenkins.md

[cap_art_st]:             capabilities/artifact_storage.md
[sol_art_st_artifactory]: solutions/artifact_storage_artifactory.md

[cap_image_repo]:        capabilities/image_repository.md
[sol_image_repo_portus]: solutions/image_repository_portus.md
___


## Capability Roadmap {#capability_roadmap}

### Next Capabilities

The following *Capabilities* will be added to **k8sdc** in the near future. 

* Git hosting.
* Dropbox like file synchronisation.
* Chat / Messaging.


### Future Capabilities

The following *Capabilities* will be added to **k8sdc** in the future.

* PaaS.
* Code review.
* Blog.
* Wiki.
* CMS.
* Forum.
* Email.
* Project management.
* Reporting and analytics.
* VPN.
* Performance / usability testing.
* Database as a service.
* Caching.
* Batch.
* etc.....

