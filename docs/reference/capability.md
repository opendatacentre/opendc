# Capability
___

Within the context of **k8sdc**, a *Capability* is the definition of a set of desired attributes that apply to a particular domain within an IT system, i.e. cluster management, monitoring, logging, etc.  A *Capability* is implemented by a [*Solution*](solution.md) and there can be more than one equivalent *Solution* to a *Capability*, leaving the choice of which *Solution* to use up to the end user.
___


## Current Capabilities

The *Capabilities* that are currently implemented within **k8sdc** are listed in the following table.

| Capability Name                              | Solutions                                                              |
| :------------------------------------------- | :--------------------------------------------------------------------- |
| [Cluster Services][cap_clust_serv]           | [(cs1) Cluster Services][sol_cs1_clust_serv]            |
| [Cluster Management][cap_clust_man]          | [(cm1) Cluster Management][sol_cm1_clust_man]                   |
| [Distributed Block Storage][cap_dist_blk_st] | [(dbs1) Distributed Block Storage][sol_dbs1_dist_blk_st]               |
| [Identity Management][cap_ident_man]         | [(im1) Identity Management][sol_im1_ident_man] |
| [HTTP/S Reverse Proxy][cap_https_rev_proxy]  | [(hrp1) HTTP/S Reverse Proxy][sol_hrp1_https_rev_proxy]          |
| [Metrics][cap_metrics]                       | [(m1) Metrics][sol_m1_metrics]                               |
| [Logging][cap_logging]                       | [(l1) Logging][sol_l1_logging]                           |
| [Job Management][cap_job_management]         | [(jm1) Job Management][sol_jm1_job_management]                 |
| [Artifact Storage][cap_art_st]               | [(as1) Artifact Storage][sol_as1_art_st]               |
| [Image Repository][cap_image_repo]           | [(ir1) Image Repository][sol_ir1_image_repo]                     |


[cap_clust_serv]:     capabilities/cluster_services.md
[sol_cs1_clust_serv]: solutions/cs1_cluster_services.md

[cap_clust_man]:     capabilities/cluster_management.md
[sol_cm1_clust_man]: solutions/cm1_cluster_management.md

[cap_dist_blk_st]:      capabilities/distributed_block_storage.md
[sol_dbs1_dist_blk_st]: solutions/dbs1_distributed_block_storage.md

[cap_ident_man]:     capabilities/identity_management.md
[sol_im1_ident_man]: solutions/im1_identity_management.md

[cap_https_rev_proxy]:      capabilities/https_reverse_proxy.md
[sol_hrp1_https_rev_proxy]: solutions/hrp1_https_reverse_proxy.md

[cap_metrics]:    capabilities/metrics.md
[sol_m1_metrics]: solutions/m1_metrics.md

[cap_logging]:    capabilities/logging.md
[sol_l1_logging]: solutions/l1_logging.md

[cap_job_management]:     capabilities/job_management.md
[sol_jm1_job_management]: solutions/jm1_job_management.md

[cap_art_st]:     capabilities/artifact_storage.md
[sol_as1_art_st]: solutions/as1_artifact_storage.md

[cap_image_repo]:     capabilities/image_repository.md
[sol_ir1_image_repo]: solutions/ir1_image_repository.md
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

