"""Reservación BEDU Travels"""

habitacion_doble = 150000.00
transporte = 3000.00
reservacion_evento = 3999.99
tour_lancha = 21750.00
alimentos_bebidas = 5000

print('-----------------------------------------------------------------')
print('RESERVACION                                        | PRECIO')
print('-----------------------------------------------------------------')
print('Habitación doble                                   |   {}'.format(habitacion_doble))
print('Transporte                                         |    {}'.format(transporte))
print('Reservación en evento                              |    {}'.format(reservacion_evento))
print('Tour en lancha                                     |   {}'.format(tour_lancha))
print('Alimentos y bebidas                                |    {}'.format(alimentos_bebidas))
print('-----------------------------------------------------------------')
print('                                              Total|  {}'.format(
    habitacion_doble + transporte + reservacion_evento + tour_lancha + alimentos_bebidas
))