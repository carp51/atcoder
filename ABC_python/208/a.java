import processing.serial.*;
Serial serial;//シリアル通信用クラス
/*
通信用変数
*/
int value1 = 0, value2 = 0;//インジケータの値
int comPortIndex = 0;//シリアルポート番号
int baudRate = 9600;//ボーレート
/*
初期化処理
*/
void setup(){

 serial = new Serial(this, Serial.list()[comPortIndex], baudRate);

 serial.clear();//バッファクリア

 serial.bufferUntil('\n');//改行が来るまでシリアルデータを受け取る

}
/*
描画処理
*/
void draw(){

 println("" + value1 + "," + value2);//コンソールに整数で表示

}
