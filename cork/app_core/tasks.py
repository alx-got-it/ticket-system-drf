from celery import shared_task

from app_core.models import Ticket


@shared_task()
def task_execute(job_params):
    ticket = Ticket.objects.get(pk=job_params["db_id"])
    print(f'Ticket done by celery task:\n{ticket.header}\n')

    # assignment.sum = assignment.first_term + assignment.second_term
    # assignment.save()
