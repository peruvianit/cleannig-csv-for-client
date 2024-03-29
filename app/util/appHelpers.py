

import datetime


class AppHelpers:

    def generate_prefix_file(self):
        date_now = f"{datetime.datetime.now():%Y%m%d}"
        time_now = f"{datetime.datetime.now():%H%M%S}"

        return "{date_now}-{time_now}_".format(date_now = date_now, time_now = time_now)