#!/usr/bin/env bash
    echo keycloak is up , check started
    echo 'start creating client corpay-resources'
    while true
         do
         export response=$(curl -I -k http://localhost:8080/auth/realms/master/ 2>/dev/null | head -n 1 | cut -d$' ' -f2)
         echo keycloak response code is $response
         if [ $response == "200" ]; then
         echo keycloak is up , check started
         echo 'start creating client corpay-resources'
#
#         /opt/jboss/keycloak/bin/kcadm.sh config credentials --server http://localhost:8080/auth --realm master --user admin --password admin
#         export app=$(/opt/jboss/keycloak/bin/kcadm.sh create users -r master -s username=approval -i)
#         export veri=$(/opt/jboss/keycloak/bin/kcadm.sh create users -r master -s username=verifier -i)
#         export entry=$(/opt/jboss/keycloak/bin/kcadm.sh create users -r master -s username=data-entry -i)
#
#         /opt/jboss/keycloak/bin/kcadm.sh set-password -r master --username approval --new-password user
#         /opt/jboss/keycloak/bin/kcadm.sh set-password -r master --username verifier --new-password user
#         /opt/jboss/keycloak/bin/kcadm.sh set-password -r master --username data-entry --new-password user
#         /opt/jboss/keycloak/bin/kcadm.sh update users/$app -r master -s enabled=true
#         /opt/jboss/keycloak/bin/kcadm.sh update users/$veri -r master -s enabled=true
#         /opt/jboss/keycloak/bin/kcadm.sh update users/$entry -r master -s enabled=true
#         /opt/jboss/keycloak/bin/kcadm.sh create roles -r master -s name=data-entry
#         /opt/jboss/keycloak/bin/kcadm.sh create roles -r master -s name=verifier
#         /opt/jboss/keycloak/bin/kcadm.sh create roles -r master -s name=approval
#         /opt/jboss/keycloak/bin/kcadm.sh create roles -r master -s name=user
#         /opt/jboss/keycloak/bin/kcadm.sh add-roles -r master --rname approval --cclientid master-realm --rolename view-clients --rolename manage-realm
#         /opt/jboss/keycloak/bin/kcadm.sh add-roles -r master --uusername approval --rolename approval --rolename user --rolename create-realm
#         /opt/jboss/keycloak/bin/kcadm.sh add-roles -r master --uusername verifier --rolename verifier --rolename user
#         /opt/jboss/keycloak/bin/kcadm.sh add-roles -r master --uusername data-entry --rolename data-entry --rolename user
#         /opt/jboss/keycloak/bin/kcadm.sh add-roles -r master --uusername admin --rolename data-entry --rolename verifier --rolename approval --rolename user
#
#         /opt/jboss/keycloak/bin/kcadm.sh create clients -r master --file=/scripts/master-public-client.json
#         /opt/jboss/keycloak/bin/kcadm.sh create clients -r master --file=/scripts/master-client.json
#         exec /opt/jboss/keycloak/bin/kcadm.sh create clients -r master --file=/scripts/authority-matrix-client.json
         break
         fi
         sleep 1
         done