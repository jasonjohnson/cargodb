import logging


LOG = logging.getLogger(__name__)


def worker(tasks):
    while True:
        task = tasks.get()

        LOG.debug('processing task %s' % task)

        try:
            operation = OPERATIONS.get(task.pop('operation'))
            operation(**task)
        finally:
            tasks.task_done()
