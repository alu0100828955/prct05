#! encoding: UTF-8
#! /usr/bin/python
n=int(raw_input("Introduzca el numero de subintervalos deseado: "))
while n>0 and:
 suma=0
 PI=3.1415926535897931159979634685441852
 for i in range (1,n+1):
   a=float(i-1)/n
   b=float(i)/n
   x_i=float(i-0.5)/n
   fx_i=float(4.0/(1.0 + x_i*x_i))
   suma+=fx_i
   pi=float(suma/n)
   print "El intervalo %d es: [%3.2f, %3.2f]" %(i,a,b)
   print "El punto x_i es: %4.3f" %(x_i)
   print "fx_i: %6.5f" %(fx_i)
 print "El valor aporximado de pi es: %f" %(pi)
 print "El valor de pi con 35 decimales es: %36.35f" %(PI)