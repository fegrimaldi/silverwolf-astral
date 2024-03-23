from st2reactor.sensor.base import PollingSensor
import st2common.util.date as date

from astral import LocationInfo, sun

__all__ = [
    'AstralSunSensor'
]


class AstralSunSensor(PollingSensor):
    def __init__(self, sensor_service, config=None, poll_interval=None):
        super(AstralSunSensor, self).__init__(sensor_service=sensor_service,
                                              config=config,
                                              poll_interval=poll_interval)
        self._logger = self._sensor_service.get_logger(__name__)

    def setup(self):
        self._latitude = self._config['latitude']
        self._longitude = self._config['longitude']
        self._update_sun_info()
        self._update_counter = 0

    def poll(self):
        if self._update_counter > 60:
            self._update_sun_info()
            self._update_counter = 0

        checks = ['dawn', 'sunrise', 'sunset', 'dusk']

        currenttime = date.get_datetime_utc_now()

        self._logger.debug("Checking current time %s for sun information" %
                           str(currenttime))

        for key in checks:
            if self.is_within_minute(self.sun[key], currenttime):
                trigger = 'astral.' + key
                self.sensor_service.dispatch(trigger=trigger, payload={})

        self._update_counter += 1

    def cleanup(self):
        pass

    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass

    def _update_sun_info(self):
        location = LocationInfo('name', 'region', 'GMT+0', float(self._latitude),
                            float(self._longitude))
        self.sun = sun(location.observer)

 

    def is_within_minute(self, time1, time2):
        timediff = time1 - time2
        diff = abs(timediff.total_seconds() // 60)
        if diff < 1:
            return True
        return False
