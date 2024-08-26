const int END_LOOP = 1000000000; // 1 Mrd.

void main() {
  int lastNumber = 0;

  for (int i = 0; i < END_LOOP; i++) {
    lastNumber++;
  }
  print('Dart:last_number=$lastNumber\n--');
}
