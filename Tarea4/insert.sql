        insert into EMPRESA values
        (12345678,'MOCEL');
        
        insert into CLIENTE values (22714709,'Gustavo El Khoury',
        'Urb. Monte Elena Qta. Santa Teresa');
        
        insert into PRODUCTO values
        ('CBZ27326','iPhone 4S','12345678',22714709);
        
        insert into SERVICIO values
        (1001,'Segundos a MOCEL',0.1,FALSE);
        
        insert into SERVICIO values
        (1002,'Segundos a Otras Operadoras',0.2,FALSE);
        
        insert into SERVICIO values
        (1003,'Mensajes de Texto',0.5,FALSE);
        
        insert into SERVICIO values
        (1004,'Megabytes de Navegacion',0.5,FALSE);
        
        insert into PLAN values
        (3002,'Mixto Plus','Este fabuloso plan incluye todos los servicios, y 
        tarifas para excesos',211,311,'prepago');
        
        insert into INCLUYE values
        (3002,1001,0.1,200);
        
        insert into INCLUYE values
        (3002,1002,0.2,100);
        
        insert into PAQUETE values
        (4001,'PegaoSMS',100);
        
        insert into PAQUETE values
        (4002,'PegaoSegundosMOCEL',150);
        
         insert into PAQUETE values
        (4003,'PegaoSegundosOP',200);
        
        insert into PAQUETE values
        (4004,'PegaoMB',150);
        
        insert into CONTIENE values
        (4001,1003,100);
        
        insert into CONTIENE values
        (4002,1001,100);
        
        insert into CONTIENE values
        (4003,1002,100);
        
        insert into CONTIENE values
        (4004,1004,100);
        
        insert into AFILIA values
        ('CBZ27326',3002,'paquete');
        
        insert into CONTRATA values
        ('CBZ27326',4001);
        
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1001,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1001,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1001,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1001,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1001,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1001,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1001,current_date-60,20000);
        
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1002,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1002,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1002,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1002,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1002,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1002,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1001,current_date-60,20000);
        
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1003,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1003,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1003,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1003,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1003,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1003,current_date,20);
        insert into CONSUME values(
        DEFAULT,'CBZ27326',1003,current_date-60,20000);

	insert into PRODUCTO values
        ('123','iPhone 5','12345678',22714709);

