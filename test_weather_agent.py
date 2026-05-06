import unittest
from unittest.mock import patch

from graph import weather_agent


class MockResponse:
    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


def location_payload(
    city="Baguio City",
    region="Cordillera Administrative Region",
    country="Philippines",
    offset="+08:00",
):
    return {
        "city": city,
        "region": region,
        "country_name": country,
        "latitude": 16.4023,
        "longitude": 120.5960,
        "utc_offset": offset,
        "timezone": "Asia/Manila",
    }


def weather_payload(temperature, weathercode, is_day, windspeed=8.5):
    return {
        "current_weather_units": {
            "temperature": "C",
            "windspeed": "km/h",
        },
        "current_weather": {
            "time": "2026-05-06T10:30",
            "temperature": temperature,
            "windspeed": windspeed,
            "winddirection": 120,
            "is_day": is_day,
            "weathercode": weathercode,
        },
    }


class WeatherAgentTests(unittest.TestCase):
    def run_agent_with_payloads(self, location, weather):
        responses = [MockResponse(location), MockResponse(weather)]

        with patch("components.nodes.requests.get", side_effect=responses):
            return weather_agent.invoke(
                {
                    "name": "Aivann",
                    "location_data": None,
                    "weather_data": None,
                    "weather_info": None,
                }
            )

    def test_daytime_clear_weather_report(self):
        final_state = self.run_agent_with_payloads(
            location_payload(),
            weather_payload(temperature=24.0, weathercode=0, is_day=1),
        )

        report = final_state["weather_info"]

        self.assertIn("Good morning, Aivann!", report)
        self.assertIn("Baguio City, Cordillera Administrative Region, Philippines", report)
        self.assertIn("• Clear sky", report)
        self.assertIn("• Temperature: 24.0C (comfortable)", report)
        self.assertIn("• Wind: 8.5 km/h", report)

    def test_nighttime_rain_weather_report(self):
        final_state = self.run_agent_with_payloads(
            location_payload(
                city="London",
                region="England",
                country="United Kingdom",
                offset="+00:00",
            ),
            weather_payload(temperature=7.0, weathercode=63, is_day=0, windspeed=14.0),
        )

        report = final_state["weather_info"]

        self.assertIn("Good evening, Aivann!", report)
        self.assertIn("London, England, United Kingdom", report)
        self.assertIn("• Moderate rain", report)
        self.assertIn("• Temperature: 7.0C (cold)", report)
        self.assertIn("• Wind: 14.0 km/h", report)

    def test_missing_location_field_is_reported(self):
        bad_location = location_payload()
        bad_location.pop("country_name")

        with self.assertRaisesRegex(Exception, "Missing required field: country_name"):
            self.run_agent_with_payloads(
                bad_location,
                weather_payload(temperature=20.0, weathercode=2, is_day=1),
            )


if __name__ == "__main__":
    unittest.main()