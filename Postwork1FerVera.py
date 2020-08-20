#Tarea de Postwork sesión 1
print("*************Tarea de Postwork sesión 1**********************")
print("*************************************************************")

print("Favor de introducir los siguentes datos de su tarjeta:")
ok = "n"
while ok == "n":

    print("Nombre:") 
        nombre = input()
	    print("Tasa de Interes Anual:") 
	        rate = int(input())
		    print("Dueda mes pasado:")
		        deuda = int(input())
			    print("Pago a realizar:")
			        pago = int(input())
				    while deuda <= pago :
				            print("Pago mayor a deuda, favor de corregir,")
					            print("Pago a realizar:")
						            pago=int(input())
							        print("Importe total de nuevos cargos:")   
								    cargos = int(input())




								        print("Confirmo sus datos:")
									    print("Sr(a). {} una tasa de interes del {} %, una deuda de {} su pago será de {}  sus nuevos cargos {}".format(nombre,rate, deuda, pago, cargos))

									        print("los datos son correctos Y/N:")  
										    ok = input() 

										    # interes_mensual = tasa_interes/12 deuda_recalculada = (deuda - pago)*(1+interes_mensual) nueva_deuda = deuda_recalculada + cargos
										    intMensual = (rate / 12)/100
										    deudaActual = (deuda - pago)*(1+intMensual)
										    nuevaDeuda = deudaActual + cargos

										    print("*************************************************************")
										    print("*************************************************************")
										    print(" ")
										    print("Interes Mensual :{}".format(intMensual) )
										    print("Su Deuda actual es de :{}".format(deudaActual) )

										    print("{}, su pago para no generar intereses es de :{}".format(nombre,nuevaDeuda) )
										    print("*************************************************************")
										    print("*************************************************************")

