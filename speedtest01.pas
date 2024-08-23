// compile with:
// fpc speedtest01.pas -o"speedtest01_pas.bin"

program Speedtest01;

const END_LOOP : LongInt = 1000000000;

procedure Main;
var
    last_number : LongInt;
    i : LongInt;
begin
    for i := 1 to END_LOOP do
        last_number := i;
    
    Write('last_number: ');
    WriteLn(last_number);
end;

begin
    Main;
end.