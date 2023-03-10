

int sensor1 = A0;
int sensor2 = A1;
int sensor3 = A2;
int sensor4 = A3;
String label1 = "sensor1";


int freq = 100; //Collect data every 100 ms
int sensorValue1;
int sensorValue2;
int sensorValue3;
int sensorValue4;
bool start = true; 


void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  pinMode(sensor1,INPUT);
  pinMode(sensor2,INPUT);
  pinMode(sensor3,INPUT);
  pinMode(sensor4,INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  //while (start) {
   // Serial.print(label1);
    //Serial.println();
    //start = false;
  //}
    
  sensorValue1 = analogRead(sensor1);
  sensorValue2 = analogRead(sensor2);
  sensorValue3 = analogRead(sensor3);
  sensorValue4 = analogRead(sensor4);
  //float	voltage	=	sensorvalue1	*	5.0;
  //voltage	/=1024.0;	 
  //threshold?
  Serial.print(sensorValue1);
  Serial.print(", ");
  Serial.print(sensorValue2);
  Serial.print(", ");
  Serial.print(sensorValue3);
  Serial.print(", ");
  Serial.print(sensorValue4);
  Serial.println();    

  delay(freq);

}
