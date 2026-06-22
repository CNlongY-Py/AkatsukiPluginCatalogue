from typing import Any

from ...base_api import BaseApi, PaginatedResult


class PollsApi(BaseApi):
    _base_path = '/poll'

    def get_polls(self, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/polls', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_poll(self, poll_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/polls/{poll_id}')
        return response.json()

    def create_poll(self, title: str, questions: list[dict[str, Any]], expires_at: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'title': title, 'questions': questions, 'expires_at': expires_at})
        response = self._post(f'{self._base_path}/polls', json=data)
        return response.json()

    def update_poll(self, poll_id: str, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/polls/{poll_id}', json=data)
        return response.json()

    def delete_poll(self, poll_id: str) -> None:
        self._delete(f'{self._base_path}/polls/{poll_id}')

    def close_poll(self, poll_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/polls/{poll_id}/close')
        return response.json()

    def get_poll_answers(self, poll_id: str, offset: int = 0, take: int = 50) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/polls/{poll_id}/answers', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def submit_answer(self, poll_id: str, question_id: str, option_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/polls/{poll_id}/answers', json={'question_id': question_id, 'option_id': option_id})
        return response.json()

    def update_answer(self, poll_id: str, answer_id: str, option_id: str) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/polls/{poll_id}/answers/{answer_id}', json={'option_id': option_id})
        return response.json()

    def delete_answer(self, poll_id: str, answer_id: str) -> None:
        self._delete(f'{self._base_path}/polls/{poll_id}/answers/{answer_id}')

    def get_poll_stats(self, poll_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/polls/{poll_id}/stats')
        return response.json()

    def get_poll_results(self, poll_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/polls/{poll_id}/results')
        return response.json()

    def get_poll_participants(self, poll_id: str, offset: int = 0, take: int = 50) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/polls/{poll_id}/participants', params={'offset': offset, 'take': take})
        return response.json()

    def get_my_polls(self, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/me/polls', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_answered_polls(self, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/me/answered', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_poll_feed(self, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/feed', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_trending_polls(self, limit: int = 10) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/trending', params={'limit': limit})
        return response.json()
