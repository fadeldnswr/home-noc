'''
Settings module to configure environment variable
'''
from __future__ import annotations

import os
from dataclasses import dataclass, field
from dotenv import load_dotenv
from typing import List

# Load environment vars
load_dotenv()

# Method to split CSV
def _split_csv(value: str) -> List[str]:
  if not value:
    return []
  return [item.strip() for item in value.split(",") if item.strip()]

# Define settings class
@dataclass(slots=True)
class Settings:
  influx_url: str = os.getenv("INFLUX_URL", "http://localhost:8086")
  influx_token: str = os.getenv("INFLUX_TOKEN", "")
  influx_org: str = os.getenv("INFLUX_ORG", "home-lab")
  influx_bucket: str = os.getenv("INFLUX_BUCKET", "network_observability")

  router_ip: str = os.getenv("ROUTER_IP", "192.168.1.1")
  ping_count: int = int(os.getenv("PING_COUNT", "5"))
  ping_timeout: int = int(os.getenv("PING_TIMEOUT", "3"))
  http_timeout: int = int(os.getenv("HTTP_TIMEOUT", "5"))
  trace_timeout: int = int(os.getenv("TRACE_TIMEOUT", "2"))
  
  # Define network targets
  http_targets: List[str] = field(
    default_factory=lambda: _split_csv(os.getenv("HTTP_TARGETS", "https://www.google.com,https://github.com"))
  )
  icmp_target: List[str] = field(
    default_factory=lambda: _split_csv("ICMP_TARGET", "1.1.1.1,8.8.8.8,google.com,github.com")
  )
  dns_resolvers: List[str] = field(
    default_factory=lambda: _split_csv("DNS_RESOLVERS", "1.1.1.1,8.8.8.8")
  )
  dns_domains: List[str] = field(
    default_factory=lambda: _split_csv("DNS_DOMAINS", "google.com,github.com")
  )
  trace_target: List[str] = field(
    default_factory=lambda: _split_csv("TRACE_TARGET", "1.1.1.1,8.8.8.8")
  )

# Call settings
settings = Settings()