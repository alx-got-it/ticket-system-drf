from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_core.models import Ticket, Location, Regularity


def populate_db():
    
    location_1 = Location(name='Питер: Лахта', adress='адрес', slug='lahta')
    location_1.save()
    
    location_2 = Location(name='Москва: Кисельный', adress='адрес', slug='kiselny')
    location_2.save()
    
    location_3 = Location(name='Туапсе: Агой', adress='адрес', slug='agoy')
    location_3.save()
    
    location_4 = Location(name='Крым: Узунджа', adress='адрес', slug='uzunja')
    location_4.save()
    
    location_5 = Location(name='Томск', adress='адрес', slug='tomsk')
    location_5.save()
    
    location_6 = Location(name='Удаленно', adress='адрес', slug='distant')
    location_6.save()
    
    regularity_1 = Regularity(name='Постоянно')
    regularity_1.save()
    
    regularity_2 = Regularity(name='Срочно')
    regularity_2.save()
    
    regularity_3 = Regularity(name='Единожды')
    regularity_3.save()
    
    ticket_1 = Ticket(header='', text='', location=location_1, regularity=regularity_1, manager='Ядумани',
                      contact='yadu@t.me')
    ticket_1.save()
    
    ticket_2 = Ticket(header='', text='', location=location_2, regularity=regularity_2, manager='Надия',
                      contact='nadiya@t.me')
    ticket_2.save()
    
    ticket_3 = Ticket(header='', text='', location=location_3, regularity=regularity_3, manager='Васудха',
                      contact='vasu@t.me')
    ticket_3.save()
    
    ticket_4 = Ticket(header='', text='', location=location_4, regularity=regularity_1, manager='Сатья',
                      contact='satya@t.me')
    ticket_4.save()
    
    ticket_5 = Ticket(header='', text='', location=location_5, regularity=regularity_2, manager='Арджуна',
                      contact='arjun@t.me')
    ticket_5.save()
    
    ticket_6 = Ticket(header='', text='', location=location_6, regularity=regularity_3, manager='Ананта Кришна',
                      contact='litand@t.me')
    ticket_6.save()
    
    print('DB successfully populated')


populate_db()
