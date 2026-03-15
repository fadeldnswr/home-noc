'''
Model module for application schema
'''
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional

from src.core.enums import (
  ProbeStatus, ProbeType, TargetType,
  IncidentType, Severity
)

# Define function to return utc datetime
def utc_now() -> datetime:
  return datetime.now(timezone.utc)

# Define dataclass for base measurement
@dataclass(slots=True)
class BaseMeasurement:
  probe_type: ProbeType
  target: str
  status: ProbeStatus
  timestamp: datetime = field(default_factory=utc_now)

# Define dataclass for ICMP measurement
@dataclass(slots=True)
class ICMPMeasurement(BaseMeasurement):
  target_type: TargetType = TargetType.SERVICE
  latency_ms: float = 0.0
  packet_loss_pct: float = 100.0
  jitter_ms: float = 0.0
  sent_packets: int = 0
  received_packets: int = 0
  
  # Initialization method
  def __post_init(self) -> None:
    self.probe_type = ProbeType.ICMP


# Define dataclass for DNS measurement
@dataclass(slots=True)
class DNSMeasurement(BaseMeasurement):
  resolve: str = ""
  domain: str = ""
  resolve_time_ms: float = 0.0
  
  def __post_init(self) -> None:
    self.probe_type = ProbeType.ICMP

# Define dataclass for HTTP measurement
@dataclass(slots=True)
class HTTPMeasurement(BaseMeasurement):
  response_time_ms: float = 0.0
  http_status_code: int = 0
  
  def __post_init(self) -> None:
    self.probe_type = ProbeType.HTTP


# Define dataclass for path hop measurement
@dataclass(slots=True)
class PathHopMeasurement(BaseMeasurement):
  destination: str = ""
  hop_number: int = 0
  hop_ip: str = ""
  latency_ms: float = 0.0

# Define dataclass for network scoring
@dataclass(slots=True)
class NetworkScore:
  score: float
  latency_component: float
  packet_loss_component: float
  jitter_component: float
  dns_component: float 
  http_component: float
  scope: str = "overall"
  timestamp: datetime = field(default_factory=utc_now)

# Define dataclass for incident
@dataclass(slots=True)
class IncidentEvent:
  incident_type: IncidentType
  severity: Severity
  target: str
  description: str
  active: bool = True
  duration_sec: float = 0.0
  timestamp: datetime = field(default_factory=utc_now)