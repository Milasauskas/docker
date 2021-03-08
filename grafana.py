docker network create dotnetmetrics
docker run -d --restart=always -v $PWD:/var/lib/grafana --network dotnetmetrics --name grafana -p 3000:3000 grafana/grafana