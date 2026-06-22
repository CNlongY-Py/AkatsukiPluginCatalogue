from typing import Any

from ...base_api import BaseApi, PaginatedResult


class FitnessApi(BaseApi):
    _base_path = '/fitness'

    def get_workouts(self, skip: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/workouts', params={'skip': skip, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_workout(self, id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/workouts/{id}')
        return response.json()

    def create_workout(self, request: dict[str, Any]) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/workouts', json=request)
        return response.json()

    def update_workout(self, id: str, request: dict[str, Any]) -> dict[str, Any]:
        response = self._put(f'{self._base_path}/workouts/{id}', json=request)
        return response.json()

    def delete_workout(self, id: str) -> None:
        self._delete(f'{self._base_path}/workouts/{id}')

    def create_workouts_batch(self, request: dict[str, Any]) -> None:
        self._post(f'{self._base_path}/workouts/batch', json=request)

    def update_workouts_visibility(self, workout_ids: list[str], visibility: int) -> int:
        response = self._patch(f'{self._base_path}/workouts/batch/visibility', json={'workout_ids': workout_ids, 'visibility': visibility})
        return int(response.json())

    def add_exercise(self, workout_id: str, request: dict[str, Any]) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/workouts/{workout_id}/exercises', json=request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: dict[str, Any]) -> dict[str, Any]:
        response = self._put(f'{self._base_path}/workouts/exercises/{exercise_id}', json=request)
        return response.json()

    def remove_exercise(self, exercise_id: str) -> None:
        self._delete(f'{self._base_path}/workouts/exercises/{exercise_id}')

    def get_goals(self, status: int | None = None, skip: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        params: dict[str, Any] = {'skip': skip, 'take': take}
        if status is not None:
            params['status'] = status
        response = self._get(f'{self._base_path}/goals', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_goal_stats(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/goals/stats')
        return response.json()

    def get_goal(self, id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/goals/{id}')
        return response.json()

    def create_goal(self, request: dict[str, Any]) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/goals', json=request)
        return response.json()

    def update_goal(self, id: str, request: dict[str, Any]) -> dict[str, Any]:
        response = self._put(f'{self._base_path}/goals/{id}', json=request)
        return response.json()

    def update_progress(self, id: str, request: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/goals/{id}/progress', json=request)
        return response.json()

    def update_goal_status(self, id: str, request: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/goals/{id}/status', json=request)
        return response.json()

    def delete_goal(self, id: str) -> None:
        self._delete(f'{self._base_path}/goals/{id}')

    def recalculate_goal(self, id: str) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/goals/{id}/recalculate')
        return response.json()

    def get_metrics(self, type: int | None = None, skip: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        params: dict[str, Any] = {'skip': skip, 'take': take}
        if type is not None:
            params['type'] = type
        response = self._get(f'{self._base_path}/metrics', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_metric(self, id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/metrics/{id}')
        return response.json()

    def create_metric(self, request: dict[str, Any]) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/metrics', json=request)
        return response.json()

    def update_metric(self, id: str, request: dict[str, Any]) -> dict[str, Any]:
        response = self._put(f'{self._base_path}/metrics/{id}', json=request)
        return response.json()

    def delete_metric(self, id: str) -> None:
        self._delete(f'{self._base_path}/metrics/{id}')

    def create_metrics_batch(self, request: dict[str, Any]) -> None:
        self._post(f'{self._base_path}/metrics/batch', json=request)

    def update_metrics_visibility(self, metric_ids: list[str], visibility: int) -> int:
        response = self._patch(f'{self._base_path}/metrics/batch/visibility', json={'metric_ids': metric_ids, 'visibility': visibility})
        return int(response.json())

    def update_goals_visibility(self, goal_ids: list[str], visibility: int) -> int:
        response = self._patch(f'{self._base_path}/goals/batch/visibility', json={'goal_ids': goal_ids, 'visibility': visibility})
        return int(response.json())

    def delete_exercise(self, id: str) -> None:
        self._delete(f'{self._base_path}/exercises/{id}')

    def get_leaderboard(self, type: int = 0, period: int = 0, skip: int = 0, take: int = 20) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/leaderboard', params={'type': type, 'period': period, 'skip': skip, 'take': take})
        return response.json()
