int data;
bool durum1=false;

void setup() {

  pinMode(3,OUTPUT);
  pinMode(8,OUTPUT);
  Serial.begin(9600);
}

void loop() {

  if(Serial.available()>0)  
  {   
     durum1 = true;
     data = Serial.read();
     if ( data == '1') {
        digitalWrite(3,HIGH);
     }

     if ( data == '2') {
        digitalWrite(3,LOW);
     }
     
     if ( data == '3') {
        digitalWrite(8,HIGH);
     }

     if ( data == '4') {
        digitalWrite(8,LOW);
     }
  }

  


  
}
