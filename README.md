You can run this application on one server or on swarm cluster.

Go to web_plus_db directory.

One server: run this command -> docker compose up -d

Cluster: you need create swarm and run this command: docker stack deploy -c compose_swarm.yml app

Application is exposed on 9999 port.
