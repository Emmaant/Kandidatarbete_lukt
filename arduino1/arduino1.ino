

int sensor1 = A0;
int sensor2 = A1;
int sensor3 = A2;
int sensor4 = A3;


String label1 = "sensor1";
String label2 = "sensor2";
String label3 = "sensor3";
String label4 = "sensor4";



int freq = 10; //Collect data every 100 ms
int sensorvalue1;
int sensorvalue2;
int sensorvalue3;
int sensorvalue4;




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
    
  sensorvalue1 = analogRead(sensor1);
  sensorvalue2 = analogRead(sensor2);
  sensorvalue3 = analogRead(sensor3);
  sensorvalue4 = analogRead(sensor4);
  
  //float	voltage	=	sensorvalue1	*	5.0;
  //voltage	/=1024.0;	 
  //threshold?
  Serial.print(sensorvalue1);
  Serial.print(',');
  Serial.print(sensorvalue2);
  Serial.print(',');
  Serial.print(sensorvalue3);
  Serial.print(',');
  Serial.print(sensorvalue4);
  
  Serial.println();    

  delay(freq);

}
