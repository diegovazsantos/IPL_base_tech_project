## Config

File:  `settings.py`. 
Porta da API definida do atributo API_PORT, default `8092`.

### Consumo

Pode-se usar a collection Postman na pasta `\postman` ou acessar a UI abaixo, onde todos endPoints estao listados:

```
http://localhost:8092/tracking/ui/
```

## Endpoints

    - GET 

        /telemetryDatas
        Select * na tabela de dados de telemetria.
        
        /GeoDatas
        Select * na tabela de dados geograficos.

    - POST 
        /telemetryDatas
        Cria uma nova entrada de dados de telemetria.
            {
          "vehicle_id": "544bca0c-c9dc-46f6-9bcd-ce2c85271b56",
          "date_time": "1982-06-06T00:00:00",
              "value": 80,
              "type": "SPEED"
            }
            
        /telemetryDatas
        Cria uma nova entrada de dados geograficos.       
            {
          "vehicle_id": "544bca0c-c9dc-46f6-9bcd-ce2c85271b56",
          "date_time": "1982-06-06T00:00:00+02:00",
              "latitude": -22.9786186,
              "longitude": -43.2213697,
              "altimeter": 0
            }
