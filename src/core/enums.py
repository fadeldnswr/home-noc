'''
Enums for data types
'''
from enum import Enum

# Define probe type enumeration
class ProbeType(str, Enum):
  ICMP = "ICMP"
  DNS = "DNS"
  HTTP = "HTTP"
  TRACEROUTE = "TRACEROUTE"

# Define probe status enums
class ProbeStatus(str, Enum):
  UP = "UP"
  DOWN = "DOWN"
  DEGRADED = "DEGRADED"

# Define target type enums
class TargetType(str, Enum):
  ROUTER = "router"
  PUBLIC_DNS = "public_dns"
  SERVICE = "service"

# Define incident type enums
class IncidentType(str, Enum):
  LOCAL_OUTAGE = "local_outage"
  WAN_OUTAGE = "wan_outage"
  DNS_DEGRADATION = "dns_degradation"
  SERVICE_DEGRADATION = "service_degradation"
  UPSTREAM_CONGESTION = "upstream_congestion"

# Define severity enums
class Severity(str, Enum):
  INFO = "info"
  WARNING = "warning"
  CRITICAL = "critical"