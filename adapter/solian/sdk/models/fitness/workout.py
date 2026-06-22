from __future__ import annotations

from enum import IntEnum
from typing import Any, Optional

from pydantic import BaseModel, Field


class WorkoutType(IntEnum):
    strength = 0
    cardio = 1
    hiit = 2
    yoga = 3
    other = 4


class FitnessVisibility(IntEnum):
    private = 0
    public = 1


class SnWorkoutExercise(BaseModel):
    id: str = ""
    workout_id: str = ""
    exercise_name: str = ""
    sets: Optional[int] = None
    reps: Optional[int] = None
    weight: Optional[float] = None
    notes: Optional[str] = None
    order_index: int = 0
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class SnWorkout(BaseModel):
    id: str = ""
    account_id: str = ""
    name: str = ""
    description: Optional[str] = None
    type: WorkoutType = WorkoutType.other
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    calories_burned: Optional[int] = None
    distance: Optional[float] = None
    distance_unit: Optional[str] = None
    average_speed: Optional[float] = None
    average_heart_rate: Optional[int] = None
    max_heart_rate: Optional[int] = None
    elevation_gain: Optional[float] = None
    max_speed: Optional[float] = None
    notes: Optional[str] = None
    visibility: FitnessVisibility = FitnessVisibility.private
    meta: Optional[dict[str, Any]] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    exercises: list[SnWorkoutExercise] = Field(default_factory=list)


class CreateWorkoutExerciseRequest(BaseModel):
    exercise_name: str = ""
    sets: Optional[int] = None
    reps: Optional[int] = None
    weight: Optional[float] = None
    notes: Optional[str] = None
    order_index: int = 0


class CreateWorkoutRequest(BaseModel):
    name: str = ""
    type: WorkoutType = WorkoutType.other
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    calories_burned: Optional[int] = None
    distance: Optional[float] = None
    distance_unit: Optional[str] = None
    average_speed: Optional[float] = None
    average_heart_rate: Optional[int] = None
    max_heart_rate: Optional[int] = None
    elevation_gain: Optional[float] = None
    max_speed: Optional[float] = None
    notes: Optional[str] = None
    visibility: FitnessVisibility = FitnessVisibility.private
    meta: Optional[dict[str, Any]] = None


class UpdateWorkoutRequest(BaseModel):
    name: str = ""
    type: WorkoutType = WorkoutType.other
    start_time: Optional[str] = None
    description: Optional[str] = None
    calories_burned: Optional[int] = None
    notes: Optional[str] = None
    visibility: Optional[FitnessVisibility] = None
    meta: Optional[dict[str, Any]] = None


class CreateWorkoutsBatchRequest(BaseModel):
    workouts: list[CreateWorkoutRequest] = Field(default_factory=list)


class AddExerciseRequest(BaseModel):
    exercise_name: str = ""
    sets: Optional[int] = None
    reps: Optional[int] = None
    weight: Optional[float] = None
    notes: Optional[str] = None
    order_index: int = 0


class UpdateWorkoutExerciseRequest(BaseModel):
    exercise_name: str = ""
    sets: Optional[int] = None
    reps: Optional[int] = None
    weight: Optional[float] = None
    order_index: Optional[int] = None
    notes: Optional[str] = None
