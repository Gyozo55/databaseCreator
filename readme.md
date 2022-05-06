						Multi Alarm homework 

Esentional programs you need to use this database creation script:

	-docker 20.10.14
	-docker-compose 1.17.1


How we can install docker/docker-compose to Ubuntu:

	docker: -https://docs.docker.com/engine/install/ubuntu/

	docker-compose: -https://docs.docker.com/compose/install/


How we can install docker/docker-compose to Ubuntu:


	https://docs.docker.com/desktop/windows/install/



If you use Ubuntu OS:
                                    
	-First you need to open one Terminal/Shell/Console session
	
	-You need to open ./multialarm folder
	
	-If you stand in the right folder you need to type this command in to the Terminal

		docker-compose up --build

	-Then you need to wait until all nessasery process run in background(when you launch this command first time this may 										     take a few minutes in worst case)


	-If you see this log in your Console or something like that. That's the when you need to open your web browser. 

		pgadmin_1 [83] [INFO] Booting worker with pid: 83


	-Then you need type this url to your browser search filed.

		http://localhost:5050/


	-Same as few step before when you try to connect first time this may take little time


	-When you see pgadmin 4 log in page, you need type following words:

		Email Adress / Username: pgadmin4@pgadmin.org

		Password: admin1234


	-If successfully logged in you need to connect postgresql server to pgadmin. You need to follow these steps:

		-Right click on Server icon
		-Then choose Register/Server option
		-Then one pop up box came up and you must find a name this new server(no matter what you name it)
		-Then you need set up the server connection(crucial):
			
			-Host name: postgresql_database
			-Port: 5432
			-Maintenance database: multiDb 
			-Username: admin
			-Password: admin1234

	-If you type everything right and the connection was successfull. You can see the multiDb structure.

	-Follow this path:
		
		-Servers/yourDbName/Databases/multiDb/Schemas/Tables

	-Finnaly you can see the two created databases with two version. First the base one and a second where the emploes 		 recive there payment raise.

		-CEO-s 10% raise
		-WebDeveloper-s 5% raise

	

	
