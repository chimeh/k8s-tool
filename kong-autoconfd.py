#!/usr/bin/env python

import  sys
import  os
import httplib
import  urllib
import urllib2
import  json
from kubernetes import client, config
from kong.exceptions import ConflictError
from kong.simulator import KongAdminSimulator
from kong.client import KongAdminClient
from kong.compat import TestCase, skipIf, run_unittests, OrderedDict, urlencode, HTTPConnection
from kong.utils import uuid_or_string, add_url_params, sorted_ordered_dict
print(sys.path)





outer_url="http://app.k8s.local"


def main():
    kong = KongAdminClient(api_url="http://10.99.11.1:31000")
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()
    inner_upstreams = {}
    v1 = client.CoreV1Api()
    print("Listing all svc :")
    ret = v1.list_service_for_all_namespaces(watch=False)
    for i in ret.items:
#        print("%s\t%s\t%d" %
#              (i.metadata.namespace, i.metadata.name, i.spec.ports[0].port))
        inner_svc_upstream="%s%s.%s.%s:%d" % ("http://", i.metadata.name, i.metadata.namespace, "svc.cluster.local", i.spec.ports[0].port)
#        print inner_url
        outer_uri="/%s/%s" % ( i.metadata.namespace, i.metadata.name)
        outer_fullurl="%s/%s/%s/" % ( outer_url, i.metadata.namespace, i.metadata.name)
        inner_upstreams[inner_svc_upstream] =  "%s/%s/%s" % (outer_url, i.metadata.namespace, i.metadata.name);
        route_name="auto-%s-%s" % (i.metadata.namespace, i.metadata.name)
        kong.apis.delete(route_name)
        kong.apis.create_or_update(inner_svc_upstream,
                        name=route_name,
                        uris=outer_uri,
                        strip_uri=True)
        print("%s\t%s\t%s" % (outer_fullurl, inner_svc_upstream, outer_uri))
    
if __name__ == '__main__':
    main()
