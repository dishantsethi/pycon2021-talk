from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))



def get_rules(self):
    config.load_kube_config()
    v1 = client.RbacAuthorizationV1Api()
    if self.kind.lower() == "role":
        return (v1.read_namespaced_role(self.name, self.namespace)).rules
    else: # "clusterrole"
        return (v1.read_cluster_role(self.name)).rules 

get_rules()
