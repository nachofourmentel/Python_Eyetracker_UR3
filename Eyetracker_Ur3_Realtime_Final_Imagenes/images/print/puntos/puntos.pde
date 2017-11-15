PFont myFont;

int x = 17;
int y = 17;

void setup() {
  size(1080, 1920);
  //background(255);

  myFont = createFont("Arial", 13);
  textFont(myFont);

  int x1 = width/8;
  int x2 = width/2;
  int x3 = width/8*7;

  int y1 = height/6;
  int y2 = height/2;
  int y3 = height/6*5;

  fill(0);
  text(x1 + " , " + y1, width/8 - 20, height/6 - 15);
  text(x2, width/2 - 10, height/6 - 15);
  text(x3, width/8*7 - 10, height/6 - 15);
  text(y2, width/8 - 10, height/2 - 15);
  text(y3, width/8 - 10, height/6*5 - 15);

  noFill();
  strokeWeight(5); 
  ellipse(width/8, height/6, x, y);
  ellipse(width/2, height/6, x, y);
  ellipse(width/8*7, height/6, x, y);
  ellipse(width/8, height/2, x, y);
  ellipse(width/2, height/2, x, y);
  ellipse(width/8*7, height/2, x, y);
  ellipse(width/8, height/6*5, x, y);
  ellipse(width/2, height/6*5, x, y);
  ellipse(width/8*7, height/6*5, x, y);

  saveFrame("_4.tiff");
  exit();
}