## Config

File: application.properties

Porta da API definida do atributo server.port, default 8091
URL PostgreSQL definida no atributo spring.datasource.url, default jdbc:postgresql://localhost:5432/xpto_vehicle

### Consumo

Usar a coleção teste no arquivo Vehicle.postman.json

## Endpoints

    - GET 

        /vehicles
        Select * na tabela de veiculos.

        /vehicles/{id}

        Substitua {id} pelo id  a ser pesquisado
        
        /vehicles?plate={placa}

        Substitua {placa} pela placa a ser pesquisado

    - POST 
        /vehicles
        Cria um novo veículo com os detalhes especificados.
            {
                "currentDriver": "f069f7b1-cc2a-42d8-94b4-ea6f9170dfee",
                "telemetryProfile": "1ad86270-8bb5-4753-b664-79ac45e6de33",
                "customerOwner": "8e134961-c283-4fa6-ba1f-e9548c4043db",
                "color": "Black Pianno",
                "vin": "ABCEDABCEDABCEDFG",
                "plate": "BJ20CE"
            }


    - PUT 
    /vehicles/{id}
    Atualiza os detalhes do veículo com o ID especificado.
        {
            "currentDriver": "f069f7b1-cc2a-42d8-94b4-ea6f9170dfee",
            "telemetryProfile": "1ad86270-8bb5-4753-b664-79ac45e6de33",
            "customerOwner": "8e134961-c283-4fa6-ba1f-e9548c4043db",
            "color": "Black Pianno",
            "vin": "ABCEDABCEDABCEDFG",
            "plate": "BJ20CE"
        }


    - DELETE 
    /vehicles/{id}
    Exclui o veículo com o ID especificado.