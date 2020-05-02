
// assign pin num
int right_pin = 12;
int left_pin = 13;
int const ENA = 10;  
int const ENB = 11; 


// initial command
int command = 0;

void setup()

{
  pinMode(right_pin, OUTPUT);
  pinMode(left_pin, OUTPUT);
  pinMode(ENA, OUTPUT);   // set all the motor control pins to outputs
  pinMode(ENB, OUTPUT);

  Serial.begin(115200);
  
  while (!Serial);
  
  Serial.println("Opencv Self Driving Robot");

}

void loop() {

if (Serial.available())

{
  //int state = Serial.parseInt();
  int state = Serial.read();

  if (state == 4)
  {
    
    digitalWrite(left_pin, LOW);
    digitalWrite(right_pin, HIGH);
    digitalWrite(ENA, HIGH);
    digitalWrite(ENB, HIGH);
    Serial.println("Left");
  }

  if (state == 2)
  {
    digitalWrite(left_pin, LOW);
    digitalWrite(right_pin, LOW);
    digitalWrite(ENA, HIGH);
    digitalWrite(ENB, HIGH);
    Serial.println("Right");
    Serial.println("Reverse");
  }

  if (state == 3)
  {
  
    digitalWrite(left_pin, HIGH);
    digitalWrite(right_pin, LOW);
    digitalWrite(ENA, HIGH);
    digitalWrite(ENB, HIGH);

  Serial.println("Right");
  }
  if (state == 1)
  {
  
    digitalWrite(left_pin, HIGH);
    digitalWrite(right_pin, HIGH);
    digitalWrite(ENA, HIGH);
    digitalWrite(ENB, HIGH);

  Serial.println("Forward");
  }
  if (state == 5)
  {
  
    digitalWrite(left_pin, LOW);
    digitalWrite(right_pin, LOW);
    digitalWrite(ENA, LOW);
    digitalWrite(ENB, LOW);

  Serial.println("Stop");
  }

}

}
/*
void loop() {
  //receive command
  if (Serial.available() > 0){
    command = Serial.read();
  }
  else{
    reset();
  }
   send_command(command);
}

void right(){
  Serial.print("Right Command\n");
  
  //delay(time);
}

void left(){
  Serial.print("left Command\n");
  digitalWrite(left_pin, LOW);
  //delay(time);
}

void forward(){
  digitalWrite(forward_pin, LOW);
  //delay(time);
}

void reverse(){
  digitalWrite(reverse_pin, LOW);
  //delay(time);
}

void forward_right(){
  digitalWrite(forward_pin, LOW);
  digitalWrite(right_pin, LOW);
  //delay(time);
}

void reverse_right(){
  digitalWrite(reverse_pin, LOW);
  digitalWrite(right_pin, LOW);
  //delay(time);
}

void forward_left(){
  digitalWrite(forward_pin, LOW);
  digitalWrite(left_pin, LOW);
  //delay(time);
}

void reverse_left(){
  digitalWrite(reverse_pin, LOW);
  digitalWrite(left_pin, LOW);
  //delay(time);
}

void reset(){
  digitalWrite(right_pin, HIGH);
  digitalWrite(left_pin, HIGH);
  digitalWrite(forward_pin, HIGH);
  digitalWrite(reverse_pin, HIGH);
}

void send_command(int command){
  switch(command){

     //reset command
     case 0: reset(); break;

     // single command
     case 1: forward(); break;
     case 2: reverse(); break;
     case 3: right(); break;
     case 4: left(); break;

     //combination command
     case 6: forward_right(); break;
     case 7: forward_left(); break;
     case 8: reverse_right(); break;
     case 9: reverse_left(); break;

     default: Serial.print("Inalid Command\n");
    }
}*/
/*
// assign pin num
int right_pin = 10;
int left_pin = 12;
int forward_pin = 11;
int reverse_pin = 13;

// duration for output
int time = 50;
// initial command
int command = 0;

void setup() {
  pinMode(right_pin, OUTPUT);
  pinMode(left_pin, OUTPUT);
  pinMode(forward_pin, OUTPUT);
  pinMode(reverse_pin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  //receive command
  if (Serial.available() > 0){
    command = Serial.read();
  }
  else{
    reset();
  }
   send_command(command,time);
}

void right(int time){
  digitalWrite(right_pin, LOW);
  delay(time);
}

void left(int time){
  digitalWrite(left_pin, LOW);
  delay(time);
}

void forward(int time){
  digitalWrite(forward_pin, LOW);
  delay(time);
}

void reverse(int time){
  digitalWrite(reverse_pin, LOW);
  delay(time);
}

void forward_right(int time){
  digitalWrite(forward_pin, LOW);
  digitalWrite(right_pin, LOW);
  delay(time);
}

void reverse_right(int time){
  digitalWrite(reverse_pin, LOW);
  digitalWrite(right_pin, LOW);
  delay(time);
}

void forward_left(int time){
  digitalWrite(forward_pin, LOW);
  digitalWrite(left_pin, LOW);
  delay(time);
}

void reverse_left(int time){
  digitalWrite(reverse_pin, LOW);
  digitalWrite(left_pin, LOW);
  delay(time);
}

void reset(){
  digitalWrite(right_pin, HIGH);
  digitalWrite(left_pin, HIGH);
  digitalWrite(forward_pin, HIGH);
  digitalWrite(reverse_pin, HIGH);
}

void send_command(int command, int time){
  switch (command){

     //reset command
     case 0: reset(); break;

     // single command
     case 1: forward(time); break;
     case 2: reverse(time); break;
     case 3: right(time); break;
     case 4: left(time); break;

     //combination command
     case 6: forward_right(time); break;
     case 7: forward_left(time); break;
     case 8: reverse_right(time); break;
     case 9: reverse_left(time); break;

     default: Serial.print("Inalid Command\n");
    }
}*/
