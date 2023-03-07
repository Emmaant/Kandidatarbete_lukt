

int sensor1 = A0;
String label1 = "sensor1";


int freq = 1000; //Collect data every 1000 ms
int sensorvalue1;
bool start = true; 


void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  pinMode(sensor1,INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  //while (start) {
   // Serial.print(label1);
    //Serial.println();
    //start = false;
  //}
    
  sensorvalue1 = analogRead(sensor1);
  //float	voltage	=	sensorvalue1	*	5.0;
  //voltage	/=1024.0;	 
  //threshold?
  Serial.print(sensorvalue1);
  Serial.println();    

  delay(freq);

}
