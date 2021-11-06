## IoT project - Moisture Level

An IoT project I did in a course at Linnaeus University. A thing, a moisture sensor, is sending the moisture level from a plant via an MQTT broker (CloudMQTT) to a backend server. A frontend is displaying the data that is fetched from the backend server. Notifications are sent from the backend to the user’s connected Telegram account via a Telegram bot. 

### Repositories in project
Thing - [https://github.com/christoffergranstedt/lnu-iot-moisture-thing](https://github.com/christoffergranstedt/lnu-iot-moisture-thing)  
Backend - [https://github.com/christoffergranstedt/lnu-iot-moisture-backend](https://github.com/christoffergranstedt/lnu-iot-moisture-backend)  
Frontend - [https://github.com/christoffergranstedt/lnu-iot-moisture-frontend](https://github.com/christoffergranstedt/lnu-iot-moisture-frontend)  

### Thing repository
This is the thing repository. A thing, a sensor that measures the mositure level in a plant and publish that data on a topic via a MQTT broker that a backend server is listening too. Currently the thing is not in use.