#include <dht.h>

#define dht_apin A0 // Analog Pin sensor is connected to

dht DHT;

void setup()
{
  Serial.begin(9600);
  delay(500); //Delay to let system boot
  Serial.println("DHT11 Humidity & temperature Sensor\n\n");
  delay(1000); //Wait before accessing Sensor

} //end "setup()"

void loop()
{
  //Start of Program

  DHT.read11(dht_apin);
  String result = "{'humidity': ";
  result.concat(DHT.humidity);
  result.concat('}');
  result.concat("{'temperature':");
  result.concat(DHT.temperature);
  result.concat('}');
  Serial.println(result);

  delay(5000); //Wait 5 seconds before accessing sensor again.

  //Fastest should be once every two seconds.

} // end loop(