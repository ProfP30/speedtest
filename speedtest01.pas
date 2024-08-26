// compile with:
// fpc speedtest01.pas -o"speedtest01_pas.bin"

program Speedtest01;

const
    END_LOOP : UInt32 = 1000000000; // 1 Mrd.
var
    last_number : UInt32 = 0;
    i : UInt32;
begin
    for i := 0 to (END_LOOP-1) do
        last_number := last_number+1;

    WriteLn('Pascal:last_number=', last_number);
    WriteLn('--');
end.