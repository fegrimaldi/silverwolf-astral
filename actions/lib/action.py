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

from st2common.runners.base_action import Action

import datetime
from astral import LocationInfo
from astral.sun import sun
from astral import moon



class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self._latitude = self.config['latitude']
        self._longitude = self.config['longitude']
        self._timezone = self.config['timezone']
        self._datetime = datetime.datetime.now()

        location = LocationInfo('name', 'region', self._timezone, float(self._latitude),
                            float(self._longitude))

        self.sun = sun(location.observer, date=self._datetime, tzinfo=location.timezone)
        self.moon = {
            "rise": moon.moonrise(location.observer, date=self._datetime, tzinfo=location.timezone),
            "set": moon.moonset(location.observer, date=self._datetime, tzinfo=location.timezone),
            "phase": moon.phase(date=self._datetime)
        }
