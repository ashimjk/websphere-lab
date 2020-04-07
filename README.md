# Websphere Lab

## Setup

```shell
docker-compose up

docker ps
docker exec -it <ibm-container> sh
$ cat /tmp/PASSWORD
```
#### Retrieve docker-machine IP
```shell script
ifconfig
docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet **172.17.0.1**  netmask 255.255.0.0  broadcast 172.17.255.255
        ether 02:42:15:65:f0:57  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

## Install API-Gateway
* IBM WebSphere Admin URL:
  - https://172.17.0.1:9043/ibm/console 
* Create new WebSphere Enterprise Application
* Upload api-gateway.war
* follow wizard screens
* save configuration
* start api-gateway_war app
## Access API-Gateway 
* Open IBM Publisc URL:
  - https://172.17.0.1:9080
* Service management address:
  - http://172.17.0.1:9080/service-management/services
  result should be similar to this:
    ```json
    { content: [Resource { content: ServiceResource(name=payment-resources, alias=Payments, status=AVAILABLE, url=null, roles={viewer=[view], creator=[create], verifier=[verify], approval=[approve]}), links: [] }, Resource { content: ServiceResource(name=outgoing-lg-resources, alias=Outgoing LG, status=AVAILABLE, url=null, roles={viewer=[view], creator=[create], verifier=[verify], approval=[approve]}), links: [] }, Resource { content: ServiceResource(name=incoming-lg-resources, alias=Incoming LG, status=AVAILABLE, url=null, roles={viewer=[view], creator=[create], verifier=[verify], approval=[approve]}), links: [] }, Resource { content: ServiceResource(name=importer-lc-resources, alias=Importer LC, status=AVAILABLE, url=null, roles={viewer=[view], creator=[create], verifier=[verify], approval=[approve]}), links: [] }, Resource { content: ServiceResource(name=export-lc-resources, alias=Exporter LC, status=AVAILABLE, url=null, roles={viewer=[view], creator=[create], verifier=[verify], approval=[approve]}), links: [] }, Resource { content: ServiceResource(name=incoming-bc-resources, alias=Incoming BC, status=AVAILABLE, url=null, roles={viewer=[view], creator=[create], verifier=[verify], approval=[approve]}), links: [] }, Resource { content: ServiceResource(name=outgoing-bc-resources, alias=Outgoing BC, status=AVAILABLE, url=null, roles={viewer=[view], creator=[create], verifier=[verify], approval=[approve]}), links: [] }, Resource { content: ServiceResource(name=inward-checks-resources, alias=Inward Checks, status=AVAILABLE, url=null, roles={viewer=[view], creator=[create], verifier=[verify], approval=[approve]}), links: [] }, Resource { content: ServiceResource(name=outward-checks-resources, alias=Outward Checks, status=AVAILABLE, url=null, roles={viewer=[view], creator=[create], verifier=[verify], approval=[approve]}), links: [] }, Resource { content: ServiceResource(name=cash-management-resources, alias=Cash Management, status=AVAILABLE, url=null, roles={viewer=[view], creator=[create], verifier=[verify], approval=[approve]}), links: [] }
    ```
  - http://172.17.0.1:9080/service-management/swagger-ui.html
  - http://172.17.0.1:9080/service-management/actuator/health
  - http://172.17.0.1:9080/service-management/actuator/env
