"""Unit tests for profile data formatting and health validation."""
import unittest
from unittest.mock import Mock, patch
import requests
from scripts.update_profile_data import (
    ACTIVITY_END, ACTIVITY_START, DATA_END, DATA_START,
    check_production, format_recent_activity, replace_marked_section,
)
class ReplaceSectionTests(unittest.TestCase):
    def test_replaces_only_content_between_markers(self):
        original = f"before\n{DATA_START}\nold\n{DATA_END}\nafter"
        self.assertEqual(replace_marked_section(original, DATA_START, DATA_END, "new"),
                         f"before\n{DATA_START}\nnew\n{DATA_END}\nafter")
    def test_missing_or_duplicate_markers_fail_closed(self):
        with self.assertRaises(RuntimeError):
            replace_marked_section("README without markers", DATA_START, DATA_END, "x")
        duplicate = f"{DATA_START}{DATA_END}{DATA_START}{DATA_END}"
        with self.assertRaises(RuntimeError):
            replace_marked_section(duplicate, DATA_START, DATA_END, "x")
    def test_activity_markers_are_distinct_from_data_markers(self):
        self.assertNotEqual(ACTIVITY_START, DATA_START)
        self.assertNotEqual(ACTIVITY_END, DATA_END)
class ActivityTests(unittest.TestCase):
    def test_empty_events_are_honest(self):
        self.assertEqual(format_recent_activity([]), "_No recent public activity available._")
    def test_unknown_events_are_not_rendered(self):
        self.assertEqual(format_recent_activity([{"type": "PrivateLikeEvent", "repo": {"name": "a/b"}}]),
                         "_No recent public activity available._")
    def test_public_repo_activity_is_rendered(self):
        result = format_recent_activity([{"type": "PushEvent", "repo": {"name": "dhe-cruzer69/x4-core"}}])
        self.assertIn("https://github.com/dhe-cruzer69/x4-core", result)
        self.assertIn("pushed commits", result)
class ProductionCheckTests(unittest.TestCase):
    def test_blank_url_is_not_live(self):
        self.assertEqual(check_production(""), ("Not configured", ""))
    def test_http_and_local_urls_are_rejected(self):
        self.assertEqual(check_production("http://example.com")[0], "Invalid URL configuration")
        self.assertEqual(check_production("https://localhost")[0], "Invalid URL configuration")
        self.assertEqual(check_production("https://127.0.0.1")[0], "Invalid URL configuration")
    @patch("scripts.update_profile_data.requests.get")
    def test_ready_status_and_version_are_required(self, get):
        get.return_value = Mock(status_code=200, json=lambda: {"status": "ready", "version": "0.3.0"})
        self.assertEqual(check_production("https://example.com"), ("Live and ready", "0.3.0"))
        get.return_value = Mock(status_code=200, json=lambda: {"status": "live", "version": "0.3.0"})
        self.assertEqual(check_production("https://example.com"), ("Unhealthy (invalid readiness response)", ""))
    @patch("scripts.update_profile_data.requests.get")
    def test_network_errors_are_not_live(self, get):
        get.side_effect = requests.Timeout("timed out")
        self.assertEqual(check_production("https://example.com"), ("Unreachable or invalid response", ""))
if __name__ == "__main__":
    unittest.main()
