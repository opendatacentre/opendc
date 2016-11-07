# Solution
___

A *Solution* is the implementation of a [*Capability*](capability.md), or a set of *Capabilities*, by using a combination of [*Product(s)*](product.md) and configuration.

___

## Solutions

The *Solutions* that are currently implemented by **k8sdc** are listed in the following table.


| Solution Name                                                          | Capabilities                                 | Products                                                                                                                                          |
| :--------------------------------------------------------------------- | :------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| [(cs1) Cluster Services][sol_cs1_clust_serv_kub]                    | [Cluster Services][cap_clust_serv]           | [Kube DNS][prd_kub_dns] and [Heapster][prd_heapster]                                                                                              |
| [(cm1) Cluster Management][sol_clust_man_kub]                   | [Cluster Management][cap_clust_man]          | [Kubernetes Dashboard][prd_kub_dash]                                                                                                              |
| [(dbs1) Distributed Block Storage][sol_dist_blk_st_ceph]               | [Distributed Block Storage][cap_dist_blk_st] | [Ceph][prd_ceph]                                                                                                                                  |
| [(im1) Identity Management][sol_ident_man_opendj_keycloak] | [Identity Management][cap_ident_man]         | [OpenDJ][prd_opendj] and [Keycloak][prd_keycloak]                                                                                                 |
| [(hrp1) HTTP/S Reverse Proxy][sol_https_rev_proxy_traefik]          | [HTTP/S Reverse Proxy][cap_https_rev_proxy]  | [Traefik][prd_traefik]                                                                                                                            |
| [(m1) Metrics][sol_metrics_prom]                               | [Metrics][cap_metrics]                       | [Prometheus][prd_prometheus] and [Grafana][prd_grafana]                                                                                           |
| [(l1) Logging][sol_logging_elk_kafka]                           | [Logging][cap_logging]                       | [Elasticsearch][prd_elasticsearch], [Logstash][prd_logstash], [Kibana][prd_kibana] and [Kafka][prd_kafka] (which uses [Zookeeper][prd_zookeeper]) |
| [(jm1) Job Management][sol_job_management_jenkins]                 | [Job Management][cap_job_management]         | [Jenkins][prd_jenkins]                                                                                                                            |
| [(as1) Artifact Storage][sol_art_st_artifactory]               | [Artifact Storage][cap_art_st]               | [Artifactory][prd_artifactory]                                                                                                                    |
| [(ir1) Image Repository][sol_image_repo_portus]                     | [Image Repository][cap_image_repo]           | [Portus][prd_portus]                                                                                                                              |

[cap_clust_serv]:         capabilities/cluster_services.md
[sol_cs1_clust_serv_kub]: solutions/cs1_cluster_services.md
[prd_kub_dns]:            https://github.com/kubernetes/kubernetes/tree/master/cluster/addons/dns
[prd_heapster]:           https://github.com/kubernetes/heapster      

[cap_clust_man]:     capabilities/cluster_management.md
[sol_clust_man_kub]: solutions/cm1_cluster_management.md
[prd_kub_dash]:      https://github.com/kubernetes/dashboard

[cap_dist_blk_st]:      capabilities/distributed_block_storage.md
[sol_dist_blk_st_ceph]: solutions/dbs1_distributed_block_storage.md
[prd_ceph]:             http://ceph.com

[cap_ident_man]:                 capabilities/identity_management.md
[sol_ident_man_opendj_keycloak]: solutions/im1_identity_management.md
[prd_opendj]:                    https://forgerock.org/opendj/
[prd_keycloak]:                  http://www.keycloak.org

[cap_https_rev_proxy]:         capabilities/https_reverse_proxy.md
[sol_https_rev_proxy_traefik]: solutions/hrp1_https_reverse_proxy.md
[prd_traefik]:                 https://traefik.io

[cap_metrics]:      capabilities/metrics.md
[sol_metrics_prom]: solutions/m1_metrics.md
[prd_prometheus]:   https://prometheus.io
[prd_grafana]:      https://grafana.net

[cap_logging]:           capabilities/logging.md
[sol_logging_elk_kafka]: solutions/l1_logging.md
[prd_elasticsearch]:     https://www.elastic.co/products/elasticsearch
[prd_logstash]:          https://www.elastic.co/products/logstash
[prd_kibana]:            https://www.elastic.co/products/kibana
[prd_kafka]:             http://kafka.apache.org
[prd_zookeeper]:         https://zookeeper.apache.org

[cap_job_management]:         capabilities/job_management.md
[sol_job_management_jenkins]: solutions/jm1_job_management.md
[prd_jenkins]:                https://jenkins.io

[cap_art_st]:             capabilities/artifact_storage.md
[sol_art_st_artifactory]: solutions/as1_artifact_storage.md
[prd_artifactory]:        https://www.jfrog.com/open-source/#os-arti      

[cap_image_repo]:        capabilities/image_repository.md
[sol_image_repo_portus]: solutions/ir1_image_repository.md
[prd_portus]:            http://port.us.org



