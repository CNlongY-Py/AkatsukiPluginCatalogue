from typing import Any

from ...base_api import BaseApi, PaginatedResult


class AccountsApi(BaseApi):
    _base_path = '/passport'

    def get_current_account(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/accounts/me')
        return response.json()

    def update_current_account(self, data: dict[str, Any]) -> dict[str, Any]:
        response = self._patch(f'{self._base_path}/accounts/me', json=data)
        return response.json()

    def delete_current_account(self) -> None:
        self._delete(f'{self._base_path}/accounts/me')

    def get_account_by_username(self, username: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/accounts/{username}')
        return response.json()

    def get_account_by_id(self, account_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/accounts/id/{account_id}')
        return response.json()

    def get_account_profile(self, username: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/accounts/{username}/profile')
        return response.json()

    def get_account_badges(self, username: str) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/accounts/{username}/badges')
        return response.json()

    def get_my_badges(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/accounts/me/badges')
        return response.json()

    def activate_badge(self, badge_id: str) -> None:
        self._post(f'{self._base_path}/accounts/me/badges/{badge_id}/active')

    def get_badges_manifest(self) -> list[dict[str, Any]]:
        response = self._get('/.well-known/badges')
        data = response.json()
        return data.get('badges', [])

    def get_relationship(self, account_id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/relationships/{account_id}')
        return response.json()

    def add_account_as_friend(self, account_id: str) -> None:
        self._post(f'{self._base_path}/relationships/{account_id}/friends')

    def block_account(self, account_id: str) -> None:
        self._post(f'{self._base_path}/relationships/{account_id}/block')

    def unblock_account(self, account_id: str) -> None:
        self._delete(f'{self._base_path}/relationships/{account_id}/block')

    def mute_account(self, account_id: str, duration: int | None = None) -> None:
        data = {'duration': duration} if duration is not None else None
        self._post(f'{self._base_path}/relationships/{account_id}/mute', json=data)

    def unmute_account(self, account_id: str) -> None:
        self._delete(f'{self._base_path}/relationships/{account_id}/mute')

    def get_followers(self, account_id: str | None = None, offset: int = 0, take: int = 20) -> list[dict[str, Any]]:
        path = f'{self._base_path}/accounts/{account_id}/followers' if account_id else f'{self._base_path}/accounts/me/followers'
        response = self._get(path, params={'offset': offset, 'take': take})
        return response.json()

    def get_following(self, account_id: str | None = None, offset: int = 0, take: int = 20) -> list[dict[str, Any]]:
        path = f'{self._base_path}/accounts/{account_id}/following' if account_id else f'{self._base_path}/accounts/me/following'
        response = self._get(path, params={'offset': offset, 'take': take})
        return response.json()

    def get_friends_overview(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/friends/overview')
        return response.json()

    def get_achievement_state(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/progression/achievements')
        return response.json()

    def get_quest_states(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/progression/quests')
        return response.json()

    def claim_reward(self, reward_id: str) -> dict[str, Any]:
        response = self._post(f'{self._base_path}/progression/rewards/{reward_id}/claim')
        return response.json()

    def get_daily_fortune(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/fortune/daily')
        return response.json()

    def get_random_fortune_saying(self) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/fortune/random')
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            return data[0]
        return {}

    def get_fortune_history(self, offset: int = 0, take: int = 20) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/fortune/history', params={'offset': offset, 'take': take})
        return response.json()

    def get_check_in_result_today(self) -> dict[str, Any] | None:
        try:
            response = self._get(f'{self._base_path}/accounts/me/check-in', params={'version': 2})
            return response.json()
        except Exception:
            return None

    def check_in(self, captcha_token: str | None = None) -> None:
        data = captcha_token if captcha_token else None
        self._post(f'{self._base_path}/accounts/me/check-in', params={'version': 2}, json=data)

    def get_next_notable_day(self) -> dict[str, Any] | None:
        try:
            response = self._get(f'{self._base_path}/notable/me/next')
            return response.json()
        except Exception:
            return None

    def get_recent_notable_day(self) -> dict[str, Any] | None:
        try:
            response = self._get(f'{self._base_path}/notable/me/recent')
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                return data[0]
            return None
        except Exception:
            return None

    def get_event_calendar(self, username: str | None = None, year: int = 0, month: int = 0, include_notable_days: bool = False) -> list[dict[str, Any]]:
        path = f'{self._base_path}/accounts/{username}/calendar' if username else f'{self._base_path}/accounts/me/calendar'
        response = self._get(path, params={'year': year, 'month': month, 'includeNotableDays': include_notable_days})
        return response.json()

    def get_merged_calendar(self, year: int, month: int) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/accounts/me/calendar/merged', params={'year': year, 'month': month})
        return response.json()

    def get_user_merged_calendar(self, username: str, year: int, month: int) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/accounts/{username}/calendar/merged', params={'year': year, 'month': month})
        return response.json()

    def list_calendar_events(self, start_time: str | None = None, end_time: str | None = None, offset: int = 0, take: int = 50) -> PaginatedResult[dict[str, Any]]:
        params = {'offset': offset, 'take': take}
        if start_time is not None:
            params['startTime'] = start_time
        if end_time is not None:
            params['endTime'] = end_time
        response = self._get(f'{self._base_path}/accounts/me/calendar/events', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def create_calendar_event(self, title: str, start_time: str, end_time: str, description: str | None = None, location: str | None = None, is_all_day: bool = False, visibility: int = 0, recurrence: dict[str, Any] | None = None, meta: dict[str, Any] | None = None, icon_id: str | None = None, background_id: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'title': title, 'start_time': start_time, 'end_time': end_time, 'description': description, 'location': location, 'is_all_day': is_all_day, 'visibility': visibility, 'recurrence': recurrence, 'meta': meta, 'icon_id': icon_id, 'background_id': background_id})
        response = self._post(f'{self._base_path}/accounts/me/calendar/events', json=data)
        return response.json()

    def get_calendar_event(self, id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/accounts/me/calendar/events/{id}')
        return response.json()

    def get_user_calendar_event(self, username: str, id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/accounts/{username}/calendar/events/{id}')
        return response.json()

    def update_calendar_event(self, id: str, title: str | None = None, start_time: str | None = None, end_time: str | None = None, description: str | None = None, location: str | None = None, is_all_day: bool | None = None, visibility: int | None = None, recurrence: dict[str, Any] | None = None, meta: dict[str, Any] | None = None, icon_id: str | None = None, background_id: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'title': title, 'start_time': start_time, 'end_time': end_time, 'description': description, 'location': location, 'is_all_day': is_all_day, 'visibility': visibility, 'recurrence': recurrence, 'meta': meta, 'icon_id': icon_id, 'background_id': background_id})
        response = self._put(f'{self._base_path}/accounts/me/calendar/events/{id}', json=data)
        return response.json()

    def delete_calendar_event(self, id: str) -> None:
        self._delete(f'{self._base_path}/accounts/me/calendar/events/{id}')

    def list_calendar_subscriptions(self) -> list[str]:
        response = self._get(f'{self._base_path}/accounts/me/calendar/subscriptions')
        return response.json()

    def subscribe_to_calendar(self, account_id: str) -> None:
        self._post(f'{self._base_path}/accounts/me/calendar/subscriptions/{account_id}')

    def unsubscribe_from_calendar(self, account_id: str) -> None:
        self._delete(f'{self._base_path}/accounts/me/calendar/subscriptions/{account_id}')

    def list_calendar_subscribers(self) -> list[str]:
        response = self._get(f'{self._base_path}/accounts/me/calendar/subscriptions/subscribers')
        return response.json()

    def get_event_countdowns(self, take: int = 5, offset: int = 0, include_notable_days: bool = True, tag: str | None = None) -> PaginatedResult[dict[str, Any]]:
        params = self._clean_none({'take': take, 'offset': offset, 'includeNotableDays': include_notable_days, 'tag': tag})
        response = self._get(f'{self._base_path}/accounts/me/calendar/countdown', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_user_event_countdowns(self, username: str, take: int = 5, offset: int = 0, include_notable_days: bool = True, tag: str | None = None) -> PaginatedResult[dict[str, Any]]:
        params = self._clean_none({'take': take, 'offset': offset, 'includeNotableDays': include_notable_days, 'tag': tag})
        response = self._get(f'{self._base_path}/accounts/{username}/calendar/countdown', params=params)
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_social_credits(self) -> float:
        response = self._get(f'{self._base_path}/accounts/me/credits')
        value = response.json()
        if isinstance(value, (int, float)):
            return float(value)
        return 0.0

    def get_social_credit_history(self, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/accounts/me/credits/history', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_abuse_report_types(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/abuse-reports/types')
        return response.json()

    def submit_abuse_report(self, target_id: str, target_type: str, report_type: int, description: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'target_id': target_id, 'target_type': target_type, 'report_type': report_type, 'description': description})
        response = self._post(f'{self._base_path}/abuse-reports', json=data)
        return response.json()

    def get_action_log(self, offset: int = 0, take: int = 20) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/actions/log', params={'offset': offset, 'take': take})
        return response.json()

    def get_account_timeline(self, username: str, offset: int = 0, take: int = 20) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/accounts/{username}/timeline', params={'offset': offset, 'take': take})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def create_affiliation_spell(self, spell: str | None = None) -> dict[str, Any]:
        data = self._clean_none({'spell': spell})
        response = self._post(f'{self._base_path}/affiliations', json=data)
        return response.json()

    def list_affiliation_spells(self, order: str = 'date', desc: bool = False, take: int = 20, offset: int = 0) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/affiliations', params={'order': order, 'desc': desc, 'take': take, 'offset': offset})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def get_affiliation_spell(self, id: str) -> dict[str, Any]:
        response = self._get(f'{self._base_path}/affiliations/{id}')
        return response.json()

    def list_affiliation_results(self, id: str, desc: bool = False, take: int = 20, offset: int = 0) -> PaginatedResult[dict[str, Any]]:
        response = self._get(f'{self._base_path}/affiliations/{id}/results', params={'desc': desc, 'take': take, 'offset': offset})
        total_count = self._get_total_count(response)
        return PaginatedResult(items=response.json(), total_count=total_count)

    def delete_affiliation_spell(self, id: str) -> None:
        self._delete(f'{self._base_path}/affiliations/{id}')

    def join_realm(self, realm_slug: str) -> None:
        self._post(f'{self._base_path}/realms/{realm_slug}/members/me')

    def leave_realm(self, realm_slug: str) -> None:
        self._delete(f'{self._base_path}/realms/{realm_slug}/members/me')

    def get_my_realms(self) -> list[dict[str, Any]]:
        response = self._get(f'{self._base_path}/realms/members/me')
        return response.json()
