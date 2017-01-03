# --*-- coding: utf-8 --*--

"""schedule jobs
implements by multi-threads
"""

import threading
import time
import graphlab

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ScheduleTimer(threading.Thread):
    __metaclass__ = Singleton

    def __init__(self, seconds):
        self._run_time = seconds
        super(ScheduleTimer, self).__init__()
        self.setDaemon(True)
        self.start()

    def run(self):
        while True:
#	    import pdb
#	    pdb.set_trace()
            from main.models import Rating
	    qs = Rating.objects.all()
	    df = qs.to_dataframe(verbose=False)
	    train_data = graphlab.SFrame(df)
	    item_sim_model = graphlab.item_similarity_recommender.create(train_data, user_id='user', item_id='item', target='rating', similarity_type='cosine')
            item_sim_model.save('cf_model')

            time.sleep(self._run_time)
