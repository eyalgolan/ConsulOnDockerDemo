#!/bin/bash

readonly IMAGE="progrium/consul"

main() {
	local container_id="$1"; shift
	local port="$1"; shift
	local path="$1"; shift
	local opts="$@"
	
	local ip="$(docker inspect -f "{{.NetworkSettings.IPAddress}}" $container_id)"
	local curl_cmd="curl \
		--silent \
		--show-error \
		--fail \
		--dump-header /dev/stderr \
		--retry 2 \
		$opts \
		http://$ip:$port$path > /dev/null"
	docker run --rm --net container:$container_id --entrypoint "/bin/bash" $IMAGE -c "$curl_cmd"
}

main $@
