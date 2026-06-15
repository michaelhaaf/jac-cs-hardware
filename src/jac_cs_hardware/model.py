# File: src/jac_cs_hardware/model.py
# Creation date: 15 Jun 2026
# Author: michaelhaaf <michael.haaf@gmail.com>
# Modified By:
#   -
# Changes made:
#   -
# -----
# This software is intended for educational use by students and teachers in the
# the Computer Science department at John Abbott College.
# See the license disclaimer below and the project LICENSE file for more information.
# -----
# Copyright (C) 2026 michaelhaaf
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from typing import Any
from pydantic import BaseModel
from gpiozero import Device
from abc import ABC, abstractmethod


class Reading(BaseModel):
    """Sensor reading class."""

    value: str
    unit: str


class CommandRequest(BaseModel):
    """Actuator command class."""

    state: str


class CommandResponse(BaseModel):
    """Actuator command class."""

    previous_state: str
    current_state: str


class Sensor(ABC):
    """Abstract class providing a common interface to GPIO sensors."""

    device: Device

    @abstractmethod
    def read_sensor(self) -> Reading:
        pass


class Actuator(ABC):
    """Abstract class providing a common interface to GPIO actuators."""

    device: Device
    state: str = ""

    def __init__(self, device: Any):
        self.device = device

    @abstractmethod
    def control_actuator(self, command: CommandRequest) -> CommandResponse:
        pass
