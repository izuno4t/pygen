"""Data service."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Metrics:
    total: int
    mean: float


def calculate_metrics(values: list[int]) -> Metrics:
    if not values:
        raise ValueError("データが空です")
    total = sum(values)
    mean = total / len(values)
    return Metrics(total=total, mean=mean)
