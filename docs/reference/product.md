# Product
___

A *Product*, within the context of **k8sdc**, is a software application that is used to realise a [*Solution*](solution.md).  The **k8sdc** platform uses a number of *Products*.
___

## Products

The *Products* that are currently used by **k8sdc** are listed in the following table.

| Product Name | Solutions | Description |
|:-------------|:----------|:------------|
| [Kubernetes Dashboard][prd_kub_dash] | [Cluster Management (Kubernetes)][sol_clust_man_kub]                   | The Kubernetes Dashboard is used to mange the Kubernetes cluster through a web interface. |
| [Ceph][prd_ceph]                     | [Distributed block storage (Ceph)][sol_dist_blk_st_ceph]               | Ceph is used to attach block storage to the *Containers*. |
| [OpenDJ][prd_opendj]                 | [Identity Management (OpenDJ+Keycloak)][sol_ident_man_opendj_keycloak] | OpenDJ is used as the LDAP server for the Identity Management *Solution*. |
| [Keycloak][prd_keycloak]             | [Identity Management (OpenDJ+Keycloak)][sol_ident_man_opendj_keycloak] | Keycloak is used as the web UI for managing users and groups in the Identity Management *Solution*. |
| [Traefik][prd_traefik]               | [HTTP/S Reverse Proxy (Traefik)][sol_https_rev_proxy_traefik]          | Traefik is used for the HTTP(S) Reverse Proxy *Solution*. |
| [Prometheus][prd_prometheus]         | [Metrics (Prometheus)][sol_metrics_prom]                               | Prometheus is used to collect, parse and store metrics from various endpoints. |
| [Grafana][prd_grafana]               | [Metrics (Prometheus)][sol_metrics_prom]                               | Grafana is used to visualise and query Prometheus metrics. |
| [Elasticsearch][prd_elasticsearch]   | [Logging (ELK+Kafka)][sol_logging_elk_kafka]                           | Elasticsearch is used to store logs from various endpoints. |
| [Logstash][prd_logstash]             | [Logging (ELK+Kafka)][sol_logging_elk_kafka]                           | Logstash is used to collect, parse and forward logs to Kafka and Elasticsearch. |
| [Kibana][prd_kibana]                 | [Logging (ELK+Kafka)][sol_logging_elk_kafka]                           | Kibana is used to visualise and query logs from Elasticsearch |
| [Kafka][prd_kafka]                   | [Logging (ELK+Kafka)][sol_logging_elk_kafka]                           | Kafka is used to temporarily buffer logs before they are forwarded to Elasticsearch.  This allows for bursts of logs to be ingested without overwhelming Elasticsearch. |
| [Zookeeper][prd_zookeeper]           | [Logging (ELK+Kafka)][sol_logging_elk_kafka]                           | Zookeeper is used by Kafka to maintain cluster state. |
| [Jenkins][prd_jenkins]               | [Job Management (Jenkins)][sol_job_management_jenkins]                 | Jenkins is used to define and run jobs, i.e. CI/CD build/test/deploy jobs. |
| [Artifactory][prd_artifactory]       | [Artifact Storage (Artifactory)][sol_art_st_artifactory]               | Artifactory is used to store the build artifacts from a build.  It is also used to store the dependancies needed for the builds. |
| [Portus][prd_portus]                 | [Image Repository (Portus)][sol_image_repo_portus]                     | Portus provides an web based UI, with security, for the Docker image repository. |


[sol_clust_man_kub]: solutions/cluster_management_kubernetes.md
[prd_kub_dash]:      https://github.com/kubernetes/dashboard

[sol_dist_blk_st_ceph]: solutions/distributed_block_storage_ceph.md
[prd_ceph]:             http://ceph.com

[sol_ident_man_opendj_keycloak]: solutions/identity_management_opendj_keycloak.md
[prd_opendj]:                    https://forgerock.org/opendj/
[prd_keycloak]:                  http://www.keycloak.org

[sol_https_rev_proxy_traefik]: solutions/https_reverse_proxy_traefik.md
[prd_traefik]:                 https://traefik.io

[sol_metrics_prom]: solutions/metrics_prometheus.md
[prd_prometheus]:   https://prometheus.io
[prd_grafana]:      https://grafana.net

[sol_logging_elk_kafka]: solutions/logging_elk_kafka.md
[prd_elasticsearch]:     https://www.elastic.co/products/elasticsearch
[prd_logstash]:          https://www.elastic.co/products/logstash
[prd_kibana]:            https://www.elastic.co/products/kibana
[prd_kafka]:             http://kafka.apache.org
[prd_zookeeper]:         https://zookeeper.apache.org

[sol_job_management_jenkins]: solutions/job_management_jenkins.md
[prd_jenkins]:                https://jenkins.io

[sol_art_st_artifactory]: solutions/artifact_storage_artifactory.md
[prd_artifactory]:        https://www.jfrog.com/open-source/#os-arti  

[sol_image_repo_portus]: solutions/image_repository_portus.md
[prd_portus]:            http://port.us.org

___


## Product Roadmap {#product_roadmap}

### Next Products

The following *Products* will be added to **k8sdc** in the near future.

* Gitlab.
* Nextcloud.
* Mattermost


### Possible Products

The following *Products* will possibly be added to **k8sdc** in the future.

* Taiga.
* PostgreSQL.
* etc.....


