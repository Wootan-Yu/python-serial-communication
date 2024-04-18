String command;
#define ENA 7
#define IN1 6
#define IN2 5
#define IN3 4
#define IN4 3
#define ENB 2


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  while(!Serial){}

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);

  analogWrite(ENA, 255); //255
  analogWrite(ENB, 255); //255

  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void loop() {
  
  if(Serial.available() > 0) // do not put a delay() inside this 'if statement'
  {
    command = Serial.readStringUntil('\n');
    //command.trim();
    //Serial.print(command + '\n'); // used only for debug, must delete after use

    if(command.equals("left"))
    {
      //Serial.println("left");
      digitalWrite(IN1, HIGH); //LEFT
      digitalWrite(IN2, LOW);
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, LOW);
    }
    else if(command.equals("right"))
    {
      //Serial.println("right");
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      digitalWrite(IN3, HIGH); //RIGHT
      digitalWrite(IN4, LOW);
    }
    else if(command.equals("center"))
    {
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      digitalWrite(IN3, HIGH);
      digitalWrite(IN4, LOW);
    
    }
  }
}
