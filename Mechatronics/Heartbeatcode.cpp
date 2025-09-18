const int RED_LED = 4;
const int ORANGE_LED = 5;
const int GREEN_LED = 6;
const int HEART_SENSOR = A0;

const int LOW_BPM = 60;
const int HIGH_BPM = 100;

#define SAMP_SIZE 4
#define RISE_THRESHOLD 4

const int MIN_SIGNAL = 500;
const unsigned long WINDOW_MS = 5000UL; // 5-second window

void setup() {
  Serial.begin(9600);
  pinMode(RED_LED, OUTPUT);
  pinMode(ORANGE_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);

  digitalWrite(RED_LED, LOW);
  digitalWrite(ORANGE_LED, LOW);
  digitalWrite(GREEN_LED, LOW);
}

void loop() {
  float reads[SAMP_SIZE] = {0};
  float sum = 0, last = 0, before = 0;
  bool rising = false;
  int rise_count = 0;
  int ptr = 0;

  unsigned long last_beat = millis();
  unsigned long windowStart = millis();
  int beatsInWindow = 0;

  while (true) {
    float reader = 0.0;
    int n = 0;
    unsigned long start = millis();
    do {
      reader += analogRead(HEART_SENSOR);
      n++;
    } while (millis() < start + 20);
    reader /= (float)n;

    if (reader < MIN_SIGNAL) {
      rising = false;
      rise_count = 0;
      digitalWrite(GREEN_LED, LOW);
      digitalWrite(ORANGE_LED, LOW);
      digitalWrite(RED_LED, HIGH);
      delay(120);
      digitalWrite(RED_LED, LOW);
      delay(120);
    } else {
      sum -= reads[ptr];
      sum += reader;
      reads[ptr] = reader;
      last = sum / SAMP_SIZE;

      if (last > before) {
        rise_count++;
        if (!rising && rise_count > RISE_THRESHOLD) {
          rising = true;
          last_beat = millis();
          beatsInWindow++;
        }
      } else {
        rising = false;
        rise_count = 0;
      }

      before = last;
      ptr++;
      ptr %= SAMP_SIZE;
    }

    if (millis() - windowStart >= WINDOW_MS) {
      float avgBPM = beatsInWindow * 6.0; // 10s -> multiply by 6 for BPM
      Serial.print("BPM = ");
      Serial.println(avgBPM);

      if (beatsInWindow == 0) {
        digitalWrite(GREEN_LED, LOW);
        digitalWrite(ORANGE_LED, LOW);
        unsigned long blinkStart = millis();
        while (millis() - blinkStart < 1000) {
          digitalWrite(RED_LED, HIGH);
          delay(200);
          digitalWrite(RED_LED, LOW);
          delay(200);
        }
      } else {
        if (avgBPM < LOW_BPM) {
          digitalWrite(RED_LED, LOW);
          digitalWrite(ORANGE_LED, HIGH);
          digitalWrite(GREEN_LED, LOW);
        } else if (avgBPM <= HIGH_BPM) {
          digitalWrite(RED_LED, LOW);
          digitalWrite(ORANGE_LED, LOW);
          digitalWrite(GREEN_LED, HIGH);
        } else {
          digitalWrite(RED_LED, HIGH);
          digitalWrite(ORANGE_LED, LOW);
          digitalWrite(GREEN_LED, LOW);
        }
      }

      beatsInWindow = 0;
      windowStart = millis();
      before = 0;
    }

    if (millis() - last_beat > WINDOW_MS) {
      digitalWrite(GREEN_LED, LOW);
      digitalWrite(ORANGE_LED, LOW);
      unsigned long blinkStart = millis();
      while (millis() - blinkStart < 800) {
        digitalWrite(RED_LED, HIGH);
        delay(150);
        digitalWrite(RED_LED, LOW);
        delay(150);
      }
      last_beat = millis();
      windowStart = millis();
      beatsInWindow = 0;
    }
  }
}
