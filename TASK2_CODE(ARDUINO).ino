// declare variables
int sensorpin = A0;  // sensor pin
int sensor;
int s=0;
int q=0;
// sensor readings
// LED pins
int led1 = 8;
int led2 = 9;
int led3 = 10;
int led4 = 11;
int led5 = 13;




const int WINDOW_SIZE = 3;     // Number of samples in moving average
double buffer[WINDOW_SIZE];    // Store values
int index = 0;                 // Current position
int count = 0;                 // How many values have been inserted
double sum = 0;                // Running sum

double movingAverage(double newValue) {
  sum -= buffer[index];
  buffer[index] = newValue;
  sum += newValue;
  index = (index + 1) % WINDOW_SIZE;
  if (count < WINDOW_SIZE) count++;
  return sum / count;
}

void setup() {
  // set LED pins as outputs
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
  pinMode(led3,OUTPUT);
  pinMode(led4,OUTPUT);
  pinMode(led5,OUTPUT);
  // initialize serial communication
  Serial.begin(9600);
}

void loop(){
  // read sensor value
  sensor = analogRead(sensorpin);
  // print sensor value
  Serial.println(sensor);
  
  double val = sensor;
  double avg = movingAverage(val);
  Serial.print(" -> Moving average: ");
  Serial.println(avg);
  
  
  // turn on LEDs if sensor reading hits a certain value
  if(avg<s && s<q){
    digitalWrite(8,HIGH);
    digitalWrite(9,LOW);
    digitalWrite(11,LOW);
    digitalWrite(13,LOW);
  }
  else if(avg==s){
    digitalWrite(8,LOW);
    digitalWrite(9,HIGH);
    digitalWrite(11,LOW);
    digitalWrite(13,LOW);
  }
  else if(avg>s && s<q){
    digitalWrite(8,LOW);
    digitalWrite(9,LOW);
    digitalWrite(11,HIGH);
    digitalWrite(13,HIGH);
  }
  else if(avg>s && s>q){
    digitalWrite(8,LOW);
    digitalWrite(9,LOW);
    digitalWrite(11,HIGH);
    digitalWrite(13,LOW);
  }
  q=s;
  s=avg;
    
}
