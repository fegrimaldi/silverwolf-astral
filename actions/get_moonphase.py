"""
Copyright 2016 Brocade Communications Systems, Inc.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from lib import action

def get_lunar_phase(day):
    if 0 <= day <= 3.499:
        return "New moon"
    elif 3.5 <= day <= 6.999:
        return "Waxing crescent"
    elif 7 <= day <= 10.499:
        return "First quarter"
    elif 10.5 <= day <= 13.999:
        return "Waxing gibbous"
    elif 14 <= day <= 17.499:
        return "Full moon"
    elif 17.5 <= day <= 20.999:
        return "Waning gibbous"
    elif 21 <= day <= 24.499:
        return "Last quarter"
    elif 24.5 <= day <= 27.999:
        return "Waning crescent"
    else:
        return "Invalid day"


class GetMoonPhaseAction(action.BaseAction):
    def run(self):
        return get_lunar_phase(round(self.moon['phase'], 3))
