#include "MQ135.h"

#define ANALOGPIN A0 //  Define Analog PIN on Arduino Board
#define RZERO 206.85 //  Define RZERO Calibration Value

MQ135 gasSensor = MQ135(ANALOGPIN);

void setup()
{
  Serial.begin(9600);
  delay(500); //Delay to let system boot
  float rzero = gasSensor.getRZero();
  delay(3000);
} //end "setup()"

void loop()
{
  //Start of Program
  float ppm = gasSensor.getPPM();
  char ppm_char[10];
  dtostrf(ppm, 6, 4, ppm_char);
  String result = "{'humidity': ";
  result.concat(0);
  result.concat(',');
  result.concat("'co2':");
  result.concat(ppm_char);
  result.concat('}');
  Serial.println(result);

  delay(5000); //Wait 5 seconds before accessing sensor again.

}