# -*- coding: utf-8 -*-
import database as db
import afiliaciones as af
import psycopg2
import psycopg2.extras
import unittest
import cliente as cl
import moduloCliente as mc
import consumos
import productos as pr
import validacion
import dbparams
import datetime
from metodoFacturacion import metodoFacturacion
from gestionarConsumos import buscarConsumosporServicio

class metodoFacturacionPrepago(metodoFacturacion):
    
    def __init__(self,Cliente,Producto,numSerie,obs):
        self.numSerie = numSerie
        self.producto = Producto
        self.cliente = Cliente
        self.obs = obs
        self.dia = ""
        self.mes = ""
        self.anio = ""
        self.listaConsumos = self.facturar()
        
    def facturar(self):
        
        planAsociado = af.ConsultarPlanesPrepago(self.numSerie)[0][0]
        
        conexion = db.operacion("", """select max(to_char(fecha, 'DD MM YYYY')) from recarga where numserie=\'%s\' group by(numserie);""" %  self.numSerie,
                                          dbparams.dbname,dbparams.dbuser,dbparams.dbpass)
        
        resultado = conexion.execute()
        
        if(len(resultado) > 0):
            fechaUltimaRecarga = resultado[0][0]
        
            listaFecha = fechaUltimaRecarga.split(" ", 2)
            
            self.dia = listaFecha[0]

            self.mes = listaFecha[1]
            
            self.anio = listaFecha[2]
            
            conexion = db.operacion("", """ select to_char(fecha, 'DD MM YYYY'), cantidad, nombreserv from consume NATURAL JOIN servicio where fecha >= to_date('%s %s %s','DD MM YYYY') 
                                            and numserie = \'%s\'; """ %(self.dia ,self.mes, self.anio, self.numSerie),
                                          dbparams.dbname,dbparams.dbuser,dbparams.dbpass)
	    print db.operacion.comando
	    
	    consumos = conexion.execute()
	    
	    #for i in consumos:
	      #print i
       
            return consumos
            
        return []
                
    def __str__(self):
        now = datetime.datetime.now()
        string = '\n=========================================================================================================='
        string += '\n{0:50}FACTURA'.format(' ') + '{0:20}Fecha de emisión: '.format(' ') + str(now.strftime("%d-%m-%Y")) + '\n' + str(self.cliente)
        string += '\n' + str(self.producto)
        string += '\n\n\n{2:40}SERVICIOS CONSUMIDOS DESDE (%s-%s-%s)\n\n{0:30} | {1:20} | {2:20}'.format('SERVICIO', 'TOTAL CONSUMIDO','FECHA',' ') % (self.dia, self.mes,self.anio)
        string += '\n----------------------------------------------------------------------------------------------------------'
        for consumo in self.listaConsumos:
            string += '\n{0:30} | {1:20} | {2:20}'.format \
                        (consumo[2], consumo[1], consumo[0])
        string += '\n----------------------------------------------------------------------------------------------------------'
        string += '\n==========================================================================================================\n'
        string += 'Observaciones: ' + str(self.obs) + '\n'
        return string

if __name__=='__main__':
    factura = metodoFacturacionPrepago('22714709','CBZ27326','')
    factura.facturar()
    print factura