precio_producto=1200
cantidad=3
descuento=10

total_sin_descuento=precio_producto*cantidad
print(f'El precio total sin descuento es {total_sin_descuento}')

monto_descuento=total_sin_descuento*descuento/100
print(f'El monto del descuento es {monto_descuento}')

total_con_descuento=total_sin_descuento-monto_descuento
print(f'El precio total con descuento es {total_con_descuento}')

print(f'Total sin descuento:{total_sin_descuento}\n',
      f'Monto de descuento:{monto_descuento}\n',
      f'Total con descuento:{total_con_descuento}')

