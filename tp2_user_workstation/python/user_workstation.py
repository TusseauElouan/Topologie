"""TP2 models for user and workstation."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Workstation:
    hostname: str
    ip_address: str
    os_name: str
    owner: Optional["User"] = None

    def set_owner(self, user: Optional["User"]) -> None:
        self.owner = user


@dataclass
class User:
    first_name: str
    last_name: str
    department: str
    role: str
    workstation: Optional[Workstation] = None

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def assign_workstation(self, workstation: Workstation) -> None:
        self.workstation = workstation
        workstation.set_owner(self)

