from enum import Enum


class OtoroshimodelsLoadBalancingType(str, Enum):
    BESTRESPONSETIME = "BestResponseTime"
    IPADDRESSHASH = "IpAddressHash"
    RANDOM = "Random"
    ROUNDROBIN = "RoundRobin"
    STICKY = "Sticky"
    WEIGHTEDBESTRESPONSETIME = "WeightedBestResponseTime"

    def __str__(self) -> str:
        return str(self.value)
